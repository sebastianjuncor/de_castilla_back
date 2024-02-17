from django.shortcuts import render

# Create your views here.
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from .models import DetallePedido
from datetime import date
from reportlab.lib.units import inch

def createHeader(canvas, doc, id_pedido):
    canvas.saveState()

    # Agregar el logo a la izquierda
    canvas.drawString(0.5 * inch, doc.height + 0.3 * inch, "Logo")

    # Agregar el título en el medio
    canvas.drawCentredString(doc.width / 2, doc.height + 0.3 * inch, "Detalles del Pedido")

    # Agregar el ID de pedido a la derecha en un recuadro
    canvas.rect(doc.width - 1.5 * inch, doc.height + 0.2 * inch, 1 * inch, 0.3 * inch)
    canvas.drawRightString(doc.width - 0.75 * inch, doc.height + 0.3 * inch, f"ID Pedido: {id_pedido}")

    # Agregar una línea horizontal debajo del encabezado
    canvas.line(0.5 * inch, doc.height + 0.15 * inch, doc.width - 0.5 * inch, doc.height + 0.15 * inch)

    canvas.restoreState()


def generate_pdf(request, id_pedido):
    # Colores personalizados
    color_oscuro = colors.HexColor('#732F48')
    color_medio = colors.HexColor('#8C274C')
    color_claro = colors.HexColor('#F26B9C')
    color_fondo1 = colors.HexColor('#F6E0E3')
    color_fondo2 = colors.HexColor('#FDEBEB')
    color_fondo3 = colors.HexColor('#FDF5E7')
    color_blanco = colors.HexColor('#ffffff')
    color_gris = colors.HexColor('#f2f2f2')

    # Obtener los detalles del pedido correspondiente desde la base de datos
    detalles_pedido = DetallePedido.objects.filter(id_pedido_fk=id_pedido)

    # Obtener la fecha actual
    today = date.today().strftime("%d/%m/%Y")

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # Define el nombre del archivo PDF
    response['Content-Disposition'] = f'attachment; filename="report_pedido_{id_pedido}.pdf"'

    # Crea un objeto SimpleDocTemplate para generar el PDF
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Crear una lista de datos para el contenido principal
    data = [
        [ "Producto", "precio", "Cantidad Producto", "Subtotal",]
    ]
    # Agregar los datos de cada detalle de pedido a la lista de datos
    for detalle in detalles_pedido:
        data.append([
            detalle.id_producto_fk.nombre_producto, 
            str(detalle.id_producto_fk.precio_producto), # Suponiendo que 'nombre_producto' es un campo en Producto
            str(detalle.cantidad_producto),
            str(detalle.subtotal_detalle_pedido),
        ])

    # Crear una tabla y definir su estilo
    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), color_oscuro),
                        ('TEXTCOLOR', (0, 0), (-1, 0), color_blanco),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), color_fondo1),
                        ('GRID', (0, 0), (-1, -1), 1, color_medio)])

    # Aplicar el estilo a la tabla
    table.setStyle(style)

    # Crear una lista de elementos Platypus para agregar al PDF
    elements = []

    # Añadir espacio para el logo
    elements.append(Spacer(1, 2 * 20))  # 2 pulgadas

    # Agregar el título
    styles = getSampleStyleSheet()
    title = Paragraph("Detalles del Pedido", styles['Title'])
    elements.append(title)

    # Definir estilo para la fecha centrada
    centered_style = ParagraphStyle(
        name='Centered',
        alignment=1,
        parent=styles['Normal']
    )

    name = Paragraph(f"{detalles_pedido[0].id_pedido_fk.no_Documento_Usuario_fk.nombre_usuario}", centered_style)
    elements.append(name)



    # Agregar la fecha
    date_paragraph = Paragraph("Fecha: " + today, centered_style)
    elements.append(date_paragraph)
    elements.append(Spacer(1, 12))  # 12 puntos de espacio

    # Agregar la tabla al contenido
    elements.append(table)

    # Generar el PDF
    doc.build(elements)

    # Devolver la respuesta con el PDF generado
    return response

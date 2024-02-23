from django.shortcuts import render

# Create your views here.
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from .models import DetallePedido
from datetime import date
from reportlab.lib.units import inch

def createHeader(canvas, doc, id_pedido):
    elements = []
    # Agregar el texto "Logo empresarial" en la esquina superior izquierda
    elements.append(Paragraph("Logo empresarial", ParagraphStyle(name='LogoStyle', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#732F48'))))

    # Agregar la fecha en la esquina superior derecha
    elements.append(Paragraph(f"{date.today().strftime('%d/%m/%Y')}", ParagraphStyle(name='DateStyle', fontName='Helvetica-Bold', fontSize=10, alignment=2)))

    # Agregar el título en el centro con el color cambiado
    elements.append(Paragraph("<br/><br/><br/>Reporte de Proveedores", ParagraphStyle(name='TitleStyle', fontName='Helvetica-Bold', fontSize=16, textColor=colors.HexColor('#8C274C'), alignment=1)))

    canvas.saveState()

    # Agregar el ID de pedido a la derecha en un recuadro
    canvas.rect(doc.width - 1.5 * inch, doc.height + 0.2 * inch, 1 * inch, 0.3 * inch)
    canvas.drawRightString(doc.width - 0.75 * inch, doc.height + 0.3 * inch, f"ID Pedido: {id_pedido}")

    canvas.restoreState()

def generate_pdf(request, id_pedido):
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
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#732F48')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#ffffff')),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F6E0E3')),
                        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#8C274C'))])

    # Aplicar el estilo a la tabla
    table.setStyle(style)

    # Crear una lista de elementos Platypus para agregar al PDF
    elements = []

    # Agregar el texto "Logo empresarial" en la esquina superior izquierda
    elements.append(Paragraph("Logo empresarial", ParagraphStyle(name='LogoStyle', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#732F48'))))

    # Agregar la fecha en la esquina superior derecha
    elements.append(Paragraph(f"{date.today().strftime('%d/%m/%Y')}", ParagraphStyle(name='DateStyle', fontName='Helvetica-Bold', fontSize=10, alignment=2)))


    # Agregar el título
    styles = getSampleStyleSheet()
    title = Paragraph("Detalles del Pedido", ParagraphStyle(name='Title', fontName='Helvetica-Bold', fontSize=16, textColor=colors.HexColor('#8C274C'), alignment=1))
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Definir estilo para la fecha centrada
    centered_style = ParagraphStyle(
        name='Centered',
        alignment=1,
        parent=styles['Normal']
    )

    elements.append(Spacer(1, 12))

    name = Paragraph(f"{detalles_pedido[0].id_pedido_fk.no_Documento_Usuario_fk.nombre_usuario}", centered_style)
    elements.append(name)

    elements.append(Spacer(1, 36))  # 12 puntos de espacio

    # Agregar la tabla al contenido
    elements.append(table)

    # Generar el PDF
    doc.build(elements)

    # Devolver la respuesta con el PDF generado
    return response

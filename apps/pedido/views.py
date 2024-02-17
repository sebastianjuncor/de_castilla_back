from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from .models import Pedido
from datetime import date

def generate_pdf(request):
    # Colores personalizados
    color_oscuro = colors.HexColor('#732F48')
    color_medio = colors.HexColor('#8C274C')
    color_claro = colors.HexColor('#F26B9C')
    color_fondo1 = colors.HexColor('#F6E0E3')
    color_fondo2 = colors.HexColor('#FDEBEB')
    color_fondo3 = colors.HexColor('#FDF5E7')
    color_blanco = colors.HexColor('#ffffff')
    color_gris = colors.HexColor('#f2f2f2')

    # Obtener todos los objetos de Pedido desde la base de datos
    pedidos = Pedido.objects.all()

    # Obtener la fecha actual
    today = date.today().strftime("%d/%m/%Y")

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # Define el nombre del archivo PDF
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Crea un objeto SimpleDocTemplate para generar el PDF
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Crear una lista de datos para el contenido principal
    data = [
        ["N° Pedido", "Descripción", "Fecha", "Estado", "Documento", "Cliente"]
    ]
    # Agregar los datos de cada pedido a la lista de datos
    for pedido in pedidos:
        data.append([
            str(pedido.id_pedido),
            pedido.descripcion_pedido,
            str(pedido.fecha_pedido),
            pedido.id_estado_pedido_fk.nombre_estado,  # Suponiendo que 'nombre_estado' es un campo en EstadoPedido
            pedido.no_Documento_Usuario_fk.no_documento_usuario, # Suponiendo que 'numero_documento' es un campo en Usuario
            pedido.no_Documento_Usuario_fk.nombre_usuario, # Suponiendo que 'nombre_usuario' es un campo en Usuario
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
    title = Paragraph("Reporte de Pedidos", styles['Title'])
    elements.append(title)

    # Definir estilo para la fecha centrada
    centered_style = ParagraphStyle(
        name='Centered',
        alignment=1,
        parent=styles['Normal']
    )

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

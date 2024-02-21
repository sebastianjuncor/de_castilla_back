from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from .models import Venta
from datetime import date
from reportlab.lib.units import inch

def createHeader(canvas, doc, id_venta):
    canvas.saveState()

    # Agregar el texto "Logo empresarial" a la izquierda
    canvas.drawString(0.5 * inch, doc.height + 0.5 * inch, "Logo empresarial")

    # Agregar la fecha de creación del documento en la esquina superior derecha
    canvas.drawString(doc.width - 2 * inch, doc.height + 0.5 * inch, f"Fecha de creación: {date.today().strftime('%d/%m/%Y')}")

    # Agregar el título en el medio
    canvas.drawCentredString(doc.width / 2, doc.height + 0.3 * inch, "Detalles de la Venta")

    # Agregar una línea horizontal debajo del encabezado
    canvas.line(0.5 * inch, doc.height + 0.25 * inch, doc.width - 0.5 * inch, doc.height + 0.25 * inch)

    canvas.restoreState()


def generate_pdf(request, id_venta):
    # Obtener los detalles de la venta correspondiente desde la base de datos
    venta = Venta.objects.get(id_venta=id_venta)

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # Define el nombre del archivo PDF
    response['Content-Disposition'] = f'attachment; filename="report_venta_{id_venta}.pdf"'

    # Crea un objeto SimpleDocTemplate para generar el PDF
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Crear una lista de datos para el contenido principal
    data = [
        [ "Número de Pedido", "ID Pedido", "Fecha Venta", "Hora Venta", "Total Venta", "Estado", "Número de Documento"]
    ]
    # Agregar los datos de la venta a la lista de datos
    data.append([
        venta.id_venta,
        venta.id_pedido_fk.id_pedido,
        venta.fecha_venta.strftime("%d/%m/%Y"), 
        venta.hora_venta.strftime("%H:%M:%S"), 
        str(venta.total_venta),
        "Activo" if venta.estado else "Inactivo",
        venta.no_documento_usuario_fk.numero_documento_usuario,
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

    # Agregar espacio para el logo y el título del documento
    elements.append(Spacer(1, 1 * inch))

    # Agregar el encabezado al contenido
    elements.append(createHeader(doc, id_venta))

    # Agregar la tabla al contenido
    elements.append(table)

    # Generar el PDF
    doc.build(elements)

    # Devolver la respuesta con el PDF generado
    return response

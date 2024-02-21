from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from .models import Proveedor
from datetime import date
from reportlab.lib.units import inch

def createHeader(canvas, doc, id_proveedor):
    canvas.saveState()

    # Agregar el texto "Logo empresarial" a la izquierda
    canvas.drawString(0.5 * inch, doc.height + 0.5 * inch, "Logo empresarial")

    # Agregar la fecha de creación del documento en la esquina superior derecha
    canvas.drawString(doc.width - 2 * inch, doc.height + 0.5 * inch, f"Fecha de creación: {date.today().strftime('%d/%m/%Y')}")

    # Agregar el título en el medio
    canvas.drawCentredString(doc.width / 2, doc.height + 0.3 * inch, "Detalles del Proveedor")

    # Agregar una línea horizontal debajo del encabezado
    canvas.line(0.5 * inch, doc.height + 0.25 * inch, doc.width - 0.5 * inch, doc.height + 0.25 * inch)

    canvas.restoreState()


def generate_pdf(request, id_proveedor):
    # Obtener los detalles del proveedor correspondiente desde la base de datos
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # Define el nombre del archivo PDF
    response['Content-Disposition'] = f'attachment; filename="report_proveedor_{id_proveedor}.pdf"'

    # Crea un objeto SimpleDocTemplate para generar el PDF
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Crear una lista de datos para el contenido principal
    data = [
        ["Empresa", "Nombre del Proveedor", "Celular", "Celular de Respaldo", "Correo Electrónico", "NIT", "Estado del Proveedor"]
    ]
    # Agregar los datos del proveedor a la lista de datos
    data.append([
        proveedor.empresa_proveedor,
        proveedor.nombre_proveedor,
        proveedor.celular_proveedor,
        proveedor.celular_respaldo_proveedor if proveedor.celular_respaldo_proveedor else "",
        proveedor.correo_proveedor,
        proveedor.nit_proveedor,
        "Activo" if proveedor.estado_proveedor else "Inactivo",
    ])

    # Crear una tabla y definir su estilo
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#732F48')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F6E0E3')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#8C274C'))
    ])

    # Aplicar el estilo a la tabla
    table.setStyle(style)

    # Crear una lista de elementos Platypus para agregar al PDF
    elements = []

    # Agregar espacio para el logo y el título del documento
    elements.append(Spacer(1, 1 * inch))

    # Agregar el encabezado al contenido
    elements.append(createHeader(doc, id_proveedor))

    # Agregar la tabla al contenido
    elements.append(table)

    # Generar el PDF
    doc.build(elements)

    # Devolver la respuesta con el PDF generado
    return response

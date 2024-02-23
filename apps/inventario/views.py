from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from .models import Inventario  # Asegúrate de que el import sea correcto y esté apuntando al modelo Inventario
from django.utils.html import escape as html_escape 
from datetime import date 

def generate_pdf(request):
    # Obtener todos los registros de inventario desde la base de datos
    inventarios = Inventario.objects.all()

    # Crear un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # Define el nombre del archivo PDF
    response['Content-Disposition'] = 'attachment; filename="reporte_inventario.pdf"'

    # Crea un objeto SimpleDocTemplate para generar el PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    
    # Crear una lista de elementos Platypus para agregar al PDF
    elements = []

    # Agregar el título en el centro
    elements.append(Paragraph("<br/><br/><br/>Reporte de inventario", ParagraphStyle(name='TitleStyle', fontName='Helvetica-Bold', fontSize=16, textColor=colors.HexColor('#8C274C'), alignment=1)))

    # Agregar espacio entre el título y la tabla
    elements.append(Spacer(1, 36))

    # Crear una lista de datos para la tabla de contenido
    data = [
        ["N°", "Stock", "Tipo", "Insumo", "Producto", "Estado"]
    ]
    # Agregar los datos de cada registro de inventario a la lista de datos
    for inventario in inventarios:
        # Asegurémonos de que los nombres de los campos y las referencias sean correctos
        insumo_nombre = inventario.id_insumo.nombre if inventario.id_insumo else ""
        producto_nombre = inventario.id_producto.nombre if inventario.id_producto else ""
        data.append([
            str(inventario.id_inventario),
            str(inventario.stock_inventario),
            html_escape(inventario.tipo_inventario),
            insumo_nombre,
            producto_nombre,
            'Activo' if inventario.estado else 'Inactivo',
        ])

    # Crear una tabla y definir su estilo
    table_style = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#732F48')),  # Color del encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#ffffff')),  # Color del texto del encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación del texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente del encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaciado inferior del encabezado
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F6E0E3')),  # Color de fondo de las filas
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#8C274C'))  # Color de las líneas de la tabla
    ]
    table = Table(data)
    table.setStyle(TableStyle(table_style))

    # Agregar la tabla a los elementos del PDF
    elements.append(table)

    # Generar el PDF
    doc.build(elements)

    # Devolver la respuesta con el PDF generado
    return response

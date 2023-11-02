from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
from django.shortcuts import render

# Configurar pdfkit para usar wkhtmltopdf
pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

def create_pdf(request):
    # Renderizar la plantilla HTML utilizando render_to_string de Django
    context = {}  # Reemplaza {} con los datos
    rendered_html = render_to_string('base.html', context)

    # Pasar el archivo CSS al PDF
    """     options = {
        'page-size': 'A5',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': "UTF-8",
        'no-outline': None,
        'disable-smart-shrinking': None,
        'quiet': ''
    } """
    options = {
        'dpi': '300',
        'page-size': 'A4',
        'encoding': "UTF-8",
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'enable-internal-links': '',
        #'footer-center': '[page] of [topage]',
        #'header-html': _path + '/web/templates/web/pdf/header.html',
        #'footer-html': _path + '/web/templates/web/pdf/footer.html',
        'page-offset': '-1',
        #'dump-outline': _path + '/web/templates/web/pdf/outline.xslt'
        'header-spacing': '4',
        'footer-spacing': '5'
    }





    css_file = 'static/styles/style.css'
    options['user-style-sheet'] = css_file

    pdf = pdfkit.from_string(rendered_html, False, configuration=pdfkit_config, options=options)

    # Crear una respuesta de Django con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cotizacion_report.pdf"'

    return response

def image(request):
    return render(request, 'report-pdf.html')
    
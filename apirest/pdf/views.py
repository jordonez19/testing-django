from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
from django.shortcuts import render, get_object_or_404
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer
import os

# Configurar pdfkit para usar wkhtmltopdf
pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

def create_pdf(request):
    # Renderizar la plantilla HTML utilizando render_to_string de Django
    context = {}  # Reemplaza {} con los datos
    rendered_html = render_to_string('test.html', context)
    _path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './templates/')

    options = {
        'dpi': '300',
        'page-size': 'A3',
        'encoding': "UTF-8",
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '1.5in',
        'margin-left': '0in',
        'enable-internal-links': '',    
        #'footer-center': '[page] of [topage]',
        'page-offset': '-1',
        #'dump-outline': _path + '/web/templates/web/pdf/outline.xslt'
        'header-html': os.path.join(_path, 'header-pdf.html'),
        'footer-html': os.path.join(_path, 'footer-pdf.html'),
        'header-spacing': '-50',
        'footer-spacing': '0'
    }

    css_file = 'static/styles/style.css'
    options['user-style-sheet'] = css_file

    pdf = pdfkit.from_string(rendered_html, False, configuration=pdfkit_config, options=options)

    # Crear una respuesta de Django con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cotizacion_report.pdf"'

    return response









#----------------------------------------------------------------------------

def image(request):
    return render(request, 'report-pdf.html')
    
#----------------------------------------------------------------------------
class CustomerListView(ListView):
    model = Customer
    template_name = 'main.html'

def customer_render_pdf_view(request, *args, **kwargs):

    PK = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=PK)

    template_path = 'pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#----------------------------------------------------------------------------

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import xlwt
from django.http import HttpResponse
from .models import AogService
from django.http import FileResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def aog_srv_pdf_report(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    # Add some lines of text
    lines = [
        "Line 1",
        "Line 2",
        "Line 3"
    ]

    # Loop
    for line in lines:
        textob.textLine(line)
    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Aog_request_order_report.pdf')


def export_invoice(request, service_id):
    # Retrieve the AogService instance
    service = AogService.objects.get(id=service_id)

    # Create a new Excel workbook
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="invoice.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Invoice')

    # Write data to the Excel file
    row_num = 0
    ws.write(row_num, 0, 'Service name')
    ws.write(row_num, 1, 'Price')
    
    row_num += 1
    ws.write(row_num, 0, service.service_name)
    ws.write(row_num, 1, service.service_name)
    
   

    # Save the workbook and return the Excel file to the user
    wb.save(response)
    return response
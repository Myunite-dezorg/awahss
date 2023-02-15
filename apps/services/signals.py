from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AogService
from apps.orders.models.aog_service_order import AogOrder
from wkhtmltopdf.views import PDFTemplateView

@receiver(post_save, sender=AogService)
def create_order(sender, instance, created, **kwargs):
    if created:
        AogOrder.objects.create(service_request=instance)

post_save.connect(create_order, sender=AogService)


# @receiver(post_save, sender=AogService)
# def generate_invoice(sender, instance, created, **kwargs):
#     if created:
#         # Use the PDFTemplateView from django-wkhtmltopdf to generate the PDF
#         pdf_view = PDFTemplateView.as_view(template_name='invoice.html', filename='invoice.pdf')
#         response = pdf_view(request=None, context={'service': instance})

#         # Save the PDF file to the AogService object
#         instance.invoice.save('invoice.pdf', response)
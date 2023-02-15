from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'apps.services'


     # add this
    def ready(self):
        import apps.services.signals

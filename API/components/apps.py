from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API.components'

    def ready(self):
        import API.components.signals
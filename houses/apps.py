from django.apps import AppConfig


class HousesConfig(AppConfig):
    # pyrefly: ignore [bad-override]
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'

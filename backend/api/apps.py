"""Приложения."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Приложение API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

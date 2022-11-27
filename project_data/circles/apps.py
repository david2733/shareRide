"""Circles app"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CirclesConfig(AppConfig):
    name = "project_data.circles"
    verbose_name = _("Circles")

    def ready(self):
        try:
            import project_data.circles.signals  # noqa F401
        except ImportError:
            pass

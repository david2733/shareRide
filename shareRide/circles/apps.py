"""Circles app"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CirclesConfig(AppConfig):
    name = "shareRide.circles"
    verbose_name = _("Circles")

    def ready(self):
        try:
            import shareRide.circles.signals  # noqa F401
        except ImportError:
            pass

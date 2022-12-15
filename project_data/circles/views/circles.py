"""Circle views."""

# Django REST framework
from rest_framework import viewsets

from project_data.circles.serializers import CircleModelSerializer

# Models
from project_data.circles.models import Circle

class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer

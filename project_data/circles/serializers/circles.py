"""Circle serializers"""

# Django Rest framework
from rest_framework import serializers

from project_data.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    class Meta:
        """Meta class."""

        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'is_public',
            'is_limited', 'members_limit',
        )

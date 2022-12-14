"""Circle views."""

# Django REST framework
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated
from shareRide.circles.serializers import CircleModelSerializer

# Models
from shareRide.circles.models import Circle, Membership

class CircleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    """Circle view set."""
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def perform_create(self, serializer):
        """Assign circle admin."""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitation=10
        )

from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# List and Create - PK Not Required
class LCSEnchroachmentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
  queryset = Enchroachment.objects.all()
  serializer_class = EnchroachmentSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['department_name', 'status_name']
  authentication_classes=[SessionAuthentication]
  permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

# Retrieve Update and Destroy(RUD) - PK Required
class RUDEnchroachmentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
  queryset = Enchroachment.objects.all()
  serializer_class = EnchroachmentSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['department_name', 'status_name']
  authentication_classes=[SessionAuthentication]
  permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

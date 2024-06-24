from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from cv_maker.serializers import ProfileSerializer
# Create your views here.


class ProfileViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    
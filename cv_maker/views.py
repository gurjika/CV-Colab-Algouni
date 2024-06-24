from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from cv_maker.models import Education, Profile
from rest_framework.response import Response
from cv_maker.serializers import EducationSerializer, ProfileSerializer
from rest_framework import status

# Create your views here.


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class EducationViewSet(ModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


    def get_serializer_context(self):
        return {'profile_pk': self.kwargs['profile_pk']}



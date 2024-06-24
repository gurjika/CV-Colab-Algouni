from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from cv_maker.models import Education, Experience, Profile
from rest_framework.response import Response
from cv_maker.serializers import EducationSerializer, ExperienceSerializer, ProfileSerializer
from rest_framework import status

# Create your views here.


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class EducationViewSet(ModelViewSet):
    serializer_class = EducationSerializer
    
    def get_queryset(self):
        return Education.objects.filter(profile_id=self.kwargs['profile_pk'])


    def get_serializer_context(self):
        return {'profile_pk': self.kwargs['profile_pk']}


class ExperienceViewSet(ModelViewSet):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(profile_id=self.kwargs['profile_pk'])


    def get_serializer_context(self):
        return {'profile_pk': self.kwargs['profile_pk']}


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework.views import APIView
from cv_maker.models import Education, Experience, Profile
from rest_framework.response import Response
from cv_maker.serializers import EducationSerializer, ExperienceSerializer, ProfileSerializer
from rest_framework import status

# Create your views here.


class ProfileViewSet(ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.prefetch_related('education').prefetch_related('experience').all()


# class EducationViewSet(ModelViewSet):
#     serializer_class = EducationSerializer
#     queryset = Education.objects.all()




# class ExperienceViewSet(ModelViewSet):
#     serializer_class = ExperienceSerializer
#     queryset = Experience.objects.all()



class DegreeChoicesAPIView(APIView):
    """
    API view to return the dictionary of degree choices available in the Education model.
    """
    def get(self, request):
        choices = dict(Education.DEGREE_CHOICES)
        return Response(choices)
from rest_framework import serializers
import phonenumbers
from cv_maker.models import Education, Experience, Profile

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'university', 'degree', 'finish_date', 'description', 'profile']



class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'employer', 'date_started', 'date_finished', 'description', 'profile']



class ProfileSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True, read_only=True)
    experience = ExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'name', 'last_name', 'image', 'about_me', 'email', 'phone_num', 'education', 'experience']



   
    
from rest_framework import serializers
import phonenumbers
from cv_maker.models import Education, Experience, Profile

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'university', 'degree', 'finish_date', 'description']



class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ['id', 'position', 'employer', 'date_started', 'date_finished', 'description']



class ProfileSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    class Meta:
        model = Profile
        fields = ['id', 'name', 'last_name', 'image', 'about_me', 'email', 'phone_num', 'education', 'experience']


    def create(self, validated_data):
        education_data = validated_data.pop('education', [])
        experience_data = validated_data.pop('experience', [])

        profile = Profile.objects.create(**validated_data)
        for edu_data in education_data:
            Education.objects.create(profile=profile, **edu_data)
        for experience in experience_data:
            Experience.objects.create(profile=profile, **experience)
        return profile



   
    
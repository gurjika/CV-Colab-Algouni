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



    def validate_phone_num(self, value):

        try:
            parsed_number = phonenumbers.parse(value, "GE")
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Invalid phone number")

        if not phonenumbers.is_valid_number(parsed_number):
            raise serializers.ValidationError("Invalid phone number")

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        return formatted_number
    
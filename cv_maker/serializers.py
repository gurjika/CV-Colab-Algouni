from rest_framework import serializers
import phonenumbers
from cv_maker.models import Education, Experience, Profile

class EducationSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Education
        fields = "__all__"

    def create(self, validated_data):
        obj = Education.objects.create(profile_id=self.context['profile_pk'], **validated_data)
        return obj

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"



    def validate_phone_num(self, value):

        try:
            parsed_number = phonenumbers.parse(value, "GE")
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Invalid phone number")

        if not phonenumbers.is_valid_number(parsed_number):
            raise serializers.ValidationError("Invalid phone number")

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        return formatted_number
    


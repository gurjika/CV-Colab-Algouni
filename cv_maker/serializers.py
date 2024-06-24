from rest_framework import serializers
import phonenumbers
from cv_maker.models import Profile


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
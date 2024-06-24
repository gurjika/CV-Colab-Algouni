from django.core.exceptions import ValidationError
import phonenumbers

def validate_redberry_email(value: str):
    if not value.endswith('@redberry.ge'):
        raise ValidationError('Email must end with @redberry.ge')
    

def validate_georgian_phone_number(value):
    try:
        phone_number = phonenumbers.parse(value, "GE")
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError("The phone number is not valid.")
    except phonenumbers.NumberParseException:
        raise ValidationError("The phone number is not valid.")
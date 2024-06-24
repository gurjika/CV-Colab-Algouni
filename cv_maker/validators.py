from django.core.exceptions import ValidationError
import phonenumbers
import re


GEORGIAN_REGEX = r'^[ა-ჰ]+$'

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
    

def validate_georgian(value):
    if not re.match(GEORGIAN_REGEX, value):
        raise ValidationError('Only Georgian Characters')
from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_redberry_email, validate_georgian_phone_number, validate_georgian

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2), validate_georgian])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2), validate_georgian])
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    about_me = models.TextField(blank=True)
    email = models.EmailField(validators=[validate_redberry_email])
    phone_num = models.CharField(max_length=255, validators=[validate_georgian_phone_number])


class Experience(models.Model):
    position = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    date_started = models.DateField()
    date_finished = models.DateField()
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')


class Education(models.Model):
    university = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    finish_date = models.DateField()
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')



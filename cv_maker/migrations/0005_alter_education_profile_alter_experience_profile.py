# Generated by Django 5.0.6 on 2024-06-24 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_maker', '0004_education_profile_experience_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='cv_maker.profile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='cv_maker.profile'),
        ),
    ]

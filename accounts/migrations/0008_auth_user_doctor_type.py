# Generated by Django 3.1.7 on 2021-04-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user',
            name='doctor_type',
            field=models.CharField(default='MBBS', max_length=64),
        ),
    ]

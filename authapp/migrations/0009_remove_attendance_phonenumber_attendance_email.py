# Generated by Django 4.1.6 on 2024-02-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_attendance_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='Phonenumber',
        ),
        migrations.AddField(
            model_name='attendance',
            name='Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(default='<django.db.models.fields.CharField>:<django.db.models.fields.CharField>:<django.db.models.fields.PositiveIntegerField>', max_length=50, null=True),
        ),
    ]

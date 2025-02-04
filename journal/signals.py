from django.contrib.auth.models import User
from .models import Student
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Student.objects.create(user=instance, first_name=instance.first_name, second_name=instance.last_name)


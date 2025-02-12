from django.contrib.auth.models import User
from .models import Student
from django.dispatch import receiver
from django.db.models.signals import post_save

# sygnal zeby stworzyc studenta jak zarejestruje sie user (User -> Student)
@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Student.objects.create(user=instance, first_name=instance.first_name, second_name=instance.last_name)

#sygnal do stworzenia usera jesli utworzy sie student (Student -> User)
@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    username = instance.first_name + instance.second_name 
    if created:
        user = User.objects.get_or_create(username=username, 
                            first_name=instance.first_name, 
                            last_name=instance.second_name)
        if not Student.objects.filter(id=instance.id, user__isnull=False).exists():
            Student.objects.filter(id=instance.id).update(user=user[0])    

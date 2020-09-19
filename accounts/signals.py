from django.db.models.signals import post_save
from .models import Member, MemberProfile
from django.dispatch import receiver


@receiver(post_save, sender=Member)
def create_profile(sender, instance, created, **kwargs):
    print("Hello1")
    if created:
        MemberProfile.objects.create(member=instance)


@receiver(post_save, sender=Member)
def save_profile(sender, instance, **kwargs):
    print("hello2")
    instance.memberprofile.save()

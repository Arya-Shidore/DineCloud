from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, userProfile

@receiver(post_save, sender=User)
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            userProfile.objects.create(user=instance)
        except Exception as e:
            raise e
    else:
        profile = userProfile.objects.filter(user=instance)
        if profile:
            profile.update(user=instance)
        else:
            userProfile.objects.create(user=instance)
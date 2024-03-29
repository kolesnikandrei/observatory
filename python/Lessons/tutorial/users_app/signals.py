# Copyright (c) 2019 Celadon Development LLC, All rights reserved.
# Author Oleg Stadnick <oleg.stadnick@celadon.ae>
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if not (instance.is_superuser or instance.is_staff) and (
            instance.is_customer
    ):
        Token.objects.get_or_create(user=instance)

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Templates(models.Model):

    #__Templates_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Templates_FIELDS__END

    class Meta:
        verbose_name        = _("Templates")
        verbose_name_plural = _("Templates")


class Executions(models.Model):

    #__Executions_FIELDS__
    template = models.CharField(max_length=255, null=True, blank=True)
    params = models.CharField(max_length=255, null=True, blank=True)

    #__Executions_FIELDS__END

    class Meta:
        verbose_name        = _("Executions")
        verbose_name_plural = _("Executions")


class Billing_Log(models.Model):

    #__Billing_Log_FIELDS__
    operation = models.CharField(max_length=255, null=True, blank=True)
    template = models.CharField(max_length=255, null=True, blank=True)

    #__Billing_Log_FIELDS__END

    class Meta:
        verbose_name        = _("Billing_Log")
        verbose_name_plural = _("Billing_Log")



#__MODELS__END

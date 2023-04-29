from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class WebsiteCredentials(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    app_name = models.CharField(_("Application Name"),max_length=255)
    password = models.CharField(_("Password"),max_length=255)
    username = models.CharField(_("Username"),max_length=255)

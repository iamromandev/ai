import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


# Create your models here.
class Tag(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""Common models file for the edi"""

import uuid
from django.db import models
from django.utils import timezone

class AbstractBaseClass(models.Model):
    """Base for all models."""
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True, auto_created=True)
    created_on = models.DateTimeField(
        db_index=True, editable=False, default=timezone.now)
    created_by = models.UUIDField(editable=False)
    updated_on = models.DateTimeField(db_index=True, default=timezone.now)
    updated_by = models.UUIDField()

    def retain_created_on_and_created_by(self):
        """Retain values for created_on and created_by fields on update."""
        try:
            initial = self.__class__.objects.get(pk=self.pk)
            self.created_on = initial.created_on
            self.created_by = initial.created_by
        except self.__class__.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        """Record today as the update date."""
        self.updated_on = timezone.now()
        self.full_clean(exclude=None)
        self.retain_created_on_and_created_by()
        super(AbstractBaseClass, self).save(*args, **kwargs)

    class Meta:
        """Initialize as meta class
        and
        order by descending dates starting with updated by.
        """

        abstract = True
        ordering = ('-updated_on', '-created_on')

class AbstractBase(AbstractBaseClass):
    """Baseclass for all models that are applicable to franchises."""

    enterprise = models.CharField(null=False, blank=False, max_length=250)

    def save(self, *args, **kwargs):
        """Override save."""
        super(AbstractBase, self).save(*args, **kwargs)
    
    class Meta:
        """Initialize it as an abstract class."""

        abstract = True


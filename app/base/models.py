from django.db import models


class BaseModel(models.Model):
    """
    Base model with timestamps behaviours

    aditional fields:
    * created: models.DateTimeField
    * updated: models.DateTimeField
    """
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel

import uuid




class Model(models.Model):
    Id = models.UUIDField(primary_key=True, db_index = True,default=uuid.uuid4, editable=False)
    
    class Meta:
        abstract = True

class CustomModel(Model,TimeStampedModel):
	class Meta:
		abstract = True
from django.db import models

from django.db import models

class Phrase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False)
    meaning = models.TextField(default="")
    priority = models.CharField(max_length=50,default="")
    reserve = models.TextField(default="")

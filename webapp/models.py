from django.db import models
from django.core.validators import int_list_validator
import datetime

class Evaluacion(models.Model):
    respuestas = models.CharField(max_length=200,validators=[int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-date']

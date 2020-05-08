from django.db import models
from .update import updatesubj1, updatesubj2, updatesubj3

class Student(models.Model) :
    name = models.CharField(max_length=30)
    subj1 = models.FloatField()
    subj2 = models.FloatField()
    subj3 = models.FloatField()
    subj1_att = models.FloatField(null=True)
    subj2_att = models.FloatField(null=True)
    subj3_att = models.FloatField(null=True)

    def _str_(self):
        return self.name

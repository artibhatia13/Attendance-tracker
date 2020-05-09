from django.db import models
from .update import updatesubj1, updatesubj2, updatesubj3

class Student(models.Model) :
    name = models.CharField(max_length=30)
    subj1 = models.FloatField()
    subj2 = models.FloatField()
    subj3 = models.FloatField()
    class_att_subj1 = models.IntegerField()
    class_att_subj2 = models.IntegerField()
    class_att_subj3 = models.IntegerField()

    def _str_(self):
        return self.name

updatesubj3([True, True, False, True, False, True, False, True, False])

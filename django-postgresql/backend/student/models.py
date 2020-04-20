from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=30)
    subj1 = models.FloatField()
    subj2 = models.FloatField()
    subj3 = models.FloatField()

    def _str_(self):
        return self.name

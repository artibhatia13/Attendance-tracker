from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=30)
    subj1 = models.DecimalField(max_digits=5, decimal_places=2)
    subj2 = models.DecimalField(max_digits=5, decimal_places=2)
    subj3 = models.DecimalField(max_digits=5, decimal_places=2)
    class_att_subj1 = models.FloatField(default=0)
    class_att_subj2 = models.FloatField(default=0)
    class_att_subj3 = models.FloatField(default=0)
    total_class_taken = models.IntegerField(default=0)

    def _str_(self):
        return self.name




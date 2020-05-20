from student.models import Student
from django.db.models import F

def updatesubj1(name):
    classAttended = Student.objects.get(name=name)
    x = classAttended.class_att_subj1
    classAttended.class_att_subj1 = F('class_att_subj1')+1
    classAttended.save(update_fields=['class_att_subj1'])

    classTaken = Student.objects.get(id=1)
    y = classTaken.total_class_taken
    classTaken.total_class_taken =  F('total_class_taken')+1
    classTaken.save(update_fields=['total_class_taken'])
 
    x+=1
    y+=1
    new_att = (x/y)*100

    Student.objects.filter(name=name).update( subj1 = new_att)

def updatesubj2(name):    
    classAttended = Student.objects.get(name=name)
    x = classAttended.class_att_subj2
    classAttended.class_att_subj2 = F('class_att_subj2')+1
    classAttended.save(update_fields=['class_att_subj2'])

    classTaken = Student.objects.get(id=2)
    y = classTaken.total_class_taken
    classTaken.total_class_taken =  F('total_class_taken')+1
    classTaken.save(update_fields=['total_class_taken'])
    
    x+=1
    y+=1
    new_att = (x/y)*100

    Student.objects.filter(name=name).update( subj2 = new_att)


def updatesubj3(name):
    classAttended = Student.objects.get(name=name)
    x = classAttended.class_att_subj3
    classAttended.class_att_subj3 = F('class_att_subj3')+1
    classAttended.save(update_fields=['class_att_subj3'])

    classTaken = Student.objects.get(id=3)
    y = classTaken.total_class_taken
    classTaken.total_class_taken =  F('total_class_taken')+1
    classTaken.save(update_fields=['total_class_taken'])

    x+=1
    y+=1
    new_att = (x+1/y+1)*100

    Student.objects.filter(name=name).update( subj3 = new_att)
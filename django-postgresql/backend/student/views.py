from django.shortcuts import render
from .models import Student
from .update import updatesubj1, updatesubj2, updatesubj3

import numpy as np
import cv2
import pickle

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    return render(request, 'index.html')

def webcam(request):
    a=0    
    face_cascade = cv2.CascadeClassifier(BASE_DIR +'/ml/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(BASE_DIR +"/ml/trainner.yml")

    labels = {"person_name" : 1}
    with open(BASE_DIR +"/ml/labels.pickle",  'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            #print(x, y, w, h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf>=36: #and conf<=65:
                print(id_)
                print(labels[id_])                 
                if a==0 :
                    updatesubj2(3)                
                    a=1

                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            else:
                cv2.putText(frame, 'unknown', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            img_item = "4.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'webcam.html')

def attendance(request):
    allStudent = Student.objects.order_by('id')
    context = {'allStudent':allStudent}

    return render(request, 'attendance.html', context)

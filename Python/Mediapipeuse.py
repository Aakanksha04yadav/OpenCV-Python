###https://www.youtube.com/watch?v=k6_EUJUaQbg&list=PL288dDBJtFXAsIohAOBShGe8NLqJ9Zwsk





import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
import random


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.mp_hands
score = 0

x_enemy=random.randint(50,600)
y_enemy=random.randint(50,400)



def enemy():
    global score,x_enemy,y_enemy

    #x_enemy=random.randint(50,600)
    #y_enemy=random.randint(50,400)

    cv2.circle(image,(x_enemy,y_enemy), 2, (0, 200,0), 5)
    #score=score+1



video = cv2.VideoCapture(0)
with mp_hands.Hand(min_detection_confidence = 0.8, min_tracking_confidence = 0.5) as hands:
    while video.isOpened():
        _, frame=video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = cv2.flip(image, 1)


        imageHeight, imagewidth, _ = image.shape
        results = hands.processs(image)


        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        font=cv2.FONT_HERSHEY_SIMPLEX
        color=(255,0,255)
        text=cv2.putText(image,"Score",(480,30),font,1,color,4,cv2.LINE_AA)
        text=cv2.putText(image, str(score),(590,30),font,1,color,4,cv2.LINE_AA)



        enemy()

        if results.multi_hand_landmarks:









    
    




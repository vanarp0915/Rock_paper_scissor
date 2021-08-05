from keras.models import load_model
import cv2
import numpy as np
import sys

__author__      = "Vanarp0915"

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}
model = load_model("rock_paper_scissor.h5")

def mapper(val):
    return REV_CLASS_MAP[val]

cap = cv2.VideoCapture(0)

def game(user_move_name):
    if user_move_name == "rock":
        img="images/paper.png"
    elif user_move_name == "paper":
        img="images/scissors.png"
    elif user_move_name == "scissors":
        img= "images/rock.png"
    else:
        img= False
    return img

while (True):
    ret, frame = cap.read()
    cv2.putText(frame, "Me", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.rectangle(frame, (5,5), (245,245), (255,255,0), 2)
    cv2.putText(frame, "Computer", (345, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.rectangle(frame, (345,5), (585,245), (255,255,0), 2)
    cropped = frame[5:245, 5:245]
    cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    cropped= cv2.resize(cropped, (227, 227))
    pred = model.predict(np.array([cropped]))
    move_code = np.argmax(pred[0])
    user_move_name = (mapper(move_code))
    print(user_move_name)
    if user_move_name != "none":
        img=game(user_move_name)
        img=str(img)
        img=cv2.imread(img)
        img=cv2.resize(img,(240,240))
        frame[5:245, 345:585]=img
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


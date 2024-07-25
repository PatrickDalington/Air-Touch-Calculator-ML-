
import cv2
from cvzone.HandTrackingModule import HandDetector
from gtts import gTTS
import os
from playsound import playsound
import threading
import queue

speech_queue = queue.Queue()
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("afplay output.mp3 -r 1.4", )  # Play the generated audio file on macOS
    speech_queue.put()




class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, image):
        cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225),
                      cv2.FILLED)
        cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)

        cv2.putText(image, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255),
                          cv2.FILLED)

            cv2.putText(image, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 0, 0), 5)

            return True
        else:
            return False


# Webcam
cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating calculator buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', 'C', '=']]

buttonList = []
for x in range(4):
    for y in range(4):
        xPos = x * 100 + 800
        yPos = y * 100 + 150
        buttonList.append(Button((xPos, yPos), 100, 100, buttonListValues[y][x]))

# Calculation
myCal = ''
delayCount = 0
isInvalidEnding = False

# Loop
while True:
    # Get image from came

    success, image = cap.read()

    # Flip the image for easy manipulation
    image = cv2.flip(image, 1)

    # Dectate Hands
    hands, image = detector.findHands(image, flipType=False)

    # Drawing all necessary buttons with the edittext box for displaying result
    cv2.rectangle(image, (800, 50), (800 + 400, 70 + 100), (225, 225, 225),
                  cv2.FILLED)
    cv2.rectangle(image, (800, 50), (800 + 400, 70 + 100), (50, 50, 50), 3)

    for button in buttonList:
        button.draw(image)

    # Check for hand
    if hands:
        lmList = hands[0]['lmList']
        length, _, image = detector.findDistance(lmList[8][0:2], lmList[12][0:2], image)

        x, y = lmList[8][0:2]
        if length < 50:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y) and delayCount == 0:
                    val = buttonListValues[int(i % 4)][int(i / 4)]
                    if val == "=":
                        if myCal[-1] == '+':
                            isInvalidEnding = True
                        elif myCal[-1] == '-':
                            isInvalidEnding = True
                        elif myCal[-1] == '*':
                            isInvalidEnding = True
                        elif myCal[-1] == '/':
                            isInvalidEnding = True
                        else:
                            isInvalidEnding = False
                            myCal = str(eval(myCal))
                    elif val == "C":
                        if len(myCal) == 0:
                            myCal = ''
                        else:
                            myCal = myCal.rstrip(myCal[-1])
                    else:
                        myCal += val
                        #text_to_speech(val)


                    delayCount = 1

    # Avoiding duplicated number
    if delayCount != 0:
        delayCount += 1
        if delayCount > 10:
            delayCount = 0

    if isInvalidEnding:
        cv2.putText(image, "Complete equation", (800 + 10, 100 + 40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    else:
        cv2.putText(image, "", (800 + 10, 100 + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

    # Display the result
    cv2.putText(image, myCal, (800 + 10, 100 + 20), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # Drawing a rectangle button using cv2

    # Display image
    cv2.imshow("Calculator", image)
    key = cv2.waitKey(1)

    if key == ord('c'):
        myCal = ''

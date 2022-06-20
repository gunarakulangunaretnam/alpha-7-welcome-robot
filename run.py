import cv2
import numpy as np
import pyttsx3
import time
import speech_recognition as sr
from gtts import gTTS
import os
import soundfile as sf
import time
from datetime import datetime, date
from time import gmtime, strftime
import random
import imutils
from pygame import mixer  # Load the required library

# Gender and age prediction <start>
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
gender_list = ['Male', 'Female']

print('Model is loading....')

age_net = cv2.dnn.readNetFromCaffe("0-system-assets/0-models/deploy-age.prototxt", "0-system-assets/0-models/age-net.caffemodel")

gender_net = cv2.dnn.readNetFromCaffe("0-system-assets/0-models/deploy-gender.prototxt", "0-system-assets/0-models/gender-net.caffemodel")



weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

currentDate = datetime.date(datetime.now())
dayNumber = currentDate.weekday()
DayAsString = weekDays[dayNumber]
today = date.today()

# Find Weekday </end>


# Find greating method <start>

now = datetime.now()

current_hour = now.strftime("%H")

current_hour = int(current_hour)

greatingMessgeTime = ""

if current_hour >= 0 and current_hour < 12:

    greatingMessgeTime = "Good Morning"

elif current_hour >= 12 and current_hour < 18:

    greatingMessgeTime = "Good Afternoon"

elif current_hour >= 18 and current_hour != 0:

    greatingMessgeTime = "Good Evening"

# Find greating method </end>


# Voice Settings <start>

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"  # female
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"  # male

engine.setProperty('voice', en_voice_id)

mixer.init()
mixer.music.load('0-system-assets/1-sound-effects/sound-1.mp3')
mixer.music.play()
time.sleep(2)

mixer.init()
mixer.music.load('0-system-assets/1-sound-effects/sound-2.mp3')
mixer.music.play()

time.sleep(3)


engine.say('''Hello, {}. Alpha 7 is starting.'''.format(greatingMessgeTime))

currentTime = strftime("%H:%M:%S")
d = datetime.strptime(str(currentTime), "%H:%M:%S")

currentTime = d.strftime("%I %M %p")

engine.say(
    "Today is {},. The date is {}. and the time is {}".format(
        DayAsString, today, currentTime))

engine.say("I am online")

engine.runAndWait()

# Voice Settings </end>


# Face Detection <start>

faceDetect = cv2.CascadeClassifier("0-system-assets/0-models/haarcascade-frontalface-alt.xml")
cam = cv2.VideoCapture(0)

facesCount = 0  # delay time to predict the face.

# Face Detection </end>


# Font Settings <start>

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 22)
fontScale = 0.6
fontColor = (139, 28, 237)
lineType = 2

font2 = cv2.FONT_HERSHEY_SIMPLEX
fontScale2 = 0.6
fontColor2 = (255, 0, 0)
lineType2 = 2

# Font Settings </end>


greatingSentances = [

    'Hello {}. Wecome to the british college of applied studies exhibition. Have a nice day'.format(greatingMessgeTime),
    'Hi, {}. I hope you are doing well, Welcome to the exhibition'.format(greatingMessgeTime),
    'Hey {}. wow you are looking very smart today. I believe that you would enjoy our exhibition much.'.format(
        greatingMessgeTime),
    'Hey, beautiful. you are warmly welcomed. And you dressing style is pretty awesome',
    'hi. Come in. It’s really nice to see you. There are lots of technological related things that you can learn today.',
    'Hey, {}. It’s a pleasure to meet you, I welcome you to enjoy our exhibition. I hope you would definitely like it'.format(
        greatingMessgeTime),
    'Hey,{}. you are looking much adorable. You are cheerfully welcomed. I hope you find it as a good day.'.format(
        greatingMessgeTime),
    '{}. Welcome to our campus. You can learn a tremendous amount of skills today. '.format(greatingMessgeTime),
    'You are welcome and {}. I think you will find something new today.'.format(greatingMessgeTime),
    'Hello, {}. You are welcomed. '.format(greatingMessgeTime),
    '{}. There is no words to welcome you. Because, you are such an adorable person'.format(greatingMessgeTime),
    '{}. I like your dressing style. Have a nice day. Welcome to the exhibition'.format(greatingMessgeTime),
    '{}. Welcome to the campus, You are looking awesome. I love you'.format(greatingMessgeTime),
    'Hello, {}. I welcome you from the bottom of my heart. Today’s going to be a great day for you.',
    'Hi, {}. I’m very excited to welcome you. Have a nice day. And i want to tell you something that you are looking very smart'.format(
        greatingMessgeTime),
    'Hey, Hello {}. You are an awesome person. I wish you all the success today and always.'.format(greatingMessgeTime),
    'Hi dear {}. Have fun day and learn lots. All the best for a bright future.'.format(greatingMessgeTime),
    'Hello beautiful {}. You are strong and smart. I give a pleasurable welcome for you buddy.'.format(
        greatingMessgeTime),
    'Hi dear {}. I wish that you find today as a rock n’ roll day in your life. Make sure to learn something from today.'.format(
        greatingMessgeTime),
    'Hi buddy {}. you are warmly welcomed and Enjoy your wonderful day.'.format(greatingMessgeTime),
    'Hello, {}. you look much beautiful. you are kindly welcomed and have a Cheerful day'.format(greatingMessgeTime),
    'Hi dear, {}. Wecome to the british college of applied studies exhibition. Have an enjoyable day'.format(
        greatingMessgeTime),
    'Hello friend {}, Wishing you a pleasant day. Here is wishing you good luck for a bright and prosperous future.'.format(
        greatingMessgeTime),
    'Hi generous, {} you are warmly welcomed and I Hope you have a pleasureable day.'.format(greatingMessgeTime),
    'Hello, {}. you are kindly welcomed and have a fun-filled {}'.format(greatingMessgeTime, DayAsString),
    'hi {}. I give a kindly welcome for you and I hope you have delightful moments today.'.format(greatingMessgeTime),
    "hello beautiful, {}. Wishing you the best of day - today and you are welcomed".format(greatingMessgeTime),
    "hi, buddy {}. May your day be Joyful. ".format(greatingMessgeTime),
    "hello, {}. you are warmly welcomed and Have a blessed day.".format(greatingMessgeTime),
    'Hello adorable, {}. I hope that you would find today as a Happy {}.'.format(greatingMessgeTime, DayAsString),
    'hey, interesting person, {}. I hope that You’re gonna rock it today.'.format(greatingMessgeTime),
    'WoW, you are looking very awesome. {}. you are kindly welcomed and i hope that you make it a good day'.format(
        greatingMessgeTime),
    'Hi dear. {}. I find my heart singing a chorus at your happy face and i can say Good luck to you during this joyous time'.format(
        greatingMessgeTime),
    'Hello dear. {}. Keep your best wishes, close to your heart and watch what happens'.format(greatingMessgeTime),
    'Hi {}. and welcome. Good luck and tons of best wishes. allah bless you in whatever you do. This is my heartiest wish just for you'.format(
        greatingMessgeTime),
    'Hey, {}. Here’s wishing you success in everything you do. Good luck.'.format(greatingMessgeTime),
    'Hi, {}. It’s kind of fun to do the impossible. All the best.'.format(greatingMessgeTime),
    'Hey, {}. Try a little harder to be a little better. All the best.'.format(greatingMessgeTime),
    'Hi{}. My heart is filled with joy at the sound of good to welcome you . Best of luck to you dear friend'.format(
        greatingMessgeTime),
    'Hello my dear. {}. i am excited see you with this happy face. You are cheerfully welcomed.'.format(
        greatingMessgeTime),
    'Hey buddy. {}. Welcome to the british college of applied studies exhibition. I wish you all the success, happiness, and joy in life.'.format(
        greatingMessgeTime),
    'Hey, beautiful. {}. you are welcomed. i would like to tell you something for you. Luck is yours wishes are mine. Let your future always shine'.format(
        greatingMessgeTime),
    'Hey buddy. {}. I welcome you from my heart. I Hope your burdens are feeling lighter, and each day is a little bit brighter.'.format(
        greatingMessgeTime),
    'Hello, {}. and you are welcomed. My good wishes are always with you. Go for it.'.format(greatingMessgeTime),
    'Hello, {}. I welcome you with the happy mind. You look smart.'.format(greatingMessgeTime),
    'hi, {}.  you are welcomed. Good Luck. I Hope you enjoy this {}.'.format(greatingMessgeTime, DayAsString),
    'Hey smart person. {}. you are cheerfully welcomed. The best time for new beginnings is now. All the best.'.format(
        greatingMessgeTime),
    'hello, {}. you are kindly welcomed and.  If I have to wish you something, I would have to say have a very nice day'.format(
        greatingMessgeTime),
    'Hai, {}. I welcome on this beautiful {}. Here are best wishes that your profession brings satisfaction'.format(
        greatingMessgeTime, DayAsString),
    "Hey, beautiful {}. You are welcomed. and i would like to tell you something. Go confidently in the direction of your dreams. Live the life you have imagined".format(
        greatingMessgeTime)

]

while (True):

    ret, img = cam.read()
    img2 = img.copy()
    img3 = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if facesCount == 10:
            currentTime = strftime("%H:%M:%S")
            d = datetime.strptime(str(currentTime), "%H:%M:%S")

            currentTime = d.strftime("%I:%M:%S:%p")

            cv2.putText(img, currentTime, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

            cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_img = img3[y:y + h, x:x + w].copy()

            blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # Predicting gender
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = gender_list[gender_preds[0].argmax()]

            if gender == "Female":

                engine.setProperty('voice', en_voice_id)
                questionChoice = random.randint(0, len(greatingSentances) - 1)
                engine.say(greatingSentances[questionChoice])
                engine.runAndWait()

            elif gender == "Male":

                engine.setProperty('voice', ru_voice_id)
                questionChoice = random.randint(0, len(greatingSentances) - 1)
                engine.say(greatingSentances[questionChoice])
                engine.runAndWait()


            # Predict age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = age_list[age_preds[0].argmax()]

            overlay_text = "%s, %s" % (gender, age)

            cv2.putText(img3, overlay_text, (x, y - 6), font2, fontScale2, fontColor2, lineType2)

            cv2.putText(img3, currentTime, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

            path, dirs, files = next(os.walk("1-system-output-data/3-photos-with-gender-and-age-prediction"))
            file_count = len(files)
            cv2.imwrite("1-system-output-data/3-photos-with-gender-and-age-prediction/image-{}.jpg".format(file_count), img3)

            path, dirs, files = next(os.walk("1-system-output-data/2-photos-with-bounding-boxes"))
            file_count = len(files)
            cv2.imwrite("1-system-output-data/2-photos-with-bounding-boxes/image-{}.jpg".format(file_count), img)

            cv2.putText(img2, currentTime, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

            path, dirs, files = next(os.walk("1-system-output-data/1-full-photos/"))
            file_count = len(files)
            cv2.imwrite("1-system-output-data/1-full-photos/image-{}.jpg".format(file_count), img2)

            face = img[y:y + h, x:x + w]

            path, dirs, files = next(os.walk("1-system-output-data/0-cropped-faces-photos"))
            file_count = len(files)
            cv2.imwrite("1-system-output-data/0-cropped-faces-photos/image-{}.jpg".format(file_count), face)

            facesCount = 0

        facesCount = facesCount + 1

    cv2.imshow("Display", img)
    if (cv2.waitKey(1) == ord('q')):
        break

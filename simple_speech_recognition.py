"""Written by Caleb Mathurin.
   October 8, 2024 - October 19, 2024.
   Written in Python 3.12 with SpeechRecognition 3.10.4, PyAudio 0.2.14 and PyAutoGUI 0.9.54 through
   Pycharm Community Edition 2024.1.1.
   This is code that takes in audio from a microphone to convert it into text. I made it because it's annoying to move
   my hand to follow along in slideshows during class when I'm sitting comfortably."""

#CM 10/8/24-10/19/24 - imports
import speech_recognition as sr
import pyaudio
import pyautogui

#CM 10/8/24 - speech_recognition objects
recognizer = sr.Recognizer()
mic = sr.Microphone()

#CM 10/8/24-10/19/24 - variables
recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True

#CM 10/19/24 - adjust for ambient noise
with mic as source:
    recognizer.adjust_for_ambient_noise(source)

#CM 10/8/24-10/19/24 - infinite while loop for listening
print("Say \'back\' to trigger a left arrow input and \'advance\' to trigger a right arrow input.")
print("It's great for slideshows!")
print("Listening..." + "\n")
while True:
    #CM 10/8/24-10/19/24 - try audio recognition and text to speech
    try:
        with mic as source:
            print("Say something...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        if "back" in text:
            pyautogui.press('left')
            print("[INPUTTING LEFT ARROW KEY]")
        if "advance" in text:
            pyautogui.press('right')
            print("[INPUTTING RIGHT ARROW KEY]")
        print()  # print blank line if both keywords are said

    #CM 10/8/24 - except if speech is unrecognizable
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio." + "\n")

    #CM 10/8/24 - except end
    except KeyboardInterrupt:
        print("Exiting...")
        break




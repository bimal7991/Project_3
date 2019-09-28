import RPi.GPIO as GPIO
import pygame
from gtts import gTTS
import os
import time
import speech_recognition as sr
import pyttsx
import threading
from threading import Thread
import multiprocessing
import pyaudio
# import pocketsphinx

from multiprocessing import Process


def system1():
    try:

        # a=1
        # voiceEngine = pyttsx.init()

        # rate = voiceEngine.getProperty('rate')
        # volume = voiceEngine.getProperty('volume')
        # voice = voiceEngine.getProperty('voice')

        # voiceEngine.setProperty('rate', 140)
        # voiceEngine.setProperty('voice', voice.id)
        # voiceEngine.say(' What kind of information would you like?')
        # voiceEngine.say('Say 1 for detailed information and 2 for a brief overview')
        # voiceEngine.say('you can also interrupt by saying 1 to repeat and 2 to stop and move on to the next system')
        # voiceEngine.runAndWait()
        # time.sleep(10)
        engine = pyttsx.init()
        sound = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', .5)
        engine.say("say 1 for male and 2 for female")
        time.sleep(5)
        engine.runAndWait()
        print("say 1 for male and 2 for female")
        r = sr.Recognizer()
        print("1")
        with sr.Microphone() as source:
            print("2")
            energy_threshold = 3000
            print("3")
            # time.sleep(5)
            audio = r.listen(source)
            print("44")
            worda = r.recognize_google(audio)
            print(worda)
            print("5")
            if worda == '1':
                print("you chosed male voice")
            if worda == '2':
                print("you chosed female voice")

            if worda == '1':
                engine = pyttsx.init()
                sound = engine.getProperty('voices')
                rate = engine.getProperty('rate')
                volume = engine.getProperty('volume')
                engine.setProperty('rate', 100)
                engine.setProperty('volume', .5)
                engine.say(
                    "What kind of information would you like to have, say one for detailed information and two for a brief  information overview.One for replay and two for stop and move on to the next system")
                time.sleep(15)
                engine.runAndWait()
                print('0')

                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    time.sleep(12)
                    audio = r.listen(source)
                    print("44")
                    worde = r.recognize_google(audio)
                    print(worde)
                    print("5")
                    # print(worda)
                    if worde == '1':
                        print("you said detail")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say(
                            "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")
                        time.sleep(20)
                        engine.runAndWait()
                        r = sr.Recognizer()
                        print("1")
                        with sr.Microphone() as source:
                            print("2")
                            energy_threshold = 3000
                            print("3")
                            time.sleep(15)
                            audio = r.listen(source)
                            print("44")
                            word = r.recognize_google(audio)
                            print(word)
                            if word == '1':
                                print("you said detail")
                                engine = pyttsx.init()
                                sound = engine.getProperty('voices')
                                rate = engine.getProperty('rate')
                                engine.setProperty('rate', 50)
                                engine.say(
                                    "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")  # give more and more importance.becoming key certain for survival of developing,manufacturing companies.digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers the complete digital representation of the entire physical value change is our ultimate goal.we call solution platform which we created for this purpose digital enterprice.kindly move on to the next system")
                                time.sleep(20)
                            if word == '2' or 'to':
                                stop1d()

                    if worde == '2' or 'to':
                        print("you said brief")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say('Bye bye.Kindly move on to the next system')
                        time.sleep(20)
                        engine.runAndWait()
                # time.sleep(10)
                # time.sleep(55)

            if worda == '2' or 'to':
                print('You chose female voice')
                pygame.mixer.init()
                pygame.mixer.music.load("intro.mp3")
                pygame.mixer.music.play()
                time.sleep(15)
                print('0')
                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    # time.sleep(5)
                    audio = r.listen(source)
                    print("4")
                    wordb = r.recognize_google(audio)
                    print(wordb)
                    print("5")
                    if wordb == '1':
                        print("you said detail")
                        pygame.mixer.init()
                        pygame.mixer.music.load("detail.mp3")
                        pygame.mixer.music.play()
                        time.sleep(55)
                        interactive1d()
                        # while(a==1)

                    if wordb == '2' or 'to':
                        print("you said brief")
                        pygame.mixer.init()
                        pygame.mixer.music.load("brief.mp3")
                        pygame.mixer.music.play()

                # time.sleep(55)
                def repeat1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    pygame.mixer.init()
                    pygame.mixer.music.load("detail.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(55)

                def stop1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1d():
                    a = 1
                    while (a == 1):

                        try:
                            audio = r.listen(source)
                            word1 = r.recognize_google(audio)
                            print(word1)
                            if word1 == '1':
                                repeat1d()

                            if word1 == '2':
                                a = 0
                                stop1d()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1d()
                    print('it stopped')
                print('End of Sys')

                def stop1b():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1b():
                    a1 = 1
                    while (a1 == 1):

                        try:
                            audio = r.listen(source)
                            word2 = r.recognize_google(audio)
                            print(word2)
                            if word2 == '1':
                                repeat1b()

                            if word2 == '2':
                                a1 = 0
                                stop1b()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1b()
                    print('it stopped')
                print('End of Sys')


    except Exception as e:
        print
        e
        print('exception1')
        system1()


def system2():
    try:
        engine = pyttsx.init()
        sound = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', .5)
        engine.say("say 1 for male and 2 for female")
        time.sleep(5)
        engine.runAndWait()
        print("say 1 for male and 2 for female")
        r = sr.Recognizer()
        print("1")
        with sr.Microphone() as source:
            print("2")
            energy_threshold = 3000
            print("3")
            # time.sleep(5)
            audio = r.listen(source)
            print("44")
            worda = r.recognize_google(audio)
            print(worda)
            print("5")
            if worda == '1':
                print("you chosed male voice")
            if worda == '2':
                print("you chosed female voice")

            if worda == '1':
                engine = pyttsx.init()
                sound = engine.getProperty('voices')
                rate = engine.getProperty('rate')
                volume = engine.getProperty('volume')
                engine.setProperty('rate', 100)
                engine.setProperty('volume', .5)
                engine.say(
                    "What kind of information would you like to Say, one for detailed information and two for a brief  information overview.One for replay and two for stop and move on to the next system")
                time.sleep(15)
                engine.runAndWait()
                print('0')

                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    time.sleep(12)
                    audio = r.listen(source)
                    print("44")
                    worde = r.recognize_google(audio)
                    print(worde)
                    print("5")
                    # print(worda)
                    if worde == '1':
                        print("you said detail")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say(
                            "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")
                        time.sleep(30)
                        engine.runAndWait()
                        r = sr.Recognizer()
                        print("1")
                        with sr.Microphone() as source:
                            print("2")
                            energy_threshold = 3000
                            print("3")
                            time.sleep(15)
                            audio = r.listen(source)
                            print("44")
                            word = r.recognize_google(audio)
                            print(word)
                            if word == '1':
                                print("you said detail")
                                engine = pyttsx.init()
                                sound = engine.getProperty('voices')
                                rate = engine.getProperty('rate')
                                engine.setProperty('rate', 50)
                                engine.say(
                                    "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")  # give more and more importance.becoming key certain for survival of developing,manufacturing companies.digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers the complete digital representation of the entire physical value change is our ultimate goal.we call solution platform which we created for this purpose digital enterprice.kindly move on to the next system")
                                time.sleep(20)
                            if word == '2' or 'to':
                                stop1d()

                    if worde == '2' or 'to':
                        print("you said brief")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say('Bye bye.Kindly move on to the next system')
                        time.sleep(20)
                        engine.runAndWait()
                # time.sleep(10)
                # time.sleep(55)

            if worda == '2' or 'to':
                print('You chose female voice')
                pygame.mixer.init()
                pygame.mixer.music.load("intro.mp3")
                pygame.mixer.music.play()
                time.sleep(15)
                print('0')
                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    # time.sleep(5)
                    audio = r.listen(source)
                    print("4")
                    wordb = r.recognize_google(audio)
                    print(wordb)
                    print("5")
                    if wordb == '1':
                        print("you said detail")
                        pygame.mixer.init()
                        pygame.mixer.music.load("detail.mp3")
                        pygame.mixer.music.play()
                        time.sleep(55)
                        interactive1d()
                        # while(a==1)

                    if wordb == '2' or 'to':
                        print("you said brief")
                        pygame.mixer.init()
                        pygame.mixer.music.load("brief.mp3")
                        pygame.mixer.music.play()

                # time.sleep(55)
                def repeat1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    pygame.mixer.init()
                    pygame.mixer.music.load("detail.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(55)

                def stop1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1d():
                    a = 1
                    while (a == 1):

                        try:
                            audio = r.listen(source)
                            word1 = r.recognize_google(audio)
                            print(word1)
                            if word1 == '1':
                                repeat1d()

                            if word1 == '2':
                                a = 0
                                stop1d()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1d()
                    print('it stopped')
                print('End of Sys')

                def stop1b():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1b():
                    a1 = 1
                    while (a1 == 1):

                        try:
                            audio = r.listen(source)
                            word2 = r.recognize_google(audio)
                            print(word2)
                            if word2 == '1':
                                repeat1b()

                            if word2 == '2':
                                a1 = 0
                                stop1b()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1b()
                    print('it stopped')
                print('End of Sys')


    except Exception as e:
        print
        e
        print('exception1')
        system2()


def system3():
    try:

        engine = pyttsx.init()
        sound = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', .5)
        engine.say("say 1 for male and 2 for female")
        time.sleep(5)
        engine.runAndWait()
        print("say 1 for male and 2 for female")
        r = sr.Recognizer()
        print("1")
        with sr.Microphone() as source:
            print("2")
            energy_threshold = 3000
            print("3")
            # time.sleep(5)
            audio = r.listen(source)
            print("44")
            worda = r.recognize_google(audio)
            print(worda)
            print("5")
            if worda == '1':
                print("you chosed male voice")
            if worda == '2':
                print("you chosed female voice")

            if worda == '1':
                engine = pyttsx.init()
                sound = engine.getProperty('voices')
                rate = engine.getProperty('rate')
                volume = engine.getProperty('volume')
                engine.setProperty('rate', 100)
                engine.setProperty('volume', .5)
                engine.say(
                    "What kind of information would you like to Say, one for detailed information and two for a brief  information overview.One for replay and two for stop and move on to the next system")
                time.sleep(5)
                engine.runAndWait()
                print('0')

                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    time.sleep(12)
                    audio = r.listen(source)
                    print("44")
                    worde = r.recognize_google(audio)
                    print(worde)
                    print("5")
                    # print(worda)
                    if worde == '1':
                        print("you said detail")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say(
                            "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")
                        time.sleep(20)
                        engine.runAndWait()
                        r = sr.Recognizer()
                        print("1")
                        with sr.Microphone() as source:
                            print("2")
                            energy_threshold = 3000
                            print("3")
                            time.sleep(15)
                            audio = r.listen(source)
                            print("44")
                            word = r.recognize_google(audio)
                            print(word)
                            if word == '1':
                                print("you said detail")
                                engine = pyttsx.init()
                                sound = engine.getProperty('voices')
                                rate = engine.getProperty('rate')
                                engine.setProperty('rate', 50)
                                engine.say(
                                    "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")  # give more and more importance.becoming key certain for survival of developing,manufacturing companies.digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers the complete digital representation of the entire physical value change is our ultimate goal.we call solution platform which we created for this purpose digital enterprice.kindly move on to the next system")
                                time.sleep(20)
                            if word == '2' or 'to':
                                stop1d()

                    if worde == '2' or 'to':
                        print("you said brief")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say('Bye bye.Kindly move on to the next system')
                        time.sleep(20)
                        engine.runAndWait()
                # time.sleep(10)
                # time.sleep(55)

            if worda == '2' or 'to':
                print('You chose female voice')
                pygame.mixer.init()
                pygame.mixer.music.load("intro.mp3")
                pygame.mixer.music.play()
                time.sleep(15)
                print('0')
                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    # time.sleep(5)
                    audio = r.listen(source)
                    print("4")
                    wordb = r.recognize_google(audio)
                    print(wordb)
                    print("5")
                    if wordb == '1':
                        print("you said detail")
                        pygame.mixer.init()
                        pygame.mixer.music.load("detail.mp3")
                        pygame.mixer.music.play()
                        time.sleep(55)
                        interactive1d()
                        # while(a==1)

                    if wordb == '2' or 'to':
                        print("you said brief")
                        pygame.mixer.init()
                        pygame.mixer.music.load("brief.mp3")
                        pygame.mixer.music.play()

                # time.sleep(55)
                def repeat1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    pygame.mixer.init()
                    pygame.mixer.music.load("detail.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(55)

                def stop1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1d():
                    a = 1
                    while (a == 1):

                        try:
                            audio = r.listen(source)
                            word1 = r.recognize_google(audio)
                            print(word1)
                            if word1 == '1':
                                repeat1d()

                            if word1 == '2':
                                a = 0
                                stop1d()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1d()
                    print('it stopped')
                print('End of Sys')

                def stop1b():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1b():
                    a1 = 1
                    while (a1 == 1):

                        try:
                            audio = r.listen(source)
                            word2 = r.recognize_google(audio)
                            print(word2)
                            if word2 == '1':
                                repeat1b()

                            if word2 == '2':
                                a1 = 0
                                stop1b()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1b()
                    print('it stopped')
                print('End of Sys')


    except Exception as e:
        print
        e
        print('exception1')
        system3()


def system4():
    try:

        engine = pyttsx.init()
        sound = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', .5)
        engine.say("say 1 for male and 2 for female")
        time.sleep(5)
        engine.runAndWait()
        print("say 1 for male and 2 for female")
        r = sr.Recognizer()
        print("1")
        with sr.Microphone() as source:
            print("2")
            energy_threshold = 3000
            print("3")
            # time.sleep(5)
            audio = r.listen(source)
            print("44")
            worda = r.recognize_google(audio)
            print(worda)
            print("5")
            if worda == '1':
                print("you chosed male voice")
            if worda == '2':
                print("you chosed female voice")

            if worda == '1':
                engine = pyttsx.init()
                sound = engine.getProperty('voices')
                rate = engine.getProperty('rate')
                volume = engine.getProperty('volume')
                engine.setProperty('rate', 100)
                engine.setProperty('volume', .5)
                engine.say(
                    "What kind of information would you like to Say, one for detailed information and two for a brief  information overview.One for replay and two for stop and move on to the next system")
                time.sleep(5)
                engine.runAndWait()
                print('0')

                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    time.sleep(12)
                    audio = r.listen(source)
                    print("44")
                    worde = r.recognize_google(audio)
                    print(worde)
                    print("5")
                    # print(worda)
                    if worde == '1':
                        print("you said detail")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say(
                            "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")
                        time.sleep(20)
                        engine.runAndWait()
                        r = sr.Recognizer()
                        print("1")
                        with sr.Microphone() as source:
                            print("2")
                            energy_threshold = 3000
                            print("3")
                            time.sleep(15)
                            audio = r.listen(source)
                            print("44")
                            word = r.recognize_google(audio)
                            print(word)
                            if word == '1':
                                print("you said detail")
                                engine = pyttsx.init()
                                sound = engine.getProperty('voices')
                                rate = engine.getProperty('rate')
                                engine.setProperty('rate', 50)
                                engine.say(
                                    "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")  # give more and more importance.becoming key certain for survival of developing,manufacturing companies.digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers the complete digital representation of the entire physical value change is our ultimate goal.we call solution platform which we created for this purpose digital enterprice.kindly move on to the next system")
                                time.sleep(20)
                            if word == '2' or 'to':
                                stop1d()

                    if worde == '2' or 'to':
                        print("you said brief")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say('Bye bye.Kindly move on to the next system')
                        time.sleep(20)
                        engine.runAndWait()
                # time.sleep(10)
                # time.sleep(55)

            if worda == '2' or 'to':
                print('You chose female voice')
                pygame.mixer.init()
                pygame.mixer.music.load("intro.mp3")
                pygame.mixer.music.play()
                time.sleep(15)
                print('0')
                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    # time.sleep(5)
                    audio = r.listen(source)
                    print("4")
                    wordb = r.recognize_google(audio)
                    print(wordb)
                    print("5")
                    if wordb == '1':
                        print("you said detail")
                        pygame.mixer.init()
                        pygame.mixer.music.load("detail.mp3")
                        pygame.mixer.music.play()
                        time.sleep(55)
                        interactive1d()
                        # while(a==1)

                    if wordb == '2' or 'to':
                        print("you said brief")
                        pygame.mixer.init()
                        pygame.mixer.music.load("brief.mp3")
                        pygame.mixer.music.play()

                # time.sleep(55)
                def repeat1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    pygame.mixer.init()
                    pygame.mixer.music.load("detail.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(55)

                def stop1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1d():
                    a = 1
                    while (a == 1):

                        try:
                            audio = r.listen(source)
                            word1 = r.recognize_google(audio)
                            print(word1)
                            if word1 == '1':
                                repeat1d()

                            if word1 == '2':
                                a = 0
                                stop1d()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1d()
                    print('it stopped')
                print('End of Sys')

                def stop1b():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1b():
                    a1 = 1
                    while (a1 == 1):

                        try:
                            audio = r.listen(source)
                            word2 = r.recognize_google(audio)
                            print(word2)
                            if word2 == '1':
                                repeat1b()

                            if word2 == '2':
                                a1 = 0
                                stop1b()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1b()
                    print('it stopped')
                print('End of Sys')


    except Exception as e:
        print
        e
        print('exception1')
        system4()


def system5():
    try:

        engine = pyttsx.init()
        sound = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', .5)
        engine.say("say 1 for male and 2 for female")
        time.sleep(5)
        engine.runAndWait()
        print("say 1 for male and 2 for female")
        r = sr.Recognizer()
        print("1")
        with sr.Microphone() as source:
            print("2")
            energy_threshold = 3000
            print("3")
            # time.sleep(5)
            audio = r.listen(source)
            print("44")
            worda = r.recognize_google(audio)
            print(worda)
            print("5")
            if worda == '1':
                print("you chosed male voice")
            if worda == '2':
                print("you chosed female voice")

            if worda == '1':
                engine = pyttsx.init()
                sound = engine.getProperty('voices')
                rate = engine.getProperty('rate')
                volume = engine.getProperty('volume')
                engine.setProperty('rate', 100)
                engine.setProperty('volume', .5)
                engine.say(
                    "What kind of information would you like to Say, one for detailed information and two for a brief  information overview.One for replay and two for stop and move on to the next system")
                time.sleep(5)
                engine.runAndWait()
                print('0')

                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    time.sleep(12)
                    audio = r.listen(source)
                    print("44")
                    worde = r.recognize_google(audio)
                    print(worde)
                    print("5")
                    # print(worda)
                    if worde == '1':
                        print("you said detail")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say(
                            "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")
                        time.sleep(20)
                        engine.runAndWait()
                        r = sr.Recognizer()
                        print("1")
                        with sr.Microphone() as source:
                            print("2")
                            energy_threshold = 3000
                            print("3")
                            time.sleep(15)
                            audio = r.listen(source)
                            print("44")
                            word = r.recognize_google(audio)
                            print(word)
                            if word == '1':
                                print("you said detail")
                                engine = pyttsx.init()
                                sound = engine.getProperty('voices')
                                rate = engine.getProperty('rate')
                                engine.setProperty('rate', 50)
                                engine.say(
                                    "The seem less integration of data,along the industrial value change will give more and more importance.Becoming key certain for survival of developing,manufacturing companies.Digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers.The complete digital representation of the entire physical value change is our ultimate goal.We call solution platform which we created for this purpose digital enterprice.Kindly move on to the next system.")  # give more and more importance.becoming key certain for survival of developing,manufacturing companies.digital factory division aims to provide its customers with comprehensive protpolia of hardware and software products which enable the comprehensive integration of data from development production and supliers the complete digital representation of the entire physical value change is our ultimate goal.we call solution platform which we created for this purpose digital enterprice.kindly move on to the next system")
                                time.sleep(20)
                            if word == '2' or 'to':
                                stop1d()

                    if worde == '2' or 'to':
                        print("you said brief")
                        engine = pyttsx.init()
                        sound = engine.getProperty('voices')
                        volume = engine.getProperty('volume')
                        rate = engine.getProperty('rate')
                        engine.setProperty('volume', .5)
                        engine.setProperty('rate', 100)
                        engine.say('Bye bye.Kindly move on to the next system')
                        time.sleep(20)
                        engine.runAndWait()
                # time.sleep(10)
                # time.sleep(55)

            if worda == '2' or 'to':
                print('You chose female voice')
                pygame.mixer.init()
                pygame.mixer.music.load("intro.mp3")
                pygame.mixer.music.play()
                time.sleep(15)
                print('0')
                r = sr.Recognizer()
                print("1")
                with sr.Microphone() as source:
                    print("2")
                    energy_threshold = 3000
                    print("3")
                    # time.sleep(5)
                    audio = r.listen(source)
                    print("4")
                    wordb = r.recognize_google(audio)
                    print(wordb)
                    print("5")
                    if wordb == '1':
                        print("you said detail")
                        pygame.mixer.init()
                        pygame.mixer.music.load("detail.mp3")
                        pygame.mixer.music.play()
                        time.sleep(55)
                        interactive1d()
                        # while(a==1)

                    if wordb == '2' or 'to':
                        print("you said brief")
                        pygame.mixer.init()
                        pygame.mixer.music.load("brief.mp3")
                        pygame.mixer.music.play()

                # time.sleep(55)
                def repeat1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    pygame.mixer.init()
                    pygame.mixer.music.load("detail.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(55)

                def stop1d():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1d():
                    a = 1
                    while (a == 1):

                        try:
                            audio = r.listen(source)
                            word1 = r.recognize_google(audio)
                            print(word1)
                            if word1 == '1':
                                repeat1d()

                            if word1 == '2':
                                a = 0
                                stop1d()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1d()
                    print('it stopped')
                print('End of Sys')

                def stop1b():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    # flag2=0

                def interactive1b():
                    a1 = 1
                    while (a1 == 1):

                        try:
                            audio = r.listen(source)
                            word2 = r.recognize_google(audio)
                            print(word2)
                            if word2 == '1':
                                repeat1b()

                            if word2 == '2':
                                a1 = 0
                                stop1b()

                        except:
                            # interactive1d()
                            print('exception')
                            # pygame.mixer.init()
                            # pygame.mixer.music.load("exception.mp3")
                            # pygame.mixer.music.play()

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # while(a==1):
                    interactive1b()
                    print('it stopped')
                print('End of Sys')


    except Exception as e:
        print
        e
        print('exception1')
        system5()


def task1():
    flag1 = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    prev_input1 = 0
    prev_input2 = 0
    prev_input3 = 0
    prev_input4 = 0
    prev_input5 = 0

    # while True:
    while (flag1 == 1):

        t1 = time.time()
        input1 = GPIO.input(24)
        input2 = GPIO.input(23)
        input3 = GPIO.input(25)
        input4 = GPIO.input(12)
        input5 = GPIO.input(16)

        # print('Hello')
        if ((not prev_input1) and input1):
            print("Button 1 pressed")
            t0 = time.time()
            system1()


        elif ((not prev_input2) and input2):
            print('Button 2 pressed')
            t0 = time.time()
            system2()

        elif ((not prev_input3) and input3):
            print('Button 3 pressed')
            t0 = time.time()
            system3()

        elif ((not prev_input4) and input4):
            print('Button 4 pressed')
            t0 = time.time()
            system4()

        elif ((not prev_input5) and input5):
            print('Button 5 pressed')
            t0 = time.time()
            system5()

        if (t1 - t0 >= 120):
            flag1 = 0

        prev_input1 = input1
        time.sleep(0.05)

        prev_input2 = input2
        time.sleep(0.05)

        prev_input3 = input3
        time.sleep(0.05)

        prev_input4 = input4
        time.sleep(0.05)

        prev_input5 = input5
        time.sleep(0.05)

    while (flag1 != 1):
        main()


def lecture():
    print('lecture')
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)


def presentation():
    print('presentation')
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)
    print('presentation')


def off():
    print('off')
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def training():
    print('Training')
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
    print('Training')


def task2():
    try:

        while (flag != 1):
            r = sr.Recognizer()
            with sr.Microphone() as source:

                energy_threshold = 4000
                print('say something')
                audio = r.listen(source)
                print('listened')
                word = r.recognize_google(audio)

                if word == 'presentation mode':
                    presentation()

                elif word == 'lecture mode':
                    lecture()

                elif word == 'mode of':
                    off()

                elif word == 'training mode':
                    training()

        while (flag == 1):
            pass


    except:
        # print(e)
        main()


def main():
    flag = 0
    flag1 = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:

        while (GPIO.input(24) == 1 or GPIO.input(23) == 1 or GPIO.input(25) == 1 or GPIO.input(12) == 1 or GPIO.input(
                16) == 1):
            task1()

        while (GPIO.input(24) == 0 and GPIO.input(23) == 0 and GPIO.input(25) == 0 and GPIO.input(
                12) == 0 and GPIO.input(16) == 0):
            task2()


if __name__ == '__main__':
    flag = 0
    # flag1=1
    main()




















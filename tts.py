import pyttsx3


# engine = pyttsx3.init()
# engine.say("The 1966 Southern Service To WEST CROYDON is now passing Sydenham station at 13:36")
# engine.runAndWait()



def speak(text):
    try: 
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 115)
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

        return True
    except Exception as e:
        print(e)
        return False


def speakFaster(text):
    try: 
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 140)
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

        return True
    except Exception as e:
        print(e)
        return False


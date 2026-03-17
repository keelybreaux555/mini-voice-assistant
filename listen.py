import speech_recognition as sr
import pyttsx3

#Initialize text-to-speech engine
engine = pyttsx3.init()

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Adjusting for background noise...")
	r.adjust_for_ambient_noise(source, duration=2)

	print("Listening...")
	audio = r.listen(source, phrase_time_limit=5)

try:
	text = r.recognize_google(audio)
	print("You said:", text)

	#Make the assistant respond
	response = f"Hello! You said: {text}"
	engine.say(response)
	engine.runAndWait()
except sr.UnknownValueError:
	print("Sorry, I couldn't understand")
	engine.say("Sorry, I could not understand.")
	engine.runAndWait()
except sr.RequestError:
	print("Could not request results; {0}".format(e))

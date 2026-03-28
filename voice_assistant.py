import speech_recognition as sr
import datetime
import webbrowser

recognizer = sr.Recognizer()

def listen():
	with sr.Microphone() as source:
		print("Listening...")
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		command = recognizer.recognize_google(audio)
		command = command.lower()
		print(f"You said: {command}")
		return command
	except sr.UnknownValueError:
		print("Sorry, I did not understand.")
		return ""
	except sr.RequestError:
		print("Speech service error.")
		return ""

def run_assistant():
	print("Voice Assistant Started. Say 'stop' to exit.\n")

	while True:
		command = listen()

		if "hello" in command:
			print("Hello! How can I help you?")

		elif "time" in command:
			now = datetime.datetime.now().strftime("%I:%M %p")
			print(f"The time is {now}")

		elif "open google" in command:
			print("Opening Google...")
			webbrowser.open("https://www.google.com")

		elif "open youtube" in command:
			print("Opening YouTube...")
			webbrowser.open("https://www.youtube.com")

		elif "stop" in command:
			print("Goodbye!")
			break

		elif command != "":
			print("Goodbye!")
			break

		elif command != "":
			print("Command not recognized.")

if __name__ == "__main__":
	run_assistant()
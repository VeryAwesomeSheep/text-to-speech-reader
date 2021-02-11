from playsound import playsound
from gtts import gTTS
import tkinter as tk
import os

def getTTS():
	text = ttr.get()
	speech = gTTS(text, lang = "en")
	with open("TTS.mp3", "wb") as f:
		speech.write_to_fp(f)
	playsound("TTS.mp3")
	os.remove("TTS.mp3")
	

def clearText():
	ttr.set("")

# Initialization of window
root = tk.Tk()
root.geometry("380x100")
root.resizable(width = False, height = False)
root.title("Text to speech reader")

tk.Label(root, text = "Enter text to read:", font = "arial 10 bold").grid(row = 0, column = 0)
ttr = tk.StringVar()
ttrField = tk.Entry(root, textvariable = ttr, width = "60").grid(row = 1, column = 0, padx = 5)

tk.Button(root, text = "Play", command = getTTS, width = 10, height = 2, bg = "green").grid(row = 2, column  = 0, padx = 40, sticky = "w")
tk.Button(root, text = "Clear text", command = clearText, width = 10, height = 2, bg = "red").grid(row = 2, column = 0, padx = 40, sticky = "e")

# Running tkinker
root.mainloop()
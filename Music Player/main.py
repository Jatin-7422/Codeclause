from tkinter import *
from tkinter import Button

import pygame

root = Tk()
root.title("Music Player")
root.geometry("700x600")

pygame.mixer.init()


def play():
    pygame.mixer.music.load("MUSIC/Har Har Shambhu Shiv Mahadeva_64(PagalWorld.com.se).mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

button_1 = Button(root, text="Play", command=play, font=("Helvetica", 32, "normal"))
button_1.pack(pady=20)

button_2 = Button(root, text="Stop", command=stop, font=("Helvetica", 32, "normal"))
button_2.pack(pady=20)


root.mainloop()

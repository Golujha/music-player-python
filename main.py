import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
music_player = tkr.Tk()
music_player.title("Music player by Sadique")
music_player.geometry("450x300")
import os

folder = askdirectory()
os.chdir(folder)

song_list = os.listdir()

play_list = tkr.Listbox(music_player,font="Arial 12 bold",bg="yellow",selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos,item)
    pos += 1

# playing song

pygame.init()
pygame.mixer.init()
var = tkr.StringVar()
song_title = tkr.Label(music_player,font="Arial 14 bold",textvariable=var)
song_title.pack()
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
button1 = tkr.Button(music_player,command=play, width=5, height=3, font=("Arial 12 bold"), text="play",bg="blue",fg="white")
button2 = tkr.Button(music_player,command=stop, width=5, height=3, font=("Arial 12 bold"), text="stop",bg="red",fg="white")
button3 = tkr.Button(music_player,command=pause, width=5, height=3, font=("Arial 12 bold"), text="pause",bg="orange",fg="white")
button4 = tkr.Button(music_player,command=unpause, width=5, height=3, font=("Arial 12 bold"), text="unpause",bg="purple",fg="white")


button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")

play_list.pack(fill="both",expand="yes")



music_player.mainloop()
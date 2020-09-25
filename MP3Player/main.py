import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

def main():
    musicPlayer = tkr.Tk()
    musicPlayer.title('MP3 Player')
    musicPlayer.geometry('450x350')

    directory = askdirectory()
    os.chdir(directory)

    songList = os.listdir()
    playList = tkr.Listbox(musicPlayer, font='Helvetica 12 bold', bg='yellow', selectmode=tkr.SINGLE)

    position = 0
    for item in songList:
        playList.insert(position, item)
        position += 1

    pygame.init()
    pygame.mixer.init()

    def play():
        pygame.mixer.music.load(playList.get(tkr.ACTIVE))
        var.set(playList.get(tkr.ACTIVE))
        pygame.mixer.music.play()

    def pause():
        pygame.mixer.music.pause()

    def unpause():
        pygame.mixer.music.unpause()

    def stopPlay():
        pygame.mixer.music.stop()

    btnPlay = tkr.Button(musicPlayer, width=5, height=3,
                        font='Helvetica 12 bold', text='Play',
                        command=play, bg='red', fg='white')
    btnStop = tkr.Button(musicPlayer, width=5, height=3,
                         font='Helvetica 12 bold', text='Stop',
                         command=stopPlay, bg='purple', fg='white')
    btnPause = tkr.Button(musicPlayer, width=5, height=3,
                          font='Helvetica 12 bold', text='PAUSE',
                          command=pause, bg='green', fg='white')
    btnUnpause = tkr.Button(musicPlayer, width=5, height=3,
                            font='Helvetica 12 bold', text='UNPAUSE',
                            command=unpause, bg='blue', fg='white')

    var = tkr.StringVar()
    songTit = tkr.Label(musicPlayer, font='Helvetica 12 bold', textvariable=var)

    songTit.pack()
    btnPlay.pack(fill='x')
    btnStop.pack(fill='x')
    btnPause.pack(fill='x')
    btnUnpause.pack(fill='x')
    playList.pack(fill='both', expand='yes')

    musicPlayer.mainloop()

if __name__ == '__main__':
    main()
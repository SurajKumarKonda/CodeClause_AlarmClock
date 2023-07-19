from tkinter import *
import time
from pygame import mixer
from tkinter import messagebox

root = Tk()
root.title("Alarm Clock")
root.geometry("610x340")

alarmtime = StringVar()
msg1 = StringVar()
head = Label(root, text="ALARM CLOCK", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)
mixer.init()

def ala():
    a = alarmtime.get()

    AlarmT = a
    CurrentTime = time.strftime("%H:%M")

    while AlarmT != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
    if AlarmT == CurrentTime:
        mixer.music.load('Alarm Clock.mp3')
        mixer.music.play()
        msg = messagebox.showinfo('It is time!', f'{msg1.get()}')
        if msg == 'ok':
            mixer.music.stop()

clockimg = PhotoImage(file="clock-neon.png")
img = Label(root, image=clockimg)
img.grid(rowspan=4, column=0)
inputt = Label(root, text="Enter Time(HH:MM):", font=('comic sans', 18))
inputt.grid(row=1, column=1)
altime = Entry(root, textvariable=alarmtime, font=('comic sans', 18), width=6)
altime.grid(row=1, column=2)
msg = Label(root, text="Enter Custom Message", font=('comic sans', 18))
msg.grid(row=2, column=1, columnspan=2)
msginput = Entry(root, textvariable=msg1, font=('comic sans', 18))
msginput.grid(row=3, column=1, columnspan=2)
submit = Button(root, text="SUBMIT", font=('comic sans', 18),
                command=ala)
submit.grid(row=4, column=1, columnspan=2)
root.mainloop()   












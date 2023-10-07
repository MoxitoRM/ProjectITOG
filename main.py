from tkinter import *
import tkinter as ttk
import time
import service

start_time = 0
n_time = 0
random_word = service.random_word()
def show_message():
    if label["text"] == entry.get():
        n_time = time.time()
    else:
        label2["text"] = "Неправильно!!!!!!!!!!!!!!!!!!!!"
def nachalo():
    start_time = time.time()
    label["text"] = random_word
def result():
    label2["text"] = delta_time

delta_time = n_time - start_time

# print(random_word)

# if service.sravnenie(word, random_word):
#     print("Дальше!")
# else:
#     print("Заново!")

root = Tk()
root.geometry("1000x500")
root.title("Калькулятор количества слов в минуту")


button1 = ttk.Button(root,text="Начать", command = nachalo)
button1.pack()
button2 = ttk.Button(root,text="Давай!", command = show_message)
button2.pack()
button3 = ttk.Button(root,text="Результат", command = result)
button3.pack()

entry = ttk.Entry()
entry.pack(expand=TRUE)

label2 = ttk.Label()
label2.place()
label2.pack()
label = ttk.Label()
label.place()
label.pack()


root.mainloop()


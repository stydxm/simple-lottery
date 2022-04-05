from tkinter import *
import random

def choose(list, number):
    #需要判断number是否超出范围以及list中是否有重复
    choosed = []
    flag = True
    while flag:
        c = random.choice(list)
        if c not in choosed:
            choosed.append(c)
        if len(choosed) >= number:
            flag = False
    return choosed

def process_input():
    number = 1
    inputs = list_input.get().split(",")
    number = int(number_input.get())
    temp = []
    msg = ""
    if number == 0 or len(inputs) == 0:
        msg = "请输入"
    else:
        for obj in inputs:
            if obj in temp:
                msg = "存在重复"
            else:
                temp.append(obj)
        if number > len(inputs):
            msg = "抽取数量过大"
        else:
            for i in choose(inputs, number):
                msg += i + " "
        result_text["text"] = msg

root= Tk()

list_input_message = Label(root, text="输入待选，以英文逗号分隔")
list_input_message.grid(row=0, sticky=W)
list_input = Entry(root)
list_input.grid(row=0, column=1, sticky=E)

number_input_message = Label(root, text="输入抽取的数量")
number_input_message.grid(row=1, sticky=W)
number_input = Entry(root)
number_input.grid(row=1, column=1, sticky=E)

choose_button = Button(root, text="抽取", command=process_input)
choose_button.grid(row=2, column=1, sticky=E)

result_text = Label(root, text="")
result_text.grid(row=3)

root.mainloop()
from tkinter import *
from tkinter import ttk
import random
from algos.bubble import bubbleSort
from algos.selection import selectionSort
from colors import *

root = Tk()
root.title("Sorting Algorithms Visualization")
root.maxsize(1500, 1000)
root.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Selection Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []


def close():
    root.destroy()



def drawInfo(data, colorArray):
    canvas.delete("all")
    canvas_width = 1300
    canvas_height = 700
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 650
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update()


def generateArray():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawInfo(data, [PINK for x in range(len(data))])

def speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.000001


def sort():
    global data
    timeSet = speed()

    if algo_menu.get() == 'Bubble Sort':
        bubbleSort(data, drawInfo ,timeSet)
    if algo_menu.get() == 'Selection Sort':
        selectionSort(data, drawInfo, timeSet)



UI_FRAME = Frame(root, width=900, height=600, bg=WHITE)
UI_FRAME.grid(row=0, column=0, padx=0, pady=0)

l1 = Label(UI_FRAME, text="algo: ", bg=WHITE, fg=BLACK, font=("Arial", 18, "bold"))
l1.grid(row=0, column=0, padx=1, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_FRAME, state="readonly",textvariable=algorithm_name, values=algo_list)
algo_menu.bind("<<ComboboxSelected>>", lambda e: UI_FRAME.focus())
algo_menu.grid(row=0, column=1, padx=1, pady=5)
algo_menu.current()

l2 = Label(UI_FRAME, text="speed: ", bg=WHITE, fg=BLACK, font=("Arial", 18, "bold"))
l2.grid(row=1, column=0, padx=1, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_FRAME, state="readonly",textvariable=speed_name, values=speed_list)
speed_menu.bind("<<ComboboxSelected>>", lambda e: UI_FRAME.focus())
speed_menu.grid(row=1, column=1, padx=1, pady=5)
speed_menu.current()

b1 = Button(UI_FRAME, text="generate new array", command=generateArray, bg=LIGHT_GREEN)
b1.grid(row=5, column=0, padx=0, pady=0)

b2 = Button(UI_FRAME, text="sort", command=sort, bg=BLUE)
b2.grid(row=5, column=1, padx=10, pady=10)

b3 = Button(UI_FRAME, text="quit", command=close, bg=BLUE)
b3.grid(row=5, column=2, padx=10, pady=10)


canvas = Canvas(root, width=1300, height=700, bg=WHITE)
canvas.grid(row=1, column=0, padx=50, pady=5)





root.mainloop()
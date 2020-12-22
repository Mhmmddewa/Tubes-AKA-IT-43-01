from tkinter import*
from tkinter import ttk
import random
import time
import sys
import threading

root = Tk()
root.title('sorting')
root.maxsize(1920, 1080)
root.config(bg='black')

#variable
selected_alg = StringVar()
alist = []
alist2 = []


def gambar(alist, warna):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(alist) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(alist) for i in alist]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=warna[i])
    root.update_idletasks()


def gambar2(alist2, warna):
    canvas2.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(alist2) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(alist2) for i in alist2]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas2.create_rectangle(x0, y0, x1, y1, fill=warna[i])
    root.update_idletasks()


def Random():
    global alist
    global alist2

    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 100
    try:
        size = int(sizeEntry.get())
    except:
        size = 50

    alist = []
    alist2 = []

    for _ in range(size):
        alist.append(random.randrange(minVal, maxVal+1))

    alist2 = alist.copy()

    gambar(alist, ['white' for x in range(len(alist))])
    gambar2(alist2, ['white' for x in range(len(alist2))])



def gnomeSort(alist, gambar): 
    start_time= time.time()
    index = 0
    n = len(alist)
    while index < n: 
        if index == 0: 
            index = index + 1
        if alist[index] >= alist[index - 1]: 
            index = index + 1
        else: 
            alist[index], alist[index-1] = alist[index-1], alist[index] 
            index = index - 1
        gambar(alist, ['blue' if x  == index or x == n else 'white' for x in range(len(alist))])
        time.sleep(0.01)
    Label(text=("%s seconds" % (time.time() - start_time))).grid(row=1, column=0, padx=5, pady=5)
    
    return alist

def insertion_sort(alist2, gambar2):
    start_time2 = time.time()
    for i in range(1, len(alist2)):
        key = alist2[i]
        j = i-1
        while j >= 0 and key < alist2[j]:
            alist2[j+1] = alist2[j]
            gambar2(alist2, ['blue' if x == j or x == key else 'white' for x in range(len(alist))])
            time.sleep(0.01)
            j -= 1
        alist2[j+1] = key
    Label(text=("%s seconds" % (time.time() - start_time2))).grid(row=1, column=2, padx=5, pady=5)

    
def Algortitma():
    global alist
    global alist2
    threading.Thread(target=insertion_sort, args=(alist2, gambar2)).start()
    threading.Thread(target=gnomeSort, args=(alist, gambar)).start()



#UI_Label
Label(text="Gnome Sort").grid(row=0, column=0, padx=5, pady=5)
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=4, column=0, padx=10, pady=5)

Label(text="Insertion Sort").grid(row=0, column=2, padx=5, pady=5)
canvas2 = Canvas(root, width=600, height=380, bg='white')
canvas2.grid(row=4, column=2, padx=10, pady=5)
Button(text="Mulai", command=Algortitma, bg='white').grid(row=1, column=1, padx=5, pady=5)

Button(text="Nilai Random", command=Random, bg='white').grid(row=0, column=1, padx=5, pady=5)


root.mainloop()
from tkinter import *
import numpy as np

import MapGenerator as mg

def onClick():
    dataArray[0] = int(map_x.get())
    dataArray[1] = int(map_y.get())
    dataArray[2] = int(terrain.get())
    dataArray[3] = float(grass_prob.get())
    dataArray[4] = int(cellular_iter_num.get())
    dataArray[5] = float(lamb.get())
    dataArray[6] = int(snow.get())
    
    heatmap_data = mg.main(dataArray)

root = Tk()
dataArray = [0,0,0,0,0,0,0]


title = Label(root, text="필요 데이터 입력")
title.grid(row=0, column=1)
 
map_x_lbl = Label(root, text="x 크기")
map_x_lbl.grid(row=1, column=1)

default1 = StringVar()
default1.set(100)
map_x = Entry(root, textvariable = default1)
map_x.grid(row=1, column=2)

map_y_lbl = Label(root, text="y 크기")
map_y_lbl.grid(row=2, column=1)

default2 = StringVar()
default2.set(100)
map_y = Entry(root, textvariable = default2)
map_y.grid(row=2, column=2)
 
terrain_lbl = Label(root, text="지형지물 종류")
terrain_lbl.grid(row=4, column=1)

default4 = StringVar()
default4.set(2)
terrain = Entry(root, textvariable = default4)
terrain.grid(row=4, column=2)

grass_prob_lbl = Label(root, text="풀 타일 밀도(0.3~0.5)")
grass_prob_lbl.grid(row=5, column=1)

default5 = StringVar()
default5.set(0.4)
grass_prob = Entry(root, textvariable = default5)
grass_prob.grid(row=5, column=2)

cellular_iter_num_lbl = Label(root, text="셀룰러 오토마타 알고리즘 수행(기본 5)")
cellular_iter_num_lbl.grid(row=6, column=1)

default6 = StringVar()
default6.set(5)
cellular_iter_num = Entry(root, textvariable = default6)
cellular_iter_num.grid(row=6, column=2)

lamb_lbl = Label(root, text="지형지물 밀도(기본 0.1)")
lamb_lbl.grid(row=7, column=1)

default7 = StringVar()
default7.set(0.1)
lamb = Entry(root, textvariable = default7)
lamb.grid(row=7, column=2)

snow_lbl = Label(root, text="눈 타일 크기")
snow_lbl.grid(row=8, column=1)

default8 = StringVar()
default8.set(5)
snow = Entry(root, textvariable = default8)
snow.grid(row=8, column=2)

btn = Button(root, text="Generate", command=onClick)
btn.grid(row=9, column=2)

root.mainloop()

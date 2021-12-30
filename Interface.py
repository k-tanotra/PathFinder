import tkinter as tk

Title = "PathFinder"
windowLength = "600"
windowBreadth = "600"

window = tk.Tk()
window.title(Title)

window.geometry(windowLength + "x" + windowBreadth)

BFS_Button = tk.Button(window, text="BFS")
BFS_Button.grid(row=1, column=0)

DFS_Button = tk.Button(window, text="DFS")
DFS_Button.grid(row=1, column=1)

UCS_Button = tk.Button(window, text="UCS")
UCS_Button.grid(row=2, column=0)

AStar_Button = tk.Button(window, text="A*")
AStar_Button.grid(row=2, column=1)


window.mainloop()

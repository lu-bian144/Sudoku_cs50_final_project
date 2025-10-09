from tkinter import*
window = Tk()
grid_frame = Frame(window, width=500, height=300)
grid_frame.propagate(False)
grid_frame.pack(expand=True)
for i in range(9):
    for j in range(9):
        cell_i= Entry(grid_frame, width= 1, font = "Arial 30")
        cell_i.grid(row = i , column = j, sticky='NSEW')
for i in range(10):
    grid_frame.grid_rowconfigure(i, weight=1, minsize=70)
    grid_frame.grid_columnconfigure(i, weight=1, minsize=70)
grid_number=0

window.mainloop()
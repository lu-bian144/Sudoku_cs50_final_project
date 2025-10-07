from tkinter import*
window = Tk()
grid_frame = Frame(window, padx=300, pady=300)
grid_frame.pack(expand=True)
while True:
    def get_input():
        value = int(input(""))
        return value

    grid_number= int(get_input())

    for i in range(grid_number):
        cell_i= Entry(grid_frame, width= 2, font = "Arial 25")
        cell_i.grid(row = i , column = 0, sticky='NSEW')
        for j in range(grid_number):
            cell_i= Entry(grid_frame, width= 2, font = "Arial 25")
            cell_i.grid(row = i , column = j, sticky='NSEW')
    for i in range(10):
        grid_frame.grid_rowconfigure(i, weight=1)
        grid_frame.grid_columnconfigure(i, weight=1)
    grid_number=0


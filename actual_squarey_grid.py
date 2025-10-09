from tkinter import *
window = Tk()
def main():
    WIDTH = 362
    HEIGHT = 362
    grid = Canvas(window, width= WIDTH, height=HEIGHT)
    ancho = WIDTH-2
    height= HEIGHT-2
    cell_size = 40
    big_square_outline = (cell_size)*3
    create_grid(ancho, height, cell_size, big_square_outline, grid)
def create_grid(grid_width, grid_height, grid_cell_size, square_outline, canvas):
    
    l=0
    for i in range (2, grid_width, grid_cell_size):# you can then asign and i to each square
        for j in range (2, grid_height, grid_cell_size): # (starting value, finish value, skip of this many per iteration (0, 40, 80 ...))
            canvas.create_rectangle( i, j, i+grid_cell_size, j+grid_cell_size, width=1, outline= "black", fill="white")
    canvas.pack(expand=True)# line above: coordinate of the upper left corner (ithinkso), coordinates of bottom right corner
    while l < 3:
        canvas.create_line((square_outline*l)+2, 2, (square_outline*l)+2, grid_height+2, width=3, fill="blueviolet")
        canvas.create_line(2, (square_outline*l)+2, grid_height+2, (square_outline*l)+2, width=3, fill="blueviolet")
        l+=1
    canvas.create_line(362,0,362,362, width=3, fill="blueviolet")
    canvas.create_line(0,362,362,362,width=3, fill="blueviolet")
main()
window.mainloop()
#if id [-1] == row/column number:
    #if input == content of each square per row/column
        #return False
    #else:
        #return True
#else:
    #pass/continue
#trying to figure out a checking system LOL basically brain puke
#grid_height+2 NOTEE: i should change this to be the idfference between the canvas width and the grid width
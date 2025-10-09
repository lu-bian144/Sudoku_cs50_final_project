from tkinter import *
window = Tk()
def main():
    WIDTH = 452
    HEIGHT = 452
    grid = Canvas(window, width= WIDTH, height=HEIGHT)
    ancho = WIDTH-2
    height= HEIGHT-2
    cell_size = 50
    big_square_outline = (cell_size)*3
    create_grid(ancho, height, cell_size, big_square_outline, grid)
    ids = create_grid(ancho, height, cell_size, big_square_outline, grid)
    print(ids)
def create_grid(grid_width, grid_height, grid_cell_size, square_outline, canvas):
    square_id = []
    l=0
    for i in range (2, grid_width, grid_cell_size):# you can then asign and i to each square
        for j in range (2, grid_height, grid_cell_size): # (starting value, finish value, skip of this many per iteration (0, 40, 80 ...))
            canvas.create_rectangle( i, j, i+grid_cell_size, j+grid_cell_size, width=1, outline= "black", fill="white")
            square_id.append(f"{round(i/grid_cell_size)+1}, {round(j/grid_cell_size)+1}")
            text= Entry(canvas, justify="center", font="Arial 20", insertontime=0)
            canvas.create_window((i+i+grid_cell_size)/2 ,(j+j+grid_cell_size)/2, window=text, width= grid_cell_size-2, height= grid_cell_size-2)
    canvas.pack(expand=True)# line above: coordinate of the upper left corner (ithinkso), coordinates of bottom right corner
    while l < 10:
        canvas.create_line((square_outline*l)+2, 2, (square_outline*l)+2, grid_height+2, width=3, fill="blueviolet")
        canvas.create_line(2, (square_outline*l)+2, grid_height+2, (square_outline*l)+2, width=3, fill="blueviolet")
        l+=1
    canvas.create_line(grid_width+2,0,grid_width+2,grid_height+2, width=3, fill="blueviolet")
    canvas.create_line(0,grid_height+2,grid_width+2,grid_height+2,width=3, fill="blueviolet")
    return square_id
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
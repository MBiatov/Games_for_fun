from tkinter import *
import time, random

def generate_matrix():
    mas = [1,0]
    array = []
    new = []
    for i in range(15):
        for j in range(15):
            new.append(random.choice(mas))
        array.append(new)
        new = []
    return array

def draw_grid(mass):
  grid = []
  for n in range(len(mass)):
    grid.append([])
    for i in range(len(mass[0])):
      if mass[n][i] == 0:
        color = 'white'
      else:
        color = 'green'
      grid[n].append(Canvas(master, background=color, height="20", width="20"))
      grid[n][i].grid(row=n, column=i)

def check_neighbours(row, column, rows, columns, mass):
  sum_of_alive = 0
  for i in range(-1,2):
    for j in range(-1,2):
      if not (i == 0 and j == 0):        
        if (row + i)< rows and (column + j)< columns:
          if  (row - i) >= 0 and (column - j) >= 0:
            sum_of_alive += mass[((row + i) % rows)][((column + j) % columns)]
  return sum_of_alive

def define_status_of_cell(rows,columns,mass,next_mass):
  for i in range(rows):
    for j in range(columns):
      number_of_neighbours = check_neighbours(i,j,rows,columns,mass)
      if number_of_neighbours < 2 or number_of_neighbours > 3:
        next_mass[i][j] = 0
      elif number_of_neighbours == 3 and mass[i][j] == 0:
        next_mass[i][j] = 1
      else:
        next_mass[i][j] = mass[i][j]
  return next_mass


mass = generate_matrix()
master = Tk()
next_mass = mass
rows = len(mass)
columns = len(mass[0])

def run_game(rows, columns, mass, next_mass):
  draw_grid(mass)
  for i in range(500):
    time.sleep(.1)
    define_status_of_cell(rows, columns, mass, next_mass)
    draw_grid(next_mass)
    master.update()

run_game(rows, columns, mass, next_mass)

master.mainloop()
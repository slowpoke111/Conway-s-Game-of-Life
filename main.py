import time
'''
j increasing - down
k increasing - right
j decreasing - up
k decreasing - left

j=rows
k=coloums
'''
def createGrid(file):
  f=open(file)
  text=f.readlines()
  f.close()
  lines=[line.strip() for line in text]
  grid=[]
  for i in range(30):
    row=[]
    for j in range(50):
      row.append(False)
    grid.append(row)
  for coord in lines:
    point=coord.split()
    grid[int(point[0])][int(point[1])]=True
  return(grid)
def printGrid(grid):
  for row in grid:
    for cell in row:
      if cell:
        print('o',end='')
      else:
        print('-',end='')
    print()
def rules(grid,j,k):
  cells=0
  if j+1<len(grid) and grid[j+1][k]:
    cells+=1
  if j+1<len(grid) and k+1<len(grid[j]) and grid[j+1][k+1]:
    cells+=1
  if j-1>=0 and grid[j-1][k]:
    cells+=1
  if j-1>=0 and k-1>=0 and grid[j-1][k-1]:
    cells+=1
  if j-1>=0 and k+1<len(grid[j]) and grid[j-1][k+1]:
    cells+=1
  if j+1<len(grid) and k-1>=0 and grid[j+1][k-1]:
    cells+=1
  if k-1>=0 and grid[j][k-1]:
    cells+=1
  if k+1<len(grid[j]) and grid[j][k+1]:
    cells+=1
    
  if grid[j][k]:
    if cells<2:
      return(False)
    elif cells==2 or cells==3:
      return(True)
    elif cells>=4:
      return(False)
  else:
    if cells==3:
      return(True)
def emptyGrid():
  grid=[]
  for i in range(30):
    row=[]
    for j in range(50):
      row.append(False)
    grid.append(row)
  return(grid)
    
grid=createGrid('b-heptomino-shuttle.in')
printGrid(grid)
while True:
  print('\033c')
  newGrid=emptyGrid()
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      newGrid[i][j]=rules(grid,i,j)
  printGrid(newGrid)
  grid=newGrid
  time.sleep(0.5)

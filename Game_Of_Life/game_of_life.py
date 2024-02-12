#!/usr/bin/env python3
"""
This is a version implementation of Conway´s Game of Life inspired from 'The big book of small python projects'
"""

import copy, random, sys, time

GRID_WIDTH = 20
GRID_HEIGHT = 20
ALIVE_CELL = '*'
DEATH_CELL = ' '

nextGrid = {}

for x in range(GRID_WIDTH):
  for y in range(GRID_HEIGHT):
    if random.randint(0, 1) == 0:
      nextGrid[(x, y)] = ALIVE_CELL
    else:
      nextGrid[(x, y)] = DEATH_CELL

while True:
  print('\n' * 50)
  grid = copy.deepcopy(nextGrid)

  for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
      print(grid[(x, y)], end='')
    print()
  print('Press Ctrl-C to exit.')

  for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
      left = (x - 1) % GRID_WIDTH
      right = (x + 1) % GRID_WIDTH
      above = (y - 1) % GRID_HEIGHT
      below = (y + 1) % GRID_HEIGHT

      totalNeighbors = 0

      if grid[(left, above)] == ALIVE_CELL:
        totalNeighbors += 1
      if grid[(right, above)] == ALIVE_CELL:
        totalNeighbors += 1
      if grid[(x, above)] == ALIVE_CELL:
        totalNeighbors += 1
      if grid[(x, below)] == ALIVE_CELL:
        totalNeighbors += 1
      if grid[(left, below)] == ALIVE_CELL:
        totalNeighbors += 1
      if grid[(right, below)] == ALIVE_CELL:
        totalNeighbors += 1

      if grid[(x, y)] == ALIVE_CELL and (totalNeighbors == 3 or totalNeighbors == 2):
        nextGrid[(x, y)] = ALIVE_CELL
      elif grid[(x, y)] == DEATH_CELL and totalNeighbors == 3:
        nextGrid[(x, y)] = ALIVE_CELL
      else:
        nextGrid[(x, y)] = DEATH_CELL

  try:
    time.sleep(1)
  except KeyboardInterrupt:
    print()
    print("Conway's Game of Life")
    sys.exit()

#!/usr/bin/env python3
# Purpose: Conway's Game of Life simulation
"""
This is a version implementation of Conway´s Game of Life inspired from 'The big book of small python projects'
"""
import argparse
import copy, random, sys, time

def simulation(height, width, symbol):
  GRID_HEIGHT = height
  GRID_WIDTH = width
  ALIVE_CELL = symbol[0]
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
    print('Grid height: {} width: {}'.format(height, width))
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

def get_args():
  """Get command line arguments."""

  parser = argparse.ArgumentParser(description = "Conway's Game of Life")
  parser.add_argument('-gh', '--height', type=int, metavar='height', default=20, help='Height of the grid')
  parser.add_argument('-gw', '--width', type=int, metavar='width', default=20, help='Width of the grid')
  parser.add_argument('-s', '--symbol', type=str, metavar='symbol', default='*', help='Symbol to represent a live cell')
  args = parser.parse_args()

  return args

def main():
  """Entry poing to call other functions to run the simulation."""
  args = get_args()
  simulation(int(args.height), int(args.width), args.symbol)

if __name__ == '__main__':
  main()


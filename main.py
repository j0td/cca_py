import sys
import time
import random
import colorsys

# Global variables
_RULE = {'w': int(sys.argv[1]), 'h': int(sys.argv[2]), 'n': int(sys.argv[3]), 'neighbor': sys.argv[4]}
_COLORS = [list(map(lambda x: int(255 * x), list(colorsys.hsv_to_rgb((i + 1) / _RULE['n'], 1, 1)))) for i in range(_RULE['n'])]

def main():
  cells = init()
  # next_generation(cells)
  try:
    while True:
      render(cells)
      cells = init()
      time.sleep(0.2)
  except KeyboardInterrupt:
    when_end()

def next_generation(cells):
  """
  Calculate next generation cells

  Parameters
  ----------
  cells: list
    2d-list cells
  
  Returns
  -------
  next_generation_cells: list
    2d-list next generation cells
  """

  return init()

def is_advance(neighbor_cells):
  """
  Return True if neighbor cells contain next generation cells over threshold
  
  Parameters
  ----------
  neighbor_cells: list
    neighborhood cells
  
  Returns
  -------
  advance: bool
    do / don't advance to next generation
  """

  return True

def when_end():
  sys.stdout.write(f'\033[J')
  sys.stdout.write('goodbye!\n')
  return -1

def init():
  """
  Set random state to all cell.

  Returns
  -------
  initialized_cells: list
    2d-list cells filled with random state
  """
  initialized_cells = [[random.randrange(0, _RULE['n']) for i in range(_RULE['w'])] for j in range(_RULE['h'])]
  return initialized_cells

def render(cells):
  """
  Rendering cells

  Parameters
  ----------
  cells: list
    2d-list cells
  """
  for row in cells:
    for cell in row:
      sys.stdout.write(f'\033[48;2;{_COLORS[cell][0]};{_COLORS[cell][1]};{_COLORS[cell][2]}m  \033[0m')
    sys.stdout.write('\n')
  sys.stdout.flush()
  sys.stdout.write(f'\033[{_RULE["h"]}A')

if __name__ == '__main__':
  main()
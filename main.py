import sys
import time
import random
import itertools
import colorsys

# Global variables
_RULE = {
  'w': int(sys.argv[1]), # width
  'h': int(sys.argv[2]), # height
  'r': int(sys.argv[3]), # range of neighborhood
  't': int(sys.argv[4]), # threshold
  'c': int(sys.argv[5]), # count of states
  'n': sys.argv[6] # type of neighborhood
}
_COLORS = [list(map(lambda x: int(255 * x), list(colorsys.hsv_to_rgb((i + 1) / _RULE['c'], 1, 1)))) for i in range(_RULE['c'])]

def main():
  cells = init()
  # next_generation(cells)
  try:
    while True:
      render(cells)
      cells = next_generation(cells)
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

  x_expanded_cells = [cells[y][-_RULE['r']:] + cells[y] + cells[y][:_RULE['r']] for y in range(len(cells))]
  expanded_cells = x_expanded_cells[-_RULE['r']:] + x_expanded_cells + x_expanded_cells[:_RULE['r']]

  flat_next_generation_cells = []
  for y in range(_RULE['r'], _RULE['h'] + _RULE['r']):
    cut_rows = expanded_cells[y - _RULE['r']:y] + expanded_cells[y:y + _RULE['r'] + 1]
    for x in range(_RULE['r'], _RULE['w'] + _RULE['r']):
      cut_cells = [r[x - _RULE['r']:x] + r[x:x + _RULE['r'] + 1] for r in cut_rows]
      flatten_cut_cells = list(itertools.chain.from_iterable(cut_cells))
      next_state = expanded_cells[y][x] + 1 if is_advance(flatten_cut_cells, expanded_cells[y][x]) else expanded_cells[y][x]

      if next_state < _RULE['c']:
        flat_next_generation_cells.append(next_state)
      else:
        flat_next_generation_cells.append(0)

  next_generation_cells = [list(t) for t in zip(*[iter(flat_next_generation_cells)]*_RULE['w'])]

  return next_generation_cells

def is_advance(neighbor_cells, current_state):
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

  advance = neighbor_cells.count(current_state + 1) > _RULE['t'] if current_state < _RULE['c'] - 1 else neighbor_cells.count(0) > _RULE['t']

  return advance

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
  initialized_cells = [[random.randrange(0, _RULE['c']) for x in range(_RULE['w'])] for y in range(_RULE['h'])]
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
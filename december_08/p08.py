
import numpy as np

def is_visible(array_heights, current_tree_height):

  for height in array_heights:
    if height >= current_tree_height:
      return False

  return True

def compute_directional_scenic_score(array_heights, current_tree_height):

  scenic_score = 0

  for height in array_heights:
    if height == -1:
      break
    if height < current_tree_height:
      scenic_score += 1
    elif height >= current_tree_height:
      scenic_score = scenic_score + 1
      break

  return scenic_score

def solve_1_and_2(fname):

  ROW_MAX = 200
  COlUMN_MAX = 200

  # Every edge entry is -1 and surrounds the actual grid
  grid = [[-1 for column in range(COlUMN_MAX)] for row in range(ROW_MAX)]

  with open(fname) as p_input:

    row = 1

    for line in p_input:

      line_stripped = line.strip()

      column = 1
      for height in line_stripped:
        grid[row][column] = int(height)
        column += 1

      row += 1

    number_of_visible_trees = 0

    np_grid = np.array(grid)

    for row in range(1,ROW_MAX - 1):
      for column in range(1,COlUMN_MAX - 1):
        tree_height = np_grid[row][column]
        if is_visible(np_grid[:row, column], tree_height) or is_visible(np_grid[row + 1:, column], tree_height) or is_visible(np_grid[row, :column], tree_height) or is_visible(np_grid[row, column+1:], tree_height):
          number_of_visible_trees += 1

    print(number_of_visible_trees)


    max_scenic_score = 0

    for row in range(1,ROW_MAX - 1):
      for column in range(1,COlUMN_MAX - 1):
        tree_height = np_grid[row][column]
        current_scenic_score = compute_directional_scenic_score(np_grid[:row, column][::-1], tree_height) * compute_directional_scenic_score(np_grid[row + 1:, column], tree_height) * compute_directional_scenic_score(np_grid[row, :column][::-1], tree_height) * compute_directional_scenic_score(np_grid[row, column+1:], tree_height)
        if max_scenic_score < current_scenic_score:
          max_scenic_score = current_scenic_score

    print(max_scenic_score)


if __name__ == '__main__':

  solve_1_and_2("p08_input_test")
  solve_1_and_2("p08_input")

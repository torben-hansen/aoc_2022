import math

def is_adjacent(tail, head):
  if math.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2) > 1.5:
    return False
  return True

def sign(n):
  if n < 0: return -1
  else: return 1

def solve_1(fname):

  tail_positions = set()
  head = (0, 0)
  tail = (0, 0)

  tail_positions.add(tail)

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()

      op_direction = line_stripped.split(' ')[0]
      op_value = int(line_stripped.split(' ')[1])

      for _ in range(op_value):
        if op_direction == 'R':
          head = (head[0], head[1] + 1)
        elif op_direction == 'U':
          head = (head[0] + 1, head[1])
        elif op_direction == 'D':
          head = (head[0] - 1, head[1])
        else:
          head = (head[0], head[1] - 1)

        if not is_adjacent(tail, head):
          if math.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2) == 2:
            # Not a diagonal move
            if tail[0] == head[0]:
              tail = (tail[0], tail[1] + sign(head[1] - tail[1])*1)
            else:
              tail = (tail[0] + sign(head[0] - tail[0])*1, tail[1])
          else:
            tail = (tail[0] + sign(head[0] - tail[0])*1, tail[1] + sign(head[1] - tail[1])*1)

          tail_positions.add(tail)

  print(len(tail_positions))

def maybe_move(tail, head):
  tail_new = tail
  if not is_adjacent(tail, head):
    if math.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2) == 2:
      # Not a diagonal move
      if tail[0] == head[0]:
        tail_new = (tail[0], tail[1] + sign(head[1] - tail[1])*1)
      else:
        tail_new = (tail[0] + sign(head[0] - tail[0])*1, tail[1])
    else:
      tail_new = (tail[0] + sign(head[0] - tail[0])*1, tail[1] + sign(head[1] - tail[1])*1)

  return tail_new

def solve_2(fname):

  tail_positions = set()
  head_and_tails = [(0, 0) for _ in range(10)]

  tail_positions.add(head_and_tails[9])

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()

      op_direction = line_stripped.split(' ')[0]
      op_value = int(line_stripped.split(' ')[1])

      for _ in range(op_value):
        head = head_and_tails[0]
        if op_direction == 'R':
          head_and_tails[0] = (head[0], head[1] + 1)
        elif op_direction == 'U':
          head_and_tails[0] = (head[0] + 1, head[1])
        elif op_direction == 'D':
          head_and_tails[0] = (head[0] - 1, head[1])
        else:
          head_and_tails[0] = (head[0], head[1] - 1)

        for i in range(9):
          head_and_tails[i+1] = maybe_move(head_and_tails[i+1], head_and_tails[i])

        tail_positions.add(head_and_tails[9])

  print(len(tail_positions))


if __name__ == '__main__':

  solve_1("p09_input_test")
  solve_1("p09_input")
  solve_2("p09_input_test")
  solve_2("p09_input_test_extra")
  solve_2("p09_input")


def is_different(a, b, c, d):

  if a == b or a == c or a == d:
    return False
  elif b == c or b == d:
    return False
  elif c == d:
    return False

  return True

def solve_1(fname):

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()

      for index in range(0, len(line_stripped)):
        if is_different(line_stripped[index], line_stripped[index + 1], line_stripped[index + 2], line_stripped[index + 3]):
          print(index+3+1)
          break


def is_different_x(array, current_index, increment):

  for i in range(increment):
    for j in range(increment - i - 1):
      if array[current_index + i] == array[current_index + i + (j + 1)]:
        return False

  return True


def solve_2(fname):

  result = 0

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()

      for index in range(0, len(line_stripped) - 14):
        if is_different_x(line_stripped, index, 14):
          print(index+13+1)
          break


if __name__ == '__main__':

  solve_1("p06_input_test")
  solve_1("p06_input")
  solve_2("p06_input_test")
  solve_2("p06_input")

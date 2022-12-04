
def solve_1(fname):

  result = 0

  with open(fname) as p_input:

    for line in p_input:

      ranges = line.split(',')

      index = 0
      range_intervals = [0 for _ in range(4)]

      for r in ranges:
        r_numbers = r.split('-')
        range_intervals[index] = int(r_numbers[0])
        range_intervals[index+1] = int(r_numbers[1])
        index = 2

      if range_intervals[0] >= range_intervals[2] and range_intervals[1] <= range_intervals[3]:
        result += 1
      elif range_intervals[2] >= range_intervals[0] and range_intervals[3] <= range_intervals[1]:
        result += 1

  print('result = {}'.format(result))


def solve_2(fname):

  result = 0

  with open(fname) as p_input:

    for line in p_input:

      ranges = line.split(',')

      index = 0
      range_intervals = [0 for _ in range(4)]

      for r in ranges:
        r_numbers = r.split('-')
        range_intervals[index] = int(r_numbers[0])
        range_intervals[index+1] = int(r_numbers[1])
        index = 2

      if range_intervals[0] >= range_intervals[2] and range_intervals[0] <= range_intervals[3]:
        result += 1
      elif range_intervals[1] >= range_intervals[2] and range_intervals[1] <= range_intervals[3]:
        result += 1
      elif range_intervals[2] >= range_intervals[0] and range_intervals[2] <= range_intervals[1]:
        result += 1
      elif range_intervals[3] >= range_intervals[0] and range_intervals[3] <= range_intervals[1]:
        result += 1

  print('result = {}'.format(result))


if __name__ == '__main__':

  solve_1("p04_input_test")
  solve_1("p04_input")
  solve_2("p04_input_test")
  solve_2("p04_input")

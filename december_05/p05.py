
def solve_1(fname):

  stacks = [[] for _ in range(9)]

  stacks[0] = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
  stacks[1] = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
  stacks[2] = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
  stacks[3] = ['M', 'D', 'P', 'N', 'G', 'Q']
  stacks[4] = ['J', 'L', 'H', 'N', 'F']
  stacks[5] = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
  stacks[6] = ['F', 'D', 'B', 'L']
  stacks[7] = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
  stacks[8] = ['G', 'L', 'D']

  with open(fname) as p_input:

    for line in p_input:

      line_elements = line.strip().split(' ')

      for i in range(int(line_elements[1])):
        stacks[int(line_elements[5]) - 1].append(stacks[int(line_elements[3]) - 1].pop())

  result = ''
  for stack in stacks:
    result += stack[len(stack)-1]
  print(result)
  print(stacks)

def solve_2(fname):

  stacks = [[] for _ in range(9)]

  stacks[0] = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
  stacks[1] = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
  stacks[2] = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
  stacks[3] = ['M', 'D', 'P', 'N', 'G', 'Q']
  stacks[4] = ['J', 'L', 'H', 'N', 'F']
  stacks[5] = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
  stacks[6] = ['F', 'D', 'B', 'L']
  stacks[7] = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
  stacks[8] = ['G', 'L', 'D']

  with open(fname) as p_input:

    for line in p_input:

      line_elements = line.strip().split(' ')

      move = []
      for i in range(int(line_elements[1])):
        move.append(stacks[int(line_elements[3]) - 1].pop())
      for i in range(int(line_elements[1])):
        stacks[int(line_elements[5]) - 1].append(move.pop())

  result = ''
  for stack in stacks:
    result += stack[len(stack)-1]
  print(result)
  print(stacks)


if __name__ == '__main__':

  #solve_1("p05_input_test")
  solve_1("p05_input")
  #solve_2("p05_input_test")
  solve_2("p05_input")

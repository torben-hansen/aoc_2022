
mappings1 = {
  "X" : 1,
  "Y" : 2,
  "Z" : 3,
}

mappings2 = {
  "X" : 0,
  "Y" : 3,
  "Z" : 6,
}

def result_for_hand_2(hand_1, hand_2):
  if hand_1 == "A":
    if hand_2 == "X":
      return 3
    elif hand_2 == "Y":
      return 6
    elif hand_2 == "Z":
      return 0
  elif hand_1 == "B":
    if hand_2 == "X":
      return 0
    elif hand_2 == "Y":
      return 3
    elif hand_2 == "Z":
      return 6
  elif hand_1 == "C":
    if hand_2 == "X":
      return 6
    elif hand_2 == "Y":
      return 0
    elif hand_2 == "Z":
      return 3


def solve_1(fname):

  result = 0

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip().split(' ')

      result += mappings1[line_stripped[1]] + result_for_hand_2(line_stripped[0], line_stripped[1])

  print('result = {}'.format(result))


def decide_for_hand_2(hand_1, hand_2):
  if hand_1 == "A":
    if hand_2 == "X":
      return 'Z'
    elif hand_2 == "Y":
      return 'X'
    elif hand_2 == "Z":
      return 'Y'
  elif hand_1 == "B":
    if hand_2 == "X":
      return 'X'
    elif hand_2 == "Y":
      return 'Y'
    elif hand_2 == "Z":
      return 'Z'
  elif hand_1 == "C":
    if hand_2 == "X":
      return 'Y'
    elif hand_2 == "Y":
      return 'Z'
    elif hand_2 == "Z":
      return 'X'

def solve_2(fname):

  result = 0

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip().split(' ')

      result += mappings1[decide_for_hand_2(line_stripped[0], line_stripped[1])] + mappings2[line_stripped[1]]


  print('result = {}'.format(result))


if __name__ == '__main__':

  solve_1("p02_input_test")
  solve_1("p02_input")
  solve_2("p02_input_test")
  solve_2("p02_input")

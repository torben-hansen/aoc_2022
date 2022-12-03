
def solve_1(fname):

  result = 0
  set_compartment1 = set()
  set_compartment2 = set() 

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()
      compartment1 = line_stripped[: int(len(line_stripped) / 2)]
      compartment2 = line_stripped[int(len(line_stripped) / 2) :]

      for char in compartment1:
        set_compartment1.add(char)
      for char in compartment2:
        set_compartment2.add(char)

      compartment_intersection = set_compartment1.intersection(set_compartment2)

      for char in compartment_intersection:
        if char.islower():
          result += ord(char) - 97 + 1
        else:
          result += ord(char) - 65 + 27

      set_compartment1.clear()
      set_compartment2.clear()

  print('result = {}'.format(result))


def solve_2(fname):

  result = 0
  iterator = 0
  sets_from_group = [set() for _ in range(3)]

  with open(fname) as p_input:

    for line in p_input:
      iterator += 1
      sets_from_group[iterator % 3].update([char for char in line.strip()]) 
      if iterator % 3 == 0:
        for char in set.intersection(*sets_from_group):
          if char.islower():
            result += ord(char) - 97 + 1
          else:
            result += ord(char) - 65 + 27
        [s.clear() for s in sets_from_group]

  print('result = {}'.format(result))


if __name__ == '__main__':

  solve_1("p03_input_test")
  solve_1("p03_input")
  solve_2("p03_input_test")
  solve_2("p03_input")

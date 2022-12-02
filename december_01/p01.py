
def solve_1(fname):

  elf_counter = 1
  elf_calories_acculator = 0
  elf_max = 1
  elf_max_value = 0

  with open(fname) as p_input:
    
    for line in p_input:
      if line.strip() == "":
        if elf_max_value < elf_calories_acculator:
          elf_max = elf_counter
          elf_max_value = elf_calories_acculator
        
        elf_counter += 1
        elf_calories_acculator = 0
      else:
        elf_calories_acculator += int(line.strip())

    print('elf_max = {}, elf_max_value = {}'.format(elf_max, elf_max_value))

def solve_2(fname):

  elf_calories_acculator = 0
  elf_values = []

  with open(fname) as p_input:

    for line in p_input:
      if line.strip() == "":
        elf_values.append(elf_calories_acculator)
        elf_calories_acculator = 0
      else:
        elf_calories_acculator += int(line.strip())

    sorted_elf_values = sorted(elf_values, reverse=True)
    top_3_max_added = sorted_elf_values[0] + sorted_elf_values[1] + sorted_elf_values[2]

    print('top 3 max added = {}'.format(top_3_max_added))

if __name__ == '__main__':

  solve_1("p01_input_test")
  solve_1("p01_input")
  solve_2("p01_input_test")
  solve_2("p01_input")

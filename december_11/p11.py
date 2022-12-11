import math

class monkey():

  def __init__(self, number, if_true, if_false):
    self.monkey_number = number
    self.items = []
    self.if_true = if_true
    self.if_false = if_false
    self.inspected_items = 0

  def add_item(self, item):
    self.items.append(item)

  def operation(self, worry):
    if self.monkey_number == 0:
      return 7 * worry
    elif self.monkey_number == 1:
      return 11 * worry
    elif self.monkey_number == 2:
      return 8 + worry
    elif self.monkey_number == 3:
      return 7 + worry
    elif self.monkey_number == 4:
      return 5 + worry
    elif self.monkey_number == 5:
      return 4 + worry
    elif self.monkey_number == 6:
      return worry * worry
    elif self.monkey_number == 7:
      return 3 + worry

  def test(self, worry):
    self.inspected_items += 1
    if self.monkey_number == 0:
      return worry % 19
    elif self.monkey_number == 1:
      return worry % 3
    elif self.monkey_number == 2:
      return worry % 13
    elif self.monkey_number == 3:
      return worry % 7
    elif self.monkey_number == 4:
      return worry % 5
    elif self.monkey_number == 5:
      return worry % 11
    elif self.monkey_number == 6:
      return worry % 17
    elif self.monkey_number == 7:
      return worry % 2

def printm(monkeys):
  for m in monkeys:
    print(m.items)

def solve_1(fname):

  monkey_business = 0
  monkeys = [monkey(0, 6, 7), monkey(1, 3, 5), monkey(2, 0, 6), monkey(3, 2, 4), monkey(4, 2, 0), monkey(5, 4, 3), monkey(6, 7, 1), monkey(7, 5, 1)]

  with open(fname) as p_input:

    monkey_counter = 0

    for line in p_input:

      line_stripped = line.strip()

      if 'Starting' in line_stripped:
        items_array = line_stripped[16:].replace(" ", "").split(',')
        for item in items_array:
          monkeys[monkey_counter].add_item(int(item))
        monkey_counter += 1

    for i in range(20):
      for j in range(8):
        counter = 0
        for item in monkeys[j].items:
          item_operated_on = int(math.floor(monkeys[j].operation(item)/3))
          if monkeys[j].test(item_operated_on) == 0:
            monkeys[monkeys[j].if_true].items.append(item_operated_on)
          else:
             monkeys[monkeys[j].if_false].items.append(item_operated_on)
          counter += 1
        for t in range(counter):
          monkeys[j].items.pop(0)

    inspections = []
    for i in range(8):
      inspections.append(monkeys[i].inspected_items)

    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])

def solve_2(fname):

  monkey_business = 0
  monkeys = [monkey(0, 6, 7), monkey(1, 3, 5), monkey(2, 0, 6), monkey(3, 2, 4), monkey(4, 2, 0), monkey(5, 4, 3), monkey(6, 7, 1), monkey(7, 5, 1)]

  with open(fname) as p_input:

    monkey_counter = 0

    for line in p_input:

      line_stripped = line.strip()

      if 'Starting' in line_stripped:
        items_array = line_stripped[16:].replace(" ", "").split(',')
        for item in items_array:
          monkeys[monkey_counter].add_item(int(item))
        monkey_counter += 1

    lcm = 19 * 3 * 13 * 7 * 5 * 11 * 17 * 2

    for i in range(10000):
      for j in range(8):
        counter = 0
        for item in monkeys[j].items:
          item_operated_on = int(monkeys[j].operation(item) % lcm)
          if monkeys[j].test(item_operated_on) == 0:
            monkeys[monkeys[j].if_true].items.append(item_operated_on)
          else:
             monkeys[monkeys[j].if_false].items.append(item_operated_on)
          counter += 1
        for t in range(counter):
          monkeys[j].items.pop(0)


    inspections = []
    for i in range(8):
      inspections.append(monkeys[i].inspected_items)

    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])

if __name__ == '__main__':

  #solve_1("p11_input_test")
  solve_1("p11_input")
  solve_2("p11_input")

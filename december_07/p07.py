
# Not particularly efficient data structure or data structure methods.
# For example, only doesn't need to be able to distinguish between node size
# and subtree size; knowing the total size is sufficient.
class Node:
  def __init__(self, name, parent_node = None):
    self.name = name
    self.child_nodes = []
    self.parent_node = parent_node
    self.node_size = 0 # Size is only files in this node
    self.subtree_size = 0 # Size is of subtree excluding this node

  def add_child_node(self, child_node):
    self.child_nodes.append(child_node)

  def update_subtree_size(self, new_node_size):
    if self.parent_node != None:
      self.parent_node.subtree_size += new_node_size
      self.parent_node.update_subtree_size(new_node_size)

  def command_ls(self, line):
    if 'dir' in line:
      self.add_child_node(Node(line[4:], self))
    else:
      split_line = line.split(' ')
      self.node_size += int(split_line[0])
      self.update_subtree_size(int(split_line[0]))

  def command_cd_dir(self, dir_name):
    for child_node in self.child_nodes:
      if child_node.name == dir_name:
        return child_node

def calculate_recursive_1(node):

  value = 0

  for child_node in node.child_nodes:
    value += calculate_recursive_1(child_node)

  # A node has total size = size of files in this directory + subtree
  if (node.node_size + node.subtree_size) <= 100000:
    value += node.node_size + node.subtree_size

  return value


def calculate_recursive_2(node, required_space, candidates):

  value = 0

  for child_node in node.child_nodes:
    calculate_recursive_2(child_node, required_space, candidates)

  if (node.node_size + node.subtree_size) >= required_space:
    candidates.append(node.node_size + node.subtree_size)


def solve_1_and_2(fname):

  root_node = Node('/')
  current_node = root_node
  ls_state = False

  with open(fname) as p_input:

    for line in p_input:

      line_stripped = line.strip()

      if line_stripped[0] == '$':
        ls_state = False

      if ls_state:
        current_node.command_ls(line_stripped)
        continue

      if '$ cd /' in line_stripped:
        current_node = root_node
      elif '$ cd ..' in line_stripped:
        current_node = current_node.parent_node
      elif '$ cd ' in line_stripped:
        current_node = current_node.command_cd_dir(line_stripped[5:])
      elif '$ ls' in line_stripped:
        ls_state = True
        continue
      else:
        print("Unknown command")
        exit(0)

    print(calculate_recursive_1(root_node))
    candidates = []
    total_size = root_node.node_size + root_node.subtree_size
    calculate_recursive_2(root_node, 30000000 - (70000000 - total_size), candidates)
    print(candidates)
    print(min(candidates))


if __name__ == '__main__':

  solve_1_and_2("p07_input_test")
  solve_1_and_2("p07_input")

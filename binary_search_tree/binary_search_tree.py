import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    pass

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    pass

  # Return the maximum value found in the tree
  def get_max(self):
    pass

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def r_for_each(self, cb):
    pass

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print()
    pass

  # Print the value of every node, starting with the given node,
  # in a breadth first traversal
  def bft_print(node):
    pass

  # Print the value of every node, starting with the given node,
  # in a depth first traversal
  def dft_print(node):
    pass


  ########Stretch Goals#########
  # Note: Research may be required

  # Print In-order DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order DFT
  def post_order_dft(self, node):
    pass
  
# How to think like a computer scientist - learn with Python

# Ch.3
# tryme3.py

def new_line():
  print

def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  # for i in range(25):
  #   print
  #   i += 1
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

clear_screen()
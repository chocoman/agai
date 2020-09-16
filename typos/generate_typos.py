#!/usr/bin/python3
import sys
import random

DELETION_PROBABILITY = 0.1
INSERTION_PROBABILITY = 0.1
CHANGE_PROBABILITY = 0.1

def generate_typos(text):
  modified_text = ''
  for char in text:
    if random.random() < DELETION_PROBABILITY:
      pass
    elif random.random() < INSERTION_PROBABILITY:
      # Insert the correct character and a random character from the
      # input text. 
      modified_text += char + text[random.randint(0, len(text) - 1)]
    elif random.random() < CHANGE_PROBABILITY:
      modified_text += text[random.randint(0, len(text) - 1)]
    else:
      modified_text += char
  return modified_text
  
def convert_file(input_path, output_path):
  with open(input_path, 'r') as input_file:
    with open(output_path, 'w') as output_file:
      for line in input_file:
        print(line)
        modified_line = generate_typos(line[:-1])
        print(modified_line)
        output_file.write(modified_line + '\n')

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print(f'usage: {sys.argv[0]} input.txt output.txt')
    sys.exit(1)
  convert_file(sys.argv[1], sys.argv[2])


def read_schema():
  grid = []
  with open('list.txt', 'r') as f:
    [grid.append(line.strip()) for line in f]
  return grid

def id_special(grid):
  special_char_positions = []
  for line in grid:
    row = []
    [row.append(False) if character == '.' or 58 > ord(character) > 47 else row.append(True) for character in line]
    special_char_positions.append(row)
  return special_char_positions

def check_neighbors(special_chars, radius =1):
  coords = set()
  for i, rows in enumerate(special_chars):
    for j, chars in enumerate(rows):
      if special_chars[i][j]:
        print(i, j)
        for h in range(i-1, i+2):
          for v in range(j-1, j+2):
            coords.add((h, v))
  final_arr = []
  for i in range(0, len(special_chars)):
    row = []
    for j in range(0, len(special_chars[0])):
      if (i, j) in coords:
        row.append(True)
      else:
        row.append(False)
    final_arr.append(row)
  return final_arr

"""a function which takes in lists of random characters and parses valid integers
 to a separate list of the leftmost and rightmost digit's position in the number
 as a tuple, alongside with its numerical value, as in the following:

 Input:

 [['a', '%', '3', '5', '.', '.'],  //needs to find "35", "1", and "416"
 ['1', 'g', '.', '4', '1', '6']]

 Return:

 [
  [(0,2), (0,3), 35],
  [(1, 0), (1, 0), 1],
  [(1, 3), (1, 5), 416]
 ]
 """
def lex_numbers():
  #TODO

  return numbers

grid = read_schema()
special_chars = id_special(grid)
valid_num_positions = check_neighbors(special_chars)
#it's time to define a data structure containing the leftmost point of a number,
#the rightmost point of a number, and the value of the number itself.
#Then its coord check time against the previously constructed bool array!
numbers = get_nums(grid) #tuple of left coords, right coords, value
valid_nums = check_number_validity(numbers, valid_num_positions)
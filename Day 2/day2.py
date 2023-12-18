def get_games():
  games = []
  with open('list.txt', 'r') as f:
    for game in f:
      samples = []
      game = game.split(':')[1]
      for sample in game.split(";"):
        colors = [0, 0, 0]
        for color in sample.split(","):
          channel = 0 #given format RGB, which channel within colors are we adding to?
          match color.split()[1]:
            case "green":
              channel = 1
            case "red":
              channel = 0
            case "blue":
              channel = 2
          colors[channel] = (color.split()[0])
        samples.append(colors)
      games.append(samples)
  return games

def evaluate_game_possible(game):
  for sample in game:
    for index, color in enumerate(sample):
      if(int(color) > 12 + index):
        return False
  return True

def evaluate_game_power(game):
  color_maxes = [1, 1, 1]
  for sample in game:
    for index, color in enumerate(sample):
      if(int(color) > color_maxes[index]):
        color_maxes[index] = int(color)
  return color_maxes[0] * color_maxes[1] * color_maxes[2]

total = 0
games = get_games() #initially populate contents of list in workable format

for index, game in enumerate(games):
  if(evaluate_game_possible(game)): #uses boolean return to determine whetehr to add each index
    total = total + index + 1

print(total)

power = 0

for game in games:
  power = power + evaluate_game_power(game)

print(power)
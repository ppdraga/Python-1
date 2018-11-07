import random

def genGameCard():
  nums = []
  while len(nums) < 15:
    num = random.randrange(1,91)
    if num not in nums:
      nums.append(num)
  print(nums)
  rows = [nums[0:5], nums[5:10], nums[10:15]]
  rows = list(map(sorted, rows))
  # print(rows)

  positions = [random.sample([0,1,2,3,4,5,6,7,8], k = 5),
                random.sample([0,1,2,3,4,5,6,7,8], k = 5),
                random.sample([0,1,2,3,4,5,6,7,8], k = 5)]
  positions = list(map(sorted, positions))
  # print(positions)
  card_rows = [ [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
  idx_row = 0
  while idx_row < 3:
    i = 0
    for idx in positions[idx_row]:
      card_rows[idx_row][idx] = rows[idx_row][i]
      i += 1
    idx_row += 1
  return card_rows

def print_Card(title, card_rows):
  print(' -- {} -- '.format(title))
  for card_row in card_rows:
    print(card_row)

def cutNumFromCard(num, card_rows):
  i = 0
  while i < 3:
    j = 0
    while j < 9:
      if type(card_rows[i][j]) is int and card_rows[i][j] == num:
        card_rows[i][j] = '--'
        return True
      j += 1
    i += 1
  return False

  # for card_row in card_rows:
  #   for card_cell in card_row:
  #     if type(card_cell) is int and card_cell == num:
  #       card_cell = '--'
  #       return True
  # return False

if __name__ == "__main__":



  my_game_card = genGameCard()
  pc_game_card = genGameCard()
  # print_Card('-- Ваша карточка --', my_game_card)
  # print_Card('-- Карточка компьютера --', pc_game_card)
  barrels = []
  nums_left_user = 15
  nums_left_pc = 15
  answer = ''
  while answer != 'q':
    barrel = random.randrange(1,91)
    while barrel in barrels:
      barrel = random.randrange(1,91)
    barrels.append(barrel)
    print('Новый бочонок: {} (осталось {})'.format(barrel, (90 - len(barrels))))
    print_Card('-- Ваша карточка --', my_game_card)
    print_Card('-- Карточка компьютера --', pc_game_card)
    answer = input("Зачеркнуть цифру? (y/n) q - выход : ")
    if answer == 'y':
      if not cutNumFromCard(barrel, my_game_card):
        print("Game is over!")
        break
      else:
        nums_left_user -= 1
    if answer == 'n':
      if cutNumFromCard(barrel, my_game_card):
        print("Game is over!")
        break
    if cutNumFromCard(barrel, pc_game_card):
      nums_left_pc -= 1
    # print(nums_left_user)
    # print(nums_left_pc)
    if nums_left_user == 0:
      print('You are the winner!')
      break
    elif nums_left_pc == 0:
      print("Game is over!")
      break

    
      
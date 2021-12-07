# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

# Namen van de scoorders
scoorder_1 = 'Ruud Gullit'
scoorder_2 = 'Marco van Basten'

# Minuut waarin de goals zijn gemaakt
goal_0 = 32
goal_1 = 54

scorers = f'{scoorder_1} {goal_0}, {scoorder_2} {goal_1}'
# print(scorers)

report = f'{scoorder_1} scored in the {goal_0}nd minute\n{scoorder_2} scored in the {goal_1}th minute'
# print(report)


# Part 2

player = 'Frank Rijkaard'

first_name = player[:player.find(' ')]
# print(first_name)

first_name_len = len(player[:player.find(' ')])
# print(first_name_len)

last_name_len = len(player[player.find(' ')+1:])
# print(last_name_len)

name_short = f"{player[0]}. {player[player.find(' ')+1:]}"
# print(name_short)

chant = (first_name + "! ") * (first_name_len - 1) + (first_name + '!')
# print(chant)

good_chant = chant != chant.rstrip
# print(good_chant)
import copy

player1 = [['A', 'K'], ['Q', 'J']]
player2 = player1
player3 = copy.copy(player1)
player4 = copy.deepcopy(player1)  # 最多複製2層
print(player1, player2, player3, player4)
player1.append('10')
print('round1', player1, player2, player3, player4)
# player3-->[]-->[orig player1]
#
player1[0][0] = '7'
print('round2', player1, player2, player3, player4)
player4[1][0] = 'JOKER'
print('round3', player1, player2, player3, player4)
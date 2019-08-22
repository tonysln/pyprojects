import math
x = int(input('If there are X people in a room, I\'ll find the probability that at least two of them share the same birthday. Enter X = '))
res = (1 - (math.factorial(365)/(math.factorial(365-x)*(365**x))))*100
print(f'The probability that at least two out of {x} people in a room will share the same birthday is {round(res, 2)}%')
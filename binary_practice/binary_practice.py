from random import randint
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def bin_to_num(inp):
    inpList = list(inp)
    decTotal = 0
    i = len(inpList) - 1

    for num in inpList:
        decTotal += int(num) * (2 ** int(i))
        i -= 1
        
    return decTotal


def num_to_bin(n):
    tmp = []
    while n:
        n, i = divmod(n, 2)
        tmp.append(str(i))
    return "".join(tmp[::-1] or "0")


def btd():
    cls()
    print('Convert to decimal! Type \'exit\' to exit or \'dtb\' for decimal-to-binary mode!')
    while True:
        randValue = num_to_bin(randint(1, 255))
        print(randValue)
        inp = input() 
        
        if str(inp) == 'exit':
            break
        elif str(inp) == 'dtb':
            main()
            break
        elif randValue == num_to_bin(int(inp)):
            print('Correct!')
        elif randValue != num_to_bin(int(inp)):
            print('Incorrect! Correct answer:', bin_to_num(randValue))


def main():
    cls()
    print('Convert to binary! Type \'exit\' to exit or \'btd\' for binary-to-decimal mode!')
    while True:
        randValue = randint(1, 255)
        print(randValue)
        inp = input() 
        
        if str(inp) == 'exit':
            break
        elif str(inp) == 'btd':
            btd()
            break
        elif randValue == bin_to_num(inp):
            print('Correct!')
        elif randValue != bin_to_num(inp):
            print('Incorrect! Correct answer:', num_to_bin(randValue))


if __name__ == '__main__':
    main()
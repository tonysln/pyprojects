from random import randint

def convertNum(inp):
    inpList = list(inp)
    decTotal = 0
    i = len(inpList) - 1

    for num in inpList:
        decTotal += int(num) * (2 ** int(i))
        i -= 1
        
    return decTotal

def main():
    print('Convert to binary! Type \'exit\' to exit.')
    while True:
        randValue = randint(1, 255)
        print(randValue)
        inp = input() 
        
        if str(inp) == 'exit':
            break
        elif randValue == convertNum(inp):
            print('Correct!')
        elif randValue != convertNum(inp):
            print('Incorrect!')

if __name__ == '__main__':
    main()
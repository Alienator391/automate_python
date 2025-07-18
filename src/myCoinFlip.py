import random
number_of_streaks = 0

for experiment_number in range(10000):# Run 100,000 experiments total.
    coin=[]  
    for i in range (100): # Code that creates a list of 100 'heads' or 'tails' values

        if random.randint(0,1) == 0:
            coin.append('H')

        else:
            coin.append('T')

    for i in range(len(coin)-6):     # Code that checks if there is a streak of 6 heads or tails in a row
        if 'H' not in coin[i:i+6] or 'T' not in coin[i:i+6]:
            number_of_streaks +=1

print('Chance of streak: %s%%' % (number_of_streaks / 10000))
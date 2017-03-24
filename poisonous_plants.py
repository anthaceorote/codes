'''
    Link to question: https://www.hackerrank.com/challenges/poisonous-plants

    We use 'dead' stack to keep track of dead plants while they are in ascending order. (They were killed by the same last plant).
    'max_dead_days' keeps track of "Last day a plant died" (what we require as our answer)
    'last_alive' is the smallest plant last seen
    'prev' is the plant just before current plant
    
    At last, the plants left alive will be in descending order
    Brute force gives TLE; solution has to be in O(n)
'''

# n = int(input().strip())
# p = list(map(int, input().strip().split(" ")))

inp = "10 2 5 6 10 9 8 7 10 9 5"                    # Ans is 5
inp2 = "20 5 6 15 2 2 17 2 11 5 14 5 10 9 19 12 5"  # Ans is 4
inp3 = "6 5 8 4 7 10 9"                             # Ans is 2
p = list(map(int, inp.strip().split(" ")))

dead = []
max_dead_days = 0
last_alive = float('inf')
prev = 0

for plant in p:
    if not dead:                # If stack is empty
        if plant <= last_alive: # See if I am the smallest plant alive
            last_alive = plant
        elif plant > prev:      # Otherwise see if my previous plant kills me
            dead.append([plant, 1])
        else:                   # Otherwise the smallest alive plant will kill me day after it has killed a plant on max_dead_days
            dead.append([plant, max_dead_days + 1])
    else:                       # If stack is there (there are some dead plants)
        if prev < plant:        # See if my previous plant kills me (I die on first day)
            dead.append([plant, 1])
        else:                   # My previous plant did not kill me; so I die after it
            while dead and dead[-1][0] >= plant:    # If there are dead plants who are >= me, they will not kill me
                last_dead_plant = dead.pop()
                if last_dead_plant[1] > dead_days:  # I will die one day after them, if there is not plant that has dies after that day
                    dead_days = last_dead_plant[1]
                max_dead_days = dead_days if dead_days > max_dead_days else max_dead_days   # Update max_dead_days
            if dead and dead[-1][0] < plant:        # If there is a plant in stack which is smaller than me, I will die after it
                dead.append([plant, dead_days+1])
            elif not dead:                          # If stack is empty, I will be killed by the smallest plant alive
                if plant > last_alive:              # If I am bigger than the smallest plant, I die on the day after a plant before me was killed (it might or might not have been killed by the smallest plant alive, hence the min condition)
                    dead.append([plant, min(max_dead_days+1, dead_days+1)])
                else:                               # I am the smallest plant alive
                    last_alive = plant
    prev = plant
    dead_days = 0
    # print(dead, max_dead_days, last_alive)

while dead: # If there are dead plants, remove to see if they update max_dead_days
    dead_days = dead.pop()[1]
    max_dead_days = dead_days if dead_days > max_dead_days else max_dead_days
    
print(max_dead_days)
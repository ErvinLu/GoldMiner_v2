import random

from GoldMiner_v4 import *

#GLOBAL
stor_pawn_x = []
stor_pawn_y = []
stor_pawn_dir = []

last_x = []
last_y = []

on_beacon = False

direction_level_2 = 0

#LEVEL 2
def level_2(size, pawn_x, pawn_y, maze):

    on_Pit = False

    global on_beacon

    global last_x
    global last_y

    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir

    global direction_level_2

    rand_value = random.randint(1, 2)

    # SCAN MEMORY
    N_mem = scan_level_2(size, pawn_x, pawn_y, maze, 1)  # SAVE SCAN NORTH MEMORY
    S_mem = scan_level_2(size, pawn_x, pawn_y, maze, 2)  # SAVE SCAN SOUTH MEMORY
    E_mem = scan_level_2(size, pawn_x, pawn_y, maze, 3)  # SAVE SCAN EAST MEMORY
    W_mem = scan_level_2(size, pawn_x, pawn_y, maze, 4)  # SAVE SCAN WEST MEMORY

    print("~~~WHAT I SEE~~~")
    print("N: " + N_mem + " | S: " + S_mem+ " | E: " + E_mem+ " | W: " + W_mem)

    if (N_mem == 'G') or (S_mem == 'G') or (E_mem == 'G') or (W_mem == 'G'):
        stor_pawn_x.append(pawn_x)
        stor_pawn_y.append(pawn_y)

        if N_mem == 'G':
            direction_level_2 = 1
            stor_pawn_dir.append(direction_level_2)
        elif S_mem == 'G':
            direction_level_2 = 2
            stor_pawn_dir.append(direction_level_2)
        elif E_mem == 'G':
            direction_level_2 = 3
            stor_pawn_dir.append(direction_level_2)
        elif W_mem == 'G':
            direction_level_2 = 4
            stor_pawn_dir.append(direction_level_2)
        return True

    elif (N_mem == 'B') or (S_mem == 'B') or (E_mem == 'B') or (W_mem == 'B'):
        stor_pawn_x.append(pawn_x)
        stor_pawn_y.append(pawn_y)

        if N_mem == 'B':
            direction_level_2 = 1
            stor_pawn_dir.append(direction_level_2)
        elif S_mem == 'B':
            direction_level_2 = 2
            stor_pawn_dir.append(direction_level_2)
        elif E_mem == 'B':
            direction_level_2 = 3
            stor_pawn_dir.append(direction_level_2)
        elif W_mem == 'B':
            direction_level_2 = 4
            stor_pawn_dir.append(direction_level_2)
        return True

    elif on_Pit and ((N_mem == 'B') or (S_mem == 'B') or (E_mem == 'B') or (W_mem == 'B')):
        if(W_mem == 'B'):
            if pawn_x < size - 1:
                pawn_x = pawn_x + 1
            elif pawn_x > 0:
                pawn_x = pawn_x - 1
            elif pawn_y < size - 1:
                pawn_y = pawn_y + 1
            elif pawn_y > 0:
                pawn_y = pawn_y - 1
        elif(E_mem == 'B'):
            if pawn_x < size - 1:
                pawn_x = pawn_x + 1
            elif pawn_x > 0:
                pawn_x = pawn_x - 1
            elif pawn_y < size - 1:
                pawn_y = pawn_y + 1
            elif pawn_y > 0:
                pawn_y = pawn_y - 1
        elif(S_mem == 'B'):
            if pawn_x < size - 1:
                pawn_x = pawn_x + 1
            elif pawn_x > 0:
                pawn_x = pawn_x - 1
            elif pawn_y < size - 1:
                pawn_y = pawn_y + 1
            elif pawn_y > 0:
                pawn_y = pawn_y - 1
        elif(N_mem == 'B'):
            if pawn_x < size - 1:
                pawn_x = pawn_x + 1
            elif pawn_x > 0:
                pawn_x = pawn_x - 1
            elif pawn_y < size - 1:
                pawn_y = pawn_y + 1
            elif pawn_y > 0:
                pawn_y = pawn_y - 1

    print(on_Pit)

    if maze[pawn_x][pawn_y] == 'G':
        print("Found Gold at", (pawn_x, pawn_y))
        return True  # EXIT WHEN GOLD IS FOUND
    elif maze[pawn_x][pawn_y] == 'P':
        on_Pit = True
        print("Found Pit at", (pawn_x, pawn_y))
        return False  # EXIT WHEN PIT IS STEPPED ON #SET TO FALSE TO AVOID PITS
    elif maze[pawn_x][pawn_y] == 'B':
        on_beacon = True
        print("Found Beacon at", (pawn_x, pawn_y))
        #maze[pawn_x][pawn_y] = 'A'  #BEACON ACTIVATED
        return True #BREAK IF BEACON IS FOUND
    elif maze[pawn_x][pawn_y] == 'V':
        #print("Visited Previously at", (pawn_x, pawn_y))
        return False    #DO NOT TAKE INTO ACCOUNT PREVIOUSLY VISITED NODE

    #MARK VISITED
    maze[pawn_x][pawn_y] = 'V'

    # rand_value = 1

    # EXPLORE NEIGHBORS CLOCKWISE STARTING FROM THE ONE ON THE RIGHT
    if rand_value == 1:  # TOP-DOWN LEFT-RIGHT
        if (pawn_x < len(maze) - 1 and level_2(size, pawn_x + 1, pawn_y, maze)):
            direction_level_2 = 2
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_y > 0 and level_2(size, pawn_x, pawn_y - 1, maze)):
            direction_level_2 = 4
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_x > 0 and level_2(size, pawn_x - 1, pawn_y, maze)):
            direction_level_2 = 1
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_y < len(maze) - 1 and level_2(size, pawn_x, pawn_y + 1, maze)):
            direction_level_2 = 3
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
    elif rand_value == 2:  # RIGHT-LEFT TOP-DOWN
        if (pawn_y < len(maze) - 1 and level_2(size, pawn_x, pawn_y + 1, maze)):
            direction_level_2 = 3
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_x > 0 and level_2(size, pawn_x - 1, pawn_y, maze)):
            direction_level_2 = 1
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_y > 0 and level_2(size, pawn_x, pawn_y - 1, maze)):
            direction_level_2 = 4
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
        if (pawn_x < len(maze) - 1 and level_2(size, pawn_x + 1, pawn_y, maze)):
            direction_level_2 = 2
            # rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            # rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem)
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_2)
            return True
#END LEVEL 2

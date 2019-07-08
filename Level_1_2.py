from GoldMiner_v2 import *

#GLOBAL
stor_pawn_x = []
stor_pawn_y = []
stor_pawn_dir = []

#SCAN
def scan_level_1(size, pawn_x, pawn_y, maze, direction):

    scan_value = 'N'

    if direction == 2:
    #if pawn_x < size - 1:    #SCAN SOUTH
        for i in range(size - pawn_x):
            if maze[pawn_x + i][pawn_y] == 'G':
                scan_value = 'G'
                break
            elif maze[pawn_x + i][pawn_y] == 'P':
                scan_value = 'P'
                break
            elif maze[pawn_x + i][pawn_y] == 'B':
                scan_value = 'B'
                break
            elif maze[pawn_x + i][pawn_y] == 'V':
                scan_value = 'V'
                break

    elif direction == 4:
    #if pawn_y > 0:  #SCAN WEST
        for i in reversed(range(pawn_y)):
            if maze[pawn_x][i] == 'G':
                scan_value = 'G'
                break
            elif maze[pawn_x][i] == 'P':
                scan_value = 'P'
                break
            elif maze[pawn_x][i] == 'B':
                scan_value = 'B'
                break
            elif maze[pawn_x][i] == 'V':
                scan_value = 'V'
                break

    elif direction == 1:
    #if pawn_x > 0:  #SCAN NORTH
        for i in reversed(range(pawn_x)):
            if maze[i][pawn_y] == 'G':
                scan_value = 'G'
                break
            elif maze[i][pawn_y] == 'P':
                scan_value = 'P'
                break
            elif maze[i][pawn_y] == 'B':
                scan_value = 'B'
                break
            elif maze[i][pawn_y] == 'V':
                scan_value = 'V'
                break

    elif direction == 3:
    #if pawn_y < size - 1:   #SCAN EAST
        for i in range(size - pawn_y):
            if maze[pawn_x][pawn_y + i] == 'G':
                scan_value = 'G'
                break
            elif maze[pawn_x][pawn_y + i] == 'P':
                scan_value = 'P'
                break
            elif maze[pawn_x][pawn_y + i] == 'B':
                scan_value = 'B'
                break
            elif maze[pawn_x][pawn_y + i] == 'V':
                scan_value = 'V'
                break

    return scan_value
#END SCAN

#LEVEL 1
def level_1(size, pawn_x, pawn_y, maze, direction):

    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir

    #MOVE
    while(True):

        #EXIT CRITERIA
        if maze[pawn_x][pawn_y] == 'G':
            print("Found Gold at", (pawn_x, pawn_y))
            break   #EXIT WHEN GOLD IS STEPPED ON
        elif (maze[pawn_x][pawn_y] == 'B'):
            print("Found Beacon at", (pawn_x, pawn_y))
            break  # EXIT WHEN GOLD IS STEPPED ON
        elif maze[pawn_x][pawn_y] == 'P':
            print("Found Pit at", (pawn_x, pawn_y))
            break   #EXIT WHEN PIT IS STEPPED ON

        #SCAN MEMORY
        N_mem = scan_level_1(size, pawn_x, pawn_y, maze, 1)  # SAVE SCAN NORTH MEMORY
        S_mem = scan_level_1(size, pawn_x, pawn_y, maze, 2)  # SAVE SCAN SOUTH MEMORY
        E_mem = scan_level_1(size, pawn_x, pawn_y, maze, 3)  # SAVE SCAN EAST MEMORY
        W_mem = scan_level_1(size, pawn_x, pawn_y, maze, 4)  # SAVE SCAN WEST MEMORY

        #GOLD ENCOUNTERS
        if N_mem == 'G':  # RUSH G N
            while maze[pawn_x][pawn_y] != 'G':
                print("RUSHING GOLD NORTH")
                pawn_x = pawn_x - 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(1)
        elif S_mem == 'G':  # RUSH G S
            while maze[pawn_x][pawn_y] != 'G':
                print("RUSHING GOLD SOUTH")
                pawn_x = pawn_x + 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(2)
        elif E_mem == 'G':  # RUSH G E
            while maze[pawn_x][pawn_y] != 'G':
                print("RUSHING GOLD EAST")
                pawn_x = pawn_x
                pawn_y = pawn_y + 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
        elif W_mem == 'G':  # RUSH G W
            while maze[pawn_x][pawn_y] != 'G':
                print("RUSHING GOLD WEST")
                pawn_x = pawn_x
                pawn_y = pawn_y - 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(4)
        #END GOLD ENCOUNTERS

        #BEACON OF HOPE
        elif N_mem == 'B':  # RUSH B N
            while maze[pawn_x][pawn_y] != 'B':
                print("RUSHING BEACON NORTH")
                pawn_x = pawn_x - 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(1)
        elif S_mem == 'B':  # RUSH B S
            while maze[pawn_x][pawn_y] != 'B':
                print("RUSHING BEACON SOUTH")
                pawn_x = pawn_x + 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(2)
        elif E_mem == 'B':  # RUSH B E
            while maze[pawn_x][pawn_y] != 'B':
                print("RUSHING BEACON EAST")
                pawn_x = pawn_x
                pawn_y = pawn_y + 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
        elif W_mem == 'B':  # RUSH B W
            while maze[pawn_x][pawn_y] != 'B':
                print("RUSHING BEACON WEST")
                pawn_x = pawn_x
                pawn_y = pawn_y - 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(4)


    #END MOVE
        #END BEACON ENCOUNTERS

        #PIT OF DESPAIR (RIGHT PRIORITY)
        elif N_mem == 'P' and E_mem == 'V':
            if pawn_y > 0:
                print("PIT NORTH, MOVE LEFT")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x
                pawn_y = pawn_y - 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(4)
        elif W_mem == 'P' and E_mem == 'V':
            if pawn_x > 0:
                print("PIT WEST, MOVE UP")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x - 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(1)
        elif N_mem == 'P':    #PIT TOP, MOVE RIGHT
            #while N_mem == 'P':
            if pawn_y < size - 1:
                print("PIT NORTH, MOVE RIGHT")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x
                pawn_y = pawn_y + 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
                #N_mem = scan_level_1(size, pawn_x, pawn_y, maze, 1)
            elif pawn_y == size - 1:
                print("PIT NORTH, RIGHT IS WALL, PROBABLY TRAPPED")
                #break
        elif S_mem == 'P':  # PIT BOT, MOVE RIGHT
            #while S_mem == 'P':
            if pawn_y < size - 1:
                print("PIT SOUTH, MOVE RIGHT")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x
                pawn_y = pawn_y + 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
                #S_mem = scan_level_1(size, pawn_x, pawn_y, maze, 1)
            elif pawn_y == size - 1:
                print("PIT SOUTH, RIGHT IS WALL, PROBABLY TRAPPED")
                #break
        elif E_mem == 'P':  # PIT RIGHT, MOVE DOWN
            #while E_mem == 'P':
            if pawn_x < size - 1:
                print("PIT EAST, MOVE DOWN")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x + 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
                #E_mem = scan_level_1(size, pawn_x, pawn_y, maze, 1)
            elif pawn_x == size - 1:
                print("PIT EAST, BOTTOM IS WALL, PROBABLY TRAPPED")
                #break
        elif W_mem == 'P':  # PIT LEFT, MOVE DOWN
            #while W_mem == 'P':
            if pawn_x < size - 1:
                print("PIT WEST, MOVE DOWN")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x + 1
                pawn_y = pawn_y
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
                #W_mem = scan_level_1(size, pawn_x, pawn_y, maze, 1)
            # elif pawn_x == size - 1:
            #     print("PIT WEST, BOTTOM IS WALL, PROBABLY TRAPPED")
                #break
        # END PIT ENCOUNTERS

        # GHOSTLY ENCOUNTERS
        elif (W_mem == 'N') or (N_mem == 'N') or (S_mem == 'N') or (E_mem == 'N'):
            if E_mem == 'N' and pawn_y < size - 1:
                print("EAST IS FREE, MOVING RIGHT")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x
                pawn_y = pawn_y + 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(3)
            elif E_mem == 'V' and W_mem == 'N':
                print("SOUTH IS WALL, WEST IS FREE, MOVING WEST")
                maze[pawn_x][pawn_y] = 'V'
                pawn_x = pawn_x
                pawn_y = pawn_y - 1
                stor_pawn_x.append(pawn_x)
                stor_pawn_y.append(pawn_y)
                stor_pawn_dir.append(4)
            elif pawn_y == size - 1:
                if S_mem == 'N' and pawn_x < size - 1:
                    print("EAST IS WALL, SOUTH IS FREE, MOVING SOUTH")
                    maze[pawn_x][pawn_y] = 'V'
                    pawn_x = pawn_x + 1
                    pawn_y = pawn_y
                    stor_pawn_x.append(pawn_x)
                    stor_pawn_y.append(pawn_y)
                    stor_pawn_dir.append(2)
                elif pawn_x == size - 1:
                    if W_mem == 'N' and pawn_y > 0:
                        print("EAST IS WALL, SOUTH IS WALL, WEST IS FREE, MOVING WEST")
                        maze[pawn_x][pawn_y] = 'V'
                        pawn_x = pawn_x
                        pawn_y = pawn_y - 1
                        stor_pawn_x.append(pawn_x)
                        stor_pawn_y.append(pawn_y)
                        stor_pawn_dir.append(4)
                    elif pawn_y == 0:
                        if N_mem == 'N' and pawn_x > 1: #CANNOT GO BACK TO START
                            #print("\nOH NO~ I DIDN'T EXPECT I'LL BE HERE")
                            print("WEST IS WALL, NORTH IS FREE, MOVING NORTH")
                            maze[pawn_x][pawn_y] = 'V'
                            pawn_x = pawn_x - 1
                            pawn_y = pawn_y
                            stor_pawn_x.append(pawn_x)
                            stor_pawn_y.append(pawn_y)
                            stor_pawn_dir.append(1)
                        elif pawn_x == 1:
                            print("\nOH DEAR~ I'M ONE BLOCK UP TO MY STARTING POINT")
                            print("I HAVEN'T SEEN GOLD, IS THERE EVEN GOLD")
                            print("PROBABLY STUCK, SEND HELP")

        # END GHOSTLY ENCOUNTERS
    # END MOVE
#END LEVEL 1

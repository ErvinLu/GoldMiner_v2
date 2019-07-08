import random

#from Level_0 import *
#from Level_1_2 import *
#from Level_2_1 import *
from Level_2_ZeroPlus import *

#GLOBAL
size = 0    #MATRIX SIZE
move_x = 0  #PATH X
move_y = 0  #PATH Y
curr_x = 0  #CURRENT X POSITION AGENT
curr_y = 0  #CURRENT Y POSITION AGENT
gold_x = 0
gold_y = 0
start = (0,0)
end = (0,0)
pit_count = 0
pit_loc = []
beac_loc = []
maze = None #REFERENCE MAZE
init_maze_res = None    #INITIALIZE MAZE RESULT
direction = 0   #AGENT DIRECTION

move_zero = 0

#SCAN
def scan_level_2(size, pawn_x, pawn_y, maze, direction):

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
    return scan_value
#END SCAN

#RUSH GOLD
def rush_gold(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem):
    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir
    # GOLD ENCOUNTERS
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
    elif W_mem == 'G':  # RUSH G W
        while maze[pawn_x][pawn_y] != 'G':
            print("RUSHING GOLD WEST")
            pawn_x = pawn_x
            pawn_y = pawn_y - 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(4)
    elif E_mem == 'G':  # RUSH G E
        while maze[pawn_x][pawn_y] != 'G':
            print("RUSHING GOLD EAST")
            pawn_x = pawn_x
            pawn_y = pawn_y + 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(3)
    # END GOLD ENCOUNTERS
#END RUSH GOLD

#RUSH BEACON
def rush_beacon(pawn_x, pawn_y, maze, N_mem, S_mem, E_mem, W_mem):
    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir
    # BEACON OF HOPE
    if N_mem == 'B':  # RUSH B N
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
    elif W_mem == 'B':  # RUSH B W
        while maze[pawn_x][pawn_y] != 'B':
            print("RUSHING BEACON WEST")
            pawn_x = pawn_x
            pawn_y = pawn_y - 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(4)
    elif E_mem == 'B':  # RUSH B E
        while maze[pawn_x][pawn_y] != 'B':
            print("RUSHING BEACON EAST")
            pawn_x = pawn_x
            pawn_y = pawn_y + 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(3)
    #END BEACON ENCOUNTERS
#END RUSH BEACON

#INITIALIZE MAZE
def init_maze(size, maze):

    global init_maze_res

    #maze is the REFERENCE MAZE VALUE

    #maze[0][0] = '0'  # STARTING POINT AT 0,0 FACING RIGHT
    #maze[0][0] = '→' #STARTING POINT AT 0,0 FACING RIGHT
    maze[0][0] = '↓'  # STARTING POINT AT 0,0 FACING DOWN

    curr_x = 0
    curr_y = 0

    global gold_x
    global gold_y
    global end

    global pit_loc  #FORGOT IF NEEDED 7/2/2019
    global beac_loc  # FORGOT IF NEEDED 7/3/2019

    #GOLD POSITION
    gold_x = int(input("Gold X Location: "))
    gold_y = int(input("Gold Y Location: "))
    end = (gold_x - 1, gold_y - 1)
    maze[gold_x - 1][gold_y - 1] = 'G' #GOLD PLACED AT LOCATION (-1 FOR COMPENSATION)
    #END GOLD POSITION

    #BEACON POSITION
    beacon_count = int(input("Enter number of beacons: "))
    for i in range(beacon_count):
        beacon_x = int(input("Beacon[" + str(i + 1) + "] X Location: "))
        beacon_y = int(input("Beacon[" + str(i + 1) + "] Y Location: "))

        maze[beacon_x - 1][beacon_y - 1] = 'B'

        where_the_beacon = (beacon_x - 1, beacon_y - 1)
        beac_loc.append(where_the_beacon)
    #END BEACON POSITION

    # PIT POSITION
    pit_count = int(input("Enter number of pits: "))
    for i in range(pit_count):
        pit_x = int(input("Pit[" + str(i + 1) + "] X Location: "))
        pit_y = int(input("Pit[" + str(i + 1) + "] Y Location: "))

        maze[pit_x - 1][pit_y - 1] = 'P'

        where_the_pit = (pit_x - 1, pit_y - 1)
        pit_loc.append(where_the_pit)
    # END PIT POSITION
    init_maze_res = maze
#END INITIALIZE MAZE

#DISPLAY MAZE
def display_maze(size, maze):
    for i in maze:
        # print(maze[i],[i]) #CHECK CONTENTS
        print(*i, sep="\t")
# END DISPLAY MAZE

def main():
    global maze
    global start
    global end
    global size

    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir

    size = int(input("Enter playing field size: "))
    maze = [[0 for x in range(size)] for y in range(size)] #INITIALIZE MAZE

    init_maze(size, maze)   #UNCOMMENT TO ASK USER INPUT

    print("INITIAL MAZE")
    display_maze(size, init_maze_res)

    # PROBLEM 1
    # init_maze_res[4][0] = 'B'
    # init_maze_res[0][4] = 'B'
    # init_maze_res[0][3] = 'P'
    # init_maze_res[2][2] = 'P'
    # init_maze_res[2][7] = 'P'
    # init_maze_res[5][2] = 'P'
    # END PROBLEM 1

    # PROBLEM 2
    # init_maze_res[22][0] = 'B'
    # init_maze_res[31][1] = 'B'
    # init_maze_res[21][1] = 'P'
    # init_maze_res[21][1] = 'P'
    # init_maze_res[20][2] = 'P'
    # END PROBLEM 2

    # PROBLEM 3
    # init_maze_res[0][26] = 'B'
    # init_maze_res[8][20] = 'B'
    # init_maze_res[8][17] = 'P'
    # init_maze_res[9][17] = 'P'
    # init_maze_res[10][18] = 'P'
    # init_maze_res[10][19] = 'P'
    # init_maze_res[10][20] = 'P'
    # init_maze_res[1][19] = 'P'
    # END PROBLEM 3

    # PROBLEM 4
    init_maze_res[16][21] = 'B'
    init_maze_res[16][23] = 'B'
    init_maze_res[15][19] = 'P'
    init_maze_res[15][20] = 'P'
    init_maze_res[15][21] = 'P'
    init_maze_res[15][23] = 'P'
    init_maze_res[16][18] = 'P'
    init_maze_res[16][24] = 'P'
    init_maze_res[17][19] = 'P'
    init_maze_res[17][20] = 'P'
    init_maze_res[17][21] = 'P'
    init_maze_res[17][23] = 'P'
    # END PROBLEM 4

    # #LEVEL 2
    global last_x
    global last_y

    global N_mem
    global S_mem
    global E_mem
    global W_mem

    global on_beacon

    rushG = False

    print("*********************************")
    level_2(size, 0, 0, init_maze_res)

    # print(last_x)
    # print(last_y)

    stor_pawn_x.reverse()
    stor_pawn_y.reverse()
    stor_pawn_dir.reverse()

    # print(stor_pawn_x)
    # print(stor_pawn_y)

    for i in range(len(stor_pawn_x)):
        if stor_pawn_dir[i] == 1:
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
        if stor_pawn_dir[i] == 2:
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
        if stor_pawn_dir[i] == 3:
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
        if stor_pawn_dir[i] == 4:
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'

        print("ITERATION", (i))
        display_maze(size, init_maze_res)
        print("*********************************")

    cont_i = len(stor_pawn_x) - 1

    N_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 1)
    S_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 2)
    E_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 3)
    W_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 4)

    print("~~~WHAT I SEE MAIN~~~")
    print("N: " + N_mem + " | S: " + S_mem + " | E: " + E_mem + " | W: " + W_mem)

    if (N_mem == 'G') or (S_mem == 'G') or (E_mem == 'G') or (W_mem == 'G'):
        rushG = True
        rush_gold(stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, N_mem, S_mem, E_mem, W_mem)
        for i in range(len(stor_pawn_x)):
            if stor_pawn_dir[i] == 1:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
            if stor_pawn_dir[i] == 2:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
            if stor_pawn_dir[i] == 3:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
            if stor_pawn_dir[i] == 4:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'

            print("ITERATION", (i))
            display_maze(size, init_maze_res)
            print("*********************************")

    elif (N_mem == 'B') or (S_mem == 'B') or (W_mem == 'B') or (E_mem == 'B'):
        rush_beacon(stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, N_mem, S_mem, E_mem, W_mem)
        #init_maze_res[stor_pawn_x[len(stor_pawn_x) - 1]][stor_pawn_y[len(stor_pawn_y) - 1]] = 'A' #BEACON ACTIVATED
        for i in range(len(stor_pawn_x)):
            if stor_pawn_dir[i] == 1:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
            if stor_pawn_dir[i] == 2:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
            if stor_pawn_dir[i] == 3:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
            if stor_pawn_dir[i] == 4:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'

            print("ITERATION", (i))
            display_maze(size, init_maze_res)
            print("*********************************")

    while init_maze_res[stor_pawn_x[len(stor_pawn_x) - 1]][stor_pawn_y[len(stor_pawn_y) - 1]] != 'G' and not rushG:

        N_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 1)
        S_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 2)
        E_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 3)
        W_mem = scan_level_2(size, stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, 4)

        if (N_mem == 'G') or (S_mem == 'G') or (E_mem == 'G') or (W_mem == 'G'):
            rush_gold(stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, N_mem, S_mem, E_mem, W_mem)

        elif (N_mem == 'B') or (S_mem == 'B') or (W_mem == 'B') or (E_mem == 'B'):
            rush_beacon(stor_pawn_x[len(stor_pawn_x) - 1], stor_pawn_y[len(stor_pawn_y) - 1], init_maze_res, N_mem, S_mem, E_mem, W_mem)
            #init_maze_res[stor_pawn_x[len(stor_pawn_x) - 1]][stor_pawn_y[len(stor_pawn_y) - 1]] = 'A'  # BEACON ACTIVATED

        for i in range(len(stor_pawn_x) - 1):
            if stor_pawn_dir[i] == 1:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
            if stor_pawn_dir[i] == 2:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
            if stor_pawn_dir[i] == 3:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
            if stor_pawn_dir[i] == 4:
                init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'

            print("ITERATION", (i))
            display_maze(size, init_maze_res)
            print("*********************************")

if __name__ == '__main__':
    main()
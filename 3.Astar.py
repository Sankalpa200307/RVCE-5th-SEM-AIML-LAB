def printstate(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j],end=' ')
        print()

def findblank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
    return None

def moveup(state):
    i,j=findblank(state)
    if i>0:
        newstate=[row[:]for row in state]
        newstate[i][j],newstate[i-1][j]=newstate[i-1][j],newstate[i][j]
        return newstate
    return None
def movedown(state):
    i,j=findblank(state)
    newstate=[row[:]for row in state]
    if i<2:
        newstate[i][j],newstate[i+1][j]=newstate[i+1][j],newstate[i][j]
        return newstate
    return None

def moveleft(state):
    i,j=findblank(state)
    newstate=[row[:]for row in state]
    if j>0:
        newstate[i][j],newstate[i][j-1]=newstate[i][j-1],newstate[i][j]
        return newstate
    return None

def moveright(state):
    i,j=findblank(state)
    newstate=[row[:]for row in state]
    if j<2:
        newstate[i][j],newstate[i][j+1]=newstate[i][j+1],newstate[i][j]
        return newstate
    return None

def calculateh(initial,goal):
    h=0
    for i in range(3):
        for j in range(3):
            if initial[i][j]!=goal[i][j]:
                h+=1
    return h

def astar(initial,goal):
    OPEN,CLOSED=[(calculateh(initial,goal),0,initial)],set()
    
    while OPEN:
        f,g,current=min(OPEN)
        OPEN.remove((f,g,current))
        CLOSED.add(tuple(map(tuple,current)))
        
        printstate(current)
        print(" ")
        
        if current==goal:
            print("Goal reached")
            return
        
        for move in [moveup,movedown,moveleft,moveright]:
            successor=move(current)
            
            if successor and tuple(map(tuple,successor)) not in CLOSED:
                OPEN.append((g+1+calculateh(successor,goal),g+1,successor)) 

# Initial and goal states
initial_state = [[1, 2, 3],
                 [4, 7, 5],
                 [6, 0, 8]]
goal_state = [[1, 2, 3],
              [4, 0, 5],
              [6, 7, 8]]

# Run A* search
astar(initial_state, goal_state)
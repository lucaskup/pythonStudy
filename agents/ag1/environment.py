import random
import time
import curses

class Environment:

    def __init__(self):
        self.agents = []
        #1 home, 2 dirty, 3 barrier
        self.ground = [[0,0,2,0,0,2],[0,3,0,0,0,2],[0,0,2,0,3,3],[0,2,3,0,0,2]]
        self.home = (0,0)
        self.agents.append(VcAgent([False,False,True]))
        self.steps = 0


    def doWork(self):
        self.steps += 1
        for a in self.agents:
            homePercept = self.home == a.pos
            dirtyPercept = self.ground[a.pos[0]][a.pos[1]] == 2
            #print(a.pos,str(len(self.ground)),str(len(self.ground[0])))
            touchPercept = a.pos[0] == 0 and a.facing == 2 or a.pos[0] == len(self.ground)-1 and a.facing == 0 or a.pos[1] == 0 and a.facing == 1 or a.pos[1] == len(self.ground[0])-1 and a.facing == 3 or self.ground[a.getMovePos()[0]][a.getMovePos()[1]] == 3
            #print(touchPercept,'touchPercept')
            a.setPercepts([touchPercept,dirtyPercept,homePercept])
            a.evalUtility()
            if not(a.photoSensor) and dirtyPercept:
                self.ground[a.pos[0]][a.pos[1]] = 0

    def showGround(self):

        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        for x in range(len(self.ground)):
            for y in range(len(self.ground[x])):
                rep = str(self.ground[x][y])
                for a in self.agents:
                    if a.pos == (x,y):
                        rep = 'X'
                #print(rep,end=' ')
                stdscr.addstr(y,2*x, rep+" ")
            #print()
        stdscr.addstr(len(self.ground)+2, 0, "Step: "+ str(self.steps))
        stdscr.addstr(len(self.ground)+3, 0, "photoSensor")
        stdscr.addstr(len(self.ground)+4, 0, "touchSensor")
        stdscr.addstr(len(self.ground)+5, 0, "homeSensor")
        stdscr.addstr(len(self.ground)+6, 0, "facing")

        for i in range(len(self.agents)):
            stdscr.addstr(len(self.ground)+2, 12 + 5*i, "AGT "+str(i))
            stdscr.addstr(len(self.ground)+3, 12 + 5*i, "YES" if self.agents[i].photoSensor else "NO ")
            stdscr.addstr(len(self.ground)+4, 12 + 5*i, "YES" if self.agents[i].touchSensor else "NO ")
            stdscr.addstr(len(self.ground)+5, 12 + 5*i, "YES" if self.agents[i].homeSensor else "NO ")
            stdscr.addstr(len(self.ground)+6, 12 + 5*i, str(self.agents[i].mov[self.agents[i].facing])+"º   ")

        stdscr.refresh()



    def envSimulation(self):
        self.showGround()

        flat = [x for sublist in self.ground for x in sublist]
        while 2 in flat :
            time.sleep(0.5)
            self.doWork()
            self.showGround()
            flat = [x for sublist in self.ground for x in sublist]
        curses.echo()
        curses.nocbreak()
        curses.endwin()

class VcAgent(object):
    """docstring for VcAgent."""
    mov = [0,90,180,270]

    def __init__(self, percepts):
        super(VcAgent, self).__init__()
        self.setPercepts(percepts)
        self.facing = 0
        self.pos = (0,0)
        self.prevSteps = []
        self.blockadeGrounds = []
        self.powerUp = True

    def setPercepts(self,percepts):
        self.touchSensor = percepts[0]
        self.photoSensor = percepts[1]
        self.homeSensor = percepts[2]

    def turnRight(self):
        if self.facing >=3:
            self.facing = 0
        else:
            self.facing += 1

    def turnLeft(self):
        if self.facing <= 0:
            self.facing = 3
        else:
            self.facing -= 1

    def getMovePos(self):
        if self.mov[self.facing] == 0:
            return (self.pos[0]+1,self.pos[1])
        elif self.mov[self.facing] == 90:
            return (self.pos[0],self.pos[1]-1)
        elif self.mov[self.facing] == 180:
            return (self.pos[0]-1,self.pos[1])
        else:
            return (self.pos[0],self.pos[1]+1)

    def move(self):
        if self.pos not in self.prevSteps:
            self.prevSteps.append(self.pos)
        self.pos = self.getMovePos()

    """Eval function for agent, choose the best action to be made """
    def evalUtility(self):
        #if road blocked ahead, register in agents knowledge
        if self.powerUp:
            if self.touchSensor and self.getMovePos() not in self.blockadeGrounds:
                self.blockadeGrounds.append(self.getMovePos())

            if self.photoSensor: # if is dirty
                self.photoSensor = False #do cleaning
            #elif self.homeSensor and len(self.prevSteps) == 16: # is in home and size of env
                #self.powerUp = False
    #        elif not self.touchSensor and not self.alreadyGone():
    #            self.move()
            else:
                self.evalWalks()

    def alreadyGone(self):
        return True if self.getMovePos() in self.prevSteps else False

    """ Eval every possible walk """
    def evalWalks(self):
        topUtility = 100
        gonePenalty = 50
        stepPenalty = 10

        possibleMov = []
        facing = self.facing
        pos = self.pos

        #eval move front
        util = topUtility
        if self.alreadyGone():
            util -= gonePenalty
        if self.getMovePos() not in self.blockadeGrounds:
            possibleMov.append((0,util))

        #eval turn left 1 time
        util = topUtility
        self.turnLeft()
        util -= stepPenalty
        if self.alreadyGone():
            util -= gonePenalty
        if self.getMovePos() not in self.blockadeGrounds:
            possibleMov.append((1,util))

        #eval turn left 2 times
        util = topUtility - 2*stepPenalty
        self.turnLeft()
        if self.alreadyGone():
            util -= gonePenalty
        if self.getMovePos() not in self.blockadeGrounds:
            possibleMov.append((2,util))

        #eval turn right 1 times
        util = topUtility - stepPenalty
        self.turnLeft()
        if self.alreadyGone():
            util -= gonePenalty
        if self.getMovePos() not in self.blockadeGrounds:
            possibleMov.append((3,util))

        possibleMov = sorted(possibleMov, key=lambda utl: utl[1], reverse=True)
        #print(possibleMov)
        self.facing = facing
        self.pos = pos

        util = possibleMov[0][1]
        probList = []
        for act in possibleMov:
            if act[1] == util:
                probList.append(act[0])
        do = random.choice(probList)
        if do == 0:
             self.move()
        elif do == 1 or do == 2:
            self.turnLeft()
        else:
            self.turnRight()

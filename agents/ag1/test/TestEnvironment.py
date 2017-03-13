from environment import Environment
from nose.tools import assert_equals
from nose.tools import assert_not_equal

#simple cleaning
def test_01():
    e = Environment()
    e.ground = [[0,0,2,0],[2,0,0,0],[0,0,2,0],[0,2,0,0]]
    e.doWork()
    e.doWork()
    assert_equals(e.ground[1][0],0)
    e.doWork()
    assert_not_equal(e.agents[0].pos,(1,0))

#corner turn around
def test_02():
    e = Environment()
    e.ground = [[0,0,2,0],[3,0,0,0],[0,0,2,0],[0,2,0,0]]
    e.agents[0].facing = 1
    e.agents[0].prevSteps.append((0,1))
    e.agents[0].blockadeGrounds.append((1,0))
    #Assert initial position
    assert_equals(e.agents[0].pos,(0,0))

    #Assert couldnt move but started turning
    e.doWork()
    assert_equals(e.agents[0].pos,(0,0))
    assert_equals(e.agents[0].facing,2)

    #Assert couldnt move but finished turning
    e.doWork()
    assert_equals(e.agents[0].pos,(0,0))
    assert_equals(e.agents[0].facing,3)

    #Assert got out from previous walked path
    e.doWork()
    assert_equals(e.agents[0].pos,(0,1))
    assert e.agents[0].pos in e.agents[0].prevSteps

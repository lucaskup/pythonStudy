from environment import VcAgent
from nose.tools import assert_equals

#simple move straight ahead test
def test_01():
    a = VcAgent([False,False,True])
    a.evalUtility()
    assert_equals(a.pos,(1,0))

#simple clean straight ahead test
def test_02():
    a = VcAgent([False,True,True])
    a.evalUtility()
    assert_equals(a.photoSensor,False)

#simple turn test
def test_03():
    a = VcAgent([True,False,True])
    a.evalUtility()
    assert a.mov[a.facing] in (90,270)
    a = VcAgent([True,False,True])
    a.evalUtility()
    assert a.mov[a.facing] in (90,270)
    a = VcAgent([True,False,True])
    a.evalUtility()
    assert a.mov[a.facing] in (90,270)

#turn around test
def test_04():
    a = VcAgent([False,False,True])
    a.prevSteps = [(0,1),(2,1),(1,2)]
    a.pos = (1,1)
    a.facing = 3
    a.evalUtility()
    #print(a.facing,a.pos)
    a.evalUtility()
    #print(a.facing,a.pos)
    #assert if its facing right side
    assert_equals(a.mov[a.facing],90)
    #it should have taken two turns to turn so pos is the same
    assert_equals(a.pos,(1,1))

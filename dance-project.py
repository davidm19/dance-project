from Myro import *
init("sim")

def tetrisFast25():
    forward(3,1.25)
    stop()
    turnLeft(3,1.25)
    forward(3,1.25)
    turnRight(10,3)
    backward(3,1.25)
    stop()
    turnLeft(20,1)
    forward(3,1.25)
    stop(), turnRight(10,1)
    backward(3,1.25)
    stop()

tetrisFast25() #put it in a loop
tetrisFast25()

def tetrisSlow13():
    forward(3,.75)
    turnRight(1.5,.75)
    backward(3,.75)
    turnLeft(2,.75)
    backward(3,.75)
    backward(2,.75)
    turnRight(3.5,.75)
    
tetrisSlow13()
tetrisSlow13()

tetrisFast25()

tetrisSlow13()

def tetrisFast6():
    forward(3,.5)
    turnLeft(5,.2)
    turnRight(5,.2)
    turnLeft(5,.2)
    backward(4,.2)
    backward(4,.2)
    backward(4,.2)
    turnLeft(3,.2)
    turnRight(3,.2)
    turnLeft(7.5,.2)
    backward(4,1)
    turnLeft(3,.2)
    turnRight(3,.2)
    forward(2,2.5)

tetrisFast6()

from Myro import *
init("sim")

def dance(movement):
    return movement
    
tetrisFast25Half1 = [forward(3,1.25), stop(), turnLeft(3,1.25), forward(3,1.25), turnRight(10,3), backward(3,1.25), stop(), turnLeft(20,1), forward(3,1.25), stop(), turnRight(10,1), backward(3,1.25), stop()]
tetrisFast25Half2 = [forward(3,1.25), stop(), turnLeft(3,1.25), forward(3,1.25), turnRight(10,3), backward(3,1.25), stop(), turnLeft(20,1), forward(3,1.25), stop(), turnRight(10,1), backward(3,1.25), stop()]
tetrisFast25 = {tetrisFast25Half1, tetrisFast25Half2}
dance(tetrisFast25)

tetrisSlow13Half1 = [forward(3,.75), turnRight(1.5,.75), backward(3,.75), turnLeft(2,.75), backward(3,.75), backward(2,.75), turnRight(3.5,.75)]
tetrisSlow13Half2 = [forward(3,.75), turnRight(1.5,.75), backward(3,.75), turnLeft(2,.75), backward(3,.75), turnLeft(2,.25), turnRight(2,.25), turnLeft(2,.25), backward(3,.5), forward(4,1), stop()]
tetrisSlow13 = {tetrisSlow13Half1, tetrisSlow13Half2}
dance(tetrisSlow13)

dance(tetrisFast25)

dance(tetrisSlow13)

<<<<<<< HEAD
tetrisFast6 = [forward(3,.5), turnLeft(5,.2), turnRight(5,.2), turnLeft(5,.2), backward(4,.2), backward(4,.2), backward(4,.2), turnLeft(3,.2), turnRight(3,.2), turnLeft(7.5,.2), backward(4,1), turnLeft(3,.2), turnRight(3,.2), forward(2,2.5)]
dance(tetrisFast6)
=======
tetrisFast6 = [forward(3,.5), turnLeft(5,.2), turnRight(5,.2), turnLeft(5,.2), backward(4,.2), backward(4,.2), turnLeft(3,.2), turnRight(3,.2), turnLeft(7.5,.2), backward(4,1), turnLeft(3,.2), turnRight(3,.2), forward(2,2.5)]
dance(tetrisFast6)
>>>>>>> f9e4b7d5bc8a398c088c55a28d841dd2572e6272

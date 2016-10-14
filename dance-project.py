from Myro import *
init("sim")

def dance(movement):
    return movement
    
tetrisFast25Half1 = [forward(3,1.25), stop(), turnLeft(3,1.25), forward(3,1.25), turnRight(10,3), backward(3,1.25), stop(), turnLeft(20,1), forward(3,1.25), stop(), turnRight(10,1), backward(3,1.25), stop()]
tetrisFast25Half2 = [forward(3,1.25), stop(), turnLeft(3,1.25), forward(3,1.25), turnRight(10,3), backward(3,1.25), stop(), turnLeft(20,1), forward(3,1.25), stop(), turnRight(10,1), backward(3,1.25), stop()]
tetrisFast25 = {tetrisFast25Half1, tetrisFast25Half2}
dance(tetrisFast25)

tetrisSlow13 = []
dance(tetrisSlow13)

tetrisFast27 = []
dance(tetrisFast27)

tetrisSlow12 = []
dance(tetrisSlow12)

tetrisFast6 = []
dance(tetrisFast6)
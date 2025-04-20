import numpy as np
import matplotlib.pyplot as plt

def randomWalkPath(steps):
    stepsArray=np.zeros(steps)
    for i in range(steps):
        stepsArray[i]=np.random.choice([-1,1])
    path=np.cumsum(stepsArray)
    return path

def pathPlot(path):
    plt.plot(path,color='green')
    plt.title("Random Walk Path")
    plt.xlabel("Steps")
    plt.ylabel("Position")
    plt.show()
    
def allRandomWalksPaths(steps,simulations):
    allPaths=np.zeros((simulations,steps))
    for i in range(simulations):
         path=randomWalkPath(steps)
         allPaths[i]=path
    return allPaths
    
def allPathsPlots(allPaths):
    for path in allPaths:
        plt.plot(path)
    plt.xlabel("Steps")
    plt.ylabel("Position")
    plt.title("Random Walk Paths")
    plt.show()

def histPlot(allPaths):
    finalPositions=allPaths[:,-1]
    plt.hist(finalPositions,bins=30,density=False,color='green')
    plt.title("Histograms of Final Positions")
    plt.xlabel("Final Position")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()
 

def main():
    steps=int(input("Dwse plithos vhmatwn: \n"))
    simulations=int(input("Dwse plithos prosomoiwsewn: \n"))
    
    pathOneParticle=randomWalkPath(steps)
    pathPlot(pathOneParticle)
    
    pathMultipleParticles=allRandomWalksPaths(steps,simulations)
    allPathsPlots(pathMultipleParticles)
    
    histPlot(pathMultipleParticles)
    
if __name__=="__main__":
   main()

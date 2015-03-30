#########################################
# Title: Circuit Solver                 #
# Filename: solver_cs_jb.py             #
# Authors: Jon Beaulieu, Chloe Sackier  #
# Most Recent Edit: 3/28/2014	        #
#########################################

#Basic class definitions#

class component:                        #Every component has two terminals, voltages at said nodes
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.vnode1 = 0
        self.vnode2 = 0

class battery(component):               #Batteries feature a voltage characteristic
    def __init__(self, voltage):
        self.voltage = voltage

class resistor(component):              #Resistors feature a resistance characteristic
    def __init__(self, resistance):
        self.resistance = resistance

def search(node, listName, listItem):
    for i in range(batteries):
        if batteries[i].node1 == node && not(listname=="batteries" && listItem==i):
            return "batteries",i,1
        elif batteries[i].node2 == node && not(listname=="batteries" && listItem==i):
            return "batteries",i,2
            
    for i in range(resistors):
        if resistors[i].node1 == node && not(listname=="resistors" && listItem==i):
            return "resistors",i,1
        elif resistor[i].node2 == node && not(listname=="resistors" && listItem==i):
            return "resistor",i,2

batteries = []
resistors = []

b = input("Number of batteries: ")
r = input("Number of resistors: ")

for i in range(b):                  
    newBat = input("Battery info as Node1, Node2, Volts: ")
    batteries.append(battery(newBat[0], newBat[1], newBat[2])

for i in range(r):
    newRes = input("Resistor info as Node1, Node2, Resistance: ")
    resistors.append(resistor(newRes[0], newRes[1], newRes[2])
    
totalBat = 0

for i in batteries
    totalBat += bat.voltage
    
totalRes = 0

for i in resistors
    totalRes += res.resistance
#\_-O-_/
I = totalBat / totalRes

for i in batteries:

for i in resistors:
    voltdrop = I * resistance

A = matrix( [[0, 0, 1, -1], [0, -resistance, 1, -1], [1, 1, 0, 0], [0, 0, 0, 1]] )
b = matrix( [[voltage], [0], [0], [0]] )
x = np.solve(A, b)                     #To solve matrix equation Ax=b

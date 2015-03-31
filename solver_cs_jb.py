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
    def __init__(self, node1, node2, voltage):
        self.voltage = voltage
        self.node1 = node1
        self.node2 = node2
        self.vnode1 = 0
        self.vnode2 = 0

class resistor(component):              #Resistors feature a resistance characteristic
    def __init__(self, node1, node2, resistance):
        self.resistance = resistance
        self.node1 = node1
        self.node2 = node2
        self.vnode1 = 0
        self.vnode2 = 0

def search(node, listName, listItem):
    for i in range(len(batteries)):
        if batteries[i].node1 == node and not(listName=="batteries" and listItem==i):
            return "batteries",i,1
        elif batteries[i].node2 == node and not(listName=="batteries" and listItem==i):
            return "batteries",i,2
            
    for i in range(len(resistors)):
        if resistors[i].node1 == node and not(listName=="resistors" and listItem==i):
            return "resistors",i,1
        elif resistors[i].node2 == node and not(listName=="resistors" and listItem==i):
            return "resistors",i,2

batteries = []
resistors = []

b = input("Number of batteries: ")
r = input("Number of resistors: ")

for i in range(b):                  
    newBat = input("Battery info as Node1, Node2, Volts: ")
    batteries.append(battery(newBat[0], newBat[1], newBat[2]))

for i in range(r):
    newRes = input("Resistor info as Node1, Node2, Resistance: ")
    resistors.append(resistor(newRes[0], newRes[1], newRes[2]))

startNode="I didn't find nothin"

for i in range(len(batteries)):
    if search(batteries[i].node1, "batteries", i)[0] == "resistors":
        startNode = "battery",i,1,batteries[i].node1
        break
    elif search(batteries[i].node2, "batteries", i)[0] == "resistors":
        startNode = "battery",i,2,batteries[i].node2
        break

print startNode

totalBat = 0

for i in range(len(batteries)):
    totalBat += batteries[i].voltage

totalRes = 0

for i in range(len(resistors)):
    totalRes += resistors[i].resistance
#\_-O-_/
I = totalBat / totalRes

for i in batteries:
    pass

#for i in range(len(resistors)):
#    voltdrop = I * resistance


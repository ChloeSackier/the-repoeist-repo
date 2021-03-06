#########################################
# Title: Circuit Solver                 #
# Filename: solver_cs_jb.py             #
# Authors: Jon Beaulieu, Chloe Sackier  #
# Most Recent Edit: 3/28/2014	        #
#########################################

#Basic class definitions#

import numpy

class component:                        #Every component has two terminals, voltages at said nodes
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

class battery(component):               #Batteries feature a voltage characteristic
    def __init__(self, node1, node2, voltage):
        self.voltage = voltage
        self.node1 = node1
        self.node2 = node2

class resistor(component):              #Resistors feature a resistance characteristic
    def __init__(self, node1, node2, resistance):
        self.resistance = resistance
        self.node1 = node1
        self.node2 = node2

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

dimension = 2*b + r - 2

A = numpy.zeros(shape=(dimension,dimension))

#X = numpy.matrix

for i in range(b):                  
    newBat = input("Battery info as Node1, Node2, Volts: ")
    batteries.append(battery(newBat[0], newBat[1], newBat[2]))

for i in range(r):
    newRes = input("Resistor info as Node1, Node2, Resistance: ")
    resistors.append(resistor(newRes[0], newRes[1], newRes[2]))

nodeLists = []

for batt in batteries:
    if ((str(batt.node1)) not in nodeLists):
        nodeLists.append(str(batt.node1))

    if ((str(batt.node2)) not in nodeLists):
        nodeLists.append(str(batt.node2))

for res in resistors:
    if ((str(res.node1)) not in nodeLists):
        nodeLists.append(str(res.node1))

    if ((str(res.node2)) not in nodeLists):
        nodeLists.append(str(res.node2))

gndNode = input("Which node should be ground? ")

nodeLists.remove(str(gndNode))

index = 0
for i in nodeLists:
    for batt in batteries:
        if batt.node1 == int(i) or batt.node2 == int(i):
            if(batt.node1 == int(i)):
                temp = A[dimension + batteries.index(batt) - 1]
                col = nodeLists.index(str(batt.node1))
                temp[col] += 1
                A[dimension + batteries.index(batt) - 1] = temp

                if str(batt.node2) in nodeLists:
                    temp = A[dimension + batteries.index(batt) - 1]
                    col = nodeLists.index(str(batt.node2))
                    temp[col] -= 1
                    A[dimension + batteries.index(batt) - 1] = temp
            else:
                temp = A[dimension + batteries.index(batt) - 1]
                col = nodeLists.index(str(batt.node2))
                temp[col] += 1
                A[dimension + batteries.index(batt) - 1] = temp

                if str(batt.node1) in nodeLists:
                    temp = A[dimension + batteries.index(batt) - 1]
                    col = nodeLists.index(str(batt.node1))
                    temp[col] -= 1
                    A[dimension + batteries.index(batt) - 1] = temp               
            
            temp = A[index]
            temp[dimension + batteries.index(batt) - 1] += 1
            A[index] = temp

    for res in resistors:
        if res.node1 == int(i) or res.node2 == int(i):
            if str(res.node1) in nodeLists:
                temp = A[index]
                col = nodeLists.index(str(res.node1))
                if(res.node1 == int(i)):
                    temp[col] += 1.0/(res.resistance)
                else:
                    temp[col] -= 1.0/(res.resistance) 
                A[index] = temp

            if str(res.node2) in nodeLists:
                temp = A[index]
                col = nodeLists.index(str(res.node2))
                if(res.node2 == int(i)):
                    temp[col] += 1.0/(res.resistance)
                else:
                    temp[col] -= 1.0/(res.resistance) 
                A[index] = temp
            
    index+=1

l = numpy.zeros(shape=(dimension,1))
offset = b + r - 2
for i in range(len(batteries)):
    l[i + offset] = [batteries[i].voltage]
x = numpy.linalg.solve(A, l)

print x

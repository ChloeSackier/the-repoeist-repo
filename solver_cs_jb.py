#########################################
# Title: Circuit Solver                 #
# Filename: solver_cs_jb.py             #
# Authors: Jon Beaulieu, Chloe Sackier  #
# Most Recent Edit: 3/28/2014	        #
#########################################

#Basic class definitions#

class component:                        #Every component has two terminals
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

class battery(component):               #Batteries feature a voltage characteristic
    def __init__(self, voltage):
        self.voltage = voltage

class resistor(component):              #Resistors feature a resistance characteristic
    def __init__(self, resistance):
        self.resistance = resistance

batteries = []
resistors = []

b = input("Number of batteries: ")
r = input("Number of resistors: ")

for i in range(b):
    newBat = input("Battery info as Node1, Node2, Volts: ")
    batteries.append(battery(newBat[1], newBat[2], newBat[3])


A = matrix( [[0, 0, 1, -1], [0, -resistance, 1, -1], [1, 1, 0, 0], [0, 0, 0, 1]] )
b = matrix( [[voltage], [0], [0], [0]] )
x = np.solve(A, b)                     #To solve matrix equation Ax=b

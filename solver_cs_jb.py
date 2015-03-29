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
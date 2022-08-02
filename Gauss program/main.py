
# At this mini project i just wanna create some program
# which help me count all currents of the circuit using the Gauss method.
U=110
# First step its counting conductivity using file of resistance
#At file im writing all resistances of my scheme
class FileReader():
    '''Class for file reading,exactly resistence'''
    def __init__(self, path_to_file):
        self.path_fo_file = path_to_file
        self.resistance_list = []

    def appending_to_list(self):
        with open(self.path_fo_file, 'r') as file:
            for elem in file.readlines()[1:]:
                self.resistance_list.append(elem[:-1])
        return self.resistance_list

class Conductivity():
    '''Class for counting conductivity of circle'''
    def __init__(self,resistance_list):
        self.resistance_list=resistance_list
        self.conductivity_list=[]
        self.intrinsic_conductivities_list=[]
    def calculation(self):
        for elem in self.resistance_list:
            self.conductivity_list.append(1/complex(str(elem.split("=")[1])))
        return self.conductivity_list
    def intrinsic_conductivities_calc(self):
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[0]+self.conductivity_list[4]+self.conductivity_list[5]))
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[1]+self.conductivity_list[4]+self.conductivity_list[6]))
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[2]+self.conductivity_list[6]))
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[3]+self.conductivity_list[5]))
        return self.intrinsic_conductivities_list
Z = FileReader("Z")
z_list=Z.appending_to_list()
y=Conductivity(z_list)
y_conductive=y.calculation()
y_intrinsic=y.intrinsic_conductivities_calc()
print(y_conductive)
print(y_intrinsic)
#Started analizing and counting exactly Gaus method
#Formed a matrix of wet conductivities and mutual conductivities of nodes
#calculation  scheme

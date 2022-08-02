# At this mini project i just wanna create some program
# which help me count all currents of the circuit using the Gauss method.

# At this task i get value of voltage (U) and value of сalculation accuracy (E)
# I`m already proected all matrix what i need
U = 110
Ubp = 116
E = 0.01


# First step its counting conductivity using file of resistance
# At file im writing all resistances of my scheme
class FileReader():
    '''Class for file reading,exactly resistence'''

    def __init__(self, path_to_file):
        self.path_fo_file = path_to_file
        self.resistance_list = []
        self.list_of_load = []

    def appending_to_list(self):
        with open(self.path_fo_file, 'r') as file:
            if self.path_fo_file == "Z":
                for elem in file.readlines()[1:]:
                    self.resistance_list.append(elem[:-1])
            else:
                for elem in file.readlines()[1:]:
                    self.list_of_load.append(complex(str(elem.split("=")[1])))
        return self.resistance_list if self.path_fo_file == "Z" else self.list_of_load


class Conductivity():
    '''Class for counting conductivity of circle'''

    def __init__(self, resistance_list):
        self.resistance_list = resistance_list
        self.conductivity_list = []
        self.intrinsic_conductivities_list = []

    def calculation(self):
        for elem in self.resistance_list:
            self.conductivity_list.append(1 / complex(str(elem.split("=")[1])))
        return self.conductivity_list

    def intrinsic_conductivities_calc(self):
        self.intrinsic_conductivities_list.append(
            -(self.conductivity_list[0] + self.conductivity_list[4] + self.conductivity_list[5]))
        self.intrinsic_conductivities_list.append(
            -(self.conductivity_list[1] + self.conductivity_list[4] + self.conductivity_list[6]))
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[2] + self.conductivity_list[6]))
        self.intrinsic_conductivities_list.append(-(self.conductivity_list[3] + self.conductivity_list[5]))
        return self.intrinsic_conductivities_list


Z = FileReader("Z")
S = FileReader("S")
s_list = S.appending_to_list()
# print(s_list)
z_list = Z.appending_to_list()
y = Conductivity(z_list)
y_conductive = y.calculation()
y_intrinsic = y.intrinsic_conductivities_calc()
# print(y_conductive)
# print(y_intrinsic)
# print(y_intrinsic)
# Started analizing and counting exactly Gaus method
# Formed a matrix of wet conductivities and mutual conductivities of nodes
# calculation  scheme
y_11 = y_intrinsic[0]
y_12 = y_conductive[4]
y_13 = 0
y_14 = y_conductive[5]
y_21 = y_conductive[4]
y_22 = y_intrinsic[1]
y_23 = y_conductive[6]
y_24 = 0
y_31 = 0
y_32 = y_conductive[6]
y_33 = y_intrinsic[2]
y_34 = 0
y_41 = y_conductive[5]
y_42 = 0
y_43 = 0
y_44 = y_intrinsic[3]
U1 = U2 = U3 = U4 = 110
# J_elem=(S_elem/U_elem)-y_index_el*U0(116) Otherwise:
J1 = (s_list[0] / U1) - y_conductive[0] * 116
J2 = (s_list[1] / U2) - y_conductive[1] * 116
J3 = (s_list[2] / U3) - y_conductive[2] * 116
J4 = (s_list[3] / U4) - y_conductive[3] * 116
# print(J1, J2, J3, J4)
# I form a matrix that will need to be iterated until we reach the specified accuracy
# and write this on file to see that
with open("matrix", "w") as file:
    file.write(f'|{y_11} {y_12} {y_13} {y_14}|    |{U1}|     |{J1}|\n'
               f'|{y_21} {y_22} {y_23} {y_24}|   *  |{U2}|  =  |{J2}|\n'
               f'|{y_31} {y_32} {y_33} {y_34}|                                               |{U3}|     |{J3}|\n'
               f'|{y_41} {y_42} {y_43} {y_44}|                                            |{U4}|     |{J4}|')
# Third step.Im starting iteration calculating until we get diagonal matrix
# iteration=1
# while y_11 != 1: #put y_44!=1
#     y_12 = y_12 / y_11
#     y_13 = y_13 / y_11
#     y_14 = y_14 / y_11
#     J1 = J1 / y_11
#     y_11 = y_11 / y_11
#     # Need to recalculating row with new data.Starting from second row
#     y_22 = y_22 - y_21 * y_12
#     y_23 = y_23 - y_21 * y_13
#     y_24 = y_24 - y_21 * y_14
#     J2 = J2 - y_21 * J1
#     y_21 = y_21 - y_21 * y_11
#     # 3 row
#     y_32 = y_32 - y_31 * y_12
#     y_33 = y_33 - y_31 * y_13
#     y_34 = y_34 - y_31 * y_14
#     J3 = J3 - y_31 * J1
#     y_31 = y_31 - y_31 * y_11
#     # 4 row
#     y_42 = y_42 - y_41 * y_12
#     y_43 = y_43 - y_41 * y_13
#     y_44 = y_44 - y_41 * y_14
#     J4 = J4 - y_41 * J1
#     y_41 = y_41 - y_41 * y_11
#     iteration+=1
    #Нужно пройти 4 раза,нужно придумать как это сделать в цикле
# print(y_11, y_12, y_13, y_14, y_21, y_22, y_23, y_24, y_31, y_32, y_33, y_34, y_41, y_42, y_43, y_44 )
# print(J1,J2,J3,J4)








# While im thinking how to loop Iteration of method Gauss i`m start to writing Zeydel
# method to compare finish variables. This method much easier than firs.

i=1
e=100
old_u1,old_u2,old_u3,old_u4=110,110,110,110
while e>E:
    U1 = 1 / y_intrinsic[0] * ((s_list[0] / U1) - y_12 * U2 - y_14 * U4 - y_conductive[0] * 116)
    U2 = 1 / y_intrinsic[1] * ((s_list[1] / U2) - y_21 * U1 - y_23 * U3 - y_conductive[1] * 116)
    U3 = 1 / y_intrinsic[2] * ((s_list[2] / U3) - y_32 * U2 - y_conductive[2] * 116)
    U4 = 1 / y_intrinsic[3] * ((s_list[3] / U4) - y_41 * U1 - y_conductive[3] * 116)
    e=max([U1.real-old_u1.real,U2.real-old_u2.real,U3.real-old_u3.real,U4.real-old_u4.real])
    old_u1, old_u2, old_u3, old_u4=U1.real+-U1.imag*1j, U2.real+-U2.imag*1j, U3.real+-U3.imag*1j, U4.real+-U4.imag*1j
    print("Iteration: ",i)
    i+=1
# After iteration we find all currents of scheme I_ij=(Ui-Uj)*y_ij
I_01=(116-U1)*y_conductive[0]
I_02=(116-U2)*y_conductive[1]
I_03=(116-U3)*y_conductive[2]
I_04=(116-U4)*y_conductive[3]
I_12=(U2-U1)*y_12
I_14=(U4-U1)*y_14
I_23=(U3-U2)*y_23
#Finish first method,need time to thinkin how solve Gauss method(iteration exactly)


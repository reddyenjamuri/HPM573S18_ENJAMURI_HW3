class Patient:

    def __init__(self, number, cost):
        self.number = number
        self.cost = cost

    def discharge(self):
        """abstract method"""

class EmergencyPatient(Patient):
    def __init__(self, number, cost):
        Patient.__init__(self, number, cost)
        print("Emergency patient")

class HospitalizedPatient(Patient):
    def __init__(self, number, cost):
        Patient.__init__(self, number, cost)
        print("Hosptialized patient")

class Hospital(Patient):
    def __init__(self, patients, cost, admit, discharge, get_total_cost):
        Patient.__init__(self, patients, cost):

        def patients(self):
            """storing the patient"""

        def cost(self):
            if HospitalizedPatient:
                exp_cost = 2000
            elif EmergencyPatient:
                exp_cost = 1000
            return exp_cost

        def admit(self):

        def discharge(self):

        def get_total_cost(self):
            exp_cost = self.cost

            total_cost=0
            i=0
            total_cost += exp_cost[i]
            i+=1
            return exp_cost

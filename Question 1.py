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
    def __init__(self, cost, discharge, get_total_cost):
        Patient.__init__(self, cost):

        def cost(self):
            if HospitalizedPatient:
                exp_cost = 2000
            elif EmergencyPatient:
                exp_cost = 1000
            return exp_cost

        def discharge(self):

        def get_total_cost(self):
            exp_cost = self.cost

            total_cost=0
            i=0
            total_cost += exp_cost[i]
            i+=1
            return exp_cost

            def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost


def get_expected_costs(self):

         exp_cost = self.costs
         exp_cost = 0 # the expected cost of this node
         i = 0 #index to iterate over probabilities
         for thisNode in self.future_nodes:
             if type(thisNode) == ChanceNode:
                exp_cost += thisNode.get_expected_cost() * self.probs[i]
            elif type(thisNode) == TerminalNode:
                exp_cost += thisNode.get_cost*() * self.probs [i]

        num_outcomes = len(self.probs)
        expected_costs = 0
        for i in range(num_outcomes):
        expected_costs += self.probs[i] * self.costs[i]

"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=0, hours_worked=0, hourly_wage=0, commission=0, bonus=0, contracts_landed=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage
        self.commission = commission
        self.bonus = bonus
        self.contracts_landed = contracts_landed

    def get_pay(self):
        if self.contract_type == "salary":
            total_pay = self.salary
        elif self.contract_type == "hourly":
            total_pay = self.hours_worked * self.hourly_wage
        else:
            total_pay = 0

        total_pay += self.calculate_commission()

        return total_pay

    def calculate_commission(self):
        if self.contract_type == "salary" and self.bonus > 0:
            return self.bonus
        elif self.contract_type == "hourly" and self.bonus > 0:
            return self.bonus
        elif self.contract_type == "salary" and self.contracts_landed > 0:
            return self.contracts_landed * self.commission
        elif self.contract_type == "hourly" and self.contracts_landed > 0:
            return self.contracts_landed * self.commission
        else:
            return 0

    def __str__(self):
        if self.contract_type == "salary":
            if self.bonus > 0:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
            elif self.contracts_landed > 0:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly":
            if self.bonus > 0:
                return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
            elif self.contracts_landed > 0:
                return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", "salary", salary=4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", "hourly", hours_worked=100, hourly_wage=25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", "salary", salary=3000, contracts_landed=4, commission=200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan","hourly", hours_worked=150, hourly_wage=25, contracts_landed=3, commission=220)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie","salary", salary=2000, bonus=1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel","hourly", hours_worked=120, hourly_wage=30, bonus=600)

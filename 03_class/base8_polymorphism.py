class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calcurate_salary(self):
        return self.base_salary
    
    def get_info(self):
        return f"{self.name}: {self.calcurate_salary()}"
    
class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size
        
    def calcurate_salary(self):
        return self.base_salary + self.team_size * 50000
    
class Engineer(Employee):
    def __init__(self, name, base_salary, skill_level):
        super().__init__(name, base_salary)
        if not 1 <= skill_level <= 5:
            raise ValueError('スキルレベルは1-5')
        self.skill_level = skill_level # 1-5
    
    def calcurate_salary(self):
        return self.base_salary + self.skill_level * 20000

class PayrollSystem:
    
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def calcurate_payroll(self):
        print('====　給与計算結果　====')
        total = 0
        for employee in self.employees:
            salary = employee.calcurate_salary()
            print(employee.get_info())
            total += salary
        
        print(f'総給料: {total}')
        return total

payroll = PayrollSystem()
payroll.add_employee(Employee('田中', 300000))
payroll.add_employee(Manager('佐藤', 800000, 8))
payroll.add_employee(Engineer('鈴木', 300000, 4))
payroll.add_employee(Employee('高橋', 400000))

payroll.calcurate_payroll()
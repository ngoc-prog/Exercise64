from MODULE3.Exercise64.models.Employee import Employee


class TemporaryEmployee(Employee):
    def __init__(self,id=None,idcard=None,name=None,birthday=None,workinghour=0):
        super().__init__(id,idcard,name,birthday)
        self.workinghour=workinghour
    def cal_salary(self):
        return self.workinghour*300000

class Programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name= name
        self.salary=salary
        self.pin=pin
    
p = Programmer("Vedansh",120000,243001)
print(p.name,p.salary,p.pin,p.company)
p = Programmer("yash",130000,1100092)
print(p.name,p.salary,p.pin,p.company)
class Person():
    def _init_(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def firstName(self):
        return self.name.split()[0]

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))

class Manager(Person):
    def _init_(self, name, pay=0):
        Person._init_(self,name,'mgr',pay)

    def giveRaise(self, percent,bonus = .10):
        Person.giveRaise(self, percent + bonus)
if __name__== '_main_':
    #self-test code
    chris = Manager('Chris Jones', 50000)
    chris.giveRaise(.20)
    print(chris)
class cashbook:
    def __init__(self):
        self.date = ''
        self.income = 0
        self.expense = 0
        self.balance = 0

    def __compute_balance(self):
        raise NotImplementedError()

    def __add_record(self):
        raise NotImplementedError()

    def print_records(self):
        raise NotImplementedError()

class mycashbook (cashbook):
    records = []
    def __init__(self,date='',income=0,expense=0):
        super().__init__()
        self.date = date
        self.income = income
        self.expense = expense
        self.balance = 0
        self.__compute_balance()
        self.__add_record()
        self.print_records()

    def __compute_balance(self):
        if len(mycashbook.records) == 0:
            self.balance = self.income - self.expense
        else:
            cindx = len(mycashbook.records)-1
            self.balance = mycashbook.records[cindx][4] + self.income - self.expense

    def __add_record(self):
        inum = len(mycashbook.records)+1
        tmp = [inum, self.date, self.income, self.expense, self.balance]
        mycashbook.records.append(tmp)

    def print_records(self):
        for i in range(len(mycashbook.records)):
            print("{0:>3}".format(mycashbook.records[i][0]), end=" ")
            print("{0:12}".format(mycashbook.records[i][1]), end=" ")
            print("{0:>10,}".format(mycashbook.records[i][2]), end=" ")
            print("{0:>10,}".format(mycashbook.records[i][3]), end=" ")
            print("{0:>10,}".format(mycashbook.records[i][4]), end=" ")
            print()

from datetime import datetime
now = datetime.now()
r1 = mycashbook(str(now.date()), 10000, 0)
r2 = mycashbook(str(now.date()), 10300, 600)

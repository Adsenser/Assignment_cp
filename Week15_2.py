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


class my_cashbook(cashbook):
    result = []

    def __init__(self, date, income, expense):
        super().__init__()
        self.date = date
        self.income = income
        self.expense = expense
        self.save_balance()
        self.__compute_balance()
        self.__add_record()

    def save_balance(self):
        for i in self.result:
            self.balance = i[4]

    def __compute_balance(self):
        self.balance += self.income - self.expense

    def __add_record(self):
        record = []
        record.append('일련번호')
        record.append(self.date)
        record.append(self.income)
        record.append(self.expense)
        record.append(self.balance)
        self.result.append(record)

    def print_records(self):
        print(self.result)


cashbook1 = my_cashbook('2022-02-12', 10000, 2000)
cashbook2 = my_cashbook('2023-05-15', 80000, 2000)
cashbook3 = my_cashbook('2023-07-11', 5000, 2000)

cashbook3.print_records()

import csv, re

FILE_NAME = "binance.csv"

def main():
    transactions = []
    with open(FILE_NAME, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        first = True
        for row in reader:
            if first:
                first = False
            else:
                t = Transaction(row[0], row[2], row[3], row[4], row[5], row[6])
                transactions.append(t)
    transactions.reverse()
    
class Transaction:
    def __init__(self, date, side, price, executed, amount, fee):
        self.date = date
        self.pair = self.identify_pair(executed, amount)
        self.side = side
        self.price = price
        self.executed = executed
        self.amount = amount
        self.fee = fee

    def identify_pair(self, executed, amount):
        s1 = re.search("[A-Z]+$", executed)
        s2 = re.search("[A-Z]+$", amount)
        return (s1.group(), s2.group())

if __name__ == "__main__":
    main()
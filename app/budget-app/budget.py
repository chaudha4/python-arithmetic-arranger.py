class Category:

    def __init__(self, category):
        self.name = category
        self.ledger = []  # Each entry is a dictionary
        self.ledger1 = []  # Each entry is an array
        self.balance = 0
        self.withdrawals = 0

    def deposit(self, amt, desc=""):
        self.balance += amt
        self.ledger.append({"amount": amt,
                            "description": desc
                            })
        self.ledger1.append([desc, amt])

    def withdraw(self, amt, desc=""):
        if (not self.check_funds(amt)):
            return False
        self.balance -= amt
        self.withdrawals += amt
        self.ledger.append({"amount": -amt,
                            "description": desc
                            })
        self.ledger1.append([desc, -amt])
        return True

    def check_funds(self, amt):
        if (amt > self.balance):
            return False
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amt, to):
        if self.check_funds(amt):
            self.withdraw(amt, "Transfer to " + to.name)
            to.deposit(amt, "Transfer from " + self.name)
            return True
        return False

    def printLedger(self):
        print("Balance - " + str(self.balance))
        for entry in self.ledger:
            for item in entry.items():
                print(item)

    def printUsingArray(self):
        count = 30 - len(self.name)
        header = ""  # Header needs to be 30 chars max
        if (count > 0):
            header += "*" * (count//2)  # Number of * before Category
            header += self.name
            header += "*" * (30 - len(header))  # Number of * After Category

        # print(len(header))

        lines = ""
        for entry in self.ledger1:
            desc = entry[0]
            line = desc[0:23]  # Truncate to 23 chars or less
            line += " " * (23 - len(line))  # Pad to 23

            # print a float with two decimal places
            amt = "{:.2f}".format(entry[1])
            leftPadding = 7 - len(amt)
            line += " " * leftPadding + amt

            line += "\n"
            lines += line

        total = "Total: " + str(self.balance)
        return header + "\n" + lines + total

    def __repr__(self):
        count = 30 - len(self.name)
        header = ""  # Header needs to be 30 chars max
        if (count > 0):
            header += "*" * (count//2)  # Number of * before Category
            header += self.name
            header += "*" * (30 - len(header))  # Number of * After Category

        lines = ""
        for entry in self.ledger:
            desc = entry["description"]
            line = desc[0:23]  # Truncate to 23 chars or less
            line += " " * (23 - len(line))  # Pad to 23

            # print a float with two decimal places
            amt = "{:.2f}".format(entry["amount"])
            leftPadding = 7 - len(amt)
            line += " " * leftPadding + amt

            line += "\n"
            lines += line

        total = "Total: " + str(self.balance)
        return header + "\n" + lines + total


def create_spend_chart(categories):
    chartData = []
    total_spend = 0
    longest_name_length = 0
    for category in categories:
        total_spend += category.withdrawals
        if (len(category.name) > longest_name_length):
            longest_name_length = len(category.name)

    for category in categories:
        percentageWD = (category.withdrawals / total_spend) * 100
        data = int(percentageWD//10) * 10  # Round "down" to 10
        chartData.append({
            "cat": category.name,
            "data": data
        })

    lines = "Percentage spent by category\n"

    number_of_dashes = 3 * len(chartData)  # 3 spaces per bar

    for x in range(100, -1, -10):  # 100..90.....10..0
        line = "{:3}".format(x) + "| "
        for dd in chartData:
            if (x > dd["data"]):
                line += "   "  # 3 spaces
            else:
                line += "o  "  # 2 spaces
        line += "\n"
        lines += line

    lines += "    " + ("-" * number_of_dashes) + "-\n"   # Add horizonal line

    jj = 0
    while (jj < longest_name_length):
        line = "   "  # 3 spaces
        for cc in categories:
            if (jj < len(cc.name)):
                line += "  " + cc.name[jj]
            else:
                line += "  " + " "
        lines += line + "  "
        jj += 1
        if (jj < longest_name_length):
            lines += "\n"

    return lines


def test_create_spend_chart():
    food = Category("Food")
    food.deposit(900, "deposit")
    entertainment = Category("Entertainment")
    entertainment.deposit(900, "deposit")
    business = Category("Business")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([business, food, entertainment]))


if __name__ == "__main__":
    food = Category("Foods")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    # print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    # food.printLedger()
    # clothing.printLedger()
    # auto.printLedger()

    print(food)
    print(clothing)
    print(create_spend_chart([food, clothing, auto]))
    test_create_spend_chart()

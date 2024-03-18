class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ''
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total_spent = sum(sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories)
    category_spent = [(category, sum(item['amount'] for item in category.ledger if item['amount'] < 0)) for category in categories]
    chart = ''

    for percentage in range(100, -10, -10):
        chart += f"{percentage:>3}| "
        for category, spent in category_spent:
            if spent / total_spent * 100 >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += '\n'

    chart += "    -" + "---" * len(categories) + '\n'

    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            name = category.category
            chart += name[i] + "  " if i < len(name) else "   "
        chart += '\n'

    return title + chart.rstrip('\n')
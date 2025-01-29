class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def __str__(self):
        # power of formatted string
        title = f'{self.name:*^30}\n'
        
        ledger_items = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = '{:.2f}'.format(item['amount'])
            
            ledger_items += f'{description:<23}{amount:>7}\n'
            
        total = f'Total: {self.get_balance():.2f}'
        
        return title + ledger_items + total
            
        
        
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
            
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
            
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
            
        
    
    

def create_spend_chart(categories=''):
    withdrawals = []
    total = 0
    chart = 'Percentage spent by category\n'
    # For each category, sum up all negative amounts (withdrawals)
    for category in categories:
        category_withdrawals = sum(amount['amount'] * -1 for amount in category.ledger if amount['amount'] < 0)
        withdrawals.append(category_withdrawals)
        total += category_withdrawals
                
    # Convert withdrawals to percentages and round down to nearest 10
    percentages = [int((amount / total * 100 ) //10 *10) if total != 0 else 0 for amount in withdrawals]
    
    
    # Create chart bars (from 100 down to 0)
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + '| '
        for percentage in percentages:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
        
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
        
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  '
            else:
                chart += '   '
        if i < max_name_length -1:
            chart += "\n"
    
    return chart
    
        
# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)



class Budget:
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        
    def __str__(self):
        title = f"{self.name}".center(25, '*')
        items = ""
        total = 0
        for item in self.ledger:
            items += "\n{} {}".format(item['description'][0:23], item['amount'])
            
            total += item["amount"]
        output = "{} {} \nTotal: {}\n".format(title, items, str(total))
        return output
        
        
    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and a description.
        If no description is given, it should default to an empty string .
        This method shouls append objects to the ledger list in the form
        {"amount": amount, "description": description}
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        The amount should be stored as to the ledger as negative amount.
        If funds is insufficient, nothing would be added to the ledger.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """
        Returns the current balance of the budget category after withdrawals and deposit have been made
        """
        total_funds= 0
        for item in self.ledger:
            total_funds += item["amount"]
            
        return total_funds

    def transfer(self, amount, category):
        """
        takes in amount and another budget category. 
        The mehod should allow for withdrawal  of an amount with the desciption "Transfer 
        to [Destination budget category]". It should then add a deposit to the other budget category 
        with the amount and description "Transfer from [source budget category].If there are enough funds,
        nothing should be added to both ledgers.Returns True if account took place and otherwise if not.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        """
        returns False if amount is greater than the balance of the budget category and True if otherwise.
        """ 
        if self.get_balance() >= amount:
            return True
        return False           


food = Budget("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "resturant and more food for dessert")
print(food.get_balance())

clothing = Budget("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

entertainment = Budget("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15)

print(food)
print(clothing)



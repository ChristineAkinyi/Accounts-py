class Account:
    def __init__(self,number,pin,owner,name):
        self.number = number
        self.__pin = pin
        self.name = name
        self._balance = 0
        self.transactions = []
        self.overdraft_limit = None
        self.is_frozen = False
    
    def check_balance(self,pin):
        if pin == self.__pin:
            return self._balance
        else:
            return "Wrong pin"
        
    def deposit(self,amount):
        self._balance += amount
        print(f"You have successfully deosited {amount}")

    def withdraw(self,amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal is successful. Your new balance is {self._balance}")
        elif amount > self._balance:
            print("Cannot withdraw due to insufficient funds")
        else:
            print("Invalid amount")
        
    def view_details(self):
        print(f"Account number: {self.number}")
        print(f"Current balance: {self._balance}")
    
    def change_ownership(self, new_name, new_pin):
        self.name = new_name
        self.pin = new_pin
        print(f"Account name updated to: {self.name} and pin has been updated to {self.__pin}")

    def generate_statements(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(f"{transaction['transaction_type']}: ${transaction['amount']} - New Balance: ${transaction['new_balance']}")
    
    def set_overdraft_limit(self, new_limit):
        self.overdraft_limit = new_limit
        print(f"Overdraft limit is: {self.overdraft_limit}")

    def calculate_interest(self, rate):
        interest = self._balance * rate/100
        self.deposit(interest)
        print(f"Interest is {interest}")

    def freeze_account(self):
        self.is_frozen = True

    def unfreeze_account(self):
        self.is_frozen = False

    


    

# class method_variable:

class Bank:
    bank_name = "Old Bank"  # ← Class variable (shared by all)

    @classmethod
    def change_bank_name(cls,name): # ← Changes the class variable
        cls.bank_name = name

# Create objects

account1 =Bank()
account2 =Bank()

print(account1.bank_name)   
print(account2.bank_name)

# Now change the bank name using class method        
Bank.change_bank_name("New Bank")

print(account1.bank_name)
print(account2.bank_name)
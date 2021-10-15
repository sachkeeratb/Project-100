class ATM(object):
    def __init__(self, cashwithdrawl, cashdeposit, balance, paybills):
        self.cashwithdrawl = cashwithdrawl,
        self.cashdeposit = cashdeposit,
        self.balance = balance,
        self.paybills = paybills    

    def cashwithdrawl(self):
        print("You have nothing. If you want money, take a loan.")
    
    def cashdeposit(self):
        print("For the first time in 172 years you got a dollar. Nice.")

    def balance(self):
        print("You have no money. A rat ate all the money and died.")
    
    def paybills(self):
        print("Wow. People can pay bills with no money?")

Automated_Teller_Machine = ATM("Can't", "Finally", "Rat", "How")
Automated_Teller_Machine.cashwithdrawl()
Automated_Teller_Machine.cashdeposit()
Automated_Teller_Machine.balance()
Automated_Teller_Machine.paybills()
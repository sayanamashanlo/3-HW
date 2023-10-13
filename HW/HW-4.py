class SavingAccount:
    pass
class CheckingAccount:
    pass
class RealEstate:
    pass
class Bonk:
    pass
class Stock:
    pass
class Security(Bonk, Stock):
    pass
class BankAccount(CheckingAccount, SavingAccount):
    pass
class Insurableltem(BankAccount, RealEstate):
    pass
class Assest(RealEstate, BankAccount, Security):
    pass
class InterestBearingItem(BankAccount,Security):
    pass

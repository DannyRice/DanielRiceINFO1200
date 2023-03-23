class Bank:
    name: str
    balance: float
    interestRate: float

    def __init__(self, nm, blnc, ir):
        self.name = nm
        self.balance = blnc
        self.interestRate = ir

    def createUserName(self):
        return f"{self.name}_1234"

    def applyRandomGift(self, gift):
        oldBalance = self.balance
        self.balance = self.balance + gift
        return f"Old Balance: {oldBalance}\n\
                Gift: {gift}\n\
                New Balance: {self.balance}"

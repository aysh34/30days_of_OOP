# Payment System:
# Define an abstract class PaymentMethod with the following abstract methods: pay and refund
# Create concrete classes CreditCard, PayPal that inherit from PaymentMethod and implement the abstract methods.

from abc import ABC, abstractmethod


class PaymentMethod(ABC):  # abstract class
    @abstractmethod
    def pay(self, amount):  # abstract method with no implementation
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_no):
        self.card_no = card_no

    def pay(self, amount):
        print(f"Paid {amount} amount using credit card {self.card_no}")

    def refund(self, amount):
        print(f"Refund ${amount} amount to credit card {self.card_no}")


class PayPal(PaymentMethod):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} amount through paypal account {self.email}")

    def refund(self, amount):
        print(f"Refund ${amount} amount to paypal account {self.email}")


credit_card = CreditCard("222-321-576")
credit_card.pay(100)

paypal_account = PayPal("abc@example.com")
paypal_account.pay(300)
paypal_account.refund(100)

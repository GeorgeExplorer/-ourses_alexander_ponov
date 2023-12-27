class Affiliate_shop():

    def __init__(self, merchant, customer, items, currency, amount, card, cash):
        self.merchant = merchant
        self.customer = customer
        self.amount = amount
        self.clothes = items
        self.currency = currency
        self.card = card
        self.cash = cash

    def description(self):
        purchase_description = \
            f"Your name: {self.customer}" \
            f"\nMerchant: {self.merchant}" \
            f"\nYour item: {self.clothes}" \
            f"\nPurchase amount: {self.amount}" \
            f"\nPurchase currency: {self.currency}"

        print(purchase_description)
        # return purchase_description

    def payment_method(self):
        choose_payment_method = input(f"How would you like to pay here: {self.cash} or {self.card}? ")
        if choose_payment_method.lower() == self.cash:
            print(f"Your payment method is {self.cash}")
        else:
            print(f"Your payment method is {self.card}")


purchase_1 = Affiliate_shop("Abibas", "Anastasia", "T-short", "AED", 500, "card", "cash")
purchase_1.description()

payment_method_purchases = Affiliate_shop("card", "cash")
payment_method_purchases.payment_method()

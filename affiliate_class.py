class Affiliate_shop():

    def __init__(self):
        self.customer = input("Enter your name: ")
        self.merchant = input("Enter your merchant: ")
        self.clothes = input("Enter the name of item you took: ")
        self.amount = input("Enter amount of your order: ")
        self.currency = "AED"
        self.card = "card"
        self.cash = "cash"

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
        define_payment_method = False
        while not define_payment_method:
            choose_payment_method = input(f"How would you like to pay here: {self.cash} or {self.card}? ")
            if choose_payment_method.lower() == self.cash:
                define_payment_method == True
                print(f"Your payment method is {self.cash}")
                break
            elif choose_payment_method.lower() == self.card:
                define_payment_method == True
                print(f"Your payment method is {self.card}")
                break
            else:
                define_payment_method == False
                print(f"We couldn't define the payment method! Please, try again!")


purchase_1 = Affiliate_shop()

purchase_1.description()


purchase_1.payment_method()

# create a credit card class with the following attributes: card number, expiration date, and
#  security code. Create a method that will print out the card number, expiration date, and 
# security code. Create an instance of the class and call the method.


class Credit_card:
    def __init__(self,card_no,expiration_date ,security_code):
        self.card_no = card_no
        self.expiration_date = expiration_date
        self.security_code = security_code


    def __str__(self):
        return f'card number: {self.card_no}\nexpiration date: {self.expiration_date}\nsecurity code: {self.security_code} '

dfcu = Credit_card(66,"20/7/2024",8990)
print(dfcu)

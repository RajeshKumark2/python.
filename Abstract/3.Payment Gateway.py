from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Stripe")
        return "stripe_123"
    
    def refund(self, amount):
        print(f"Refunding ${amount} via Stripe")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
        return "paypal_456"
    
    def refund(self, amount):
        print(f"Refunding ${amount} via PayPal")

# Controller using abstraction
def handle_payment(processor: PaymentProcessor, amount):
    transaction_id = processor.process_payment(amount)
    print(f"Transaction ID: {transaction_id}")
    # Common post-processing logic here

# Usage
stripe = StripeProcessor()
paypal = PayPalProcessor()

handle_payment(stripe, 100)
handle_payment(paypal, 50)


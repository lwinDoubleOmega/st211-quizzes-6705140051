class PaymentGateway:
    def change(self,amount):
        raise NotImplementedError("Real gateway should not available in tests")

class OrderProcessor:
    def __init__(self,gateway):
        self.gateway = gateway

    def process(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        result = self.gateway.change(amount)
        return f"Order processed : {result}"


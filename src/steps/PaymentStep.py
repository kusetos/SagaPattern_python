from src.steps.BaseStep import SagaStep
from typing import Dict, Any

class PaymentStep(SagaStep):
    def __init__(self):
        super().__init__("Payment")

    def do(self, context: Dict[str, Any]) -> bool:
        try:
            total_amount = sum(product['price'] * product['quantity'] 
                               for product in context['products'])
            context['payment_details'] = {
                'transaction_id': self.transaction_id,
                'amount': total_amount
            }
            self.logger.info(total_amount)
            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def compensate(self, context: Dict[str, Any]) -> bool:
        try:
            self.logger.info(context['payment_details'])
            return True
        except Exception as e:
            self.logger.error(e)
            return False
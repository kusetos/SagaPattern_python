from typing import List, Dict, Any
from src.steps.BaseStep import SagaStep

class ShippingStep(SagaStep):
    def __init__(self):
        super().__init__("Shipping")

    def execute(self, context: Dict[str, Any]) -> bool:
        try:
            # Simulate shipping order creation
            shipping_details = {
                'order_id': self.transaction_id,
                'products': context['products']
            }
            context['shipping_details'] = shipping_details
            self.logger.info(shipping_details)
            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def compensate(self, context: Dict[str, Any]) -> bool:
        try:
            self.logger.info(context.get('shipping_details'))
            return True
        except Exception as e:
            self.logger.error(e)
            return False
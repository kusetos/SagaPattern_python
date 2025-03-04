from typing import Dict, Any
from src.steps.BaseStep import SagaStep

class InventoryStep(SagaStep):
    def __init__(self):
        super().__init__("Inventory")

    def do(self, context: Dict[str, Any]) -> bool:
        try:
            for product in context['products']:
                self.logger.info(f"Reserved {product['quantity']} of product {product['id']}")
            return True
        except Exception as e:
            return False

    def compensate(self, context: Dict[str, Any]) -> bool:
        try:
            for product in context['products']:
                self.logger.info(f"Restored {product['quantity']} of product {product['id']}")
            return True
        except Exception as e:
            self.logger.error(e)
            return False
from typing import List, Dict, Any
import src.models.StepStatus as StepStatus
import uuid

class SagaStep:
    def __init__(self, name: str):
        self.name = name
        self.status = StepStatus.PENDING
        self.transaction_id = str(uuid.uuid4())

    def execute(self, context: Dict[str, Any]) -> bool:
        raise NotImplementedError("Subclasses must implement execute method")

    def compensate(self, context: Dict[str, Any]) -> bool:
        raise NotImplementedError("Subclasses must implement compensate method")
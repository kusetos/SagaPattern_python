from typing import List, Dict, Any
from src.steps.BaseStep import SagaStep

class SagaOrchestrator:
    def __init__(self, steps: List[SagaStep]):
        self.steps = steps

    def execute(self, context: Dict[str, Any]) -> bool:
        for step in self.steps:
            if not step.execute(context):
                self._compensate_steps(context, step)
                return False
        return True

    def _compensate_steps(self, context: Dict[str, Any], failed_step: SagaStep):
        compensation_steps = self.steps[:self.steps.index(failed_step) + 1]
        for step in reversed(compensation_steps):
            step.compensate(context)
# SagaPattern_python

## Saga Pattern Implementation:
1. Created a SagaOrchestrator that manages the workflow
2. Implemented Steps: Payment, Inventory, and Shipping
3. Each step has do() and compensate() methods
4. If any step fails, previous steps are compensated in reverse order, so it make it atomic.

## Technical Stack:
Python and FastAPI

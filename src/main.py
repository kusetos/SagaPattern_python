import logging
from fastapi import FastAPI, HTTPException
from src.models.CheckoutRequest import CheckoutRequest
from src.steps.PaymentStep import PaymentStep
from src.steps.InventoryStep import InventoryStep
from src.steps.ShippingStep import ShippingStep
from src.services.SagaOrchestrator import SagaOrchestrator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/checkout")
async def process_checkout(request: CheckoutRequest):
    context = {
        'user_id': request.user_id,
        'products': [
            {'id': p.id, 'quantity': p.quantity, 'price': 50.00} 
            for p in request.products
        ],
        'payment_method': request.payment_method
    }

    saga_steps = [
        PaymentStep(),
        InventoryStep(),
        ShippingStep()
    ]

    orchestrator = SagaOrchestrator(saga_steps)
    
    try:
        success = orchestrator.do(context)
        if success:
            return {"status": "success", "message": "Checkout completed"}
        else:
            raise HTTPException(status_code=400, detail="Checkout failed")
    except Exception as e:
        logger.error(f"Saga execution error: {e}")
        raise HTTPException(status_code=500, detail="Internal saga execution error")
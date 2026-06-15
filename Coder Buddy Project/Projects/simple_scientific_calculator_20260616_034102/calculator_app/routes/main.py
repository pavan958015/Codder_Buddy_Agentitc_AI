from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from calculator_app.services.calculator_service import CalculatorService

calculator_router = APIRouter()
calculator_service = CalculatorService()

class CalculationRequest(BaseModel):
    operation: str  # '+', '-', '*', '/', '^', 'sqrt', 'sin', 'cos', 'tan', 'log'
    a: float
    b: Optional[float] = None

@calculator_router.post("/api/calculate")
def calculate_result(request: CalculationRequest):
    """
    Calculates the result based on the provided operation and operands.
    """
    op = request.operation
    a = request.a
    b = request.b

    try:
        if op == '+':
            if b is None:
                raise HTTPException(status_code=400, detail="Missing operand b for addition.")
            result = calculator_service.add(a, b)
        elif op == '-':
            if b is None:
                raise HTTPException(status_code=400, detail="Missing operand b for subtraction.")
            result = calculator_service.subtract(a, b)
        elif op == '*':
            if b is None:
                raise HTTPException(status_code=400, detail="Missing operand b for multiplication.")
            result = calculator_service.multiply(a, b)
        elif op == '/':
            if b is None:
                raise HTTPException(status_code=400, detail="Missing operand b for division.")
            if b == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero.")
            result = calculator_service.divide(a, b)
        elif op == '^':
            if b is None:
                raise HTTPException(status_code=400, detail="Missing exponent operand b for power.")
            result = calculator_service.power(a, b)
        elif op == 'sqrt':
            if a < 0:
                raise HTTPException(status_code=400, detail="Cannot calculate square root of a negative number.")
            result = calculator_service.square_root(a)
        elif op == 'sin':
            result = calculator_service.sine(a)
        elif op == 'cos':
            result = calculator_service.cosine(a)
        elif op == 'tan':
            result = calculator_service.tangent(a)
        elif op == 'log':
            if a <= 0:
                raise HTTPException(status_code=400, detail="Logarithm argument must be positive.")
            result = calculator_service.logarithm(a, b)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported operation: {op}")

        return {
            "status": "success",
            "operation": op,
            "result": result
        }
    except HTTPException as e:
        raise e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
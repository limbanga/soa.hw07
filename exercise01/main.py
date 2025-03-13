from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, confloat, Field
from typing import List, Optional
import uuid

app = FastAPI()

# Define the Product model
class Product(BaseModel):
    product_id: int
    name: str = Field(..., min_length=3)
    price: confloat(gt=0)  # must be positive
    discount: Optional[confloat(ge=0, le=50)] = None  # optional, between 0-50%
    tags: Optional[List[str]] = None  # optional list of strings

# Define the CustomerDetails model
class CustomerDetails(BaseModel):
    name: str
    email: EmailStr

# Define the Invoice model
class Invoice(BaseModel):
    invoice_id: uuid.UUID
    customer_details: CustomerDetails
    products: List[Product]

# Create the /invoice/ endpoint
@app.post("/invoice/")
async def create_invoice(invoice: Invoice):
    # Here you can process the invoice as needed
    return {"message": "Invoice created successfully", "invoice": invoice}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
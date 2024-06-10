from pydantic import BaseModel, Field
from decimal import Decimal
from enum import Enum
from typing import Optional

class Currency(Enum):
    RUB = "RUB"
    USD = "USD"

class ProductMeasureType(Enum):
    PIECES = "PCS"
    KG = "KG"

class ProductMeasure(BaseModel):
    value: Decimal
    measure_type: ProductMeasureType

class ProductCost(BaseModel):
    value: Decimal
    currency: Currency

class Product(BaseModel):
    name: str = Field(max_length=50)
    measure: ProductMeasure
    cost: Optional[ProductCost] = None

class ProductListItem(BaseModel):
    id: int
    checked: bool
    product: Product

class ProductList(BaseModel):
    id: str
    name: str = Field(max_length=50)
    items: list[ProductListItem]

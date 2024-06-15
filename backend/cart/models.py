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
    item_id: int
    checked: bool
    product: Product

class ProductList(BaseModel):
    product_list_id: str
    username: str
    name: str = Field(max_length=50)
    color: str = Field(pattern=r"^#[a-f0-9]{6}$")
    items: list[ProductListItem]

class ProductListCreate(BaseModel):
    name: str = Field(max_length=50)
    color: str = Field(pattern=r"^#[a-f0-9]{6}$")
    items: list[ProductListItem]

class ProductListUpdate(BaseModel):
    name: Optional[str] = Field(max_length=50, default=None)
    color: Optional[str] = Field(pattern=r"^#[a-f0-9]{6}$", default=None)
    items: Optional[list[ProductListItem]] = None

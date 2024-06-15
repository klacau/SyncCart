from motor.motor_asyncio import AsyncIOMotorDatabase

from cart.models import ProductList, ProductListUpdate

from result import Result, Ok, Err
from typing import Optional

class ProductListsRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.__db = db

    async def get_product_lists(self, username: str) -> list[ProductList]:
        cursor = self.__db.product_lists.find({ "username": username })
        raw_list = await cursor.to_list(length=None)
        return list(map(ProductList.model_validate, raw_list))

    async def get_product_list(self, product_list_id: str) -> Optional[ProductList]:
        document = await self.__db.product_lists.find_one({ "product_list_id": product_list_id })
        if document is None:
            return None
        return ProductList.model_validate(document)

    async def add_product_list(self, product_list: ProductList) -> Result[None, str]:
        try:
            await self.__db.product_lists.insert_one(product_list.model_dump(mode='json'))
        except:
            return Err('Product list with this id already exists')
        
        return Ok(None)
    
    async def update_product_list(self, product_list_id: str, data: ProductListUpdate):
        await self.__db.product_lists.update_one(
            filter={ "product_list_id": product_list_id },
            update={ "$set": dict(filter(lambda p: p[1] is not None, data.model_dump(mode='json').items())) }
        )
    
    async def delete_product_list(self, product_list_id: str):
        await self.__db.product_lists.delete_one({ "product_list_id": product_list_id })

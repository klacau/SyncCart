from motor.motor_asyncio import AsyncIOMotorDatabase

from cart.models import ProductList

class ProductListsRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.__db = db

    async def get_product_lists(self, username: str) -> list[ProductList]:
        cursor = self.__db.product_lists.find({ "username": username })
        return await cursor.to_list(length=None)

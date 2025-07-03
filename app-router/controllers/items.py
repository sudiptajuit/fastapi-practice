from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def get_items():
    return {"message": "List of all items"}

@router.get("/item")
async def get_item(item_id: int):
    return {"item_id": item_id, "item details": "Details of the item"}
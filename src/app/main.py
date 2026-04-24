from litestar import Litestar, get


@get("/")
async def healthcheck() -> str:
    healthcheck_status = 'its okay'
    return healthcheck_status


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])

from fastapi import FastAPI
from test_order_producer.producer import send_test_order
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    """
    Sends a test order.
    """
    res = send_test_order()
    return res


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)

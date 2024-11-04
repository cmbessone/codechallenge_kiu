from fastapi import FastAPI
from controllers.journey_controller import journey_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is running"}


#  Register the router for Journeys
app.include_router(journey_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

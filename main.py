import uvicorn
# uvicorn server
if __name__ == "__main__":
    uvicorn.run("backend.api:app", host="127.0.0.1", port=8000, lifespan="on", reload=True)

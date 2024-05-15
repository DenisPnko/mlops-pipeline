from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Model building complete"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="Multi Model Chat Gateway")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

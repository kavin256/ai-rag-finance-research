from fastapi import FastAPI

app = FastAPI(title="AI Financial Research Assistant")

@app.get("/health")
def health():
    return {"status": "ok"}
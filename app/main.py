from fastapi import FastAPI

app = FastAPI(
    title="ClinicOps AI",
    description="AI Agent 기반 한의원 업무 자동화 시스템",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "ClinicOps AI API"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
    }
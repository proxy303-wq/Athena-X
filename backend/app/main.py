from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.market.router import router as market_router
from app.decision.router import router as decision_router
from app.dashboard.router import router as dashboard_router
from app.optionchain.router import router as optionchain_router

app = FastAPI(
    title="Athena X",
    version="0.1.0",
)

# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------

app.include_router(market_router)
app.include_router(decision_router)
app.include_router(dashboard_router)
app.include_router(optionchain_router)

# -----------------------------
# Root
# -----------------------------

@app.get("/")
async def root():
    return {
        "project": "Athena X"
    }

# -----------------------------
# Health
# -----------------------------

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }

# -----------------------------
# Analysis
# -----------------------------

@app.get("/analysis")
async def analysis():
    return {
        "bias": "UNKNOWN",
        "confidence": 0,
        "reason": []
    }

# -----------------------------
# Signal
# -----------------------------

@app.get("/signal")
async def signal():
    return {
        "action": "WAIT"
    }
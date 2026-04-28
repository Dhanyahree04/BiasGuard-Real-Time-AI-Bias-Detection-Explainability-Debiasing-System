from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import tempfile
import os
import uvicorn

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def audit_bias(csv_path):
    df = pd.read_csv(csv_path)

    result = {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_values": int(df.isnull().sum().sum())
    }

    return result


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/audit")
async def audit(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp:
        content = await file.read()
        temp.write(content)
        temp_path = temp.name

    result = audit_bias(temp_path)
    os.remove(temp_path)

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

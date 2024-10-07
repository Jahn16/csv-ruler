from __future__ import annotations

from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/apply")
def apply_rules(config: UploadFile) -> dict[str, str]:
    return {"config": config.filename or ""}

# CRUD 예제
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PC(BaseModel):
    name: str
    price: float
    desc: str | None = None

@app.get("/")
def read_root():
    return {"message": "PC 관리 API입니다. /docs로 이동해서 테스트해보세요!"}

# 임시 저장소 (딕셔너리)
pc_storage = {
    "Samsung Laptop": PC(name="Samsung Laptop", price=1500000, desc="Good price!"),
    "LG Gram": PC(name="LG Gram", price=1800000, desc="Very light!"),
    "MSI Gamming Laptop": PC(name="MSI Gamming Laptop", price=2000000, desc="Heavy but runs well!")
}

# Create (생성)
@app.post("/PC/")
def create_pc(item: PC):
    if item.name in pc_storage:
        raise HTTPException(status_code=400, detail="It already exists")
    pc_storage[item.name] = item
    return {"message": "Register success."}

# Read (전체 조회)
@app.get("/PC/")
def read_all_pc():
    return pc_storage

# Read (단일 조회)
@app.get("/PC/{name}")
def read_pc(name: str):
    if name not in pc_storage:
        raise HTTPException(status_code=404, detail=f"Cannot find {name}.")
    return pc_storage[name]

# Update (수정)
@app.put("/PC/{name}")
def update_pc(name: str, item: PC):
    if name not in pc_storage:
        raise HTTPException(status_code=404, details=f"Cannot find {name}.")
    pc_storage[name]
    return {"message": f"Updated {name}.", "Updated": item}

# Delete (삭제)
@app.delete("/PC/{name}")
def delete_pc(name: str):
    if name not in pc_storage:
        raise HTTPException(status_code=404, detail=f"Cannot find {name}.")
    del pc_storage[name]
    return {"message": f"Deleted {name}."}
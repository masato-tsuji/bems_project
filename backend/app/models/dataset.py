from pydantic import BaseModel

class Dataset(BaseModel):
    id: int
    name: str
    value: float

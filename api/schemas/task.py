from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
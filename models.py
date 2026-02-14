from pydantic import BaseModel, Field
from enum import Enum

class RootCauseCategory(str, Enum):
    NETWORK = "NETWORK"
    DISK = "DISK"
    AUTH = "AUTH"
    CODE = "CODE"

class IncidentReport(BaseModel):
    impact_score: int = Field(gt=0, lt=10)
    root_cause_category: RootCauseCategory
    is_critical: bool
    summary: str = Field(description="A 1-sentence technical summary of the event")


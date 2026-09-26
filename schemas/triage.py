from typing import Literal
from pydantic import BaseModel, Field


class TriageResult(BaseModel):

    category: Literal[
        "faq",
        "seat",
        "booking",
        "flight",
        "baggage",
        "cancellation",
        "escalation"
    ] = Field(
        description="The category of the customer's request."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1."
    )

    reason: str = Field(
        description="Short explanation for the classification."
    )
from typing import Any
from schemas.triage import TriageResult


def validate_triage_output(result) -> tuple[bool, Any]:
    """
    Validate the structured output produced by the triage task.
    """

    triage_result = getattr(result, "pydantic", None)

    if triage_result is None:
        raw_output = getattr(result, "raw", None)

        if raw_output:
            try:
                triage_result = TriageResult.model_validate_json(
                    raw_output
                )
            except Exception:
                return (
                    False,
                    "Triage output must contain a valid structured result."
                )

    if triage_result is None:
        return (
            False,
            "Triage output must contain a valid structured result."
        )

    if not triage_result.category:
        return (
            False,
            "Triage category cannot be empty."
        )

    if not 0.0 <= triage_result.confidence <= 1.0:
        return (
            False,
            "Confidence must be between 0 and 1."
        )

    if not triage_result.reason.strip():
        return (
            False,
            "Triage reason cannot be empty."
        )

    return True, triage_result
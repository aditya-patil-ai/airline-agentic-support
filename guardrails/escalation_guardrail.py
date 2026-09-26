from typing import Any


def validate_escalation(result) -> tuple[bool, Any]:
    """
    Validate requests that require human escalation.
    """

    if result is None:
        return (
            False,
            "Escalation result cannot be empty."
        )

    return True, result
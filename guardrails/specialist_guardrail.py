from typing import Any


def validate_specialist_output(result) -> tuple[bool, Any]:
    """
    Validate the final response produced by a specialist agent.
    """

    if result is None:
        return (
            False,
            "Specialist agent output cannot be empty."
        )

    response = getattr(result, "raw", None)

    if response is None:
        return (
            False,
            "Specialist agent must produce a valid response."
        )

    if not str(response).strip():
        return (
            False,
            "Specialist agent response cannot be empty."
        )

    return True, result
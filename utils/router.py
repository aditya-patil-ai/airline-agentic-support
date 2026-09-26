from schemas.triage import TriageResult
from agents.registry import AGENT_REGISTRY


def route_request(result: TriageResult):

    if result.category == "escalation":
        return None

    return AGENT_REGISTRY[result.category]
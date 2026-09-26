from agents.faq_agent import faq_agent
from agents.seat_agent import seat_agent
from agents.booking_agent import booking_agent
from agents.flight_agent import flight_agent
from agents.baggage_agent import baggage_agent
from agents.cancellation_agent import cancellation_agent


AGENT_REGISTRY = {
    "faq": faq_agent,
    "seat": seat_agent,
    "booking": booking_agent,
    "flight": flight_agent,
    "baggage": baggage_agent,
    "cancellation": cancellation_agent,
}
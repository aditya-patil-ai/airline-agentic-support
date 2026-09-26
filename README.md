# ✈️ Airline Agentic Support System

An agentic AI-powered airline customer support system built with **CrewAI**, featuring intelligent request triage, specialized support agents, tool calling, structured outputs, and guardrails for reliable responses.

The system uses a triage agent to understand a customer's request and automatically routes it to a specialized agent that can use the appropriate tool to handle the request.

## How It Works

```text
Customer Request
       ↓
Triage Agent
       ↓
Request Category
       ↓
Router
       ↓
Specialized Agent
       ↓
Tool
       ↓
Final Response
-------------------------------------------------------------------------
🤖 Agents

The system currently includes specialized agents for:

Triage Agent — Classifies incoming customer requests
FAQ Agent — Handles common airline questions
Booking Agent — Looks up booking information
Flight Agent — Checks flight status
Seat Agent — Handles seat changes
Baggage Agent — Provides baggage information
Cancellation Agent — Handles booking cancellations

Requests that require human assistance can also be routed to escalation.
----------------------------------------------------------------------------
🛠️ Tools

Each specialist agent can use a dedicated tool when required:

FAQ Lookup Tool
Booking Lookup Tool
Flight Status Tool
Seat Update Tool
Baggage Tool
Cancellation Tool
-----------------------------------------------------------------------------
🛡️ Guardrails

The system uses guardrails to validate agent outputs.
Triage Guardrail

Ensures that the triage agent returns:
A valid category
A confidence score between 0 and 1
A valid reason

Specialist Guardrail

Ensures that the specialist agent produces a valid, non-empty response.
------------------------------------------------------------------------------
🎯 Project Goals

This project demonstrates how multiple specialized AI agents can work together to handle different customer-support tasks.

The main focus is on:

Agent orchestration
Intelligent request routing
Tool calling
Structured outputs
Guardrails
Modular agent design

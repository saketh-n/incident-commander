This roadmap outlines a rigorous, 4-hour intensive to master **PydanticAI**. By moving from simple text generation to type-safe dependency injection, you’ll build an agent capable of surviving a production environment.

---

# 🛠️ PydanticAI Masterclass: From Strings to Systems

This repository contains a structured, 4-phase implementation of an **Automated Incident Response Agent**. We move beyond simple "chatbots" to build a type-safe, tool-augmented system designed for reliability.

## 📈 Roadmap Overview

| Phase | Focus | Key Concept |
| --- | --- | --- |
| **1. Structured Outputs** | Validation | Moving from `str` to Pydantic Schemas. |
| **2. System Tools** | Agency | Giving the LLM "hands" via type-hinted tools. |
| **3. Dependency Injection** | Architecture | Managing state and resources via `deps`. |
| **4. Observability** | Reliability | Tracing the thought loop and unit testing logic. |

---

## 🏗️ Phase 1: Structured Outputs & Validation

**Goal:** Ensure the LLM speaks the language of your backend.

We define a strict schema for incident reporting. If the LLM tries to return a category that doesn't exist (e.g., "DATABASE"), PydanticAI will automatically catch the error and ask the model to retry until it conforms to the `IncidentReport` model.

```python
from enum import Enum
from pydantic import BaseModel

class RootCause(str, Enum):
    NETWORK = "NETWORK"
    DISK = "DISK"
    AUTH = "AUTH"
    CODE = "CODE"

class IncidentReport(BaseModel):
    impact_score: int
    root_cause_category: RootCause
    is_critical: bool
    summary: str

```

---

## 🔧 Phase 2: System Tools & Type Safety

**Goal:** Investigation over hallucination.

Instead of guessing why a server is down, the agent uses `@agent.tool`. PydanticAI inspects your Python **type hints** to explain to the LLM exactly what arguments these tools require.

* `get_service_health`: Returns real-time metrics (CPU/RAM).
* `query_deployment_logs`: Checks recent git commits for potential "bad deploys."

---

## 💉 Phase 3: Dependency Injection

**Goal:** Professional-grade resource management.

In production, tools shouldn't have "hardcoded" access to everything. We use `SupportContext` to inject dependencies. This allows us to:

1. Verify if a service exists in a **Service Registry** before querying it.
2. Pass **API Keys** securely without global variables.
3. Easily swap real services for mocks during testing.

```python
@dataclass
class SupportContext:
    service_registry: dict[str, str]
    api_key: str
    debug_mode: bool = True

```

---

## 🔍 Phase 4: Observability & Testing

**Goal:** Verify the "Thought Loop."

We implement logging to trace how many steps the agent takes to reach a conclusion. We validate the agent against three distinct scenarios:

1. **Database Timeout:** Expects `RootCause.NETWORK`.
2. **Bad Deployment:** Expects `RootCause.CODE`.
3. **False Alarm:** Expects `is_critical=False`.

---

## 🚀 Getting Started

1. **Install dependencies:**
```bash
pip install pydantic-ai logfire

```


2. **Run the Agent:**
```bash
python main.py

```

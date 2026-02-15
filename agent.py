'''
**The Goal:** Give the agent "hands" to investigate.

- **Task:** Create two "Tools" (Python functions decorated with `@agent.tool`):
    1. `get_service_health(service_name: str)`: Returns a mock JSON of CPU/Memory.
    2. `query_deployment_logs(service_name: str)`: Returns a string of recent "Git Commits."
- **Requirement:** Ensure your tools use Python type hints. PydanticAI uses these hints to generate the tool definitions sent to the LLM.
- **Action:** The agent must now call these tools *before* finalizing the report. It shouldn't just guess; it must "investigate."
'''

from pydantic_ai import Agent, RunContext
from models import IncidentReport
from deps import SupportContext
import random

incident_response_agent = Agent[str](
    'claude-haiku-4-5',
    output_type=IncidentReport,
    system_prompt='You are a Senior SRE. Do not guess. You must investigate health metrics and recent deployment logs before concluding any Incident Report. Please take a look at the following unstructured text description of an incident and parse it into a structured format'
)

@incident_response_agent.tool
def get_service_health(ctx: RunContext[SupportContext], service_name: str):
    """
    Checks CPU and Memory for a specific service.
    
    Args:
        service_name: The name of the service to check (e.g., 'auth-api', 'payments').
    """
    if (service_name in ctx.deps.service_registry.keys()):
        return {'cpu': random.randint(1, 100), 'memory': random.randint(1, 100)}

    return f"Service {service_name} was not found in list of services {ctx.deps.service_registry.keys()}"

@incident_response_agent.tool
def query_deployment_logs(ctx: RunContext[SupportContext], service_name: str):
    """
    Returns the most recent Git commits for a service.
    """
    if (service_name in ctx.deps.service_registry.keys()):
        return [
            "feat(auth): add JWT rotation logic to identity provider (#442)",
            "fix(db): increase connection pool size to 50 for high-load events",
            "chore: update kubernetes manifest for resource limits in us-east-1",
            "perf!: refactor message broker consumer to use batching logic",
            "fix(api): handle null pointer exception when service-x is unreachable",
            "docs: update incident runbook for service-unavailable errors"
        ]

    return f"Service {service_name} was not found in list of services {ctx.deps.service_registry.keys()}"
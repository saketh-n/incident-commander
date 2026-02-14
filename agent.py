from pydantic_ai import (Agent)
from models import IncidentReport

incident_response_agent = Agent[str](
    'claude-haiku-4-5',
    output_type=IncidentReport,
    system_prompt='You are a master at diagnosing incidents that occur for SREs. Please take a look at the following unstructured text description of an incident and parse it into a structured format'
)
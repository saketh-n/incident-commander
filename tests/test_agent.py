from pydantic_ai import RunContext
from pydantic_ai.usage import Usage
from pydantic_ai.models.test import TestModel

from agent import get_service_health, query_deployment_logs
from deps import SupportContext

def test_tool_get_service_health():
    # Fake Registry for testing
    registry = {'auth-api': {
        "tier": 1,
        "owner": "identity-team",
        "description": "Handles user authentication and JWT issuance"
    }}
    deps = SupportContext(service_registry=registry, api_key="123")

    ctx = RunContext(deps=deps,
        retry=0,
        tool_name="get_service_health", 
        model=TestModel(),
        usage=Usage()
    )

    # TEST PATH A: The service exists
    result_ok = get_service_health(ctx, "auth-api")
    assert isinstance(result_ok, dict)  # It should return the CPU/Mem dict
    assert "cpu" in result_ok

    # TEST PATH B: The service is missing (The Gatekeeper should catch this)
    result_fail = get_service_health(ctx, "fake-service")
    assert isinstance(result_fail, str) # It should return the error string
    assert "not found" in result_fail

def test_tool_query_deployment_logs():
    # Fake Registry for testing
    registry = {'auth-api': {
        "tier": 1,
        "owner": "identity-team",
        "description": "Handles user authentication and JWT issuance"
    }}
    deps = SupportContext(service_registry=registry, api_key="123")

    ctx = RunContext(deps=deps,
        retry=0,
        tool_name="query_deployment_logs", 
        model=TestModel(),
        usage=Usage()
    )

    # TEST PATH A: The service exists
    result_ok = query_deployment_logs(ctx, "auth-api")
    assert isinstance(result_ok, list)  # It should return the commits list
    assert "fix(api): handle null pointer exception when service-x is unreachable" in result_ok

    # TEST PATH B: The service is missing (The Gatekeeper should catch this)
    result_fail = query_deployment_logs(ctx, "fake-service")
    assert isinstance(result_fail, str) # It should return the error string
    assert "not found" in result_fail

from agent import incident_response_agent
from deps import SupportContext

messy_slack_messages = ['OMG the DB is down', "Network spike in us-east-1", "50 percent of hosts are off-line in eu-west-1"]
# Use this as your 'service_registry' dictionary
SERVICES_GATEWAY = {
    "auth-provider": {
        "tier": 1,
        "owner": "identity-team",
        "description": "Handles user authentication and JWT issuance"
    },
    "payment-processor": {
        "tier": 1,
        "owner": "billing-eng",
        "description": "Processes all customer transactions and refunds"
    },
    "image-resizer": {
        "tier": 3,
        "owner": "media-infra",
        "description": "Async processing for user profile uploads"
    },
    "search-index-01": {
        "tier": 2,
        "owner": "search-platform",
        "description": "Maintains the pgvector indices for search"
    }
}

deps = SupportContext(service_registry=SERVICES_GATEWAY, api_key="sk-internal-cloud-auth-9922", environment="production")

for message in messy_slack_messages:
    print(incident_response_agent.run_sync(message, deps=deps).output)
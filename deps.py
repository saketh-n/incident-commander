from dataclasses import dataclass

@dataclass
class SupportContext:
    service_registry: dict[str, dict]
    api_key: str
    environment: str = "production"
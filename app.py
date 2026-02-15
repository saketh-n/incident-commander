from agent import incident_response_agent
from deps import deps
import logfire
from logfire import ScrubMatch

messy_slack_messages = ['OMG the DB is down', "Network spike in us-east-1", "50 percent of hosts are off-line in eu-west-1"]

# Custom scrubbing callback that only scrubs specific patterns
def scrubbing_callback(match: ScrubMatch) -> str:
    # we don't want to scrub any auth (just for this case)
    if match.pattern_match.group(0) == 'auth':
        return match.value

logfire.configure(
    scrubbing=logfire.ScrubbingOptions(callback=scrubbing_callback)
)

logfire.instrument_pydantic_ai()

def parse_messy_slack_messages(messy_slack_messages: list[str]):
    for message in messy_slack_messages:
        print(incident_response_agent.run_sync(message, deps=deps).output)

parse_messy_slack_messages(messy_slack_messages)
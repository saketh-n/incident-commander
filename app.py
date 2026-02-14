from agent import incident_response_agent

messy_slack_messages = ['OMG the DB is down', "Network spike in us-east-1", "50 percent of hosts are off-line in eu-west-1"]

for message in messy_slack_messages:
    print(incident_response_agent.run_sync(message).output)
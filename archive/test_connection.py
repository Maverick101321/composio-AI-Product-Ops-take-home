import os
from composio import Composio

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])

toolkits = composio.toolkits.list()
print(toolkits)
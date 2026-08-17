import inspect
import os
from composio import Composio

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
print(inspect.signature(composio.toolkits.list))

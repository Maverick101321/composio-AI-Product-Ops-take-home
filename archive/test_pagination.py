import os
from composio import Composio

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])

all_items = []
try:
    page = 1
    while True:
        res = composio.toolkits.list(page=page, limit=100) # Or try to see how pagination works
        items = getattr(res, 'items', None)
        if items is None:
            # Maybe res is a list?
            if isinstance(res, list):
                all_items.extend(res)
                break
            else:
                break
        
        all_items.extend(items)
        if getattr(res, 'next_cursor', None) or page >= getattr(res, 'total_pages', 1):
            if getattr(res, 'next_cursor', None):
                # How to pass cursor?
                pass
            if page >= getattr(res, 'total_pages', 1):
                break
        page += 1
except Exception as e:
    print(e)
print(f"Total fetched: {len(all_items)}")

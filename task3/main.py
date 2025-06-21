import json
from utils import get_value_from_path

# 🔽 USER INPUT REQUIRED HERE
json_string = '''
{
  "data": {
    "customer": {
      "name": "Reni",
      "address": {
        "city": "Dallas",
        "zip": "75001"
      }
    }
  }
}
'''

path = "data.customer.name"  

data = json.loads(json_string)
result = get_value_from_path(data, path)
print("Result:", result)

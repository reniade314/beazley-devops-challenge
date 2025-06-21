import json

def get_value_from_path(obj, path):
    try:
        keys = path.split("/")
        for key in keys:
            obj = obj[key]
        return obj
    except (KeyError, TypeError) as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    json_string = '''
    {
        "employee": {
            "details": {
                "name": "Reni",
                "city": "Dallas"
            }
        }
    }
    '''
    path = "employee/details/city"  
    data = json.loads(json_string)
    result = get_value_from_path(data, path)
    print("Result:", result)

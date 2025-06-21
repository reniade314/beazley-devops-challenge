def get_value_from_path(data, path):
    try:
        keys = path.split(".")
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return f"Error: Invalid key path '{path}'"

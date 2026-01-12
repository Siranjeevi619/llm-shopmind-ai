def sanitize_keys(data: dict) -> dict:
    clean = {}
    for k, v in data.items():
        if isinstance(k, str):
            k = k.strip().strip('"').strip("'")
        clean[k] = v
    return clean

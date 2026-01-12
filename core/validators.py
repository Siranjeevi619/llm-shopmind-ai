def require(payload: dict, fields: list):
    for f in fields:
        if f not in payload or payload[f] is None:
            raise ValueError(f"Missing required field: {f}")

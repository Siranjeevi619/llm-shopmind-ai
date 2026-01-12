ADMIN_ONLY = {
    "ADD_PRODUCT",
    "ADD_STOCK",
    "SET_STOCK",
    "REMOVE_PRODUCT"
}

def check_permission(role: str, intent: str):
    if intent in ADMIN_ONLY and role != "ADMIN":
        raise PermissionError("Unauthorized operation")

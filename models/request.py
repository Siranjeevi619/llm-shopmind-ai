from pydantic import BaseModel


class AssistantRequest(BaseModel):
    message: str
    role: str = "USER"

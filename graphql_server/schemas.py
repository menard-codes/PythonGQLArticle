import strawberry
from typing import Optional

# Schema:


@strawberry.type
class Task:
    id: int
    content: str
    is_done: bool = False


# =============================

# Input Schema:


@strawberry.input
class UpdateTaskInput:
    content: Optional[str] = None
    is_done: Optional[bool] = None


@strawberry.input
class PaginationInput:
    offset: int
    limit: int

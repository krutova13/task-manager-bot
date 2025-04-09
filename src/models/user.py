from __future__ import annotations

from dataclasses import dataclass


@dataclass  # TODO: заменить на Pydantic
class User:
    id: int
    name: str
    surname: str
    username: str
    age: int | None

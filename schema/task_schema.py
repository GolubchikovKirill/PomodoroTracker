from pydantic import BaseModel, Field, model_validator


class Task(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    categoryID: int = Field(alias="category_id")

    @classmethod
    @model_validator(mode="after")
    def check_name_or_pomodoro_count_is_not_name(cls):
        if cls.name is None and cls.pomodoro_count is None:
            return ValueError("name or pomodoro_count is required")
        return cls

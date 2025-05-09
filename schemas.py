from pydantic import BaseModel, Field


class CreateProduct(BaseModel):
    """Схема для создания продукта."""

    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category: int


class CreateCategory(BaseModel):
    """Схема для создания категории."""

    name: str
    parent_id: int | None = None


class CreateUser(BaseModel):
    """Схема для создания пользователя."""

    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class CreateReview(BaseModel):
    """Схема для создания отзыва."""

    comment: str | None = Field(None, description="Комментарий отзыва")
    grade: int = Field(..., description="Оценка отзыва", ge=1, le=10)

from tortoise import fields

from . import AbstractBaseModel
from .mixins import TimestampMixin


class User(AbstractBaseModel, TimestampMixin):
    telegram_id = fields.IntField(unique=True)

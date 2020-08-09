from tortoise import fields

from . import AbstractBaseModel
from .mixins import TimeStampMixin


class User(AbstractBaseModel, TimeStampMixin):
    telegram_id = fields.IntField(unique=True)

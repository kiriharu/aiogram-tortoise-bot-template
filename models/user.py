from . import AbstractBaseModel
from .mixins import TimeStampMixin
from tortoise import fields

class User(AbstractBaseModel, TimeStampMixin):
    telegram_id = fields.IntField(unique=True)
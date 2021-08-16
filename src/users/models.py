import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from shared.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    name = Column(String, nullable=False)
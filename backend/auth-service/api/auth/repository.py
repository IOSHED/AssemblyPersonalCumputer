from api.auth.models import User
from api.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

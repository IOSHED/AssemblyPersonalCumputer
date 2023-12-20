# import pytest
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
#
# from sqlalchemy.orm import Session, sessionmaker
# from starlette.testclient import TestClient
#
# from api import config
# from api.auth.models import User
# from api.db.db import get_async_session
# from api.main import app
#
#
# @pytest.fixture(name="session", scope="session")
# async def session_fixture():
#     engine = create_async_engine(config.TEST_DATABASE_URL)
#     async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#     async with async_session_maker() as session:
#         await session.run_sync(User.metadata.create_all(session))
#         yield session
#         await session.run_sync(User.metadata.drop_all(session))
#
#
# @pytest.fixture(name="client", scope="session")
# async def client_fixture(session: Session):
#     async def get_session_override():
#         return session
#     app.dependency_overrides[get_async_session] = get_session_override
#     client = TestClient(app)
#     yield client
#     app.dependency_overrides.clear()

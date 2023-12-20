# import json
# import pytest
# from http import HTTPStatus
# from typing import Dict, Any
# from starlette.testclient import TestClient
#
# from api import config
#
#
# @pytest.mark.asyncio
# @pytest.mark.parametrize(
#     "json_request, expect_response, expect_status_code",
#     [
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_001@example.com",
#                 "password": "qwertyui",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             {
#                 "username": "name",
#                 "email": "test_user_001@example.com",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             HTTPStatus.CREATED,
#         ),
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_001@example.com",
#                 "password": "qwertyui",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             {
#                 "detail": "REGISTER_USER_ALREADY_EXISTS"
#             },
#             HTTPStatus.BAD_REQUEST,
#         ),
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_002@example.com",
#                 "password": "qwe",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             {
#                 "detail": {
#                     "code": "REGISTER_INVALID_PASSWORD",
#                     "reason": "Password should be at least 8 characters"
#                 }
#             },
#             HTTPStatus.BAD_REQUEST,
#         ),
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_003@example.com",
#                 "password": "test_user_003",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             {
#                 "detail": {
#                     "code": "REGISTER_INVALID_PASSWORD",
#                     "reason": "Password should not contain e-mail"
#                 }
#             },
#             HTTPStatus.BAD_REQUEST,
#         ),
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_004@example.com",
#                 "password": "test_user_003",
#             },
#             {
#                   "detail": [
#                     {
#                       "type": "json_invalid",
#                       "loc": [
#                         "body",
#                         102
#                       ],
#                       "msg": "JSON decode error",
#                       "input": {},
#                       "ctx": {
#                         "error": "Expecting property name enclosed in double quotes"
#                       }
#                     }
#                   ]
#             },
#             HTTPStatus.UNPROCESSABLE_ENTITY,
#         ),
#         (
#             {
#                 "username": "name",
#                 "email": "test_user_005@example.com",
#                 "password": "qwertyui",
#                 "is_active": True,
#                 "is_superuser": True,
#                 "is_verified": True,
#             },
#             {
#                 "username": "name",
#                 "email": "test_user_005@example.com",
#                 "is_active": True,
#                 "is_superuser": False,
#                 "is_verified": False,
#             },
#             HTTPStatus.CREATED,
#         ),
#     ]
# )
# async def test_registration(
#         json_request: Dict[str, Any],
#         expect_response: Dict[str, Any],
#         expect_status_code: int,
#         client: TestClient,
# ):
#     response = client.post(f"{config.PATH_SERVICE}/register", data=json.dumps(json_request))
#     json_response = response.json()
#     print(json_response)
#     print(response)
#     assert response.status_code == expect_status_code
#     assert json_response == expect_response

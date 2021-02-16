#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: auth.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
登录认证
"""
from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import db as models
from core import deps, security
from core.security import create_access_token, get_password_hash
from schemas import Response200, Response400
from schemas.admin import AdminInit, Token

auth_router = APIRouter(tags=["登录"], prefix="/auth")


@auth_router.post("/login", name="管理员登录", response_model=Union[Response200, Response400])
async def admin_login(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(models.Admin).filter(models.Admin.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.password_hash):
        return Response400(msg="用户名或密码错误")
    token = Token(access_token=create_access_token(user.id))
    return Response200(data={"token": token})

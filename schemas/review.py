#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: comment.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:

"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# 创建/修改的基类, 回复的评论
class Review(BaseModel):
    post_id: int  # 文章id
    author: str
    content: str


class ReviewCreate(Review):
    pass


# 回复的评论
class ReviewReply(ReviewCreate):
    pass


# 数据库查询出来的模型类
class ReviewBase(Review):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

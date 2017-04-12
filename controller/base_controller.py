__author__ = 'Administrator'
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 初始化数据库连接:
engine = create_engine("postgresql://postgres:wozuishuai@192.168.1.224/postgres",  echo = True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
print('--------------------connect-----------------------------'+str(engine))
# def __init__(self,DBSession,engine):
#     self.engine = create_engine("postgresql://xiaoheng:wozuishuai@127.0.0.1:5432/xiaoheng_analysis",  echo = True)
#     self.DBSession= sessionmaker(bind=engine)


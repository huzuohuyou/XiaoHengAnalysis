__author__ = 'Administrator'
# 导入:
from sqlalchemy import Column, String, create_engine,Integer,DECIMAL,Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class OrderLog(Base):
    # 表的名字:
    __tablename__ = 'order_log'
    # 表的结构:
    id = Column(Integer,primary_key=True)
    day = Column(Date)
    page=Column(Integer)

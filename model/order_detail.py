__author__ = 'Administrator'
# 导入:
from sqlalchemy import Column, String, create_engine,Integer,DECIMAL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class OrderDetail(Base):
    # 表的名字:
    __tablename__ = 'order_detail'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    order_id = Column(Integer)
    name = Column(String)
    charge = Column(DECIMAL)
    count = Column(Integer)

    def __init__(self,  order_id, name, charge,count):
        self.order_id = order_id
        self.name = name
        self.charge = charge
        self.count=count

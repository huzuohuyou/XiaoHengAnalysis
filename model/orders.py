__author__ = 'Administrator'
# 导入:
from sqlalchemy import Column, String, create_engine,Integer,DECIMAL,Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class orders(Base):
    # 表的名字:
    __tablename__ = 'orders'
    # 表的结构:
    id = Column(Integer,primary_key=True)
    shop_id = Column(Integer)
    order_id=Column(Integer)
    shop_name = Column(String)
    order_date = Column(Date)
    charge = Column(DECIMAL)
    charge_type = Column(String)
    status = Column(String)

    def __init__(self,  shop_id, order_id, shop_name,order_date,charge,charge_type,status):
        self.shop_id = shop_id
        self.order_id = order_id
        self.shop_name = shop_name
        self.order_date=order_date
        self.charge=charge
        self.charge_type=charge_type
        self.status=status

    def __repr__(self):
        return "{'id':%s,'shop_id':%s,'order_id':%s,'shop_name':%s,'order_date':%s,'charge':%s,'charge_type':%s,'status':%s}"\
               %(self.id,self.shop_id,self.order_id,self.shop_name,self.order_date,self.charge,self.charge_type,self.status)

class shop(Base):
    # 表的名字:
    __tablename__ = 'shop'
    # 表的结构:
    id = Column(Integer,primary_key=True)
    name = Column(String)
    location=Column(Integer)
    master = Column(String)
    telephone = Column(String)

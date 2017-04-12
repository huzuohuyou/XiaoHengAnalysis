__author__ = 'Administrator'
# 导入:
import controller
from model import order_detail

session=controller.base_controller.DBSession()

def add(order_id,name,charge,count):
    new_order_detail = order_detail.OrderDetail(order_id,name,charge,count)
    session.add(new_order_detail)
    session.commit()


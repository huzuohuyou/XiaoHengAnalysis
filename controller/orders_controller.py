__author__ = 'Administrator'
# 导入:
import controller.base_controller
from model import orders
import json

session=controller.base_controller.DBSession()
def add(shop_id,order_id,shop_name,order_date,charge,charge_type,status):
    new_order = orders.orders(shop_id=shop_id,order_id=order_id,shop_name=shop_name,order_date=order_date,charge=charge,charge_type=charge_type,status=status)
    # print('************************')
    # print(str(new_order))
    # shop = orders.shop(id='22',name='1',location='2',master='3',telephone='4')
    # session.add(shop)
    session.add(new_order)
    session.commit()
    session.close()
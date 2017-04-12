__author__ = 'Administrator'
# 导入:
import controller.base_controller
from model import order_log
import json

session=controller.base_controller.DBSession()
def update(day,page):
    new_order = order_log.OrderLog(day=day,page=page)
    # print('************************')
    # print(str(new_order))
    # shop = orders.shop(id='22',name='1',location='2',master='3',telephone='4')
    # session.add(shop)
    session.add(new_order)
    session.commit()
    session.close()
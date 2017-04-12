from flask import Flask
import requests
from bs4 import BeautifulSoup
import urllib
import json
import re
import time,datetime
import pickle
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def getOrderDetail(orderId):
    url='http://www.xiaohengjiaozi.com/MvcComponents/Popup_Details/OpOrderDetails?ItemIDs='+orderId
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    req=requests.get(url,headers = headers)
    # print(req.text)
    regex = re.compile("widgetInitData.json = (.*);")
    machList = regex.findall(req.text)
    import controller.order_detail_controller
    dic=json.loads(machList[0])
    for item in dic['displayItems'][0]['OrderItems']:
        controller.order_detail_controller.add(order_id=orderId,name=item['Name'],charge=float(item['Price']),count=int(item['Number']))

def getAllOrder():
    global begin
    global page_start
    if os.path.exists('orderLog.txt'):
        print('******************************************read log')
        f= open('orderLog.txt','rb')
        r=pickle.load(f)
        f.close()
        begin=r['day']
        page_start=r['page']
    else:
        begin = datetime.date(2017,1,1)
        page_start=0
    end = datetime.date(2017,4,9)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        for page in range(page_start,99):
            orderLog={'day':day,'page':page}
            res=getOrderList(day,page)
            if None==res:
                print('*********************************************break ')
                break
            else:
                print('*********************************************write log')
                f=open('orderLog.txt','wb')
                pickle.dump(orderLog,f)
                res=getOrderList(day,page)
                f.close()

def getOrderList(day,page):
    # page=1
    print('###################################################日期：'+str(day)+'页码：'+str(page))
    postdata =urllib.parse.urlencode({
        'ParamHttp.FilterFromDate':str(day),
        'ParamHttp.FilterToDate':str(day),
        'ParamHttp.FilterFromTimeSpan':'00:00',
        'ParamHttp.FilterToTimeSpan':'23:59',
        'ParamHttp.CurPage':str(page)
    }).encode('utf-8')
    headers={
        'Accept': '*/*',
        'Origin': 'http://www.xiaohengjiaozi.com/MvcWidgets/Admin_OpOrder/List_Json/Company/60',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://www.xiaohengjiaozi.com/Admin/Op_AllOrder',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie': '.ASPXFORMSAUTH=5BBB87576DFF35E0A823C40140FECCB1EE800CBEFB35AF741E6EDA3679CC3FADFADF15C61211F3BDEDC399A06D2BC5674CFAC2753420358797B5C34F08F6552543D6470845A5287438A34FD7173DAA6CD92BD687; SiJia=clientGuid721c6ff80a6d3e4ad4ffa52a04c60085=3b5e0922-9810-4de6-8470-c7905d3de448',
    }
    req = urllib.request.Request('http://www.xiaohengjiaozi.com/MvcWidgets/Admin_OpOrder/List_Json/Company/60',postdata,headers)
    orderlist = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    if orderlist['itemPaging']['curPage']!=page:
        return None
    print(orderlist)
    for item in orderlist.get('displayItems'):
        print(item)
        import controller.orders_controller
        t=datetime.datetime.strptime('2017-'+str(item['ReceiveTimeStr']).replace('月','-').replace('日',''),"%Y-%m-%d %H:%M")
        controller.orders_controller.add(shop_id=1,order_id=int(item['ItemID']),shop_name=str(item['ShopName']),order_date=t,charge=float(item['PayMoney']),charge_type=str(item['PayTypeStr']),status=str(item['PaymentStatusStr']))
        getOrderDetail(str(item['ItemID']))
    return 'OK'
if __name__ == '__main__':
    getAllOrder()
    app.run()

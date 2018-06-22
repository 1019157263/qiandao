import datetime

def qian():
   import requests
   
   li=[eval(i) for i in open('F:\qiandao\qiandao\qian.config','r+')]
   for i in li:
       try:
          print(i)
          if i['fk']=='GET':
             b=requests.get(i['url'],headers=i['header'],cookies=i['cookie'])         
          if i['fk']=='POST':
             b=requests.post(i['url'],data=i['data'],headers=i['header'],cookies=i['cookie'])
          print(b.json())
          c=str(datetime.datetime.now())
          a={'time':c,'data':b.json()['message']}
          f=open('F:\qiandao\qiandao\qian.log','a+')
          f.write('\n')
          f.write(str(a))
       except:
          print('错误')
          print(b.text)
          f=open('F:\qiandao\qiandao\qian.log','a+')
          c=str(datetime.datetime.now())
          a={'time':c,'data':b.text}
          f.write('\n')
          f.write(str(a))
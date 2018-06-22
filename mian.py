#!/usr/bin/env python
# -*- coding:utf-8 -*-   
import tornado.ioloop
import tornado.web        
from DING import *
import sys
import datetime,time
sys.path.append("F:\qiandao\qiandao")

class TimeHandler(tornado.web.RequestHandler):

    def get(self):
        f=open('F:\qiandao\qiandao\\time.config','r+').read()
        li=eval(f)
        hours=datetime.datetime.now().strftime('%H')
        riqi=datetime.datetime.now().strftime('%Y%m%d')
        li.append([str(riqi),int(hours)])
        open('F:\qiandao\qiandao\\time.config','w').write(str(li))
        XXX=[int(i[0]) for i in li]
        OOO=[i[1] for i in li]
        print(XXX)
        print(OOO)
        d1 = datetime.datetime.strptime(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.strptime(open('F:\qiandao\qiandao\\time.log','r+').read(), '%Y-%m-%d %H:%M:%S')
        delta = d1 - d2
        print(d1)
        bday=delta.days
        print(delta)
        self.render('time_p.html',a=open('F:\qiandao\qiandao\\time.log','r+').read(),b=bday,c=d1,l0=str(XXX),l1=str(OOO))
        
    def post(self,*args,**kwargs):

        d1 = datetime.datetime.strptime(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), '%Y-%m-%d %H:%M:%S')

        d2 = datetime.datetime.strptime(open('F:\qiandao\qiandao\\time.log','r+').read(), '%Y-%m-%d %H:%M:%S')

        delta = d1 - d2

        bday=delta.days

        print(delta)    

        a=self.get_argument('time')

        print(a)

        open('F:\qiandao\qiandao\\time.log','w+').write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        self.render("time.html",a=open('F:\qiandao\qiandao\\time.log','r+').read(),b=bday,c=d1)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("admin.html")
    def post(self,*args,**kwargs):
        a=self.get_argument('username')
        b=self.get_argument('pwd')
        print(a+','+b)
        if a=='admin' and b=='a18381801393':
             li=[eval(i) for i in open('F:\qiandao\qiandao\qian.log','r+')][::-1]
             self.render('mob.html',f=li,q=a)
        else:
             self.write('<center><h1>登录失败:帐号或密码错误</h1></center>')
class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("renwu.html")
    def post(self):
        name=self.get_argument('name')
        url=self.get_argument('url')
        cookie=self.get_argument('cookie')
        header=self.get_argument('header')
        fk=self.get_argument('fk')
        data=self.get_argument('data')
        print('%s,%s,%s,%s'%(name,url,cookie,header))
    
        try:
            if data=='':
                        dict={'fk':fk,'data':data,'name':name,'url':url,'cookie':eval(cookie),'header':eval(header)}
            else:
                        dict={'fk':fk,'data':eval(data),'name':name,'url':url,'cookie':eval(cookie),'header':eval(header)}
						
            print(dict)
            f=open('F:\qiandao\qiandao\qian.config','a+')
            f.write('\n')
            f.write(str(dict))
            f.close
            self.write('<center><h1>添加成功</h1></center>')
        except:
            self.write('<center><h1>添加失败</h1></center>')
class XianHandler(tornado.web.RequestHandler):
    def get(self):
        list=[eval(i) for i in open('F:\qiandao\qiandao\qian.config','r+')][::-1]
        self.render("xians.html",list=list)
    def post(self):
        pass

application = tornado.web.Application([
    (r"/admin", MainHandler),
    (r"/add", AddHandler),
    (r"/time", TimeHandler),
    (r"/list", XianHandler),

])   
if __name__ == "__main__":
   
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
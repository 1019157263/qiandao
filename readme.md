# 简单自动签到站点

服务器环境要求为Windows版本
因为在Windows服务器调试时MySQL数据库一直安装不成功
到最后也没有解决
所有干脆不用数据库了
给搭建也带来了好处

不需要配置数据库！！！

# 放到：F:\qiandao\qiandao目录下
# 安装对应依赖库
# 安装python3环境
# cmd执行
pip install tornado
pip install schedule
pip install requests
# cmd 执行
python F:\qiandao\qiandao\main.py

或者双击main.py即可运行


# 打开127.0.0.1:8888/admin
查看签到任务

# 打开127.0.0.1:8888/time
查看网站运行时间

# 打开127.0.0.01:8888/add
添加签到任务

# 打开127.0.0.01:8888/list
查看任务列表







##### 虚拟环境

###### 创建虚拟环境

```shell
python -m venv venv1 
```

###### 激活虚拟环境（linux，Windows命令不同）

```shell
source venv1/bin/activate
```

###### 退出虚拟环境

```shell
deactivate
```

###### 查看已安装的软件包

```shell
pip freeze
```

###### 保存已安装的软件包

```shell
pip freeze > pip.txt
```

###### 批量安装软件包

```shell
pip install -r ./pip.txt
```

##### python高级数据类型

###### 双端队列

```python
from collections import deque
# 定义双端队列
atog = deque("def")
#在右侧插入数据
atog.append('g')
#在左侧插入数据
atog.appendleft('c')
#插入多个
atog.extendleft('ba')
#遍历
for ele in atog:
    print(ele)

```

##### 标准库

###### time

```python
import time
#时间戳
time.time()
#格式化时间
time.strftime("%Y-%m-%d %X",time.localtime())
#日期转时间戳
timearray = time.strptime("2020-11-28 14:51:10","%Y-%m-%d %X")
timeStamp = int(time.mktime(timeArray))
```

###### datatime

```python
from datetiem import *
datetime.today()
datetime.now()
#昨天日期
datetime.today()-timedelta(days=1)

```

###### logging

```python
import logging
logging.basicConfig(filename="log.log", level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',format="%(asctime)s %(pathname)-8s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s")
```

###### random

```python
from random import *
# 生成随机数
random()
#生成0-100随机整数，步长2
randomrange(0,101,2)
#从列表中随机选择
choice(['red','yellow','blue'])
#随机选择多个
sample([1,2,3,4,5],k=2)
```

###### json

```python
import json
#解码
json.loads()
#编码
json.dumps()
```

###### pathlib

```python
from pathlib import Path
p=Path()
#当前绝对路径
p.resolv()

path="usr/local/a.txt.py"
p=Path(path)

#获取文件名
p.name
#获取文件名（不含后缀）
p.stem
#获取后缀
p.suffix
#获取多个后缀
p.suffixes
#路径名称
p.parent
#可迭代对象
p.parents
#元组
p.parts
```



###### os

```python
import os

os.path.adspath('test.log')

path="/usr/local/a.txt"
#获取文件名
os.path.basename(path)
#获取路径名
os.path.dirname(path)
#判断目录是否存在
os.path.exists('/ect/passwd')
#是否为文件
os.path.isfile('/ect/passwd')
#是否为目录
os.path.isdir('/ect/passwd')
#连接路径
os.path.join('a','b')
```

###### re

```python
import re

prog=re.compile(pattern)
result=prog.match(string)
# 等价于
result=re.match(pattren,string)

#匹配11位数字
re.match('.{11}','18888888888')
#获取匹配内容
re.match('.{11}','18888888888').group()
#获取匹配范围
re.match('.{11}','18888888888').span()
#匹配邮箱
re.match('.*@.*','123@123.com')
#分组
re.match('(.*)@(.*)','123@123.com').group(1)
#扫描字符串
re.search("@","123@123.com")
re.findall("123","123@123.com")
#替换字符串
re.sub("123","456","123@123.com")
re.sub("\d+","456","123@123.com")
#分割字符串
re.split("@","123@123.com")
re.split("(@)","123@123.com")

```



##### 手动编写一个daemon进程

```python
#!/usr/bin/env python
import sys
import os
import time

'''
手动编写一个daemon进程
'''

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:

        # 创建子进程
        pid = os.fork()

        if pid > 0:
            # 父进程先于子进程exit，会使子进程变为孤儿进程，
            # 这样子进程成功被init这个用户级守护进程收养
            sys.exit(0)

    except OSError as err:
        sys.stderr.write('_Fork #1 failed: {0}\n'.format(err))
        sys.exit(1)

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir确认进程不占用任何目录，否则不能umount
    os.chdir("/")
    # 调用umask(0)拥有写任何文件的权限，避免继承自父进程的umask被修改导致自身权限不足
    os.umask(0)
    # setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离
    os.setsid()

    # 第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            # 第二个父进程退出
            sys.exit(0)
    except OSError as err:
        sys.stderr.write('_Fork #2 failed: {0}\n'.format(err))
        sys.exit(1)

    # 重定向标准文件描述符
    sys.stdout.flush()
    sys.stderr.flush()

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    # dup2函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

# 每秒显示一个时间戳
def test():
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid()) 
    while True:
        now = time.strftime("%X", time.localtime())
        sys.stdout.write(f'{time.ctime()}\n') 
        sys.stdout.flush() 
        time.sleep(1)

if __name__ == "__main__":
    daemonize('/dev/null','/Users/edz/Downloads/demo/d1.log','/dev/null')
    test()
```

re
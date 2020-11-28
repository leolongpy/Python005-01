

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


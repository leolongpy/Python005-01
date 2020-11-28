import logging
import os
import time


def log():
    # 获取当前日期
    data = time.strftime("%Y-%m-%d", time.localtime())
    fname = "var/log/python-" + data

    if not os.path.exists(fname):
        os.makedirs(fname)
    logging.basicConfig(filename
                        =fname + "/log.log", level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s %(pathname)-8s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s",
                        encoding='utf-8')

    logging.debug("函数调用的时间为:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    log()

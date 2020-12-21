import requests
from lxml import etree
from time import sleep
import pymysql
import time

db = pymysql.connect("127.0.0.1", "root", "root", "testdb",
                     cursorclass=pymysql.cursors.DictCursor)

def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':ua}
    response = requests.get(myurl,headers=header)

    selector = etree.HTML(response.text)
    contents = selector.xpath('//*[@id="comments"]/div[@class="comment-item "]/div[2]')
    for content in contents:
        # 短评
        film_content = content.xpath('./p/span/text()')[0]
        # 星级
        film_star = content.xpath('./h3/span[@class="comment-info"]/span[contains(@class, "rating")]/@title')
        if film_star:
            film_star=film_star[0]
        else:
            film_star=''
        with db.cursor() as cursor:
            sql = 'INSERT INTO douban (film_content,film_star) VALUES (%s,%s)'
            value = (film_content,film_star)
            cursor.execute(sql,value)
        db.commit()

if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = tuple(f'https://movie.douban.com/subject/35155748/comments?start={page * 20}&limit=20&status=P&sort=new_score' for page in range(10))
    for page in urls:
        get_url_name(page)
        sleep(5)
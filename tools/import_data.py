import os
import sys

import pymysql.cursors

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hynovel.settings")

import django
django.setup()

from novels.models import Novel, Chapter

DB = 'db_novel'
HOST = '127.0.0.1'
USER = 'root'
PORT = 3306

def import_from_mysql():
    connect_select = pymysql.connect(
        user=USER,
        host=HOST,
        db=DB,
        port=PORT,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    try:
        with connect_select.cursor() as cursor:
            sql_select = "SELECT * FROM novel_novels"
            cursor.execute(sql_select)
            result = cursor.fetchall()
            for item in result:
                novel = Novel()
                novel.book_name = item['book_name']
                novel.book_author = item['book_author']
                novel.book_category = item['book_category']
                novel.book_identify = item['book_identify']
                novel.book_image = item['book_image']
                novel.book_desc = item['book_desc']
                novel.book_latest = item['book_latest']
                novel.save()
        with connect_select.cursor() as cursor:
            sql_select = "SELECT * FROM novel_chapter"
            cursor.execute(sql_select)
            result = cursor.fetchall()
            for item in result:
                chapter = Chapter()
                chapter.chap_title = item['chap_title']
                chapter.chap_identify = item['chap_identify']
                chapter.chap_contentUrl = item['chap_contentUrl']
                chapter.book_identify = item['book_identify']
                chapter.save()
        connect_select.commit()
    finally:
        connect_select.close()


if __name__ == "__main__":
    import_from_mysql()

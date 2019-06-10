# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

DBNAME="forum"

def get_posts():
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc")
  posts = cursor.fetchall()
  print posts
  cursor.close()
  conn.close()
  return posts

def add_post(content):
  cleanContent = bleach.clean(content)
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute("insert into posts values (%s)", (cleanContent,))
  conn.commit()
  cursor.close()
  conn.close()



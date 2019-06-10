#!usr/bin python
# Python 2.7.12
# report.py
# By Taylor Larsen
# News report gathering scripts

import psycopg2

def getPopularArticles(curs, number):
    articleList = ""
    articlesQ = """
        select title, count(*) as views from log, articles
        where log.path like '%%'||articles.slug
        group by articles.id
        order by views desc limit %s;
    """

    curs.execute(articlesQ, (number,))
    articles = curs.fetchall()

    count = 1
    for art in articles:
        articleList += "  %d. '%s' - %d views\n" % (count, art[0], art[1])
        count += 1

    return articleList


def getPopularAuthors(curs):
    authorList = ""
    authorsQ = """
        select authors.name, count(*) as views from log, articles, authors
        where log.path like '%'||articles.slug and authors.id=articles.author
        group by authors.id
        order by views desc;
    """

    curs.execute(authorsQ)
    authors = curs.fetchall()

    count = 1
    for author in authors:
        authorList += "  %d. %s - %d views\n" % (count, author[0], author[1])
        count += 1

    return authorList


def getDaysWithPctError(curs, pctError):
    daysList = ""
    getDaysQ = """
        select date, 100.0*fail/total as pct from
        (select time::date as date,
        count(case status when '404 NOT FOUND' then 1 else null end) as fail,
        count(*) as total from log group by date) as aggregate
        where 100.0*fail/total>1.0 order by pct desc;
    """

    curs.execute(getDaysQ)
    days = curs.fetchall()

    for day in days:
        daysList += "  * %s - %.1f%% errors\n" % (day[0], day[1])

    return daysList


if __name__ == '__main__':
    db = psycopg2.connect("dbname=news")
    curs = db.cursor()
    print("\nMost popular three articles of all time:")
    print(getPopularArticles(curs, 3))

    print("\nMost popular authors of all time:")
    print(getPopularAuthors(curs))

    print("\nDays with more than 1% of request errors:")
    print(getDaysWithPctError(curs, 1))

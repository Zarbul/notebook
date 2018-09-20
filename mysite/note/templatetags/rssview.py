from django import template
from django.shortcuts import render_to_response
import datetime
import feedparser

register = template.Library()


@register.inclusion_tag('note/rss_news.html')
def pull_feed(feed_url, posts_to_show=5):
    try:
        feed = feedparser.parse(feed_url)
        posts = []
        for i in range(posts_to_show):
            pub_date = feed['entries'][i].updated_parsed
            published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
            posts.append({

                'title': feed['entries'][i].title,
                'summary': feed['entries'][i].summary,
                'link': feed['entries'][i].link,
                'date': published,
            })
    except:
        pass
    return {'posts': posts}

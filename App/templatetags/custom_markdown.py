from django.contrib.syndication.views import Feed
from App.models import App

class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"

    description = "RSS feed - blog posts"

    def items(self):
        return App.objects.order_by('_date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self,item):
        return item.add_date

    def item_description(self, item):
        return item.content
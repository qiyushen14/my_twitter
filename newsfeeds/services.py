from typing import List

from friendships.services import FriendShipService
from newsfeeds.models import NewsFeed


class NewsFeedService(object):

    @classmethod
    def fanout_to_followers(cls, tweet):
        #followers = FriendShipService.get_followers(tweet.user)
        # for follower in followers:
        #     NewsFeed.objects.create(user=follower,tweet=tweet)
        # not allowed: for(query)
        newsfeeds = [
           NewsFeed(user=follower,tweet=tweet)
           for follower in FriendShipService.get_followers(tweet.user)
       ]
        newsfeeds.append(NewsFeed(user=tweet.user,tweet=tweet))
        NewsFeed.objects.bulk_create(newsfeeds)

    
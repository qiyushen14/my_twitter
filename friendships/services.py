from friendships.models import Friendship


class FriendShipService(object):

    @classmethod
    def get_followers(cls,user):
        # friendships = Friendship.objects.filter(to_user=user)
        # return [friendships.from_user for friendship in friendships]
        # slow! n+1 queries problem


        # friendships = Friendship.objects.filter(
        #     to_user=user
        # ).select_related('from_user')
        # return [friendships.from_user for friendship in friendships]
        #!!!select_related == join

        #same as below
        # friendships = Friendship.objects.filter(to_user=user,)
        # follower_ids = [friendship.from_user_id for friendship in friendships]
        # followers = User.objects.filter(id__in=follower_ids)

        friendships = Friendship.objects.filter(
            to_user=user,
        ).prefetch_related('from_user')
        return [friendship.from_user for friendship in friendships]

        # friendships = Friendship.objects.filter(to_user=user,)
        # follower_ids = [friendship.from_user_id for friendship in friendships]
        # followers = User.objects.filter(id_in=follower_ids)
        #
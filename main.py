from instapy import InstaPy
from instapy import smart_run
import random

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    users = ['barbara_macau', 'mona.storeee', 'bonita.macau', 'mrsbeauty_shop', 'hazelwood.made', '00in_usa']
    """ Activity flow """
    # general settings
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=24,
                                 peak_likes_daily=560,
                                 peak_comments_hourly=6,
                                 peak_comments_daily=120,
                                 peak_follows_hourly=6,
                                 peak_follows_daily=120,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=120,
                                 peak_server_calls_daily=2600)

    session.set_skip_users(skip_private=False,
                           private_percentage=0,
                           skip_no_profile_pic=True,
                           no_profile_pic_percentage=100,
                           skip_business=True,
                           skip_non_business=False,
                           business_percentage=0,
                           )

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=20000,
                                    max_following=10000,
                                    min_followers=0,
                                    min_following=20,
                                    )

    session.set_action_delays(enabled=True, like=45, follow=56, comment=45, unfollow=56, randomize=True,
                              random_range_from=100,
                              random_range_to=300)

    # session.set_do_like(enabled=True, percentage=100)
    # session.set_do_follow(enabled=True, percentage=100, times=1)
    # session.set_do_comment(enabled=True, percentage=80)
    # session.set_comments(['🔥🔥', '💯💯'])
    # session.set_delimit_liking(enabled=True, max_likes=1000, min_likes=0)
    # session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    # session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')

    # action
    # session.like_by_tags(hashtags, amount=10, randomize=True, media=None)
    session.follow_user_following(users, amount=30, randomize=True, sleep_delay=300)
    #
    session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="RANDOM", unfollow_after=90 * 60 * 60, sleep_delay=501)
    session.like_by_feed(amount=50, randomize=True, unfollow=True, interact=True)

    # Joining Engagement Pods
    # session.set_comments(comments, media='Photo')
    # session.join_pods(engagement_mode='no_comments')

"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
import json

def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    # print post['created_time']
    print post


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBABCFf5vjPlWcaZA0XQyeOdVd0Rv5php7ANW1EF6huhrvnDECUoZCTpwubmKtKWmk71HecfJJCJZAz6MPfWWlIAhoEz6ZAf1OCzGO8IVRqZB4Wbz4jvzhFVpZCRcGvrZAfcCmbFhH6NlRDr76ZAQ7jE8GKzZAJRoBS4V9FsoVOjJZAW5C6HzyJ1VLba25knmZBO9Nm8m7IldMMbNJfdXGZCYCxIkZD'

# users = ["comscoreinc", "conchoresources", "csodcommunity", "WorkAtBRAVO", "iHeartMedia", "CTGinc", "GrouponJobs", "InsperityJobs", "tmobilecareers", "ReachLocal", "SymmetryMedical", "Zillow"]
users = ["ReachLocal", "SymmetryMedical", "Zillow"]
# Look at user's profile for this example by using his Facebook id.
for user in users:

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(user)
    print profile
    # exit()

    # user timeline
    try:
        posts = graph.get_connections(profile['id'], 'posts')
    except:
        pass

    # job opening page posts.  TODO
    # posts = graph.get_connections("118437573003", 'posts')
    post_list = list()

    # Wrap this block in a while loop so we can keep paginating requests until
    # finished.
    while True:
        try:
            # Perform some action on each post in the collection we receive from
            # Facebook.
            # [some_action(post=post) for post in posts['data']]
            post_list.append(posts)
            # Attempt to make a request to the next page of data, if it exists.
            posts = requests.get(posts['paging']['next']).json()
        except KeyError as e:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            print "API error ", e
            break

    with open(user+"_timeline.json", "w") as outfile:
        json.dump(post_list, outfile )

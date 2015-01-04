'''
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
'''
import facebook
import requests
import json

def some_action(post):
    ''' Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    '''
    print post['created_time']
    # print post


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBABUvW75btYiMtxMTuNKoPKhVDSptQet5nDBQ50fq1S2fNUbZC5ZChAc4LR68Eldc1F0GQQhhk6u9UuDm4YQE60PaSjA4MI1MAhrSrdZA4SnmDw7ZAoRLJKIO4FNiK7g12nz082ooOOOGBZBCl2BhxshZAZCKP4d1x3ve5iCpFTwfJPahVKcEkdaZAFENuZCKMueWZACesyvxfJ24vwE7MUhxYZD'

# users = ['comscoreinc', 'conchoresources', 'csodcommunity', 'WorkAtBRAVO', 'iHeartMedia', 'CTGinc', 'GrouponJobs', 'InsperityJobs', 'tmobilecareers', 'ReachLocal', 'SymmetryMedical', 'Zillow']
# users = ['GrouponJobs', 'SymmetryMedical', 'conchoresources', 'iHeartMedia']
users = ['SymmetryMedical']
# users = ['Zillow']
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
    post_list = list()

    # Wrap this block in a while loop so we can keep paginating requests until
    # finished.
    while True:
        try:
            # Perform some action on each post in the collection we receive from
            # Facebook.
            [some_action(post=post) for post in posts['data']]
            post_list.append(posts)
            # Attempt to make a request to the next page of data, if it exists.

            # for other companies that can not reach 2011
            # posts = requests.get(posts['paging']['next'].replace('limit=25', 'limit=200')).json()

            # posts = requests.get(posts['paging']['next']).json()

            # Zillow only
            posts = requests.get(posts['paging']['next'].replace('limit=25', 'limit=200').replace('until=1365771802', 'until=1322715938')).json()
        except KeyError as e:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            print 'API error ', e
            break

    with open('fb_data/'+user+'.json', 'w') as outfile:
        json.dump(post_list, outfile )

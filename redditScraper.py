import json, requests
import datetime
import os
import string

# subreddit that one wants to collect data from
subreddit = 'popular'

# Create external file to save info in
file = open(os.path.expanduser("currentDay.txt"), "wb")

# json request
r = requests.get(
    'http://www.reddit.com/r/{}.json?limit=100'.format(subreddit),
    headers={'user-agent': 'Mozilla/5.0'}
)


info = []



#scrape title, Score, Link, subreddit
for post in r.json()['data']['children']:
    print ("Title: " + post['data']['title'])
    print ("Score: " + str(post['data']['score']))
    print ("Link: " + "http://www.reddit.com" + post['data']['permalink'])
    print ("Subreddit: " + post['data']['subreddit'] + '\n')

    info.append("Title: " + post['data']['title'])
    info.append("Score: " + str(post['data']['score']))
    info.append("Link: " + "http://www.reddit.com" + post['data']['permalink'])
    info.append("Subreddit: " + post['data']['subreddit'] + '\n')


# Turn list elements to strings
subReddits = ''.join(str(e + '\n') for e in info)

# Save data into external file
file.write(bytes(subReddits, encoding="ascii", errors='ignore'))

print (info)

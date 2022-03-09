import twitter
from datetime import datetime

now = str(datetime.now())

api = twitter.Api(consumer_key='####',
                  consumer_secret='####',
                  access_token_key='####',
                  access_token_secret='####')

hashtags_to_track = ['query1', 'query2', 'query3']
stream = api.GetStreamFilter(track=hashtags_to_track)

count = 0
tweets = []

for line in stream:
    tweet = twitter.Status.NewFromJsonDict(line)
    if len(tweets) < 10000: #number of tweets per batch
        try:
            tweets.append(tweet)
        except:
            continue
    else:
        with open('data/'+ now + str(count) + '.json', 'w') as outfile: # PATH to directory and name of the file
            for tweet in tweets:
                outfile.write(str(tweet) + '\n')
        count += 1
        tweets = []

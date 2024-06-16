import tweepy
import pandas as pd

# Set up your credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to get user tweets
def get_user_tweets(username):
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended', include_rts=False).items():
        tweets.append(tweet._json)
    return tweets

# Replace 'twitter_username' with the actual username of the account you want to scrape tweets from
username = 'twitter_username'
tweets = get_user_tweets(username)

# Optionally, save the tweets to a CSV file
df = pd.DataFrame(tweets)
df.to_csv(f'{username}_tweets.csv', index=False)

print(f'Downloaded {len(tweets)} tweets from {username}')
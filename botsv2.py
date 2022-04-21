import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,BEARER_TOKEN

# api_key = API_KEY
# api_secret_key =  API_SECRET_KEY
# access_token = ACCESS_TOKEN
# access_token_secret = ACCESS_TOKEN_SECRET
# bearer_token = BEARER_TOKEN

 #authorization v2
client = tweepy.Client(
consumer_key= API_KEY,
consumer_secret= API_SECRET_KEY,
access_token = ACCESS_TOKEN,
access_token_secret = ACCESS_TOKEN_SECRET
)

client.create_tweet( text="hey peeps testing V2 creating tweets, @VeldaKiara", user_auth=True)

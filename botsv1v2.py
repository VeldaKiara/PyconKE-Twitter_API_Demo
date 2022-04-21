import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,BEARER_TOKEN
from datetime import date
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
start_date = date(2022, 5, 6)
today_date = date.today() 
days = start_date - today_date
client.create_tweet(text=" We are " + str(days.days) + " days to PyconKE 2022, I cannot keep calm!! " " #BuildWhatsNext  #Tweepy #TwitterAPI #PyconKE @VeldaKiara ", user_auth=True)



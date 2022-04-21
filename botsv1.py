import tweepy
from datetime import date
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,BEARER_TOKEN


api_key = API_KEY
api_secret_key =  API_SECRET_KEY
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET
bearer_token = BEARER_TOKEN


def challengeDays():

    # authorization v1
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # # access to api
    api = tweepy.API(auth)


    
    start_date = date(2022, 5, 6)
    today_date = date.today() 
    days = start_date - today_date
    # Tweeting with my dev account .days to remove time in seconds
    api.update_status(status = 
    " We are " + str(days.days) + " days to PyconKE 2022 I cannot keep calm!!" " #BuildWhatsNext  #Tweepy #TwitterAPI #PyconKE @VeldaKiara")


challengeDays()


# testing
# try:
#     api.verify_credentials()
#     print("Authentication OK")

# except:
#     print("Error during authentication")

#v2  issues with tweepy client, sol create virtualenv then upgrade
import tweepy
import json

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():

  cfg = {
    "consumer_key"        : "r1h3UrXLgce8tji7diSY6tP3y",
    "consumer_secret"     : "YOX7K8zXlx2zF31rWoLnRLL77q8T39PIY1KeXJai7tNxq3vYHm",
    "access_token"        : "706436613321134080-5tgRztYyUNXjZPuSZQNay8M5GqWlqbG",
    "access_token_secret" : "QExTnHjop1hPp69UpgSIbvRWwhvjmlkMzBrrsGbOjrGoa"
    }
  api = get_api(cfg)
  json_ret = tweepy.Cursor(api.search, q="@realDonaldTrump",count="100").items(100)
  restapi =""
  for tweet in json_ret:
      rest = json.dumps({'tweet' : tweet.text,'user' :str(tweet.user.screen_name), 'location' : str(tweet.place.name if tweet.place else "Undefined place"),
                                                                                 'retweet_count' : tweet.retweet_count, 'created' : str(tweet.created_at)},sort_keys=True,indent=4,separators=(',',': '))
      restapi = restapi+str(rest)+","
  f = open("tweets.json",'a')
  f.write(str(restapi))
  f.close()

if __name__ == "__main__":
  main()


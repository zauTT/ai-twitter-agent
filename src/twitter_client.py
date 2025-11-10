import tweepy
from config import TWITTER_API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def post_tweet(content):
    """
    Post a tweet to Twitter/X.

    Args:
        content(str): Tweet content (max 280 characters).

    Returns:
        Bool: True if successful, False if otherwise.
    """

    if not content:
        print("Error, Tweet content is Empty")
        return False
    
    if len(content) > 280:
        print(f"Error: Tweet is too long ({len(content)} chars.)")
        return False

    try:
        response = client.create_tweet(text=content)
        tweet_id = response.data['id']
        print(f"Tweet posted successfully! ID: {tweet_id}")
        return True

    except tweepy.Forbidden as e:
        print(f"permission error {e}")
        return False

    except tweepy.TooManyRequests as e:
        print(f"rate limit exceeded: {e}")
        return False

    except Exception as e:
        print(f"error posting tweet: {e}")
        return False

if __name__ == "__main__":
      test_tweet = "Testing my Twitter bot! 🤖"
      success = post_tweet(test_tweet)

      if success:
          print("✓ Test successful!")
      else:
          print("✗ Test failed!")

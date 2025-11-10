from content_generator import generate_joke
from twitter_client import post_tweet

def post_ai_joke():
    """Generate and post a joke. Returns True if successful"""

    joke = generate_joke()
    if not joke:
        print("Failed to generate joke")
        return False

    print(f"Generated Joke: {joke}")

    success = post_tweet(joke)
    return success

if __name__ == "__main__":
    print("Testing AI joke bot integration...")
    print("=" * 50)

    success = post_ai_joke()

    print("=" * 50)
    if success:
       print("✓ Integration test successful!")
       print("Check your Twitter profile to see the joke!")
    else:
        print("✗ Integration test failed!")
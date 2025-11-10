from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_joke():
    """
    GENERATE a joke/tweet content using Claude AI
    REturns String containing the joke.
    """

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=150,
            temperature=1.0,
            messages=[
                {
                    "role": "user",
                    "content": "Tell me a short, funny programming joke under 280 characters. Make it unique and creative."
                }
            ]
        )

        joke = response.content[0].text.strip()

        if len(joke) > 280:
            joke = joke[:277] + "..."

        return joke

    except Exception as e:
        print(f"Error generating joke: {e}")
        return None

if __name__ == "__main__":
    print("testing joke generator...")
    joke = generate_joke()
    if joke:
        print(f"\nGenerated joke ({len(joke)} chars):")
        print(joke)
    else:
        print("Failed to generate joke")

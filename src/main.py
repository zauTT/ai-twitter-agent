"""
AI Twitter Bot - Main entry point

Automatically post AI-Generated jokes to Twitter/x at regular intervals.
"""

import sys
from scheduler import start_scheduler
from config import POST_INTERVAL_HOURS

def print_banner():
    """Display startup banner"""
    print("=" * 60)
    print("🤖  AI TWITTER BOT")
    print("=" * 60)
    print("Automated joke posting powered by Claude AI")
    print(f"Interval: Every {POST_INTERVAL_HOURS} hours")
    print("=" * 60)
    print()

def main():
    """Main entry point for the bot"""
    try:
        print_banner()
        start_scheduler()
    
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
        sys.exit(0)

    except Exception as e:
          print(f"\n❌ Fatal error: {e}")
          sys.exit(1)

if __name__ == "__main__":
    main()

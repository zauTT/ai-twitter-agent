"""
AI Twitter Agent - Automated joke posting bot

This package contains all modules for the AI Twitter bot that automatically
posts AI-generated programming jokes to Twitter/X at regular intervals.

Modules:
    config: Configuration and environment variable management
    content_generator: AI joke generation using Claude API
    twitter_client: Twitter/X API integration and posting
    bot_actions: Integration layer combining generation and posting
    scheduler: Job scheduling and automation
    main: Main entry point for the bot

Example:
    Run the bot:
        $ python3 src/main.py

    Test individual components:
        $ python3 src/content_generator.py
        $ python3 src/twitter_client.py
"""

__version__ = "1.0.0"
__author__ = "Giorgi Zautashvili"
__description__ = "AI-powered Twitter bot for automated joke posting"

# Package-level exports (optional)
__all__ = [
    "config",
    "content_generator",
    "twitter_client",
    "bot_actions",
    "scheduler",
    "main"
]

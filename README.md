# AI Twitter Agent

An automated Twitter/X bot that posts AI-generated programming jokes at regular intervals using Claude AI and the Twitter API.

## Features

- **AI-Powered Content**: Generates unique, creative programming jokes using Anthropic's Claude AI
- **Automated Posting**: Posts tweets automatically at configurable intervals
- **Smart Scheduling**: Uses APScheduler for reliable, interval-based posting
- **Error Handling**: Comprehensive error handling for API failures and rate limits
- **Graceful Shutdown**: Clean shutdown handling with Ctrl+C
- **Configurable**: Easy configuration through environment variables
- **Production Ready**: Includes logging, validation, and robust error recovery

## Project Structure

```
ai-twitter-agent/
├── .env                      # API keys and configuration (not in repo)
├── .env.example              # Template for environment variables
├── .gitignore                # Git ignore rules
├── .dockerignore             # Docker ignore rules
├── Dockerfile                # Docker image configuration
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── logs/                     # Log files (auto-generated, not in repo)
│   └── bot.log               # Bot activity logs
└── src/
    ├── __init__.py           # Package initialization
    ├── main.py               # Main entry point
    ├── config.py             # Configuration management
    ├── content_generator.py  # AI joke generation
    ├── twitter_client.py     # Twitter API integration
    ├── bot_actions.py        # Integration layer
    └── scheduler.py          # Scheduling logic
```

## Prerequisites

- Python 3.8 or higher
- Twitter/X Developer Account with API access
- Anthropic API account with API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/zauTT/ai-twitter-agent.git
cd ai-twitter-agent
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API credentials:

```bash
# Twitter/X API Credentials
TWITTER_API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here

# Anthropic API Key
ANTHROPIC_API_KEY=your_anthropic_key_here

# Bot Settings
POST_INTERVAL_HOURS=2
LOG_LEVEL=INFO
```

## Getting API Keys

### Twitter/X API Keys

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new App (or use existing)
3. Set App permissions to **"Read and Write"**
4. Go to "Keys and tokens" tab
5. Copy:
   - API Key and Secret
   - Access Token and Secret (regenerate after changing permissions!)

**Important**: Make sure your app has **"Read and Write"** permissions before generating Access Tokens.

### Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Sign up/Sign in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key immediately (you won't see it again)

## Usage

### Run the Bot

```bash
python3 src/main.py
```

The bot will:
1. Display a startup banner
2. Post an initial joke immediately
3. Continue posting jokes at the configured interval
4. Run until you press Ctrl+C

### Testing with Shorter Intervals

For testing, you can use fractional hours in `.env`:

```bash
# Post every 2 minutes (for testing)
POST_INTERVAL_HOURS=0.033

# Post every 30 minutes
POST_INTERVAL_HOURS=0.5

# Post every 2 hours (production)
POST_INTERVAL_HOURS=2
```

### Individual Component Testing

Test joke generation:
```bash
python3 src/content_generator.py
```

Test tweet posting:
```bash
python3 src/twitter_client.py
```

Test integration:
```bash
python3 src/bot_actions.py
```

## Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `TWITTER_API_KEY` | Twitter API Key | - | Yes |
| `API_SECRET` | Twitter API Secret | - | Yes |
| `ACCESS_TOKEN` | Twitter Access Token | - | Yes |
| `ACCESS_TOKEN_SECRET` | Twitter Access Token Secret | - | Yes |
| `ANTHROPIC_API_KEY` | Anthropic API Key | - | Yes |
| `POST_INTERVAL_HOURS` | Hours between posts | 2 | No |
| `LOG_LEVEL` | Logging level | INFO | No |

### Rate Limits

**Twitter Free Tier:**
- 50 tweets per 24 hours
- Default interval (2 hours) = 12 tweets/day

**Anthropic API:**
- Varies by plan
- Bot uses minimal tokens per request (~150 tokens)

## How It Works

1. **Initialization**: Loads configuration and validates API credentials
2. **Content Generation**: Uses Claude AI to generate unique programming jokes
3. **Tweet Posting**: Posts jokes to Twitter/X using OAuth 1.0a authentication
4. **Scheduling**: APScheduler triggers posts at configured intervals
5. **Error Handling**: Handles API failures, rate limits, and network issues
6. **Logging**: Comprehensive logging of all operations

## Stopping the Bot

Press `Ctrl+C` to gracefully shut down the bot. It will:
- Stop the scheduler
- Log shutdown message
- Exit cleanly

## Logs

The bot logs all activity to both console and file:
- **Console**: Real-time output when running
- **File**: `logs/bot.log` for historical review

View logs:
```bash
# See recent activity
tail -f logs/bot.log

# View entire log file
cat logs/bot.log

# Search logs for errors
grep ERROR logs/bot.log
```

Logs include timestamps, so you can track when jokes were posted and any errors that occurred.

## Running 24/7

### Option 1: Using screen or tmux

```bash
screen -S twitter-bot
python3 src/main.py
# Press Ctrl+A then D to detach
```

Reattach later:
```bash
screen -r twitter-bot
```

### Option 2: Using nohup

```bash
nohup python3 src/main.py > bot.log 2>&1 &
```

### Option 3: systemd Service (Linux)

Create `/etc/systemd/system/twitter-bot.service`:

```ini
[Unit]
Description=AI Twitter Bot
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/ai-twitter-agent
ExecStart=/path/to/ai-twitter-agent/venv/bin/python3 src/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable twitter-bot
sudo systemctl start twitter-bot
```

### Option 4: Docker (Recommended)

Docker provides the easiest way to run the bot in a consistent, isolated environment.

#### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

#### Quick Start with Docker

1. **Ensure your `.env` file is configured** (Docker will use it automatically)

2. **Build and start the container:**
```bash
docker-compose up -d
```

3. **View logs:**
```bash
docker-compose logs -f
```

4. **Stop the bot:**
```bash
docker-compose down
```

#### Docker Commands

**Build the image:**
```bash
docker-compose build
```

**Start the bot in the background:**
```bash
docker-compose up -d
```

**View real-time logs:**
```bash
docker-compose logs -f twitter-bot
```

**Stop the bot:**
```bash
docker-compose stop
```

**Restart the bot:**
```bash
docker-compose restart
```

**Remove container and image:**
```bash
docker-compose down
docker rmi ai-twitter-agent
```

#### Using Docker without Docker Compose

**Build the image:**
```bash
docker build -t ai-twitter-agent .
```

**Run the container:**
```bash
docker run -d \
  --name ai-twitter-agent \
  --env-file .env \
  -v $(pwd)/logs:/app/logs \
  --restart unless-stopped \
  ai-twitter-agent
```

**View logs:**
```bash
docker logs -f ai-twitter-agent
```

**Stop the container:**
```bash
docker stop ai-twitter-agent
```

#### Docker Advantages

- **Isolated Environment**: No conflicts with system Python or packages
- **Easy Deployment**: Works the same on any machine
- **Auto-restart**: Container restarts automatically if it crashes
- **Simple Updates**: Rebuild and restart to update
- **Resource Limits**: Optionally limit CPU/memory usage
- **Clean Removal**: Delete container without affecting system

#### Development with Docker

To mount source code for live development (changes reflect without rebuild):

1. Uncomment the volume mount in `docker-compose.yml`:
```yaml
volumes:
  - ./logs:/app/logs
  - ./src:/app/src  # Uncomment this line
```

2. Restart the container:
```bash
docker-compose restart
```

## Troubleshooting

### "403 Forbidden" Error
- Check that your Twitter app has "Read and Write" permissions
- Regenerate Access Token and Secret after changing permissions

### "401 Unauthorized" Error
- Verify all 4 Twitter credentials are correct in `.env`
- Check for extra spaces or quotes in `.env` file

### "Rate Limit Exceeded"
- Wait for the rate limit window to reset
- Increase `POST_INTERVAL_HOURS` to post less frequently

### Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Bot Stops After Closing Terminal
- Use `screen`, `tmux`, or `nohup` to run in background
- Or set up as a systemd service

## Development

### Project Architecture

- **config.py**: Centralized configuration management
- **content_generator.py**: Claude AI integration for joke generation
- **twitter_client.py**: Twitter API wrapper with error handling
- **bot_actions.py**: Integration layer combining generation and posting
- **scheduler.py**: APScheduler setup with signal handling
- **main.py**: Entry point with startup banner

### Adding New Features

To modify joke style, edit `content_generator.py`:
```python
"content": "Tell me a [your style] joke under 280 characters."
```

To change scheduling behavior, edit `scheduler.py`:
```python
scheduler.add_job(
    trigger='interval',  # or 'cron' for specific times
    hours=POST_INTERVAL_HOURS
)
```

## Security Notes

- **Never commit `.env` file** to version control
- Keep your API keys secure and private
- Rotate API keys periodically
- Monitor API usage and costs
- Use read-only keys where possible (except Twitter which needs write access)

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [Anthropic Claude AI](https://www.anthropic.com/) for joke generation
- [Tweepy](https://www.tweepy.org/) for Twitter API integration
- [APScheduler](https://apscheduler.readthedocs.io/) for job scheduling

## Support

For issues or questions, please open an issue on GitHub.

---

Built with love and AI

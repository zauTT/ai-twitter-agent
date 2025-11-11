import logging
import signal
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from bot_actions import post_ai_joke
from config import POST_INTERVAL_HOURS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/bot.log', mode='a')
    ]
)

scheduler=BlockingScheduler()

def scheduled_job():
    """"Job that runs every interval"""
    logging.info("=" * 60)
    logging.info("Starting scheduled tweet job...")

    try:
        success = post_ai_joke()

        if success:
            logging.info("✓ Tweet posted successfully!")
        else:
            logging.error("✗ Failed to post tweet")

    except Exception as e:
        logging.error(f"Error in scheduling job: {e}")

    logging.info("=" * 60)

def signal_handler(sig, frame):
    """Handle graceful shutdown on Ctrl+C"""
    logging.info("\n🛑 Shutting down scheduler gracefully...")
    scheduler.shutdown()
    sys.exit(0)

def start_scheduler():
    """Start the Scheduler"""

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    scheduler.add_job(
        func=scheduled_job,
        trigger='interval',
        hours=POST_INTERVAL_HOURS,
        id="tweet_job",
        name="Post ai joke to Twitter",
        replace_existing=True
    )

    logging.info("🤖 AI Twitter Bot Scheduler Started!")
    logging.info(f"⏰ Will post jokes every {POST_INTERVAL_HOURS} hours")
    logging.info("Press Ctrl+C to stop\n")

    logging.info("Running initial tweet job...")
    scheduled_job()

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Scheduler stopped")

if __name__ == "__main__":
    start_scheduler()
        
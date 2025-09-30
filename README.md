# Telegram Referral Bot

A feature-rich Telegram bot built with aiogram 3.x that implements a referral system with user tracking and admin management capabilities.

## Features

### User Features
- **Referral System**: Users can invite friends using unique referral links
- **Channel Subscription Check**: Ensures users are subscribed to a specified channel before accessing the bot
- **User Profiles**: View personal statistics including unique ID and referral count
- **Leaderboard**: Display top 10 users by referral count

### Admin Features
- **User Management**: View complete list of registered users
- **Statistics Dashboard**: Monitor total users and referrals
- **Admin Panel**: Easy-to-use interface for administrative tasks

## Commands

- `/start` - Start the bot and get your referral link
- `/myprofile` - View your profile information
- `/top` - See the top 10 referrers leaderboard
- `/admin` - Access admin panel (admin only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MuttaqiynDev/konkurs-bot.git
cd telegram-referral-bot
```

2. Install dependencies:
```bash
pip install requirenents.txt
```

3. Create a `config.py` file with your settings:
```python
BOT_TOKEN = "your_bot_token_here"
CHANNEL_ID = -1001234567890  # Your channel ID
ADMINS = [123456789] 
```


## Author

[MuttaqiynDev](https://github.com/MuttaqiynDev)

---

⭐ If you find this project useful, please give it a star on GitHub!

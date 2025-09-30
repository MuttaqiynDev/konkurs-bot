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


## Project Structure

```
telegram-referral-bot/
├── main.py              # Bot initialization and startup
├── handlers.py          # Command and callback handlers
├── database.py          # Database operations
├── keyboards.py         # Inline keyboard layouts
├── config.py           # Configuration settings
└── README.md           # This file
```

## How It Works

### Referral System
1. Each user gets a unique referral link when they start the bot
2. When a new user joins via a referral link, the inviter's count is incremented
3. The inviter receives a notification about the new referral
4. Users can track their referral statistics in their profile

### Subscription Verification
- Before accessing any features, users must join the specified channel
- The bot checks subscription status using Telegram's API
- Users can verify their subscription using the "Check Subscription" button

## Configuration

Edit `config.py` to customize:

- `BOT_TOKEN`: Your Telegram bot token from @BotFather
- `CHANNEL_ID`: The channel users must subscribe to (use negative ID for channels)
- `ADMINS`: List of user IDs who have admin access

## Database Schema

The bot requires the following user data structure:
- User Telegram ID
- User name
- Unique bot-assigned ID
- Inviter ID (nullable)
- Referral count

## Requirements

- Python 3.8+
- aiogram 3.x
- A Telegram Bot Token
- A database (implementation not included)

## Admin Panel

Admins can access additional features through the `/admin` command:
- View all registered users with clickable profile links
- Check bot statistics (total users and referrals)
- Monitor bot performance and user engagement

## Security Notes

- Admin access is restricted to user IDs listed in `ADMINS`
- All admin callbacks verify user permissions before executing
- User data is protected through proper access control

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Author

Your Name - [MuttaqiynDev](https://github.com/MuttaqiynDev)

---

⭐ If you find this project useful, please give it a star on GitHub!

import aiosqlite
from config import DATABASE_NAME

async def create_db():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            unique_bot_id INTEGER,
            referral_count INTEGER DEFAULT 0,
            invited_by INTEGER
        )''')
        await db.commit()

async def add_user(user_id, first_name, invited_by=None):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        # Get next auto-incremented ID
        cursor = await db.execute("SELECT MAX(unique_bot_id) FROM users")
        max_id = await cursor.fetchone()
        new_id = 1 if max_id[0] is None else max_id[0] + 1

        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, first_name, unique_bot_id, invited_by) VALUES (?, ?, ?, ?)",
            (user_id, first_name, new_id, invited_by)
        )
        await db.commit()
        return new_id

async def get_user(user_id):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        return await cursor.fetchone()

async def increment_referral_count(inviter_id):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            "UPDATE users SET referral_count = referral_count + 1 WHERE user_id=?",
            (inviter_id,)
        )
        await db.commit()

async def get_top_referrals():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.execute(
            "SELECT first_name, referral_count FROM users ORDER BY referral_count DESC LIMIT 10"
        )
        return await cursor.fetchall()

async def get_total_stats():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.execute("SELECT COUNT(*), SUM(referral_count) FROM users")
        return await cursor.fetchone()

async def get_all_users():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.execute("SELECT user_id, first_name FROM users")
        return await cursor.fetchall()
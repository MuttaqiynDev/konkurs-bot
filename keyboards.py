from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def check_sub_keyboard():
    ''' Keyboard for checking channel subscription '''
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Join Channel", url="https://t.me/PythonuzHUB"),
        InlineKeyboardButton(text="✅ Check Subscription", callback_data="check_sub")
    ]])

def referral_keyboard(link):
    ''' Keyboard for sharing referral link '''
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Share Referral Link", url=f"https://t.me/share/url?url={link}")
    ]])

def admin_keyboard():
    ''' admin panel keyboard '''
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👥 Users", callback_data="admin_users")],
        [InlineKeyboardButton(text="📊 Stats", callback_data="admin_stats")]
    ])
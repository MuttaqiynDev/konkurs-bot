from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from config import ADMINS, CHANNEL_ID
from database import add_user, get_user, increment_referral_count, get_top_referrals, get_total_stats, get_all_users
from keyboards import check_sub_keyboard, referral_keyboard, admin_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message, bot):
    ''' Handle /start command '''
    # Check if user is subscribed
    member = await bot.get_chat_member(CHANNEL_ID, msg.from_user.id)
    if member.status in ["left", "kicked"]:
        await msg.answer(
            "📢 Please join our channel to use this bot!",
            reply_markup=check_sub_keyboard()
        )
        return

    # Extract referral ID from deep link
    inviter_id = None
    if len(msg.text.split()) > 1:
        start_arg = msg.text.split()[1]
        if start_arg.startswith("ref_"):
            try:
                inviter_id = int(start_arg.split("_")[1])
            except (ValueError, IndexError):
                pass

    # Register user
    user = await get_user(msg.from_user.id)
    if not user:
        bot_id = await add_user(msg.from_user.id, msg.from_user.first_name, inviter_id)

        # Update referral count if applicable
        if inviter_id:
            await increment_referral_count(inviter_id)
            try:
                await bot.send_message(
                    inviter_id,
                    f"🎉 New referral! {msg.from_user.first_name} joined using your link!"
                )
            except:
                pass
    else:
        bot_id = user[2]

    # Generate referral link
    ref_link = f"https://t.me/{(await bot.get_me()).username}?start=ref_{msg.from_user.id}"

    # Send welcome message
    await msg.answer(
        f"👋 Welcome {msg.from_user.first_name}!\n\n"
        f"Your unique ID: {bot_id}\n"
        f"Your referral link:\n{ref_link}",
        reply_markup=referral_keyboard(ref_link)
    )


@router.callback_query(F.data == "check_sub")
async def check_sub_handler(query: CallbackQuery, bot):
    ''' Check if user has subscribed to the channel '''
    member = await bot.get_chat_member(CHANNEL_ID, query.from_user.id)
    if member.status in ["left", "kicked"]:
        await query.answer("You're still not subscribed! ❌", show_alert=True)
    else:
        await query.message.delete()
        await start_handler(query.message, bot)


@router.message(Command("myprofile"))
async def profile_handler(msg: Message):
    ''' Show user's profile '''
    user = await get_user(msg.from_user.id)
    if user:
        await msg.answer(
            f"👤 Your Profile\n\n"
            f"ID: {user[2]}\n"
            f"Name: {user[1]}\n"
            f"Referrals: {user[4]}"
        )


@router.message(Command("top"))
async def top_handler(msg: Message):
    ''' Show top 10 users by referrals '''
    top_users = await get_top_referrals()
    response = "🏆 Top 10 Referrals:\n\n"
    for i, (name, count) in enumerate(top_users, 1):
        response += f"{i}. {name}: {count} referrals\n"
    await msg.answer(response)


@router.message(Command("admin"))
async def admin_handler(msg: Message):
    ''' Admin panel access '''
    if msg.from_user.id in ADMINS:
        await msg.answer("Admin Panel:", reply_markup=admin_keyboard())


@router.callback_query(F.data.startswith("admin_"))
async def admin_callback_handler(query: CallbackQuery):
    ''' Handle admin panel actions '''
    if query.from_user.id not in ADMINS:
        await query.answer("Access denied!", show_alert=True)
        return

    action = query.data.split("_")[1]

    if action == "users":
        users = await get_all_users()
        response = "👥 Users List:\n\n"
        for user in users:
            response += f"• <a href='tg://user?id={user[0]}'>{user[1]}</a>\n"
        await query.message.edit_text(response, parse_mode="HTML")

    elif action == "stats":
        total_users, total_refs = await get_total_stats()
        await query.message.edit_text(
            f"📊 Bot Statistics\n\n"
            f"Total Users: {total_users}\n"
            f"Total Referrals: {total_refs if total_refs else 0}"
        )

    await query.answer()

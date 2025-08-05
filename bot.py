import nest_asyncio
import asyncio
from pyrogram import Client, filters
import google.generativeai as genai
import requests

# Apply for Jupyter/Colab
nest_asyncio.apply()

# ====== CONFIGURATION ======
API_ID = 23200475
API_HASH = "644e1d9e8028a5295d6979bb3a36b23b"
BOT_TOKEN = "7713211393:AAEUh5lug3dizn85fhjLGV9b3a4UVr8exi8"
GEMINI_API_KEY = "AIzaSyChQIakiViRcGIEC4fy0yAJ3a1hVkmuzak"

# Init Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Init Telegram Bot
bot = Client("VaginiBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ====== ANIME FETCHER FUNCTION ======
def get_latest_anime():
    try:
        url = "https://api.jikan.moe/v4/seasons/now"
        response = requests.get(url)
        data = response.json()

        top_5 = data["data"][:5]
        reply = "**📺 Top Airing Anime (Now):**\n\n"
        for anime in top_5:
            title = anime["title"]
            episodes = anime.get("episodes", "?")
            score = anime.get("score", "N/A")
            reply += f"• **{title}** – {episodes} eps | ⭐ {score}\n"
        return reply
    except Exception as e:
        return f"❌ Error fetching anime info: {e}"

# ====== TELEGRAM HANDLER ======
@bot.on_message(filters.group & filters.text)
async def handle_group_msg(client, message):
    user_msg = message.text.strip().lower()

    try:
        print(f"[{message.chat.title}] {message.from_user.first_name}: {user_msg}")

        # Anime command trigger
        if "anime" in user_msg:
            response = get_latest_anime()

        # Default Gemini AI reply
        else:
            gemini_response = model.generate_content(user_msg)
            response = f"**🤖 Vagini says:**\n{gemini_response.text}"

        await message.reply_text(response)
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {e}")

# ====== BOT MAIN ======
async def main():
    await bot.start()
    print("✅ Vagini bot is running...")
    await asyncio.Event().wait()

asyncio.run(main())

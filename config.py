import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-domain.com/webapp")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN topilmadi! .env faylini yarating (.env.example dan nusxa oling) "
        "va BOT_TOKEN ni to'ldiring."
    )

# IELTS Prep Bot — ishga tushirish

## 1. Muhitni tayyorlash

```bash
cd ielts_bot
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Token sozlash

`.env.example` faylidan nusxa oling:

```bash
cp .env.example .env
```

`.env` faylini oching va `BOT_TOKEN` qatoriga @BotFather bergan tokenni qo'ying.

## 3. Botni ishga tushirish (hozircha Mini App'siz test)

```bash
python bot.py
```

Telegram'da botingizga `/start` yuboring — u javob berishi kerak. Mini App tugmasi
hozircha ishlamaydi, chunki `WEBAPP_URL` haqiqiy manzil emas (Telegram Mini App
**faqat https manzilda** ishlaydi, localhost bilan ishlamaydi).

## 4. Mini App'ni onlayn joylashtirish (keyingi qadam)

Mini App'ni ko'rish uchun `webapp/index.html` faylini https orqali ochiladigan
joyga qo'yish kerak. Eng tez yo'llar:

- **GitHub Pages** — bepul, oddiy statik sahifalar uchun yetarli
- **Vercel / Netlify** — bepul tier, bir necha daqiqada deploy qilish mumkin
- **Ngrok** — faqat local test uchun (`ngrok http 8000` kabi), doimiy emas

Deploy qilgandan so'ng, `.env` faylidagi `WEBAPP_URL` ni haqiqiy manzilga
almashtiring va botni qayta ishga tushiring.

## Keyingi bosqichlar (rejada)

- [ ] Vocabulary bo'limi — so'zlar bazasi + spaced repetition
- [ ] Grammar mashqlari
- [ ] Listening audio + savollar
- [ ] Speaking — ovozli xabar qabul qilish, Whisper orqali matnga o'girish
- [ ] Writing — matn qabul qilish, Claude API orqali baholash
- [ ] Mini App'dan bot serveriga ma'lumot yuborish (Telegram WebApp `sendData` yoki backend API)

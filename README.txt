README - Telegram webhook bot for Render

Fayllar:
- main.py         : Flask webhook server (TOKEN ni env orqali o'qiydi)
- requirements.txt: Kerakli kutubxonalar
- .env.example    : Misol uchun muhit o'zgaruvchilari

Qanday ishlatish (Render):
1) Github reposiga ushbu fayllarni joylang.
2) Render.com ga kiring → New + → Web Service.
3) GitHub reposni tanlang.
4) Runtime: Python, Start Command: python main.py
5) Environment variables ga qo'shing:
   - TOKEN = sizning_bot_tokeningiz
6) Deploy qiling. Render sizga URL beradi, masalan:
   https://seningboting.onrender.com

7) Webhook o'rnatish uchun brauzerga quyidagilarni yozing:
   https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://seningboting.onrender.com/webhook

Eslatma:
- TOKEN ni hech qachon public joyga qo'ymang.
- Agar lokalda sinash uchun raw ngrok yoki boshqa tunneling ishlatsa bo'ladi.

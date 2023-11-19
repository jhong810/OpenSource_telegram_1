import telegram
import asyncio
import time


now = time

async def send():
    token =""
    bot = telegram.Bot(token = token)
    chat_id = ""

    await bot.sendMessage(chat_id=chat_id,text=now.strftime('현재 시간 : %Y-%m-%d %H:%M:%S'))

async def main():
    while True:
        if(now.localtime().tm_hour>5 and now.localtime().hour<=22):
            await send()
        time.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
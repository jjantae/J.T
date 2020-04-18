import asyncio
import discord
from discord import file

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzAxMTEyMjg4NzMxNDYzNzEy.XpswwA.Ui1W8uJ3m4N9RMDEEKg9kuHqa50"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('반가워요!')
    if message.content.startswith('!짠태봇'):
        channel = message.channel
        await channel.send('현재 개발중...')
    if message.content.startswith('!뭐해?'):
        channel = message.channel
        await channel.send('그러게요..?')
    if message.content.startswith('!배고파'):
        channel = message.channel
        await channel.send('밥드세요')
    if message.content.startswith('!천안문'):
        channel = message.channel
        await channel.send('사랑합니다')

    if message.content.startswith('!짤'):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

client.run(token)

import asyncio
import discord
from discord.ext import commands
import random
from pprint import pprint

TOKEN = "OTQwMzkxMjA0Mjc1NzY5NDE1.YgGtjg.zVB4IBlRHJ712ggz0gkM0lnmchI"
bot = commands.Bot(command_prefix='!')

current_task = '-1'
all_tasks = {}
with open('егэ по физике задания.txt', encoding='utf-8', mode="r") as f:
    tasks = f.read()
    tasks = tasks.split(';;;')
    for i in tasks:
        isplited = i.split('--')
        print(isplited)
        all_tasks[isplited[0].strip('\n')] = [isplited[1].strip('\n'),
                                              isplited[2].strip('\n'),
                                              isplited[3].strip('\n'),
                                              isplited[4].strip('\n')]
                                              #0 - номер задания, 1 - ответ, 2 - картинки, 3 - пояснение, 4 - само задание

pprint(all_tasks)


@bot.command(name='задание')
async def tasks(ctx, number):
    global current_task
    await ctx.send('x')
    one_task = []
    for i in list(all_tasks):
        if str(i[:i.find('.')]) == str(number):
            one_task.append(i)

    current_task = random.choice(one_task)
    pictures = all_tasks[current_task][1]
    if pictures == 'none':
        await ctx.send(all_tasks[current_task][3])
    else:
        await ctx.send('x')


@bot.event
async def on_message(message):
    global current_task
    await bot.process_commands(message)
    if message.author == bot.user or '!' in message.content:
        return
    if 'анекдот' in message.content:
        await message.channel.send("а я тоже анекдотики знаю... Вот команда - !анекдот")
        return

    if message.content == all_tasks[current_task][0]:
        await message.channel.send("правильно!")
        await tasks(message.channel, current_task)
        return
    elif message.content == 'подсказка':
        if all_tasks[current_task][2] == 'none':
            await message.channel.send('подсказок к этому заданию нет.')
            return
        else:
            await message.channel.send(all_tasks[current_task][2])
            return
    else:
        await message.channel.send('неверно, попробуйте еще раз!')
        return


bot.run(TOKEN)



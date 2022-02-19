import asyncio
import discord
from discord.ext import commands
import random
from pprint import pprint

TOKEN = "OTQwMzkxMjA0Mjc1NzY5NDE1.YgGtjg.zVB4IBlRHJ712ggz0gkM0lnmchI"

bot = commands.Bot(command_prefix='!')


class RandomThings(commands.Cog):
    def __init__(self, bt):
        self.bot = bt
        self.current_task = '-1'
        self.all_tasks = {}
        with open('егэ по физике задания.txt', encoding='utf-8', mode="r") as f:
            tasks = f.read()
            tasks = tasks.split(';;;')
            for i in tasks:
                isplited = i.split('--')
                self.all_tasks[isplited[0].strip('\n')] = [isplited[1].strip('\n'),
                                                           isplited[2].strip('\n'),
                                                           isplited[3].strip('\n'),
                                                           isplited[4].strip('\n')]
                # 1 - номер задания, 2 - картинки, 3 - пояснение, 4 - само задание

    @bot.event
    async def on_message(self, message):
        pprint(message.content)
        pprint(self.all_tasks[self.current_task])

        if message.content == self.all_tasks[self.current_task]:
            await message.channel.send("правильно!")
            self.tasks(self.current_task[:self.current_task.find('.')])
        else:
            await ctx.send('неверно, попробуйте еще раз!')

    @bot.command(name='задание')
    async def tasks(self, ctx, number):
        one_task = []
        for i in list(self.all_tasks):
            if i[:i.find('.')].strip('\n') == number:
                one_task.append(i.strip('\n'))

        self.current_task = random.choice(one_task)
        pictures = self.all_tasks[self.current_task][1]
        if pictures == 'none':
            await ctx.send(self.all_tasks[self.current_task][3])
        else:
            await ctx.send({files: [pictures]})


bot.run(TOKEN)


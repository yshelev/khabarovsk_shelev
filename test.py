import asyncio
import discord
from discord.ext import commands
import random
from pprint import pprint


class RandomThings(commands.Cog):
    def __init__(self, bt):
        self.bot = bt

    @commands.command(name='задание')
    async def tasks(self, ctx, number):
        with open('егэ по физике задания.txt', encoding='utf-8', mode="r") as f:
            tasks = f.read()
            tasks = tasks.split(';;;')
            all_tasks = {}
            one_task = []
            pprint(tasks)
            for i in tasks:
                isplited = i.split('--')
                all_tasks[isplited[0].strip('\n')] = [isplited[1].strip('\n'),
                                                      isplited[2].strip('\n'),
                                                      isplited[3].strip('\n'),
                                                      isplited[4].strip('\n')]
                # 1 - номер задания, 2 - картинки, 3 - пояснение, 4 - само задание

            for i in list(all_tasks):
                if i[:i.find('.')].strip('\n') == number:
                    one_task.append(i.strip('\n'))

            number_of_task = random.choice(one_task)
            pictures = all_tasks[number_of_task][1]
            if pictures == 'none':
                await ctx.send(all_tasks[number_of_task][3])
            else:
                await ctx.send({files: [pictures]})

TOKEN = "OTQwMzkxMjA0Mjc1NzY5NDE1.YgGtjg.zVB4IBlRHJ712ggz0gkM0lnmchI"

bot = commands.Bot(command_prefix='!')
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)


import asyncio
import discord
from discord.ext import commands
import random
from pprint import pprint
import json
import requests
from random import *

TOKEN = "OTQwMzkxMjA0Mjc1NzY5NDE1.YgGtjg.zVB4IBlRHJ712ggz0gkM0lnmchI"
bot = commands.Bot(command_prefix='!')

current_task = '-1'
current_command = -1
all_tasks = {}
with open('егэ по физике задания.txt', encoding='utf-8', mode="r") as f:
    tasks = f.read()
    tasks = tasks.split(';;;')
    for i in tasks:
        isplited = i.split('--')
        all_tasks[isplited[0].strip('\n')] = [isplited[1].strip('\n'),
                                              isplited[2].strip('\n'),
                                              isplited[3].strip('\n'),
                                              isplited[4].strip('\n')]
                                              #0 - номер задания, 1 - ответ, 2 - картинки, 3 - пояснение, 4 - само задание


@bot.command(name='задание')
async def tasks(ctx, number):
    global current_task, current_command
    current_command = 0
    one_task = []
    for i in list(all_tasks):
        if str(i[:i.find('.')]) == str(number):
            one_task.append(i)

    await ctx.send(one_task)
    current_task = random.choice(one_task)
    pictures = all_tasks[current_task][1]
    if pictures == 'none':
        await ctx.send(all_tasks[current_task][3])
    else:
        await ctx.send('x')


@bot.command(name='большиефакты')
async def bignumbers(ctx):
    global current_command
    current_command = 1
    response = requests.get('http://numbersapi.com/random/year?json').json()

    await ctx.send('факт о: ' + str(response['number']) + ' - ' + str(response['text']))


@bot.command(name='маленькиефакты')
async def smallnumbers(ctx, num):
    global current_command
    current_command = 2
    response = requests.get('http://numbersapi.com/1..100').json()
    await ctx.send('факт о: ' + str(num) + ' - ' + response[str(num)])


@bot.command(name='скучно')
async def bored(ctx):
    global current_command
    current_command = 3
    response = requests.get('http://www.boredapi.com/api/activity/').json()
    await ctx.send(response['activity'])
    await ctx.send('а помимо этого, я тебе могу анекдот рассказать)')
    await anekdot(ctx)


@bot.command(name='узнатьмасть')
async def mast(ctx):
    global current_command
    a = {'2': 'двойка', '3': 'тройка', '4': 'четверка', '5': 'пятерка',
         '6': 'шестерка', '7': 'семерка', '8': "восьмерка", '9': 'девятка', '10': 'десятка',
         "QUEEN": 'королева', "KING": 'король',
         "ACE": 'туз', 'JACK': 'валет', "CLUBS": 'трефовый(ая)',
         "SPADES": "пиковый(ая)", "HEARTS": "червовый(ая)", "DIAMONDS": "бубовый(ая)"}
    current_command = 4
    deck = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
    card = requests.get('https://deckofcardsapi.com/api/deck/' + deck["deck_id"] + '/draw/?count=1').json()
    pprint(card)
    pprint(deck)
    if card['cards'][0]["value"] in list(a):
        await ctx.send('ты по масти ' + a[card['cards'][0]["value"]] + ' ' + a[card['cards'][0]["suit"]])
        await ctx.send(card['cards'][0]["image"])
    else:
        await ctx.send('ты по масти ' + card['cards'][0]["value"] + ' ' + a[card['cards'][0]["suit"]])
        await ctx.send(card['cards'][0]["image"])


@bot.command(name='мяу')
async def meow(ctx):
    global current_command
    current_command = 5
    animal = requests.get('https://aws.random.cat/meow').json()
    await ctx.send(animal['file'])


@bot.command(name='помощь')
async def help(ctx):
    global current_command
    current_command = 100
    await ctx.send('есть факты о числах(!маленькиефакты + число от 1 до 100 !большиефакты)')
    await ctx.send('задание эге по физике(!задание + его номер)')
    await ctx.send('что делать когда скучно(!скучно)')


@bot.command(name='анекдот')
async def anekdot(ctx):
    global current_command
    current_command = 6
    shutka = requests.get('http://rzhunemogu.ru/Rand.aspx?CType=1')
    await ctx.send(shutka.text.split('<content>')[1].split('</content>')[0])


@bot.command(name='стих')
async def stih(ctx):
    global current_command
    current_command = 7
    shutka = requests.get('http://rzhunemogu.ru/Rand.aspx?CType=3')
    await ctx.send(shutka.text.split('<content>')[1].split('</content>')[0])


@bot.command(name='цитата')
async def citata(ctx):
    global current_command
    current_command = 8
    shutka = requests.get('http://rzhunemogu.ru/Rand.aspx?CType=5')
    await ctx.send(shutka.text.split('<content>')[1].split('</content>')[0])


@bot.command(name='статус')
async def status(ctx):
    global current_command
    current_command = 9
    shutka = requests.get('http://rzhunemogu.ru/Rand.aspx?CType=8')
    await ctx.send(shutka.text.split('<content>')[1].split('</content>')[0])


@bot.command(name='данет')
async def yesorno(ctx):
    global current_command
    a = {'no': 'нет', 'yes': 'да', 'maybe': 'наверное..'}
    current_command = 10
    yon = requests.get('https://yesno.wtf/api').json()
    print(yon)
    await ctx.send(a[yon['answer']])
    await ctx.send(yon['image'])


@bot.command(name='изображение')
async def randomimage(ctx):
    global current_command
    current_command = 11
    image = requests.get('https://picsum.photos/200/300').json()
    await ctx.send(image.text)


@bot.command(name='аниме')
async def anime(ctx, *name):
    global current_command
    current_command = 12
    animelist = requests.get('https://api.jikan.moe/v4/anime?q=' + ' '.join(name)).json()
    for i in animelist['data'][:5]:
        await ctx.send(i['images']['jpg']['large_image_url'])
        await ctx.send('название: ' + i['title'])
        await ctx.send('синопсис: ' + i['synopsis'])
        await ctx.send('кол-во эпизодов: ' + str(i["episodes"]))
        await ctx.send("длительность эпизода: " + i["duration"])
        await ctx.send("статус: " + i["status"])


@bot.command(name='биток')
async def bitcoin(ctx):
    global current_command
    current_command = 12
    bitok = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    pprint(bitok)
    await ctx.send(bitok['bpi']['USD']['rate'][:bitok['bpi']['USD']['rate'].find('.')] + ' ' + bitok['bpi']['USD']['code'])


@bot.command(name='придумайчеловека')
async def randombro(ctx):
    global current_command
    current_command = 12
    bro = requests.get('https://randomuser.me/api/').json()
    pprint(bro)
    await ctx.send('имя - ' + bro['results'][0]['name']['first'])
    await ctx.send('гендер - ' + bro['results'][0]['gender'])
    await ctx.send("возраст - " + str(bro['results'][0]['dob']['age']))
    await ctx.send("страна проживания - " + bro['results'][0]['location']['country'])
    await ctx.send("улица - " + bro['results'][0]['location']['street']['name'] + ' ' + str(bro['results'][0]['location']['street']['number']))
    await ctx.send("телефон - " + bro['results'][0]['phone'])
    await ctx.send("email: " + bro['results'][0]['email'])
    await ctx.send('любимый никнейм - ' + bro['results'][0]['login']['username'])
    await ctx.send('любимый пароль - ' + bro['results'][0]['login']['password'])
    await ctx.send('фото: ')
    await ctx.send(bro['results'][0]['picture']['large'])


@bot.event
async def on_message(message):
    global current_task
    await bot.process_commands(message)
    if current_command == 0:
        if message.author == bot.user or '!' in message.content:
            return
        if 'анекдот' in message.content:
            await message.channel.send("а я тоже анекдотики знаю... Вот команда - !анекдот")
            return

        if message.content == all_tasks[current_task][0]:
            await message.channel.send("правильно!")
            await tasks(message.channel, current_task[:current_task.find('.')])
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



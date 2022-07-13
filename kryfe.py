import discord
from random import choice
from discord.ext import commands

kryfe = commands.Bot(command_prefix = '@Толерантный 2', bot = True)

@bot.event
async def on_ready():
  while True:
    try:
      question = await kryfe.wait_for(stupid_question, timeout = 9999)
    except TimeoutExcept:
      await voice.leave()
    else:
      list = [other.stupid.question, stupid.answer, ignore]
      await question.reply(choice(list))

async def mind(thing):
  try:
    await thing.mind()
  except:
    await thing.reply('Мне рано еще думать')
  else:
    await thing.reply(stupid_answer)
        

bot.run('kryfe.lox')

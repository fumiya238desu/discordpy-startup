from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def しおみ(msg):
    if msg.author.bot:
        # Botの発言に反応しないようにするため必須
        return

    if msg.content:
        # ローカルのファイルを送信する場合は以下の用に書く
        file_img = discord.File("C:\Users\test\Pictures\shiomi")
        await msg.channel.send(File=file_img)

 
bot.run(token)

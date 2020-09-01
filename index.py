import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

#primero asignamos un prefijo al bot, para poder comunicarse con el.
bot = commands.Bot(command_prefix=".", description="Bot de Mateo Ifrán.")

#ejecutamos el decorador llamado "command" que nos permite crear un comando.
@bot.command()
#pero vamos a tener que manejar ese comando con una funcion
async def botinfo(ctx):
    #el async y await es para que espere un momento antes de ejecutarse
    embed = discord.Embed(title="Bot desarrollado por Mateo Ifrán.", description="Por ahora puedo hacer poco, pero la forma de utilizarme es poniendo un punto como prefijo. Por ejemplo: .mateo \n \n Cosas que puedo hacer hasta ahora: \n \n -Busco videos de youtube, solo con el comando: .yt /seguido de lo que quieras buscar.\n \n -Describo a cada participante del chat 'Bar de manolo'. Solo tenes que poner el prefijo y el nombre del participante. \n \n -Se sumar!! Solamente pone: .suma (numeros que quieras sumar separados por un espacio). \n \n Con .info puedo mostrarte la información del servidor." , timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

#SUMA
@bot.command()
async def suma(ctx, numero1: float, numero2: float):
    await ctx.send(numero1 + numero2)
#MOSTRAR ESTADISTICAS
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Marginados y exiliados, sean bienvenidos.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url=) //esto sirve para agregar una imagen
    
    await ctx.send(embed=embed)
    
#COMANDOS DE OPINION HACIA LOS USUARIOS
@bot.command()
async def mateo(ctx):
    await ctx.send("Mateo me controla. Estoy obligado a decir que es un genio.")
@bot.command()
async def leme(ctx):
    await ctx.send("Antes se escuchaba el rumor de que se la comía. Pero ahora sabemos que solo se come balas del Cs Go.")
@bot.command()
async def rodri(ctx):
    await ctx.send("El viejo es un tierno, pero se hace el duro.")
@bot.command()
async def lea(ctx):
    await ctx.send("Un talentoso en el arte. (pero colorado :/)")
@bot.command()
async def fede(ctx):
    await ctx.send("Tiene que tomarse la vida con calma y dejar de empastillarse.")
@bot.command()
async def walter(ctx):
    await ctx.send("No importa cual sea la actividad. El te va a poner una excusa de porque no es el mejor en eso.")
@bot.command()
async def lucas(ctx):
    await ctx.send("Sabemos que es el más turbio de todos, aún asi lo queremos.")
@bot.command()
async def mauri(ctx):
    await ctx.send("Un blandito, fan de Auron y laburador (jajajajaja).")
@bot.command()
async def bon(ctx):
    await ctx.send("Él te bardea por las dudas, ni se lo piensa.")
@bot.command()
async def nacho(ctx):
    await ctx.send("Casi todo le da paja, le da paja hasta tener paja.")
@bot.command()
async def fer(ctx):
    await ctx.send("Fer, su risa lo incrimina más y más. Atras señor Fer AHHHHHHAIUSDHJIUASDHI")
@bot.command()
async def rusa(ctx):
    await ctx.send("Ansiosa, copada y juega bien al Cs 1.6 ¿Qué más queres?")
@bot.command()
async def pri(ctx):
    await ctx.send("Cara de angel pero fan del kpop, una lástima. Aunque buen gusto para el anime.")
@bot.command()
async def saul(ctx):
    await ctx.send("De forma unánime creemos que es el más confiable, aunque sea un rompehuevos de Jojo's.")
@bot.command()
async def gaston(ctx):
    await ctx.send("Un talentoso que puede jugar al Counter sin mouse, un distinto.")

#YOUTUBE
@bot.command()
async def yt(ctx, *, search):
    #estas son las palabras que el usuario busca
    query_string = parse.urlencode({'search_query': search})
    #le hacemos la peticion a youtube
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    #extraemos los ids de los videos y tenemos una lista
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    #enviamos solo el primer resultado
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

#evento
#este evento nos dice que el bot esta listo
@bot.event
async def on_ready():
    #podemos configurar que el bot muestre que estamos stremeando, de esta forma: 
    #await bot.change_presence(activity=discord.Streaming(name="Tutorial", url="http://www.twitch.tv/accountname"))
    print("My bot is ready")

#ejecutamos
#pero a este "run" hay que darle un token que sacarmos de la aplicacion de discord
bot.run("NzUwMTExMjAzNDQ3MTQ0NDQ4.X01xfw.W7hwjATDQ9R2NJ_XYsaUQw0pJ3g")
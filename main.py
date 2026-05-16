import discord
import asyncio
import yt_dlp


def bot_start():

    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()

    intents = discord.Intents.default()
    intents.message_content = True

    bot = discord.Client(intents=intents)

    voz_cliente = {}

    yt_dl_options = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "nocheckcertificate": True,
        "ignoreerrors": False,
        "quiet": True,
        "default_search": "auto",
    }

    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = {
        "before_options": (
            "-reconnect 1 "
            "-reconnect_streamed 1 "
            "-reconnect_delay_max 5"
        ),
        "options": '-vn -filter:a "volume=0.25"',
    }

    @bot.event
    async def on_ready():
        print(f"{bot.user} está pronto para tocar!")

    @bot.event
    async def on_message(message):

        if message.author.bot:
            return

        if message.content.startswith("!play"):

            args = message.content.split()

            if len(args) < 2:
                await message.channel.send(
                    "Use: !play <nome da música ou link>"
                )
                return

            if not message.author.voice:
                await message.channel.send(
                    "Você precisa estar em um canal de voz."
                )
                return

            if (
                message.guild.id in voz_cliente
                and voz_cliente[message.guild.id].is_connected()
            ):
                voice_client = voz_cliente[message.guild.id]

            else:
                voice_client = await (
                    message.author.voice.channel.connect()
                )

                voz_cliente[message.guild.id] = voice_client

            busca = " ".join(args[1:])
            print(f"Busca: {busca}")

            loop = asyncio.get_running_loop()

            try:
                data = await loop.run_in_executor(
                    None,
                    lambda: ytdl.extract_info(
                        f"ytsearch:{busca}",
                        download=False,
                    ),
                )

                if "entries" in data:
                    data = data["entries"][0]

                song = data["url"]

                player = discord.FFmpegPCMAudio(
                    song,
                    executable="ffmpeg",
                    **ffmpeg_options,
                )

                if voice_client.is_playing():
                    voice_client.stop()

                voice_client.play(player)

                await message.channel.send(
                    f"🎵 Tocando agora: "
                    f"{data.get('title', 'Música desconhecida')}"
                )

            except Exception as e:
                await message.channel.send(
                    f"Erro ao tocar música: {e}"
                )
                print(f"[ERRO] {e}")

        elif message.content.startswith("!stop"):

            if message.guild.id not in voz_cliente:
                await message.channel.send(
                    "O bot não está em um canal de voz."
                )
                return

            vc = voz_cliente[message.guild.id]

            if vc.is_connected():
                vc.stop()
                await vc.disconnect()

            del voz_cliente[message.guild.id]

            await message.channel.send(
                "⏹️ Bot desconectado."
            )

        elif message.content.startswith("!pause"):

            if message.guild.id in voz_cliente:

                vc = voz_cliente[message.guild.id]

                if vc.is_playing():
                    vc.pause()

                    await message.channel.send(
                        "⏸️ Música pausada."
                    )

                else:
                    await message.channel.send(
                        "Nenhuma música tocando."
                    )

        elif message.content.startswith("!resume"):

            if message.guild.id in voz_cliente:

                vc = voz_cliente[message.guild.id]

                if vc.is_paused():
                    vc.resume()

                    await message.channel.send(
                        "▶️ Música retomada."
                    )

                else:
                    await message.channel.send(
                        "A música não está pausada."
                    )

        elif message.content.startswith("!help"):

            comandos = """
🎵 **Comandos do Bot de Música**

`!play <nome da música>`
▶️ Toca uma música pesquisando no YouTube

`!pause`
⏸️ Pausa a música atual

`!resume`
▶️ Continua a música pausada

`!stop`
⏹️ Para a música e desconecta o bot

`!ping`
🏓 Verifica se o bot está online

`!help`
📖 Mostra esta lista de comandos
"""

            await message.channel.send(comandos)

        elif message.content.startswith("!ping"):

            await message.channel.send("🏓 Pong!")

    bot.run(TOKEN)


bot_start()
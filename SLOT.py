
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('SLOT DEVELOPER')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!폭파'):
        if message.author.guild_permissions.manage_messages:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='채널 폭파됨', colour=discord.Colour.red())
            await new.send(embed=embed)

client.run('MTAzNDgyMjc2ODU3Mjc2ODMwNg.GmbD-7.q1YrROxf6B1MCFjPaTwRs7zP7BxAtgnVQZtx5c')

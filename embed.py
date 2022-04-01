
import disnake
import asyncio

async def embed_new(title = None, description = None, color = disnake.Embed.Empty, user : disnake.Member = None, fields : dict = None, thumbnail = None):

    embed = disnake.Embed(title=title, description=description, color=color)

    if fields != None:
        for k in fields:
            embed.add_field(name=k, value=fields[k], inline=False)

    if user != None:
        embed.set_thumbnail(url=user.display_avatar.url)

    if thumbnail != None:
        embed.set_thumbnail(url=thumbnail)
    
    return embed

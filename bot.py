import os 
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    why_you_should_stop_asking = [
        'You just asked, when this comes out. It took you a few seconds for you to type that, instead of reading that and you typing that we could have done something better. You should have just waited or read the faq channel.',
        (
            'You have just asked when this comes out. Do you know what it takes to send a message on Discord? Electricity. What do you use to make electricity? Energy. Energy can be renewable or not, and it always contributes a little bit to pollution. Your message was useless, so you just contributed to pollution'
        ),
    ]

    if message.content == 'When does this come out?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when does this come out?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'what\'s the ETA?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'what\'s the ETA':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'what\'s the release date?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'what\'s the eta':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'What\'s the ETA?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'What\'s the release date?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when is questcraft gonna release?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when is questcraft?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when quest?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'questcraft when':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'questcraft when does it release?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when is the unofficial minecraft port to the oculus quest2 going to make its release to the public?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when does the vr port to minecraft come out?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when does the quest 2 minecrafts come out?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when does quest minecraft vr release?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'minecraft for quest? when?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'questcraft?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQUESTCRAFTWHENAAAAAAAAAAAAAAAAAAAAAAAAAAAAA?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'whenw will  questcwafwt comwe out?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'Yo when QuestCraft release':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when questcraft':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when questcaft':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'When craft of the quest release':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when will qc release?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'When gta 7':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'is it tuesday':
        response = 'yes'
        await message.channel.send(response)
    elif message.content == 'when questcraft?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when will this get released?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'When craft of the quest release':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'when will qc release?':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'where is questcraft':
        response = random.choice(why_you_should_stop_asking)
        await message.channel.send(response)
    elif message.content == 'Who\'s Joe?':
        response = 'joe mama'
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)


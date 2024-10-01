import configparser, asyncio, sys, os # Standard Libs
from datetime import datetime # standard lib
import discord # Requires from pip3: discord-py

## Setup
##
config = configparser.ConfigParser()
config.read('lua_scripts/elunamod-DiscordCore/DiscordCore.cfg') # PATH TO WHERE YOUR CFG FILE IS. WHEN ELUNA LAUNCHES THIS PY FILE, IT BEGINS IN /bin/

apiKey = config['discord']['key']
logFile = config['python']['log']
## Setup END
##

intents=discord.Intents.default()
intents.members = True
intents.guilds = True
client = discord.Client(intents=intents)

# define our log for this python script
log = open(logFile, 'a')

# create a function that prints to this log
def logPrint(log, message):
    # define the current time
    now = datetime.now()
    print(f"[DiscordCore:PY]: {now} : {message}")
    log.write(f"[DiscordCore:PY]: {now} : {message}\n")
    log.flush()

# loop and print out the sysargs
logPrint(log, "Arguments passed:")
for i in range(len(sys.argv)):
    logPrint(log, f"sys.argv[{i}]: {sys.argv[i]}")

#if len(sys.argv) <= 2: # we can exit the script since no arguments are passed by this point
#    logPrint(log, "No arguments passed. Exiting.")
#    sys.exit()

# create a function what to do if sendMessage is called
async def sendMessage(channel_id, message):
    await client.wait_until_ready()
    channel = client.get_channel(int(channel_id))
    if channel is None:
        logPrint(log, f"Channel with ID {channel_id} not found. Exiting.")
        sys.exit()
    await channel.send(message)

# create a function what to do if sendEmbed is called
async def sendEmbed(channel_id, description, title=None, file_path=None):
    await client.wait_until_ready()
    channel = client.get_channel(int(channel_id))
    if channel is None:
        logPrint(log, f"Channel with ID {channel_id} not found. Exiting.")
        sys.exit()

    embed = discord.Embed(description=description)
    if title:
        embed.title = title
    if file_path and os.path.isfile(file_path):
        file = discord.File(file_path)
        await channel.send(embed=embed, file=file)
    else:
        await channel.send(embed=embed)

# define table of supported arg[2] commands
commands = {
    "sendMessage": {
        "function": sendMessage,
        "expected_arguments": 2 # channel_id, message, discord_id
    },
    "sendEmbed": {
        "function": sendEmbed,
        "expected_arguments": 2  # channel_id, description, [title], [file_path]
    },
    "sendFile": {
        "function": None,  # Placeholder for future implementation
        "expected_arguments": None  # Placeholder for future implementation
    },
    "sendFileEmbed": {
        "function": None,  # Placeholder for future implementation
        "expected_arguments": None  # Placeholder for future implementation
    },
    "sendFileEmbedMessage": {
        "function": None,  # Placeholder for future implementation
        "expected_arguments": None  # Placeholder for future implementation
    },
    "sendFileMessage": {
        "function": None,  # Placeholder for future implementation
        "expected_arguments": None  # Placeholder for future implementation
    }
}

# check if arg[2] is a supported command and has the correct number of arguments
if sys.argv[1] not in commands:
    logPrint(log, f"Command {sys.argv[1]} is not supported. Exiting.")
    sys.exit()

command_info = commands[sys.argv[1]]
if len(sys.argv) < command_info["expected_arguments"] + 2:
    logPrint(log, f"Command {sys.argv[1]} expects at least {command_info['expected_arguments']} arguments. Exiting.")
    sys.exit()

# Extract the command, channel ID, and message from sys.argv
command = sys.argv[1]

# Check if the command exists
if not command_info["function"]:
    logPrint(log, f"Command {command} is not implemented. Exiting.")
    sys.exit()

# Define the main function to run the bot
async def main():
    logPrint(log, "Starting bot...")
    await client.start(apiKey)

@client.event
async def on_ready():
    logPrint(log, "Bot started.")
    if command == "sendMessage":
        channel_id = sys.argv[2] # Extract the command, channel ID, and message from sys.argv
        message = sys.argv[3]
        await command_info["function"](channel_id, message)
        logPrint(log, f"Message sent to channel {channel_id}: {message}")
    elif command == "sendEmbed":
        channel_id = sys.argv[2]
        description = sys.argv[3]
        title = sys.argv[4] if len(sys.argv) > 4 else None
        file_path = sys.argv[5] if len(sys.argv) > 5 else None
        await command_info["function"](channel_id, description, title, file_path)
        logPrint(log, f"Embed sent to channel {channel_id} with description '{description}'")
    await client.close()
    sys.exit()

# Run the main function
asyncio.run(main())

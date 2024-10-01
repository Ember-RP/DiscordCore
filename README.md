# DiscordCore

Ember's multi-faceted Warcraft to Discord communication feature.

# Disclaimer

This entire concept is a work in progress and a rough draft, even this readme. Please read through the code for any questions that cannot be immediately answered.

# Introduction

DiscordCore is a feature set that allows multiple avenues of using Discord with your World of Warcraft server via Eluna and Python. In order to use this, you need to have python3 along with the dependencies listed in DiscordCore.py.

Clone this repository into your lua_scripts folder.

Ensure the configuration settings are correct. These are located in -

- DiscordCore.cfg
  - key
  - log (This is already set to a valid default value, but ensure the path is correct anyways).
- DiscordCore.py
  - config.read('lua_scripts/elunamod-DiscordCore/DiscordCore.cfg') (The location of your cfg file. This is also valid, but ensure the path is correct anyways.)
- scripts->Server_DiscordLoginAnnounce.lua
  - DiscordLogin_Channel
- Server_DiscordCore.lua
  - local pythonfile = "$HOME/server/bin/lua_scripts/elunamod-DiscordCore/DiscordCore.py" (Ensure this path is set to your python file. This is NOT a valid default path.)
 
  # Planned Features & Milestones

  Currently this bot is only capable of sending a message to a channel when a user logs into your game server.

  The plan is to add things such as API support for custom messages to custom channels, experimental features such as proximity voice chat, and authentication features such as the previously released Discord User Authentication module, will be solely delegated to this one repository and all these features will be toggleable.

  # License

  Currently there is no license. Just please credit if you used or learned from this repository in any way. Thank you!

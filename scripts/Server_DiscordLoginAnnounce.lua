local DiscordCore_Functions = DiscordCore_Functions or require("Server_DiscordCore")

local DiscordLogin_Channel = "000000000000" -- the announcement channel ID for announcing logins. must be a string.

local function OnLogin(event, player)
	-- local python_string = "sendMessage " .. DiscordLogin_Channel .. " 'Player " .. player:GetName() .. " has logged in!'"
	local python_string = "sendEmbed " .. DiscordLogin_Channel .. " 'Account : <@" .. DiscordCore_Functions.EmailCache[player:GetAccountId()] ..  "> has logged in with the Character : " .. player:GetName() .. "!' 'Login Detected'"
	DiscordCore_Functions.Launch(python_string)
end

RegisterPlayerEvent( 3 , OnLogin ) -- on login, do the function
DiscordCore_Functions = {}

local pythonfile = "$HOME/server/bin/lua_scripts/elunamod-DiscordCore/DiscordCore.py"
local function DiscordCore_Launch(arg1) -- function that runs the python program. accepts a string as argument to insert.
	local python_instance = os.execute("python3 " .. pythonfile .. " " .. tostring(arg1) .. " &")
	return python_instance
end

DiscordCore_EmailCache = {} -- [account_id] = email
local function DiscordCore_generateEmailCache()
	local query = AuthDBQuery("SELECT id, email FROM account")
	if query then
		repeat
			local account_id = query:GetUInt32(0)
			local email = query:GetString(1)
			DiscordCore_EmailCache[account_id] = email
		until not query:NextRow()
	end
	print("[DiscordCore]: " .. query:GetRowCount() .. " Emails cached.")
	return DiscordCore_EmailCache
end

DiscordCore_generateEmailCache()

DiscordCore_Functions.Launch = DiscordCore_Launch
DiscordCore_Functions.EmailCache = DiscordCore_EmailCache
DiscordCore_Functions.generateEmailCache = DiscordCore_generateEmailCache
return DiscordCore_Functions
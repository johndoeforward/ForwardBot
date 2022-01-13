from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzMBu1vbiOjMBR_4-dJToVweLWbAcjASj_eINfxB-rtv8FgQmZs4dxrPFQrczsOezbtSUsq8ShQTXK7J9mXHGr0hQkRczl8j2Hfu00QMeUJdACqqj5i8gSdok4X77z2Q_fYDzMcxIZisUp6HGtnmRXScLig20aGeD-Fvx21fN6SUc_Q73Gadsgu7u0IHMlvqmFPvTue2kP5YnKNrAitbtEkNHclmxyQwSwqDuQYwb5i1CLa2oNIDTt4md9bhZ89HLf0dCHwhnskUxnvjW2UtBMSZ3-mbFaZCgK4b9w4qBkCa191won7yEl4PIXslwlCg9X3TO6ixDC6lJBs0B1R0Pc3k6o0="
    SUDO_USERS = "5093917807"
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """

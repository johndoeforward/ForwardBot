from os import environ
class Config(object):
    API_ID = "12344880"
    API_HASH = "182534c4ef902d9a322b75980e76324e"
    BOT_TOKEN = "5002280896:AAH8FNnahmetCxvR6nZd-eOEj8XdDvEdh-E"
    STRING_SESSION = "1AZWarzgBu4xW1Nlaa9XnfbmtgAZWhevUKX3_gfpzrrvHm_R2XzMwJ_nZmibYH9PW8jWYibUNPR-i2I_zwtsVgZJElI4_052_nvphMiQINruzaTkz842UfOr4SJHTpWQKh_jsjdmo6CwM_7CzgVJcki3xU9ldMNcGARasxfi4oyjF_VdeqT8wgK_nuxhNNNbL-ynDoF2isWcgsVk4tOP6NZ6wiLMsn5mCgrryzWLomm8Tj6Hw5q6O6BYPsnOQe2YPlRnsXIyE47NWhAO4YWrqWsVAe1E0665-bCWhB-r7ogcwszCPu3RGhwFMzDDemIqnhUjZHgXHyEwEFMcfGq1MyNhuq3MgWeM="
    SUDO_USERS = "5059059145"
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

from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzUBuw3wRrLpe0lTsyUhkOydY2gVfwliydn4iQYubs1E38LGKHvmHeP8xOKtikdnC7Ck9yZp6x22obMAAST2Pl_y8B-HLsSYEUdqrlXVe9nF5yokOJlWUEn_qLWO5hOQYshplbZy_7n5Zp-Z-K5TMae0C260QLlWrLb8c-hOsacjY77j6V_RP-rcrcRxcS6tD0tkUlzCDp0gBKks4xTegbYEuSLqr59bRIYBpxGW_NCsNjHpdZ9TndT98KvkjxkkaxSF3llZNv04-yOjw1gWLENp-EYvd2ixBPIXa7hDrpITJx3nMdGZAE2Bq7gm0WI3sOjwszdmZf8F_rwyfPEhnuwIPiI="
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

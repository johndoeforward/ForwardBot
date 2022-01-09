from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzsBuyV0IFqjvo7nEkHfLcvlNDHihS3uGo11W32gKzZJv8_oAyXALIITTEk2OebkU2hza_96LOFuOwpGLzxVg22g7mvhgMXHSithbtRnGYd8UF2o3mljcAB9TZNi_lCn2ADtRHaGjFQtmRuHIfEn6yDW7WQ4TXi5xPrqFzxnPTdZTiGBIss7nAE5oc7LI8wzDyUSg6WZmviuK5x6VFy9Umxfo62-xBTYfBdRL3SVFII8FV1oWtW1is50fNEcevkqCrwr-jtNucVffugSroe3w4mjX4C6WEimyXULHTEq3PP9Amwr_RE8sKPzGzmCDN467iW9i3Zzr1r8QIUar3gGG96hM0s="
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

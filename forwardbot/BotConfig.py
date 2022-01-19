from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzwBu6ktinQnCjqp-PwPwoYcAHwpCr149OcM8ck0tNuwFqqI9nvHPxdsb2gF2yv0HgHJTXMfBZJAAuiZY1OYC1_tsfh5wkc5UErQHBFMqBrPbCZhWNFQecaM1EfDUMNupx80RZzVvahpogAkSyu0-8I-4uz6fwvg_CRhimqR4VBgTEotMau0yje2fb3o1p3k2YetWwCqyyhkLUPJOcr8p1QDirZDbXgbGWRHdpE-AXlzeZS423fqb6E7pYAN9fuvzjQhu4sta8PiOm9TUEc_uSfIuHvcNefOdQnMogVZfiiWT2YX8emRRB3QW0Ecrwv-G5yhaNPLvdV80QL7X25cD5UbPxo="
    SUDO_USERS = "831054990"
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

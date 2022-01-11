from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBuygxG1s0DJqhUcSV9r9IaxLzRo8q5ER3jE2QuMRBAnhjV13WzUMlqwzRbFLSR4ZrxL19NKDjGM9SoOj4lhImYUgTr1KvnJQToLj5ebyyY4WhcW2ghUTVlQ6nI9WEXxC6v_-OLJfPSLZ-vLogqLAVol8O7mChi43TyX63hHVb1io2rR31cToMUeuU8o0KowUxhmshOR0GvGRrVOQJoBbbt4g-q3oKmJjnNQYgCbyhvBm9X3nu__wftAy0ZTq6E_UEDfMIlint3SwIaYaM83WXfxf7afA5wwG1RkfOJW1RDy3T8meT9qrvJaE8Y937eAey_2gE64D6o9wS8347Ew_Gdwc="
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

from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBu0Tz5hVi1uusUYNfbmVCWbjou8gybHgNjKoSABMQyXIuv0X4ijtRAz-JlW_zM7N6ErwRPuEiM74MljrqEErtT8MhmQymLPZJ5FgWejCLMeQI49eejEG3UY9Zz4cW3ykrLlJzgEhOHrYq69ZkkDhMs4UXHe7EEZTQwaX1PPzAYSx1OBe96a6Vl_0P9lBxi6y1kv_rpUMk0s2vGLIFeBntoS2ovEjgGRkYKwuLqG_WUKjk1DaKtpRV8NWEFpXf_oqB1xUHkKCzqr8jCqQ9bVjcmWOvUKL1zPEsWGiDDiy3KFNDV4bJAJgJgKNspawP7ilPyzvrSXn13gVN-8U-fg7Y85I="
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

from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzoBu3XJWhsIPvBGNdkTaOsgfDSb-jKvZyPHIo5M5sI3NHFnow-kdymFtKIUXUdntfxznSGJOUyNbRJi9U-LOZdDy_7KqEdTpxgmRiaxZrTg1O72giJcBQ7NWt4X_9wAzNEYdNryVMG1beacZuZxazsy03mRuBF1FRNpxkZQmplFRyDSLzRlfSvK6fM4Ms2bku-hhohjSqypl3laGgMNJzjdefCZ6CnYiOzM-JwLWpk1eDqCUDTVIQzQCg3n4908MjmNjNYIzjIqP_B38lVJpR4wYKVoRe-1WLNpXCcXO7ydBPHE9UDA_gITWK5wsGO4xN34r3HV05KOoE4xQTtVu-zgIqU="
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

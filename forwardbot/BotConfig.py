from os import environ
class Config(object):
    API_ID = "12344880"
    API_HASH = "182534c4ef902d9a322b75980e76324e"
    BOT_TOKEN = "5088525898:AAEQsYO7vukD6YxYwZEqtySENXOb2_Fz1a8"
    STRING_SESSION = "1AZWarzsBu1hd791q31G_9Osob4Yzx5dRq4BfE5x_IMWpRljdeipE8UuwrhGMvdKUvvoRjBo3tYJ_OKUkUTjTlKgXiNypSUk2gl3Gwmx_qRffEvgZjMhwpU6LAhkzKFLCm6BvhLxTfW6-ZPDp2jwSX3epXBAf9PvLAEU_Mwfe_hWH_-TjeDXA_VOH2Vpayy2qFj1ORy-6tDoYtr1SCrSQysRuoykeDgegQkKE-48ODybj2wg0P9y-lgA19HHkNN1JKltRrSX-PdBJWbn4p4Y4KL47QvgVmHH4ucPb5IVwP2G9T_G9wFKIlmEP22pYX6HwOJARFxK9B54rqPNaaa-SVeQgaK1mzzY="
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

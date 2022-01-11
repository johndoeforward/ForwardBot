from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBu2ZsMFjIVM_EgTCHnfGVIlKM7LKvauBOO3bqkwIgC8VLsR8pbuLOM7njxH3SJR7HYgHCEYZo6q-L0F8hD3X16tjo2SKaV6ZrkKmhRzXkLGK_Olk6V3AtKmO6JdlMCPy4V0WinQQUWeb5_6AI733CHamrlfSXvoPy6ttc3hNGER3tXMx23myjLGHwUocnLBwCoKMiIFbkQnUV0bbX4TsudYa1LwB72zE8dwwOcC8vItXkP_fkcEWpGWST8lrluwTLlbcRDJXuRuX-tF8TijKjQNnwXcGB-HBxo-gPDa-o1j_Ce5RC3CH0IIkKmTRlwTdcqn2Ju0pitwoStDJ-_CobZ74="
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

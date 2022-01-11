from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzQBu2BcFyUtbAPD8m3nFssXtHgcWBhKb1Fe4jnX5QJCJl0lIPCj3XiwKUQR-oGEaLjsbLtfca4WoTv0Y1kZR6KbRELbsMiMN-JlcBP9O4Tqsoeq-a6R36qR6jA6tGxWX_T0eQ2hheNd9Za7KXXZ8qDfCPs_RybkJ1bCJXfYq-fL5-Li7UqPt7ludM17JmbCKwAGRNRhArGz0yTmaTzXRK3OO7DmSaHF2etrkqmS_GnYSbZXDahaiFn-1U7-elGI8K41MUDI8gaUuJnsVdiMb_eLhkTLhxtcX5ZsCJdhvZCPLgbaCwpsLPqmlXhm3Dyxu7e7XqxxKKv-6dNewG18y8tasAs="
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

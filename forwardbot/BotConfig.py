from os import environ
class Config(object):
    API_ID = "15312263"
    API_HASH = "8de06ac6a6d9becf69e7558f12132b74"
    BOT_TOKEN = "5098404525:AAES7-avl8ttz80pb2KHmD0rJ15urWr1aq8"
    STRING_SESSION = "1AZWarzcBu0H9VOSmZtxcB0qlAVy3AJzlAbzCImsMO1U7yi2umBoeQ1bwO5m4De-583Zkfmo14oCWEyOgiykv58a6kTUrhV1DescJvO_Qpuj5uq_O51xkJiVZFDNVyP2QPB6iqtS4cBfwsYVfWW0xge98f9ockdI63jGZrALVVZWwCo1darZcSu-LhLMPmc4r9Lwhh99D4UXBN9Qz1w8QSMmwnAYPuS4J9Cu0ybOMM2rzJx_LVqwYdDO2lzLYIVQk4Fb8l8V3XrQYDoNzCYoEpxZcU7R3eCFQyVmTcNMjJtTCjkOBl3l2en8In2zfOhtA8goAqq9Eq0EV4DY5DFx_-oP1sqsfxAg="
    SUDO_USERS = "5095158838"
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

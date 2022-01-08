from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzQBuw1x9Uw5l4aWJY9T92_Le2RIr5hWRB2HZd0gLhutVpQZd3PtkvLhdyVOUhRr74ASvSGlP5asKdSw1SHC1X5LhgjM38LYhpj_x-dlnsycywoIXCAkY1dAtza-RgTUthK2HIjNxFcCOlqWv5-Bu8nWTZT03yPJYOdrtO7vUJ8YI7cdL9qXcYOu2hA9JRp2aXRJdRXaCjMb5jBUN2BqNGQplGfLXNzzcj3V4eNYdfZTgkgIUDzfMasXIaV6G9P4OrTXo0Pmvee2dF_TELzSscyVh9sxRXuISsQGylZ0V7fdTfeUCSkvz2XD34LDLWt_C9NCACJJ1-1L-43BxG0mbzDjZzI="
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

from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBu1aSB6b2fsoYcBHlQgLF3EYbkTwofRq158xcpnAL4p2_gMuNUJelrjjDY5hcAvJBQEcuRGzBVhFl6NyCbwF0fUVvXonjr9aUZ4Kp8XRKDIYQDSscYwTSCJlWHKAUgfB8D_xM_uNqm1srhIEybrnD2E4Qgjx__4nyuNLy-3G5dBincFixrz9QQnLQV7m3OLi7FE8Xln4kpuBvWFz6v2TuBD4bYvVW7rksAwWn2lTloQGNwCxPi5d8NM1F0pKGYvK_3kDn4bEi9u_ol69wIgz6MI7PMivuUNwlW9-8pbLN-pHnYTaJ1pio4WHhpEPsVHBPgy1EsCgd6oWqWxIv0myzwpI="
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

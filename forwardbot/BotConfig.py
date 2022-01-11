from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBu394yIavmmuxxhSbefa6-oACF_YRkPsf3qkJf_7pE0nRkoltK4IYYk9g63Fz_qG0tAmkNiycWB76tAa3fmMyJs9t7P_rjc2C08udLv-OKnBcrFWL8lfkqDcCU7FD8EzmCr3i50vnYi1l-yuW0Mz1gael8XP2JLFub7bP9fhOnH3TqaVre_Wf4FZcetcsDbvWD3ob-lCFHLWaU1isBGqh3Y6_VaNS9b8GzN4iadRcBEOplW9Qw1mosXU6axI_8C7g-QPt3yZ0u3MX2hwyfRgVIeNjk-LN1cQHrcEuzD03VAhBmiiPoNmPOd2qjKBltqgsrP-94FSPs0rmbAYerZPoX00="
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

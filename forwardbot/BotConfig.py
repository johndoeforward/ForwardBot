from os import environ
class Config(object):
    API_ID = "16226233"
    API_HASH = "c0f07f2b09573a2e09e62f6085f507ad"
    BOT_TOKEN = "5018774285:AAF11VqQmvW6clN3LIgtND_FH1XozKqri24"
    STRING_SESSION = "1AZWarzQBu73UmBkx8SfxRNldkK97ysuNUEuh48K07zIqHz29tKI6K4t7xR2e6onro3Ccm5I5lrKVM9jiGbUj2geXFZrDxhyI7Sf5fH6cwgdczehD0NxxotZ45OJJ5-IsPt_R00ThX-i3z1dYNDyMEvbv8I3mRNlZgJOZTy9gqiYUGgPYSVktaKvGahIYzQUEi8lirvHUpte1GISRn_25odliqby000cZTVotKDV3QkxAN5g9upldlbpQ3kka-SWAJLpMW4N_P8Jd4njK1bRcEd-f7h_T2qIZiauwSDfYzQGw0rNtiaGBqDZfu2tQn-FxtsR5dAOwanmkQ96JJusrOWKkw5ttW2o="
    SUDO_USERS = "5051694197"
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

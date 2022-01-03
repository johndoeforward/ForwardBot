from os import environ
class Config(object):
    API_ID = "11074643"
    API_HASH = "529aa3cb16fbdfc3e0f1c0d19391f798"
    BOT_TOKEN = "5013169201:AAHE72RqsW8bx0m6_Xt5eTpkrC7ATmJEPHc"
    STRING_SESSION = "1AZWarzYBu1jr3Ia43BlTwkbMrZ8sWU3bp-QglNox8OB7iUYjAfjn3XtTUWq7kOq0xNEl7zwpcTJPNrR_N2cCeleMxwwMfvOXSiOWeBEiJmbIPB50elJDtk2f0etFrc5Oklt7A5xD-m3AKaolWZ9coi59B9j1euIs_-BGgf8d70iRxr6oLQR71aRTxcsSxSSl6uej2z3H6iqdL-jcph-1bn8OMifR-9a9a8Uu4A9Jj-q3zW8ZnVdcRDbeb6JDIPrS6hHrEXKkBmddrzQE3UlsWhcs_DQpplS_8AxEtLeEb-5Iw1JKJmbfP8AAB6CIaNcEhJoH40v1pakZEpVETr50hk7PYw0mtfE="
    SUDO_USERS = "5092767370"
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

from os import environ
class Config(object):
    API_ID = "3352706"
    API_HASH = "8c712f0779b7de1053bb4faf4151f123"
    BOT_TOKEN = "5077138814:AAFLqvb5aUIfTYHsRjmBl7nv--5ZQu15a74"
    STRING_SESSION = "1AZWarzcBu4Qd0XRa7tjHIZ4K1ZRRaFtL-Z14UIp3y1tn8I2sIVJmsx9J7U9Z_tRZ4raPxNA9HnZe5myQrfpPAYlLF5PI_HtSZPU_-o3vxPkwoNRN5Ulqm-F5AFOwVJSc6_-k29Pg322qDiFb4-Ux9zhw0YWxiiimAlpBZoGI1AspTi_rOOVwIEbbZtnYcwh4Lhs2W9ipwDFnzvA5DyfBGHqka8Mxt6d-HorFzqYUVAs-W7Hjv3HnFIDpXf9YaEfrlpzVjbZXufRPrSf1rmodyJBPza6njU7ARSrXLVEf8P2tYAUjGAvQQ1ABw_qtKok9lVxD6QI5fHwn_Sm1fSFhGiCvdzBbXUg="
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

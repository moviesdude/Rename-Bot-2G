import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "16229284")
    API_HASH  = os.environ.get("API_HASH", "ebd1fead3cc15343bea10b5c164165ba")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7282531608:AAETOv306wNgIOFDPSPQFRMxC1PPbcIUSaY") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Renamebot_Render2")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://moviesdudebot:MDbots@cluster0.y4gwugw.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/9acca333738f41eba89f8.jpg")
    ADMIN = int(os.environ.get("ADMIN", "1103137195"))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Team_MDL") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002023083749"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

➻ Denote For Live Bot : `thriudev04@okicici`.

Bot Is Made By : @Team_MDL</b>"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Team_MDL>Team_MDL</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/Team_MDL_Admin_Bot>Owner</a>
├<b>📱 YT Channel</b> : <a href=https://www.youtube.com/@MoviesDudez>YouTube Channel</a></b>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>🔥 Rename Repo</b> : <a href=https://github.com/JishuDeveloper/Rename-Bot-2GB>Github Repo</a>
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Team_MDL>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `thriudev04@okicici`
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper

class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """ <b>β­ββββ[ πππ’π¨π§ π π ]βββββ
β
ββ MΚ Ι΄α΄α΄α΄ : {}
β
ββ Oα΄‘Ι΄α΄Κ : <a href='https://telegram.dog/happy_kid_sk'>Hα΄α΄α΄Κ π§ββοΈ KΙͺα΄</a>
β
ββ CΚα΄Ι΄Ι΄α΄Κ : <a href='https://t.me/kr_botz'>KR β οΈ Bα΄α΄α΄’</a>
β
ββ Vα΄Κκ±Ιͺα΄Ι΄ : 2.2.5 [ Bα΄α΄α΄ ]
β
ββ Sα΄Κα΄ α΄Κ : Hα΄Κα΄α΄α΄
β
ββ Lα΄Ι΄Ι’α΄α΄Ι’α΄ : PΚα΄Κα΄Ι΄ 3.10.5
β
ββ FΚα΄α΄α΄α΄‘α΄Κα΄ : PΚΚα΄Ι’Κα΄α΄ 1.4.16
β
ββ Dα΄α΄ α΄Κα΄α΄α΄Κ : <a href='https://telegram.dog/LastDrogz'>Lα΄sα΄ π² DΚα΄Ι’α΄’</a>
β
ββ Pα΄α΄‘α΄Κα΄α΄ ΚΚ : @BGM_LinkzZ
β
ββ Uα΄α΄α΄α΄α΄α΄ α΄Ι΄ : [ 26.05.2022 ] 7:28 PM
β
β°βββββ[ @KR_Botz ]ββββββ </b> """
    SOURCE_TXT = """πππ₯ππ¨π¦π π­π¨ πππ ππ’π§π€π³π 
                              ππ’π§ππ¦π ππ’π¦π ππππ’ππ’ππ₯
<b>
                  <a href=https://t.me/+GPrm8sxTWsdkOGM1>π° πα΄Ιͺπ πΚπα΄π π°</a>

               <a href=https://t.me/+lsAp2MDnUC9mMmE1>βοΈ πα΄α¨α¦α΄π πΚα΄NΙ΄α΄π βοΈ</a>

                 <a href=https://t.me/+MB8a61q_98A3MThl>π§² πα΄α¨α¦α΄π πΚπα΄π π§²</a>

          β ββββββββ β ββββββββ β 

                  <a href=https://t.me/+hR6DpC_xpPBiM2Zl>β€βπ₯  Bα΄T Uα΄α΄α΄α΄E  β€βπ₯</a>

             β― βββββ β‘οΈ βββββ β― </b>

<b>β­οΈ α Ιͺsα΄Κα΄Ιͺα΄α΄Κ </b> : <code> All The Content in this Channel is Taken From the Internet, We Don't Own Any Content. </code>
<b>
Pα΄α΄‘α΄Κα΄α΄ BΚ - @BGM_LinkzZ

Cα΄Ι΄α΄α΄α΄α΄ Mα΄ - @KR_AdmiN_Bot

SΚα΄Κα΄ & Sα΄α΄α΄α΄Κα΄ Us </b> """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Sk should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Happy Kidz Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. HappyKidBGMZ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/kr_Botz)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Happy Kidz

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>β­ββββββͺ π¦π§ππ§π¨π¦ β«ββββββ
β
ββ Tα΄α΄α΄Κ FΙͺΚα΄s : <code>{}</code>
β
ββ Aα΄α΄Ιͺα΄ α΄ Uκ±α΄Κκ± : <code>{}</code>
β
ββ Tα΄α΄α΄Κ GΚα΄α΄α΄s : <code>{}</code>
β
ββ DΙͺκ±α΄ SΙͺα΄’α΄ : <code> 500.42 GB </code>
β
ββ DΙͺκ±α΄ Uκ±α΄α΄ : <code>{}</code>
β
ββ FΚα΄α΄ DΙͺκ±α΄ : <code>{}</code>
β
β°ββββββͺ @BGM_LinkzZ β«ββββββ </b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

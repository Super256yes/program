import time #line:1
import os #line:2
import subprocess #line:3
import keyboard #line:4
import pyautogui #line:5
from datetime import datetime #line:6
from PIL import Image #line:7
import pytesseract #line:8
from pytesseract import image_to_string #line:9
import requests #line:10
import json #line:11
from gtts import gTTS #line:12
from groq import Groq #line:13
from screeninfo import get_monitors #line:14
from openai import OpenAI #line:15
import base64 #line:16
from colorama import Fore #line:17
import hashlib #line:18
import colorama #line:19
import socket #line:20
clientName ="theArc"#line:23
version ="v1.1"#line:24
buildDate ="Feburary 20th, 2025"#line:25
vlc_path ="vlc.exe"#line:26
inputCheckDelay =0.016666 #line:27
hostname =socket .gethostname ()#line:28
ip_address =socket .gethostbyname (hostname )#line:29
clientKey =""#line:30
colorama .init ()#line:32
headers ={'Content-Type':'application/json'}#line:36
def toSHA256 (OO0OOO0O00O000O00 ):#line:38
    O0O00OO0OOO00O0OO =hashlib .sha256 ()#line:39
    O0O00OO0OOO00O0OO .update (OO0OOO0O00O000O00 .encode ('utf-8'))#line:40
    O000OO000O00OO0OO =O0O00OO0OOO00O0OO .hexdigest ()#line:41
    return O000OO000O00OO0OO #line:42
def getLocalIP ():#line:44
    OO000OO0OO00O0OO0 =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:45
    try :#line:46
        OO000OO0OO00O0OO0 .connect (("8.8.8.8",80 ))#line:48
        OO0O0O000O0O00O0O =OO000OO0OO00O0OO0 .getsockname ()[0 ]#line:49
    except Exception as O00O00O0OOO00O000 :#line:50
        OO0O0O000O0O00O0O ="Unable to get local IP"#line:51
    finally :#line:52
        OO000OO0OO00O0OO0 .close ()#line:53
    return OO0O0O000O0O00O0O #line:54
def log (O00OOOOOOO00O0O0O ):#line:56
    print (f"[{Fore.GREEN}INFO{Fore.RESET}] {O00OOOOOOO00O0O0O}")#line:57
def logError (O0OOO000OOO0O0OO0 ):#line:59
    print (f"[{Fore.RED}ERROR{Fore.WHITE}] {O0OOO000OOO0O0OO0}")#line:60
def logWarning (OOOO0OOO000O0OOOO ):#line:62
    print (f"[{Fore.YELLOW}WARNING{Fore.WHITE}] {OOOO0OOO000O0OOOO}")#line:63
def logFatal (OOOO00OOO00OO0O00 ):#line:65
    print (f"[{Fore.RED}FATAL{Fore.WHITE}] {OOOO00OOO00OO0O00}")#line:66
    exit ()#line:67
def pingDomain (O0OO000OO00OOOO00 ,OOO0O0O000O0O0OO0 ):#line:69
    try :#line:70
        O00OO0O00OO0OO0O0 =requests .get (f"http://{O0OO000OO00OOOO00}",timeout =5 )#line:71
        if O00OO0O00OO0OO0O0 .status_code ==200 :#line:72
            if OOO0O0O000O0O0OO0 ==True :#line:73
                log (f"Website: {O0OO000OO00OOOO00} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00OO0O00OO0OO0O0.status_code}")#line:74
            return True #line:75
        else :#line:76
            if (O00OO0O00OO0OO0O0 .status_code ==403 ):#line:77
                    if OOO0O0O000O0O0OO0 ==True :#line:78
                        log (f"Website: {O0OO000OO00OOOO00} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00OO0O00OO0OO0O0.status_code}")#line:79
                    return True #line:80
            else :#line:81
                if OOO0O0O000O0O0OO0 ==True :#line:82
                    logError (f"Website: {O0OO000OO00OOOO00} Status:"+Fore .RED +f" Unable to Connect (Status code: {O00OO0O00OO0OO0O0.status_code})"+Fore .RESET )#line:83
                return False #line:84
    except requests .exceptions .RequestException as OOOO0OO0OO00O000O :#line:85
        if OOO0O0O000O0O0OO0 ==True :#line:86
            logError (f"Website: {O0OO000OO00OOOO00} Status:"+Fore .RED +" Unable to Connect"+Fore .RESET )#line:87
        return False #line:88
def logThroughWebhook (O000OOO00OO0000OO ):#line:90
    O00O000OOOOOO0OO0 ={'content':'{}'.format (O000OOO00OO0000OO ),'username':'theArc'}#line:95
    requests .post ("https://discord.com/api/webhooks/1336862514591305810/O4YZZalX6AJXut4TEY0_4EEXb13eEmu6C4v3MKCzHLROATyfkdxyt-wzWWI14vV9WutT",data =json .dumps (O00O000OOOOOO0OO0 ),headers =headers )#line:96
os .system ("cls")#line:98
if pingDomain ("raw.githubusercontent.com",False )==False :#line:99
    logFatal ("Was unable to connect to 'raw.githubuser.content.com' which is required to run to program. Make sure that it isn't being blocked by a firewall.")#line:100
def get_text_from_github_raw (O0O00OO0O0OO0OOO0 ):#line:108
    O0O0OO00O00000O00 =requests .get (O0O00OO0O0OO0OOO0 )#line:109
    if O0O0OO00O00000O00 .status_code ==200 :#line:110
        O0OO0OOO00OO0OO0O =O0O0OO00O00000O00 .text #line:111
        OOOO0OOOOOO000OO0 =O0OO0OOO00OO0OO0O .split ('\n')#line:112
        return OOOO0OOOOOO000OO0 #line:113
    else :#line:114
        print ("Failed to fetch the text from the given URL.")#line:115
        return []#line:116
raw_url ='https://raw.githubusercontent.com/Super256yes/48a53f0774c8ceff574a1fdcb0d470dbd382b3db273cff4344b6d39d5379c923/refs/heads/super/48a53f0774c8ceff574a1fdcb0d470dbd382b3db273cff4344b6d39d5379c923.txt'#line:119
listOfKeys =get_text_from_github_raw (raw_url )#line:120
doLogging =False #line:123
if pingDomain ("discord.com/api/webhooks/1336862514591305810/O4YZZalX6AJXut4TEY0_4EEXb13eEmu6C4v3MKCzHLROATyfkdxyt-wzWWI14vV9WutT",False )==True :#line:124
    doLogging =True #line:125
configJsonFile =open ("config.json","r",encoding ="utf-8")#line:133
configJsonFileData =json .load (configJsonFile )#line:134
configJsonFile .close ()#line:135
clientKey =configJsonFileData ["client_key"]#line:137
for x in range (len (listOfKeys )):#line:139
    if toSHA256 (clientKey )==listOfKeys [x ]:#line:140
        log ("Key has been successfully validated.")#line:141
        log ("Welcome user ID: "+str (x ))#line:142
        if doLogging ==True :#line:143
            logThroughWebhook (f"VALID KEY LOGIN:\nKey: {clientKey} \nIP Adress: {ip_address} \nHost Name: {hostname}\nNetwork Address: {getLocalIP()}")#line:144
        break #line:145
    else :#line:146
        if x +1 ==len (listOfKeys ):#line:147
            logThroughWebhook (f"INVALID KEY LOGIN:\nAttempted Key: {clientKey} \nIP Adress: {ip_address} \nHost Name: {hostname}\nNetwork Address: {getLocalIP()}")#line:148
            logFatal ("Key is invalid. Make sure you properly put your key into the parameter 'client_key' in 'config.json'.")#line:149
pressEnter =input ("[{}]: Press 'Enter' to start the program.".format (clientName ))#line:153
log ("Attempting to start program...")#line:155
time .sleep (1.5 )#line:157
os .system ("cls")#line:158
print (Fore .LIGHTRED_EX +"""


        ▄▄▄█████▓ ██░ ██ ▓█████ ▄▄▄       ██▀███   ▄████▄  
        ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  
        ▒ ▓██░ ▒░▒██▀▀██░▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ 
        ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒
          ▒██▒ ░ ░▓█▒░██▓░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░
          ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░
            ░     ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒   
          ░       ░  ░░ ░   ░    ░   ▒     ░░   ░ ░        
                  ░  ░  ░   ░  ░     ░  ░   ░     ░ ░      
                    developed by: wassaps         ░        
                    
      """+Fore .RESET )#line:175
log ("Program is starting. {}, {} developed by wassaps.".format (clientName ,version ))#line:177
configJsonFile =open ("config.json","r",encoding ="utf-8")#line:179
configJsonFileData =json .load (configJsonFile )#line:180
configJsonFile .close ()#line:181
log ("config data has been sucessfully loaded from 'config.json'")#line:183
groq_api_key =configJsonFileData ["groq_api_key"]#line:185
log ("Set groq api key to: {}".format (groq_api_key ))#line:186
webhook_url =configJsonFileData ["webhook_url"]#line:187
log ("Set webhook url to: {}".format (webhook_url ))#line:188
discord_user_id =configJsonFileData ["discord_user_id"]#line:189
log ("Set discord user id to: {}".format (discord_user_id ))#line:190
delete_cache_option =configJsonFileData ["delete_cache"]#line:191
log ("Set'delete_cache_option' to: {}".format (delete_cache_option ))#line:192
read_response_sound =configJsonFileData ["read_response_sound"]#line:193
log ("Set'read_response_sound' to: {}".format (read_response_sound ))#line:194
discord_webhook_enabled =configJsonFileData ["discord_webhook_enabled"]#line:195
log ("Set'discord_webhook_enabled' to: {}".format (discord_webhook_enabled ))#line:196
show_response_text =configJsonFileData ["show_response_text"]#line:197
log ("Set'show_response_text' to: {}".format (show_response_text ))#line:198
allow_image_sending =configJsonFileData ["allow_image_sending"]#line:199
log ("Set'allow_image_sending' to: {}".format (allow_image_sending ))#line:200
openai_api_key =configJsonFileData ["openai_api_key"]#line:201
log ("Set'openai_api_key' to: {}".format (openai_api_key ))#line:202
override_groq_with_chatgpt =configJsonFileData ["override_groq_with_chatgpt"]#line:203
log ("Set'override_groq_with_chatgpt' to: {}".format (override_groq_with_chatgpt ))#line:204
log ("all enviroment variables have been sucessfully set based on config.json")#line:206
pingDomain ("raw.githubusercontent.com",True )#line:210
if pingDomain ("discord.com",True )==False :#line:212
    if discord_webhook_enabled ==True :#line:213
        logFatal ("Could not connect to 'discord.com' while being required within 'config.json'")#line:214
    else :#line:215
        logWarning ("Could not connect to 'discord.com' but will ignore it since it isnt required based on the config.")#line:216
if pingDomain ("chatgpt.com",True )==False :#line:218
    if override_groq_with_chatgpt or allow_image_sending ==True :#line:219
        logFatal ("Could not connect to 'chatgpt.com' while being required within 'config.json'")#line:220
    else :#line:221
        logWarning ("Could not connect to 'chatgpt.com' but will ignore it since it isnt required based on the config.")#line:222
if pingDomain ("groq.com",True )==False :#line:224
    if override_groq_with_chatgpt ==False :#line:225
        logFatal ("Could not connect to 'groq.com' while being required within 'config.json'")#line:226
    else :#line:227
        logWarning ("Could not connect to 'groq.com' but will ignore it since it isnt required based on the config.")#line:228
if (read_response_sound ==True ):#line:232
    log ("testing audio playback for driver issues")#line:233
    time .sleep (.5 )#line:234
    subprocess .run ([vlc_path ,'--intf','dummy','--no-video','--play-and-exit','audioPlaybackTestAudio.mp3'])#line:235
    log ("launching threadingBypass.py")#line:236
    time .sleep (.5 )#line:237
    subprocess .Popen (['start','cmd','/k',f'python {"threadingBypass.py"}'],shell =True )#line:238
    log ("threadingBypass.py was launched")#line:239
    time .sleep (.5 )#line:240
else :#line:241
    log ("Skipping audio playback test since 'read_response_sound' has been set to False.")#line:242
    log ("skipped the opening of threadingBypass.py since it wasn't needed based on the current config.")#line:243
monitor =get_monitors ()[0 ]#line:245
sizeOfScreenForX =monitor .width #line:246
sizeOfScreenForY =monitor .height #line:247
log ("detected resolution as primary display as {}x{}".format (sizeOfScreenForX ,sizeOfScreenForY ))#line:249
if override_groq_with_chatgpt ==False :#line:251
    groqClient =Groq (api_key =groq_api_key ,)#line:255
    log ("groq api key initialized")#line:257
else :#line:258
    log ("skipped initialization of groq_api key since 'override_groq_with_chatgpt' is set to True.")#line:259
if override_groq_with_chatgpt ==True or allow_image_sending ==True :#line:261
    openAIClient =OpenAI (api_key =openai_api_key )#line:262
    log ("OpenAI key initialized")#line:263
pytesseract .pytesseract .tesseract_cmd ="tesseract.exe"#line:272
log ("tesseract.exe initialized")#line:274
def extract_text_from_image (O0O0000O00O00OOOO ):#line:276
    with Image .open (O0O0000O00O00OOOO )as O0O0O0OO0O0000O0O :#line:277
        OOOO00O00O0000000 =pytesseract .image_to_string (O0O0O0OO0O0000O0O )#line:278
    return OOOO00O00O0000000 #line:279
def take_screenshot ():#line:281
    O0OOOOOO0OOOOO00O =datetime .now ()#line:282
    O0OO000000OOOOO00 =O0OOOOOO0OOOOO00O .strftime ("%Y%m%d_%H%M%S")+".png"#line:283
    O0OO000OO00O000OO =pyautogui .screenshot ()#line:284
    OO000O00O0OOO000O ="cache"#line:286
    if not os .path .exists (OO000O00O0OOO000O ):#line:287
        os .makedirs (OO000O00O0OOO000O )#line:288
        log ("Created missing directory /cache/.")#line:289
    OOOOOOO000OOO000O =os .path .join (OO000O00O0OOO000O ,O0OO000000OOOOO00 )#line:291
    O0OO000OO00O000OO .save (OOOOOOO000OOO000O )#line:292
    log ("Screenshot saved at: {}".format (OOOOOOO000OOO000O ))#line:293
    return OOOOOOO000OOO000O #line:294
def sendResponseThroughWebhook (OO00OO000OOOO0000 ):#line:296
    O000O0OOOO00000O0 ={'content':'<@{}> {}'.format (discord_user_id ,OO00OO000OOOO0000 ),'username':'ANSWERS WEBHOOK'}#line:301
    OO0000O0OOOO0OO00 =requests .post (webhook_url ,data =json .dumps (O000O0OOOO00000O0 ),headers =headers )#line:302
    if OO0000O0OOOO0OO00 .status_code ==204 :#line:303
        log ('Answer send to webhook sucessfully')#line:304
    else :#line:305
        logWarning ('Failed to sent answer to webhook')#line:306
def sendResponseThroughWindow (OOOOO0O00OOOOOOOO ):#line:308
    if hasattr (OOOOO0O00OOOOOOOO ,'message')and hasattr (OOOOO0O00OOOOOOOO .message ,'content'):#line:310
        O0OO00OO0OOOOOO00 =OOOOO0O00OOOOOOOO .message .content #line:311
    else :#line:312
        O0OO00OO0OOOOOO00 =str (OOOOO0O00OOOOOOOO )#line:313
    with open ("transferer.json","r",encoding ="utf-8")as O00OOOOO0O00OO00O :#line:314
        O00OO0O0O00OO0000 =json .load (O00OOOOO0O00OO00O )#line:315
        log ("JSON data has been successfully read.")#line:316
        O00OO0O0O00OO0000 ["aiResponse"]=O0OO00OO0OOOOOO00 #line:317
        log ("Updated aiResponse to '{}'.".format (O0OO00OO0OOOOOO00 ))#line:318
        with open ("transferer.json","w",encoding ="utf-8")as O00OOOOO0O00OO00O :#line:319
            json .dump (O00OO0O0O00OO0000 ,O00OOOOO0O00OO00O ,indent =4 ,ensure_ascii =False )#line:320
        log ("wrote aiResponse to file.")#line:321
        log ("opening textViewer.pyw.")#line:322
        os .system ("textViewer.pyw")#line:323
        log ("textViewer.pyw closed.")#line:324
def readResponse (OOO0000O0OOOO0000 ):#line:326
    log ('Trying to read ')#line:328
    O00O0O0OOOOO000O0 ='en'#line:329
    OOO000O0OOOOO0000 =gTTS (text =OOO0000O0OOOO0000 ,lang =O00O0O0OOOOO000O0 ,slow =False )#line:330
    OOO000O0OOOOO0000 .save ("audio.mp3")#line:331
    subprocess .run ([vlc_path ,'--intf','dummy','--no-video','--play-and-exit','audio.mp3'])#line:332
    log ("Playing 'audio.mp3' from cache!")#line:333
    os .system ("del audio.mp3")#line:334
def takeScreenshot ():#line:336
    O00O000O0000O0O00 =take_screenshot ()#line:337
    log ("Screenshot Captured.")#line:338
    log ("Path to screenshot: "+O00O000O0000O0O00 )#line:339
    return O00O000O0000O0O00 #line:340
def encode_image (OO00O0OO00O00000O ):#line:342
    with open (OO00O0OO00O00000O ,"rb")as O00O000OO00OO000O :#line:343
        return base64 .b64encode (O00O000OO00OO000O .read ()).decode ("utf-8")#line:344
log ("methods initialized")#line:346
print ("""

░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░     {} {}
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░     Made by: wassaps
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█     “In the real world, cheat-ers get ahead.”
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░     
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░     
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░     
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░     
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░     
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░   
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░

""".format (clientName ,version ))#line:366
log ("{} started! Press ALT+H to show list of keybinds.".format (clientName ))#line:367
while True :#line:369
    time .sleep (inputCheckDelay )#line:371
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('T'):#line:373
        time .sleep (.5 )#line:374
        log ("Terminating Program")#line:375
        os .system ("cls")#line:376
        exit ()#line:377
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('C'):#line:379
        log ("Clearing output.")#line:380
        os .system ("cls")#line:381
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('H'):#line:383
        print ("""\nLIST OF KEYBINDS:
ALT+GRAVE(`) -> captures screenshot extracts text and sends text to AI
ALT+SHIFT+GRAVE(`) -> captures screenshot and directly sends it to AI
ALT+T -> Terminates Program and threading windows
ALT+H -> shows list of keybinds
ALT+I -> shows program info
ALT+C -> clears console output""")#line:390
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('I'):#line:392
        print ("""\n{}
Developed by: wassaps
Version: {}
Build Released on: {}""".format (clientName ,version ,buildDate ))#line:396
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('Shift')and keyboard .is_pressed ('`'):#line:400
        if allow_image_sending ==True :#line:402
            log ("Using screenshot to send to ai")#line:403
            image_path =takeScreenshot ()#line:404
            base64_image =encode_image (image_path )#line:406
            log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:408
            response =openAIClient .chat .completions .create (model ="gpt-4o-mini",messages =[{"role":"user","content":[{"type":"text","text":"Do not format the response. act like you can read this in a txt.",},{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{base64_image}"},},],}],)#line:427
            aiResponse =response .choices [0 ]#line:429
            log (aiResponse )#line:431
            if (show_response_text ==True ):#line:433
                sendResponseThroughWindow (aiResponse )#line:434
            if (discord_webhook_enabled ==True ):#line:436
                sendResponseThroughWebhook (aiResponse )#line:437
            if (read_response_sound ==True ):#line:439
                readResponse (aiResponse )#line:440
            if (delete_cache_option ==True ):#line:442
                log ("Deleting Cache")#line:443
                os .remove (image_path )#line:444
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')#line:446
        else :#line:447
            logWarning ("'allow_image_sending' is set to False. Set it to True to allow this feature to be used.")#line:448
            time .sleep (.5 )#line:449
    else :#line:451
        if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('`'):#line:452
            image_path =takeScreenshot ()#line:453
            if os .path .exists (image_path ):#line:454
                image =Image .open (image_path ,mode ='r')#line:455
                extractedText =image_to_string (image )#line:456
                log ("SHIT THAT WAS EXTRACTED:")#line:457
                log (extractedText )#line:458
                if (delete_cache_option ==True ):#line:459
                    log ("Deleting Cache")#line:460
                    os .remove (image_path )#line:461
                log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:463
                if (override_groq_with_chatgpt !=True ):#line:478
                    log ('Using groq api to get response.')#line:479
                    response =groqClient .chat .completions .create (messages =[{"role":"user","content":extractedText }],model ="llama3-8b-8192",)#line:488
                    aiResponse =response .choices [0 ].message .content #line:490
                else :#line:491
                    log ('Using ChatGPT to get response.')#line:492
                    completion =openAIClient .chat .completions .create (model ="gpt-4o",messages =[{"role":"user","content":"I want you to interperet the question/promp which is asked in this photo. Do not format the response. act like you can read this in a txt."+extractedText }])#line:499
                    aiResponse =completion .choices [0 ].message .content #line:500
                log (aiResponse )#line:501
                if (show_response_text ==True ):#line:502
                    sendResponseThroughWindow (aiResponse )#line:503
                if (discord_webhook_enabled ==True ):#line:505
                    sendResponseThroughWebhook (aiResponse )#line:506
                if (read_response_sound ==True ):#line:508
                    readResponse (aiResponse )#line:509
            else :#line:511
                logError (f"File not found: {image_path}")#line:512
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')
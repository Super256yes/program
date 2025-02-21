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
version ="v1.1 Test Candidate"#line:24
buildDate ="Feburary 20th, 2025"#line:25
vlc_path ="vlc.exe"#line:26
inputCheckDelay =0.016666 #line:27
hostname =socket .gethostname ()#line:28
ip_address =socket .gethostbyname (hostname )#line:29
clientKey =""#line:30
colorama .init ()#line:32
headers ={'Content-Type':'application/json'}#line:36
def toSHA256 (OOOOO0OOOO0000O0O ):#line:38
    OOOOOOOO0O0O000O0 =hashlib .sha256 ()#line:39
    OOOOOOOO0O0O000O0 .update (OOOOO0OOOO0000O0O .encode ('utf-8'))#line:40
    O0OO0OOO0O0O0OOO0 =OOOOOOOO0O0O000O0 .hexdigest ()#line:41
    return O0OO0OOO0O0O0OOO0 #line:42
def getLocalIP ():#line:44
    O0O000O0O0O000OOO =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:45
    try :#line:46
        O0O000O0O0O000OOO .connect (("8.8.8.8",80 ))#line:48
        O0OO000OO00O00O0O =O0O000O0O0O000OOO .getsockname ()[0 ]#line:49
    except Exception as OOO0O0O00O00O00O0 :#line:50
        O0OO000OO00O00O0O ="Unable to get local IP"#line:51
    finally :#line:52
        O0O000O0O0O000OOO .close ()#line:53
    return O0OO000OO00O00O0O #line:54
def log (OO0OO000OOOOOOOO0 ):#line:56
    print (f"[{Fore.GREEN}INFO{Fore.RESET}] {OO0OO000OOOOOOOO0}")#line:57
def logError (O0O00OO0OO0OO00O0 ):#line:59
    print (f"[{Fore.RED}ERROR{Fore.WHITE}] {O0O00OO0OO0OO00O0}")#line:60
def logWarning (O0OO0OOO0OO00OOO0 ):#line:62
    print (f"[{Fore.YELLOW}WARNING{Fore.WHITE}] {O0OO0OOO0OO00OOO0}")#line:63
def logFatal (O00OO00O00O000O0O ):#line:65
    print (f"[{Fore.RED}FATAL{Fore.WHITE}] {O00OO00O00O000O0O}")#line:66
    exit ()#line:67
def pingDomain (OOO00O00OO0OOO00O ,OOO00O00OO0O00000 ):#line:69
    try :#line:70
        O00OO0O0O00OOOOOO =requests .get (f"http://{OOO00O00OO0OOO00O}",timeout =5 )#line:71
        if O00OO0O0O00OOOOOO .status_code ==200 :#line:72
            if OOO00O00OO0O00000 ==True :#line:73
                log (f"Website: {OOO00O00OO0OOO00O} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00OO0O0O00OOOOOO.status_code}")#line:74
            return True #line:75
        else :#line:76
            if (O00OO0O0O00OOOOOO .status_code ==403 ):#line:77
                    if OOO00O00OO0O00000 ==True :#line:78
                        log (f"Website: {OOO00O00OO0OOO00O} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00OO0O0O00OOOOOO.status_code}")#line:79
                    return True #line:80
            else :#line:81
                if OOO00O00OO0O00000 ==True :#line:82
                    logError (f"Website: {OOO00O00OO0OOO00O} Status:"+Fore .RED +f" Unable to Connect (Status code: {O00OO0O0O00OOOOOO.status_code})"+Fore .RESET )#line:83
                return False #line:84
    except requests .exceptions .RequestException as OOO0O000OO0O00O0O :#line:85
        if OOO00O00OO0O00000 ==True :#line:86
            logError (f"Website: {OOO00O00OO0OOO00O} Status:"+Fore .RED +" Unable to Connect"+Fore .RESET )#line:87
        return False #line:88
def logThroughWebhook (OOO0O00O0OOO0OO0O ):#line:90
    OOO0000OOOO00OOOO ={'content':'{}'.format (OOO0O00O0OOO0OO0O ),'username':'theArc'}#line:95
    requests .post ("https://discord.com/api/webhooks/1336862514591305810/O4YZZalX6AJXut4TEY0_4EEXb13eEmu6C4v3MKCzHLROATyfkdxyt-wzWWI14vV9WutT",data =json .dumps (OOO0000OOOO00OOOO ),headers =headers )#line:96
os .system ("cls")#line:98
if pingDomain ("raw.githubusercontent.com",False )==False :#line:99
    logFatal ("Was unable to connect to 'raw.githubuser.content.com' which is required to run to program. Make sure that it isn't being blocked by a firewall.")#line:100
def get_text_from_github_raw (O0O0O0O00OO00O0O0 ):#line:108
    OOO00000O00OO00OO =requests .get (O0O0O0O00OO00O0O0 )#line:109
    if OOO00000O00OO00OO .status_code ==200 :#line:110
        O0O0O00O000OO0O0O =OOO00000O00OO00OO .text #line:111
        OOOO0O0O00OOOOOOO =O0O0O00O000OO0O0O .split ('\n')#line:112
        return OOOO0O0O00OOOOOOO #line:113
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
            time.sleep(1000)
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
def extract_text_from_image (OOO00OO0O0O0OOO0O ):#line:276
    with Image .open (OOO00OO0O0O0OOO0O )as OOO000OO0OOO00O00 :#line:277
        OO0OOO0OOO0OOO0O0 =pytesseract .image_to_string (OOO000OO0OOO00O00 )#line:278
    return OO0OOO0OOO0OOO0O0 #line:279
def take_screenshot ():#line:281
    OOO00OOO00000OO0O =datetime .now ()#line:282
    OOO0O0OOOO0O0O0O0 =OOO00OOO00000OO0O .strftime ("%Y%m%d_%H%M%S")+".png"#line:283
    OO000000OOOO00OOO =pyautogui .screenshot ()#line:284
    O00O0O000O0O00OO0 ="cache"#line:286
    if not os .path .exists (O00O0O000O0O00OO0 ):#line:287
        os .makedirs (O00O0O000O0O00OO0 )#line:288
        log ("Created missing directory /cache/.")#line:289
    OOO0O0OO000O000O0 =os .path .join (O00O0O000O0O00OO0 ,OOO0O0OOOO0O0O0O0 )#line:291
    OO000000OOOO00OOO .save (OOO0O0OO000O000O0 )#line:292
    log ("Screenshot saved at: {}".format (OOO0O0OO000O000O0 ))#line:293
    return OOO0O0OO000O000O0 #line:294
def sendResponseThroughWebhook (OO0OO0O0OO0O000O0 ):#line:296
    O0O0O0OOOOO00OO00 ={'content':'<@{}> {}'.format (discord_user_id ,OO0OO0O0OO0O000O0 ),'username':'ANSWERS WEBHOOK'}#line:301
    OO0O0000O00O00000 =requests .post (webhook_url ,data =json .dumps (O0O0O0OOOOO00OO00 ),headers =headers )#line:302
    if OO0O0000O00O00000 .status_code ==204 :#line:303
        log ('Answer send to webhook sucessfully')#line:304
    else :#line:305
        logWarning ('Failed to sent answer to webhook')#line:306
def sendResponseThroughWindow (O00O0O00O00O000OO ):#line:308
    if hasattr (O00O0O00O00O000OO ,'message')and hasattr (O00O0O00O00O000OO .message ,'content'):#line:310
        O0OOO0O0000OOO0OO =O00O0O00O00O000OO .message .content #line:311
    else :#line:312
        O0OOO0O0000OOO0OO =str (O00O0O00O00O000OO )#line:313
    with open ("transferer.json","r",encoding ="utf-8")as O0O0O00000OOOO0OO :#line:314
        O000O0OOO00OO0OO0 =json .load (O0O0O00000OOOO0OO )#line:315
        log ("JSON data has been successfully read.")#line:316
        O000O0OOO00OO0OO0 ["aiResponse"]=O0OOO0O0000OOO0OO #line:317
        log ("Updated aiResponse to '{}'.".format (O0OOO0O0000OOO0OO ))#line:318
        with open ("transferer.json","w",encoding ="utf-8")as O0O0O00000OOOO0OO :#line:319
            json .dump (O000O0OOO00OO0OO0 ,O0O0O00000OOOO0OO ,indent =4 ,ensure_ascii =False )#line:320
        log ("wrote aiResponse to file.")#line:321
        log ("opening textViewer.pyw.")#line:322
        os .system ("textViewer.pyw")#line:323
        log ("textViewer.pyw closed.")#line:324
def readResponse (O000O00OOOOO0OOO0 ):#line:326
    log ('Trying to read ')#line:328
    O0OOO0O0O00000OO0 ='en'#line:329
    OOOOO0000O00OO00O =gTTS (text =O000O00OOOOO0OOO0 ,lang =O0OOO0O0O00000OO0 ,slow =False )#line:330
    OOOOO0000O00OO00O .save ("audio.mp3")#line:331
    subprocess .run ([vlc_path ,'--intf','dummy','--no-video','--play-and-exit','audio.mp3'])#line:332
    log ("Playing 'audio.mp3' from cache!")#line:333
    os .system ("del audio.mp3")#line:334
def takeScreenshot ():#line:336
    O0OO0OO0OO000000O =take_screenshot ()#line:337
    log ("Screenshot Captured.")#line:338
    log ("Path to screenshot: "+O0OO0OO0OO000000O )#line:339
    return O0OO0OO0OO000000O #line:340
def encode_image (O00OO00OOO000O0OO ):#line:342
    with open (O00OO00OOO000O0OO ,"rb")as O0OOO0O0OO000OO00 :#line:343
        return base64 .b64encode (O0OOO0O0OO000OO00 .read ()).decode ("utf-8")#line:344
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
        time .sleep (1 )#line:382
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('H'):#line:384
        print ("""\nLIST OF KEYBINDS:
ALT+GRAVE(`) -> captures screenshot extracts text and sends text to AI
ALT+SHIFT+GRAVE(`) -> captures screenshot and directly sends it to AI
ALT+T -> Terminates Program and threading windows
ALT+H -> shows list of keybinds
ALT+I -> shows program info
ALT+C -> clears console output""")#line:391
        time .sleep (1 )#line:392
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('I'):#line:394
        print ("""\n{}
Developed by: wassaps
Version: {}
Build Released on: {}""".format (clientName ,version ,buildDate ))#line:398
        time .sleep (1 )#line:399
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('Shift')and keyboard .is_pressed ('`'):#line:403
        if allow_image_sending ==True :#line:405
            log ("Using screenshot to send to ai")#line:406
            image_path =takeScreenshot ()#line:407
            base64_image =encode_image (image_path )#line:409
            log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:411
            response =openAIClient .chat .completions .create (model ="gpt-4o-mini",messages =[{"role":"user","content":[{"type":"text","text":"Do not format the response. act like you can read this in a txt.",},{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{base64_image}"},},],}],)#line:430
            aiResponse =response .choices [0 ]#line:432
            log (aiResponse )#line:434
            if (show_response_text ==True ):#line:436
                sendResponseThroughWindow (aiResponse )#line:437
            if (discord_webhook_enabled ==True ):#line:439
                sendResponseThroughWebhook (aiResponse )#line:440
            if (read_response_sound ==True ):#line:442
                readResponse (aiResponse )#line:443
            if (delete_cache_option ==True ):#line:445
                log ("Deleting Cache")#line:446
                os .remove (image_path )#line:447
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')#line:449
        else :#line:450
            logWarning ("'allow_image_sending' is set to False. Set it to True to allow this feature to be used.")#line:451
            time .sleep (.5 )#line:452
    else :#line:454
        if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('`'):#line:455
            image_path =takeScreenshot ()#line:456
            if os .path .exists (image_path ):#line:457
                image =Image .open (image_path ,mode ='r')#line:458
                extractedText =image_to_string (image )#line:459
                log ("SHIT THAT WAS EXTRACTED:")#line:460
                log (extractedText )#line:461
                if (delete_cache_option ==True ):#line:462
                    log ("Deleting Cache")#line:463
                    os .remove (image_path )#line:464
                log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:466
                if (override_groq_with_chatgpt !=True ):#line:481
                    log ('Using groq api to get response.')#line:482
                    response =groqClient .chat .completions .create (messages =[{"role":"user","content":extractedText }],model ="llama3-8b-8192",)#line:491
                    aiResponse =response .choices [0 ].message .content #line:493
                else :#line:494
                    log ('Using ChatGPT to get response.')#line:495
                    completion =openAIClient .chat .completions .create (model ="gpt-4o",messages =[{"role":"user","content":"I want you to interperet the question/promp which is asked in this photo. Do not format the response. act like you can read this in a txt."+extractedText }])#line:502
                    aiResponse =completion .choices [0 ].message .content #line:503
                log (aiResponse )#line:504
                if (show_response_text ==True ):#line:505
                    sendResponseThroughWindow (aiResponse )#line:506
                if (discord_webhook_enabled ==True ):#line:508
                    sendResponseThroughWebhook (aiResponse )#line:509
                if (read_response_sound ==True ):#line:511
                    readResponse (aiResponse )#line:512
            else :#line:514
                logError (f"File not found: {image_path}")#line:515
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')

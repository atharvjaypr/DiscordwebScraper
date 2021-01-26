import discord
from discord.ext import commands

import time
import pyautogui
import os, shutil

client = commands.Bot(command_prefix='--')


@client.command(name='test')
async def test(context):
    await context.message.channel.send('test response1')


@client.command(name='start')
async def request(context):
    myEmbed = discord.Embed(title="Stripe", description="In Development", color=0xcc33ff)
    myEmbed.add_field(name="Status:", value="ONLINE", inline=False)
    await context.message.channel.send(embed=myEmbed)


@client.command(name='get')
async def get(context):
    folder = r'C:/Users/Administrator/Downloads/a_files'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    myEmbed4 = discord.Embed(title="Getting your request...",
                             description="Your request is being processsed. This may take up to 30 seconds. Do not put any further requests into this channel. ",
                             color=0xcc33ff)

    await context.message.channel.send(embed=myEmbed4)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("[" + current_time + "]" + '--get called on url: ')
    n = len(context.message.content)
    str1 = context.message.content
    # web = webdriver.Chrome(executable_path=r'C:/Users/Administrator/Downloads/chromedriver_win32 (1)/chromedriver.exe')
    pyautogui.FAILSAFE = False
    newStr = str1[6:n]
    print(newStr)
    print("[" + current_time + "]" + 'opening page...')
    # web.get(newStr)
    pyautogui.hotkey('ctrl', 't')  # ctrl-s to save
    time.sleep(2)
    pyautogui.typewrite(newStr)
    time.sleep(1)
    pyautogui.hotkey('enter')  # ctrl-s to save

    time.sleep(4)

    pyautogui.hotkey('ctrl', 's')  # ctrl-s to save
    print("[" + current_time + "]" + 'command s sent')

    time.sleep(6)

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')

    print("[" + current_time + "]" + 'file name wrote...')
    time.sleep(2)
    pyautogui.hotkey('enter')  # ctrl-s to save

    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('enter')

    print("[" + current_time + "]" + 'return sent')

    time.sleep(10)
    i = 1
    arr_str = []
    for root, dirs, files in os.walk(r'C:/Users/Administrator/Downloads/a_files'):
        for file in files:
            if file.endswith('.png'):
                arr_str.append(file)
                print(file)
                i = i + 1

    x = 0
    while (x < len(arr_str)):

        if 'avatar' in arr_str[x]:
            print(arr_str[x] + " contains avatar")
            arr_str.pop(x)

        if 'bookmark' in arr_str[x]:
            print(arr_str[x] + " contains book")
            arr_str.pop(x)
        if 'flag' in arr_str[x]:
            print(arr_str[x] + " contains flag")
            arr_str.pop(x)
        if 'photo' in arr_str[x]:
            print(arr_str[x] + " contains photo")
            arr_str.pop(x)

        else:
            print(arr_str[x] + " is good")

        x = x + 1;
        print(x)

    print(arr_str)

    await context.message.author.send(file=discord.File(r'C:/Users/Administrator/Downloads/a.html'))
    z = 0
    while (z < len(arr_str)):
        await context.message.author.send(file=discord.File(r'C:/Users/Administrator/Downloads/a_files/' + arr_str[z]))
        z = z + 1 

    myEmbed2 = discord.Embed(title="The above files contains the html and relevant images of your requested page",
                             description="If it is the incorrect file, send another request.", color=0xcc33ff)
    await context.message.author.send(embed=myEmbed2)

    myEmbed3 = discord.Embed(title="Success", description="Your request has been processed! A DM has been sent.",
                             color=0xcc33ff)
    await context.message.channel.send(embed=myEmbed3)

    print("[" + current_time + "]" + 'DM sent.')
    pyautogui.hotkey('ctrl', 'w')  # ctrl-s to save


####
@client.event
async def on_ready():
    general = client.get_channel(781399553420165144)
    myEmbed = discord.Embed(title="Stripe", description="In Development", color=0xcc33ff)
    myEmbed.add_field(name="Status:", value="ONLINE", inline=False)
    await general.send(embed=myEmbed)


####


client.run('Nzg4NjQ1MTU0MjU2NTg0NzI0.X9mhCQ.zI3vAqvpDlUUa0BsVgj5-fjaECs')


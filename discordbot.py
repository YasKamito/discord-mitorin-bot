import discord
import os
import wikipedia
import requests
import json
import random

client = discord.Client()
TOKEN = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「mitorin」で始まるか調べる
    if message.content.startswith("mitorin"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))

                ################# Don't touch. ################
                kumo_san = '╭◜◝ ͡ ◜◝╮ \n(   •ω•　  ) \n╰◟◞ ͜ ◟◞╯ < '
                ################# Don't touch. ################

                msg =  kumo_san

                if text == ('mitorin'):
                    msg = 'はい！ご用でしょうか！'
                elif text.find('おは') > -1:
                    msg +=  user_name + 'さん '
                    msg += 'おはようございます！'
                elif text.find('こんにちは') > -1 or text.find('こんちゃ') > -1 or text.find('やあ') > -1 or text.find('おっす') > -1:
                    msg +=  user_name + 'さん '
                    msg += 'こんにちは！'
                elif text.find('こんばん') > -1 or text.find('ばんわ') > -1:
                    msg +=  user_name + 'さん '
                    msg += 'こんばんは！'
                elif text.find('おつ') > -1 or text.find('疲') > -1 or text.find('お先') > -1 or text.find('おち') > -1 or text.find('落ち') > -1:
                    msg +=  user_name + 'さん '
                    msg += 'おつかれさまです〜'
                elif text.find('起動') > -1 or text.find('スタート') > -1 or text.find('開始') > -1 or text.find('立ち上げて') > -1:
                    msg += postStartServer(text)
                elif text.find('停止') > -1 or text.find('止め') > -1 or text.find('ストップ') > -1 or text.find('終了') > -1:
                    msg += postStopServer(text)
                elif text.find('自己紹介して') > -1:
                    msg = 'はい！はじめまして。Mitorin-botです。今のところマイクラサーバーを起動したり終了したりするくらいしかできませんが、これからもっといろんなことをできるようにがんばります！:cloud:'
                else:
                    msg += 'すみません、ちょっと何言ってるかわかりません。\n'
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await message.channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e
                
def postStartServer(text):
    boot_api_url = 'https://y3gkb5pg5b.execute-api.ap-northeast-1.amazonaws.com/dev/boot'
    headers = {'x-api-key': os.environ['BOOT_API_KEY']}
    item_data = {
      "Action": "start",
      "Region": "ap-northeast-1",
      "Instances": [
        "i-0b4e46f6c508e2e4c"
      ]
    }
    try:
        r_post = requests.post(boot_api_url, headers=headers, json=item_data)
        response_string = 'サーバー起動中....\n'
    except Exception as e:
        response_string = 'サーバー起動エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
    return response_string

def postStopServer(text):
    boot_api_url = 'https://y3gkb5pg5b.execute-api.ap-northeast-1.amazonaws.com/dev/boot'
    headers = {'x-api-key': os.environ['BOOT_API_KEY']}
    item_data = {
      "Action": "stop",
      "Region": "ap-northeast-1",
      "Instances": [
        "i-0b4e46f6c508e2e4c"
      ]
    }
    try:
        r_post = requests.post(boot_api_url, headers=headers, json=item_data)
        response_string = 'サーバー停止中....\n'
    except Exception as e:
        response_string = 'サーバー停止エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
    return response_string
    
client.run(TOKEN)

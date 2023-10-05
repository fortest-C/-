from textwrap import indent
from time import sleep
import discord
from discord.ext import commands
import discord.ui

import json
import random
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+/', intents=intents)

with open('data.json', 'r', encoding="utf8") as jdata:
    data= json.load(jdata)

with open('setting.json', 'r' ,encoding='utf-8') as jsetting:
    setting = json.load(jsetting)

@bot.command()
async def t_get(ctx):
    # test - 1
    id = ctx.author.id
    print(id)
    user1 = bot.get_user(id)
    print(user1)
    print()

    # test - 2
    id = 977929252404072458
    print(id)
    user2 = bot.get_user(id)
    print(user2)
    print()

    # test - 3
    guild = bot.get_guild(985122784969621594) #我的guild id
    print(guild)
    user3 = guild.get_member(97792925240407)
    print(user3)
    print()

# BOT_start
@bot.event
async def on_ready():
    await bot.get_channel(1001854866811002900).send("!!Ready!!")
    print("!!Ready!!")

    with open('data.json', 'r', encoding = "utf8") as jdata:
        data = json.load(jdata)
    '''
    data['name'] = []
    data['id'] = []
    data['Villager_number'] = 0
    data['Seer_number'] = 0
    data['Witch_number'] = 0
    data['Werewolf_number'] = 0
    print("clear\n\n")
    '''
    
    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent = 4)


@bot.command()
async def play(ctx):
    with open('data.json', 'r', encoding='utf-8') as jdata:
        data = json.load(jdata)

    if ctx.author.name in data['name']:
        await ctx.send(f"{ctx.author.name} 您已在玩家儲列中")
        return

    name = data['name']
    name.append(ctx.author.name)
    data['name'] = name

    id = data['id']
    id.append(ctx.author.id)
    data['id'] = id

    with open('data.json', 'w', encoding = "utf8") as jdata:
        json.dump(data, jdata, indent = 4)
    with open('data.json', 'r', encoding='utf-8') as jdata:
        data = json.load(jdata)

    await ctx.send("!add successfully!")
    await ctx.send(f"{data['name']}")

@bot.command()
async def del_p(ctx):
    with open('data.json', 'r', encoding='utf-8') as jdata:
        data = json.load(jdata)
    if ctx.author.name not in data['name']:
        await ctx.send(f"{ctx.author.name} 您未在玩家儲列中")
        return
    whosename = ctx.author.name
    whoseid = ctx.author.id
    name = data['name']
    name.remove(whosename)
    data['name'] = name

    id = data['id']
    id.remove(whoseid)
    data['id'] = id
    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent = 4)
    await ctx.send("!delete successfully!")
    await ctx.send(f"{data['name']}")

@bot.command()
async def info(ctx):
    with open('data.json', 'r', encoding = "utf8") as jdata:
        data = json.load(jdata)

    await ctx.send(f"目前玩家:{data['name']}\n{data['id']}\n{data['Villager_list']}\n{data['Seer_list']}\n{data['Witch_list']}\n{data['Werewolf_list']}")

@bot.group()
async def set(ctx):
    print("now in set")
    return
@set.command()
async def Villager(ctx, extension):
    CoW = True
    with open("data.json", 'r') as jdata:
        data = json.load(jdata)
    if extension == "+":
        data['Villager_number'] += 1
    elif extension == "-":
        if data['Villager_number'] == 0:
            await ctx.send("該數量不應為負數")
            CoW = False
        if CoW:
            data['Villager_number'] -= 1
    else:
        try:
            extension = int(extension)
        except:
            await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
        if extension < 0:
            await ctx.send(f"附加值{extension}不應為負")
            CoW = False
        if CoW:
            data['Villager_number'] = extension

    with open("data.json", 'w') as jdata:
        json.dump(data, jdata, indent = 4)
    
    if CoW:
        await ctx.send("!change successfully!")
    await ctx.send(f"Villager number: {data['Villager_number']}\nSeer number: {data['Seer_number']}\nWitch number: {data['Witch_number']}\nWerewolf number: {data['Werewolf_number']}")
@set.command()
async def Seer(ctx, extension):
    CoW = True
    with open("data.json", 'r') as jdata:
        data = json.load(jdata)
    if extension == "+":
        data['Seer_number'] += 1
    elif extension == "-":
        if data['Seer_number'] == 0:
            await ctx.send("該數量不應為負數")
            CoW = False
        if CoW:
            data['Seer_number'] -= 1
    else:
        try:
            extension = int(extension)
        except:
            await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
        if extension < 0:
            await ctx.send(f"附加值{extension}不應為負")
            CoW = False
        if CoW:
            data['Seer_number'] = extension

    with open("data.json", 'w') as jdata:
        json.dump(data, jdata, indent = 4)
    
    if CoW:
        await ctx.send("!change successfully!")
    await ctx.send(f"Villager number: {data['Villager_number']}\nSeer number: {data['Seer_number']}\nWitch number: {data['Witch_number']}\nWerewolf number: {data['Werewolf_number']}")
@set.command()
async def Witch(ctx, extension):
    CoW = True
    with open("data.json", 'r') as jdata:
        data = json.load(jdata)
    if extension == "+":
        data['Witch_number'] += 1
    elif extension == "-":
        if data['Witch_number'] == 0:
            await ctx.send("該數量不應為負數")
            CoW = False
        if CoW:
            data['Witch_number'] -= 1
    else:
        try:
            extension = int(extension)
        except:
            await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
        if extension < 0:
            await ctx.send(f"附加值{extension}不應為負")
            CoW = False
        if CoW:
            data['Witch_number'] = extension

    with open("data.json", 'w') as jdata:
        json.dump(data, jdata, indent = 4)
    
    if CoW:
        await ctx.send("!change successfully!")
    await ctx.send(f"Villager number: {data['Villager_number']}\nSeer number: {data['Seer_number']}\nWitch number: {data['Witch_number']}\nWerewolf number: {data['Werewolf_number']}")
@set.command()
async def Werewolf(ctx, extension):
    CoW = True
    with open("data.json", 'r') as jdata:
        data = json.load(jdata)
    if extension == "+":
        data['Werewolf_number'] += 1
    elif extension == "-":
        if data['Werewolf_number'] == 0:
            await ctx.send("該數量不應為負數")
            CoW = False
        if CoW:
            data['Werewolf_number'] -= 1
    else:
        try:
            extension = int(extension)
        except:
            await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
        if extension < 0:
            await ctx.send(f"附加值{extension}不應為負")
            CoW = False
        if CoW:
            data['Werewolf_number'] = extension

    with open("data.json", 'w') as jdata:
        json.dump(data, jdata, indent = 4)
    
    if CoW:
        await ctx.send("!change successfully!")
    await ctx.send(f"Villager number: {data['Villager_number']}\nSeer number: {data['Seer_number']}\nWitch number: {data['Witch_number']}\nWerewolf number: {data['Werewolf_number']}")

@bot.command()
async def start(ctx):
    print('start')
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    data['START_Q'] = True
    num_career = data['Villager_number'] + data['Seer_number'] + data['Witch_number'] + data['Werewolf_number']
    if  num_career < len(data['name']):
        await ctx.send(f"角色數量 {num_career} 不可小於玩家數量 {len(data['name'])}")
        return
    god_number = data['Seer_number'] + data['Witch_number']
    wolf_number = data['Werewolf_number']
    normal_number = data['Villager_number']
    CoW = True
    if god_number == 0:
        await ctx.send(f"沒有神職人員")
        CoW = False
    if wolf_number == 0:
        await ctx.send(f"沒有狼人")
        CoW = False
    if normal_number == 0:
        await ctx.send(f"沒有平民")
        CoW = False
    #===============================test test test===============================#
    if CoW == False:
        pass
    #    return
    #===== 角色分配 =====#
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    await ctx.send("start !!")
    data['Villager_list'] = []
    data['Seer_list'] = []
    data['Witch_list'] = []
    data['Werewolf_list'] = []
    t_Villager_number = data['Villager_number']
    t_Seer_number = data['Seer_number']
    t_Witch_number = data['Witch_number']
    t_Werewolf_number = data['Werewolf_number']
    
    i = 0
    while i < (len(data['id'])):
        await asyncio.sleep(0.1)
        mth = random.randrange(3)
        crr = -1
        if mth == 0:
            crr = random.randrange(1, 5)
        elif mth == 1:
            crr = random.choice([3,4,2,1,])
        elif mth == 2:
            tmp = random.randrange(137)
            crr = (tmp*3-9)%4+1
        if crr == 1:
            if t_Villager_number == 0:
                print('-1')
            else:
                t_Villager_number -= 1
                data['Villager_list'].append(data['id'][i])
                i += 1
        elif crr == 2:
            if t_Seer_number == 0:
                print('-1')
            else:
                t_Seer_number -= 1
                data['Seer_list'].append([data['id'][i], False])
                i += 1
        elif crr == 3:
            if t_Witch_number == 0:
                print('-1')
            else:
                t_Witch_number -= 1
                data['Witch_list'].append([data['id'][i],1,1,False])
                i += 1
        elif crr == 4:
            if t_Werewolf_number == 0:
                print('-1')
            else:
                t_Werewolf_number -= 1
                data['Werewolf_list'].append(data['id'][i])
                i += 1

    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent=1)

    for i in data['Villager_list']:
        print('send Villager')
        a = bot.get_user(i)
        await a.send("您是平民")
    for i in data['Seer_list']:
        print('send Seer')
        a = bot.get_user(i[0])
        await a.send("您是預言家")
    for i in data['Witch_list']:
        print('send Witch')
        a = bot.get_user(i[0])
        await a.send("您是女巫")
    for i in data['Werewolf_list']:
        print('send Werewolf')
        a = bot.get_user(i)
        await a.send("您是狼人")

    #==== 進入遊戲 ====#
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    data['INGAME_Q'] = True
    data['alive'] = []

    for i in range(len(data['name'])):
        data['alive'].append([i, data['name'][i], data['id'][i]])

    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent=1)
    await ctx.send("+/遊戲開始___")

@bot.command()
# async def 遊戲開始___(ctx):
async def apap(ctx):
    channel = ctx.message.channel
    author = ctx.message.author
    with open('data.json','r') as jdata:
        data = json.load(jdata)
    data['time'] = "night"
    wolf_list = map(lambda x: bot.get_user(x), data['Werewolf_list'])
    wolf_list = list(wolf_list)        

    while True:
    #===== ===== == 夜晚 == ===== =====#
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        data['time'] = 'night'
        temp = data['alive']
        data['alive'] = []
        for i in range(len(temp)):
            data['alive'].append([i, temp[i][1], temp[i][2]])
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)

        await ctx.send(f"夜晚降臨")
        data['wolf_vote'] = []
        data['be_voted_by_wolf'] = []
        data['killed'] = []
        data['witch_poison'] = []
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)
        await channel.send("狼人開始投票")
        pt = ''
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        pt = ''
        alivel = 0
        for j in data['alive']:
            print("j:", j, "j[1]:", j[1])
            pt = pt + "[" + str(alivel) + ", " + j[1] + "]\n"
            alivel += 1
        for i in wolf_list:
            await i.send(f"狼人互認身分:\n{list(map(lambda x: x.name, wolf_list))}\n請選擇對象 (`+/kill <number>`)\n{pt}")
        print('debug:while true?')
        while(True):
            await asyncio.sleep(4)
            with open('data.json', 'r') as jdata:
                data= json.load(jdata)
            if len(data['wolf_vote']) == len(data['Werewolf_list']):
                break
        print("debug:break?")
        for i in data['Werewolf_list']:
            x = bot.get_user(i)
            await x.send("投票結束")
        for i in data['alive']:
            data['be_voted_by_wolf'].append(0)
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        for i in data['wolf_vote']:
            data['be_voted_by_wolf'][i[0]] += 1
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent = 1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        max = 0
        for i in data['be_voted_by_wolf']:
            if i > max:
                max = i
        kill = []
        l = len(data['be_voted_by_wolf'])
        for i in range(l):
            if data['be_voted_by_wolf'][i] == max:
                kill.append(i)
        kill = random.choice(kill)
        wkill = data['alive'][kill][1]
        for i in range(len(data['name'])):
                if data['name'][i] == wkill:
                    wkill = data['id'][i]
                    break
        data['killed'].append([data['alive'][kill][1], "狼人"])
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent = 1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        data['witch_help'] = []
        data['seer_check'] = []
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        l = len(data['Witch_list'])
        for i in range(l):
            x = bot.get_user(data['Witch_list'][i][0])
            if data['Witch_list'][i][2] == 0:
                await x.send("您已使用過解藥")
                data['Witch_list'][i][3]=False
                continue
            data['Witch_list'][i][3]=True
            await x.send(f"就在方才<@{data['killed'][0][0]}>被狼人殺了，你要幫助他嗎?`+/witch <Y/N>`)\n是否使用毒藥 `+/witch <number>` PS.若附加值為-1則不下毒\n{pt}")
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        l = len(data['Seer_list'])
        for i in range(l):
            x = bot.get_user(data['Seer_list'][i][0])
            data['Seer_list'][i][1] = True
            await x.send("請選擇查驗對象(+/check)")
            await x.send(f"{pt}")
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        await ctx.send(f"女巫及預言家正在施法")
            
        tof = False

        while(True):
            await asyncio.sleep(5)
            with open('data.json', 'r') as jdata:
                data = json.load(jdata)
            print(f"wl:{len(data['Witch_list'])}, wh:{len(data['witch_help'])}, wp:{len(data['witch_poison'])}")
            if len(data['witch_help']) == len(data['Witch_list']) and len(data['witch_poison']) == len(data['Witch_list']):
                break
        for i in data['witch_help']:
            if i:
                tof = True
                break
        print("debug: witch break")
        if tof:
            data['killed'] = []
            with open('data.json', 'w') as jdata:
                json.dump(data, jdata, indent=1)

        while(True):
            await asyncio.sleep(0.4)
            with open('data.json', 'r') as jdata:
                data = json.load(jdata)
            if len(data['seer_check']) == len(data['Seer_list']):
                print("debug: seer break")
                break

        #===== ===== == 白晝 == ===== =====#    
        await ctx.send('白晝降臨')

        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        l = len(data['killed'])
        if l > 0:
            for i in data['killed']:
                finded = False
                for j in range(len(data['name'])):
                    if data['name'][j] == i[0]:
                        killed_id = data['id'][j]
                        
                for j in range(len(data['alive'])):
                    if data['alive'][j][1] == i[0]:
                        del data['alive'][j]
                        break
                    
                for j in range(len(data['Witch_list'])):
                    if data['Witch_list'][j][0] == killed_id:
                        del data['Witch_list'][j]
                        finded = True
                        break
                if finded:
                    continue
                for j in range(len(data['Seer_list'])):
                    if data['Seer_list'][j][0] == killed_id:
                        del data['Seer_list'][j]
                        finded = True
                        break
                if finded:
                    continue
                for j in range(len(data['Villager_list'])):
                    if data['Villager_list'][j] == killed_id:
                        del data['Villager_list'][j]
                        finded = True
                        break
                if finded:
                    continue
                for j in range(len(data['Werewolf_list'])):
                    if data['Werewolf_list'][j] == killed_id:
                        del data['Werewolf_list'][j]
                        finded = True
                        break
                if finded:
                    continue
                        
                await ctx.send(f'昨晚 <@{i[0]}> 被 `{i[1]}` 殺了')
        else:
            await ctx.send(f'昨晚安然度過')

        data['people_vote'] = []
        data['time'] = 'day'
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        pt = ''
        alivel = 0
        for j in data['alive']:
            print("j:", j, "j[1]:", j[1])
            pt = pt + "[" + str(alivel) + ", " + j[1] + "]\n"
            alivel += 1
            data['be_voted_by_people'].append(0)
        with open("data.json", "w") as jfile:
            json.dump(data, jfile, indent=1)
        # need to DEBUG
        await ctx.send(f'眾人開始討論並投票`+/vote <number>`\n{pt}')
        while(True):
            await asyncio.sleep(2)
            with open('data.json', 'r') as jdata:
                data = json.load(jdata)
            if len(data['people_vote']) == alivel:
                    break

        max = 0
        for i in data['people_vote']:
            data['be_voted_by_people'][i[1]] += 1
            if data['be_voted_by_people'][i[1]] > max:
                max = data['be_voted_by_people'][i[1]]
        maxlist = []
        for i in range(len(data['be_voted_by_people'])):
            if data['be_voted_by_people'][i] == max:
                maxlist.append(i)
        print("debug: people vote append")
        kill_by_people = random.choice(maxlist)
        killed_b_p_id =  data['alive'][kill_by_people][2]
        finded=False
        if finded == False:
            for i in range(len(data['Villager_list'])):
                if data['Villager_list'][i] == killed_b_p_id:
                    del data['Villager_list'][i]
                    finded = True
                    break
        if finded == False:
            for i in range(len(data['Seer_list'])):
                if data['Seer_list'][i][0] == killed_b_p_id:
                    del data['Seer_list'][i]
                    finded = True
                    break
        if finded == False:
            for i in range(len(data['Witch_list'])):
                if data['Witch_list'][i][0] == killed_b_p_id:
                    del data['Witch_list'][i]
                    finded = True
                    break
        if finded == False:
            for i in range(len(data['Werewolf_list'])):
                if data['Werewolf_list'][i] == killed_b_p_id:
                    del data['Werewolf_list'][i]
                    finded = True
                    break
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        gq=False
        bq=False
        if len(data['Villager_list']) or len(data['Seer_list']) or len(data['Witch_list']):
            gq = True
        if len(data['Werewolf_list']):
            bq = True
        
        await ctx.send(f"投票結束\n{data['alive'][kill_by_people][1]}被放逐了")
        del data['alive'][kill_by_people]
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent=1)
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        
        if gq==True and bq==False:
            await ctx.send("GAME OVER: Good Guys Win!!")
            return
        if bq==True and gq==False:
            await ctx.send("GAME OVER: Bad Guys Win!!")
            return
    


#===== ===== == 指令 == ===== =====#
@bot.command()
async def vote(ctx, ext):
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    if data['time'] == 'night':
        await ctx.send('您只能在白天時投票')
        return

    try:
        ext = int(ext)
    except:
        await ctx.send("資料錯誤")
        return
    if ext >= len(data['alive']) or ext < 0:
        await ctx.send("查無此人")

    havebeen = False
    for i in data['people_vote']:
        if i[0] == ctx.author.name:
            await ctx.send("您已投過票")
            havebeen = True
            break
    if havebeen:
        return
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    data['people_vote'].append([ctx.author.name, ext])
    await ctx.send('投票已送出')
    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent=1)






@bot.command()
async def kill(ctx, ext):
    with open('data.json','r') as jdata:
        data = json.load(jdata)
    if ctx.author.id not in data['Werewolf_list']:
        await ctx.send("您無拜訪此命令之權限")
        return
    if data['time'] == "day":
        await ctx.send("目前無法投票")
        return
    try:
        ext = int(ext)
    except:
        await ctx.send("資料錯誤")
        return
    if ext >= len(data['alive']) or ext < 0:
        await ctx.send("查無此人")
        return
    id = ctx.author.id
    for i in data['wolf_vote']:
        if i[1] == ctx.author.id:
            i[0] = ext
            await ctx.author.send("目標已變更")
            with open('data.json', 'w') as jdata:
                json.dump(data, jdata, indent =1)
            return
    data['wolf_vote'].append([ext, id])
    await ctx.author.send("目標已選定")
    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent =1)
    
@bot.command()
async def check(ctx, ext):
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    ''' ==================test test test==================
    if data['time'] == 'day':
        await ctx.send('白天無法施法')
        return
    '''
    tmp = False
    where = -1
    id = ctx.author.id
    l = len(data['Seer_list'])
    for i in range(l):
        if id == data['Seer_list'][i][0]:
            tmp = True
            print(f"debug: tmp = True\n{data['Seer_list'][i][1]}")
            where = i
            if data['Seer_list'][i][1] == False:
                await ctx.send('抱歉，您目前無此權力')
                return
            else:
                data['Seer_list'][i][1] = False
    if tmp == False:
        await ctx.send('您無拜訪此命令之權限')
        print("debug: tmp return")
        return
    try:
        ext = int(ext)
    except:
        await ctx.send(f"附加值錯誤")
        return
    if ext >= len(data['alive']) or ext < 0:
        await ctx.send("查無此人")
        return
    wantwho = data['name'][ext]
    hisid = data['alive'][ext][2]
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)

    data['seer_check'].append(1)

    with open('data.json', 'w') as jdata:
        json.dump(data, jdata, indent=1)
    if hisid in data['Werewolf_list']:
        data['Seer_list'][where][1] = False
        with open('data.json','w') as jdata:
            json.dump(data, jdata, indent=1)
        await ctx.send(f"<@{hisid}>是 '狼人'")
        return
    elif hisid in data['Villager_list']:
        data['Seer_list'][where][1] = False
        with open('data.json','w') as jdata:
            json.dump(data, jdata, indent=1)
        await ctx.send(f"<@{hisid}>是 '好人'")
    tof = False
    for i in data['Seer_list']:
        if hisid == data['Seer_list'][0]:
            tof = True
            break
    if tof:
        data['Seer_list'][where][1] = False
        with open('data.json','w') as jdata:
            json.dump(data, jdata, indent=1)
        await ctx.send(f"<@{wantwho}>是 '好人'")
        return
    for i in data['Witch_list']:
        if hisid == i[0]:
            tof = True
            break
    if tof:
        data['Seer_list'][where][1] = False
        with open('data.json','w') as jdata:
            json.dump(data, jdata, indent=1)
        await ctx.send(f"<@{wantwho}>是 '好人'")
        return
    await ctx.send("我不知道，請洽開發者")

@bot.command()
async def witch(ctx, ext):
    print(f"debug: ext = {ext}")
    id = ctx.author.id
    where = -1
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    ''' ==================test test test==================
    if data['time'] == 'day':
        await ctx.send('白天無法施法')
        return
    for i in range(len(data['Witch_list'])):
        if id == data['witch_list'][i][0]:
            where = i
            
    if where == -1:
        await ctx.send('您無拜訪此命令之權限')
        return
    '''
        
    if ext == 'Y' or ext == 'y':
        if data['Witch_list'][where][3] == False:
            await ctx.send('抱歉，您目前無此權力')
            return
        data['witch_help'].append(True)
        data['Witch_list'][where][2] = 0
        data['Witch_list'][where][3] = False
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        await ctx.send("您救了他")

    elif ext == 'N' or ext == 'n':
        if data['Witch_list'][where][3] == False:
            await ctx.send('抱歉，您目前無此權力')
            return
        data['witch_help'].append(False)
        data['Witch_list'][where][3] = False
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        await ctx.send("可憐的孩子.....孤兒")
    
    else: # 毒藥
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        id = ctx.author.id
        for i in data['witch_poison']:
            if i == id:
                await ctx.send("抱歉，您目前無此權力")
                print('witch error return')
                return #error
        try:
            ext = int(ext)
        except:
            await ctx.send("附加值錯誤")
            print('witch error return')
            return #error
        if ext >= len(data['alive']) or ext < -1:
            await ctx.send("查無此人")
            print('witch error return')
            return #error
#does not work
        data['witch_poison'].append(ctx.author.id)
        if ext == -1:
            await ctx.send("今晚您將不下毒")
            with open('data.json', 'w') as jdata:
                json.dump(data, jdata, indent=1)
            return #done
        
        with open('data.json', 'r') as jdata:
            data = json.load(jdata)
        wkill = data['alive'][ext][1]
        for i in data['killed']:
            if i[0] == wkill:
                await ctx.send("目標已被鎖定")
                return #error
        data['Witch_list'][where][1] = 0
        for i in range(len(data['name'])):
            if data['name'][i] == wkill:
                wkill = data['id'][i]
                break
        with open("data.json", "r") as jdata:
            data = json.load(jdata)
        data['killed'].append([wkill, '女巫'])
        print(f"debug: killed append {wkill}")
        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent =1)
        print(f"debug: succesfully??")
        await ctx.send(f"您殺了 <@{wkill}>")

@bot.command()
async def Discuss(ctx):
    print('Discuss')
    with open('data.json', 'r') as jdata:
        data = json.load(jdata)
    if ctx.author.id not in data['Werewolf_list']:
        await ctx.send("您不是狼人，沒有在夜晚溝通的權利")
    else:
        if len(data['Werewolf_list']) == 0:
            await ctx.send("沒有說話對象")
        else:
            cont = ctx.message.content
    for i in data['Werewolf_list']:
        x = bot.get_user(i)
        await x.send(f"公告: \n  {ctx.author.name} says: {cont[9:]}")


# GROUP
bot.remove_command("help")
@bot.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Commands helper", description = "use `help <subject>` to get more help", color = random.randint(0, 16777216))
    em.add_field(name = "Setting", value = "set", inline = True)
    em.add_field(name = "Game_start", value = "play\ndel_p\nstart", inline = True)
    em.add_field(name = "For_Witch", value = "witch", inline = True)
    em.add_field(name = "For_Seer", value = "check", inline = True)
    em.add_field(name = "For_Werewolf", value = "kill", inline = True)
    em.add_field(name = "Vote", value = "vote", inline = True)
    await ctx.send(embed = em)

@help.command()
async def Setting(ctx):
    em = discord.Embed(title="Setting", description="use `set <role_name> <num>` to set the number of role", color = random.randint(0, 16777216))
    em.add_field(name = "Villager", value="Set number of villager", inline=False)
    em.add_field(name = "Seer", value="Set number of seer", inline=False)
    em.add_field(name = "Witch", value="Set number of witch", inline=False)
    em.add_field(name = "Werewolf", value="Set number of werewolf", inline=False)
    await ctx.send(embed = em)

@help.command()
async def Game_start(ctx):
    em = discord.Embed(title="Game_start")
    em.add_field(name = "play", value = "use `play` to  join the game", inline=False)
    em.add_field(name = "del_p", value = "use `del_p` to leave the game", inline=False)
    em.add_field(name = "start", value = "use `start` to start the game", inline=False)
    await ctx.send(embed = em)

@help.command()
async def For_Witch(ctx):
    em = discord.Embed(title="For Witch", description = "use `witch <cmd>` to make a choice")
    em.add_field(name = "witch <Y/N>", value = "to choose weather you want to save the person killed", inline=False)
    em.add_field(name = "witch <num>", value = "to pick one you do not trust and kill him or her", inline=False)
    await ctx.send(embed = em)

@help.command()
async def For_Seer(ctx):
    em = discord.Embed(title="For Seer", description="use `check` command to check weather the doubt person is a werewolf")
    await ctx.send(embed = em)

@help.command()
async def For_Werewolf(ctx):
    em = discord.Embed(title="For Werewolf", description="use `kill` command to kill the person")
    await ctx.send(embed = em)

@help.command()
async def rule(ctx):
    em = discord.Embed(title="Rule", description="use `rule <cmd>` to get more help")
    em.add_field(name = "Start", value = "First, you need to set the number of roles. Contents the following:\nWitch   Seer   Villager   Werewolf.")
    em.add_field(name = "Role Desciption", value="")
    
    
bot.run(setting['TOKEN'])
import discord
from discord.ext import commands
import requests
import math
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import random
from time import sleep
import asyncio


from discord.utils import get

참여자id=[]
참여자name=[]
참명={}
마리=[]
의리=[]
경리=[]
시리=[]
선시리=[]
살명단=[]
죽명단=[]
검명단=[]
투명단=[]
직업=[960113218544615454,960113482357964812,960113543770931220,960113576012550214]
n=[0]


투자자={}
증권=["쟈졌마트", "삼진제약"]
쟈졌마트={}
삼진제약={}

d쟈졌증권=0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("A")

    print('{} logged in.'.format(client))
    print('Bot: {}'.format(client.user))
    print('Bot name: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    쟈졌마트["시가"]=100
    쟈졌마트["초기시가"]=100
    삼진제약["시가"]=1000
    삼진제약["초기시가"]=1000
    while True:        
        for i in 증권:
            plus=random.randint(0, 101)
            mius=random.randint(-66,-1)
            pm=random.randint(0,1)
            if pm==0:
                eval(i)["증가량"]=plus
            else:
                eval(i)["증가량"]=mius
                if (eval(i)["초기시가"]/100)*80<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*90:
                    mius=random.randint(-46,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*70<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*80:
                    mius=random.randint(-42,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*60<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*70:
                    mius=random.randint(-38,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*50<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*60:
                    mius=random.randint(-34,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*40<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*50:
                    mius=random.randint(-30,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*40<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*50:
                    mius=random.randint(-26,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*30<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*40:
                    mius=random.randint(-22,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*20<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*30:
                    mius=random.randint(-18,-1)
                    eval(i)["증가량"]=mius
                elif (eval(i)["초기시가"]/100)*10<eval(i)["시가"]<=(eval(i)["초기시가"]/100)*20:
                    mius=random.randint(-15,-1)
                    eval(i)["증가량"]=mius
                elif eval(i)["시가"]<eval(i)["초기시가"]/100:
                    eval(i)["증가량"]=plus

            eval(i)["시가"]=eval(i)["시가"]*(1+(eval(i)["증가량"]/100))
            
            for x in 투자자:
                for a in range(2, len(투자자[x])):
                    try:
                        투자자[x][a][i]
                        투자자[x][a][i][0]=투자자[x][a][i][1]*eval(i)["시가"]
                    except KeyError:
                        pass

        await asyncio.sleep(5)


        
    

    



@client.event
async def on_message(message):





    if message.content.startswith("/주식등록"):
        확인리스트=[]
        for i in 투자자:
            확인리스트.append(i)
        if 확인리스트.count(message.author.id)==True:
            embed = discord.Embed(title="이미 등록된 투자가입니다.", description="", color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            투자자[message.author.id]=[message.author.name, 10000]
            for i in 증권:        
                투자자[message.author.id].append({i:[0,0]})     
            embed = discord.Embed(title="투자가 목록에 등록되었습니다.", description="/주식도움말 명령어를 사용해보세요.", color=0x00FF00)
            await message.channel.send(embed=embed)

    if message.content.startswith("/주식도움말"):
        embed = discord.Embed(title="주식 시스템 관련 명령어 사용법", description="", color=0x62c1cc)
        embed.add_field(name="/내주식", value="내가 보유하고 있는 주식을 볼 수 있습니다." , inline=False)
        embed.add_field(name="/주식현황", value="현재 모든 주식의 시가, 증가률을 불러옵니다." , inline=False)
        embed.add_field(name="/구매 (주식이름) (수량)", value="/구매 명령어를 사용해서 주식을 매수합니다." , inline=False)
        embed.add_field(name="/판매 (주식이름) (수량)", value="/판매 명령어를 사용해서 주식을 매수합니다." , inline=False)
        
        
        await message.channel.send(embed=embed)

        

    if message.content.startswith("/구매"):
        
        선택증권 = message.content[4:8]
        수량 = message.content[9:]
        확인리스트=[]
        for i in 투자자:
            확인리스트.append(i)
        if 확인리스트.count(message.author.id)!=True:
            embed = discord.Embed(title="/주식등록 명령어를 이용해서 주식을 시작하세요.", description="등록되지 않은 투자가입니다.", color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            if 선택증권== "":
                embed = discord.Embed(title="옳바른 명령어를 입력해주십시오.", description="", color=0xFF0000)
                embed.set_footer(text="/구매 (주식이름) (수량)")
                await message.channel.send(embed=embed)               
            elif 수량 == "":
                embed = discord.Embed(title="옳바른 명령어를 입력해주십시오.", description="", color=0xFF0000)
                embed.set_footer(text="/구매 (주식이름) (수량)")
                await message.channel.send(embed=embed)
            else:
                수량=float(수량)
                try:
                    수량= int(수량)
                    if 수량<=0:
                        embed = discord.Embed(title="수량은 자연수만 가능합니다.", description="", color=0xFF0000)
                        await message.channel.send(embed=embed)
                    elif 증권.count(선택증권)!=True:
                        

                        embed = discord.Embed(title=선택증권+"은/는 존재하지 않는 주식입니다.", description="", color=0xFF0000)               
                        await message.channel.send(embed=embed)
                    투자자[message.author.id][1]-= 수량*(eval(선택증권)['시가'])

                    for i in range(2, len(투자자[message.author.id])):
                        try:
                            투자자[message.author.id][i][선택증권]
                            투자자[message.author.id][i][선택증권][1]+=수량
                            if 투자자[message.author.id][1] <0:
                                투자자[message.author.id][i][선택증권]
                                투자자[message.author.id][1]+= 수량*(eval(선택증권)['시가'])
                                투자자[message.author.id][i][선택증권][1]-=수량                    
                                embed = discord.Embed(title="돈이 부족합니다!", description="", color=0xFF0000)
                                embed.set_footer(text="현재 " + str(math.floor(투자자[message.author.id][1]))+ "원을 가지고 있습니다.")
                                await message.channel.send(embed=embed)
                            else:
                                embed = discord.Embed(title=선택증권+"을/를 "+ str(수량)+ "개 구매했습니다.", description="", color=0x00FF00)
                                embed.add_field(name="자산", value=str(math.floor(투자자[message.author.id][1]))+"원", inline=True)
                                for i in range(2, len(투자자[message.author.id])):
                                    try:
                                        투자자[message.author.id][i][선택증권]                
                                        embed.add_field(name="구매 갯수", value=str(math.floor(투자자[message.author.id][i][선택증권][1]))+ "개", inline=True)
                                    except KeyError:
                                        pass     
                    
                                await message.channel.send(embed=embed)
                                    
                        except KeyError:
                            pass  
                except:
                    embed = discord.Embed(title="수량은 자연수만 가능합니다.", description="", color=0xFF0000)
                    await message.channel.send(embed=embed)

                    



                


    if message.content.startswith("/판매"):
        선택증권 = message.content[4:8]
        수량 = message.content[9:]
        확인리스트=[]
        for i in 투자자:                    
                확인리스트.append(i)
        if 확인리스트.count(message.author.id)!=True:
            embed = discord.Embed(title="/주식등록 명령어를 이용해서 주식을 시작하세요.", description="등록되지 않은 투자가입니다.", color=0xFF0000)
            await message.channel.send(embed=embed)
        else:            
            if 선택증권== "":
                embed = discord.Embed(title="옳바른 명령어를 입력해주십시오.", description="", color=0xFF0000)
                embed.set_footer(text="/판매 (주식이름) (수량)")
                await message.channel.send(embed=embed)
            elif 수량 == "":
                embed = discord.Embed(title="옳바른 명령어를 입력해주십시오.", description="", color=0xFF0000)
                embed.set_footer(text="/구매 (주식이름) (수량)")
                await message.channel.send(embed=embed)

            else:
                try:
                    int(수량)
                    if 수량<=0:
                        embed = discord.Embed(title="수량은 자연수만 가능합니다.", description="", color=0xFF0000)
                        await message.channel.send(embed=embed)
                    elif 증권.count(선택증권)!=True:                  
                        embed = discord.Embed(title=선택증권+"은/는 존재하지 않는 주식입니다.", description="", color=0xFF0000)               
                        await message.channel.send(embed=embed)
                    try:
                        투자자[message.author.id][1]+= 수량*(eval(선택증권)['시가'])
                        for i in range(2, len(투자자[message.author.id])):
                            투자자[message.author.id][i][선택증권]                
                            투자자[message.author.id][i][선택증권][1]-=수량
                            if 투자자[message.author.id][i][선택증권][1]<0:
                                투자자[message.author.id][i][선택증권][1]+=수량
                                투자자[message.author.id][1]-= 수량*(eval(선택증권)['시가'])
                                embed = discord.Embed(title="갯수가 부족합니다!", description="", color=0xFF0000)
                                embed.set_footer(text="현재 " + 선택증권 + "은/는 " + str(투자자[message.author.id][2][선택증권][1])+ "개를 가지고 있습니다.")
                                await message.channel.send(embed=embed)
                            else:
                                embed = discord.Embed(title=선택증권+"을/를 "+ str(수량)+ "개 팔았습니다.", description="", color=0x00FF00)
                                embed.add_field(name="자산", value=str(math.floor(투자자[message.author.id][1]))+"원", inline=True)
                                embed.add_field(name=선택증권, value="수량 : " + str(math.floor(투자자[message.author.id][i][선택증권][1]))+ "개", inline=True)

                                        
                                await message.channel.send(embed=embed)                                
                    except KeyError:
                        pass

                except:
                    embed = discord.Embed(title="수량은 자연수만 가능합니다.", description="", color=0xFF0000)
                    await message.channel.send(embed=embed)

      
   


    if message.content.startswith("/내주식"):
        try:
            embed = discord.Embed(title=message.author.name + "님의 정보", description="", color=0x62c1cc)
            embed.add_field(name="자산", value=str(math.floor(투자자[message.author.id][1]))+"원", inline=True)
            for l in 증권:
                for i in range(2, len(투자자[message.author.id])):
                    try:
                        투자자[message.author.id][i][l]                
                        embed.add_field(name=l, value=str(math.floor(투자자[message.author.id][i][l][0]))+"원"+"(수량 : " + str(math.floor(투자자[message.author.id][i][l][1]))+ "개)", inline=True)
                    except KeyError:
                        pass     
            embed.set_footer(text="내가 산 주식의 자산은 갱신까지 최대 5초가 걸릴 수 있습니다.")
            await message.channel.send(embed=embed)
        except KeyError:
            embed = discord.Embed(title="/주식등록 명령어를 이용해서 주식을 시작하세요.", description="등록되지 않은 투자가입니다.", color=0xFF0000)
            await message.channel.send(embed=embed)
        



    if message.content.startswith("/주식현황"):
        embed = discord.Embed(title="주식정보", description="", color=0xF7FF39)
        for i in 증권:    
            if eval(i)['증가량']<0:
                화살표="▼"
            elif eval(i)['증가량']==0:
                화살표="="
            elif eval(i)['증가량']>0:
                화살표="▲"                       
            embed.add_field(name=i, value=str(math.floor(eval(i)['시가']))+"원" +"("+ 화살표 +str(eval(i)["증가량"])+ "%)" , inline=True)
            embed.set_footer(text="주식 시가는 5초마다 갱신됩니다.")
        c=await message.channel.send(embed=embed)
        while True:
            await asyncio.sleep(3)
            
            changedembed = discord.Embed(title="증권정보", description="", color=0xF7FF39)
            for i in 증권:    
                if eval(i)['증가량']<0:
                    화살표="▼"
                elif eval(i)['증가량']==0:
                    화살표="="
                elif eval(i)['증가량']>0:
                    화살표="▲"                       
                changedembed.add_field(name=i, value=str(math.floor(eval(i)['시가']))+"원" +"("+ 화살표 +str(eval(i)["증가량"])+ "%)" , inline=True)
                changedembed.set_footer(text="주식 시가는 5초마다 갱신됩니다.")
            await c.edit(embed=changedembed)     




    if message.content.startswith("/maple"):
        name = message.content[7:]
        embedname = name
        name = parse.quote(name)
        mapleurl = urlopen('https://maple.gg/u/' + str(name))
        searchurl = urlopen('https://maple.gg/search?q=' + str(name))
        mapleserverurl = urlopen('https://maplestory.nexon.com/Ranking/World/Total?c=' + str(name)+'&w=0')



        soup = BeautifulSoup(mapleurl, 'html.parser')
        soup1 = BeautifulSoup(searchurl, 'html.parser')
        soup2 = BeautifulSoup(mapleserverurl, 'html.parser')
        try:
            server= soup2.select("#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk")[0].find_all('a')
            for tag in server:
                serverurl =tag['href']


            rserverurl = urlopen('https://maplestory.nexon.com' + str(serverurl))
            go = BeautifulSoup(rserverurl, 'html.parser')
            for anchorg in go.select("#wrap > div.center_wrap > div.char_info_top > div.char_info > dl:nth-child(3) > dd"):
                maple_서버 =  str(anchorg.get_text())
            for anchorg in soup.select("#user-profile > section > div.row.row-normal > div.col-lg-8 > div.row.row-normal.user-additional > div.col-lg-2.col-md-4.col-sm-4.col-12.mt-3 > a.text-yellow"):
                maple_길드 =  str(anchorg.get_text())

            for anchore in soup.select("#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(1)"):
                maple_경험치 = str(anchore.get_text())
            for anchorj in soup.select("#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(2)"):
                maple_직업 =  str(anchorj.get_text())
            for anchorm in soup.select("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > h1.user-summary-floor"):
                anchorm = anchorm.get_text()
                anchorm = anchorm.replace(" ", "")
                anchorm = anchorm.replace("층", "")
                anchorm = anchorm.strip()

                maple_무릉 =  anchorm + "층"

            for anchormt in soup.select("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > small.user-summary-duration"):
                maple_무릉시간 = ""
                maple_무릉시간 =  str(anchormt.get_text())
                

            for anchormt in soup.select("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span"):
                
                maple_유니온 =  str(anchormt.get_text())

            img= go.select("#wrap > div.center_wrap > div.char_info_top > div.char_info > dl:nth-child(3) > dd")[0].find_all('img')
            for tag in img:
                서버_아이콘 =tag['src']
            img= soup.select("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div")[0].find_all('img')
            for tag in img:
                유니온_아이콘 =tag['src']



            embed = discord.Embed(title=embedname + "님의 정보", description="", color=0x62c1cc, url='https://maple.gg/u/%s'%embedname) 
            embed.add_field(name="직업", value=maple_직업, inline=True)
            embed.add_field(name="서버", value=maple_서버, inline=True)
            embed.set_thumbnail(url=서버_아이콘)
            embed.set_image(url=유니온_아이콘)
            embed.add_field(name="경험치", value=maple_경험치, inline=True)
            try:
                embed.add_field(name="길드", value=maple_길드, inline=False)
            except UnboundLocalError:
                embed.add_field(name="길드", value="없음", inline=False)
            try:
                embed.add_field(name="무릉", value=maple_무릉, inline=False)
            except UnboundLocalError:
                embed.add_field(name="무릉", value="없음", inline=False)
            try:
                embed.add_field(name="무릉", value=maple_무릉시간, inline=False)
            except UnboundLocalError:
                embed.add_field(name="무릉시간", value="없음", inline=False)
            try:
                embed.add_field(name="유니온", value=maple_유니온, inline=False)
            except UnboundLocalError:
                embed.add_field(name="유니온", value="없음", inline=False)


        except IndexError:
            embed = discord.Embed(title= embedname + "님 캐릭터를 찾을 수 없습니다", description="", color=0x62c1cc)

        await message.channel.send(embed=embed)

    if message.content.startswith("/마피아"):
        리스트 = [참여자id,참여자name,참명,마리,의리,경리,시리,선시리,살명단,죽명단,검명단,투명단]
        for i in 리스트:
            while i:
                try:
                    i.pop()
                except:
                    pass
        시작스위치=0
        n=5
        광장 = client.get_channel(1005757949957910569)
        마피아방 = client.get_channel(1005757740238508052)
        시작방 = client.get_channel(1005758067268403210)
        경찰방 = client.get_channel(1005757903556325446)
        embed = discord.Embed(title="마피아 게임 ", description="참여인원은 체크이모티콘 클릭", color=0x58FAF4)
        embed.set_footer(text="20초안에 눌러주세요")
        start = await 시작방.send(embed=embed)
        await start.add_reaction('☑')
        sleep(14)
        await start.delete()
        참여자명수=len(참여자id)
        if len(참여자id)<=4:
            embed = discord.Embed(title="참여인원이 부족합니다", description="5명 이상부터 시작가능합니다", color=0x58FAF4)
            await 시작방.send(embed=embed)
        else:
            while 시작스위치==0:
                if n<=참여자명수 and 참여자명수<n+5:
                    시작스위치 = 1
                else:
                    n=n+5
#----------역할분배-----------------------------------------------

            embed = discord.Embed(title="마피아 게임", description="규칙", color=0xFF00FF)
            embed.add_field(name="1.", value="죽일 명단, 살릴 명단, 조사할 명단에는 각 member nickname과 member id가 적혀있습니다.", inline=False)
            embed.add_field(name="1-1.", value="죽일 명단, 살릴 명단, 조사할 명단은 /죽명단, /살명단, /경명단으로 호출 할 수 있습니다.", inline=False)
            embed.add_field(name="1-2.", value="죽일, 살릴, 조사 명단에서 죽일, 살릴, 조사할 사람을 정하셨으면 ", inline=False)
            embed.add_field(name="1-3.", value="그에 맞는 명령어는 /킬 (id), /힐 (id), /조사 (id) 입니다.", inline=False)
            embed.add_field(name="2.", value="시민 투표시 지목된 사람은 1번만 변경시킬 수 있습니다. 신중하게 투표해주세요", inline=False)
            embed.add_field(name="2-2.", value="시민 투표명령어는 /투표 입니다.", inline=False)
            embed.add_field(name="3.", value="밤은 20초, 낮은 약 2분입니다.", inline=False)
            embed.add_field(name="4.", value="```"+"게임 흐름과 관계없는 명령어는 제발 사용하지말아주세요. 에러 발생의 원인입니다."+"```", inline=False)
            embed.add_field(name="4.", value="```"+"띄어쓰기 제발 주의해주세요. 에러 발생의 원인입니다. \n ex) 없는 띄어쓰기 넣기, 넣어야 하는 띄어쓰기 삭제"+"```", inline=False)
            embed.set_footer(text="고임#4174")
            await message.channel.send(embed=embed)
            마피아명수 = n/5
            경찰명수 = (n/5)*2
            의사명수 = (n/5)*2
            시민명수 = int(참여자명수)-int(마피아명수)-int(경찰명수)-int(의사명수)
            print(마피아명수)
            print(경찰명수)
            print(의사명수)
            print(시민명수)


            while 마피아명수!= 0:

                선택=random.choice(참여자id)
                마리.append(선택)
                참여자id.remove(선택)
                마피아명수 = 마피아명수-1
            while 경찰명수!=0:
                선택=random.choice(참여자id)
                경리.append(선택)
                참여자id.remove(선택)
                경찰명수 = 경찰명수-1
            while 의사명수!=0:
                선택=random.choice(참여자id)
                의리.append(선택)
                참여자id.remove(선택)
                의사명수 = 의사명수-1
            while 시민명수!=0:
                선택=random.choice(참여자id)
                시리.append(선택)
                참여자id.remove(선택)
                시민명수 = 시민명수-1
            print(시리)
            print(마리)
            print(경리)
            print(의리)
            


            
            for i in range(0, int(len(마리))):
                선택id=마리[i]
                user =discord.utils.get(message.guild.members, id=선택id)
                role = discord.utils.get(message.guild.roles, id = 960113218544615454)
                await user.add_roles(role)
                
                await user.add_roles(role)
            for i in range(0, int(len(경리))):
                선택id=경리[i]
                선시리.append(선택id)
#----------------------------!!-------------
                user =discord.utils.get(message.guild.members, id=선택id)
                role = discord.utils.get(message.guild.roles, id = 960113543770931220)
                await user.add_roles(role)
#----------------------------!!-------------
            for i in range(0, int(len(의리))):
                선택id=의리[i]
                선시리.append(선택id)
                user =discord.utils.get(message.guild.members, id=선택id)
                role = discord.utils.get(message.guild.roles, id = 960113482357964812)
                await user.add_roles(role)
            for i in range(0, int(len(시리))):
                if i==0:
                    pass
                else:
                    선택id=시리[i]
                    선시리.append(선택id)
                    user =discord.utils.get(message.guild.members, id=선택id)
                    role = discord.utils.get(message.guild.roles, id = 960113576012550214)
                    await user.add_roles(role)

#-----------------------------------------------------
            while True:
                if len(마리)==0:
                    embed = discord.Embed(title="마피아 게임 ", description="게임이 끝났습니다.", color=0x58FAF4)
                    embed.add_field(name="결과는...", value="마피아가 승리하였습니다.")
                    embed.set_footer(text="수고하셨습니다.")
                    await 광장.send(embed=embed)
                    await asyncio.sleep(30)
                    await embed.delete()
                    for i in 참여자id:
                        for e in 직업:
                            user = discord.utils.get(message.guild.members, id=i)
                            role = discord.utils.get(message.guild.roles, id = e)
                            await user.remove_roles(role)
                    break
                else:
                    if len(선시리)==0:
                        embed = discord.Embed(title="마피아 게임 ", description="게임이 끝났습니다.", color=0x58FAF4)
                        embed.add_field(name="결과는...", value="시민이 승리하였습니다.")
                        embed.set_footer(text="수고하셨습니다.")
                        await 광장.send(embed=embed)
                        await asyncio.sleep(30)
                        await embed.delete()                      
                        for i in 참여자id:
                            for e in 직업:
                                user = discord.utils.get(message.guild.members, id=i)
                                role = discord.utils.get(message.guild.roles, id = e)
                                await user.remove_roles(role)
                        break
                    else:
                    
                        embed = discord.Embed(title="마피아 게임 ", description="지금은 밤 입니다.", color=0x58FAF4)
                        embed.set_footer(text="밤은 45초 입니다.")
                        await 광장.send(embed=embed)
                        await asyncio.sleep(45)
                        print(검명단)
                        print(살명단)
                        print(죽명단)


            #----------경찰 조사 결과------------------------
                        결과=""
                        for i in 마리:
                            if 검명단[0]==i:
                                결과="마피아입니다."
                            else:
                                결과="마피아가 아닙니다."
                        embed = discord.Embed(title="마피아 게임 ", description="조사결과 입니다.", color=0x58FAF4)
                        embed.add_field(name=참명[검명단[0]]+"님은...", value=결과)
                        await 경찰방.send(embed=embed)

            #----------의사 결과------------------------------
                        결과=""
                        for i in 죽명단:
                            if 살명단[0]==i:
                                죽명단.pop()
                                결과="의사의 캐리로 아무도 죽지 않았습니다."
                            else:
                                결과=참명[죽명단[0]]

            #-----------마피아 결과----------------
                                user =discord.utils.get(message.guild.members, id=죽명단[0])
                                for i in 직업:
                                    try:
                                        role = discord.utils.get(message.guild.roles, id = i)
                                        await user.remove_roles(role)
                                        선시리.remove(죽명단[0])
                                    except AttributeError:
                                        pass
                        embed = discord.Embed(title="마피아 게임 ", description="낮이 밝았습니다.", color=0x58FAF4)
                        
                        
                        embed.add_field(name="이번에 죽은사람", value=결과)
                        try:
                            죽명단.pop()
                        except IndexError:
                            pass
            #----------------------------------------
                        embed.set_footer(text="투표까지 2분입니다.")
                        투표 = await 광장.send(embed=embed)
                        await asyncio.sleep(120)
                        await 투표.delete()
                        embed = discord.Embed(title="마피아 게임 ", description="누구를 죽이시겠습니까?", color=0x58FAF4)
                        random.shuffle(선시리)
                        random.shuffle(마리)
                        경=선시리+마리
                        for i in range(0,len(경)):
                            embed.add_field(name=경[i], value=참명[경[i]], inline=False)
                        embed.set_footer(text="투표할 사람은 바꿀 수 없습니다. 투표시간은 15초 입니다. 명령어는 /v (id)")
                        투표 = await 광장.send(embed=embed)
                        await asyncio.sleep(15)
                        await 투표.delete()
                        embed = discord.Embed(title="마피아 게임 ", description="투표결과", color=0x58FAF4)
                        embed.add_field(name="투표로 죽은 사람은...", value=참명[투명단[0]], inline=False)
                        await 광장.send(embed=embed)
                        try:
                            선시리.remove(투명단[0])
                        except:
                            pass
                        user =discord.utils.get(message.guild.members, id=투명단.pop())
                        for i in 직업:
                            try:
                                role = discord.utils.get(message.guild.roles, name = i)
                                await user.remove_roles(role)
                            except AttributeError:
                                pass




#-----------마피아-----------------------
    if message.content.startswith("/킬명단"):
        random.shuffle(선시리)
        선량한시민=len(참여자id)-len(마리)
        embed = discord.Embed(title="마피아 게임 ", description="죽일 사람 명단입니다.", color=0x58FAF4)
        for i in range(0,len(선시리)):
            embed.add_field(name=선시리[i], value=참명[선시리[i]], inline=False)
        embed.set_footer(text="죽일 사람은 중간에 바꿀 수 있습니다. 명령어는 /k (id)")
        마피아방 = client.get_channel(1005757740238508052)
        await 마피아방.send(embed=embed)
#        await asyncio.sleep(20)
#        await embed.delete()
        
    
    if message.content.startswith("/k"):
        마피아방 = client.get_channel(1005757740238508052)
        if len(죽명단)==0:
            id = int(message.content[3:])
            죽명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-살인.", color=0x58FAF4)
            embed.add_field(name="죽일 사람은...", value=참명[id])
            됨 = await 마피아방.send(embed=embed)
            sleep(4)
            await 됨.delete()
        else:
            죽명단.pop()
            id = message.content[3:]
            죽명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-살인.", color=0x58FAF4)
            embed.add_field(name="죽일 사람은...", value=참명[id])
            됨 = await 마피아방.send(embed=embed)
            sleep(4)
            await 됨.delete()

#----------의사------------------------
    if message.content.startswith("/힐명단"):
        의사방=client.get_channel(1005757856399761419)
        random.shuffle(선시리)
        random.shuffle(마리)
        힐=선시리+마리
        embed = discord.Embed(title="마피아 게임 ", description="살릴 사람 명단입니다.", color=0x58FAF4)
        for i in range(0,len(힐)):
            embed.add_field(name=힐[i], value=참명[힐[i]], inline=False)
        embed.set_footer(text="살릴 사람은 중간에 바꿀 수 있습니다. 명령어는 /h (id)")
        await 의사방.send(embed=embed)
#        await asyncio.sleep(20)
#        await embed.delete()
    if message.content.startswith("/h"):
        의사방=client.get_channel(1005757856399761419)
        if len(살명단)==0:
            id = int(message.content[3:])
            살명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-치료.", color=0x58FAF4)
            embed.add_field(name="치료할 사람은...", value=참명[id])
            됨 = await 의사방.send(embed=embed)
            sleep(4)
            await 됨.delete()
        else:
            살명단.pop()
            id = int(message.content[3:])
            살명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-치료.", color=0x58FAF4)
            embed.add_field(name="치료할 사람은...", value=참명[id])
            됨 = await 의사방.send(embed=embed)
            sleep(4)
            await 됨.delete()
#----------경찰---------------------------
    if message.content.startswith("/경명단"):
        경찰방 = client.get_channel(1005757903556325446)
        random.shuffle(선시리)
        random.shuffle(마리)
        경=선시리+마리
        embed = discord.Embed(title="마피아 게임 ", description="조사할 사람 명단입니다.", color=0x58FAF4)
        for i in range(0,len(경)):
            embed.add_field(name=경[i], value=참명[경[i]], inline=False)
        embed.set_footer(text="조사할 사람은 중간에 바꿀 수 있습니다. 명령어는 /j (id)")
        await 경찰방.send(embed=embed)
#        await asyncio.sleep(20)
#        await embed.delete()
    if message.content.startswith("/j"):
        경찰방 = client.get_channel(1005757903556325446)
        if len(검명단)==0:
            id = int(message.content[3:])
            검명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-조사.", color=0x58FAF4)
            embed.add_field(name="조사할 사람은...", value=참명[id])
            됨 = await 경찰방.send(embed=embed)
            sleep(4)
            await 됨.delete()
        else:
            검명단.pop()
            id = int(message.content[3:])
            검명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="-조사.", color=0x58FAF4)
            embed.add_field(name="조사할 사람은...", value=참명[id])
            됨 = await 경찰방.send(embed=embed)
            sleep(4)
            await 됨.delete()



    if message.content.startswith("/v"):
        광장 = client.get_channel(1005757949957910569)
        if len(투명단)==0:
            id = int(message.content[3:])
            투명단.append(id)
            embed = discord.Embed(title="마피아 게임 ", description="투표가 끝났습니다.", color=0x58FAF4)
            embed.add_field(name="투표로 지목된 사람은...", value=참명[id])
            embed.set_footer(text="투표시간은 투표 완료 관계없이 15초입니다. 기다려주세요")
            
            됨 = await 광장.send(embed=embed)
            sleep(4)
            await 됨.delete()
        else:
            pass








@client.event
async def on_reaction_add(reaction, user):

    if user.bot == 1: #봇이면 패스
        return None
    if reaction.emoji == "☑":
        참여자id.append(user.id)
        참여자name.append(user.name)
        참명[user.id]=user.name
        print(참명)


client.run("OTkxNjc0MjA5MTgyOTQ1Mjgw.GIebfi.OrtRGRMBi17UwLjRlR8U0Zqq_bhVB_-HhaEeKQ")

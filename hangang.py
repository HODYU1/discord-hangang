@bot.slash_command(name="한강",description="서울 한강 수온을 알려줍니다")
async def 한강(interaction:nextcord.Interaction):
    await interaction.response.defer()
    han=requests.get("https://api.hangang.msub.kr/").json()
    temp=han["temp"]

    with open("config/bot_option_list.json","r",encoding="UTF-8") as f:data=json.load(f)

    wisenum=random.randint(1,50)

    embed=nextcord.Embed(title=f"🏞 현재 한강 수온은 **{temp}℃** 입니다")
    await interaction.followup.send(embed=embed)

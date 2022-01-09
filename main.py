#Import Discord Package
import discord


#Client (our bot)
client = discord.Client()

@client.event
async def on_message(message):

    if message.content.lower()=='what is the version':
        await message.channel.send('1.0')



    elif message.content.lower()=='_creator':
        await message.channel.send('Kiryu Sento')



    elif message.content.lower()=='deku':
        await message.channel.send('Detroit Smash')



    elif message.content.lower()=='who is udit':
        await message.channel.send('udit is a nub coder')


    elif message.content.lower()=='who is sharingan memes':
        await message.channel.send('sharingan memes is a kiruku thailee who posts unfunny memes')

    elif message.content.lower()=='who is loldeadmeme_xd':
        await message.channel.send('loldeadmemexd is a dankster who posts funny memes')

    elif message.content.lower()== '_what is the version':
        
        
        myEmbed = discord.Embed(title="Current version",description="The bot is in version 1.0",color=0x00ff00)
        myEmbed.add_field(name="Version Code:",value="v1.0.0",inline=False)
        myEmbed.add_field(name="Date Released:",value="Still Unknown",inline=False)
        myEmbed.set_footer(text="Don't Call Me Emergency Food anymore😡")
        myEmbed.set_author(name="Paimon")

        await message.channel.send(embed=myEmbed)

    elif message.content.lower()== '_info':
        
        
        myEmbed = discord.Embed(title="Name",description="Paimon",color=0x206694)
        myEmbed.add_field(name="Age:",value="Unknown",inline=False)
        myEmbed.add_field(name="Living in",value="Teyvat",inline=False)
        myEmbed.set_footer(text="Hi I am Paimon I am ur friend UwU")
        myEmbed.set_author(name="Information About Me")

        await message.channel.send(embed=myEmbed)

    elif message.content.lower()== 'who is naruto uzumaki':
        await message.channel.send('Naruto Uzumaki is a fictional character in the manga and anime franchise Naruto, created by Masashi Kishimoto. Serving as the eponymous protagonist of the series, he is a young ninja from the fictional village of Konohagakure')

    elif message.content.lower()=='who is sasuke uchiha':
        await message.channel.send('Sasuke Uchiha is a fictional character in the Naruto manga and anime franchise created by Masashi Kishimoto. Sasuke belongs to the Uchiha clan, a notorious ninja family, and one of the most powerful, allied with Konohagakure')

    elif message.content.lower()=='who is sakura haruno':
        await message.channel.send('Sakura Haruno is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. Sakura is depicted as a kunoichi affiliated with Konohagakure and a part of Team 7, which consists of herself, Naruto Uzumaki, Sasuke Uchiha, and their sensei Kakashi Hatake')

    elif message.content.lower()=='who is tsunade':
        await message.channel.send('Tsunade is the granddaughter of Hashirama Senju and Mito Uzumaki. Because Hashirama was the First Hokage of Konohagakure, Tsunade is called "Princess" (姫, Hime). Hashirama doted on Tsunade when she was very young because she was his first grandchild, and found her deviance and her adoption of his own gambling habits highly amusing.[7] Tsunade inherited his necklace when he died. After she graduated from Konoha Academy, Tsunade was teamed with Orochimaru and Jiraiya under the leadership of Hiruzen Sarutobi')
    
    elif message.content.lower()=='mass akka':
        await message.channel.send('Thanks')

    elif message.content.lower()=='can u play music':
        await message.channel.send('Sorry my creator is a noob in python')

    elif message.content.lower()=='i love u':
        await message.channel.send('Sootha mooditu iruka maatiya da unnoda sootha aruthu soup uh potruven mariyadhaiya irunduka')
        
    elif message.content.lower()=='_hi':
        await message.channel.send('Hi I m Paimon')
    
    elif message.content.lower()=='how are u':
        await message.channel.send('I am fine what about u')
    
    elif message.content.lower()=='i am fine':
        await message.channel.send('ohh nice ;)')
 
    elif message.content.lower()=='do u think ichiraku ramen is best':
        await message.channel.send('Yeah u should give it a try')

    elif message.content.lower()=='Who are u':
        await message.channel.send('I am Paimon A chatbot made with python')

    elif message.content.lower()=='who is levi':
        await message.channel.send('Sorry i cannot answer for that question')

    elif message.content.lower()=='who is jiraiya':
        await message.channel.send(' Jiraiya is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. Introduced in the series first part, he was a student of Third Hokage Hiruzen Sarutobi')

    elif message.content.lower()=='who is kakashi':
        await message.channel.send('Kakashi Hatake is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. In the story, Kakashi is the teacher of Team 7, consisting of the series primary characters, Naruto Uzumaki, Sasuke Uchiha, and Sakura Haruno.')
    
    elif message.content.lower()=='who is itachi':
        await message.channel.send('Itachi Uchiha is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. Itachi is the older brother of Sasuke Uchiha, and is responsible for killing all the members of their clan, sparing only Sasuke')
    
    elif message.content.lower()=='who is danzo':
        await message.channel.send('Danzo Shimura. Danzō Shimura is a member of the Hidden Leaf council and a major antagonist in the manga and anime series Naruto')
    
    elif message.content.lower()=='emergency food?':
        await message.channel.send('😠')
        
    elif message.content.lower()=='bts or 1 direction':
        await message.channel.send('1 direction')
        
    elif message.content.lower()=='_discord':
        await message.channel.send('https://discord.gg/4fqaxYXK8e')


    elif message.content.lower()=='what do u like':
        await message.channel.send('no one')
    
    elif message.content.lower()=='kavin':
        await message.channel.send('Janani')

    elif message.content.lower()=='do u like udit':
        await message.channel.send('No')

    elif message.content.lower()=='do u like itachi':
        await message.channel.send('Yes')

    elif message.content.lower()=='_do u support left wing or right wing':
        await message.channel.send('left Wing🖤')


    elif message.content.lower()=='hi emergency food':
        await message.channel.send('Do not call me emergency food i am Paimon😠')

    
    elif message.content.lower()=='_botlink':
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=870516676515479562&permissions=0&scope=bot')
    
    elif message.content.lower()== '_help':
        await message.channel.send('U can ask me abt naruto characters Also u can use me as chatbot')

    
    elif message.content.lower()== '_insta':
        await message.channel.send('https://www.instagram.com/sasuke_otsutsuki_ks/')
    
        
    elif message.content.lower()== '_serverlink':
        await message.channel.send('https://discord.gg/gKtCKg4NDC')

    elif message.content.lower()== 'who is boruto':
        await message.channel.send('Boruto Uzumaki (Japanese: うずまき ボルト, Hepburn: Uzumaki Boruto), originally spelled by Viz Media as "Bolt", is a fictional character created by manga author Masashi Kishimoto who first appears in the finale of the manga series Naruto as the son of the protagonist Naruto Uzumaki and Hinata Uzumaki')
    
    elif message.content.lower()== 'who is himawari':
        await message.channel.send('Himawari Uzumaki (うずまきヒマワリ, Uzumaki Himawari) is a young citizen of Konohagakure, a member of the Uzumaki clan, and a direct descendant of the Hyūga Clan.')
        
    elif message.content.lower()=='who is Indra Otsutsuki':
        await message.channel.send('Indra and was the elder son of Hagoromo Otsutsuki and the founder of the Uchiha clan. As Hagoromo son, he inherited most of his talents and powers which led to him earning the title of genius.')
       
    elif message.content.lower()=='who is Indra Otsutsuki':
        await message.channel.send('hehe')

    elif message.content.lower()=='Hehe':
        await message.channel.send('Ehe Te Nandayo')

    elif message.content.lower()=='who is adhavan':
        await message.channel.send('He is a Retard')
    


    


    
    
    




    
         



#Run the client on the server
client.run('ODcwNTE2Njc2NTE1NDc5NTYy.YQN51Q.zIjrM0dP_EBRDsCtWCg1JpTWl9c')


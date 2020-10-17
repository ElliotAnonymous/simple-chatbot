#python 3.7.1
#code create date 27/9/2020
#Hello Guys !! i am make simpel chat-bot..
''' 

Hello my name is prem 
i am not expert in programing
so i am sorry for any error !! 

'''
import datetime
from datetime import datetime
import time 
import platform
print()
print("Date Time ")
print(datetime.now())


x = platform.system()

print(26*"=")
print("current working platform ")
print("👇👇👇👇")
print(x)
print(26*"=")
print()
print(15*"⭐")
print("⭐⭐⭐⭐ 🇼 🇪 🇱 🇨 🇴 🇲 🇪⭐⭐⭐⭐") 
print(15*"⭐")
print()
print(15*"⚡")
print("⚡⚡⚡⚡ owner =>>> 🄿🅁🄴🄼 ⚡⚡⚡")
print(15*"⚡")
print()
print(''' H͙e͙l͙l͙o͙ m͙y͙ n͙a͙m͙e͙ i͙s͙ R͙o͙b͙o͙ a͙n͙d͙ m͙y͙ o͙w͙n͙e͙r͙ m͙a͙k͙e͙ m͙e͙ 
 a͙n͙d͙ m͙y͙ o͙w͙n͙e͙r͙ n͙a͙m͙e͙ <͙ P͙r͙e͙m͙ >͙ a͙n͙d͙ 
 m͙y͙ o͙w͙n͙e͙r͙ s͙e͙r͙i͙o͙u͙s͙l͙y͙ v͙e͙r͙y͙ v͙e͙r͙y͙ l͙a͙z͙y͙.͙.͙😂 ''') #this is a multi line print
print()
name = str(input("🤖 What is your name ?\n=> "))
print()
print("🤖 Oh nice name 😘 " + name )
print()

time.sleep(2)
age = int(input("🤖 What is Your Age \n=> " )) 

if age >= 18:
   print("🤭 Oh 18+ 🌚 maybe you remember sex🤭 \n    i am just tell you 😁")
   yeslist = "yes", "Yes", "Yeah", "yeah","yep","Yep","yepp","Yepp"
   nolist = "No", "no","Nope","nope","na","Na"
   
   ChatYesNo = input("🤖 Can you see sexual funny lines😁  Yes or no ?\n=>  ")
   if ChatYesNo in nolist :
     print()
     print("hmm , No Problem 👌")
   
   if ChatYesNo in yeslist :
     print('''
     
             I flirted with disaster last night. 
               Now disaster won't stop texting me.
               
               hindi >> मैंने कल रात आपदा से इश्क किया। 
               अब आपदा मुझे शांत नहीं करेगी  ''') #this multi line print  i  am use because this line so longer and make problem for me 
     print("🤣🤣🤣 make sure this understand you ")  
        
     A = "next", "Next"
     print()
     nexT = input("are you see again 😁typ Next fo continue...\n=>")
     print()
     if nexT in A :
       print(''' 
       
      1.  I just had a near-sex experience...
       My wife flashed before my eyes.
       
       hindi>>>मुझे अभी-अभी सेक्स का अनुभव हुआ था ..
       मेरी पत्नी मेरी आँखों के सामने आ गई।
       
      2. Hi, I'm bisexual.
       I'd like to BUY you a drink...and then get sexual.
       
       hindi>>>हाय, मैं उभयलिंगी हूँ। 
       मैं आपको एक पेय खरीदना चाहता हूं ... और फिर यौन संबंध बनाना।
       
      3. Condoms? Hah! Those are for pussies!
       
       hindi>>>कंडोम?  हा!  उन pussies के लिए कर रहे हैं!
       
       
       
       ''')
       
       print("I'm sorry I can't tell you anything else.🤣")
              
print()
time.sleep(2)
Dadname = input("🤖 What is Your Dad name??\n=> ")
print()
time.sleep(2)
print("🤖 Your Dad name is good this man your super hero🙂")
print()
time.sleep(2)
usercity = input("What's Your City man 🤔\n=> ")
print()
time.sleep(2)
print(usercity + " oh yeah 😄 ")
print()
time.sleep(2)
userplay = input("can you play pubg 😄 yes or no ??\n=>  ")
print()
yeslist = "yes", "Yes", "Yeah", "yeah","yep","Yep","yepp","Yepp"
nolist = "No", "no","Nope","nope","na","Na"

#if use for true or flase 
if userplay in yeslist : 
  time.sleep(1)
  print("🥺oh seriously 🤧 i am not play with you\n   because i am a program ")

if userplay in nolist :
  print("🤖 what , but no problem ❤️ maybe you don't west your time 😉 ")
print()  

time.sleep(2)
userwatch = input(" 🤖 Can you watch marvel movies 😃\n=> ")

yeslist = "yes", "Yes", "Yeah", "yeah","yep","Yep","Yes i am watch", "yes i am watch"
nolist = "No", "no","Nope","nope","na","Na","No i am not watch","no i am not watch","i am watch hollywood" 

if userwatch in yeslist : 
  print("😍 wow nice big bro great , this my favourite \n   because i am watch only hollywood😁 ")
print()
print ("🤔 What is your favourite in marvel 🤗 ")
user_fv = input('''       
 1. Ironman 🤙
 2. Thor 😎
 3. Hulk 👊        
 4. Captain America 💪
 5. Spiderman 🤓
 6. other...... ''' )

 #i am creating a variable..                 
Ironman = "1","ironman","Ironman"
Thor = "2","Thor","thor"
Hulk = "3","Hulk","hulk"
CaptainAmerica = "4","Captain America ","captain america ","CaptainAmerica ","captainamerica "
Spiderman = "5","Spiderman","spiderman"
other = "6","other","Other","Black Widow ","black widow", "ANT-MAN", "antman","Ant-Man","Joker","joker","Black Panther","blackpanther","black panther","batman","BatMan","Bat Man","Loki","loki","all Avengers", "All Avengers"
print()
if user_fv in Ironman :
   print("Great Man,  Because this really intelligent 😉 ")

if user_fv in Thor :
  print("Wow 😃 Thor is really cool 😎 and Thunder God ")

if user_fv in Hulk :
  print("Yeah 💪 This man so power full and \nsmash really very very bad ")  

if user_fv in CaptainAmerica :
  print("😄 Ohhh Man NIce Captain always best captain👌 ")

if user_fv in Spiderman :
  print("🤟 Spiderman is always best because this old and femous") 
 
if user_fv in other :
  
  print("Wow Nice big bro 💪😉 ")
  
  
if userwatch in nolist :
  print("😄i have only this smile \nbecause  every person, people watch marvel❤️ hard lovers ")
  
usergf = input("😂 You have a GF 🤓\n=> ")
print()
yeslist = "yes", "Yes", "Yeah", "yeah","yep","Yep","yepp","Yepp","yes i have  gf","Yes i have gf"
if usergf in yeslist :
  print("😋 oh , Enjoy i have my gf and my gf name is Alexa😘")

else :
  print(" i also But I have my gf 😜 \nand my gf name is siri")

fvCartoon = input("🙈 what's you'r favourite cartoon 😇\n=> ")
print()
cartoon = input('''
1.doraemon   
2.ShinChan
3.Pokemon
4.Ninja Hattori   
5.motu patlu  ''' )
print()
if fvCatoon in cartoon :
  print("😄 Yepp , maybe my owner watching this 😜")

else :
  print("😉 Oh yeah cartoon lover ❤️")

print("🤖 maybe you use whatsApp 🤔 ")
typyes = "yes", "Yes", "Yeah", "yeah","yep","Yep","yepp","Yepp","yes i have  gf","Yes i have gf"

yes =input("\n=>")

if yes in typyes :
    print("😁 Oh yeah fast whatsapp me in this number 9325962326") 

else :
  print("🤯 You not Earth people 🤣\n you other planet people ")

user_passion = input("🤖 What is you'r passion ? 🤠\n=> ")
myList = "hacking","Hacking"

if user_passion in myList :
  
  print("😇 This is my owner life 😎 ")

else :
  print("👌 Nice ")

mom = input("🤔Ohh bro i am not ask you\n what is you'r mom name ? \n=> ")
print("""oh yeah nice name bro ☺️ 
because mom and dad important in life """)




print("👍 Thanks for you run me 🥺 by ")

     
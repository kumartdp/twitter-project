from django.shortcuts import render
import requests
import tweepy
from random import randint
from textblob import TextBlob
import re
from time import sleep
import json
import matplotlib.pyplot as plt



def button(request):
    print("enter")
    return render(request,'new2.html')
def button1(request):
    return render(request,'button1.html')
def button2(request):
    return render(request,'button2.html')
def output1(request):
    data=request.GET['key']
    repeat(data,2)
    return render(request,'button2.html')
def output(request):
    
    data=request.GET['key']
    repeat(data,0)
    print(data)
     
    consumerkey="lwoafbF70NIyPlkreXEOcQm8s"
    consumersecret="ri4e5iVBAhNNgK6oQ6VCIVZ4covHBVa0onbpP1rUDyqGuzDsZa"
    accesskey="1174334913710940160-MLIfcY3nXhVJqNifUI7XfaaLfyDKzz"
    accesssecret="FnRkCYm6KPDv4NZpgj6eNHEOVrm2YHMUJkHx53ZKjFZXm"
    auth = tweepy.OAuthHandler(consumerkey, consumersecret) 
    auth.set_access_token(accesskey, accesssecret)    
    api=tweepy.API(auth)
    auth.secure=True
    l=['#pollution','#rainfall']
    polp,poln,ipos,ineg=0,0,0,0
    i=0
    vb,b,o,g,p=0,0,0,0,0
    count=0
    return render(request,'button1.html')
    
def repeat(d,p):
    print("okkk")
    print(p)
    
    consumerkey="lwoafbF70NIyPlkreXEOcQm8s"
    consumersecret="ri4e5iVBAhNNgK6oQ6VCIVZ4covHBVa0onbpP1rUDyqGuzDsZa"
    accesskey="1174334913710940160-MLIfcY3nXhVJqNifUI7XfaaLfyDKzz"
    accesssecret="FnRkCYm6KPDv4NZpgj6eNHEOVrm2YHMUJkHx53ZKjFZXm"
    auth = tweepy.OAuthHandler(consumerkey, consumersecret) 
    auth.set_access_token(accesskey, accesssecret)    
    api=tweepy.API(auth)
    auth.secure=True
    vb,b,o,g,p1=0,0,0,0,0
    count=0
         
            
           
    
    
    
    if(p!=2):
        
        
        z=150   
        
        for tweet in tweepy.Cursor(api.search,q=d,lang='en',unicode='UTF-8').items(z):
            print("hello")
            twee=tweet.text
            twee = twee.lower() 
                    
            twee= re.sub(r'@[^\s]+', ' ', twee) 
            twee = re.sub(r'#([^\s]+)', r'\1', twee) 
            t=twee.split(" ")
            d1=dict()
            tw=str()
            for i in t:
                
                d1[i]=0
            for j in t:
                if(d1[j]==0):
                    
                    tw=tw+" "+j
                    d1[j]=1
            a=TextBlob(tw)
            sub=a.sentiment[1]
            if(sub>0.5):
                z-=1
                
                
                count+=1
                pol=a.sentiment.polarity
                print(tw)
                if(pol>=-1.0 and pol<=-0.5):
                    
                   
                    vb+=1
                elif(pol>-0.5 and pol<=-0.1):
                    b+=1
                elif (pol>-0.1 and pol<=0.2):
                    o+=1
                elif(pol>0.2 and pol<=0.6):
                    g+=1
                else:
                    
                    p1+=1
                sleep(1)
            
        dict1={vb:"very bad",b:"bad",o:"ok",g:"good",p1:"positive"}
        l1=[]
        l1.append(vb)
        l1.append(b)
        l1.append(o)
        l1.append(g)
        l1.append(p1)
        max1=max(l1)
        print(count)
        print(l1)
        print(dict1[max1])
        if(p==1):
        
            labels = 'verybad', 'bad', 'ok', 'good','very good'
            sizes = [vb,b,o,g,p1]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','green']
            plt.pie(sizes,labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
            plt.axis('equal')
            plt.show()
        if(p==0):
            count1=0
        
         
            for tweet in tweepy.Cursor(api.search,q=d,lang='en',unicode='UTF-8').items(110):
    
            
            
            
                count1+=1
        
            
            
            
                t="#automated tweet feeling\n"+" "+dict1[max1]+" "+"regarding"+" "+d+str(count1)
                try:
                    api.update_status(t)
                    tweet.retweet()
                except tweepy.TweepError as e:
                    print(e)
                
    if(p==2): 
        for tweet in api.user_timeline(screen_name=d):
            tweet.favorite();
    return      
def newfun(request):
    return render(request,'button1.html')
def trend(request):
    print("trend")
    
    
        
        
    consumerkey="UNl49VtzHxHMzmocMHa00P7gQ"
    consumersecret="W2SLgpJh6wmSe7Z46Q8361qvVcV0STbku7UpnLgvMpPJRonsFA"
    accesskey="1174334913710940160-OXl03lmQzIGrDXOp2GaeUo6YnBS6od"
    accesssecret="BwbJgpNYcLF3vr5Kb52RvEueReEcKA8JJ1Y7FnggxSSiX"
    auth = tweepy.OAuthHandler(consumerkey, consumersecret) 
    auth.set_access_token(accesskey, accesssecret)    
    api=tweepy.API(auth)
    auth.secure=True
    
    brazil=23424848
    print("okkkkkkkkkkk")
    btrends=api.trends_place(brazil)
    print(btrends)
    trends=json.loads(json.dumps(btrends,indent=1))
    for trend in trends[0]["trends"]:
        
        
        d=trend['name']
        sleep(5)
        print(d)
            
        repeat(d,1)
        sleep(180)
        break
    
    return render(request,'new2.html')



    

    


    
        


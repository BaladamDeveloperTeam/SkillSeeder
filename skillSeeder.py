import random
import json


users = open("./users.json",'r').readlines()
skills = open("./skills.json",'a')
# print(json.loads(users[0])['_id']['$oid'])

# user = json.loads(users[0])

# ['occupations'][random.randrange(0,len(json.loads(users[0])['occupations']))]['occupation']['$numberInt']
# print(user['profile']['occupations'][random.randrange(0,len(user['profile']['occupations']))]['occupation']['$numberInt'])
c = 0
for user in users:
    user = json.loads(user)

    if (user['role']['$numberInt'] == '1'):
        for i in range(random.randrange(1,6)):
            randomCat =random.randrange(0,len(user['profile']['occupations']))
            category = user['profile']['occupations'][randomCat]['occupation']['$numberInt']
            filds = user['profile']['occupations'][randomCat]['fields']
            subCategory = filds[random.randrange(0,len(filds))]['$numberInt']
            accept='accept'
            randAccept = random.randrange(1,100)
            if (randAccept%2==0):
                accept = 'accept'
            elif(randAccept%5==0):
                accept = 'reject'
            elif(randAccept%2==1):
                accept ='stall'
            deliverCount = random.randint(1,3)

            deliveries = [
               {
                   "cost":random.randint(1,5)*1000,
                   "repeat":random.randint(1,5)
               },
               {
                   "cost":random.randint(5,8)*1000,
                   "repeat":random.randint(1,5)
               },
               {
                   "cost":random.randint(8,10)*1000,
                   "repeat":random.randint(1,5)
               }
            ]
            if (bool(random.randint(0,1))):
                deliveries[0] = {}
            if (bool(random.randint(0,1))):
                deliveries[1] = {}
            if (bool(random.randint(0,1))):
                deliveries[2] = {}


            feature1=[]
            feature2=[]
            feature3=[]
            randFeature = random.randint(5,10)
            for j in range(randFeature):
                isTik = random.randint(0,1)
                check = True
                if (isTik == 0):
                    check=True
                    isTik ='text'
                else:
                    check = bool(random.randint(0,1))
                    isTik ='checkbox'
                feature1.append({'title':'feature'+str(random.randint(1,100)),'type':isTik,'check':check})

            for j in range(randFeature):
                feature2.append(feature1[j])
                if (feature1[j]['type'] == 'text'):
                    feature2[j]['title'] = 'feature'+str(random.randint(1,100))
                if (not feature1[j]['check']):
                    feature2[j]['check'] = bool(random.randint(0,1))
            for j in range(randFeature):
                feature3.append(feature2[j])
                if (feature2[j]['type'] == 'text'):
                    feature3[j]['title'] = 'feature'+str(random.randint(1,100))
                if (not feature2[j]['check']):
                    feature3[j]['check'] = bool(random.randint(0,1))

            images=[]
            for j in range(3):
                images.append( {
                    'topic':"عکس مهارت",
                    'url':"images/"+str(j)+".jpg",
                    'pos':j+1

                })

            
            skill = {
                "name":"skill"+str(c),
                "category": int(category),
                "subCategory": int(subCategory),
                "images":images,
                "description":"لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.",
                "tags":['tag'+str(random.randint(1,5)),'tag'+str(random.randint(6,10)),'tag'+str(random.randint(11,15))],
                "boxes":[
                    {
                        "cost":random.randint(1,70)*1000,
                        "time":random.randint(1,5),
                        "delivery":deliveries[0],
                        "features":feature1
                        },
                    {
                        "cost":random.randint(100,800)*1000,
                        "time":random.randint(6,10),
                        "delivery":deliveries[1],
                        "features":feature2
                        },
                    {
                        "cost":random.randint(800,1000)*1000,
                        "time":random.randint(11,20),
                        "delivery":deliveries[2],
                        "features":feature3
                        },

                ],
                "user_id":user['_id']['$oid'],
                "stamina":5,
                "seen":[],
                "buyNumber":0,
                "avgRate":0.0,
                "status":bool(random.randint(0,1)),
                'accept':accept,
                'like':[],
                'buys':[],
                "favorite":[]

            }
            c+=1
            skills.write(json.dumps(skill))
            skills.write('\n')





# print(skill)

import firebase_admin
from firebase_admin import db, credentials
from firebase_admin import storage
import random
import math
import requests

# you need to add your credentials here
cred = credentials.Certificate("../DAO/credentials.json")
# cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "your database url",
    'storageBucket': 'your storage url'})

# need a round mark in db

# get it from frontend
# uid = 'asdkhasd'
version = 'customizable'


def adduser(uid):
    # default settings
    name = "S.B."
    email = "xxx@xxx.com"
    gender = "male"
    age = 30
    height = 180
    weight = 75
    location = "Hong Kong"
    persona = "friendly"
    style = "friendly and warm"
    character = "none"
    contraindication = "none"
    healthconcern = "none"
    # default settings
    emotion = 'neutral_'
    habit = 'regular_'
    limitation = 'neutral_'
    goal = 'keep healthy_'
    preference = 'delicous healthy food'
    env = 'home_'
    his = 'delicious local foods_'
    accfrst = "none"
    accscnd = "none"
    accfood = "none"

    userinit = {"S_name": name, "S_email": email, "S_gender": gender, "S_age": age, "S_height": height,
                "S_weight": weight, "S_location": location, "S_character": character, "S_persona": persona,
                "S_style": style, "S_health": healthconcern, "S_history": his, "D_contraindication": contraindication,
                "D_emotion": emotion, "D_eating habit": habit, "D_time limitation": limitation, "D_goal": goal,
                "D_env": env, "D_preference": preference, "D_firstaccept": accfrst, "D_secondaccept": accscnd,
                "D_accfood": accfood}

    chitchatround = 0
    chathistory = ''
    currenttopic = 'icebreak'
    preferencefood = 'none'
    image = ''
    allfoods = ''
    tasks = {"emotion": 0, "hunger level": 0, "time limitation": 0, "goal": 0, "env": 0, "his": 0}

    convinit = {"D_history": chathistory, "D_currenttopic": currenttopic, "D_chitchatround": chitchatround,
                "image": image, "preferencefood": preferencefood, "allfoods": allfoods, "D_tasks": tasks}

    acca = 'none'
    expa = 'none'
    expb = 'none'
    expc = 'none'
    intera = 'none'
    usefa = 'none'
    usefb = 'none'
    trusta = 'none'
    trustb = 'none'
    eata = 'none'
    useia = 'none'
    useib = 'none'
    useic = 'none'
    quaa = 'none'
    ada = 'none'
    adb = 'none'
    cusa = 'none'
    cusb = 'none'
    cusc = 'none'
    edul = 'none'
    workf = 'none'
    race = 'none'
    hper = 'none'
    feedback = 'none'
    extra = 'none'

    surveytime = ''

    uxinit = {"accuracya":acca,"explanationa":expa,"explanationb":expb,"explanationc":expc,"interactiona":intera,"usefula":usefa,"usefulb":usefb,"trusta":trusta,"trustb":trustb,'eata':eata,'useintenta':useia,'useintentb':useib,'useintentc':useic,'quality':quaa,'additionala':ada,'additionalb':adb,'customizea':cusa,'customizeb':cusb,'customizec':cusc,'education':edul,'work':workf,'race':race,'humanpersonality':hper,'feedback':feedback,"extra":extra,"surveytime":surveytime}

    proid = 'none'

    db.reference("/" + version + '/' + uid).update(
        {
            'userprofile': userinit,
            'conversation': convinit,
            'userexperience': uxinit,
            'AprolificID': proid
        })


def addbaseline(uid):
    fixper = 'introverted'
    fixstyle = 'formally'

    # default settings
    name = "S.B."
    email = "xxx@xxx.com"
    gender = "male"
    age = 30
    height = 180
    weight = 75
    location = "Hong Kong"
    persona = fixper
    style = fixstyle
    character = "none"
    contraindication = "none"
    healthconcern = "none"
    # default settings
    emotion = 'neutral_'
    habit = 'regular_'
    limitation = 'neutral_'
    goal = 'keep healthy_'
    preference = 'delicous healthy food'
    env = 'home_'
    his = 'delicious local foods_'
    accfrst = "none"
    accscnd = "none"
    accfood = "none"

    userinit = {"S_name": name, "S_email": email, "S_gender": gender, "S_age": age, "S_height": height,
                "S_weight": weight, "S_location": location, "S_character": character, "S_persona": persona,
                "S_style": style, "S_health": healthconcern, "S_history": his, "D_contraindication": contraindication,
                "D_emotion": emotion, "D_eating habit": habit, "D_time limitation": limitation, "D_goal": goal,
                "D_env": env, "D_preference": preference, "D_firstaccept": accfrst, "D_secondaccept": accscnd,
                "D_accfood": accfood}

    chitchatround = 0
    chathistory = ''
    currenttopic = 'icebreak'
    preferencefood = 'none'
    image = ''
    allfoods = ''
    tasks = {"emotion": 0, "hunger level": 0, "time limitation": 0, "goal": 0, "env": 0, "his": 0}

    convinit = {"D_history": chathistory, "D_currenttopic": currenttopic, "D_chitchatround": chitchatround,
                "image": image, "preferencefood": preferencefood, "allfoods": allfoods, "D_tasks": tasks}

    acca = 'none'
    expa = 'none'
    expb = 'none'
    expc = 'none'
    intera = 'none'
    usefa = 'none'
    usefb = 'none'
    trusta = 'none'
    trustb = 'none'
    eata = 'none'
    useia = 'none'
    useib = 'none'
    useic = 'none'
    quaa = 'none'
    ada = 'none'
    adb = 'none'
    botstyle = 'none'
    edul = 'none'
    workf = 'none'
    race = 'none'
    hper = 'none'
    feedback = 'none'
    extra = 'none'

    surveytime = ''

    uxinit = {"accuracya":acca,"explanationa":expa,"explanationb":expb,"explanationc":expc,"interactiona":intera,"usefula":usefa,"usefulb":usefb,"trusta":trusta,"trustb":trustb,'eata':eata,'useintenta':useia,'useintentb':useib,'useintentc':useic,'quality':quaa,'additionala':ada,'additionalb':adb,'chatbotstyle':botstyle,'education':edul,'work':workf,'race':race,'humanpersonality':hper,'feedback':feedback,"extra":extra,"surveytime":surveytime}

    proid = 'none'

    db.reference("/" + version + '/' + uid).update(
        {
            'userprofile': userinit,
            'conversation': convinit,
            'userexperience': uxinit,
            'AprolificID': proid
        })


def upload_image_to_firebase(user_id, image_name, image_url):
    response = requests.get(image_url)
    image_data = response.content

    destination_filename = f'{user_id}/{image_name}'

    bucket = storage.bucket()
    blob = bucket.blob(destination_filename)
    blob.upload_from_string(image_data, content_type='image/jpeg')

    blob.make_public()
    image_url = blob.public_url

    return image_url


def pulluid():
    snapshot = db.reference('/' + version + '/').order_by_key().get()
    uidlst = list(snapshot.keys())
    return uidlst


def getemail(uid):
    email = db.reference('/' + version + '/' + uid + "/userprofile/S_email").get()
    return email


def getcal(uid):
    gender = db.reference('/' + version + '/' + uid + "/userprofile/S_gender").get()
    age = db.reference('/' + version + '/' + uid + "/userprofile/S_age").get()
    height = db.reference('/' + version + '/' + uid + "/userprofile/S_height").get()
    weight = db.reference('/' + version + '/' + uid + "/userprofile/S_weight").get()
    meta = (10 * weight + 6.25 * height - 5 * age) * 1.55
    if gender == 'male':
        return math.ceil(0.5 * (meta + 5 * 1.55))
    if gender == 'female':
        return math.ceil(0.5 * (meta - 161 * 1.55))
    if gender == 'intersex':
        return math.ceil(0.5 * (meta + 5 * 1.55))


def getloc(uid):
    loc = db.reference('/' + version + '/' + uid + "/userprofile/S_location").get()
    return loc


def getchara(uid):
    cha = db.reference('/' + version + '/' + uid + "/userprofile/S_character").get()
    return cha


def getpersona(uid):
    per = db.reference('/' + version + '/' + uid + "/userprofile/S_persona").get()
    return per


def getstyle(uid):
    style = db.reference('/' + version + '/' + uid + "/userprofile/S_style").get()
    return style


def getconcern(uid):
    concern = db.reference('/' + version + '/' + uid + "/userprofile/S_health").get()
    return concern


def gethistory(uid):
    his = db.reference('/' + version + '/' + uid + "/userprofile/S_history").get()
    return his


def getcon(uid):
    con = db.reference('/' + version + '/' + uid + "/userprofile/D_contraindication").get()
    return con


def getemo(uid):
    emo = db.reference('/' + version + '/' + uid + "/userprofile/D_emotion").get()
    return emo


def geteh(uid):
    eh = db.reference('/' + version + '/' + uid + "/userprofile/D_eating habit").get()
    return eh


def getlimit(uid):
    limit = db.reference('/' + version + '/' + uid + "/userprofile/D_time limitation").get()
    return limit


def getgoal(uid):
    goal = db.reference('/' + version + '/' + uid + "/userprofile/D_goal").get()
    return goal


def getenv(uid):
    env = db.reference('/' + version + '/' + uid + "/userprofile/D_env").get()
    return env


def getprefer(uid):
    prefer = db.reference('/' + version + '/' + uid + "/userprofile/D_preference").get()
    return prefer


def gettopic(uid):
    topic = db.reference('/' + version + '/' + uid + "/conversation/D_currenttopic").get()
    return topic


def getround(uid):
    round = db.reference('/' + version + '/' + uid + "/conversation/D_chitchatround").get()
    return round


def getimage(uid):
    image = db.reference('/' + version + '/' + uid + "/conversation/image").get()
    return image


def getallfoods(uid):
    allfoods = db.reference('/' + version + '/' + uid + "/conversation/allfoods").get()
    return allfoods


def getpreferencefood(uid):
    food = db.reference('/' + version + '/' + uid + "/conversation/preferencefood").get()
    return food


def gettask(uid):
    tasks = db.reference('/' + version + '/' + uid + "/conversation/D_tasks").get()
    taskAvailable = []
    for key in tasks:
        if tasks[key] == 0:
            taskAvailable.append(key)

    if len(taskAvailable) != 0:
        random.shuffle(taskAvailable)
        return taskAvailable[0]
    if len(taskAvailable) == 0:
        return 'finished'


def getwholeconversation(uid):
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    return conv


def getlasttround(uid):
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    lst = conv.split('chatbot: ')
    if len(lst) > 1 and lst[-2:][0] != '':
        res1 = "chatbot: " + lst[-2:][0]
        res2 = "chatbot: " + lst[-2:][1]
        return res1, res2
    else:
        return 'none', 'none'


def getlastround(uid):
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    lst = conv.split('chatbot: ')
    res = "chatbot: " + lst[-1]
    return res


def getlastusersent(uid):
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    lst = conv.split('user: ')
    res = "user: " + lst[-1]
    return res


def getexpc(uid):
    expc = db.reference('/' + version + '/' + uid + "/userexperience/explanationc").get()
    return expc


def getextra(uid):
    extra = db.reference('/' + version + '/' + uid + "/userexperience/extra").get()
    return extra


def getbotstyle(uid):
    style = db.reference('/' + version + '/' + uid + "/userexperience/chatbotstyle").get()
    return style


def upemail(uid, email):
    db.reference('/' + version + '/' + uid + "/userprofile/S_email").set(email)


def upgender(uid, gen):
    db.reference('/' + version + '/' + uid + "/userprofile/S_gender").set(gen)


def upage(uid, age):
    db.reference('/' + version + '/' + uid + "/userprofile/S_age").set(int(age))


def upheight(uid, height):
    db.reference('/' + version + '/' + uid + "/userprofile/S_height").set(float(height))


def upweight(uid, weight):
    db.reference('/' + version + '/' + uid + "/userprofile/S_weight").set(float(weight))


def uploc(uid, loc):
    db.reference('/' + version + '/' + uid + "/userprofile/S_location").set(loc)


def upcha(uid, cha):
    db.reference('/' + version + '/' + uid + "/userprofile/S_character").set(cha)


def uppersona(uid, per):
    db.reference('/' + version + '/' + uid + "/userprofile/S_persona").set(per)


def upstyle(uid, style):
    db.reference('/' + version + '/' + uid + "/userprofile/S_style").set(style)


def upconcern(uid, concern):
    db.reference('/' + version + '/' + uid + "/userprofile/S_health").set(concern)


def uphistory(uid, his):
    db.reference('/' + version + '/' + uid + "/userprofile/S_history").set(his)


def upemo(uid, emo):
    db.reference('/' + version + '/' + uid + "/userprofile/D_emotion").set(emo)


def upeh(uid, eh):
    db.reference('/' + version + '/' + uid + "/userprofile/D_eating habit").set(eh)


def uplimit(uid, limit):
    db.reference('/' + version + '/' + uid + "/userprofile/D_time limitation").set(limit)


def upgoal(uid, goal):
    db.reference('/' + version + '/' + uid + "/userprofile/D_goal").set(goal)


def upenv(uid, env):
    db.reference('/' + version + '/' + uid + "/userprofile/D_env").set(env)


def upprefer(uid, prefer):
    db.reference('/' + version + '/' + uid + "/userprofile/D_preference").set(prefer)


def upcon(uid, con):
    ocon = db.reference('/' + version + '/' + uid + "/userprofile/D_contraindication").get()
    ncon = con
    if ocon == 'none':
        ncon = con
    else:
        ncon = ocon.replace('none', '') + ', ' + con
    db.reference('/' + version + '/' + uid + "/userprofile/D_contraindication").set(ncon)


def uptopic(uid, topic):
    db.reference('/' + version + '/' + uid + "/conversation/D_currenttopic").set(topic)


def upround(uid, round):
    db.reference('/' + version + '/' + uid + "/conversation/D_chitchatround").set(round)


def upimage(uid, image):
    db.reference('/' + version + '/' + uid + "/conversation/image").set(image)


def upallfoods(uid, food):
    ofood = db.reference('/' + version + '/' + uid + "/conversation/allfoods").get()
    db.reference('/' + version + '/' + uid + "/conversation/allfoods").set(ofood + food + '[FSEP]')


def uppreferencefood(uid, food):
    db.reference('/' + version + '/' + uid + "/conversation/preferencefood").set(food)


def uptask(uid, task):
    db.reference('/' + version + '/' + uid + "/conversation/D_tasks/" + task).set(1)


def upconversation(uid, botsent, usersent):
    meta = "chatbot: " + botsent + " user: " + usersent + " "
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    if conv == '':
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(meta)
    else:
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(conv + meta)


def upconversation_u(uid, usersent):
    meta = " user: " + usersent + " "
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    if conv == '':
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(meta)
    else:
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(conv + meta)


def upconversation_b(uid, botsent):
    meta = "chatbot: " + botsent
    conv = db.reference('/' + version + '/' + uid + "/conversation/D_history").get()
    if conv == '':
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(meta)
    else:
        db.reference('/' + version + '/' + uid + "/conversation/D_history").set(conv + meta)


def upaccfrst(uid, state):
    db.reference('/' + version + '/' + uid + "/userprofile/D_firstaccept").set(state)


def upaccscnd(uid, state):
    db.reference('/' + version + '/' + uid + "/userprofile/D_secondaccept").set(state)


def upaccfood(uid, accfood):
    db.reference('/' + version + '/' + uid + "/userprofile/D_accfood").set(accfood)


def upacca(uid, acca):
    db.reference('/' + version + '/' + uid + "/userexperience/accuracya").set(acca)


def upexpa(uid, expa):
    db.reference('/' + version + '/' + uid + "/userexperience/explanationa").set(expa)


def upexpb(uid, expb):
    db.reference('/' + version + '/' + uid + "/userexperience/explanationb").set(expb)


def upexpc(uid, expc):
    db.reference('/' + version + '/' + uid + "/userexperience/explanationc").set(expc)


def upintera(uid, intera):
    db.reference('/' + version + '/' + uid + "/userexperience/interactiona").set(intera)


def upusefa(uid, usefa):
    db.reference('/' + version + '/' + uid + "/userexperience/usefula").set(usefa)


def upusefb(uid, usefb):
    db.reference('/' + version + '/' + uid + "/userexperience/usefulb").set(usefb)


def uptrusta(uid, trusta):
    db.reference('/' + version + '/' + uid + "/userexperience/trusta").set(trusta)


def uptrustb(uid, trustb):
    db.reference('/' + version + '/' + uid + "/userexperience/trustb").set(trustb)


def upeata(uid, eata):
    db.reference('/' + version + '/' + uid + "/userexperience/eata").set(eata)


def upuseria(uid, useia):
    db.reference('/' + version + '/' + uid + "/userexperience/useintenta").set(useia)


def upuserib(uid, useib):
    db.reference('/' + version + '/' + uid + "/userexperience/useintentb").set(useib)


def upuseric(uid, useic):
    db.reference('/' + version + '/' + uid + "/userexperience/useintentc").set(useic)


def upquaa(uid, quaa):
    db.reference('/' + version + '/' + uid + "/userexperience/quality").set(quaa)


def upada(uid, ada):
    db.reference('/' + version + '/' + uid + "/userexperience/additionala").set(ada)


def upadb(uid, adb):
    db.reference('/' + version + '/' + uid + "/userexperience/additionalb").set(adb)


def upcusa(uid, cusa):
    db.reference('/' + version + '/' + uid +"/userexperience/customizea").set(cusa)


def upcusb(uid, cusb):
    db.reference('/' + version + '/' + uid +"/userexperience/customizeb").set(cusb)


def upcusc(uid, cusc):
    db.reference('/' + version + '/' + uid +"/userexperience/customizec").set(cusc)


def upedu(uid, edu):
    db.reference('/' + version + '/' + uid + "/userexperience/education").set(edu)


def upwork(uid, workf):
    db.reference('/' + version + '/' + uid + "/userexperience/work").set(workf)


def uprace(uid, race):
    db.reference('/' + version + '/' + uid + "/userexperience/race").set(race)


def uphper(uid, hper):
    db.reference('/' + version + '/' + uid + "/userexperience/humanpersonality").set(hper)


def upfeedback(uid, feedback):
    db.reference('/' + version + '/' + uid + "/userexperience/feedback").set(feedback)


def upextra(uid, extra):
    db.reference('/' + version + '/' + uid + "/userexperience/extra").set(extra)


def upbotstyle(uid, style):
    db.reference('/' + version + '/' + uid + "/userexperience/chatbotstyle").set(style)


def upsurveytime(uid, surveytime):
    db.reference('/' + version + '/' + uid + "/userexperience/surveytime").set(surveytime)


def upproid(uid, proid):
    db.reference('/' + version + '/' + uid + "/AprolificID").set(proid)

# lst = pulluid()
# print(lst)

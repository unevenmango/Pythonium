import os
import sys
import random

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
print(bcolors.FAIL + "hello" + bcolors.ENDC)



def NameGen():
    sname = ['DitcherQuick&HydeDivorceLawyers.co', 'Gloooble.com', 'HeevinDistress.com']
    sname1 = ['terse','feint','vain','vituperate','drone','sidestep','repudiate','disingenuous','frugal','pitfall','countenance','sheath','redoubtable','weigh','protracted','overweening','aplomb','delineate','fluke','bogus','palliate','aver','enzyme','catalyst','coagulation','connotation','qualm','embellish','diffidence','shyness','rural','psychotic','madly','bright','fresh','third','adventurous','numberless','extra-large','nonchalant','dull','zesty','adaptable','protective','endurable','poised','illustrious','abrupt','lively','clear','crowded','massive','aberrant','drab','rustic']    
    sname2 = ['past','after','among','save','as','of','in','until','without','beneath','onto','despite','within','following','than','versus','outside','to','above','considering']    
    sname3 = ['.co','.com','.biz','.net']
    ran = random.randint(0,25)    
    if ran > 2:        
        servername = random.choice(sname1) + random.choice(sname2) + random.choice(sname3)    
    else:        
        servername = random.choice(sname)    
    return servername
def ip_gen(option='null'):        
    if option == 'local':
        ip1 = random.randint(10, 99) 
        ip2 = random.randint(10, 99) 
        ip3 = random.randint(100, 999)  
        ip_gen = str(ip1) + '.' + str(ip2) + '.' + str(ip3) 
    elif option == 'ran':   
        ip1 = random.randint(100, 400)
        ip2 = random.randint(150, 150)
        ip3 = random.randint(100, 999)
        ip4 = random.randint(10, 150)
        ip_gen = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
    else:
        ip1 = random.randint(100, 999)        
        ip2 = random.randint(10, 99)        
        ip3 = random.randint(100, 999)
        ip_gen = str(ip1) + '.' + str(ip2) + '.' + str(ip3)
    return ip_gen
def mac_gen():
    return "indev"

def ip_setup():
    port_types = {22:"ssh",21:"ftp",8080:"https"}
    ip_conf = {}
    for port in port_types:
        ip_conf[port] = {"local_ip":ip_gen('local'),"service":port_types[port]}
    return ip_conf
def Generator(ip_count):
    dyn_num = 0
    Ip_dict = {}
    while dyn_num < ip_count:
        dyn_num = dyn_num + 1
        Ip_dict[ip_gen()] = ip_setup()
    return Ip_dict

def prompt(prefix):
    command_line = "$"
    print(command_line)
    usr = input(prefix + " ")
    return usr
if (len(sys.argv) > 1):
    if sys.argv[1] == "start":
        user = prompt("username")
        print("your username is " + user)
        cwd = os.getcwd()
        if not os.path.isdir(cwd+'/'+user):
            os.mkdir(user)
            os.chdir(user+'/')
            print(user + ' dosent exsist. creating dir...')
            conf = open(user+'.conf', 'w')
            conf.write(user)
            conf.close
        else:
            print(user + 'already exsists')
        prompt = ""
        while prompt != '-q':
            prompt = prompt(user+'>')
    else:
        print(eval(sys.argv[1])) 
print('program end')


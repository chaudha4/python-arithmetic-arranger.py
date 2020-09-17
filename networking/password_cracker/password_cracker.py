import hashlib

def crack_sha1_hash(hash, use_salts=False):
    
    # /home/chaudha4/Projects/pyprojects/python-projects/networking/password_cracker/password_cracker.py
    # ['', 'home', 'chaudha4', 'Projects', 'pyprojects', 'python-projects', 'networking', 'password_cracker', 'password_cracker.py']  
    currDir = ""  
    for aa in __file__.split("/")[:-1]:
        #print(aa)
        currDir = currDir + aa + "/"


    # It is good practice to use the with keyword when dealing with file objects. The advantage is that the 
    # file is properly closed after its suite finishes, even if an exception is raised at some point.
    salts = list()
    if use_salts:
        with open(currDir + "known-salts.txt", 'r') as ff:
            for ss in ff:
                salts.append(ss.strip("\n"))



    with open(currDir + "top-10000-passwords.txt", 'r') as ff:
        for line in ff:
            line = line.strip("\n")
            if use_salts:
                for ss in salts:
                    pwd = ss + line
                    lhash = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
                    if (lhash == hash):
                        return line
                    pwd = line + ss
                    lhash = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
                    if (lhash == hash):
                        return line

            else:
                lhash = hashlib.sha1(line.encode('utf-8')).hexdigest()
                if (lhash == hash):
                    return line

    return "PASSWORD NOT IN DATABASE"

if __name__ == "__main__":

    #print(crack_sha1_hash("18c28604dd31094a8d69dae60f1bcd347f1afc5a"))
    #print(crack_sha1_hash("05bbf26a28148f531cf57872df546961d1ed0861", use_salts=True))

    assert crack_sha1_hash("18c28604dd31094a8d69dae60f1bcd347f1afc5a") == "superman", "superman test" 
    assert crack_sha1_hash("05bbf26a28148f531cf57872df546961d1ed0861", use_salts=True) == "01071988", "Salt test"    
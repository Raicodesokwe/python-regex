import random,re,this

class dondori:
    def __init__(self,under):
        self.under=under
    def __getitem__(self, item):
        return self.under[item]
    def __len__(self):
        return len(self.under)+2

mihadarati=dondori(["A","B","C","D","E"])
print(len(mihadarati))

class izaman:
    def __init__(self,saloon):
        self.saloon=saloon
    def __getitem__(self, item):
        return self.saloon[item+random.randint(-1,1)]
    def __len__(self):
        return len(self.saloon)*random.randint(0,2)
hekoku=izaman(["A","B","C","D","E"])
print(len(hekoku))
print(len(hekoku))
print(hekoku[2])
print(hekoku[2])



class diabling:
    def __init__(self):
        self.mi=["A","B"]
    def __setitem__(self, key, value):
        self.mi[key]=value
    def __getitem__(self, item):
        return self.mi[item]
y=1
z="punyeto"
x=diabling()
x[y]=z
print(x[y])

kwatakawaya=r"spam"
jaba=re.search(kwatakawaya,"eggspameggspam")
if jaba:
    print(jaba.start())
    print(jaba.end())
    print(jaba.span())
    print(jaba.group())

jocko="The name is Willock.Jocko Willock"
patan=r"Willock"
print(re.sub(patan,"Murai",jocko,1))


paterni=r"^hu.t$"
if re.match(paterni,"huet"):
    print("yo")
if re.match(paterni,"hiot"):
    print("ru")
if re.match(paterni,"huot"):
    print("pi")


jobo=r"[abcdefgh]"
if re.search(jobo,"yz"):
    print("my nigga")
if re.search(jobo,"aiii"):
    print("my nigga")
if re.search(jobo,"nyonya"):
    print("my nigga")

ndianga=r"[A-Z,a-z,0-9]"
if re.search(ndianga,"aD7"):
    print("tifi")
if re.search(ndianga,"gH5"):
    print("tifi")
if re.search(ndianga,"La5"):
    print("kweche")


gugu=r"[^A-Z]"
if re.search(gugu,"AI"):
    print("grinding")
if re.search(gugu,"Ka"):
    print("tories")
if re.search(gugu,"aa"):
    print("whigs")

Twara=r"8{1,3}"
if re.match(Twara,"8"):
    print("first instance")
if re.match(Twara,"88"):
    print("second instance")
if re.match(Twara,"8888"):
    print("third instance")

dore=r"[^A-Z]"
if re.match(dore,"aii"):
    print("tacos!")
if re.match(dore,"AII"):
    print("not tacos!")

grufu=r"a(bc)(de)(f(g)h)i"
hujintao=re.match(grufu,"abcdefghi")
if hujintao:
    print(hujintao.group())
    print(hujintao.group(0))
    print(hujintao.group(1))
    print(hujintao.group(2))
    print(hujintao.group(3))
    print(hujintao.group(4))
    print(hujintao.groups())

SisterSam=r"(?P<onest>abc)(?:def)(ghi)"
Patrick=re.match(SisterSam,"abcdefghi")
print(Patrick.group("onest"))
print(Patrick.groups())



punyeto=r"(.+)\1"
ndiole=re.match(punyeto,"abcabcde")
if ndiole:
    print("imematch wan")
ndiole=re.match(punyeto,"%^ %^")
if ndiole:
    print("imematch tu")
ndiole=re.match(punyeto,"bg gb")
if ndiole:
    print("imematch trii")


tinfoil=r"\D+\d"
match=re.match(tinfoil,"abc abc")
if match:
    print("wakiritho")
match=re.match(tinfoil,"abc56")
if match:
    print("ethic")
match=re.match(tinfoil,"w!")
if match:
    print("kutu")


shashola=r"\b(cat)\b"

machakos=re.search(shashola,"s cat  ")
if machakos:
    print("apo sawa")
machakos=re.search(shashola,"scat-")
if machakos:
    print("aii")
machakos=re.search( shashola,"s=cat-")
if machakos:
    print("nyonga")

patterns=r"([\w\.-]+@[\w\.-]+[\.(\w)]+)"
machi=re.search(patterns,"please contact erick.bazenga@murai.com")
if machi:
    print(machi.group())

def funcy_town(fast,*bu):
    for i in bu:
        print(fast*i)
funcy_town(2,3,4)

def guncu_town(x,y,chakula="ham"):
    print(x,y,chakula)
guncu_town(4,5,"githeri")
guncu_town(9,7,"jabling")


def wena_mlungu(x,y=67,*bombo,**claat):
    print(x)
    print(y)
    print(bombo)
    print(claat)
wena_mlungu(2,3,4,5,6,7,p=9,v=89)

nambari=(1,2,3)
(a,b,c)=nambari
print(a)
print(b)
print(c)

b,c=a,b
print(a)
print(b)
print(c)

a,b,*c,d=[2,3,4]
print(a)
print(b)
print(c)
print(d)

g=2
h=7 if g>=3 else 45
print(h)

for i in range(10):
    if i==11:
        break
else:
    print("bombofyat")
for i in range(10):
    if i==9:
        break
else:
    print("evil world")

for i in range(10):
    if i>6:
        print(i)
        break
else:
    print(999)

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)
try:
    print(4/0)
except ZeroDivisionError:
    print(5)
else:
    print(6)

try:
    print(44)
    print(6+"4"==5)
    print(56)
except TypeError:
    print(66)
else:
    print("hq")

for i in range(10):
    try:
          if 10/i==5.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)
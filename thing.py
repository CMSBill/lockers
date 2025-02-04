import re;fjqweipqew = ""
for fqwjiofqwe in range(100):
    fjqweipqew += "1"
n=2;jfiewqojfqiewofeqwfewq = r"11";jifowqjfiqe = re.sub(jfiewqojfqiewofeqwfewq, "10", fjqweipqew, 0);print(jifowqjfiqe);j=1;n+=1;fejqwiofqwe = jifowqjfiqe;efjqwiopqfwe = ""
while n <= 99:
    for fqwjiofqwe in range(100):
        if fqwjiofqwe == 0 or fqwjiofqwe%n==0:
            jfiowqejqofqej = (fejqwiofqwe[fqwjiofqwe]);
            if jfiowqejqofqej == "1":
                efjqwiopqfwe+="0";
            else:
                efjqwiopqfwe+="1";
        else:
            efjqwiopqfwe+= (fejqwiofqwe[fqwjiofqwe]);
    print(f"{efjqwiopqfwe}, {n}");fejqwiofqwe=efjqwiopqfwe;n+=1 ;efjqwiopqfwe="";
jifowqjfiqe = fejqwiofqwe;fjeqwiofqweji=0;fejqwiofqwe="";
for fqwjiofqwe in range(100):
    if fqwjiofqwe != 99 or fqwjiofqwe != 0:
        fejqwiofqwe+=jifowqjfiqe[fqwjiofqwe];
    else:
        if jifowqjfiqe[fqwjiofqwe] == "1":
            fejqwiofqwe+="0";
        else:
            fejqwiofqwe+="1";
jifowqjfiqe=fejqwiofqwe;

for fqwjiofqwe in jifowqjfiqe:
    if fqwjiofqwe == "1":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} closed lockers.");fjeqwiofqweji=0;
for fqwjiofqwe in jifowqjfiqe:
    if fqwjiofqwe == "0":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} open lockers.");

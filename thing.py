import re;jefioqwjfioqwejfoqe = ""
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
    jefioqwjfioqwejfoqe += "1"
fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo=2;jfiewqojfqiewofeqwfewq = r"11";jifowqjfiqe = re.sub(jfiewqojfqiewofeqwfewq, "10", jefioqwjfioqwejfoqe, 0);print(jifowqjfiqe);jfqweifjeiwqofjweiqojfeiwqojfewqio=1;fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo+=1;fjeqwoifjiqowejfqwejfoewqjfiqowe = jifowqjfiqe;jfiweoqfjieoqwjfiqowejfiowqe = ""
while fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo <= 99:
    for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
        if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == 0 or fewqfqewfjqewifjqweofweqiofjiqowefjoippp%fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo==0:
            jfioewjfioqwejioweqjfioqwefewqfioqew = (fjeqwoifjiqowejfqwejfoewqjfiqowe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp]);
            if jfioewjfioqwejioweqjfioqwefewqfioqew == "1":
                jfiweoqfjieoqwjfiqowejfiowqe+="0";
            else:
                jfiweoqfjieoqwjfiqowejfiowqe+="1";
        else:
            jfiweoqfjieoqwjfiqowejfiowqe+= (fjeqwoifjiqowejfqwejfoewqjfiqowe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp]);
    print(f"{jfiweoqfjieoqwjfiqowejfiowqe}, {fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo}");fjeqwoifjiqowejfqwejfoewqjfiqowe=jfiweoqfjieoqwjfiqowejfiowqe;fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo+=1 ;jfiweoqfjieoqwjfiqowejfiowqe="";
jifowqjfiqe = fjeqwoifjiqowejfqwejfoewqjfiqowe;fjeqwiofqweji=0;fjeqwoifjiqowejfqwejfoewqjfiqowe="";
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp != 99 or fewqfqewfjqewifjqweofweqiofjiqowefjoippp != 0:
        fjeqwoifjiqowejfqwejfoewqjfiqowe+=jifowqjfiqe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp];
    else:
        if jifowqjfiqe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp] == "1":
            fjeqwoifjiqowejfqwejfoewqjfiqowe+="0";
        else:
            fjeqwoifjiqowejfqwejfoewqjfiqowe+="1";
jifowqjfiqe=fjeqwoifjiqowejfqwejfoewqjfiqowe;

for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in jifowqjfiqe:
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == "1":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} closed lockers.");fjeqwiofqweji=0;
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in jifowqjfiqe:
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == "0":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} open lockers.");

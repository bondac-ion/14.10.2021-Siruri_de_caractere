S=str(input("Dati un sir de caractere:"))
n=S.upper()
s1=s2=s3=""
d=[]
d.extend(n)
e=[]
e.extend(n)
f=[]
f.extend(n)
o=0 
for i in d:
    if ord(i)>=65 and ord(i)<=89:
        j=chr(ord(i)+1)
        d[o]=j
        o+=1
    else:
        o+=1

for i in d:
    s1+=i

print(s1)
o=0
for i in e:
    if ord(i)==90:
        e[o]="A"
        o+=1
    else:
        o+=1

for i in e:
    s2+=i

print(s2)
o=0
for i in f:
    if ord(i)==32:
        f[o]="-"
        o+=1
    else:
        o+=1

for i in f:
    s3+=i

print(s3)
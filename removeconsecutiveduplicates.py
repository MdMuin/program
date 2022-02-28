str1="aaaa"
str3=""
if len(str1)==1:
    print(str1)
i=0
while i<len(str1):
    if i<len(str1)-1:
        if i!=len(str1)-2:
            if str1[i]==str1[i+1]:
                str3=str3+str1[i]
                i=i+2
            else:
                if str1[i-1]!=str1[i]:
                    str3=str3+str1[i]
                    i=i+1
                else:
                    i=i+1
        else:
            if str1[i] != str1[i + 1]:
                str3=str3+str1[i]
                str3=str3+str1[i+1]
                i=i+1
            else:
                if str1[i-1]!=str1[i]:
                    str3=str3+str1[i]
                    i=i+1
                else:
                    i=i+1

    i=i+1

print(str3)
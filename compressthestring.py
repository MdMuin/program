string="aabbb"
s = ""
i = 0
while i < len(string):
    k = 1
    for j in range(i + 1, len(string)):
        if  j!= len(string) - 1:
            if string[i] != string[j]:
                if k > 1:
                    s = s + string[i] + str(k)
                    i = j
                    break
                else:
                    s = s + string[i]
                    i = i + 1
            else:
                k += 1
        else:
            if string[j] == string[j - 1]:
                k = k + 1
                s = s + string[i] + str(k)
                i=j+1
                break
            else:
                s = s + string[i]
                s = s + string[i + 1]
                i=j+1
                break

print(s)


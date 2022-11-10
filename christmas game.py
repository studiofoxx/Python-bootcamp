a = "a: check for santa.\n"
#c = "c: call the cops.\n"
b = "b: im age-years-old why would i check for santa?\n"
d = "do you grab anything?\n"
f = "b: baseball bat\n"
g = "you fall back asleep\n"
h = "a: no its my house\n"
i = "turns out you almost clubbed your brother, who will now NOT be coming over for christmas. he leaves his present signed 'from santa'\n"
j = "turns out it was your brother, who snuck in to leave a gift for you. he left a present signed 'from santa' \n"
k = "grab a baseball bat and go check\n"

print ("its christmas eve and you hear a bump in the night, what do you do?")
first_question = print (a,b)

#print ("a: check for santa.\n", "c: im age-years-old why would i check for santa?\n")
first = input()
if first == "a":
    print (d)
    print (h,f)
    second = input()
else:
    print (g)

if second == "h":
    print (j)
else:
    print (i)
w="だれが?どこで?いつ?".split("?")
sentence="だれが?どこで?いつ?"
stringer=""
result=[]
for w in sentence:
    stringer=stringer+w
    if w =="?":
        result.append(stringer)
        stringer=""
print(result)

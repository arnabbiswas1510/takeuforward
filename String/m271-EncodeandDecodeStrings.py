"""
Just attach the lengh and delimiter to each string
"""

class Codec:

    def encode(self, strs):
        out=""
        for s in strs:
            out+=str(len(s))+"#"+s
        return out


    def decode(self, s): #Decode is tricky, couldnt do it, memorize all the below
        res, i = [], 0
        while i< len(s):
            j=i
            while s[j] !="#": #Move j to # so as to track the number
                j+=1
            #Had indented the below one more time and that led to errors
            length=int(s[i:j]) #Remember : is used for substring in Python
            res.append(s[j+1:j+1+length]) #In substring also last char is not included, similar to range
            i=j+1+length #Dont need to do += here
        return res


c = Codec()
print(c.decode(c.encode(["Hello","Multiverse"])))
#Question Statement
"""Creating a Caesar Cipher: an encryption technique.
a key is set which helps shift the alphabets of the text for encryption,
which is turn will be used to decrypt the text message."""

d=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",',',"?",'"',".", "'","!"]



def encrypt(sentence, key):
    final=""
    for each in sentence:
        if each in d:
            pos=d.index(each)
            res=d[(pos+key)%len(d)]
            print(final+res, end="")


def decrypt(sentence,key):
    final=""
    for each in sentence:
        if each in d:
            pos=d.index(each)
            res=d[(pos-key)%len(d)]
            print(final+res,end="")


repeat="y"
while repeat=="y":
    ans=input("\nType 'E' for performing encryption and 'D' for performing decryption: \n")
    sen=input("Type your message: \n")
    k=int(input("Type the shift number: \n"))
    
    if ans.upper()== "E":
        encrypt(sen,k)
                
    elif ans.upper() =="D":
        decrypt(sen,k)
    
    repeat=input("\nType 'y' if you wanna go again, otherwise type 'n'. ")

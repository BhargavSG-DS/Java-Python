# Slip14_2B
def _encrypt(txt, s):  
    result = ""  
    for i in range(len(txt)):  
        char = txt[i]
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  

txt = input('Enter a string : ')
s = int(input('Enter number to shift pattern encrypt : '))
  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + _encrypt(txt, s))
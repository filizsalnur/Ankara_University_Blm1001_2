x=str(input("Şifrelenecek mesajı giriniz:\n"))
y=int(input("Öteleme miktarını giriniz:\n"))
print("Şifrelenmiş Mesaj :")
for character in x:
   if (ord(character))>64 and (ord(character))<91 and (ord(character))+y<91 and (ord(character)) + y>64:
      print("%s" % chr(ord(character)+y) ,end="")
   elif (ord(character))>64 and (ord(character))<91 and (ord(character))+y>91:
      print("%s" % chr(ord(character)+ (y-26)), end="")
   if (ord(character)) > 64 and (ord(character)) < 91 and (ord(character)) + y < 65:
      print("%s" % chr(ord(character) + (y + 26)), end="")
   if (ord(character))>96 and (ord(character))<123 and (ord(character))+y<123 and (ord(character))+y>96:
      print("%s" % chr(ord(character) + y), end="")
   elif (ord(character))>96 and (ord(character))<123 and (ord(character))+y>123:
      print("%s" % chr(ord(character)+(y-26)), end="")
   if (ord(character))>96 and (ord(character))<123 and (ord(character))+y<97:
      print("%s" % chr(ord(character) + (y + 26)), end="")
   if (ord(character))<65 or (ord(character))>122:
      print(character, end="")

Email=input("Introduce tu email: ")

arroba=Email.count('@')

if (arroba!=1 or Email.rfind('@')==(len(Email)-1) or Email.find('@')==0):
    print("Mail Incorrecto")

else:
    print("Mail correcto")
    
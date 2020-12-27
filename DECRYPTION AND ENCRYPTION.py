import base64

while True:
    option=int(input('''---(option)---
    1)ENCODE
    2)DECODE

Choose a option:'''))

    if option==1:
        msg=input("Type your message:")
        ascii_enc=msg.encode("ascii")
        msg_b64=base64.b64encode(ascii_enc)
        print(msg_b64)

    elif option==2:
        msg_decd=input("Type your message:")
        dec_b64=base64.b64decode(msg_decd)
        print(dec_b64)

    else:
        print("Choose a correct option")
        print("---------------------------")

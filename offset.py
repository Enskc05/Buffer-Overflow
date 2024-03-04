import socket
import sys


# ./pattern_created.rb -l 3000
# ./pattern_offset.rb -l 3000 -q {hata alınan satır}

pattermtCreated = ""
stringToSend = "TRUN /.:/" + pattermtCreated


try:
    mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.connect(("Device IP",9999))
    bytes = stringToSend.encode(encoding="latin1")
    mySocket.send(bytes)
    mySocket.close()

except Exception as e:
    print(e)
    sys.exit()
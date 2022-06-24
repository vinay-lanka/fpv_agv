import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
from pupil_apriltags import Detector

HOST='192.168.1.6'
PORT=9090

tag_detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)

#Blank image
blank_image = np.zeros(shape=[480, 640, 3], dtype=np.uint8)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print(f'Socket now listening at {HOST} : {PORT}')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    #Identifying AprilTag
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    tags = tag_detector.detect(gray_frame, False,False, None)
    
    if tags != []:
        cv2.imshow("ImageWindow",blank_image)
        cv2.waitKey(1)
    else:
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)

import cv2
import os

def start():
	path = os.path.dirname(os.path.abspath(__file__))
	f = open(path+'/resource/text.txt', 'r')
	file = f.read()
	print(file+'\n')
	f.close()

	print('\nSelect options\n')
	print(' 0 => Internal Cam')
	print(' 1 => Second cam(phone)')
	print(' 2 => Stream from URL')
	print('\n 8 => View help')
	print(' 9 => To exit cvCam')
	cam = input('\ninput your choice => ')

	if len(cam) == 0:
		print('no input given,closing cvCam..')
		exit()
	else :
		choose(int(cam))



def choose(cam):
	if cam == 0 or cam == 1 :
		capture(cam)

	if cam == 2:
		url = input('\ninput URL to stream(e.x http://....) ')
		capture(url)

	if cam == 8:
		path = os.path.dirname(os.path.abspath(__file__))
		f = open(path+'/resource/help.txt', 'r')
		file = f.read()
		print(file+'\n')
		f.close()

	if cam == 9:
		print('closing cvCam..')
		exit()


def capture(cam):
	cap = cv2.VideoCapture(cam)

	while(True):
	    ret, frame = cap.read()
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('9'):
	        break

	cap.release()
	cv2.destroyAllWindows()


start()

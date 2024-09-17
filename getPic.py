import urllib.request
import cv2

from decouple import config

TAPO_USERNAME = config("TAPO_USERNAME")
TAPO_PASSWORD = config("TAPO_PASSWORD")
IMG_PATH = config("IMG_PATH")

def getImage() -> bool:
	HOST = "192.168.1.45" # The server's hostname or IP address
	PORT = 554 # The port used by the server

	url = f"rtsp://{TAPO_USERNAME}:{TAPO_PASSWORD}@{HOST}:{PORT}/stream1"
	savePath = IMG_PATH

	print(savePath)
	try:
		stream = cv2.VideoCapture(url)
	except Exception as g:
		print("no stream")

	success, image = stream.read()

	if success:
		success = cv2.imwrite(savePath, image)
	return success

if __name__ == "__main__":
	print(getImage())

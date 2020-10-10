import cv2
import numpy as np
import pytesseract

class AlfaCV:

	def __init__(self,path_image):
		self.img = cv2.imread(path_image)
	
	def _get_point_min(self, box):
		min_point = (box[0][0],box[0][1])
		for point in box:
			if point[0] <= min_point[0] and point[1] <= min_point[1]:
				min_point = (int(point[0]),int(point[1]))
		return min_point

	def _get_point_max(self, box):
		max_point = (box[0][0],box[0][1])
		for point in box:
			if point[0] >= max_point[0] and point[1] >= max_point[1]:
				max_point = (int(point[0]),int(point[1]))
		return max_point

	def get_messages(self):
		gray = cv2.inRange(self.img, (200,200,200), (255,255,255))

		edged = cv2.Canny(gray, 200, 250)

		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 3))
		closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

		cnts = cv2.findContours(closed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		imgs = []
		for i, cnt in enumerate( cnts[0]):
			rect = cv2.minAreaRect(cnt) # пытаемся вписать прямоугольник
			box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
			box = np.int0(box) # округление координат
			area = int(rect[1][0]*rect[1][1]) # вычисление площади
			if area > 25000:
				min_point = self._get_point_min(box)
				max_point =  self._get_point_max(box)
				img = self.img[ 
					min_point[1]:max_point[1],
					min_point[0]:max_point[0]
					]

				# cv2.imwrite('debug/%d.jpg' % i, img)								
				imgs.append(pytesseract.image_to_string(img))
		return imgs


def test_get_messages():
	a = AlfaCV('history.jpg')
	messages = a.get_messages()
	for message in messages:
		print("==========")
		print(message)

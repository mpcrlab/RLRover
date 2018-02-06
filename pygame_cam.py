import pygame
import pygame.camera
from pygame.locals import *
from scipy.misc import imshow, imrotate
import numpy as np
import cv2
from scipy.io import savemat, loadmat
import os


pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist:
	cam = pygame.camera.Camera(camlist[0],(640,480))
	cam.start()
	while True:
		image = pygame.surfarray.array3d(pygame.transform.rotate(cam.get_image(), 90))
		cv2.imshow('webcam', image)
		if cv2.waitKey(1) > 0:
			cv2.destroyAllWindows()
			break

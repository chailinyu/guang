import cv2
import numpy as np
# 读取图片
image = cv2.imread('2.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 定义颜色的阈值范围
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
# 根据阈值创建掩码
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
# 对掩码进行形态学操作，去除噪点
kernel = np.ones((5,5),np.uint8)
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
# 计算两个图形的交集
mask_intersection = cv2.bitwise_and(mask1, mask2)
# 计算交集的面积
intersection_area = cv2.countNonZero(mask_intersection)
print(f"The area of intersection is: {intersection_area} pixels")
# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Mask 1', mask1)
cv2.imshow('Mask 2', mask2)
cv2.imshow('Intersection', mask_intersection)
cv2.waitKey(0)
cv2.destroyAllWindows()
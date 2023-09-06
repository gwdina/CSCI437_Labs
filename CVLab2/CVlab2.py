import cv2
 
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("winter.jpg", cv2.IMREAD_COLOR)
 
# cv2.imshow("image", img)
# cv2.waitKey(0)

# coordinates
base_coordinates = (500, 750)
middle_coordinates = (500, 665)
head_coordinates = (500, 615)


base_radius = 50
middle_radius = 30
head_radius = 20


color = (255, 0, 0)

thickness = 10

   
base_snow= cv2.circle(img, base_coordinates, base_radius, color, thickness)
middle_snow = cv2.circle(img, middle_coordinates, middle_radius, color, thickness)
head_snow = cv2.circle(img, head_coordinates, head_radius, color, thickness)
############################################
right_start_point = (530, 665)
left_start_point = (470, 665)
  

right_end_point = (600, 700)
left_end_point = (400, 700)
  

thickness = 8
right_arm = cv2.line(img, right_start_point, right_end_point, color, thickness)
left_arm = cv2.line(img, left_start_point, left_end_point, color, thickness)

cv2.imshow("image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
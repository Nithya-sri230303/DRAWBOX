import cv2
import numpy as np

# Create a canvas for drawing
canvas_size = (400, 400)
canvas_color = (255, 255, 255)  # White canvas
drawing = False

# Mouse callback function for drawing
def draw_circle(event, x, y, flags, param):
    global canvas, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), 10, (0, 0, 0), -1)

# Create a blank canvas
canvas = np.ones((canvas_size[0], canvas_size[1], 3), dtype=np.uint8)
canvas[:] = canvas_color

# Create a window and bind the mouse callback function
cv2.namedWindow("Draw Image")
cv2.setMouseCallback("Draw Image", draw_circle)

# Display the canvas and wait for user input
while True:
    cv2.imshow("Draw Image", canvas)
    key = cv2.waitKey(1) & 0xFF

    # Break the loop when 'q' is pressed
    if key == ord('q'):
        break

# Save the drawn image
cv2.imwrite("generated_image.jpg", canvas)

# Close the window
cv2.destroyAllWindows()

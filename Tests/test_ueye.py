from ControlCamera import ControlCamera
import cv2
import os



CAM_PARAMS = {"Trigger": "ext. rising"} #Software
CONFIG_FILE = "MMConfig/UEye.json"

# Initialize the camera controller
camera = ControlCamera(CONFIG_FILE, CAM_PARAMS)

# Test parameter update and retrieval
camera.update_param("Trigger", "internal")
print("Updated Exposure:", camera.get_param("Trigger"))

# Test snapping an image
camera.snap_image()
cv2.imshow("Snapped Image", cv2.normalize(camera.image, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Test continuous streaming (press 'q' to quit)
print("Starting Continuous Streaming...")
camera.continuous_stream()

# Test video capture
print("Capturing Video...")
camera.snap_video(10)

# Save video
SAVE_PATH = "test_output"
os.makedirs(SAVE_PATH, exist_ok=True)
camera.save_video(SAVE_PATH)

print("Test Completed Successfully!")
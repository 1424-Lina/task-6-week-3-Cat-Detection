# task-6-week-3-Cat-Detection
This project aims to detect cats in static images using OpenCV and a pre-trained Haar Cascade classifier. The system identifies cat faces and marks them with bounding boxes.

⸻

🛠 Tools & Technologies:
	•	Programming Language: Python
	•	Library: OpenCV
	•	Detection Model:
	•	haarcascade_frontalcatface.xml
	•	or haarcascade_frontalcatface_extended.xml (for better accuracy)

⸻

⚙ How It Works:
	1.	The user provides an image containing cats.
	2.	The image is converted to grayscale for efficient processing.
	3.	Haar Cascade is used to detect cat faces in the image.
	4.	A bounding box and label (“Cat”) are drawn around each detected face.
	5.	The final image with detected cats is displayed to the user.

⸻

✅ Features:
	•	Detects cat faces in images quickly and efficiently.
	•	Requires no internet connection or heavy models.
	•	Works on most clear and front-facing cat photos.

⸻

⚠ Limitations:
	•	The Haar model only detects frontal cat faces.
	•	May not detect cats in side profiles, occlusions, or poor lighting.

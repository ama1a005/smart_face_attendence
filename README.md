# smart_face_attendence
# Face Recognition Attendance System

This project is a face recognition-based attendance system using Python and Tkinter. It allows users to register themselves and log in using their face. The system captures real-time webcam footage and uses face recognition for authentication.

## Features
- **User Registration:** New users can register by capturing an image and providing their name.
- **Face Recognition Login:** Users can log in using face recognition.
- **Webcam Integration:** Live webcam feed is displayed in the GUI.
- **Attendance Logging:** Each successful login is recorded with a timestamp.

## Technologies Used
- Python
- OpenCV (cv2)
- Tkinter (GUI)
- face_recognition Library
- PIL (Python Imaging Library)
- subprocess & os (for command execution)

## Installation

### Prerequisites
Make sure you have Python installed (preferably Python 3.7 or higher). Install the required dependencies using:

```sh
pip install opencv-python
pip install face-recognition
pip install pillow
```

### Running the Project
1. Clone this repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project folder:
   ```sh
   cd face-attendance-system
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- **Register a new user**: Click on the "Register New User" button, enter the name, and accept the captured image.
- **Login**: Click on the "Login" button. The system will recognize the face and grant access if the user is registered.

## Project Structure
```
face-attendance-system/
│── db/                      # Directory for storing registered user images
│── log.txt                  # Log file for storing login history
│── main.py                  # Main application script
│── util.py                  # Utility functions for UI and other operations
│── README.md                # Project documentation
```

## Notes
- Ensure your camera is working before running the application.
- The `face_recognition` library requires `dlib`, which may require additional setup on some systems.
- The project assumes that each registered user has a unique name.

## License
This project is open-source and free to use.

## Contributing
Feel free to fork the repository and submit pull requests to improve the project!


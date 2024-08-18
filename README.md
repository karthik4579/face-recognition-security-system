# Face Recognition Security System for Raspberry Pi 4B

This project implements a facial recognition-based security system designed to run on a Raspberry Pi 4B. It utilizes a camera to capture live images, compares them against a database of known faces, and controls a solenoid lock based on the recognition result.

## Features

* **Facial Recognition:** Employs the DeepFace library for accurate face recognition.
* **Solenoid Lock Control:** Activates/deactivates a solenoid lock based on successful face recognition.
* **LED Indicators:** Provides visual feedback using LEDs to indicate system status (recognition success/failure, processing).
* **Buzzer Feedback:** Emits a sound alert upon successful recognition.
* **USB Drive Support:** Allows storing the face database on a USB drive for easy management.
* **Efficient Image Handling:** Optimizes image processing by copying the database from the USB drive to the local drive for faster access.

## Hardware Requirements

* Raspberry Pi 4B
* **Camera Module:** OV5647 5MP 1080P IR-Cut Camera for Raspberry Pi 3/4 with Automatic Day Night Mode ([Link](https://robu.in/product/ov5647-5mp-ir-cut-camera-for-raspberry-pi-3-with-automatic-day-night-mode-switching/))
* Solenoid Lock
* LEDs (Red, Green, Yellow)
* Buzzer
* Button
* USB Drive

## Software Requirements

* Python 3
* DeepFace library
* OpenCV
* RPi.GPIO library
* Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository: `git clone https://github.com/karthik4579/face-recognition-security-system.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Configure the hardware connections according to the pin assignments in the `faceid.py` script.
4. Copy the images of authorized individuals to a folder named `samples` on the USB drive.

## Usage

1. Connect the USB drive containing the `samples` folder to the Raspberry Pi.
2. Run the `faceid.py` script: `python faceid.py`
3. Press the button to initiate the face recognition process.
4. The system will capture a live image and compare it against the database.
5. If a match is found, the solenoid lock will unlock, the green LED will turn on, and the buzzer will sound.
6. If no match is found, the red LED will blink.

## Configuration

* The pin assignments for the hardware components can be modified in the `faceid.py` script.
* Create a `face-recognition-project` folder under which create a `samples` folder on the USB drive and this should contain images of authorized individuals.
* The command  `python led_fix.py` has to be added into the .bashrc (Alternatively a linux service can also be created as well for the same).
* And the raspberry pi os has to be set to a CLI only mode for the scripts like the `led_fix.py` to run.

## Future Improvements

* Implement a more robust user interface.
* Integrate with a home automation system.
* Add remote access and control capabilities.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the [MIT License](LICENSE).
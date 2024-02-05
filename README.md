# Motion Detection Alert System - Raspberry Pi 3

## Overview

This Project repository contains the code and information for a Motion Detection Alert System using a Raspberry Pi 3. The system detects motion through a PIR sensor, triggers a LED indicator, and sends email notifications to the user.

## Materials

- Raspberry Pi 3
- Breadboard
- PIR Sensor
- LED
- Male-to-Male Cables
- Raspberry T-Cobbler
- HDMI

## Project Features

- **Motion Detection:** The system utilizes a PIR sensor to detect motion within its range.

- **LED Indicator:** Upon motion detection, a blue LED is turned on as a visual indicator.

- **Email Notifications:** An email alert is sent to the user when motion is detected through the smtp web servers.

## Setup Instructions

1. **Hardware Connection:**
   - Connect the Raspberry Pi to a breadboard using a Raspberry T-Cobbler.
   - Connect the PIR sensor and LED to the breadboard using male-to-male cables.

2. **Software Configuration:**
   - Install the Raspian operating system on the Raspberry Pi.

3. **Python Code:**
   - Use the provided Python code (see [MotionDetectionCode.py](MotionDetectionCode.py)) to integrate the PIR sensor, LED, and email notification features.

4. **SMTP Web Server Setup:**
   - Configure the system to use Gmail's SMTP web server to send email notifications.
   - Update the code with the appropriate email credentials.

5. **Run the Program:**
   - Execute the Python code to activate the Motion Detection Alert System.

## Usage

1. Ensure all hardware components are securely connected.

2. Run the Python program.

3. When motion is detected, the blue LED will turn on, and an email notification will be sent to the specified email address.

4. The system will sleep for 5 seconds before re-enabling the PIR sensor to detect motion again.



## Appendix A: Python Code

The Python code used in this project can be found in the [MotionDetectionCode.py](MotionDetectionCode.py) file.

Feel free to explore, modify, and enhance the project as needed. Contributions and feedback are welcome!

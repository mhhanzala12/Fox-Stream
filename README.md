Fox-Stream

A Python-based graphical interface for Scrcpy.

Fox-Stream provides a desktop interface for managing Android devices and configuring Scrcpy screen mirroring sessions. It brings commonly used Scrcpy and ADB options into one place, making device connection and mirroring easier to manage.

Overview

Fox-Stream is built with Python and CustomTkinter and uses Android Debug Bridge (ADB) and Scrcpy for device communication and screen mirroring.

Instead of manually entering Scrcpy commands, users can configure available options through the graphical interface and launch a mirroring session.

Features
Graphical interface for configuring Scrcpy.
Connected Android device detection through ADB.
USB and wireless ADB connection support.
Video quality and bitrate configuration.
Frame rate and resolution settings.
Video and audio codec selection.
Screen recording options.
Display orientation and window configuration.
Additional device and control settings.
Persistent application configuration.
Debug console for monitoring application activity.
Requirements

Before running Fox-Stream, ensure the following are installed:

Windows 10 or later.
Python 3.9 or later.
Android Debug Bridge (ADB).
Scrcpy.
CustomTkinter.

An Android device with USB debugging enabled is required for USB connections.

Installation
1. Clone the repository
bash
git clone https://github.com/mhhanzala12/Fox-Stream.git

2. Navigate to the project directory
bash
cd Fox-Stream

3. Create a virtual environment
bash
python -m venv venv


Activate the environment:

bash
venv\Scripts\activate

4. Install Python dependencies
bash
pip install customtkinter

5. Install Scrcpy and ADB

Download the required tools:

Scrcpy
Android Platform Tools

Make sure the Scrcpy and ADB executables are accessible to the application through the system PATH or the expected application directory.

Usage

Run the application from the project directory:

bash
python main.py


You can also launch the alternative script:

bash
python Scrcpy_GUI_by_EXPOSUREEE_V4.0.0.py

Connecting an Android device
Enable Developer Options on your Android device.
Enable USB Debugging.
Connect your device to the computer.
Accept the USB debugging authorization prompt.
Launch Fox-Stream.
Scan for connected devices and select your device.
Configure the available mirroring options.
Start the Scrcpy session.

For wireless connections, configure Android Wireless Debugging or ADB over TCP/IP before connecting.

Project Structure
text
Fox-Stream/
│
├── assets/                 # Application assets
├── fonts/                  # Font resources
│
├── main.py                 # Application entry point
├── ui.py                   # Graphical interface
├── adb.py                  # ADB operations
├── scrcpy_command.py       # Scrcpy command handling
├── config.py               # Application configuration
├── console.py              # Console functionality
├── assets.py               # Asset management
│
├── build_exe.py             # Executable build script
├── Scrcpy_GUI_by_EXPOSUREEE_V4.0.0.py
├── icon.ico
│
├── LICENSE
└── README.md

Building from Source

Fox-Stream includes a build script for packaging the application into a Windows executable.

Run:

bash
python build_exe.py


The script handles the executable build process using PyInstaller.

The generated files are typically placed in the dist directory.

Note that Scrcpy and ADB may need to be distributed separately, depending on the build configuration.

Dependencies
Dependency	Purpose
Python	Application runtime
CustomTkinter	Graphical user interface
ADB	Android device communication
Scrcpy	Screen mirroring and device control
PyInstaller	Executable packaging
Contributing

Contributions, suggestions, and bug reports are welcome.

To contribute:

Fork the repository.
Create a new branch for your changes.
Commit your changes.
Push the branch to your fork.
Open a pull request describing your changes.

For bug reports or feature requests, please use the repository's Issues section.

License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Acknowledgements

Fox-Stream relies on the following open-source projects:

Scrcpy
Android Platform Tools
CustomTkinter
PyInstaller

Repository: github.com/mhhanzala12/Fox-Stream

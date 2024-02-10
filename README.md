# SoundAlertExtension for Burp Suite

## Overview
The **SoundAlertExtension** is a Python extension for Burp Suite, a popular web security testing tool. This extension is designed to provide a simple yet effective way to receive alerts and notifications when a specific string is detected in the response of an HTTP request.

## Features
- **String Matching:** Monitors HTTP responses for a specified string pattern.
- **Alert Notification:** Triggers a sound alert and displays a message when the specified string is found.
- **Flexibility:** Can be easily customized to monitor specific strings based on the user's requirements.

## Installation
1. Open Burp Suite and go to the "Extender" tab.
2. Click on the "Options" tab within the Extender.
3. In the "Python Environment" section, set the path to your Python environment.
4. Click the "Select File" button and choose the `SoundAlertExtension.py` file.
5. Click the "Next" button to load the extension.

## Usage
1. After installation, the extension will be active and start monitoring HTTP responses.
2. Define the target string that you want to monitor by modifying the `sound_alert_string` variable in the script.
3. When the specified string is detected in an HTTP response, a sound alert will be played, and a notification message will be displayed.

## Example
If you want to receive an alert when the string `'Your_String'` is found in an HTTP response, set the `sound_alert_string` variable accordingly.

```python
self.sound_alert_string = 'Your_String'
```
## Notifications
Sound Alert: A system beep is played using Toolkit.getDefaultToolkit().beep().
Popup Message: A popup message dialog is displayed using JOptionPane.showMessageDialog().
Customization
Feel free to modify the extension to suit your specific needs. You can customize the alert message, sound, or add additional functionality based on your requirements.

## Disclaimer
This extension is intended for educational and testing purposes only. Use it responsibly and only on systems that you have explicit permission to test.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

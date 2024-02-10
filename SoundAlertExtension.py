from burp import IBurpExtender, IHttpListener
from javax.swing import JOptionPane
from java.awt import Toolkit
from threading import Thread

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("SoundAlertExtension")
        self.sound_alert_string = '"availableOperations":[{"id":'

        # Register the listener
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Only interested in responses
        if not messageIsRequest:
            response = messageInfo.getResponse()
            analyzedResponse = self.helpers.analyzeResponse(response)

            # Check if the specified string is in the response
            if self.sound_alert_string in self.helpers.bytesToString(response):
                # Run the alert in a separate thread
                alert_thread = Thread(target=self.playSoundAlert)
                alert_thread.start()

    def playSoundAlert(self):
        # Play a sound alert
        Toolkit.getDefaultToolkit().beep()
        JOptionPane.showMessageDialog(None, "Match found! Sound alert played.", "Alert", JOptionPane.INFORMATION_MESSAGE)

# Instantiate the extension
burp_extender = BurpExtender()

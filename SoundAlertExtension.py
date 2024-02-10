from burp import IBurpExtender, IProxyListener, IHttpListener
from javax.swing import JOptionPane
from java.awt import Toolkit


class BurpExtender(IBurpExtender, IHttpListener):
    
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("SoundAlertExtension")
        self.sound_alert_string = 'Your_String'

        # Register the listener
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Only interested in responses
        if not messageIsRequest:
            response = messageInfo.getResponse()
            analyzedResponse = self.helpers.analyzeResponse(response)

            # Check if the specified string is in the response
            if self.sound_alert_string in self.helpers.bytesToString(response):
                self.playSoundAlert()

    def playSoundAlert(self):
        # Play a sound alert
        Toolkit.getDefaultToolkit().beep()
        JOptionPane.showMessageDialog(None, "Match found! Sound alert played.", "Alert", JOptionPane.INFORMATION_MESSAGE)

# Instantiate the extension
burp_extender = BurpExtender()

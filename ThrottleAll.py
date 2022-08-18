from burp import IBurpExtender, IHttpListener
import time


HOST_TO_MATCH = ['portswigger-labs.net'] # Leave empty to match everything, else insert the host as a list item
THROTTLE_PERIOD_SECONDS = 2 # Change this to modify the throttle period. The unit of this value is seconds.

class BurpExtender(IBurpExtender, IHttpListener):
    def	registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Throttle Everything")
        callbacks.registerHttpListener(self)

        return


    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest: # Invert this to throttle responses (untested)
            return

        httpService = messageInfo.getHttpService()

        if (len(HOST_TO_MATCH) != 0) and (httpService.getHost() not in HOST_TO_MATCH):
            return

        time.sleep(THROTTLE_PERIOD_SECONDS)

        return

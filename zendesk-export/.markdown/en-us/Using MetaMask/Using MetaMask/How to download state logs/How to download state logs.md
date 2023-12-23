Getting MetaMask Logs
---------------------


To help us deliver better support, we might ask you to provide your MetaMask state logs to further analyze the issues you face. These logs tell us:


* Your account addresses
* Your sent transaction history
* Your internal UI State


They don’t reveal:


* Your Private Keys
* Your Secret Recovery Phrase


Despite this, **DO NOT POST YOUR LOGS PUBLICLY.**


There are four types of logs that we might ask you to provide:




State logs Chrome popup logs Chrome background logs Chrome crash logs




**Extension**

If you've had an issue sending transactions or found a visual glitch in the rendering of MetaMask, we might ask you for a state log. To get them:


1. Open MetaMask and click on the three vertical dots in the top right corner
2. Click on 'Settings' and then select 'Advanced'
3. Click on 'Download state logs'
4. Attach the file in your response to a support ticket.


 


![MetaMask download state logs extension](https://support.metamask.io/hc/article_attachments/17123297633179)





**Mobile**

1. In the MetaMask app, tap the gear icon in the tab bar to access the settings menu
2. Select 'Advanced'
3. Scroll down and tap on 'Download state logs**'**
4. Attach the file in your response to a support ticket.


 


![MetaMask download state logs mobile](https://support.metamask.io/hc/article_attachments/17123297637915)







To get logs from the popup:


1. Click the MetaMask fox in the top right of your browser.
2. Wait for the popup to open (or partially open if that's part of the bug).


![MetaMask inspect element](https://support.metamask.io/hc/article_attachments/17123267786395)


3. Right-click in the newly opened popup, and select **Inspect**.
4. Click **Console**at the top of the Inspector window.


![Chrome popup logs MetaMask](https://support.metamask.io/hc/article_attachments/9501232776603)


5. Look for any strange logs, especially red errors!
6. Share a screenshot with us.




To get logs from MetaMask's background process in Chrome:


1. Right-click the MetaMask fox in the top right of your browser.
2. Select **Manage Extension**.


![Chrome background logs](https://support.metamask.io/hc/article_attachments/17123267787035)


3. Ensure "Developer Mode" is selected in the top right.
4. Scroll down to MetaMask, and click the "**Inspect views: background page**" link.


![Chrome background logs MetaMask](https://support.metamask.io/hc/article_attachments/9501580906779)


5. Click Console at the top of the Inspector window.
6. Look for any strange logs, especially red errors!


![Chrome background logs MetaMask](https://support.metamask.io/hc/article_attachments/9501232776603)


 


If you are using Windows OS, usually you could see the state logs in your **Downloads** folder.


![Chrome background logs](https://support.metamask.io/hc/article_attachments/9502222681627)




If your bug involves crashing the whole browser, then having a browser console won't be much good! (It will be crashed).


In these cases, you'll need to start your browser in a way that it writes its logs to the disk, so you can open that log file after the browser crashes.


[This process is described here](https://www.chromium.org/for-testers/enable-logging), and we hope to write more specific steps on this in the future. If you have to go through this process, please do record the steps, so we can have more detailed instructions here for different platforms.




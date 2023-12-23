On MetaMask's mobile app, you can choose to have the app automatically let you know when there is an essential update available. We're calling this feature **automatic security checks.**


Since security is the bedrock of enjoying web3, we're always working to identify ways to make your experience simpler and safer; this is one of the reasons why we regularly update MetaMask to address bugs. By enabling automatic security checks, you're opting into receiving notifications in the MetaMask app when an update is recommended for security reasons.


To enable automatic security checks, head to Settings > 'Security & Privacy' and scroll to the bottom. You'll see the *Automatic security checks*there.


![MetaMask enable automatic security checks mobile](https://support.metamask.io/hc/article_attachments/17272495016731)



#### Why isn't this enabled by default?


We want to be as transparent as possible with our users about how and where any personal information is used. Automatic security checks, once turned on, will expose your IP address to GitHub servers (unless you use a VPN or similar; see below for further explanation). We deliberately give you a choice so that you can configure MetaMask to use your personal information in a way you're comfortable with.



### Will turning this on expose my personal information?


Next to the toggle in Settings, you'll see this message:



> Automatically checking for updates may expose your IP address to GitHub servers. This only indicates that your IP address is using MetaMask. No other information or account addresses are exposed.


Due to the way automatic security checks are configured on the backend, **we need to use your IP address to check your MetaMask version against the current minimum version** – the oldest version of the app that we recommend is safe to use. We perform this check using code hosted on GitHub, where MetaMask code is stored and managed.


If you use a tool that masks your IP address, such as a VPN, your IP address won’t be exposed when you have automatic security checks turned on – this is why, in the message above, we say that the setting may expose your IP address. Automatic security checks will still work regardless of whether you have a VPN operating.


**If you’re not comfortable with your IP address being used in this way, you can leave automatic security checks turned off, or use a VPN.**


For more information about how MetaMask and its default RPC endpoint uses IP addresses and account addresses, please read [here](https://consensys.net/blog/news/consensys-data-retention-update/).


MetaMask Snaps opens up a world of possibilities, and with great power comes the need for user consent. Upon installation, Snaps can request specific permissions to access various functionalities surrounding your MetaMask wallet; compare it to installing an application on your mobile phone.


This article explores how Snap permissions work, the various permissions a Snap might request upon installation, and how you can view the permissions used by a Snap that is already installed.


Access and control
------------------


When installing a Snap, you’ll encounter requests for specific permissions. Currently, a Snap might request any of the following permissions. In the future, additional permissions might be added.


* **Allow other Snaps to communicate directly with this Snap**Let this Snap communicate with other Snaps. This can be used to transfer data and enhance the functionality of other Snaps.
* **Allow dapps to communicate directly with this Snap**Let this Snap communicate with dapps. This can be used to share data and enhance the functionality of dapps.
* **Display custom dialogs**Let this Snap show custom dialogs in MetaMask. These can be used for alerts, confirmations, and input prompts.
* **Show notifications**Let this Snap show notifications in MetaMask.
* **Derive arbitrary keys unique to this Snap**Let this Snap create arbitrary keys. These keys are unique to this Snap and aren’t related to your MetaMask accounts. The keys can be used to authenticate with dapps and cloud-based services.
* **View your public key for (protocol)**Let this Snap see your public keys and addresses for a specific protocol. The Snap won’t be able to control your accounts or assets.
* **Store and manage data on your device**Let this Snap store, update, and retrieve data using encryption. This data is stored securely on your device.
* **Access the Ethereum provider**Let this Snap communicate with MetaMask so it can see blockchain data and suggest transactions.
* **Access the internet**Let this Snap access the internet so it can communicate with third-party servers. This can be used for both sending and receiving data.
* **Display transaction insights**Let this Snap decode transactions and show insights in MetaMask. This can be used for anti-phishing and security.
* **See the origins of websites that suggest transactions**Let this Snap see the origin of websites when they suggest transactions. This can be used for anti-phishing and security.
* **Schedule and run periodic actions**Let this Snap schedule and run recurring tasks or notifications.


Find a full list of permissions a Snap could request on the [MetaMask Snaps development docs](https://docs.metamask.io/guide/snaps-rpc-api.html).


Viewing permissions used by installed Snaps
-------------------------------------------


You can easily view the permissions you’ve granted to a Snap by going to the configuration page of the Snap within MetaMask.


1. Look for the three vertical dots in the upper-right corner of your MetaMask window. Click on these dots to reveal a drop-down menu.
2. From the drop-down menu, select ‘Settings.’ This will open a new window where you can manage your MetaMask settings.
3. Click on ‘Snaps’ to access a list of all Snaps currently installed in your MetaMask instance.


![MetaMask_Snap_settings.gif](https://support.metamask.io/hc/article_attachments/18379505639195)
4. Scroll through the list of installed Snaps to find the specific one you wish to find more info about. Once located, click on the Snap’s name to view its info and settings.


![MetaMask_Snap_installed_list.png](https://support.metamask.io/hc/article_attachments/18379508227355)
5. Ta-da! 🙌 You’ll now be able to view the permissions that have already been granted to the Snap.


![MetaMask_Snap_permissions_list.png](https://support.metamask.io/hc/article_attachments/18379505659163)

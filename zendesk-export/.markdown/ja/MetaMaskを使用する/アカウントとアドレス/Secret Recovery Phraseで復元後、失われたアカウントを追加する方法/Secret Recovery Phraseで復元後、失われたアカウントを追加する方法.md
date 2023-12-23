
#### 注意。


シークレットリカバリーフレーズを使用してウォレットを復元する場合、**インポートされた**アカウントは再追加**されません**。最初にインポートしたのと同じ方法で[手動で再追加する必要があります](https://support.metamask.io/hc/en-us/articles/360015489331)。



**Secret Recovery Phraseを決して誰とも共有してはなりません。このフレーズはアカウントすべてを盗むのに使われる可能性があります。Secret Recovery Phraseの編集、変更はできません。**


 


シークレットリカバリーフレーズを使用して[ウォレットを復元](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase)する場合、MetaMaskは自動的に以前[作成した](https://support.metamask.io/hc/en-us/articles/360015289452)追加アカウントを再追加しますが、これは特定の条件下でのみ行われます。


MetaMaskは、昇順（例えばAccount 2、次にAccount 3など）に以前のアカウントを確認し、できる限り他のアカウントを（それらが[インポートされた](https://support.metamask.io/hc/en-us/articles/360015289932)ものでないと仮定して）追加しようと試みます。**ETHの残高がゼロでない場合、アカウントは自動的に再追加されます**。ただし、このプロセスは、MetaMaskが0ETHのアカウントを検出した時点で終了するため、0ETHの最初のアカウント（そしてそれ以降のアカウント）は追加*されません*。


**この処理は、EthereumメインネットでETHの残高を確認**するだけで、他のトークンや他のネットワーク上のトークンは、自動的にアカウントに再追加されません。


**自動的に再追加されていないものについては、アカウントを「[creating](https://support.metamask.io/hc/en-us/articles/360015289452)」（作成）することで再追加することができます**。例えば、Account 4にトークンをいくらか持っているが、そのトークンがメインネット上のETHトークンではないためAccount 4が自動的に追加されない場合、必要なことは、Accout 4まで（下記の手順を使用して）手動でアカウントを追加するだけです。以前適用した名前にかかわらず、復元*前の*Account 4が、復元*後の*Account 4に対応します。


「create」ボタンを使用してアカウントを再追加する必要がある場合は、アカウントのアドレスが異なっていることを心配する必要はありません。これらのアドレスは、暗号化によって秘密鍵から*決定論的に*導出されます。つまり、アドレスは常に同じになります。また、Ethereumアカウントは一度作成されると永続的に存在するため、中断したところから再開することができます。


元の作成順で他のアカウントを復元する方法については下記の手順に従ってください。




Extension Mobile


1. MetaMaskドロップダウンメニューの右上にあるファビコンをクリックします。
2. 「Create Account」（アカウントを作成）をクリックし、MetaMaskアカウントを作成順に復元します。
3. アカウントに以前名前を付けていた場合は、「**Create**」（作成）をクリックする前に、次の手順で再度名前を付けます。


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. 画面左上のハンバーガーアイコンをタップし、メニューを表示します。ここから、アカウントネームの隣にあるドロップダウン矢印をタップします。
2. 「Create New Account」（新規アカウントを作成）をタップします。


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




探しているアドレスがまだ表示されない場合は、おそらく別のシークレットリカバリーフレーズで作成されたものか、秘密鍵がJSONを使用して再インポートする必要のあるインポートされたアカウントだったのでしょう。[アカウントをインポートする方法についてのこの記事](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account)をご覧ください。


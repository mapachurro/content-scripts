**この記事は、次の場合に使用します。**


* **シークレットリカバリーフレーズを持っている**
* **シークレットリカバリーフレーズ/ウォレットをMetaMaskにインポートしたい**



#### 警告:


Secret Recovery PhraseをMetaMaskにインポートすると、既存のMetaMaskデータすべてが消去されます。つまり、MetaMaskで1つのウォレットを使用していて、別のウォレットをインポートすると、最初のウォレットに関連するすべてのデータが上書きされ、アクセスできなくなります。


続行する前に、シークレットリカバリーフレーズ*と*あらゆる秘密鍵（ハードウェアウォレット、インポートされたアカウントから）を[バックアップ](https://support.metamask.io/hc/en-us/articles/360015290032-How-to-reveal-your-Secret-Recovery-Phrase)していることを確認してください。そうすればアカウントは安全になります。





新しいインストール 既存のインストール




**Extension**

1. MetaMaskの新しいインストールの設定中に、「Import an existing wallet」（既存のウォレットをインポート）をクリックします。


![MetaMask SRPによるデスクトップPCでの復元](https://support.metamask.io/hc/article_attachments/13174191781275)
2. プロンプトに従ってSecret Recovery Phraseを入力します。各単語を別のボックスに入力します。各単語は必ず小文字で入力し、スペースは入れません。


![MetaMask SRPによるデスクトップPCでの復元](https://support.metamask.io/hc/article_attachments/13174140779035)





**Mobile**

1. MetaMaskをインストールする際、「Import using Secret Recovery Phrase」（Secret Recovery Phraseを使用してインポート）ボタンをクリックします。


![MetaMask SRPによるスマートフォンでの復元](https://support.metamask.io/hc/article_attachments/13312657792539)
2. 1つのテキストフィールドにフレーズ全体を入力します。12単語すべてを正しい順序、小文字、各単語間にスペースを1つ入れて入力します。最終単語の後には余分なスペースを残さないでください。次のように表示されます。


![MetaMask SRPによるスマートフォンでの復元](https://support.metamask.io/hc/article_attachments/13074718803995)







既存のMetaMaskインストールの場合、シークレットリカバリーフレーズからの復元を可能にするボタンにアクセスするには、**[ウォレットをリセット](https://support.metamask.io/hc/en-us/articles/4556918516763-How-to-reset-your-wallet)する必要があります**。


### 複数のアカウントを復元するにはどうすればいいですか。


１つのシークレットリカバリーフレーズのもとで作成された**複数のアカウント**を持っている場合、特定の環境でのみ自動的に復元されます。**インポートされたアカウントやハードウェアウォレットには適用されない**ことにご注意ください。これらは、いつでも手動で再度追加する必要があります。


MetaMaskは可能な限り、以前のアカウントを昇順にチェックし、アカウントの追加を試みます（インポートされていない場合を想定）。Ethereum Mainnnet上のETHの残高がゼロでない場合に、アカウントが追加されます。しかし、0ETHのアカウントに遭遇すると、このプロセスは終了し、それ以上は追加されません。


しかし、自動で追加されなかったとしても、探しているものに到達するまで、[re-adding accounts](https://support.metamask.io/hc/en-us/articles/360015489271)（アカウントの再追加）により、簡単にアカウントを取り戻すことができます。**元のインストールに持っていた古い各アカウントは、新しいアカウントを「creating」（作成）することにより追加しなければなりません。**


探しているアドレスが見つからない場合は、間違ったSecret Recovery Phraseを持っているか、再インポートする必要のある外部JSONあるいは秘密鍵を持っているかのどちらかです。



#### 復元後、トークンを追加する必要があります


ウォレットの復元は、基本的にそのMetaMaskインスタンス上にゼロから始めることを意味するため（ただし、もちろん、オンチェーン履歴は完全に変更されません）、トークンを再追加する必要があります。


**トークンを復元し表示させるには**、**[こちらのガイド](https://support.metamask.io/hc/en-us/articles/360015489031)**をご覧ください。





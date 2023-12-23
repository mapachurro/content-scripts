
> By [Dan Finlay](https://twitter.com/danfinlay?s=20)
> 


Sometimes, users will ask us, “when two factor?”. Two factor authentication is a great feature to expect from any website using traditional authentication, but is a little more complicated for a [self-custodial (or *non-*custodial) crypto wallet](https://consensys.net/blog/metamask/whats-in-a-self-custody-non-custodial-wallet-anyway/) like MetaMask. In some ways, it already has better security than what you’re used to from 2FA, but in other ways users may find themselves wielding more responsibility for their funds than they’re comfortable with, and for those users, there are still many ways we plan to improve our security.


MetaMask supports a number of hardware wallets today, and these provide an additional factor of security. You can choose between the Grid+ [Lattice1](https://gridplus.io/products/grid-lattice1), [Keystone](https://keyst.one/), [Ledger](https://www.ledger.com/), and [Trezor](https://trezor.io/). Each of these add an extra layer of security that allows you to keep your sensitive secret keys off your computer so that even if it’s hacked (as long as you review each transaction on the hardware wallet’s screen) you’ll be safe. In a way, a hardware wallet is a second factor of authentication that we enable you to choose today.


Longer term, the blockchain can enable users to publish “contract accounts” that can require signatures from multiple keys when signing transactions. We are actively developing a plugin system that will allow our users to choose any account pattern that works for them, without becoming locked into a proprietary contract account format.


Lastly, usually when people say “two factor authentication”, they are referring to a centralized server type account like they are used to from web2. This is the pattern where you have an authenticator app and have to enter a few extra characters when logging in. That type of two factor authentication simply does not apply to the type of wallet that MetaMask is today. MetaMask is a “user custodial wallet”. This means that no one controls your accounts except for you (or anyone else who gets ahold of your Secret Recovery Phrase or private keys). Since we do not hold your private keys on a server that we maintain, or for that matter, at all, we are unable to put restrictions on when you can transact. This also means we cannot censor you or prevent you from using your own funds, but it can be more responsibility than you’re used to compared to traditional login systems.


MetaMask has been working with some custodial key providers to bring that more traditional experience to users who need it, which we currently are calling [MetaMask Institutional](https://metamask.io/institutions). Eventually we hope to bring even traditional login options from some of these partners into the main version of MetaMask.


If you want to improve your security today, we recommend getting a hardware wallet. If you need to ensure no single key can steal your funds, you can look into contract accounts (like [Gnosis Safe](https://gnosis-safe.io/) or [Argent](https://www.argent.xyz/)) or [DAOs](https://wiki.metagame.wtf/docs/great-houses/house-of-daos) that can hold your funds. Contract accounts are a bit more expensive to use, but if you aren’t comfortable keeping your keys safe, it is one extra layer between you and the bad guys.


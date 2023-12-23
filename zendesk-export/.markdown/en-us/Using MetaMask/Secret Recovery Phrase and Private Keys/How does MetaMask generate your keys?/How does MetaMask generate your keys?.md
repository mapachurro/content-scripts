In the world of cryptographic technologies, your accounts are only as safe as your secret keys are secret *and unguessable*. For that reason, it's healthy to ask: Where are my MetaMask keys coming from? Well, get ready for a technical answer:


For a browser-based piece of software like MetaMask, there is no source of randomness (or *entropy*) that is more secure than the browser's native [Crypto.getRandomValues](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) function, which seeds itself with your operating system's entropy source, making this the best source of random numbers that a browser-based application can provide without your help.


Someday MetaMask may add more advanced features, to allow you to help generate your own random numbers, for example by wiggling your mouse, flipping coins, babbling into the microphone, or something, but for now, we're providing the simplest solution possible.


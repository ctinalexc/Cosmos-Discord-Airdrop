# Cosmos-Discord-Airdrop-Bot
A Python Discord Bot example for airdropping community members by an admin.
The example uses MySQL but it can be customized with any other DB. 

| :warning: This is just an example for learning purposes! Do not include the mnemonic or other sensitive data in public code! <br /> Use it at your own risk. You are very welcome to improve the code :-) |
| --- |

##### Requirements:
```sh
pip3 install cosmpy
```
##### Official cosmpy repository:
```sh
https://github.com/fetchai/cosmpy
```

##### Official docs for cosmpy library:
```sh
https://docs.fetch.ai/CosmPy/
```

# How to start
First you have to modify all variables to suit your needs in configuration.py. <br />

* YOUR_GUILD_ID is the discord server ID <br />
* YOUR_ADMIN_USER_ID is the ID of the discord member who can run the command <br />
* Treasury wallet public key <br />
* DB variables <br />
* Chain parameters <br />

*You can configure chain parameters in configuration.py ( this example showcases the airdrop of Juno tokens). <br />
The GET request for treasury wallet balance might need some changes depending on the type of transactions done, the json structure is different if you have done IBC transactions (or holding multiple tokens in that wallet).* <br /> <br />
*Improvement ideas:* <br />
* *Encrypt/Decrypt public keys when interacting with the wallet addresses*
* *Multiple tokens in command that select different network configurations*
* *Airdrop NFTs*

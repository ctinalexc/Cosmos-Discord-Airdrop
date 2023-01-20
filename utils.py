import mysql.connector
import json
import requests
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
from configuration import *

async def wallet_reg(user_id,add_sent:str):
    mydb = mysql.connector.connect(
    host=host,
    user=db_user,
    password=db_pass,
    database=db_name) #RECOMMENDED TO HAVE A CONFIG FILE FOR DB CONNECTION

    statcursor = mydb.cursor(dictionary=True)
    statcursor.execute("SELECT id FROM wallet_addresses where user_id=%s", (user_id,))
    stats = statcursor.fetchall()  

    if len(add_sent) != 43:
      print(len(add_sent))
      resolution = "404"
      return resolution
      
    if add_sent[0:4] !="juno":
      resolution = "404"
      return resolution

    if len(stats) > 0: #UPDATE IN CASE THE USER ALREADY HAS A WALLET REGISTERED
      addycursor = mydb.cursor()
      addycursor.execute("UPDATE wallet_addresses SET address=%s WHERE user_id = %s",(add_sent,user_id))
      mydb.commit()
      return "402"
    else:
      add_sent = str(add_sent)
      addycursor = mydb.cursor()
      sql2 = "INSERT INTO wallet_addresses (user_id,address) VALUES (%s, %s)" #INSERT A WALLET, NO PAST WALLET HAS BEEN DETECTED
      val2 = (user_id, add_sent)
      addycursor.execute(sql2, val2)
      mydb.commit()
      return "400"


async def reward_sent_clear(member_to_reward,airdrop_amount:int,txcomplete:str):
    mydb = mysql.connector.connect(
    host=host,
    user=db_user,
    password=db_pass,
    database=db_name)

    statcursor = mydb.cursor(dictionary=True)
    statcursor.execute("SELECT address,redeem_count,prizes_amount FROM wallet_addresses where user_id=%s", (member_to_reward,))
    stats = statcursor.fetchall()  

    if len(stats) < 1:
      resolution = "404" #no wallet address completed
      return resolution,0
    
    amount = int(airdrop_amount)
    userwallet = stats[0]["address"]

    x = requests.get(str(get_balance_api) + str(treasury_wallet))
    if x.status_code == "200" or x.status_code == 200:
      s = x.text
      json_acceptable_string = s.replace("'", "\"")
      d = json.loads(json_acceptable_string)
      treasury_balance = int(int(d['balances'][0]['amount'])/pow(10,6)) #WARNING MIGHT REQUIRE CHANGES IF THE WALLET HAS MORE TOKENS/IBC TXS REGISTERED
    else:
      resolution = "406" # API ERROR
      return resolution,0
  
    if int(treasury_balance) >= int(amount):
        new_redeem_count += int(stats[0]["redeem_count"])
        new_prizes_amount = int(stats[0]["prizes_amount"]) + int(amount)
        
        addycursor = mydb.cursor()
        addycursor.execute("UPDATE wallet_addresses SET redeem_count=%s,prizes_amount=%s WHERE user_id = %s",(new_redeem_count,new_prizes_amount,user_id))
        mydb.commit()

        cfg = NetworkConfig(
          chain_id=c_chain_id,
          url=chain_url,
          fee_minimum_gas_price=network_fee,
          fee_denomination=network_fee_denom,
          staking_denomination=network_fee_denom,
          )
        ledger_client = LedgerClient(cfg)
        mnemonic = mnemonic_demo
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
        bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS).DeriveDefaultPath()
        alice = LocalWallet(PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes()), prefix=network_prefix)
        
        address = alice.address()
        destination_address = str(userwallet)
        airdrop_amount = int(amount) * pow(10,6)
        tx = ledger_client.send_tokens(destination_address, airdrop_amount, network_fee_denom, alice)
        # block until the transaction has been successful or failed
        tx.wait_to_complete()
        txcomplete = tx
        
        hashcursor = mydb.cursor()
        sql2 = "INSERT INTO txhash (user_id,tx_hash,amount) VALUES (%s, %s, %s)"
        val2 = (member_to_reward, txcomplete, amount)
        hashcursor.execute(sql2, val2)
        mydb.commit()
        
        resolution = "400"
        return resolution,juno_balance
    else:
      resolution = "405" #not enough rubies
      return resolution, juno_balance

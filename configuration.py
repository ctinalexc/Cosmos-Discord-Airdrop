#GENERAL CONFIG

#FOR BOT COMMANDS
YOUR_GUILD_ID = 816256689078403103

#FOR ADMIN ONLY COMMANDS
YOUR_ADMIN_USER_ID = 339123001225892755

#BOT TOKEN
DISCORD_TOKEN = "YOUR_DISCORD_TOKEN"

#TREASURY WALLET ADDRESS
treasury_wallet = "juno1axxyyzxyzxyzxzyxzyxzyxzyxzyxzyxzyxzyx"

#DB VARIABLES
host="localhost",
db_user="YOUR_DB_USER",
db_pass="YOUR_DB_PASS",
db_name="YOUR_DB_NAME") 

#NETWORK CONFIG
c_chain_id = "juno-1"
chain_url = "grpc+https://grpc-juno-ia.cosmosia.notional.ventures:443"
get_balance_api = "https://api.juno.kingnodes.com/cosmos/bank/v1beta1/balances/"
network_fee = 1
network_fee_denom = "ujuno"
network_prefix = "juno"
mnemonic_demo = "wait this is just a demo this is not for production environment"

#DEPENDING ON TYPES OF TRANSACTION AND TOKENS ON THE TREASURY WALLET YOU MIGHT
#NEED TO ADJUST IN THE MAIN.PY THIS CODE:
#juno_balance = int(int(d['balances'][0]['amount'])/pow(10,6))

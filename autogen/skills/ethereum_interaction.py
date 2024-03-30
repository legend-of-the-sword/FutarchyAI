"""
Prerequisites:
- Install the following Python packages:
  - web3: A Python library for interacting with Ethereum.
  - solcx: The Solidity compiler for Python.
  - eth-account: Account management for Ethereum.

You can install these packages using pip:

$ pip install --quiet web3 solcx eth-account

Environment Variables:
- Set the following environment variables before running the script:
  - PRIVATE_KEY: Your Ethereum private key.
  - DEPLOYER_ADDRESS: Your Ethereum address.
  - INFURA_API_KEY: Your Infura project API key.

Workflow:
1. Define the Solidity contract source code.
2. Compile the Solidity contract to obtain bytecode and ABI.
3. Deploy the contract to the Ethereum network (Sepolia testnet).
4. Interact with the contract by calling its functions.
"""

import os
from web3 import Web3, HTTPProvider
from eth_account import Account
from solcx import compile_source

# Set up web3 connection
infura_api_key = os.getenv('INFURA_API_KEY')
rpc_url = f"https://sepolia.infura.io/v3/{infura_api_key}"
w3 = Web3(HTTPProvider(rpc_url))

# Check if connected to Ethereum network
if not w3.is_connected():
    raise Exception("Failed to connect to Ethereum network.")

# Set deployer account from environment variables
private_key = os.getenv('PRIVATE_KEY')
deployer_address = os.getenv('DEPLOYER_ADDRESS')

# Solidity source code
# Replace the contract_source_code with your contract's Solidity code
contract_source_code = '''
pragma solidity ^0.8.0;

// Your contract code goes here

'''

# Function to compile and deploy a Solidity contract
def compile_and_deploy_contract(solidity_source_code):
    # Compile the contract
    compiled_sol = compile_source(solidity_source_code, output_values=["abi", "bin"])
    contract_id, contract_interface = compiled_sol.popitem()
    bytecode = contract_interface["bin"]
    abi = contract_interface["abi"]

    # Create contract instance
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Build constructor transaction
    constructor_txn = Contract.constructor().build_transaction({
        "from": deployer_address,
        "nonce": w3.eth.get_transaction_count(deployer_address),
        "gas": 1000000,
        "gasPrice": w3.toWei("20", "gwei")
    })

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(constructor_txn, private_key=private_key)

    # Send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Get the contract address
    contract_address = tx_receipt["contractAddress"]
    print(f"Contract deployed at address: {contract_address}")

    return contract_address, abi

# Function to interact with a deployed contract
def interact_with_contract(contract_address, contract_abi, function_name, *args):
    # Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Build function transaction
    contract_function = contract.get_function_by_name(function_name)(*args)
    function_txn = contract_function.build_transaction({
        "from": deployer_address,
        "nonce": w3.eth.get_transaction_count(deployer_address),
        "gas": 100000,
        "gasPrice": w3.to_wei("20", "gwei")
    })

    # Sign the transaction
    signed_function_txn = w3.eth.account.sign_transaction(function_txn, private_key=private_key)

    # Send the transaction
    function_tx_hash = w3.eth.send_raw_transaction(signed_function_txn.raw_transaction)

    # Wait for transaction receipt
    function_tx_receipt = w3.eth.wait_for_transaction_receipt(function_tx_hash)
    print(f"Function '{function_name}' transaction hash: {function_tx_hash.hex()}")

    return function_tx_receipt

# Instructions for viewing contracts and transactions on the Sepolia testnet explorer
def print_explorer_instructions(contract_address, transaction_hash):
    print("To view the contract or transactions on the Sepolia testnet explorer, use the following URLs:")
    print(f"Contract: https://sepolia.etherscan.io/address/{contract_address}")
    print(f"Transaction: https://sepolia.etherscan.io/tx/{transaction_hash}")

# Replace 'contract_source_code' with your actual Solidity contract code
contract_address, contract_abi = compile_and_deploy_contract(contract_source_code)

# Example interaction with the contract
# Replace 'function_name' with the actual function you want to call and provide the necessary arguments
# interact_with_contract(contract_address, contract_abi, 'function_name', arg1, arg2, ...)

# If you have any more tasks or questions, feel free to ask. If everything is done, there's nothing more to do.

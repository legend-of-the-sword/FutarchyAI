"""
Tool: Create Prediction Market Question

Description:
This tool allows you to create a new prediction market question in the Futarchy Prediction Market contract.

Prerequisites:
- Set the following environment variables:
  - PRIVATE_KEY: Your Ethereum private key.
  - DEPLOYER_ADDRESS: Your Ethereum address.
  - INFURA_API_KEY: Your Infura project API key.
  - CONTRACT_ADDRESS: The address of the deployed Futarchy Prediction Market contract.

Inputs:
- question: The text of the prediction market question.
- duration: The duration (in seconds) for the voting period.

Example Usage:
create_question("Will the price of ETH exceed $3000 by the end of the year?", 3600)
"""

import os
from web3 import Web3, HTTPProvider
from eth_account import Account


def create_question(question, duration):
    # Set up web3 connection
    infura_api_key = os.getenv("INFURA_API_KEY")
    rpc_url = f"https://sepolia.infura.io/v3/{infura_api_key}"
    w3 = Web3(HTTPProvider(rpc_url))

    # Set deployer account from environment variables
    private_key = os.getenv("PRIVATE_KEY")
    deployer_address = os.getenv("DEPLOYER_ADDRESS")

    # Set contract address from environment variable
    contract_address = os.getenv("CONTRACT_ADDRESS")

    # Load the contract ABI (replace with your actual ABI)
    contract_abi = [
        {
            "inputs": [
                {"internalType": "string", "name": "_question", "type": "string"},
                {"internalType": "uint256", "name": "_duration", "type": "uint256"},
            ],
            "name": "createQuestion",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_questionIndex", "type": "uint256"}
            ],
            "name": "determineOutcome",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getQuestionCount",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "questions",
            "outputs": [
                {"internalType": "string", "name": "text", "type": "string"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {
                    "internalType": "enum FutarchyPredictionMarket.Decision",
                    "name": "outcome",
                    "type": "uint8",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_questionIndex",
                    "type": "uint256",
                },
                {
                    "internalType": "enum FutarchyPredictionMarket.Decision",
                    "name": "_decision",
                    "type": "uint8",
                },
            ],
            "name": "vote",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]

    # Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Build transaction to create a new question
    create_question_txn = contract.functions.createQuestion(
        question, duration
    ).buildTransaction(
        {
            "from": deployer_address,
            "nonce": w3.eth.get_transaction_count(deployer_address),
            "gas": 100000,
            "gasPrice": w3.to_wei("20", "gwei"),
        }
    )

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(
        create_question_txn, private_key=private_key
    )

    # Send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"New question created. Transaction hash: {tx_hash.hex()}")

    return tx_receipt

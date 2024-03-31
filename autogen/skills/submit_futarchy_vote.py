"""
Tool: Submit Prediction Market Vote

Description:
This tool allows AI agents to submit votes for a prediction market question in the Futarchy Prediction Market contract.

Prerequisites:
- Set the following environment variables:
  - PRIVATE_KEY: The AI agent's Ethereum private key.
  - AGENT_ADDRESS: The AI agent's Ethereum address.
  - INFURA_API_KEY: Your Infura project API key.
  - CONTRACT_ADDRESS: The address of the deployed Futarchy Prediction Market contract.

Inputs:
- question_index: The index of the prediction market question.
- decision: The decision to vote for (0 for Yes, 1 for No).

Example Usage:
submit_vote(0, 0)  # Vote "Yes" for the first question
"""

import os
from web3 import Web3, HTTPProvider
from eth_account import Account
import json


def submit_vote(question_index, decision):
    # Set up web3 connection
    infura_api_key = os.getenv("INFURA_API_KEY")
    rpc_url = f"https://sepolia.infura.io/v3/{infura_api_key}"
    w3 = Web3(HTTPProvider(rpc_url))

    # Set agent account from environment variables
    private_key = os.getenv("PRIVATE_KEY")
    agent_address = os.getenv("AGENT_ADDRESS")

    # Set contract address from environment variable
    contract_address = os.getenv("CONTRACT_ADDRESS")

    # Load the contract ABI (replace with your actual ABI)
    contract_abi = '[{"inputs":[{"internalType":"string","name":"_question","type":"string"},{"internalType":"uint256","name":"_duration","type":"uint256"}],"name":"createQuestion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_questionIndex","type":"uint256"}],"name":"determineOutcome","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getQuestionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"questions","outputs":[{"internalType":"string","name":"text","type":"string"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"enum FutarchyPredictionMarket.Decision","name":"outcome","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_questionIndex","type":"uint256"},{"internalType":"enum FutarchyPredictionMarket.Decision","name":"_decision","type":"uint8"}],"name":"vote","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    # Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Build transaction to submit a vote
    submit_vote_txn = contract.functions.vote(
        question_index, decision
    ).build_transaction(
        {
            "from": agent_address,
            "nonce": w3.eth.get_transaction_count(agent_address),
            "gas": 100000,
            "gasPrice": w3.to_wei("20", "gwei"),
        }
    )

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(
        submit_vote_txn, private_key=private_key
    )

    # Send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Vote submitted. Transaction hash: {tx_hash.hex()}")

    return tx_receipt

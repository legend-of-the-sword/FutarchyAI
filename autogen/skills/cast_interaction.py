"""
Tool: Submit Random Vote to Prediction Market

Description:
This tool picks a random number between 0 and 1 and submits a vote to a Futarchy Prediction Market contract using the Foundry 'cast' command.

Prerequisites:
- Install Foundry (https://book.getfoundry.sh/getting-started/installation.html) or the script will attempt to install it.
- Set the following environment variables:
  - PRIVATE_KEY: The Ethereum private key.
  - ETH_RPC_URL: The Ethereum RPC URL.
  - CONTRACT_ADDRESS: The address of the deployed Futarchy Prediction Market contract.

Inputs:
- question_index: The index of the prediction market question.

Example Usage:
submit_random_vote(1)  # Submit a random vote for the second question
"""

import os
import random
import subprocess

def install_foundry():
    print("Installing Foundry...")
    subprocess.run(["curl", "-L", "https://foundry.paradigm.xyz", "|", "bash"])
    subprocess.run(["foundryup"])
    print("Foundry installed successfully.")

def submit_random_vote(question_index):
    # Check if Foundry is installed
    if subprocess.run(["which", "cast"], capture_output=True).returncode != 0:
        install_foundry()

    # Pick a random number between 0 and 1
    decision = random.randint(0, 1)

    # Set up environment variables
    private_key = os.getenv("PRIVATE_KEY")
    infura_api_key = os.getenv("INFURA_API_KEY")
    eth_rpc_url = f"https://sepolia.infura.io/v3/{infura_api_key}"
    contract_address = os.getenv("CONTRACT_ADDRESS")

    # Build the cast command
    cast_command = [
        "cast", "send", "--private-key", private_key,
        contract_address, f"vote(uint256,uint8) {question_index} {decision}",
        "--rpc-url", eth_rpc_url
    ]

    # Execute the cast command
    result = subprocess.run(cast_command, capture_output=True)
    if result.returncode == 0:
        print(f"Vote submitted successfully: {decision}")
    else:
        print(f"Failed to submit vote: {result.stderr.decode()}")

    return result.returncode

# Example usage
submit_random_vote(1)

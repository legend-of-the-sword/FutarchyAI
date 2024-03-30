// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FutarchyPredictionMarket {
    enum Decision { Yes, No }
    
    address public creator;
    string public question;
    uint256 public deadline;
    mapping(Decision => uint256) public votes;
    mapping(address => bool) public hasVoted;
    Decision public outcome;

    constructor(string memory _question, uint256 _duration) {
        creator = msg.sender;
        question = _question;
        deadline = block.timestamp + _duration;
    }

    function vote(Decision _decision) public {
        require(block.timestamp < deadline, "Voting period has ended");
        require(!hasVoted[msg.sender], "Already voted");

        votes[_decision] += 1;
        hasVoted[msg.sender] = true;
    }

    function determineOutcome() public {
        require(block.timestamp >= deadline, "Voting period has not ended");
        
        if (votes[Decision.Yes] > votes[Decision.No]) {
            outcome = Decision.Yes;
        } else {
            outcome = Decision.No;
        }
    }
}
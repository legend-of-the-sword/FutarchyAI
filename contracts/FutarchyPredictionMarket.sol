// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FutarchyPredictionMarket {
    enum Decision { Yes, No }
    
    struct Question {
        string text;
        uint256 deadline;
        mapping(Decision => uint256) votes;
        mapping(address => bool) hasVoted;
        Decision outcome;
    }
    
    Question[] public questions;
    
    function createQuestion(string memory _question, uint256 _duration) public {
        Question storage newQuestion = questions.push();
        newQuestion.text = _question;
        newQuestion.deadline = block.timestamp + _duration;
    }
    
    function vote(uint256 _questionIndex, Decision _decision) public {
        Question storage question = questions[_questionIndex];
        require(block.timestamp < question.deadline, "Voting period has ended");
        require(!question.hasVoted[msg.sender], "Already voted");
        
        question.votes[_decision] += 1;
        question.hasVoted[msg.sender] = true;
    }
    
    function determineOutcome(uint256 _questionIndex) public {
        Question storage question = questions[_questionIndex];
        require(block.timestamp >= question.deadline, "Voting period has not ended");
        
        if (question.votes[Decision.Yes] > question.votes[Decision.No]) {
            question.outcome = Decision.Yes;
        } else {
            question.outcome = Decision.No;
        }
    }
    
    function getQuestionCount() public view returns (uint256) {
        return questions.length;
    }
}
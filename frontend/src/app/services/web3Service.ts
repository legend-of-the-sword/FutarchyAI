import Web3 from "web3";
import FutarchyPredictionMarket from "../contracts/FutarchyPredictionMarket.json";
import { Question } from "../types";

const infuraApiKey = process.env.NEXT_PUBLIC_INFURA_API_KEY;
const contractAddress = process.env.NEXT_PUBLIC_CONTRACT_ADDRESS;

const web3 = new Web3(`https://sepolia.infura.io/v3/${infuraApiKey}`);
const contract = new web3.eth.Contract(
  FutarchyPredictionMarket.abi as any,
  contractAddress
);

const web3Service = {
  getQuestions: async (): Promise<Question[]> => {
    const questionCount = await contract.methods.getQuestionCount().call();
    const questions: Question[] = [];

    for (let i = 0; i < questionCount; i++) {
      const question = await contract.methods.questions(i).call();
      questions.push({
        id: i,
        text: question.text,
        deadline: new Date(question.deadline * 1000),
      });
    }

    return questions;
  },

  submitVote: async (questionId: number, decision: number): Promise<void> => {
    const accounts = await web3.eth.getAccounts();
    await contract.methods
      .vote(questionId, decision)
      .send({ from: accounts[0] });
  },

  getVotingResults: async (
    questionId: number
  ): Promise<{ yesVotes: number; noVotes: number }> => {
    const question = await contract.methods.questions(questionId).call();
    return {
      yesVotes: parseInt(question.votes[0]),
      noVotes: parseInt(question.votes[1]),
    };
  },
};

export default web3Service;

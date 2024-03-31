import Web3 from "web3";
import FutarchyPredictionMarket from "../contracts/FutarchyPredictionMarket.json";
import { Question } from "../types";

const infuraApiKey = process.env.NEXT_PUBLIC_INFURA_API_KEY;
const contractAddress = process.env.NEXT_PUBLIC_CONTRACT_ADDRESS;

if (!infuraApiKey || !contractAddress) {
  throw new Error("Missing Infura API key or contract address");
}

const web3 = new Web3(`https://sepolia.infura.io/v3/${infuraApiKey}`);
const contract = new web3.eth.Contract(
  FutarchyPredictionMarket.abi as any,
  contractAddress
);

const web3Service = {
  getQuestions: async (): Promise<Question[]> => {
    const questionCount = await contract.methods.getQuestionCount().call();
    const parsedQuestionCount = Number(questionCount);
    const questions: Question[] = [];

    for (let i = 0; i < parsedQuestionCount; i++) {
      const question = (await contract.methods.questions(i).call()) as {
        text: string;
        deadline: number;
      };
      questions.push({
        id: i,
        text: question.text,
        deadline: new Date(Number(question.deadline) * 1000),
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
    const voteCounts = (await contract.methods
      .getVoteCounts(questionId)
      .call()) as { yesVotes: string; noVotes: string };
    return {
      yesVotes: Number(voteCounts.yesVotes),
      noVotes: Number(voteCounts.noVotes),
    };
  },
};

export default web3Service;

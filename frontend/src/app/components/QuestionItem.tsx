import { Question } from "../types"
import VotingForm from "./VotingForm"
import VotingResults from "./VotingResults"

interface QuestionItemProps {
  question: Question
}

export default function QuestionItem({ question }: QuestionItemProps) {
  return (
    <div className="bg-white shadow rounded-lg p-6">
      <h3 className="text-xl font-semibold mb-4">{question.text}</h3>
      <p className="text-gray-600 mb-6">
        Deadline: {question.deadline.toLocaleDateString()}
      </p>
      <div className="flex justify-between items-center">
        <VotingForm questionId={question.id} />
        <VotingResults questionId={question.id} />
      </div>
    </div>
  )
}
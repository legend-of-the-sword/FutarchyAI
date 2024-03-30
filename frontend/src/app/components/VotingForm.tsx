"use client"

import { useState } from "react"
import web3Service from "../services/web3Service"

interface VotingFormProps {
  questionId: number
}

export default function VotingForm({ questionId }: VotingFormProps) {
  const [decision, setDecision] = useState<number>(0)

  const handleVote = async () => {
    try {
      await web3Service.submitVote(questionId, decision)
    } catch (error) {
      console.error("Error submitting vote:", error)
    }
  }

  return (
    <div className="flex items-center space-x-4">
      <div className="flex items-center space-x-2">
        <input
          type="radio"
          id="yes"
          name="decision"
          value={0}
          checked={decision === 0}
          onChange={() => setDecision(0)}
          className="form-radio text-blue-500"
        />
        <label htmlFor="yes" className="text-gray-700">
          Yes
        </label>
      </div>
      <div className="flex items-center space-x-2">
        <input
          type="radio"
          id="no"
          name="decision"
          value={1}
          checked={decision === 1}
          onChange={() => setDecision(1)}
          className="form-radio text-blue-500"
        />
        <label htmlFor="no" className="text-gray-700">
          No
        </label>
      </div>
      <button
        onClick={handleVote}
        className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
      >
        Vote
      </button>
    </div>
  )
}
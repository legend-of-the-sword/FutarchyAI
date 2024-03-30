'use client';

import { useEffect, useState } from 'react';
import { Box, Heading, VStack } from '@chakra-ui/react';
import { Question } from '../types';
import QuestionCard from './QuestionCard';
import web3Service from '../services/web3Service';

export default function QuestionList() {
  const [questions, setQuestions] = useState<Question[]>([]);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const fetchedQuestions = await web3Service.getQuestions();
        setQuestions(fetchedQuestions);
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    };

    fetchQuestions();
  }, []);

  return (
    <Box>
      <Heading as="h2" size="xl" mb={8}>
        Questions
      </Heading>
      <VStack spacing={6} align="stretch">
        {questions.map((question) => (
          <QuestionCard key={question.id} question={question} />
        ))}
      </VStack>
    </Box>
  );
}
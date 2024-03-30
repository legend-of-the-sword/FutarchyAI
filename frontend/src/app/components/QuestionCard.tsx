import { Box, Heading, Text, useColorModeValue, VStack } from '@chakra-ui/react';
import { Question } from '../types';
import VotingResults from './VotingResults';

interface QuestionCardProps {
  question: Question;
}

export default function QuestionCard({ question }: QuestionCardProps) {
  const cardBgColor = useColorModeValue('white', 'gray.700');
  const cardTextColor = useColorModeValue('gray.600', 'gray.400');

  return (
    <Box bg={cardBgColor} borderRadius="lg" p={6} boxShadow="md">
      <VStack spacing={4} align="start">
        <Heading as="h3" size="lg">
          {question.text}
        </Heading>
        <Text color={cardTextColor} fontSize="md">
          Deadline: {question.deadline.toLocaleDateString()}
        </Text>
        <VotingResults questionId={question.id} />
      </VStack>
    </Box>
  );
}
'use client';

import { useEffect, useState } from 'react';
import { Box, Heading, Text, useColorModeValue, VStack } from '@chakra-ui/react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import web3Service from '../services/web3Service';

ChartJS.register(ArcElement, Tooltip, Legend);

interface VotingResultsProps {
  questionId: number;
}

export default function VotingResults({ questionId }: VotingResultsProps) {
  const [votingResults, setVotingResults] = useState<{ yesVotes: number; noVotes: number }>({
    yesVotes: 0,
    noVotes: 0,
  });

  const chartTextColor = useColorModeValue('gray.600', 'gray.400');

  useEffect(() => {
    const fetchVotingResults = async () => {
      try {
        const results = await web3Service.getVotingResults(questionId);
        setVotingResults(results);
      } catch (error) {
        console.error('Error fetching voting results:', error);
      }
    };

    fetchVotingResults();
  }, [questionId]);

  const data = {
    labels: ['Yes', 'No'],
    datasets: [
      {
        data: [votingResults.yesVotes, votingResults.noVotes],
        backgroundColor: ['#48BB78', '#F56565'],
      },
    ],
  };

  const options = {
    plugins: {
      legend: {
        labels: {
          color: chartTextColor,
        },
      },
    },
  };

  return (
    <VStack spacing={4} align="start">
      <Heading as="h4" size="md">
        Voting Results
      </Heading>
      <Box width="100%">
        <Pie data={data} options={options} />
      </Box>
      <Text color={chartTextColor}>
        Yes: {votingResults.yesVotes}, No: {votingResults.noVotes}
      </Text>
    </VStack>
  );
}
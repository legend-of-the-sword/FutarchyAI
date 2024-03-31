'use client';

import { Box, Heading, Text, VStack, Code, HStack, Spacer } from '@chakra-ui/react';
import Header from './components/Header';
import Footer from './components/Footer';
import QuestionList from './components/QuestionList';

const contractAddress = process.env.NEXT_PUBLIC_CONTRACT_ADDRESS;
const network = 'Sepolia Testnet';

export default function Home() {
  return (
    <Box minHeight="100vh" display="flex" flexDirection="column">
      <Header />
      <Box flexGrow={1} py={8}>
        <VStack spacing={8} align="stretch" maxWidth="container.lg" mx="auto">
          <Box textAlign="center">
            <Heading as="h1" size="2xl" mb={4}>
              Futarchy Dashboard
            </Heading>
            <Text fontSize="xl" color="gray.500">
              Visualize and track the Futarchy contract on the blockchain
            </Text>
          </Box>
          <QuestionList />
        </VStack>
      </Box>
      <Footer />
      <Box position="fixed" bottom={4} right={4} bg="white" p={2} borderRadius="md" boxShadow="md">
        <HStack spacing={4} fontSize="sm">
          <Text fontWeight="bold">Contract:</Text>
          <Code>{contractAddress}</Code>
          <Spacer />
          <Text fontWeight="bold">Network:</Text>
          <Text>{network}</Text>
        </HStack>
      </Box>
    </Box>
  );
}
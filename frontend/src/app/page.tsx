'use client';

import { Box, Heading, Text, VStack } from '@chakra-ui/react';
import Header from './components/Header';
import Footer from './components/Footer';
import QuestionList from './components/QuestionList';

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
    </Box>
  );
}
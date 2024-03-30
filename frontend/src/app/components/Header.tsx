import { Box, Flex, Heading, Spacer } from '@chakra-ui/react';

export default function Header() {
  return (
    <Box bg="brand.500" py={4} px={8}>
      <Flex align="center" maxWidth="container.lg" mx="auto">
        <Heading as="h1" size="lg" color="white">
          Futarchy.ai
        </Heading>
        <Spacer />
        {/* Add navigation items */}
      </Flex>
    </Box>
  );
}
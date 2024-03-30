import { Box, Text } from '@chakra-ui/react';

export default function Footer() {
  return (
    <Box bg="gray.100" py={4} px={8} textAlign="center">
      <Text color="gray.500" fontSize="sm">
        &copy; {new Date().getFullYear()} Futarchy.ai. All rights reserved.
      </Text>
    </Box>
  );
}
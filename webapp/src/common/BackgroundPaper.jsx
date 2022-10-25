import React from 'react';

// Components:
import { Center, Paper, Box } from '@mantine/core';

export default function BackgroundPaper({ content, height, width }) {
  return (
    <Center>
      <Paper
        shadow="md"
        radius="md"
        p="xl"
        sx={{
          height: height ? height : 'auto',
          width: width ? width : '100%',
          margin: 5,
        }}
      >
        <Box>{content}</Box>
      </Paper>
    </Center>
  );
}

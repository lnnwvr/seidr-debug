import React from 'react';

// Components:
import { ScrollArea, Stack } from '@mantine/core';

//Variables:
const spacing = 10;

export default function BackgroundPaper({ content }) {
  return (
    <ScrollArea sx={{ height: 'calc(100vh - 100px)', backgroundColor: '#DCDCDC' }}>
      <Stack spacing={spacing} sx={(theme) => ({ marginTop: spacing, marginBottom: spacing })}>
        {content}
      </Stack>
    </ScrollArea>
  );
}

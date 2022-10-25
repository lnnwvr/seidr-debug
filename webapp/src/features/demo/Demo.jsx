import React from 'react';
import { Box, Paper, Center, Text } from '@mantine/core';
import { DataGrid, SeidrApiProvider } from 'seidr-react';

export default function AssetsPage() {
  return (
    <Box sx={{ height: '100%' }}>
      <Box sx={{ padding: '20px', height: '95%', display: 'flex', alignItems: 'stretch' }}>
        <Box sx={{ flex: 1 }}>
          <SeidrApiProvider path="/assets">
            <DataGrid hideActions hideSettings />
          </SeidrApiProvider>
        </Box>
      </Box>
    </Box>
  );
}

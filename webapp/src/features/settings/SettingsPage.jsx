import React from "react";

// Components:
import {
    Box,
    Button,
  } from "@mantine/core";
  import { Logout} from "tabler-icons-react";

export default function SettingsPage({ name }) {
return <Box>
  <p>use this for the Settings</p>

  <Button rightIcon={<Logout size={16}/>}>
    LogOut
  </Button>
</Box>
}

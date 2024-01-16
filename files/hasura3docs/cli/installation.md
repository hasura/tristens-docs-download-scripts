# Installation

You can download the CLI binaries below and start using it immediately. Please follow the instructions for your system.

## Install instructions for Linux/Macs​

- M1 / M2 Macs
- Intel Macs
- Linux


1. Download the latest `hasura3_aarch64-apple-darwin` binary:


`curl  -L https://graphql-engine-cdn.hasura.io/ddn/cli/latest/cli-hasura3-darwin-arm64 -o hasura3`

Downloading from the browser

If you are downloading from the browser, you'll likely encounter a notification that macOS cannot verify if this app is
free of malware. You can bypass this by right-clicking on the downloaded file and selecting "Open". This will open a
dialog box asking if you want to open the file. Click "Open" to continue. A terminal window will open, which you can
close, and proceed with the installation instructions below.

1. Run `chmod +x hasura3` (This makes the binary executable on your system)
2. Move the binary to `/usr/local/bin/` (run `mv hasura3 /usr/local/bin/` ). Please ensure that `/usr/local/bin/` is in
your PATH with `echo $PATH` .


1. Download the latest `hasura3_x86_64-apple-darwin` binary:


`curl  -L https://graphql-engine-cdn.hasura.io/ddn/cli/latest/cli-hasura3-darwin-amd64 -o hasura3`

Downloading from the browser

If you are downloading from the browser, you'll likely encounter a notification that macOS cannot verify if this app is
free of malware. You can bypass this by right-clicking on the downloaded file and selecting "Open". This will open a
dialog box asking if you want to open the file. Click "Open" to continue. A terminal window will open, which you can
close, and proceed with the installation instructions below.

1. Run `chmod +x hasura3` (This makes the binary executable on your system)
2. Move the binary to `/usr/local/bin/` (run `mv hasura3 /usr/local/bin/` ). Please ensure that `/usr/local/bin/` is in
your PATH with `echo $PATH` .


1. Download the latest `hasura3_x86_64-unknown-linux-musl` binary:


`curl  -L https://graphql-engine-cdn.hasura.io/ddn/cli/latest/cli-hasura3-linux-amd64 -o hasura3`

1. Run `chmod +x hasura3` (This makes the binary executable on your system)
2. Move the binary to `/usr/local/bin/` (run `mv hasura3 /usr/local/bin/` ). Please ensure that `/usr/local/bin/` is in
your PATH with `echo $PATH` .


Permissions error

If you get a message about permissions, run the above commands with the `sudo` keyword and enter your password.

## Install instructions for Windows​

1. Download the latest `hasura3_x86_64-pc-windows-gnu.exe` binary and run it.


`curl  -L https://graphql-engine-cdn.hasura.io/ddn/cli/latest/cli-hasura3-windows-amd64.exe -o hasura3.exe`

Unrecognized application warning

In Windows, if you get an "Unrecognized application" warning, click "Run anyway".

## Verify Installation​

Running `hasura3` should print the following message:

```
 HH\                                                         333333\
 HH |                                                       33 ___33\
 HHHHHHH\   AAAAAA\   SSSSSSS\ UU\   UU\  RRRRRR\  AAAAAA\  \_/   33 |
 HH  __HH\  \____AA\ SS  _____|UU |  UU |RR  __RR\ \____AA\   33333 /
 HH |  HH | AAAAAAA |\SSSSSS\  UU |  UU |RR |  \__|AAAAAAA |  \___33\
 HH |  HH |AA  __AA | \____SS\ UU |  UU |RR |     AA  __AA |33\   33 |
 HH |  HH |\AAAAAAA |SSSSSSS  |\UUUUUU  |RR |     \AAAAAAA |\333333  |
 \__|  \__| \_______|\_______/  \______/ \__|      \_______| \______/
DDN commands:
  project       Manage Hasura DDN Projects
  secret        Commands related to Hasura Cloud Secret Ops
  login         Login to Hasura Cloud
  logout        Logout from Hasura Cloud
  build         Manage Hasura DDN Project Builds [alias: builds]
  environment   Environments in Hasura Projects [aliases: env, environments]
  subgraph      Manage Hasura project subgraphs
  daemon        Manage Hasura Secure Connect Tunnel Daemon
  tunnel        Hasura Secure Connect service
  init          Init Hasura DDN project
  metadata      Manage Hasura DDN Projects' Metadata
  watch         Watch a local Hasura project
Other commands:
  version      Print the CLI version
  update-cli   Update the CLI to latest or a specific version
  plugins      Manage plugins for the CLI
Use "hasura3 [command] --help" for more information about a command.
```

### What did you think of this doc?

- [ Install instructions for Linux/Macs ](https://hasura.io/docs/3.0/cli/installation/#install-instructions-for-linuxmacs)
- [ Install instructions for Windows ](https://hasura.io/docs/3.0/cli/installation/#install-instructions-for-windows)
- [ Verify Installation ](https://hasura.io/docs/3.0/cli/installation/#verify-installation)

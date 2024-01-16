# Install / Uninstall the Hasura CLI

## Install the Hasura CLI​

### Install the Hasura CLI binary globally​

The recommended installation method of the Hasura CLI is to install it as a global binary. You can download it by
following the instructions for your operating system:

- Linux
- Mac
- Windows


In your Linux shell, run the following command:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   bash`

This will install the Hasura CLI in `/usr/local/bin` . You might have to provide your `sudo` password depending on the
permissions of your `/usr/local/bin` location.

If you'd prefer to install to a different location other than `/usr/local/bin` , set the `INSTALL_PATH` variable
accordingly:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   INSTALL_PATH = $HOME /bin  bash`

You can also install a specific version of the CLI by providing the `VERSION` variable:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   VERSION = v2.33.0  bash`

In your Terminal, run the following command:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   bash`

This will install the Hasura CLI in `/usr/local/bin` . You might have to provide your `sudo` password depending on the
permissions of your `/usr/local/bin` location.

If you'd prefer to install to a different location other than `/usr/local/bin` , set the `INSTALL_PATH` variable
accordingly:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   INSTALL_PATH = $HOME /bin  bash`

You can also install a specific version of the CLI by providing the `VERSION` variable:

`curl  -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh  |   VERSION = v2.33.0  bash`

Download the binary `cli-hasura-windows-amd64.exe` available under `Assets` of the latest release from the GitHub
release page :

Rename the downloaded file to `hasura` . You can add the path to the environment variable `PATH` for making `hasura` accessible globally.

Tip: Add shell completion

To add command auto-completion in your shell, refer to the[ hasura completion ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_completion/)command.

### Install through npm​

The Hasura CLI is available as an[ npm package ](https://www.npmjs.com/package/hasura-cli)which wraps the compiled
binary and is **independently maintained by members of the community. Hasura does not offer maintenance or support for
this package** .

## Uninstall the Hasura CLI​

### Uninstall a binary globally​

If you installed the binary directly on your system, delete the binary file from its installation location.

```
# By default, the binary is installed at /usr/local/bin/hasura
$  which  hasura
  /usr/local/bin/hasura
# use sudo if required
$  rm  /usr/local/bin/hasura
```

### Uninstall through npm​

Follow the instructions on the[ npm package ](https://www.npmjs.com/package/hasura-cli)page to uninstall the npm
package.

### What did you think of this doc?

- [ Install the Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#install-the-hasura-cli)
    - [ Install the Hasura CLI binary globally ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#install-the-hasura-cli-binary-globally)

- [ Install through npm ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#install-through-npm)
- [ Uninstall the Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#uninstall-the-hasura-cli)
    - [ Uninstall a binary globally ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#uninstall-a-binary-globally)

- [ Uninstall through npm ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/#uninstall-through-npm)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
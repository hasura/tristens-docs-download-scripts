# Manage Hasura Metadata (config v2)

## Introduction​

If your Postgres schema is already managed with a tool like knex, TypeORM, Django/Rails migrations, you will still need
a way to export the actions you performed on the Hasura Console to apply it later on another Hasura instance.

All the actions performed on the Console, like tracking tables/views/custom functions, creating relationships,
configuring permissions, creating Event Triggers and Remote Schemas, etc. can be exported as a JSON/yaml Metadata file
which can be version controlled. The Metadata file can be later imported to another Hasura instance to get the same
configuration. You can also manually edit the Metadata file to add more objects to it and then use it to update the
instance.

## Exporting Hasura Metadata​

- CLI
- Console
- API


Metadata can be exported with the[ hasura metadata export ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_export/)command.

This will export the Metadata as yaml files in the `/metadata` directory

1. Click on the settings (⚙) icon at the top right corner of the Console screen.
2. In the Hasura Metadata actions page that opens, click on the `Export Metadata` button.


Click on the settings (⚙) icon at the top right corner of the Console screen.

In the Hasura Metadata actions page that opens, click on the `Export Metadata` button.

Image: [ Export metadata ](https://hasura.io/docs/assets/images/metadata-export-dc82d84d94a2a6dfa5903d798e079aad.png)

1. This will prompt a file download for `hasura_metadata_{timestamp}.json` . Save the file.


The export can be done via the[ export_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-export-metadata)Metadata API. Response will
be a JSON object with the Hasura Metadata.

Here is an example using `curl` to save this as a file:

`curl  -d '{"type": "export_metadata", "args": {}}'  http://localhost:8080/v1/metadata -o hasura_metadata.json`

This command will create a `hasura_metadata.json` file. If an admin secret is set, add `-H 'X-Hasura-Admin-Secret: {your-admin-secret}'` as the API is an admin-only API.

Note

The Metadata exported via the **console and API** will be a single JSON file that can be applied via the Console or the
API only.

The Metadata exported via the **CLI** is broken into multiple YAML files for easier management in version control and
CI/CD and can be applied via the CLI or the[ cli-migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/)image only.

## Applying/Importing Hasura Metadata​

You can apply exported Metadata from one Hasura GraphQL Engine instance to another. You can also apply an older or
modified version of an instance's Metadata onto itself.

Importing completely replaces the Metadata on that instance, i.e. you lose any Metadata that was already present before.

- CLI
- Console
- API


Metadata can be applied with the[ hasura metadata apply ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_apply/)command.

1. Click on the settings (⚙) icon at the top right corner of the Console screen.
2. Click on `Import Metadata` button.


Click on the settings (⚙) icon at the top right corner of the Console screen.

Click on `Import Metadata` button.

Image: [ Import metadata ](https://hasura.io/docs/assets/images/metadata-import-0f5c0beda7c7bea18c2d26efcf038436.png)

1. Choose a `hasura_metadata.json` file that was exported earlier.
2. A notification should appear indicating the success or error.


Choose a `hasura_metadata.json` file that was exported earlier.

A notification should appear indicating the success or error.

The exported JSON can be imported via the[ replace_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-replace-metadata)Metadata API.

Here is an example using `curl` :

`curl  -d '{"type":"replace_metadata", "args":' $( cat  hasura_metadata.json ) '}'  http://localhost:8080/v1/metadata`

This command reads the `hasura_metadata.json` file and makes a POST request to replace the metadata. If an admin secret
is set, add `-H 'X-Hasura-Admin-Secret: {your-admin-secret}'` as the API is an admin-only API.

Note

All the dependent objects, like tables, views, functions etc. should exist on Postgres before importing the metadata.
Otherwise, it will result in an error saying the object does not exist. So, apply the Postgres schema first, before
importing the metadata.

## Reloading Hasura Metadata​

In some cases, the Metadata can be out of sync with the Postgres schema. For example, when a new column has been added
to a table via an external tool such as `psql` .

- CLI
- Console
- API


Metadata can be reloaded with the[ hasura metadata reload ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/)command.

1. Click on the settings (⚙) icon at the top right corner of the Console screen.
2. Click on `Reload` button.


Click on the settings (⚙) icon at the top right corner of the Console screen.

Click on `Reload` button.

Image: [ reload metadata ](https://hasura.io/docs/assets/images/metadata-reload-7a369449166ec17dc0c585fdba3f864c.png)

1. A notification should appear indicating the success.


The reload of Metadata can be done via the[ reload_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-reload-metadata)Metadata API.

Here is an example using `curl` :

`curl  -d '{"type": "reload_metadata", "args": {}}'  http://localhost:8080/v1/metadata`

If an admin secret is set, add `-H 'X-Hasura-Admin-Secret: {your-admin-secret}'` as the API is an admin-only API.

Note

Reloading may result in inconsistent Metadata status. You may need to resolve all inconsistent objects manually or
delete them. After that, you need to reload Metadata again.

## Resetting Hasura Metadata​

Resetting GraphQL Engine's Metadata is an irreversible process. It is recommended to first export the metadata so that
it can be reapplied if needed or else that information will be lost and Hasura will have to be configured again from
scratch (e.g. tracking tables, relationships, creating triggers, actions, etc.).

- CLI
- Console
- API


Metadata can be reset with the[ hasura metadata clear ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_clear/)command.

1. Click on the settings (⚙) icon at the top right corner of the Console screen.
2. Click on `Reset` button.


Click on the settings (⚙) icon at the top right corner of the Console screen.

Click on `Reset` button.

Image: [ reset metadata ](https://hasura.io/docs/assets/images/metadata-reset-267b49b09e7c7be8b096f4f93d21e479.png)

1. A pop-up will appear prompting you to confirm the process.
2. A notification should appear indicating the success.


A pop-up will appear prompting you to confirm the process.

A notification should appear indicating the success.

The reset of Metadata can be done via the[ clear_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-clear-metadata)Metadata API.

Here is an example using `curl` :

`curl  -d '{"type": "clear_metadata", "args": {}}'  http://localhost:8080/v1/metadata`

If an admin secret is set, add `-H 'X-Hasura-Admin-Secret: {your-admin-secret}'` as the API is an admin-only API.

## Managing Hasura Metadata in CI/CD​

In case you need an automated way of applying/importing the metadata, take a look at the[ cli-migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/)Docker image,
which can start the GraphQL Engine after automatically importing a mounted Metadata directory.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#introduction)
- [ Exporting Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#exporting-hasura-metadata)
- [ Applying/Importing Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#applyingimporting-hasura-metadata)
- [ Reloading Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#reload-metadata-manual-v2)
- [ Resetting Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#reset-metadata-manual-v2)
- [ Managing Hasura Metadata in CI/CD ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/manage-metadata/#managing-hasura-metadata-in-cicd)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
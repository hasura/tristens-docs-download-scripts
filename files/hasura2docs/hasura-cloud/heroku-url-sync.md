# Heroku Database Integration

Note

To know more about Heroku's latest announcement on deprecation of free resources, please see[ this page ](https://hasura.io/docs/latest/databases/postgres/heroku/).

Warning

Recently, Heroku introduced a[ change to Postgres extensions ](https://devcenter.heroku.com/changelog-items/2446)that
affects our integration and the use of Event Triggers. If you're having trouble creating Event Triggers with a database
hosted on Heroku, you can find more information[ in this GitHub issue ](https://github.com/hasura/graphql-engine/issues/8734).

## Introduction​

Hasura Cloud makes it easy for you to use Heroku Postgres as a datasource in your Hasura Cloud projects. It makes sure
that the `DATABASE_URL` environment variable of your Heroku App stays in sync with a given environment variable of your
Hasura Cloud project. This means that whenever the database credentials of your Heroku Postgres are rotated, this
integration ensures that the linked environment variable in your Hasura Cloud project also gets updated.

## Connecting an existing Heroku database​

You can connect your Heroku database to your Hasura Project by following these steps:

1. Go to your Hasura Cloud dashboard and head to the settings section of the desired project
2. Go to `Integrations` tab and click on the Heroku integration under `Databases`
3. Login into Heroku, enter an env var name of your choice (say `PG_DATABASE_URL` ) and connect the desired database
from the list of databasesAfter a couple of seconds the env var will be updated with your connected database url and you can see it in the `Env Vars` tab of your project.
4. Now you can go ahead to your project Console's `Data` tab and connect the database through the env var that you
created.


Go to your Hasura Cloud dashboard and head to the settings section of the desired project

Go to `Integrations` tab and click on the Heroku integration under `Databases` 

Image: [ Heroku Integration ](https://hasura.io/docs/assets/images/heroku-integration-d395b4b66040c9b7acafde8b43ef02cb.png)

Login into Heroku, enter an env var name of your choice (say `PG_DATABASE_URL` ) and connect the desired database
from the list of databases

After a couple of seconds the env var will be updated with your connected database url and you can see it in the `Env Vars` tab of your project.

Now you can go ahead to your project Console's `Data` tab and connect the database through the env var that you
created.

Image: [ Heroku DB Connect ](https://hasura.io/docs/assets/images/heroku-db-connect-8910dfb1055db866641d147ea774985d.png)

This completes your integration setup, you can now go ahead, track tables and try out Hasura's GraphQL APIs.

Note

Deleting the Heroku integration from your `Integrations` section does not delete the associated env var, it only stops
the database url sync. Should you want to remove the env var also, it is recommended to remove the connected database
from your Console and then deleting the associated env var to prevent Metadata inconsistency.

## Heroku database URL sync​

If you use Hasura Cloud's Heroku integration, it keeps your project's Heroku database URL i.e. the associated env var in
sync with the Postgres URL from a Heroku app. This is especially helpful in cases when the database credentials of
Heroku Postgres are rotated automatically by Heroku.

Note

The database sync automatically gets disconnected if you transfer the ownership of your project to another account. The
new project owner can restart the sync with the Heroku account that they have connected their Hasura Cloud account to.

### Enable Heroku database URL sync​

If you create a project with a Heroku trial database using the Hasura Console, your project has the Heroku database URL
sync enabled by default, which means, Hasura Cloud keeps the database URL of your project in sync with the related
Heroku Postgres.

If you have already connected your Heroku database to your Hasura Cloud project and would like to enable database URL
sync on it, you can remove and re-add the database url env var with the Heroku integration as shown[ above ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#cloud-connect-existing-heroku-db)

### Opt out of Heroku database URL sync​

If your project has Heroku database URL sync enabled, you can opt out using the following methods:

#### Option 1:​

1. Go to the `Env vars` tab of your project and click on the env var that is involved in the Heroku database URL sync.
2. Click on `Opt out of the sync` button next to Heroku note.


Go to the `Env vars` tab of your project and click on the env var that is involved in the Heroku database URL sync.

Click on `Opt out of the sync` button next to Heroku note.

Image: [ Enabled DB Sync ](https://hasura.io/docs/assets/images/heroku-db-sync-enabled-new-31670ea7a14e6858b28374ce6e993d88.png)

#### Option 2:​

You can also opt out of Heroku database URL sync by deleting the integration from project integrations page.

Image: [ Delete Heroku Integration ](https://hasura.io/docs/assets/images/heroku-delete-integration-d587d637db292c663d8625dacee2643d.png)

## How it works?​

Heroku database URL sync is useful because Postgres credentials of Heroku Postgres are sometimes rotated thus making the
old database URL invalid. Hasura Cloud listens to the changes in the database URL of your app and keeps the project
updated. This is done using:

1. [ Heroku Releases ](https://devcenter.heroku.com/articles/releases): Whenever a config variable of a Heroku app
changes, a new `release` is made for that app.
2. [ Heroku Webhooks ](https://devcenter.heroku.com/articles/app-webhooks): Heroku allows us to get notifications about
these releases on a webhook.


Whenever Postgres credentials of a Heroku app are rotated:

1. The `DATABASE_URL` config variable of the Heroku app gets updated with the new credentials.
2. The config variable change triggers a new release, which notifies Hasura Cloud's webhook.
3. When Hasura Cloud is notified about the new release, it fetches the newest database URL from Heroku and updates the
connected env var of your project with it.
4. This way, your project is always configured with the correct database URL.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#introduction)
- [ Connecting an existing Heroku database ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#cloud-connect-existing-heroku-db)
- [ Heroku database URL sync ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#heroku-database-url-sync)
    - [ Enable Heroku database URL sync ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#enable-heroku-database-url-sync)

- [ Opt out of Heroku database URL sync ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#opt-out-of-heroku-database-url-sync)
- [ How it works? ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/#how-it-works)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
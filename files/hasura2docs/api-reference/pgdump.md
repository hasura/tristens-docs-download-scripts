# PG Dump API Reference

## Introduction​

The PG Dump API is an **admin-only** endpoint that can be used to execute `pg_dump` on the Postgres instance that Hasura
is configured with.

The primary motive of this API is to provide convenience methods to initialize Migrations from an existing Hasura
instance. But the functionality can be later expanded to do other things such as taking a data dump, etc.

## Endpoint​

All requests are `POST` requests to the `/v1alpha1/pg_dump` endpoint.

## API Spec​

### Request​

```
POST   /v1alpha1/pg_dump   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
X-Hasura-Admin-Secret :   <admin-secret>
{
   "opts" :   [ "-O" ,   "-x" ,   "--schema-only" ,   "--schema" ,   "public" ] ,
   "clean_output" :   true ,
   "source" :   "<database-source-name>"
}
```

- `opts` : Arguments to be passed to the `pg_dump` tool. Represented as array of strings. The underlying command that is
executed is:
- `clean_output` : When this optional argument is set to `true` , the output SQL from the command is cleaned to remove the
following:
    - SQL front matter, like SET statements.

- `CREATE SCHEMA public` .

- `COMMENT ON SCHEMA public is 'standard public schema'` ;

- Comments ( `--` ) and empty newlines.

- Postgres triggers created by Hasura for Event Triggers.
- `source` : the name of the connected database on which to run `pg_dump` on. If skipped, it is set to `default`


 `opts` : Arguments to be passed to the `pg_dump` tool. Represented as array of strings. The underlying command that is
executed is:

`pg_dump  $DATABASE_URL   $OPTS  -f  $FILENAME`

 `clean_output` : When this optional argument is set to `true` , the output SQL from the command is cleaned to remove the
following:

 `source` : the name of the connected database on which to run `pg_dump` on. If skipped, it is set to `default` 

### Sample response​

```
HTTP/1.1   200   OK
Content-Type :   application/sql
SET check_function_bodies = false;
CREATE TABLE public.author (
    id integer NOT NULL,
    name text NOT NULL
);
CREATE SEQUENCE public.author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.author_id_seq OWNED BY public.author.id;
ALTER TABLE ONLY public.author ALTER COLUMN id SET DEFAULT nextval('public.author_id_seq'::regclass);
```

## Disabling PG Dump API​

Since this API can be used to dump all the Postgres data and schema, it can be disabled, especially in production
deployments.

The `enabled-apis` flag or the `HASURA_GRAPHQL_ENABLED_APIS` env var can be used to enable/disable this API. By default,
The PG DumpAPI is enabled. To disable it, you need to explicitly state that this API is not enabled. i.e. remove it from
the list of enabled APIs.

```
# enable only graphql & Metadata apis, disable pgdump
--enabled-apis = "graphql,metadata"
HASURA_GRAPHQL_ENABLED_APIS = "graphql,metadata"
```

See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for info on setting the
above flag/env var.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/pgdump/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/pgdump/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/pgdump/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/pgdump/#request)

- [ Sample response ](https://hasura.io/docs/latest/api-reference/pgdump/#sample-response)
- [ Disabling PG Dump API ](https://hasura.io/docs/latest/api-reference/pgdump/#disabling-pg-dump-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
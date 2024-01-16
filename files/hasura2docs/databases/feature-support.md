# Database Feature Support

The below matrices show the database wise support for the different GraphQL features under schema, queries, mutations
and subscriptions.

Tip

Each ✅ below links **directly** to the feature within a particular type of database.

## Schema​

|  | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB |
|---|---|---|---|---|---|---|
| Table Relationships | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/) |
| Remote Relationships | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/ms-sql-server/remote-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/bigquery/index/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#relationships) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/) |
| Views | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/views/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/views/) | [ ✅ ](https://hasura.io/docs/latest/schema/ms-sql-server/views/) | ✅ | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/views/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/views/) |
| Custom Functions | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-functions/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-functions/) | ❌ | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#functions) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-functions/) |
| Enums | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/enums/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/enums/) | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/enums/) | ❌ |
| Computed Fields | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/computed-fields/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#computed-fields) | ❌ | [ ✅ ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#functions) | ❌ |
| Data Validations | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/data-validations/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/data-validations/) | ✅ | [ ✅ ](https://hasura.io/docs/latest/schema/bigquery/data-validations/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/data-validations/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/data-validations/) |
| Relay Schema | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/relay-schema/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/relay-schema/) | ❌ | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/relay-schema/) |
| Naming Conventions | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/naming-convention/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#naming-conventions) | ❌ | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#naming-conventions) | ❌ |
| Custom Fields | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/) | [ ✅ ](https://hasura.io/docs/latest/schema/ms-sql-server/custom-field-names/) | [ ✅ ](https://hasura.io/docs/latest/schema/bigquery/custom-field-names/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/) |
| Default Values | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/default-values/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/default-values/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/index/) | ❌ | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/default-values/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/default-values/index/) |


## Queries​

|  | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB |
|---|---|---|---|---|---|---|
| Simple | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/simple-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/simple-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/simple-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/simple-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/simple-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/simple-object-queries/) |
| Nested Object | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/nested-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/nested-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/nested-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/nested-object-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/nested-object-queries/) |
| Aggregation | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/aggregation-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/aggregation-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/aggregation-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/aggregation-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/aggregation-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/aggregation-queries/) |
| Filter / Search | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/filters/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/filters/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/filters/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/filters/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/filters/index/) |
| Sort | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/sorting/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/sorting/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/sorting/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/sorting/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/sorting/) |
| Distinct | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/distinct-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/distinct-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#queries) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/distinct-queries/) |
| Paginate | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/pagination/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/pagination/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/pagination/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/pagination/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/pagination/) |
| Multiple Arguments | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-arguments/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-arguments/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/multiple-arguments/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-arguments/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-arguments/) |
| Multiple Queries | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/multiple-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/) |
| Variables / Aliases / Fragments | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/variables-aliases-fragments-directives/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/variables-aliases-fragments-directives/) | [ ✅ ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/) | [ ✅ ](https://hasura.io/docs/latest/queries/bigquery/index/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/variables-aliases-fragments-directives/) | [ ✅ ](https://hasura.io/docs/latest/queries/postgres/variables-aliases-fragments-directives/) |


## Mutations​

|  | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB |
|---|---|---|---|---|---|---|
| Insert | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/insert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/insert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/) | ❌ | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/insert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/insert/) |
| Upsert | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/upsert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/upsert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/) | ❌ | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/upsert/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/upsert/) |
| Update | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/update/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/update/) | [ ✅ ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/) | ❌ | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/update/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/update/) |
| Delete | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/delete/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/delete/) | [ ✅ ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/) | ❌ | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/delete/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/delete/) |
| Multiple per Request | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/) | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/) | [ ✅ ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/) |


## Subscriptions​

|  | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB |
|---|---|---|---|---|---|---|
| Value of Field | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-field) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-field) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#pg-subscribe-field) | ❌ | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-field) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-field) |
| Updates to Rows | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-table) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-table) | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-table) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-table) |
| Value of Derived Field | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-derived) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-derived) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#pg-subscribe-derived) | ❌ | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-derived) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-derived) |
| Streaming Subscriptions | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/) | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/) | [ ✅ ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/) |


## Event Triggers​

|  | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB |
|---|---|---|---|---|---|---|
| INSERT | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers) | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#event-triggers) | ❌ |
| UPDATE | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers) | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#event-triggers) | ❌ |
| DELETE | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers) | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#event-triggers) | ❌ |
| MANUAL | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers) | [ ✅ ](https://hasura.io/docs/latest/event-triggers/overview/) | ❌ | [ ❌ ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/hasura-cockroachdb-compatibility/#event-triggers) | ❌ |


## Joins​

| From ⬇️ / To ➡️ | Postgres | Citus | SQL Server | BigQuery | CockroachDB | CosmosDB | Action | Remote Schema |
|---|---|---|---|---|---|---|---|---|
| Postgres Database | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/) | ❌ | ❌ | ❌ | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/) |
| Database (non-Postgres) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ⚠️ |
| Action | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/) | [ ✅ ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/) | ❌ | ❌ | ❌ | ❌ | [ ✅ ](https://hasura.io/docs/latest/actions/action-relationships/#action-to-action-relationships) | ❌ |
| Remote Schema | [ ✅ ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/) | [ ✅ ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | [ ✅ ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-relationships/) |


For any ⚠️ above

Check your individual database's compatibility page for more details.

Additional Resources

Get Started with Hasura today -[ Watch video guide ](https://hasura.io/events/webinar/get-started-with-hasura/?pg=docs&plcmt=body&cta=getting-started&tech=).

### What did you think of this doc?

- [ Schema ](https://hasura.io/docs/latest/databases/feature-support/#schema)
- [ Queries ](https://hasura.io/docs/latest/databases/feature-support/#queries)
- [ Mutations ](https://hasura.io/docs/latest/databases/feature-support/#mutations)
- [ Subscriptions ](https://hasura.io/docs/latest/databases/feature-support/#subscriptions)
- [ Event Triggers ](https://hasura.io/docs/latest/databases/feature-support/#event-triggers)
- [ Joins ](https://hasura.io/docs/latest/databases/feature-support/#joins)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
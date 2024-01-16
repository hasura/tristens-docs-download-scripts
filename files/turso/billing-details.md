# Billing details

## Pricing tiers​

Turso has three pricing tiers:

- Starter (free, with limits)
- Scaler (monthly cost, with limits)
- Enterprise (unlimited)


For a breakdown of what each plan costs and includes, see the[ pricing page ](http://turso.tech/pricing).

## Usage-based billing model​

For the Starter and Scaler plans, Turso usage is limited monthly based on the
following usage observations during each calendar month:

- Number of table rows read
- Number of table rows written
- Amount of total storage


The accounting for this usage is based on SQLite internal implementation
details. This documentation explains the usage patterns that affect the above
metrics. In order to understand the usage of a particular database operation,
you must first understand how SQLite implements that operation.

## Show current monthly usage​

You can use the Turso CLI to[ inspect usage statistics ](https://docs.turso.tech/reference/turso-cli#inspect-database-usage)for a database for the
current calendar month.

## Accounting for rows read​

A "row read" is more accurately described as a "row scanned" by SQLite during
the process of executing a statement. There are two things to know as you
observe the rows read metric provided by the Turso CLI:

- A SQL query may cause more rows to be scanned than are returned by that query.
- A SQL update statement incurs at least one row read for each row updated.


### Queries with aggregate functions​

Use of[ aggregate functions ](https://www.sqlite.org/lang_aggfunc.html)such as `count` , `avg` , `min` , `max` , and `sum` incur one row read for each table row considered in the aggregation.

info

You may want to optimize both the cost and performance of aggregation queries by
using another table to store aggregate values, and keeping it up to date (using
a transaction) as the original table is updated.

### Queries without a supporting index (full table scan)​

Any query that is not able to make use of an index on a table incurs one row
read for each row in the table.

Read some[ general advice ](https://docs.turso.tech//billing-details/#advice-for-reducing-usage)on avoiding expensive
table scans.

### Table joins, subqueries, and compound queries​

A query that consults multiple tables incurs one row read for each row that was
considered from each table participating in the query.

### Row updates​

A SQL update command that changes row data incurs one read (in addition to one
write) for each row updated. If the update uses a filter to choose rows to
modify, and SQLite is unable to use an index to find those rows, it performs a
full table scan, incurring one read for *each* row in the entire table, in
addition to one row write for each row updated.

### ALTER TABLE row reads​

`ALTER TABLE`

Use of an `ALTER TABLE` statement that effectively rewrites the contents of each
row in a table requires a full table scan, which incurs one row read for each
existing row in the table.

An `ALTER TABLE DROP COLUMN` statement[ might not cause a full-table scan ](https://www.sqlite.org/lang_altertable.html).

An `ALTER TABLE` statement might also[ incur row
writes ](https://docs.turso.tech//billing-details/#alter-table-row-writes).

### Adding an index to a table with existing rows​

Adding an index to a table requires a full table scan, and incurs one read for
each row that currently exists in the table.

### SQLite system tables​

SQLite tables that are maintained internally, such as `dbstat` and tables
prefixed with `sqlite_` do not incur row reads when used in a query.

### Commands that incur no row reads​

If a command doesn't incur any row reads or row writes as part of its execution,
the command instead incurs one row read. For example, `select 1` incurs one row
read.

## Accounting for rows written​

A "row written" includes both a newly inserted row and an update of a single
existing row.

### ALTER TABLE row writes​

`ALTER TABLE`

 `ALTER TABLE` statements may incur one row write for each existing row if row
data is modified during the operation. Read about[ how SQLite works for
different types of alterations ](https://www.sqlite.org/lang_altertable.html#how_it_works).

An `ALTER TABLE` statement might also[ incur row reads ](https://docs.turso.tech//billing-details/#alter-table-row-reads).

### Aborted transactions​

A row inserted or updated during a transaction still incurs a row write even if
the transaction isn't committed.

## Accounting for total storage​

The SQLite virtual table[ dbstat ](https://www.sqlite.org/dbstat.html)is used to determine the total space occupied
by all tables and indexes. The smallest unit of measurement is a database file[ page ](https://www.sqlite.org/fileformat.html#pages)of 4KB in size.

info

With SQLite databases, the VACUUM command is normally used to optimize storage.
This command is currently disabled in Turso. In the future, we hope to provide a
way for developers to compact the total storage of a database.

## Exceeding quotas​

For billing plans with monthly usage quotas for row reads, row writes, and total
storage, a query that causes overage fails with the error code `BLOCKED` .

## Advice for reducing usage​

To minimize the incurred reads and writes on your database:

- Read about the[ SQLite query planner ](https://www.sqlite.org/queryplanner.html)to understand how queries work.
- Use SQLite's[ EXPLAIN QUERY PLAN statement ](https://www.sqlite.org/eqp.html)to understand if a query performs
a full table scan, and if it's using the best available index to minimize
reads.
- Ensure that every query that filters rows is able to use an index to find the
relevant rows. Without an index, SQLite performs a table scan to find the
rows, which costs one read for each existing row in the table.
- Add all required indexes at the time a table is created. Adding indexes to
tables with existing rows incurs one read for each existing row.


## Report issues with billing​

If there is a question or problem with your bill or its accounting, contact[ support@turso.tech ](mailto:support@turso.tech).

- [ Pricing tiers ](https://docs.turso.tech//billing-details/#pricing-tiers)
- [ Usage-based billing model ](https://docs.turso.tech//billing-details/#usage-based-billing-model)
- [ Show current monthly usage ](https://docs.turso.tech//billing-details/#show-current-monthly-usage)
- [ Accounting for rows read ](https://docs.turso.tech//billing-details/#accounting-for-rows-read)
    - [ Queries with aggregate functions ](https://docs.turso.tech//billing-details/#queries-with-aggregate-functions)

- [ Queries without a supporting index (full table scan) ](https://docs.turso.tech//billing-details/#queries-without-a-supporting-index-full-table-scan)

- [ Table joins, subqueries, and compound queries ](https://docs.turso.tech//billing-details/#table-joins-subqueries-and-compound-queries)

- [ Row updates ](https://docs.turso.tech//billing-details/#row-updates)

- [ ALTER TABLE row reads ](https://docs.turso.tech//billing-details/#alter-table-row-reads)

- [ Adding an index to a table with existing rows ](https://docs.turso.tech//billing-details/#adding-an-index-to-a-table-with-existing-rows)

- [ SQLite system tables ](https://docs.turso.tech//billing-details/#sqlite-system-tables)

- [ Commands that incur no row reads ](https://docs.turso.tech//billing-details/#commands-that-incur-no-row-reads)
- [ Accounting for rows written ](https://docs.turso.tech//billing-details/#accounting-for-rows-written)
    - [ ALTER TABLE row writes ](https://docs.turso.tech//billing-details/#alter-table-row-writes)

- [ Aborted transactions ](https://docs.turso.tech//billing-details/#aborted-transactions)
- [ Accounting for total storage ](https://docs.turso.tech//billing-details/#accounting-for-total-storage)
- [ Exceeding quotas ](https://docs.turso.tech//billing-details/#exceeding-quotas)
- [ Advice for reducing usage ](https://docs.turso.tech//billing-details/#advice-for-reducing-usage)
- [ Report issues with billing ](https://docs.turso.tech//billing-details/#report-issues-with-billing)


- [ 

Sign Up




 ](https://api.turso.tech/?webui=true&type=signup)
- [ 

Star Our Repo






 ](https://github.com/libsql/libsql)


Sign Up

Star Our Repo

- [ About ](https://turso.tech/about-us)
- [ Investors ](https://turso.tech/investors)
- [ Blog ](https://blog.turso.tech)


- [ Turso Discord ](https://discord.com/invite/4B5D7hYwub)
- [ libSQL Discord ](https://discord.gg/VzbXemj6Rg)
- [ Follow us on Twitter ](https://twitter.com/tursodatabase)
- [ Schedule a Zoom ](https://calendly.com/d/gt7-bfd-83n/meet-with-chiselstrike)


- [ Turso GitHub ](https://github.com/tursodatabase/)
- [ Turso extended GitHub ](https://github.com/turso-extended/)
- [ libSQL GitHub ](http://github.com/tursodatabase/libsql)


- [ Privacy Policy ](https://turso.tech/privacy-policy)
- [ Terms of Use ](https://turso.tech/terms-of-use)


Image: [ Turso logo ](https://docs.turso.tech/img/turso.svg)
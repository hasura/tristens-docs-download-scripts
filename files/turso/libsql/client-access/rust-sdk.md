# Rust SDK

## Installation​

Add the[ libsql-client crate ](https://crates.io/crates/libsql-client)to your project using `cargo` :

`$ cargo  add  libsql-client`

For CloudFlare Workers code that compiles to WASM, you must use a special
configuration:

`$ cargo  add  libsql-client --no-default-features -F workers_backend`

## Initialization​

Call the `Client::from_config` function to create a new Client object:

```
let  client  =   libsql_client :: Client :: from_config ( libsql_client :: Config   {
    url :   url :: Url :: parse ( "libsql://localhost:8080" ) . unwrap ( ) ,
    auth_token :   None ,
} )
. await
. unwrap ( ) ;
```

## Example data set​

All of the examples in this section assume tables and data established by these
statements:

```
create   table  example_users  (
    uid  text   primary   key ,
    email  text
) ;
create   table  example_scores  (
    uid  text ,
     level   integer ,
    score  integer ,
     primary   key   ( uid ,   level )
) ;
insert   into  example_users  values   ( 'uid1' ,   'foo@bar.com' ) ;
insert   into  example_users  values   ( 'uid2' ,   'baz@bar.com' ) ;
insert   into  example_scores  values   ( 'uid1' ,   1 ,   100 ) ;
insert   into  example_scores  values   ( 'uid1' ,   2 ,   95 ) ;
```

## Execute a single statement​

### SQL string argument​

```
let  rs  =  client . execute ( "select * from example_users" ) . await ? ;
// rs is a ResultSet object containing rows and columns
```

### Positional placeholders​

Create a new Statement using `Statement::with_args` and use the `args` macro to
specify the values to bind to the placeholders.

```
use   libsql_client :: { Statement ,  args } ;
let  rs  =  client
     . execute ( Statement :: with_args (
         "select score from example_scores where uid = ? and level = ?" ,
         args! ( "uid1" ,   2 ) ,
     ) )
     . await ? ;
// rs is a ResultSet object containing rows and columns
```

## Execute a batch of statements​

info

Be sure to read the[ common section on batches ](https://docs.turso.tech/libsql/client-access#batches)for libSQL clients to understand
their behavior.

```
use   libsql_client :: { Statement ,  args } ;
let  rss  =  client
     . batch ( [
         Statement :: with_args (
             "insert into example_users values (?, ?)" ,
             args! ( "uid3" ,   "uid3@turso.tech" ) ,
         ) ,
         Statement :: with_args (
             "insert into example_scores values (?, ?, ?)" ,
             args! ( "uid3" ,   1 ,   200 ) ,
         ) ,
     ] )
     . await ? ;
// rss is a Vec<ResultSet> containing results from all the queries
```

## Interactive transactions​

info

Be sure to read the[ common section on interactive transactions ](https://docs.turso.tech/libsql/client-access#interactive-transactions)for libSQL
clients to understand their behavior.

The following code uses an interactive transaction to update a user’s level
score, but only if it’s greater than the one that currently exists:

```
use   libsql_client :: { Statement ,  args } ;
let  uid  =   "uid1" ;
let  level  =   1 ;
let  new_score  =   200 ;
let  transaction  =  client . transaction ( ) . await ? ;
let  rs  =  transaction
     . execute ( Statement :: with_args (
         "select score from example_scores where uid = ? and level = ?" ,
         args! ( uid ,  level ) ,
     ) )
     . await ? ;
let  old_score  =  rs . rows . first ( ) . map ( | row |   & row . values [ 0 ] ) ;
let  old_score  =   match  old_score  {
     Some ( Value :: Integer   {  value :  i  } )   =>   * i ,
    _  =>   0 ,
} ;
if  new_score  >  old_score  {
    transaction
         . execute ( Statement :: with_args (
             "update example_scores set score = ? where uid = ? and level = ?" ,
             args! ( new_score ,  uid ,  level ) ,
         ) )
         . await ? ;
}
transaction . commit ( ) . await ? ;
```

## ResultSet​

A ResultSet struct contains values for the rows and columns returned by a query.

```
pub   struct   ResultSet   {
     pub  columns :   Vec < String > ,
     pub  rows :   Vec < Row > ,
     pub  rows_affected :   u64 ,
     pub  last_insert_rowid :   Option < i64 > ,
}
```

Each row is contained in a Row struct that provides the values of the row
available by column index.

```
pub   struct   Row   {
     pub  values :   Vec < Value > ,
}
```

Each Value can be one of the types supported by SQLite:

```
pub   enum   Value   {
     Null ,
     Integer   {
        value :   i64 ,
     } ,
     Float   {
        value :   f64 ,
     } ,
     Text   {
        value :   String ,
     } ,
     Blob   {
        value :   Vec < u8 > ,
     } ,
}
```

Your code will need to make an assumption or a decision about the type of each
value found in a Row.  The following code examines the first Value in the first
Row of a ResultSet and sets up a match for how to interpret it:

```
let  row  =  rs . rows . first ( ) . expect ( "one row" ) ;
let  value  =   & row . values [ 0 ] ;
match  value  {
     Value :: Null   =>   todo! ( ) ,
     Value :: Integer   {  value  }   =>   todo! ( ) ,
     Value :: Float   {  value  }   =>   todo! ( ) ,
     Value :: Text   {  value  }   =>   todo! ( ) ,
     Value :: Blob   {  value  }   =>   todo! ( ) ,
} ;
```

If your code is expecting a Text type (containing a Rust `&String` ), then you
could express that assumption like this:

```
if   let   Value :: Text   {  value  }   =  value  {
     println! ( "Text value as &String: {value}" ) ;
}   else   {
     return   Err ( "Expected a Text value" . into ( ) ) ;
}
```

- [ Installation ](https://docs.turso.tech//libsql/client-access/rust-sdk/#installation)
- [ Initialization ](https://docs.turso.tech//libsql/client-access/rust-sdk/#initialization)
- [ Example data set ](https://docs.turso.tech//libsql/client-access/rust-sdk/#example-data-set)
- [ Execute a single statement ](https://docs.turso.tech//libsql/client-access/rust-sdk/#execute-a-single-statement)
    - [ SQL string argument ](https://docs.turso.tech//libsql/client-access/rust-sdk/#sql-string-argument)

- [ Positional placeholders ](https://docs.turso.tech//libsql/client-access/rust-sdk/#positional-placeholders)
- [ Execute a batch of statements ](https://docs.turso.tech//libsql/client-access/rust-sdk/#execute-a-batch-of-statements)
- [ Interactive transactions ](https://docs.turso.tech//libsql/client-access/rust-sdk/#interactive-transactions)
- [ ResultSet ](https://docs.turso.tech//libsql/client-access/rust-sdk/#resultset)


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
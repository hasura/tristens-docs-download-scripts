# Creating an e-commerce store with Remix, Turso, Drizzle, and Cloudflare Workers

In this tutorial, we are going to learn how to build an e-commerce store “The
Mugs Store” using the titled stack and afterwards deploy it to Cloudflare
workers. The store builds upon the implementation that is listed on the[ Create a shopping cart using Qwik and Turso ](https://blog.turso.tech/create-a-shopping-cart-using-qwik-and-turso-b51994f6ab73), with the addition of user
authentication.

We are using the stack in question (Cloudflare Workers and Turso) to build The
"Mugs Store" since it makes for a good combination for an e-commerce website
offering low-latency for all visitors as Cloudflare workers places the compute
on the edge with a globally distributed network, and with Turso’s database
replication, we get to place the site’s data where our users are.

The complete source code to the project we will build in this tutorial can also
be[ found on GitHub ](https://github.com/turso-extended/app-the-mug-store)for reference.

[ Remix ](https://github.com/turso-extended/app-the-mug-store)is a full stack web framework that lets you focus on the user interface
and work back through web standards and deliver a fast, slick, and resilient
user experience.

[ Turso ](https://turso.tech)is the distributed database based on[ libSQL ](https://github.com/libsql/libsql#readme), the open-contribution
fork of SQLite.

[ Drizzle ](https://orm.drizzle.team)is a TypeScript Object-Relational Mapping tool (ORM) with support for
PostgreSQL, MySQL, and SQLite databases.

The tutorial has been broken down to the following steps for readability.

## Setting up the project​

In this step, you'll be walked through creating a new Remix project and setting
up some essential parts of the e-commerce store user interface (UI).

## Setting up Turso​

In this step, you'll be guided through creating a Turso database, acquiring the
database credentials required by the[ libSQL client library ](https://github.com/libsql/libsql-client-ts), and adding them as
the Remix app's environment variables.

## Configuring Drizzle​

In this step, you'll be guided through configuring Drizzle as the Remix app's
object-relational mapping (ORM) tool.

## Listing store items​

In this step, you will be walked through implementing the store's product
listing and it's associated components.

## User authentication​

In this step, we'll see how user authentication can be set up to guard some
parts of the store that should only be accessible to registered users.

## Adding the shopping cart​

In this step, we'll go through setting up the store's cart page, a mini cart
component that's accessible throughout the store, and implementing logic that
will help us manage the items within the cart.

## Checking out and placing orders​

In this step, we will take care of checking out customers that have added items
to their carts and want to place orders.

## Deploying the app to Cloudflare Workers​

In the final step we will go through the deployment of the e-commerce store to
Cloudflare Workers.

## More resources​

- [ Remix documentation ](https://remix.run/docs/en/1.18.1)
- [ Cloudflare Workers documentation ](https://workers.cloudflare.com/)
- [ Drizzle documentation ](https://orm.drizzle.team/)
- [ Example apps and more on github.com/turso-extended ](https://github.com/turso-extended)


- [ Setting up the project ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#setting-up-the-project)
- [ Setting up Turso ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#setting-up-turso)
- [ Configuring Drizzle ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#configuring-drizzle)
- [ Listing store items ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#listing-store-items)
- [ User authentication ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#user-authentication)
- [ Adding the shopping cart ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#adding-the-shopping-cart)
- [ Checking out and placing orders ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#checking-out-and-placing-orders)
- [ Deploying the app to Cloudflare Workers ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#deploying-the-app-to-cloudflare-workers)
- [ More resources ](https://docs.turso.tech//tutorials/e-commerce-store-codelab/#more-resources)


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
# Distributed Tracing

## Introduction​

Hasura Cloud projects have support for *distributed tracing* , a technique for debugging Hasura in production in the
context of the services it works with. These services might include your own Postgres database, any Remote Schemas,
Event Trigger webhook providers, action providers or authentication hooks. Distributed tracing attempts to give a
unified view into the performance characteristics of all of these components of your architecture.

## Visualizing traces​

The Hasura Pro Console makes it possible to view Hasura's own tracing data, by opening the details view for an operation
in the Operations tab:

Image: [ View timing data in the Operations tab ](data:image/png;base64,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)

Given that other system components will report their own tracing data to your APM system, and not to Hasura, it is not
possible to give a complete picture of a trace, but since Hasura sits in a central position in the architecture of many
systems, it can often give a reasonably comprehensive view of the provenance of data in your system.

For example, Hasura can report interactions with Postgres, Remote Schemas, Event Trigger webhooks and action handlers.

## APM system integration​

Hasura will report trace information to your APM or *application performance monitoring* system, where it can be
correlated with similar sources of data from other components of your service architecture.

If you are considering integrating Hasura with your APM system, please get in touch so that we can help to coordinate
that effort.

## Trace propagation​

At the boundaries between different services, tracing information needs to be shared in order for trace fragments from
different systems to be correlated with each other in the APM system. This is called *trace propagation* .

There are several subtly-incompatible proposals for trace propagation, which can make it difficult to arrange for any
two services to work together.

### Propagation to web services​

For propagation during a call to a web service over HTTP, Hasura currently implements the[ B3 propagation specification ](https://github.com/openzipkin/b3-propagation). This means that we send trace information
in various HTTP headers, which should be read and handled by any compatible web services.

If you are unsure how to implement B3 propagation in your own web service, the simplest thing to do is to read these
headers and pass them along to any HTTP services you call which also support B3 propagation, including Hasura itself.

In particular, if an Event Trigger webhook or action handler propagates these B3 headers back to Hasura, we will be able
to trace the entire interaction.

### Propagation via Postgres​

There is no standard method for trace propagation via Postgres transactions. For example, Event Triggers can be invoked
by mutations, and so their traces should be correlated.

For this reason, we have adopted our method of propagating a trace context in Postgres transactions.

The trace context will be serialized during mutations as a transaction-local variable, `hasura.tracecontext` . This value
has the Postgres type `json` , and it can be read in trigger functions and propagated to any downstream services.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#introduction)
- [ Visualizing traces ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#visualizing-traces)
- [ APM system integration ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#apm-system-integration)
- [ Trace propagation ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#trace-propagation)
    - [ Propagation to web services ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#propagation-to-web-services)

- [ Propagation via Postgres ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/#propagation-via-postgres)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)
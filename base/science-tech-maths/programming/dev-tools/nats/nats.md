# NATS

- [NATS](#nats)
  - [Introduction](#introduction)
  - [Subjects](#subjects)
  - [Core NATS](#core-nats)
    - [Publishers](#publishers)
    - [Subscribers (or consumers)](#subscribers-or-consumers)
    - [Queues](#queues)
  - [JetStream](#jetstream)
    - [Streams](#streams)
    - [Retention policies](#retention-policies)
    - [Publishing with JetStream](#publishing-with-jetstream)
    - [Consuming with JetStream](#consuming-with-jetstream)
      - [Push-based](#push-based)
      - [Pull-based](#pull-based)
      - [Ephemeral or durable](#ephemeral-or-durable)
      - [ACK](#ack)
  - [FAQ](#faq)
  - [Run a NATS server](#run-a-nats-server)
  - [Python client](#python-client)

## Introduction

Nats is a messaging system that is very fast and lightweight. It is written in Go and has clients for many languages.

NATS makes it easy for applications to communicate by sending and receiving messages. These messages are addressed and identified by subject strings, and do not depend on network location.

## Subjects

The subject is a string that can be anything. It is a way of grouping messages.

The dot character `.` is the token separator.

The asterisk character `*` is a token wildcard match: e.g `foo.*` matches `foo.bar`, `foo.baz`, but not `foo.bar.baz`.

The greater-than symbol `>` is a full wildcard match. It will match multiple tokens: e.g. `foo.>` matches `foo.bar`, `foo.baz`, `foo.bar.baz`, `foo.bar.1`, etc.

The wildcard `*` can appear multiple times in the same subject. Both types can be used as well. For example, `*.*.east.>` will receive `time.us.east.atlanta`.

## Core NATS

### Publishers

A publisher sends a message to a subject.

### Subscribers (or consumers)

If a subscriber is subscribed to a subject, it will receive all messages sent to that subject. Thus, it's by default a one-to-many relationship.

![](https://683899388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-22d59af386038cc2717176561ffc95c63c295926%2Fpubsub.svg?alt=media)

### Queues

NATS provides an additional feature named "queue", which allows subscribers to register themselves as part of a queue. Subscribers that are part of a queue, form the "queue group".

If a subscriber is registered based on a queue name, it will always receive messages it is subscribed to, based on the subject name. However, if more subscribers are added to the same queue name, they become a queue group, and only one randomly chosen subscriber of the queue group will consume a message each time a message is received by the queue group. Such distributed queues are a built-in load balancing feature that NATS provides.

If one subject is being listened to by several consumers with the same queue group, the message will go to a random consumer each time.

When you publish a message, for instance at the beginning of a request, every subscriber will receive the message. If subscribers form a queue group, only one subscriber will be picked at random to receive the message.

The choice to join a queue group is made when the subscription is created, by supplying an optional queue group name.

Queue group names follow the same naming rules as subjects. Foremost, they are case sensitive and cannot contain whitespace.

## JetStream

Core NATS is a fire-and-forget messaging system. It will only hold messages in memory and will never write messages directly to disk.

JetStream adds persistence to NATS. This means that messages can be stored on disk and replayed if a consumer is not available when a message is sent.

NATS JetStream offers persistence with "at-least-once" and "exactly-once" (within a time window) delivery.

JetStream provides both:

- the ability to consume messages as they are published (i.e. 'queueing')
- the ability to replay messages on demand (i.e. 'streaming').

### Streams

A stream is a messae store, a collection of messages.

A stream consumes normal subjects. It can consume several subjects at the same time. Any message sent to a subject will be stored in the stream on disk.

Each stream defines how messages are stored and what the limits (duration, size, interest) of the retention are.

Note that if no explicit subject is specified, the default subject will be the same name as the stream

![](https://683899388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-dedcc17f082fa1e39497c54ed8191b6424ee7792%2Fstreams-and-consumers-75p.png?alt=media)

In the image above, we have a stream named "ORDERS", that consumes  to all subjects starting with "ORDERS.".

### Retention policies

A message cannot stay forever in NATS. It will be deleted after a certain amount of time.

You can choose what kind of retention you want for each stream:

- limits: the number of messages to keep
- work queue: keep messages until they are acknowledged (provides the exactly-once consumption of messages in the stream)

### Publishing with JetStream

Changes nothing. You publish to a subject, and the message will be stored in the stream if the subject is consumed by the stream.

### Consuming with JetStream

A stream can also be used as a queue by setting the retention policy to WorkQueuePolicy.

JetStream provides streaming/replaying of messages. This means that a consumer can replay messages that were sent before it was created.

#### Push-based

The server will push messages to the consumer. It's the fastest way to consume messages. But serverload is higher.

#### Pull-based

The consumer will pull messages from the server, by batches if needed, for better performance.

#### Ephemeral or durable

A consumer is considered durable when an explicit name is set on the `Durable` field when creating the consumer, otherwise it is considered ephemeral.

Durables and ephemeral behave exactly the same except that an ephemeral will be automatically cleaned up (deleted) after a period of inactivity, specifically when there are no subscriptions bound to the consumer.

By default, durables will remain even when there are periods of inactivity (unless InactiveThreshold is set explicitly).

#### ACK

JetStream supports more than one kind of acknowledgment:

- Positive acknowledgements (ack) are the default.
- You can also send back negative acknowledgements. The message will be redelivered to another consumer.
- You can even send in progress acknowledgments (to indicate that you are still processing the message in question and need more time before acking or nacking it).

## FAQ

- Is there a message size limitation in NATS: Messages have a maximum size (which is set in the server configuration with max_payload) that is enforced by the server and communicated to the client during connection setup. The size is set to 1 MB by default, but can be increased up to 64 MB if needed (though we recommend keeping the max message size to something more reasonable like 8 MB).

## Run a NATS server

```bash
docker run --rm -p 4222:4222 nats -js
```

To subscribe to a subject:

```bash
nats --server localhost:4222 subscribe "some.subject.*"
```

Or with docker compose:

```yaml
nats_js_test:
image: nats:latest
command:
    - "-m"
    - "8222"
    - "--debug"
    - "--jetstream"
healthcheck:
    test:
    - "CMD"
    - "sh"
    - "-c"
    - "wget http://localhost:8222/healthz -q -O - | xargs | grep ok || exit 1"
    interval: 1s
    timeout: 3s
    retries: 5
ports:
    - 8222:8222
    - 4222:4222
```

## Python client

<https://github.com/airtai/faststream>

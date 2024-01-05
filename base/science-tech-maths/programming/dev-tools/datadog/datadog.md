# Datadog

## Logs format

Datadog has some reserved fields in the JSON structure and if you use these fields for something else, the log will not be indexed and then not visible in the log search page.
Here are the reserved fields:

- Date attributes: @timestamp, timestamp, _timestamp, Timestamp, eventTime, date, published_date, syslog.timestamp
- Host attributes: host, hostname, syslog.hostname
- Service attributes: service, syslog.appname, dd.service
- Status attributes: status, severity, level, syslog.severity
- Trace Id attributes: dd.trace_id, contextMap.dd.trace_id
- Message attributes: message, msg, log

So for example, if you use { "status": "SUCCESS" } in your JSON log, it will not be indexed because status accepts only log level values such as INFO, DEBUG, etc...

<https://docs.datadoghq.com/logs/log_collection/?tab=host#attributes-and-tags>

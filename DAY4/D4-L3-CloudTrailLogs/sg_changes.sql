select eventname, useridentity.username, sourceIPAddress, eventtime, requestparameters from cloudtrail_logs
where (requestparameters like '%sg-0d3e1594cac5f282e%')
and eventtime > '2018-01-15T00:00:00Z'
order by eventtime asc;
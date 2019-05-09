select useridentity.principalId, sourceipaddress, eventtime
from cloudtrail_logs
where eventname = 'TerminateInstances'
and eventtime >= '2018-11-01T00:00:00Z'
order by eventtime desc;
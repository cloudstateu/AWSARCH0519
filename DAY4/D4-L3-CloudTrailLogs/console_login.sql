select useridentity.username, sourceipaddress, eventtime
from cloudtrail_student10
where eventname = 'ConsoleLogin'
and eventtime >= '2018-11-04T00:00:00Z'
order by eventtime desc;
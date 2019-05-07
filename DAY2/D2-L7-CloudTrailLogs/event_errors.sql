select count (*) as TotalEvents, eventname, errorcode, errormessage 
from cloudtrail_logs
where errorcode is not null
and eventtime >= '2018-11-01T00:00:00Z' 
group by eventname, errorcode, errormessage
order by TotalEvents desc
limit 10;
select count (*) as TotalEvents, eventname, useridentity.invokedby
from cloudtrail_logs
where eventtime >= '2018-01-01T00:00:00Z' 
and useridentity.type = 'Root'
group by useridentity.username, eventname, useridentity.invokedby
order by TotalEvents desc;
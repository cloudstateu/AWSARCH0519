select count (*) as TotalEvents, useridentity.username
from cloudtrail_student14
where eventtime >= '2018-12-05T00:00:00Z' 
and useridentity.type = 'IAMUser'
group by useridentity.username
order by TotalEvents desc;
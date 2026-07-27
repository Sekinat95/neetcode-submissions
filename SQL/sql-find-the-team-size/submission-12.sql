-- Write your query below
select employee_id, team_size
from employee e
inner join (
    select team_id, count(*) as team_size
    from employee
    group by team_id
) t
on e.team_id = t.team_id






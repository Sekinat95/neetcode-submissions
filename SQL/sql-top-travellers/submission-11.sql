--with total_distance_per_user as (
--   select name, coalesce(sum(distance), 0) as travelled_distance
--  from users 
--   left join rides on rides.user_id = users.id
--   group by users.id, users.name
--)
--select name, travelled_distance
--from total_distance_per_user
--order by travelled_distance desc, name asc;

--------------------------

select name, coalesce(sum(distance), 0) as travelled_distance
from users u 
left join rides r on u.id = r.user_id
group by u.id, u.name
order by travelled_distance desc, name asc;













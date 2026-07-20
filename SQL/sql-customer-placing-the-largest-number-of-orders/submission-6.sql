-- Write your query below
--select customer_number 
--from orders 
--group by customer_number
--order by count(*) desc
--limit 1;


with customer_orders as (
    select count(order_number) as num_orders, customer_number
    from orders
    group by customer_number
)
select customer_number
from customer_orders
where num_orders=(select max(num_orders) from customer_orders)
limit 1;
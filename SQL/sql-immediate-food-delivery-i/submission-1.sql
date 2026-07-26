-- Write your query below
with immediate_orders as (
    select *, 
    case 
        when order_date = customer_pref_delivery_date then 1
        else 0
    end as is_immediate
    from delivery

)
select round(100.0 * sum(is_immediate)/count(*) , 2) as immediate_percentage
from immediate_orders

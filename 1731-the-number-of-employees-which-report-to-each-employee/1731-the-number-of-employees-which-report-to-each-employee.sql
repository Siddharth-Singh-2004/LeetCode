# Write your MySQL query statement below
select employees.employee_id, employees.name, count(*) as reports_count, round (avg(tmp1.age), 0) as average_age
from employees,
(select employee_id, name, reports_to, age from employees
where reports_to is not null) as tmp1
where employees.employee_id = tmp1.reports_to
group by employees.employee_id, employees.name
order by employees.employee_id;
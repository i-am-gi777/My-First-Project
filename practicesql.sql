SELECT * FROM CUSTOMER;

SELECT COUNTRY FROM CUSTOMER 
WHERE COUNTRY IN ('USA');

SELECT firstname, lastname 
from customer;

select count (*) from customer;

select distinct count(*)
 from customer;

select country from customer;  

select count(country)
 from customer;

select distinct country from 
customer;

select count(distinct country),
count(state),count(customerid)
from customer where country='USA';

select max(country),
min(country) from customer ;

 select country, max(country)
 from customer
 group by country;
 
 select country, 
 count (country)
 from customer 
 group by country;
 
 select  * from customer
 where country in ('Brazil','USA');
 
 
  select country, 
 count (country)
 from customer 
 group by country
 in('Brazil');
  
  select * from customer 
  where (country='USA'or 
  state='SP');
  
  select * from customer 
  where country='USA'
  and (customerid>20);
  
  select state from customer 
  where state in
  (select state from customer);
  
  
 select id from workers 
 intersect
 select id from address;
 
 select id from workers 
 union
 select id from  address;
 
 select id from workers 
 union all
 select id from  address;
 
 select id from workers 
 except 
 select id from address;
 
 select 
 workers.id, workers.name,workers.amount,
 address.id,address.city,address.country
 from workers 
 join address 
 on  workers.id=address.id;
 
 select 
 workers.id, workers.name,workers.amount,
 address.id,address.city,address.country
 from workers 
right join address 
 on  workers.id=address.id;
 
 select * from workers 
 where id between 1 and 3;
 
 select * from workers 
 where id>2 or id<3;
 
 select * from workers 
 order by id desc;

  select * from workers 
 order by id,name desc;
  
  select amount from workers
  group by amount 
  having  id>3;
  
  select 
  id,
  name,
  amount,
  case 
     when id = '1' then '001'
  else 'na'
  end as no 
  from workers;
  
  select * from workers;
  
  select * from workers 
  where name like's%';
  
  select * from workers 
  where name not like 's%';
  
  select * from workers 
  where name like'%rr%';
  
  select * from workers 
  where exists(
  select 1 as result 
  from address where workers.id=
  address.id);
  
  update workers 
  set id=5
  where rowid =5;
  
  update workers
  set amount =amount + 500;
  
  select amount ,amount+500 as value
  from workers;
  
  select * from invoice;
  select Billingstate  from invoice ;
  select *from invoice 
  where BillingState like 's%'
  
  create table data(id integer,
  name text,
  amount decimal);
  
  insert into data
  (id,name,amount)
  values
  (1,'john',2000),
  (2,'sam',3000),
  (3,'won',4000),
 (4,'rome',5000); 
  
  select distinct * from data;
   
  select * from invoice;
  
  select Billingcity ,count(Invoice.BillingCity )
  from Invoice 
 group by Billingcity = 'paris';


 -- (1) Setup

-- Create the table
CREATE TABLE agents (
    id INTEGER,
    sal INTEGER,
    dept TEXT
);

-- Insert data into the table
INSERT INTO agents (id, sal, dept) VALUES (117, 100, 'D1'),
(127, 200, 'D2'),
(137, 50, 'D2'),
(147, 60, 'D1'),
(157, 60, 'D1'),
(167, 50, 'D1');


select *
from agents;


-- (2) Rank on All Rows
select
id,
sal,
dept,
rank() 
over (order by sal desc) as sal_rank
from agents;

select *
from (select
id,
sal,
dept,
dense_rank() over (order by sal desc) as sal_rank
from agents)
where sal_rank = 2;

-- (2) Rank on Departmen…
 
 select *
from (select
id,
sal,
dept,
dense_rank() over (partition by dept order by sal desc) as sal_rank
from agents)
where sal_rank = 2;
 
 
select * from invoice; 


 
 --find the total billingcountry usa  

 select BillingCountry,count(1) as sum
 from Invoice 
 group by BillingCountry 
 having BillingCountry = "USA";
 


 --find customer id of usa
  select CustomerId 
 from Invoice 
where BillingCountry = "USA";
 
 
simple avg

select total from invoice

 select 
 sum(Total),
 avg(Total)
 from invoice;
 
 
 select BillingCountry,sum(total),avg(total) as sum
 from Invoice 
 group by BillingCountry 
 having BillingCountry = "USA";
 
 lenght and 3 letters in billingcountry
 
 select substr(BillingCountry,1,3),
 LENGTH(BillingCountry) 
 from invoice;
 


 select BillingCountry, max(total),min(total)
 from Invoice 
 group by BillingCountry 
 having BillingCountry = "USA";
 
 select InvoiceDate,
 datediff(year=2025,InvoiceDate,getdate()),*
 from invoice;
 
 
 select * from invoice;
 
 select CustomerId, 
 InvoiceDate, 
 BillingCity 
 from invoice;
 
 select count(customerID)
 from invoice;
 
 select distinct BillingCity,
 count(distinct BillingCity)
 from invoice;
 
 select count(BillingCIty)
 from Invoice 
 where BillingCity ='Berlin';
 
 select CustomerId, Total,
 rank() over ( order by total desc) as rank
 from Invoice ;
 
 select *
 from(
 select CustomerId, Total,
 rank() over ( order by total desc) as rank
 from invoice)
where rank = 7;
 
 
  select *
 from(
 select CustomerId, Total,
dense_rank() over ( order by total desc) as rank
 from invoice)
where rank = 7;

CREATE TABLE TaxUpdatedReturns (
    SlNo INT,
    Name VARCHAR(255),
    Status VARCHAR(50),
    Amount INT
);

INSERT INTO TaxUpdatedReturns (SlNo, Name, Status, Amount) VALUES
(1, 'AijaazHussainMohammed_Updatedreturn_2425', 'Filed', 700),
(2, 'VenkateswarluCherupalli_Updatedreturn_2425', 'Filed', 700),
(3, 'LakshmiPathiKanuboina_Updatedreturn_2425', 'Filed', 700),
(4, 'RajuKomanolu_Updatedreturn_2425', 'Filed', 700),
(5, 'AijaazHussainMohammed_Updatedreturn_2324', 'Filed', 700),
(6, 'VenkateswarluCherupalli_Updatedreturn_2324', 'Filed', 700),
(7, 'Kare Vaikunta_Updated return_24-25', 'Pending', NULL);

select distinct * from TaxUpdatedReturns;



 select distinct * FROM TaxUpdatedReturns;

select * from customer;

create table serial(
No);

insert into serial(No)
values
(1),(2),(3),(4),(5),(6),(7);

select * from serial



WITH RECURSIVE Days(day) AS (
    SELECT DATE('2025-03-01')  -- Start date
    UNION ALL
    SELECT DATE(day, '+1 day')  -- Add 1 day
    FROM Days
    WHERE day < DATE('2025-03-31')  -- End date
)
SELECT day FROM Days;


select * from invoice;

select BillingCity from invoice;

select BillingCity ,count(*) as count_order
from invoice
where BillingCity ='Berlin'
group by BillingCity
having count_order > 1
order by count_order ASC 





--create a table
CREATE TABLE employees (
    id integer,
    name text,
    salary integer
);

--insert into data into table
INSERT INTO employees (id, name, salary) VALUES
(1, 'Alice', 50000),
(2, 'Bob', 60000),
(3, 'Charlie', 70000),
(4, 'David', 60000),
(5, 'Eve', 90000),
(6, 'Frank', 75000),
(7, 'Grace', 85000),
(8, 'Hank', 90000);

--use select to retrive data
SELECT distinct * FROM employees;

--Find the second high salary employee

--group & order by salaries of employees for finding high salary employees
  SELECT distinct * FROM employees
  GROUP BY salary 
  ORDER by salary desc;

--given the rank to salaried employees 
  select name, salary,rank from
  (select name, salary,dense_rank() 
  over(order by salary desc)as rank
  from employees);
  
 --finding 2nd high salary employee from table
  SELECT * FROM
  (SELECT id,name,salary, 
  DENSE_RANK()
  OVER( ORDER by salary DESC)  as rank 
  FROM employees)
  WHERE rank = 2;
 
 
 --Create the employee table

CREATE TABLE employees (
id integer,
name text,
salary integer
);

--Insert sample employees data

INSERT INTO  employees 
(id, name, salary)
values
(1, "Alice", 55000),
(2, "Bob", 60000),
(3, "Charlis", 75000),
(4, "David", 50000),
(5, "Emma", 65000);

--select all employees

SELECT * FROM employees;

--Find the second high salary employee

--group & order by salaries of employees for finding high salary employees
  SELECT * FROM employees
  GROUP BY salary 
  ORDER by salary desc;

--given the rank to salaried employees 
  select name, salary,rank from
  (select name, salary,rank() 
  over(order by salary desc)as rank
  from employees);
  
 --finding 2nd high salary employee from table
  SELECT * FROM
  (SELECT id,name,salary, 
  DENSE_RANK()
  OVER( ORDER by salary DESC)  as rank 
  FROM employees)
  WHERE rank = 2;
  

create table workers(
id integer, name text, amount decimal);

 insert into workers(
 id, name, amount)
 VALUES 
 (1, 'amay', 1000),
 (2, 'sani', 2000),
 (3,'jerry',3000),
 (4,'jerry',4500);
 
 select * from workers;
 
 create table address(
 id integer, city text, country text);
 
 insert into address (
 id, city, country)
 values
 (1, 'delhi','india'),
 (2, 'hyderabad','india'),
 (3, 'vijayawada', 'india'),
 (4,'vizag','india');
 
 select distinct * from  address;

SELECT distinct
workers.id,
workers.name, 
workers.amount,
address.id,
address.city,
address.country 
FROM workers 
INNER JOIN address 
ON workers.id = address.id;

select distinct * from workers;

select distinct id from workers 
where name = 'sani';

select distinct id ,name from workers
where name in ( 'jerry','sani');

select distinct id,name from workers 
where id between 2 and 3; 


for first letter 
----------------
select * from workers 
where name like 's%'or name like 'j%';

in middile any letter
---------------------
select * from workers 
where name like '%rr%';

second letter

---------------
select * from workers 
where name like'_a%'
order by name;

SELECT distinct amount 
FROM workers
UNION ALL
SELECT SUM(amount) 
FROM workers;

select distinct name from workers;

select count(name)from workers
where name like '%rr%';

select max (id),min(id)
from workers;

select id from workers 
where group by name;
  

  
  

 
 
 
 
 
 
 





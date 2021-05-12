
--main table
create table users(
id serial primary key,
first_name varchar(255) not null,
last_name text,
age int,
email text unique not null
);
-- alt tables
--  1 to m
-- 1 to many
create table Coreid (
id serial primary key,
title text not null,
"CID" int reference users(id) not null
);

insert into posts
    (title, "creatorId")
values ('halo2', 1);

drop table users

insert into users 
( id , first_name, last_name, age , email)
values
( default , 'Bill', 'Billy', 19, 'steev@gmail.com')

alter table users drop column age;
alter table users add column age int;
  
select * from users;  

--if needed
update users
set age = age + 1;
where age *;

select * from users;

select * from users where id = 2 or id = 3;

--
delete from users
where last_name is null;

create table comments (
    id serial primary key,
    message text not null,
    post_id int references posts(id),
    creator_id int references users(id)
);

insert into comments
(message, post_id, creator_id)
values ('hello, nice post!', 2, 4);


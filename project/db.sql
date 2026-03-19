create database school;
use school;
create table students (
    id int primary key auto_increment,
    name varchar(255) not null,
    marks int not null
);
insert into students (id, name, marks) values ('Alice', 85);
insert into students (id, name, marks) values ('Bob', 90);
insert into students (id, name, marks) values ('Charlie', 78);

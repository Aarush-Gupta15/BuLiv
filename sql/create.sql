CREATE DATABASE BULIV;
USE BULIV;

/* CREATE TABLE FOR CREATING THE PROGRAM */

CREATE TABLE PROGRAM(
ID INT PRIMARY KEY auto_increment,
NAME VARCHAR(100));

/* creating table for students*/
CREATE TABLE STUDENTS(
ID INT PRIMARY KEY auto_increment,
MOBILE varchar(20) NOT NULL,
FIRST_NAME varchar(100),
SECOND_NAME varchar(100),
COURSE_ID INT(10),
UNIQUE (MOBILE)
);
show tables
select * from students

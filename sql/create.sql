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


CREATE TABLE ROOMS(
ID INT PRIMARY KEY auto_increment,
BLOCK_NAME varchar(20) NOT NULL,
CAPACITY INT,
NO_STUDENTS INT
);




CREATE TABLE ROOM_ALLOTMENT(
ID INT PRIMARY KEY auto_increment,
STUDENT_ID INT,
ROOM_ID varchar(10),
FROM_DATE DATE,
TO_DATE DATE
);



show tables;
select * from students;

use BULIV;
delete from room_allotment;
delete from rooms;
delete from students;
alter table room_allotment AUTO_INCREMENT = 1;
alter table rooms AUTO_INCREMENT = 1;
alter table students AUTO_INCREMENT = 1;


insert into rooms(BLOCK_NAME,CAPACITY,NO_STUDENTS) VALUES ("A1",2,0);
insert into rooms(BLOCK_NAME,CAPACITY,NO_STUDENTS) VALUES ("A2",3,0);
insert into students(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES ("8826670530","AARUSH","GUPTA",1)
insert into students(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES ("8966705370","SATYAM","THAKUR",3)
insert into students(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES ("9910202221","RAMESH","SHARMA",1)
insert into students(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES ("6623291233","VINAY","RAWAL",2)
insert into students(MOBILE,FIRST_NAME,SECOND_NAME,COURSE_ID) VALUES ("7222121212","VIKAS","TYAGI",1)



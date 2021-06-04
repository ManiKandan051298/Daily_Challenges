import sqlite3
conn=sqlite3.connect('mydb.db')
import datetime
# create database for employee

# # conn.execute("create table car(id int primary key,name varchar,startdate date, enddate date,status varchar)")
# # conn.execute("create table employee(id int primary key,name varchar,status varchar)")

# # conn.execute("create table register(id int primary key,today_date date,car_id int,employeeid1 int, employeeid2 int,clocked varchar)")


# # insert value for employee

# sql='insert into employee(id,name,status) values(?,?,?)'
# data=[
# #     (1,'a','available'),
# #     (2,'b','available'),
# #     (3,'c','available'),
# #     (4,'d','available'),
# #     (5,'e','available'),
# #     (6,'f','available'),
# #     (8,'g','available'),
# #     (7,'h','available'),
# #     (9,'i','available'),
# #     (10,'j','available'),
# #     (11,'k','available')
#       (12,'l','free'),
#     (13,'m','free'),
#     (14,'n','free'),
#     (15,'o','free'),
  
    
    
# ]

# with conn:
#     conn.executemany(sql,data)

# conn.commit()


# # insert values in cars



# # sql='insert into car(id,name,startdate,enddate,status) values(?,?,?,?,?)'

# # data=[
# #     (1,'bmw',"2021-05-28","2021-06-05","working"),
# #     (2,'bmw',"2021-05-26","2021-06-03","working"),
# #     (3,'suzuki',"2021-05-25","2021-06-02","working"),
# #     (4,'tata',"2021-05-20","2021-06-01","working"),
# #     (5,'honda',"2021-05-21","2021-06-02","working"),
# # ]

# # with conn:
# #     conn.executemany(sql,data)

# # conn.commit()



# # insert into register


# # sql='insert into register(id,today_date,car_id,employeeid1,employeeid2,clocked) values(?,?,?,?,?,?)'

# # data=[
# #     (1,"2021-05-20",4,1,2,"in"),
# #     (2,"2021-05-22",4,1,2,"in"),
# #     (3,"2021-05-24",4,1,2,"in"),
# #     (4,"2021-05-26",4,1,2,"in"),
# #     (5,"2021-05-28",4,1,2,"in"),
# #     (6,"2021-05-30",4,1,2,"in"),

# #     (7,"2021-05-21",5,3,4,"in"),
# #     (8,"2021-05-23",5,3,4,"in"),
# #     (9,"2021-05-25",5,3,4,"in"),
# #     (10,"2021-05-27",5,3,4,"in"),
# #     (11,"2021-05-29",5,3,4,"in"),
# #     (12,"2021-06-01",5,3,4,"in"),

# #      (13,"2021-05-25",3,5,6,"in"),
# #     (14,"2021-05-27",3,5,6,"in"),
# #     (15,"2021-05-29",3,5,6,"in"),
# #     (16,"2021-06-01",3,5,6,"in"),


# #     (17,"2021-05-26",2,7,8,"in"),
# #     (18,"2021-05-28",2,7,8,"in"),
# #     (19,"2021-05-30",2,7,8,"in"),
# #     (20,"2021-06-02",2,7,8,"in"),    


# #     (21,"2021-05-28",1,9,10,"in"),
# #     (22,"2021-05-30",1,9,10,"in"),
# #     (23,"2021-06-02",1,9,10,"in"),
# #     (24,"2021-06-04",1,9,10,"in"),
# #   ]

# # with conn:
# #     conn.executemany(sql,data)

# # conn.commit()


# # knowing how many employees showed work on a specific day
# # ans=conn.execute('select employeeid1,employeeid2 from register where today_date="2021-05-28"')
# # value=[]
# # for i in ans:
# #     value.extend([i[0],i[1]])

# # for i in value:
# #     for row in conn.execute('SELECT * FROM employee where  id == ?',[i]):
# #         print(row)


# # knowing who worked on a specfic car

# # ans=conn.execute('select employeeid1,employeeid2 from register where car_id=1')
# # value=[]
# # for i in ans:
# #     value.extend([i[0],i[1]])
# # value=set(value)
# # value=list(value)
# # for i in value:
# #     for row in conn.execute('SELECT * FROM employee where  id == ?',[i]):
# #         print(row)

# how long they took to complete their task
# ans=conn.execute("SELECT  strftime('%d', '2021-06-05') - strftime('%d', enddate) FROM car where id=2")
# print(ans)
# for i in ans:
#     print(i)


# # which employee  is free to take up a new task
# ans=conn.execute('select * from employee where status="free"')
# for i in ans:
#     print(i)




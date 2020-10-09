--


INSERT INTO movies(id,title,release_date) values(1,'Avengers End Game','2020-06-01');
INSERT INTO movies(id,title,release_date) values(2,'Pursuit of happiness','2014-05-01');
INSERT INTO movies(id,title,release_date) values(3,'Dark Night','2019-04-01');
INSERT INTO movies(id,title,release_date) values(4,'Batman Begins','2015-03-20');
INSERT INTO movies(id,title,release_date) values(5,'sherlock holmes','2014-02-11');

movie1 = Movie(title='Avengers End Game', release_date='2020-06-01')
movie2 = Movie(title='Pursuit of happiness', release_date='2014-05-01')
movie3 = Movie(title='Dark Night', release_date='2019-04-01')
movie4 = Movie(title='Batman Begins', release_date='2015-03-20')
movie5 = Movie(title='sherlock holmes', release_date='2014-02-11')


INSERT INTO actors(id,name,age,gender) values('Brad Pitt',40,'Male');
INSERT INTO actors(id,name,age,gender) values('Morgan Freeman',33,'Male');
INSERT INTO actors(id,name,age,gender) values('Robert Downey Jr',50,'Male');
INSERT INTO actors(id,name,age,gender) values('Benedict Cumberbatch',30,'Male');
INSERT INTO actors(id,name,age,gender) values('Will Smith',44,'Male');
INSERT INTO actors(id,name,age,gender) values('Jay Bendict',60,'Male');

actor1 = Actor(name='Brad Pitt',age=40,gender='Male')
actor2 = Actor(name='Morgan Freeman',age=33,gender='Male')
actor3 = Actor(name='Robert Downey Jr',age=50,gender='Male')
actor4 = Actor(name='Benedict Cumberbatch',age=30,gender='Male')
actor5 = Actor(name='Will Smith',age=44,gender='Male')
actor6 = Actor(name='Jay Bendict',age=60,gender='Male')

-- Completed on 2020-05-24 02:24:00

--
-- PostgreSQL database dump complete
--


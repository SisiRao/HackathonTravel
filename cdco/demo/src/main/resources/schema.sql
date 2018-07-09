DROP TABLE IF EXISTS system;
CREATE TABLE system (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  lastaudit DATE NOT NULL,
  PRIMARY KEY (id));

DROP TABLE IF EXISTS travelplan;
create table travelplan(
  plan_id int not null auto_increment,
  time_range varchar(100),
  place_list varchar(100),
  schedule varchar(1900),
  primary key (plan_id));

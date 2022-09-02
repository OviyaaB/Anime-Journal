--user
create table user_details (
	user_id SERIAL, 
	user_name varchar(100) unique not null, 
	first_name varchar(100) not null,
	last_name varchar(100), 
	email varchar(75) not null, 
	password varchar(20) not null, 
	primary key(user_id)
)

--anime
create table anime (
	anime_id varchar unique not null,
	anime_name varchar(150), 
	anime_genre varchar,
	anime_ratings varchar(100) check (anime_ratings > 0),
	anime_episodes varchar(100),
	primary key(anime_id)
)

--diary
create table diary(
	user_id integer not null,
	anime_id varchar not null,
	date_watched timestamp,
	FOREIGN KEY (user_id) REFERENCES user_details(user_id),
	FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
)

--scores
create table scores(
	user_id integer not null,
	anime_id varchar not null,
	overall integer check (overall > 0),
	story integer check (story > 0),
	animation integer check (animation > 0),
	character integer check (character > 0),
	background_score integer check (background_score > 0),
	FOREIGN KEY (user_id) REFERENCES user_details(user_id),
	FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
)


--services
create table services(
	anime_id varchar not null,
	streamed_on varchar,
	subscription_required boolean,
	subscription_fee integer,
	languages varchar(100),
	FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
)

--likes
create table likes(
	user_id integer not null,
	anime_id varchar not null,
	rating integer,
	review varchar(200),
	has_spoilers boolean,
	FOREIGN KEY (user_id) REFERENCES user_details(user_id),
	FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
)

--wishlist
create table wish_list(
	user_id integer not null,
	anime_id varchar not null,
	FOREIGN KEY (user_id) REFERENCES user_details(user_id),
	FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
)


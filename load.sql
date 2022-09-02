
--Insertion: 

-- Anime

COPY anime FROM '/Users/user/Desktop/animes.csv' CSV

-- Ensure animes.csv file is present in your desktop directory and provide the proper directory. (user has to be replaced with the Actual account name)
-- The above command works for mac OS. For windows, The complete file directory has to be provided.

-- User Details 

Insert into user_details(user_name, first_name, last_name, email, password) 
SELECT md5(RANDOM()::TEXT), md5(RANDOM()::TEXT), md5(RANDOM()::TEXT), 'user_' || seq || '@' || (
    CASE (RANDOM() * 2)::INT
      WHEN 0 THEN 'gmail'
      WHEN 1 THEN 'hotmail'
      WHEN 2 THEN 'yahoo'
    END
  ) || '.com' AS email,  substr(md5(random()::text), 0, 19) FROM GENERATE_SERIES(1, 10000) seq;



-- Diary 

INSERT INTO diary(user_id, anime_id, date_watched)
SELECT floor(random() * (10000-2+1) + 2)::int, anime_id, timestamp '2022-01-10 20:00:00' +
       random() * (timestamp '2000-01-10 20:00:00' -
                   timestamp '2022-01-10 10:00:00') FROM anime limit 5000;



-- Scores

INSERT INTO scores(user_id, anime_id, overall, story, animation, character, background_score)
SELECT distinct on (anime_id) 
floor(random() * (10000-2+1) + 2)::float, 
anime_id, 
floor(random() * (10-1+1) + 1)::int,  
floor(random() * (10-1+1) + 1)::int,
floor(random() * (10-1+1) + 1)::int,
floor(random() * (10-1+1) + 1)::int,
floor(random() * (10-1+1) + 1)::int
FROM anime limit 10000;


-- wish list 

INSERT INTO wish_list(user_id, anime_id)
SELECT distinct on (anime_id) 
floor(random() * (10000-2+1) + 2)::float, 
anime_id
FROM anime limit 3000;


-- likes 

Insert into likes(user_id, anime_id, rating, review, has_spoilers) 
SELECT distinct on (anime_id) 
floor(random() * (10000-2+1) + 2)::float, 
anime_id, 
floor(random() * (10-1+1) + 1)::int,  
(
    CASE (RANDOM() * 2)::INT
      WHEN 0 THEN 'Good'
      WHEN 1 THEN 'Average'
      WHEN 2 THEN 'Bad'
    END
) AS review,  
(
    CASE (RANDOM() * 1)::INT
      WHEN 0 THEN TRUE
      WHEN 1 THEN FALSE
    END
) AS has_spoilers
FROM anime, GENERATE_SERIES(1, 8000) seq;


-- Services

Insert into services(anime_id, streamed_on, subscription_required, subscription_fee, languages) 
SELECT distinct on (anime_id) 
anime_id, 
(
    CASE (RANDOM() * 4)::INT
      WHEN 0 THEN 'Netflix'
      WHEN 1 THEN 'Amazon Prime Video'
      WHEN 2 THEN 'Hulu'
	  WHEN 3 THEN 'HBO Max'
      WHEN 4 THEN 'Paramount'
    END
) AS streamed_on,  
(
    CASE (RANDOM() * 1)::INT
      WHEN 0 THEN TRUE
      WHEN 1 THEN FALSE
    END
) AS subscription_required,
floor(random() * (100-45+1) + 45)::float, 
(
    CASE (RANDOM() * 4)::INT
      WHEN 0 THEN 'English'
      WHEN 1 THEN 'English, Hindi, French'
      WHEN 2 THEN 'English, Japanese, Spanish, French'
	  WHEN 3 THEN 'English, Mandarin, Korean, Chinese'
      WHEN 4 THEN 'Tibetian, Italian, Tamil, Dutch, Telugu'
    END
) AS languages  
FROM anime, GENERATE_SERIES(1, 9000) seq;



CREATEREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age DATE
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Good Will Hunting', 
    'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
    1
    ),
    ( 'Oceans Eleven', 
    'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
    2);

CREATE TABLE producers (
    producer_id SERIAL PRIMARY KEY,
    movie_id INT,
    producer_name VARCHAR(50),
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

INSERT INTO producers (movie_id, producer_name)
VALUES (1, 'John Doe');

SELECT movies.movie_id, movies.movie_name, producers.producer_name
FROM movies
INNER JOIN producers ON movies.movie_id = producers.movie_id;
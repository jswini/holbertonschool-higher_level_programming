-- This script outputs all shows that have at least 1 genre
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
    FROM tv_shows
    RIGHT JOIN tv_show_genres
    ON show_id
    ORDER BY tv_shows.title, tv_show_genres.genre_id;

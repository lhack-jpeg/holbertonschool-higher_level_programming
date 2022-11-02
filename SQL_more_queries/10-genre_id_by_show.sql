-- Task 10: Genre ID by show
-- Script that list all shows in Database with one Genre Linked.
SELECT
	tv_shows.title,
	tv_show_genres.genre_id
from tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, genre_id;

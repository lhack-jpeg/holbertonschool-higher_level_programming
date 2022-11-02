-- Task 12: No Genre
-- Script to show TV shows without a Genre attached
SELECT
 	title,
	tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres on id = tv_show_genres.show_id
WHERE genre_id IS NULL;

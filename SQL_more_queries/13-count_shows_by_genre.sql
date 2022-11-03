-- Task 13
-- Returns a list and count of all Genres in the database
SELECT
	tv_genres.name as 'genre',
	COUNT(genre_id) AS 'number_of_shows'
FROM tv_show_genres
LEFT JOIN tv_genres
     ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;

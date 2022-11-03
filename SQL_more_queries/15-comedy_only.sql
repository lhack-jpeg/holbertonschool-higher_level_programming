
-- Task 15: Comedy only
-- Return the name of the shows that have the genre comedy
SELECT
	title
FROM tv_shows
LEFT JOIN tv_show_genres
     ON tv_show_genres.show_id = id
INNER JOIN tv_genres
      ON tv_genres.id = tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy"
ORDER BY title ASC;

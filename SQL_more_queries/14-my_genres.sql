-- Task 14: My genres
-- Return the name of the genres attached to the show "Dexter"
SELECT
	tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_genres
     ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
      ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = "Dexter"
ORDER BY `name` ASC;

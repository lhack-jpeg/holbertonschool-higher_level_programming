-- Task 100: Not my genres
-- Return the name of the genres  not attached to the show "Dexter"
SELECT
	name
from tv_genres
WHERE name NOT IN
(SELECT
	tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_genres
     ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
      ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = "Dexter")
ORDER BY name ASC;

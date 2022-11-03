-- Task 11: Genre ID for all shows
-- Script that list all shows in Database
SELECT
	title,
	tv_genres.name
from tv_shows
LEFT OUTER JOIN tv_show_genres
     ON tv_show_genres.show_id = id
LEFT OUTER JOIN tv_genres
      ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;

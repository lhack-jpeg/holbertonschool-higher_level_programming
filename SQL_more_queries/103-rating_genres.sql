-- Task 20: Best Genre
-- Find the rating for each Genre
SELECT
	tv_genres.name,
	SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_show_genres
INNER JOIN tv_genres
      ON tv_genres.id = genre_id
LEFT JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY genre_id
ORDER BY rating DESC;

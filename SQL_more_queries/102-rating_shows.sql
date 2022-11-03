-- Task 19: Rotten Tomatoes
-- List show by their ratings summed up in DESC order.
SELECT
	tv_shows.title,
	SUM(rate) AS 'rating'
FROM tv_show_ratings
LEFT JOIN tv_shows
     ON tv_shows.id = show_id
GROUP BY show_id
ORDER BY rating DESC;

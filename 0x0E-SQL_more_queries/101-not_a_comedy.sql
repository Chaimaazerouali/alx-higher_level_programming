-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- uses a database to list all rows not linked to one row

SELECT DISTINCT tv_shows.title FROM tv_show_genres RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title NOT IN (SELECT tv_shows.title FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = "Comedy") ORDER BY tv_shows.title;

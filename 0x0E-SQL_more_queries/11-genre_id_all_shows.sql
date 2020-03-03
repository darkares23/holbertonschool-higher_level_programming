-- hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
SELECT tv_shows.title, tv_shows_genres.genre.id FROM tv_shows
LEFT OUTER JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY title, genre_id ASC;

-- list all shows contained in hbtn_0d_tvshows having at least 1 genre
-- each record displays tv_shows.tile tv_show_genres.genre_id
-- results soretd in ascending order by
-- tv_shows.title tv_show_genres.genres_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

def search_games(keyword):

    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        keyword_lower = keyword.lower()

        cursor.execute("""
            SELECT id, name, releaseYear
            FROM Game
            WHERE LOWER(name) LIKE ?
            ORDER BY name;
        """, (f"%{keyword_lower}%",))

        return cursor.fetchall()


games = search_games("zel")

for game in games:
    print(game)

    
import csv

def main():
    playtest_hash = {}
    points_hash = {'In Person': 5, 'Virtual': 3}

    with open('playtesting.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] in playtest_hash:
                playtest_hash[row['name']] += points_hash[row['location']]
            else:
               playtest_hash[row['name']] = points_hash[row['location']]

    sorted_p_hash = {k: v for k, v in sorted(playtest_hash.items(), key=lambda item: item[1], reverse = True)}
    page = LeaderboardPage(sorted_p_hash)
    page.generate()

class LeaderboardPage:
    def __init__(self, players):
        self.players = players

    def generate(self):
        player_table = ""
        position = 1
        for p in self.players:
            player_table += self.leaderboard_row(position, p, self.players[p])
            position += 1
    
        page = ""
        page += self.open_html()
        page += self.head()
        page += self.body_opening()
        page += player_table
        page += self.body_closing()

        f = open("index.html", "w")
        f.write(page)
        f.close()

    def open_html(self):
        return "<html>"

    def close_html(self):
        return "</html>"
  
    def head(self):
        return """<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Attack on Scraptown Playtest Leaderboard</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css">
        </head>"""
  
    def body_opening(self):
        return """<body>
        <section class="section">
            <div class="content">
            <h1>Attack on Scraptown Playtesting Leaderboard</h1>
            </div>
            <div class="columns">
            <div class="column">
                <table class="table">
                <thead>
                    <tr>
                    <th><abbr title="Number">#</abbr></th>
                    <th><abbr title="Name">Name</abbr></th>
                    <th><abbr title="Points">Pts</abbr></th>
                    </tr>
                </thead>
                <tbody>"""
  
    def leaderboard_row(self, position, name, points):
        return "<tr><th>" + str(position) + "</th><td>" + str(name) +  "</td><td>" + str(points) + "</td></tr>"

    def body_closing(self):
        return """</tbody>
            </table>
        </div>
        <div class="column content">
            <p>
            This is the leaderboard for the players with the most playtests for the tabletop game Attack on Scraptown.
            </p>
            <p>
            Points:
            <ul>
                <li>In Person Playtest: 5 points</li>
                <li>Tabletop Simulator Playtest: 3 points</li>
            </ul>
            </p>
            <p>
            Want to get on the board? <a href="https://forms.gle/jDN5Kv2bcAVkU4eQ8">Sign up for playtesting today!</a>
            </p>
        </div>
        </div>
    </section>
    </body>
    </html>"""
  

main()
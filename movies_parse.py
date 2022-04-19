import json
import webbrowser

input_file = open ('movies.json')
movies = json.load(input_file)

'''
for item in json_array:
    print(item['Title'], "\n", 15*"=", "\n")
    print(item["Year"], "\n", 15*"=", "\n")
    print(item["Released"], "\n", 15*"=", "\n")
    print(item["Runtime"], "\n", 15*"=", "\n")
    print(item["Genre"], "\n", 15*"=", "\n")
    print(item["Plot"], "\n", 15*"=", "\n")
    print(item["Language"], "\n", 15*"=", "\n")
    print(item["Poster"], "\n", 15*"=", "\n")
'''

moviesWeb = open('movies.html', 'w', encoding='utf-8')
html_template = '''<html>
<head>
<title>WebMovies</title>
<style>
h1 {
    margin-top: 50px;
    margin-bottom: 50px;
    text-align: center;
}
body {
    width: 60%;
    margin: 0 auto
}
img {
    border-radius: 50px;
}
h2 {
    text-align: center;
    font-size: 32px;
}
</style>
</head>
<body>
<h1>Top 10 movies</h1>
'''
for item in movies:
    Title = item["Title"]
    Year = item["Year"]
    Runtime = item["Runtime"]
    Genre = item["Genre"]
    Plot = item["Plot"]
    Language = item["Language"]
    Poster = item["Poster"]

    html_template += f"<h2>{Title}</h2>"
    html_template += f"<p><b>Genre: </b>{Genre}</p>"
    html_template += f"<p><b>Year of release: </b>{Year}</p>"
    html_template += f"<p><b>Film runtime: </b>{Runtime}</p>"
    html_template += f"<p><b>Plot: </b>{Plot}</p>"
    html_template += f"<p><b>Languages: </b>{Language}</p>"
    html_template += f"<img src='{Poster}'>"
html_template += """
</body>
</html>
"""
moviesWeb.write(html_template)
moviesWeb.close()

webbrowser.open_new_tab('movies.html')
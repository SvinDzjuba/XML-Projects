import json
import webbrowser

input_file = open ('pizza.json')
pizzas = json.load(input_file)

'''
for item in pizzas:
    print(item['name'], "\n", 15*"=", "\n")
    print(item["ingredients"], "\n", 15*"=", "\n")
    print(item["cooking"], "\n", 15*"=", "\n")
    print(item["steps"], "\n", 15*"=", "\n")
'''


pizzaWeb = open('pizza.html', 'w', encoding='utf-8')
html_template = '''<html>
<head>
<title>WebPizza</title>
<style>
h1 {
    text-align: center;
}
</style>
</head>
<body>
<h1>Top 4 pizzas</h1>
'''
for item in pizzas:
    Poster = item["poster"]
    Name = item["name"]
    Ingredients = item["ingredients"]
    Cooking = item["cooking"]
    Steps = item["steps"]

    html_template += f"<h2>{Name}</h2>"
    html_template += f"<img src='{Poster}'>"
    for Ingredient in Ingredients:
        prtIngredient = Ingredient["name"], Ingredient["unit"], Ingredient["count"]
        html_template += f"<p>{prtIngredient.pop(1)}</p>"
    html_template += f"<p>{Cooking}</p>"
    html_template += f"<p>{Steps}</p>"
html_template += """
</body>
</html>
"""
pizzaWeb.write(html_template)
pizzaWeb.close()

webbrowser.open_new_tab('pizza.html')
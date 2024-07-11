from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
@app.route("/",methods=('GET', 'POST'))
def pokedex():
    pokemon = get_pokemon()
    return render_template('pokemon.html', pokemon=pokemon)

@app.route("/",methods=('GET', 'POST'))
def get_pokemon():
    if request.method == "POST":
        pokemon_name = request.form.get("name")
        print(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        return requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()

from flask import Flask, render_template,request
import urllib.request, json

app = Flask(__name__)

@app.route("/")    #rota para a página inicial
def get_list_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)   #pega os dados
    data = response.read()  
    dict = json.loads(data)           #converte os dados para dicionario
    
    return render_template("index.html", characters=dict["results"]) #retorna a página


@app.route("/character_id/<id>")    #rota para um personagem especifico
def get_character_id(id):     #carrega um parametro para a rota
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)   #pega os dados
    data = response.read()  
    dict = json.loads(data)           #converte os dados para dicionario
    
    return render_template("character_id.html", character_id=dict)

@app.route("/list")    #rota para a listagem dos personagens 
def get_list_characters():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)   #pega os dados
    characters = response.read()             
    dict = json.loads(characters)           #converte os dados para dicionario
   
    characters = []   #cria uma lista vazia
    
    for character in dict["results"]:  #percorre a lista de personagens
       
        character = {
            "id": character["id"],
            "name": character["name"],
            "status": character["status"],
            "species": character["species"],
            "gender": character["gender"],
            "origin": character["origin"],
            "location": character["location"],
            
        }
        characters.append(character)

    return render_template("characters.html", characters=characters)                     #retorna a lista de personagens

@app.route("/location_id/<id>")    # rota para um local específico
def get_location_id(id):     # carrega um parâmetro para a rota
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)   # pega os dados
    data = response.read()
    dict = json.loads(data)

    return render_template("location_id.html", location_id=dict)


@app.route("/local")    #rota para a listar as localizacoes
def get_list_local():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)   #pega os dados
    data = response.read()  
    dict = json.loads(data)           #converte os dados para dicionário

    locations = []   #cria uma lista vazia

    for location in dict["results"]:  #percorre a lista de localizações
        location = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
            
        }
        locations.append(location)

    return render_template("locations.html", locations=locations)

    
@app.route("/episode_id/<id>")    #rota para um episodio específico
def get_episode_id(id):     #carrega um parâmetro para a rota
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)   #pega os dados
    data = response.read()  
    dict = json.loads(data)      
    
    #converte os dados para dicionário

    return render_template("episode_id.html", episode_id=dict)

@app.route("/episode")    #rota para a listar os episodios
def get_list_episode():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)   #pega os dados
    data = response.read()  
    dict = json.loads(data)           #converte os dados para dicionário

    episodes = []   #cria uma lista vazia

    for episode in dict["results"]:  #percorre a lista de episodios
        episode = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"]
            
        }
        episodes.append(episode)

    return render_template("episodes.html", episodes=episodes)

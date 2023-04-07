import random
from tkinter import *
from tkinter import ttk

from dados import *
from PIL import Image, ImageTk

# importando pillow


print('oi')
# cores ###
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

# janelas ###
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)


style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


def trocar_pokemon(i):
    global imagem_pokemom, pok_imagem

    # trocando cor do dundo frame
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    # tipo de pokemom
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    imagem_pokemom = pokemon[i]['tipo'][2]

    # imagem do pokemon
    imagem_pokemom = Image.open(imagem_pokemom)
    imagem_pokemom = imagem_pokemom.resize((238, 238))
    imagem_pokemom = ImageTk.PhotoImage(imagem_pokemom)

    pok_imagem = Label(frame_pokemon, image=imagem_pokemom,
                       relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_imagem.place(x=60, y=50)

    pok_tipo.lift()

    # pokemon status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_atk['text'] = pokemon[i]['status'][1]
    pok_def['text'] = pokemon[i]['status'][2]
    pok_vel['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    # pokemon habilidades
    pok_hb1['text'] = pokemon[i]['habilidades'][0]
    pok_hb2['text'] = pokemon[i]['habilidades'][1]


# nome
pok_nome = Label(frame_pokemon, text='', relief='flat',
                 anchor=CENTER, font=('Fixedsys 20'),  fg=co1)
pok_nome.place(x=12, y=15)

# categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat',
                 anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# ID
pok_id = Label(frame_pokemon, text='', relief='flat',
               anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)


# Status
pok_status = Label(janela, text='Status', relief='flat',
                   anchor=CENTER, font=('Veradana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# HP
pok_hp = Label(janela, text='HP: 100', relief='flat',
               anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)


# atk
pok_atk = Label(janela, text='Ataque: 600', relief='flat',
                anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_atk.place(x=15, y=385)

# def
pok_def = Label(janela, text='Defesa: 200', relief='flat',
                anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_def.place(x=15, y=410)

# vel
pok_vel = Label(janela, text='Velocidade: 800', relief='flat',
                anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_vel.place(x=15, y=435)

# total
pok_total = Label(janela, text='Total: 800', relief='flat',
                  anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)


# habilidades
pok_hb = Label(janela, text='Habilidades', relief='flat',
               anchor=CENTER, font=('Veradana 20'), bg=co1, fg=co0)
pok_hb.place(x=180, y=310)

# HP
pok_hb1 = Label(janela, text='choque do trovao', relief='flat',
                anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195, y=360)

# atk
pok_hb2 = Label(janela, text='Soco Trovao', relief='flat',
                anchor=CENTER, font=('Veradana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195, y=385)


# criando botoes de cada pokemom

# imagem do botao 1
imagem_pokemom1 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-pikachu.png')
imagem_pokemom1 = imagem_pokemom1.resize((40, 40))
imagem_pokemom1 = ImageTk.PhotoImage(imagem_pokemom1)

B_pok1 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=imagem_pokemom1, text='Pikachu', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok1.place(x=375, y=10)


# imagem do botao 2
imagem_pokemom2 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-bulbasaur.png')
imagem_pokemom2 = imagem_pokemom2.resize((40, 40))
imagem_pokemom2 = ImageTk.PhotoImage(imagem_pokemom2)

B_pok2 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'),  image=imagem_pokemom2, text='Bulbasaur', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok2.place(x=375, y=65)

# imagem do botao 3
imagem_pokemom3 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-charmander.png')
imagem_pokemom3 = imagem_pokemom3.resize((40, 40))
imagem_pokemom3 = ImageTk.PhotoImage(imagem_pokemom3)

B_pok3 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pokemom3, text='Charmander', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok3.place(x=375, y=120)

# imagem do botao 4
imagem_pokemom4 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-gyarados.png')
imagem_pokemom4 = imagem_pokemom4.resize((40, 40))
imagem_pokemom4 = ImageTk.PhotoImage(imagem_pokemom4)

B_pok4 = Button(janela, command=lambda: trocar_pokemon('Gyarados'), image=imagem_pokemom4, text='Gyarados', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok4.place(x=375, y=175)

# imagem do botao 5
imagem_pokemom5 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-gengar.png')
imagem_pokemom5 = imagem_pokemom5.resize((40, 40))
imagem_pokemom5 = ImageTk.PhotoImage(imagem_pokemom5)

B_pok5 = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=imagem_pokemom5, text='Gengar', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok5.place(x=375, y=230)


# imagem do botao 6
imagem_pokemom6 = Image.open(
    'E:\Bruno\Estudos\Python\pokedex\pokedex-main\src\images\cabeca-dragonite.png')
imagem_pokemom6 = imagem_pokemom6.resize((40, 40))
imagem_pokemom6 = ImageTk.PhotoImage(imagem_pokemom6)

B_pok6 = Button(janela, command=lambda: trocar_pokemon('Dragonite'), image=imagem_pokemom6, text='Dragonite', width=150,
                relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
B_pok6.place(x=375, y=285)


Lista_pokemon = ['Dragonite', 'Gengar', 'Gyarados',
                 'Charmander', 'Bulbasaur', 'Pikachu']

pokemon_escolhido = random.sample(Lista_pokemon, 1)
print(pokemon_escolhido[0])
trocar_pokemon(pokemon_escolhido[0])

janela.mainloop()

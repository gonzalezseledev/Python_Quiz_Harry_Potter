import random
from string import ascii_lowercase

num_questions_per_quiz = 10

questions = {
    "Cómo se llaman los padres de Harry Potter": [
        "Lily y James", "Remus y Nymphadora", "Albus y Gellert"
    ],
    "Cómo se llama la lechuza de Harry Potter": [
        "Hedwing", "Jordan", "Ripper"
    ],
    "Cómo se llama la rata de Ron Weasley": [
        "Scabbers", "Titus", "Francis"
    ],
    "Cómo se llama el gato de Hermione Granger": [
        "Crookshanks", "Finn", "Selma"
    ],
    "Cómo se llama la rana de Neville Longbotton": [
        "Trevor", "Curupira", "Errol"
    ],
    "Qué actor interpreta al personaje de Cedric Digory en la cuarta película de Harry Potter": [
        "Robert Pattinson", "Kit Harrington", "Elijah Wood"
    ],
    "Quién es el padre de Draco Malfoy": [
        "Lucius Malfoy", "Rubeus Hagrid", "Tom Riddle"
    ],
    "Quién es el Príncipe Mestizo": [
        "Severus Snape", "Sirius Black", "El Barón Sanguinario"
    ],
    "Qué actriz interpreta a Bellatrix Lestrange": [
        "Helena Bonham Carter", "Emma Watson", "Emma Thompson"
    ],
    "Qué hechizo usó Harry para matar a Lord Voldemort": [
        "Expelliarmus", "Riddikulus", "Sectumsempra"
    ],
    "Qué nombres recibían los miembros del grupo de James Potter en Hogwarts": [
        "Los Merodeadores",
        "La Órden del Fénix",
        "El ejército de las tinieblas"
    ],
    "Cómo se llama el padre de Luna Lovegood": [
        "Xenophilius Lovegood", "Remus Lupin", "Viktor Krum"
    ],
    "Qué criaturas invisibles tiran de las carrozas en Hogwarts": [
        "Thestrals", "Basiliscos", "Dementores"
    ],
    "Qué personas pueden ver las criaturas Thestrals": [
        "Aquellos que han presenciado la muerte",
        "Aquellos que tienen problemas de salud",
        "Solo los que tiene  esa suerte"
    ],
    "Cómo se llama el conductor del autobus noctámbulo que aparece en la tercera película de Harry Potter": [
        "Ernie", "Bilbo", "Kaladin"
    ],
    "Cuál es el nombre del primer Goblin que recibe a Harry Potter en el banco de Gringotts": [
        "Griphook", "Porlock", "Horklump"
    ],
    "Qué criatura es Aragog en el mundo mágico de Harry Potter": [
        "Acromántula", "Gusarajo", "Quimera"
    ],
    "Cómo se llama el fiel compañero y perro de Hagrid": [
        "Fang", "Viento gris", "Drogon"
    ],
    "El hechizo 'Felifors' convierte a un gato en un qué": [
        "En un caldero", "En un ser humano", "En un perro"
    ],
    "Las lágrimas de qué animal son el único antídoto conocido contra el veneno de basilisco": [
        "Fénix", "Unicornio", "Gato"
    ],
    "Cuál de los siguientes hechiceros NO fue uno de los fundadores de Hogwarts": [
        "Gellert Grindelwald", "Rowena Ravenclaw", "Grodric Gryffindor"
    ],
    "Quién mato al elfo Dobby con un cuchillo en la primera parte de Harry Potter y las relíquias de la muerte": [
        "Bellatrix Lestrange", "La señora Norris", "Ginny Weasley"
    ],
    "En qué posición juega Harry en su equipo de Quidditch": [
        "Buscador", "Guardián", "Golpeador"
    ],
    "Qué requisito puso JK Rowling al equipo de producción de Harry Potter a la hora de escoger el reparto de las películas": [
        "Todos tenían que ser de origen británico",
        "Tener entre 10 y 80 años",
        "Tener experiencia en circo, baile, interpretación o teatro"
     ],
    "Qué hechizo se utiliza para desarmar a otro mago": [
        "Expeliarmus", "Accio", "Engorgio"
    ],
    "De qué está hecha la varita de Harry Potter": [
        "Pluma de Fénix",
        "Pelo de Unicornio",
        "Su madera, núcleo, longitud y flexibilidad son desconocidas"
    ],
    "Qué forma animal tiene el patronous de Luna Lovegood": [
        "Liebre", "Nutria", "Urraca"
    ],
    "Cuándo se publicó el primer libro de Harry Potter": [
        "1997", "1996", "2010"
    ],
    "Cuándo se estrenó la primera película de Harry Potter": [
        "2001", "1977", "2011"
    ],
    "Qué debe decir el usuario del Mapa del Merodeador después de usarlo para restablecerlo": [
        "Travesura realizada",
        "A lo hecho, pecho",
        "Lo que pasó, pasó"
    ],
    "En qué calle de Inglaterra vive la familia de los Dursley": [
        "Número 4 de Privet Drive",
        "221B Baker Street",
        "Whitehaven Mansions Apt 56B"
    ],
    "Qué planta ingiere Harry Potter en el lago negro para poder respirar bajo el agua en el torneo de los tres magos": [
        "Branquialgas", "Asfódelo", "Arce azucarado"
    ],
    "Qué nombre recibe el perro guardián de 3 cabezas": [
        "Fluffy", "Ronald", "Mordisquitos"
    ],
    "Qué instrumento mágico mantiene dormido al perro guardián de 3 cabezas": [
        "Un arpa mágica", "Una ocarina mágica", "Un didgeridoo mágico"
    ],
    "Cuántas escaleras tiene Hogwarts ": [
        "142 escalones", "11.674 escalones", "922 escalones"
    ],
    "Qué se obtiene al ingerir la pócima Felix Felicis": [
        "Suerte", "Inteligencia", "Obsesión, atracción y deseo"
    ],
    "Cuál de los siguientes NO es un Horrocrux de Voldemort": [
        "El espejo de Oesed",
        "La Diadema de Rowena Ravenclaw",
        "El Guardapelo de Salazar Slytherin"
    ],
    "Cómo conseguía Hermione Granger asistir a todas sus clases": [
        "Viajando en el tiempo",
        "Embaucando a sus profesores",
        "Madrugando"
    ],
    "Con qué caza Harry su primera Snitch": [
        "Con la boca", "Con la mano", "Con el trasero"
    ],
    "Cuántas varitas rompió Daniel Radcliffe en el set al usarlas como baquetas de bateria": [
        "80", "50", "20"
    ],
    "El sauce Boxeador fue un regalo de Albus Dumbledore para proteger al colegio. ¿Verdadero o Falso?": [
        "Falso", "Verdadero"
    ],
    "Qué prenda le regalo Harry Potter a Dobby para ser libre": [
        "Un calcetín", "Una bufanda", "Un sombrero"
    ],
    "Qué significan las iniciales R.A.B en el Horrocrux que guarda Albus Dumbledore": [
        "Regulus Arcturus Black",
        "Raisa Adara Broomstix",
        "Romina Alexandra Burkes"
    ],
    "Qué es “El Quisquilloso”": [
        "Un periódico", "Una peluquería mágica", "Una panadería"
    ],
    "Qué nombre recibe la tienda de chucherías cerca de Hogwarts": [
        "Honeydukes", "Sortilegios Weasley", "Flourish & Blotts"
    ],
    "Qué pasa si un muggle encuentra Hogwarts": [
        "Encontrarían un edificio abandonado y en ruinas",
        "Se volatiliza",
        "Les invitan a matricularse"
    ],
    "A qué edad murió Albus Dumbledore": [
        "115", "38", "200"
    ],
    "Un mago que no puede hacer magia se conoce como...":[
        "Squib", "Muggle", "Confundus"
    ],
        "A quién se encuentran Ron, Hermione y Harry en el bosque en 'Las reliquias de la muerte'":[
        "Fenrir Greyback", "Lucius Malfoy", "Voldemort"
    ],
        "Qué hechizo usa Ron para salvar a Hermione del troll en 'Harry Potter y la piedra filosofal'":[
        "Wingardium Leviosa", "Confundus", "Petrificus totalus"
    ],
        "Quién fue con Hermione a la fiesta de Navidad de Slughorn":[
        "Cormac McLaggen", "Ron Weasley", "Neville Longbottom"
    ],
        "Quién fue la primera víctima 'petrificada' del basilisco":[
        "La señora Norris", "Hermione Granger", "Ginny Weasley"
    ],
        "Cuál es el nombre del hijo pequeño de Harry Potter":[
        "Albus", "Sirius", "James"
    ],
        "Quién fue el comentarista de quidditch en los primeros años de Harry Potter":[
        "Lee Jordan", "Angela Johson", "Dean Thomas"
    ],
        "Qué le dejó Dumbledore a Hermione en su testamento":[
        "Un libro", "Un medallón", "Un bolso encantado"
    ],
        "Qué organización fundó Hermione en su cuarto año en Hogwarts":[
        "La Plataforma Élfica de Defensa de los Derechos Obreros", 
        "Fuerzas especiales del estatuto secreto", 
        "Asamblea medieval de magos de europa"
    ],
        "Cuántas editoriales rechazaron el manuscrito de 'La piedra filosofal'":[
        "12", "11", "15"
    ],
        "Cuántos libros se habían vendido de la saga a fecha de 2015 y a cuántos idiomas se ha traducido":[
        "450 millones de copias en 67 idiomas", 
        "325 millones de copias en 165 idiomas", 
        "765 millones de copias en 50 idiomas"
    ],
        "Cómo se llamaba la niña que alentó la publicación del primer libro de Harry Potter":[
        "Alice Newton, la hija del propietario de la editorial Bloomsbury", 
        "Mary James, la sobrina del portero de la editorial Bloomsbury", 
        "Elisabeth Perkins, la ahijada del presidente de la BBC"
    ],
        "Cuál es el libro favorito de la saga del dueño de Bloomsbury":[
        "El prisionero de Azkaban", 
        "Las reliquias de la muerte", 
        "El cáliz de fuego"
    ],
        "Cuál de los volúmenes es el libro más rápidamente vendido de la historia":[
        "Harry Potter y las reliquias de la muerte", 
        "Harry Potter y el cáliz de fuego", 
        "Harry Potter y el misterio del príncipe"
    ],
        "Quién le entrega la capa de invisibilidad a Harry Potter":[
        "Albus Dumbledore", "Sirius Black", "Minerva McGonagall"
    ],
        "En qué trabaja Charlie Weasley":[
        "Entrena dragones en Rumanía", 
        "Con los Gringotts en Egipto", 
        "Prepara elfos en Islandia"
    ],
        "En cuanto está valorada la marca Harry Potter":[
        "15.000 millones de dólares", 
        "25.000 millones de dólares", 
        "12.000 millones de dólares"
    ],
        "Qué forma tienen los pendientes que lleva Luna cuando habla por primera vez con Harry":[
        "Rábanos", "Corchos de cerveza de mantequilla", "Torre Eiffel"
    ],
        "Cuál es la fecha de cumpleaños de Harry Potter":[
        "31 de julio", "21 de junio", "30 de abril"
    ],
        "De que músico es tan fan J.K. Rowling que le permite comprender el enganche que muchos tienen con Harry Potter":[
        "Morrisey", "Bono", "Sting"
    ],
        "Qué objeto usaron como traslador en el Mundial de Quidditch":[
        "Una bota", "Un cubo sucia", "La copa de los tres magos"
    ],
        "Quién fue director de Hogwarts antes de Dumbledore":[
        "Phineas Nigellus Black", "Dilys Derwent", "Vindictus Viridian XVIII"
    ],
        "Quién es Peeves":[
        "Un poltergeist", "Un ghoul", "Un fantasma"
    ]

    # 70 preguntas
}

num_questions = min(num_questions_per_quiz, len(questions))
questions = random.sample(list(questions.items()), k=num_questions)

num_correct = 0
print('🧙‍♂️ ¿LISTOS PARA PONER A PRUEBA VUESTROS CONOCIMIENTOS SOBRE MAGIA Y HECHICERÍA? 🧙‍♂️')
print('Este quiz de Harry Potter definirá de una vez por todas si tenéis alma de mago o de muggle. ¿Preparades?')
for num, (question, alternatives) in enumerate(questions, start=1):
  print(f'\n◽ Pregunta {num}:')
  print(f'\n¿{question}?\n')
  correct_answer = alternatives[0]
  labeled_alternatives = dict(
      zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
      )

  for label, alternative in labeled_alternatives.items():
    print(f' {label}) {alternative}')

  while (answer_label := input('\nRespuesta: ')) not in labeled_alternatives:
    print(f'🙄 Alma de cántaro, haz el favor de introducir una de las siguientes opciones 👉 {", ".join(labeled_alternatives)}')

  answer = labeled_alternatives[answer_label]
  if answer == correct_answer:
    num_correct += 1
    print('\n⭐ ¡Has acertado! ⭐')
  else:
    print(f'\n😞 La respuesta correcta es {correct_answer!r}, no {answer!r}')

print(f'\n🏆 ¡Enhorabuena! Has acertado {num_correct} de {num} preguntas 🏆')
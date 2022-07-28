print("HISTOIRIAS LOCAS")

nombre = input("Hola bienvenido a Hisotrias Locas, cual es tu nombre ? \n")
print(f"Hola, {nombre}, espero que estes bien, vamos a jugar un juego, "
          f"en el cual contruiremos una historia con tus palabras .\n Empezamos ...")


dia = input("Que dia es hoy?\n")
comida = input("Ques es lo que mas te gusta? Desayunar, almorzar o cenar?\n")
nivel = input("poco o mucho? \n")
divertir = input("Donde te gusta diviertirte? \n ")
hacer = input("Que te gusta hacer donde te diviertes? \n")




historia_loca = (f"Hoy es {dia}, como cualquier dia, nos disponemos a {comida}, cuando"
                 f" de pronto, una alarma suena en la cocina, habia {nivel} humo, "
                 f"llamamos a los bomberos, y me percate que habia una fuga de gas en"
                 f" una tuberia, Una vez apagado el fuego, nos fuimos a divertir a {divertir}" 
                 f" para {hacer}, y  asi olvidar  el mal rato... FIN DE LA HISTORIA")


print(historia_loca)
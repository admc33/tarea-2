print("¡Bienvenido a la aventura mágica!")
print("Te encuentras en un bosque encantado. Tienes dos caminos frente a ti.")
print("1. Tomar el camino de la izquierda.")
print("2. Tomar el camino de la derecha.")
    
camino = input("¿Cuál camino eliges? (1 o 2): ")

if camino == "1":
    print("Has tomado el camino de la izquierda y te encuentras con un río.")
    print("Puedes:")
    print("1. Tratar de cruzar el río.")
    print("2. Buscar un puente.")
        
    decision = input("¿Qué decides hacer? (1 o 2): ")

    if decision == "1":
        print("Intentas cruzar el río, pero la corriente es muy fuerte y caes al agua.")
        print("¡Has sido arrastrado y te encuentras en una isla mágica!")
        print("Un hada te ofrece tres deseos.")
        deseos = input("¿Qué deseas? (1. Riqueza, 2. Poder, 3. Sabiduría): ")
            
        if deseos == "1":
            print("¡Has deseado riquezas! Eres ahora el más rico del reino.")
        elif deseos == "2":
            print("¡Has deseado poder! Eres ahora un poderoso mago.")
        elif deseos == "3":
            print("¡Has deseado sabiduría! Ahora conoces todos los secretos del universo.")
        else:
            print("Esa no es una opción válida. Te quedas en la isla para siempre.")
        
    elif decision == "2":
        print("Buscas un puente y lo encuentras. Cruzas el río con éxito.")
        print("Al otro lado, descubres un castillo abandonado.")
        print("Puedes:")
        print("1. Entrar al castillo.")
        print("2. Seguir explorando el bosque.")
            
        entrada = input("¿Qué decides hacer? (1 o 2): ")
            
        if entrada == "1":
            print("Entro al castillo y descubres un tesoro escondido. ¡Eres rico!")
        elif entrada == "2":
            print("Sigues explorando el bosque y encuentras criaturas mágicas que se convierten en tus amigos.")
        else:
            print("Esa no es una opción válida. Te quedas en el bosque para siempre.")

elif camino == "2":
    print("Has tomado el camino de la derecha y llegas a una cueva oscura.")
    print("Puedes:")
    print("1. Entrar a la cueva.")
    print("2. Volver atrás.")
        
    cueva = input("¿Qué decides hacer? (1 o 2): ")

    if cueva == "1":
        print("Entras a la cueva y descubres un dragón dormido.")
        print("Puedes:")
        print("1. Intentar robarle un tesoro.")
        print("2. Salir sigilosamente.")
            
        robo = input("¿Qué decides hacer? (1 o 2): ")
            
        if robo == "1":
            print("Intentas robarle el tesoro, pero el dragón se despierta y te ahuyenta.")
        elif robo == "2":
            print("Sales sigilosamente y logras escapar sin ser visto. ¡Eres un maestro del sigilo!")
        else:
            print("Esa no es una opción válida. Te quedas atrapado en la cueva para siempre.")
        
    elif cueva == "2":
        print("Decides volver atrás y tomas el camino de la izquierda donde comenzaste.")
    else:
        print("Esa no es una opción válida. Te quedas en la cueva para siempre.")

else:
    print("Esa no es una opción válida. Te pierdes en el bosque.")
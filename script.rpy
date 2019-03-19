define MC = Character("[MCname]")
define Genre = "NA"

label initialize:
    $gn = True
    while gn != False:
        $MCgenre = renpy.input("Entrez votre genre: M/F").strip()
        if MCgenre == 'M':
            $genre = "Male"
            $gn = False
        elif MCgenre == 'F':
            $genre = "Female"
            $gn = False

    $Genre = genre
    $MCname = renpy.input("Entrez votre nom:").strip()

    if not MCname:
        $MCname = "Jassy"
    jump begin

image splash = "splashscreen.png"

label splashscreen:
    scene black
    with Pause(1)

    show text "Cancercorp vous présente..." with dissolve
    with Pause(1)
    show splash with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    scene black with dissolve
    with Pause(1)

    return

label start:
    #call to initialize the MC parameters
    jump initialize

label begin:
    scene bg room

    "*Dring Dring* ... *Dring Dring* *Clac*"
    "..."
    "Premier jour de lycée, et je me lève déjà en retard."
    "Je me prépare rapidement, enfila mes chaussures, puis me mit à courir en direction du lycée."
    "Sur le chemin, je croise un groupe de jeunes lycéennes, semblant avoir mon âge."
    "L'une d'elles en particulier, retient mon attention."
    "Tiens ? Sa tête me dit quelque chose... ça ne serai pas marie ? On habitait a côté quand on était petites je crois."
    "Quand aux autres filles, je ne les reconnaissaient pas. Elles ont l'air agitées, je me demande ce qu'elles lui veulent... "
    menu:
        "S'approcher":
            jump Marie_path
        "Continuer son chemin":
            jump keep_walking

label Marie_path:
    "test1"
    return

label keep_walking:
    "test2"
    return

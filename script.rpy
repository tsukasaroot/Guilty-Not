define MC = Character("[MCname]")
define Girl1 = Character("Fille 1")
define Girl2 = Character("Fille 2")

label initialize:
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
    stop music
    $renpy.music.set_volume(0.2, channel='music')
    $renpy.sound.set_volume(0.3, channel='sound')
    #call to initialize the MC parameters
    jump initialize

label begin:
    play music [ "<loop 1>" "songs/everydaylife.mp3" ] fadein 1.0
    scene bg bedroom
    with dissolve

    play sound "songs/homering.wav"
    "*Dring Dring* ... *Dring Dring*"
    stop sound fadeout 1.0

    "..."
    "Premier jour de lycée, et je me lève déjà en retard."
    "Je me prépare rapidement, enfila mes chaussures, puis me mit à courir en direction du lycée."
    scene black
    with dissolve
    scene bg street
    "Pas loin du portail de l'école, je croise un groupe de jeunes lycéennes, semblant avoir mon âge."
    "L'une d'elles en particulier, retient mon attention."
    "Tiens ? Sa tête me dit quelque chose... ça ne serai pas marie ? On habitait a côté quand on était petites je crois."
    "Quand aux autres filles, je ne les reconnaissaient pas. Elles ont l'air agitées, je me demande ce qu'elles lui veulent... "
    # marie path amène sur la route de marie
    menu:
        "S'approcher":
            jump Marie_path
        "Continuer son chemin":
            $inactive=1
    "Bah, après tout je suis déjà juste au niveau temps, je n'ai pas de temps à perdre."
    return

label Marie_path:
    Girl1 "Alors ? Tu me donnes ces 20 euros ou tu comptes t'empiffrer ce midi ?"
    Girl2 "Ouais ouais, on en a besoin nous, comment on va sortir ce soir sans cet argent ?"
    "Peut être que je devrai calmer un peu la situation... ?"
    menu:
        # marie path amène sur la route de marie
        "Tenter de s'interposer":
            jump Marie_path2
        "Continuer à observer":
            $inactive=1
    return

label Marie_path2:
    MC "Excusez-moi..."
    Girl1 "Oui ? On est en pleine discussion avec notre amie. Tu peux nous laisser ?"
    MC "Je n'ai pas l'impression qu'elle apprécie cette conversation... Ni qu'elle souhaite vous prêter ces 20 euros."
    Girl1 "Et ? C'est pas tes affaires, à moins que tu ne veuilles partager l'addition avec cette truie ?"
    "Elle s'approche de moi, menaçante."
    MC "Je ne voulais pas déranger, haha..."
    play sound [ "<loop 0>" "songs/schoolring.mp3" ]
    MC "Ah, c'est l'heure, on ferait mieux de pas être en retard pas vrai ?"
    Girl2 "Partons, on s'en occupera plus tard."
    "Tandis que le groupe de fille se rend dans l'enceinte du lycée, Marie les suit de loin, trainant des pieds et regardant le sol."
    "J'ai tenté de m'approcher d'elle, mais elle a subitement accéléré le rythme."
    "Ce début d'année commence bien..."
    scene black
    with dissolve
    scene bg classroom
    "Après une dizaines de minutes, je suis enfin arrivée dans la salle de classe."
    return

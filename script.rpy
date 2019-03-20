define MC = Character("[MCname]")
define Marie = Character("Marie")
define Girl1 = Character("Fille 1")
define Girl2 = Character("Fille 2")
define Girl3 = Character("Fille 3")
define Groupe = Character("Groupe")

label initialize:
    $MCname = renpy.input("Entrez votre nom:").strip()

    if not MCname:
        $MCname = "Jassy"
    $friend = 0
    $inactive = 0
    jump begin

image splash:
    "splashscreen.png"
    yalign 0.5
    xalign 0.8

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
    "Je me prépare rapidement, enfila mes chaussures, puis me mis à courir en direction du lycée."
    scene black
    with dissolve
    scene bg street
    "Pas loin du portail de l'école, je croise un groupe de jeunes lycéennes, semblant avoir mon âge."
    "L'une d'elles en particulier, retient mon attention."
    "Tiens ? Sa tête me dit quelque chose... ça ne serai pas Marie ? On habitait a côté quand on était petites je crois."
    "Quand aux autres filles, je ne les reconnaissaient pas. Elles ont l'air agitées, je me demande ce qu'elles lui veulent... "
    "J'ai donc décidée de m'approcher."
    scene black
    with dissolve
    scene bg lycee
    Girl1 "Alors ? Tu me les donnes ces 20 euros ? Ou tu comptes tout dépenser ce midi pour t'empiffrer ?"
    Girl2 "Ouais ouais, on en a besoin nous, comment on va sortir ce soir sans cet argent ?"
    Girl3 "J'avoue, et puis t'as pas vraiment besoin de manger hein, hahaha."
    "Le groupe de fille se mit à rire en choeur."
    "Peut être que je devrai calmer un peu la situation... ?"
    menu:
        # marie path amène sur la route de marie
        "Tenter de s'interposer":
            jump Marie_path
        "Continuer à observer":
            $inactive=1
    return

label Marie_path:
    MC "Excusez-moi..."
    Girl1 "Oui ? On est en pleine discussion avec notre amie. Tu peux nous laisser ?"
    MC "Je n'ai pas l'impression qu'elle apprécie cette conversation... Ni qu'elle souhaite vous prêter ces 20 euros."
    Girl1 "Et ? C'est pas tes affaires, à moins que tu ne veuilles partager l'addition avec cette truie ?"
    "Elle s'approche de moi, menaçante."
    MC "Je ne voulais pas déranger, haha..."
    play sound [ "<loop 0>" "songs/schoolring.mp3" ]
    pause(1)
    MC "Ah, c'est l'heure, on ferait mieux de pas être en retard pas vrai ?"
    Girl2 "Partons, on s'en occupera plus tard."
    "Tandis que le groupe de fille se rend dans l'enceinte du lycée, Marie les suit de loin, trainant des pieds et regardant le sol."
    "J'ai tenté de m'approcher d'elle, mais elle a subitement accéléré le rythme."
    "Ce début d'année commence bien..."
    stop music fadeout 1.0
    scene black
    with dissolve
    scene bg classroom
    $renpy.music.set_volume(0.4, channel='music')
    play music [ "<loop 1>" "songs/lyceetheme.mp3" ] fadein 1.0
    "Après une dizaines de minutes, je suis enfin arrivée dans la salle de classe."
    "Tiens, il n'y a pas beaucoup de filles. J'aurai peut-être l'occasion de me trouver un petit copain dès le début de l'année !"
    "En entrant dans la salle de classe, j'ai remarqué Marie toute seule au fond."
    "Je me suis donc assise à la place d'à côté."
    MC "Salut !"
    Marie "..."
    "Ahah, totalement ignorée..."
    scene black
    with dissolve
    scene bg lycee
    play sound [ "<loop 0>" "songs/schoolring.mp3" ]
    pause(1)
    "L'heure de pause."
    MC "Ah Marie, attends."
    Marie "Elle s'arrêta un instant, puis continua son chemin."
    menu:
        "La suivre":
            $friend-=1
            jump follow_her
        "Manger dans la salle":
            $friend+=1
            "Il fait beaucoup trop chaud pour manger dehors, je décide donc de retourner dans la salle de classe."
    jump back_class

label follow_her:
    "En arrivant dans l'arrière cours, Marie se retourna. l'air effayée."
    Marie "Ex-excuse moi, tu peux me laisser ? Je préfère rester seule."
    MC "Je voulais juste qu'on discute un peu, après ce qu'il s'est passé ce matin..."
    Marie "..."
    "Elle semble se renfermer encore plus sur elle-même."
    MC "Du coup, tu veux pas en parler ?"
    Marie "..."
    "Hum, j'ai l'impression que je m'y suis mal prise. Je ferai mieux de la laisser et d'aller manger."
    MC "On se revoit en classe, à toute."
    jump back_class

label back_class:
    scene black
    with dissolve
    scene bg classroom
    "Au final, j'ai mangé avec un groupe composé de garçons et de filles."
    MC "Ouf, j'ai trop mangé. Je vais marcher un peu pour digérer. A plus tard !"
    Groupe "A toute !"

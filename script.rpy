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
    $renpy.music.set_volume(1, channel='voice')
    $renpy.music.set_volume(0.1, channel='music')
    $renpy.sound.set_volume(0.2, channel='sound')
    #call to initialize the MC parameters
    jump initialize

label begin:
    play music [ "<loop 1>" "songs/everydaylife.mp3" ] fadein 1.0
    scene bg bedroom with dissolve

    play sound "songs/homering.wav"
    "*Dring Dring* ... *Dring Dring*"
    stop sound fadeout 1.0

    "..."
    #voice "p1"
    "Premier jour de lycée, et je me lève déjà en retard."
    #voice "p2"
    "Je me prépare rapidement, enfile mes chaussures, puis me mets à courir en direction du lycée."
    scene black with dissolve
    scene bg street
    #voice "p3"
    "Pas loin du portail de l'école, je croise un groupe de jeunes lycéennes, semblant avoir mon âge."
    #voice "p4"
    "L'une d'elles en particulier, retient mon attention."
    #voice "p5"
    "Tiens ? Sa tête me dit quelque chose... ça ne serai pas Marie ? On habitait a côté quand on était petites je crois."
    #voice "p6"
    "Quand aux autres filles, je ne les reconnaissaient pas. Elles ont l'air agitées, je me demande ce qu'elles lui veulent... "
    #voice "p7"
    "J'ai donc décidée de m'approcher."
    scene black with dissolve
    scene bg lycee
    #voice "p8"
    Girl1 "Alors ? Tu me les donnes ces 20 euros ? Ou tu comptes tout dépenser ce midi pour t'empiffrer ?"
    #voice "p9"
    Girl2 "Ouais ouais, on en a besoin nous, comment on va sortir ce soir sans cet argent ?"
    #voice "p10"
    Girl3 "J'avoue, et puis t'as pas vraiment besoin de manger hein, hahaha."
    #voice "p11"
    "Le groupe de fille se mit à rire en choeur."
    #voice "p12"
    "Peut être que je devrais calmer un peu la situation... ?"
    menu:
        #voice "c1"
        #voice "c2"
        # marie path amène sur la route de marie
        "Tenter de s'interposer":
            jump Marie_path
        "Continuer à observer":
            $inactive=1
    ""
    return

label Marie_path:
    #voice "p13"
    MC "Excusez-moi..."
    #voice "p14"
    Girl1 "Oui ? On est en pleine discussion avec notre amie. Tu peux nous laisser ?"
    #voice "p15"
    MC "Je n'ai pas l'impression qu'elle apprécie cette conversation... Ni qu'elle souhaite vous prêter ces 20 euros."
    #voice "p16"
    Girl1 "Et ? C'est pas tes affaires, à moins que tu ne veuilles partager l'addition avec cette truie ?"
    #voice "p17"
    "Elle s'approche de moi, menaçante."
    #voice "p18"
    MC "Je ne voulais pas déranger, haha..."
    play sound [ "<loop 0>" "songs/schoolring.mp3" ]
    pause(1)
    #voice "p19"
    MC "Ah, c'est l'heure, on ferait mieux de pas être en retard pas vrai ?"
    #voice "p20"
    Girl2 "Partons, on s'en occupera plus tard."
    #voice "p21"
    "Tandis que le groupe de fille se rend dans l'enceinte du lycée, Marie les suit de loin, trainant des pieds et regardant le sol."
    #voice "p22"
    "J'ai tenté de m'approcher d'elle, mais elle a subitement accéléré le rythme."
    #voice "p23"
    "Ce début d'année commence bien..."
    stop music fadeout 1.0
    scene black with dissolve
    scene bg classroom
    $renpy.music.set_volume(0.2, channel='music')
    play music [ "<loop 1>" "songs/lyceetheme.mp3" ] fadein 1.0
    "Après une dizaines de minutes, je suis enfin arrivée dans la salle de classe."
    "Tiens, il n'y a pas beaucoup de filles. J'aurai peut-être l'occasion de me trouver un petit copain dès le début de l'année !"
    "En entrant dans la salle de classe, j'ai remarqué Marie toute seule au fond."
    "Je me suis donc assise à la place d'à côté."
    MC "Salut !"
    Marie "..."
    "Ahah, totalement ignorée..."
    scene black with dissolve
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
    scene black with dissolve
    scene bg classroom
    "Au final, j'ai mangé avec un groupe composé de garçons et de filles."
    MC "Ouf, j'ai trop mangé. Je vais marcher un peu pour digérer. A plus tard !"
    Groupe "A toute !"
    scene black with dissolve
    scene bg lycee
    "Pendant ma balade digestive dans l'enceinte du lycée, j'entends des voix provenant de derrière un pilier."
    "Je prends le risque de m'approcher..."
    "... Comme je pensais, cette voix me disait quelque chose. C'est Marie, entourée par les filles de ce matin."
    "L'une d'elle remarque ma présence."
    Girl3 "Encore toi ? Qu'est-ce que tu nous veux ?"
    Girl2 "Ah je sais ! Tu vas payer à sa place !"
    Girl1 "Allez raboule l'argent."
    MC "Arrêtez ça ! Sinon je vais devoir en parler à un professeur."
    Girl1 "Haha, c'est quoi cette chouineuse ?"
    "Je prends Marie par la main, puis la tire en direction de notre classe."
    Girl2 "C'est ça, enfuis-toi ! On se chargera de toi en même temps que ta grosse pote."
    Girl3 "On verra si tu protègeras cette baleine pour longtemps."
    "En arrivant devant la salle de classe, Marie retira brusqement sa main."
    "Elle rentre dans la salle sans se retourner, j'ai cependant cru entendre un léger murmure..."
    Marie "... Merci."
    menu:
        "Je suis là si tu veux en parler":
            MC "pas forcément maintenant, mais plus tard, dans un cion tranquille, ça t'irait ?"
            Marie "Oh j'ai l'habitude de tout ça."
            MC "Dis pas ça ! Tu mérites d'être respecté !"
            Marie "On n'est pas obligé..."
            MC "Déjà on devrait aller voir un professeur ! Il pourra sûrement faire quelque chose."
            Marie "Je suis pas sûre..."
            MC "T'en fais pas, on y va ?"
            "Elle semblait hésitante, mais a finit par accepter"
            $friend+=1
        "Ne les laisses pas faire ce qu'elles veulent !":
            MC "C'est exactement pour ça qu'elles continuent, car tu leur donne ce qu'elles souhaite !"
            MC "Allons en parler à un professeur."
            Marie "... Je suis pas sûre que ça changera grand chose..."
            Marie "Et pourquoi tu t'en mêles ?"
            "Je lui réponds en ignorant sa question."
            MC "Essayons quand même."
            $friend-=1
    return

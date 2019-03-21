label day2:
    $renpy.music.set_volume(0.1, channel='music')
    play music everydaylife fadein 1.0
    play sound homering
    show text "Jour 2" with dissolve
    pause(1)
    scene bg bedroom
    "Mmmh..."
    stop sound fadeout 1.0
    "*clic*"
    "Ahhh... déjà."
    "Bon, j'ai hâte de voir Marie."
    "Ca fait cinq ans qu'elle avait déménagée avec ses parents. Je me demande pourquoi elle est revenue ?"
    "Oh non ! Je vais être en retard !"
    stop music fadeout 1.0
    $renpy.music.set_volume(0.3, channel='music')
    play music lycee fadein 1.0
    scene black with dissolve
    scene bg classroom
    "La mâtinée passe rapidement."
    play sound schoolring
    MC "[Marie] attends ! Ca te dérange si on mange toutes les deux dans la classe ? Tout le monde est sorti, on sera pas dérangé."
    Marie "... Si tu veux."
    "Youpi ! Je prends ça comme une petite victoire."
    "Après le repas, Marie se lève brusquement."
    Marie "Je vais marcher un peu."
    MC "On y va ensemble ?"
    Marie "Je préfère être seule..."
    MC "Ah...d'accord, je t'attends."
    scene black with dissolve
    scene bg classroom with dissolve
    "..."
    scene black with dissolve
    scene bg classroom with dissolve
    "Ca fait déjà vingt minutes..."
    "Je vais aller voir dans l'arrière cour. J'ai le sentiment qu'elle y est retournée."
    scene black with dissolve
    scene bg lycee
    stop music fadeout 1.0
    play music hero fadein 1.0
    "En arrivant presque à l'arrière cour, j'entends des bruits."
    "*paf*"
    "..."
    MC "Qu'est-ce que..."
    "Je me précipite vers la provenance de ses sons."
    "Le groupe de fille habituel était en cercle. Marie au milieu, allongée sur le dos, protégeant sa tête avec ses bras."
    "Aïe !"
    Girl1 "Alors ! On fait moins sa maligne maintenant ?"
    Girl2 "Ouais, [MC] est pas toujours là pour te sauver."
    MC "Arrêtez ça !!!"
    Girl3 "Rhaa sérieux ? Casse-toi, on règle nos problèmes, c'est tout."
    MC "Quels problèmes, hein ??"
    "Je me place juste au dessus de Marie, dans l'espoir qu'elles s'arrêtent."
    Girl1 "Tu ferais mieux de te mêler de tes affaires !"
    scene bg lycee with hpunch
    "L'une d'elle me gifle."
    "Je la foudroie du regard."
    Girl1 "... Ca vous apprendra à toutes les deux."
    "Je me suis agenouillée à côté de Marie, elle a le visage en sang."
    MC "Viens on va à l'infirmerie..."
    Marie "Snif... J'en ai marre... et ça sera comme ça toute l'année encore une fois..."
    MC "T'en fais pas, on trouvera une solution..."
    stop music fadeout 2.0
    scene black with dissolve
    pause(1)
    play music lycee fadein 1.0
    "Je l'ai accompagnée à l'infirmerie, puis suis retournée en classe."
    scene bg classroom with dissolve
    "Une heure plus tard, Marie est entrée dans la salle de classe et s'est assise sur sa chaise sans même me regarder."
    "Les cours se passent, le soleil tourne lentement, et la fin des cours approche."
    scene black with dissolve
    play sound schoolring
    scene bg lycee with dissolve
    "Je vais tenter de rentrer avec Marie aujourd'hui."
    "Je me suis donc tournée à ma droite afin de lui demander si ça la dérangeait."
    "... !!"
    "Le bureau est vide. Je me demande à quel moment elle est partie."
    "Bah, la prochaine fois."
    "En posant mon sac sur le bureau, une feuille blanche tombe."
    "Je la déplie, puis la lis..."
    scene black with dissolve
    stop music fadeout 1.0
    play music suicidal fadein 1.0
    scene bg classroom
    "..."
    "Ca m'a l'air sérieux là !!"
    "Cette feuille, Marie avait écrit dedans, un peu comme une lettre d'adieu..."
    "Elle doit encore être dans l'école."
    "Il faut que je la retrouve."
    menu:
        "Aller sur le toit":
            jump save_her
        "Aller dans l'arrière cour":
            jump bad_end1

label save_her:
    scene black with dissolve
    scene bg roof
    ""
    return

label bad_end1:
    scene black with dissolve
    scene bg lycee
    "Je me suis donc rendu à l'arrière cours."
    "..."
    "Personne !"
    "Je n'ai aucune idée d'où elle pourrait être... de plus je n'ai pas son numéro de téléphone..."
    "Je me dirige donc vers la sortie."
    "*Pouf*"
    "un bruit sourd provenant de derrière se fait entendre."
    "Je me retourne lentement..."
    "Puis, je vois au sol une masse de forme humaine."
    scene bg lycee with vpunch
    scene bg lycee with hpunch
    #process de l'image pour la brouiller, à afficher avec un dissolve
    MC "Hein.. !?"
    MC "Hah... non... quoi... ?"
    MC "... Marie... ?"
    scene bg lycee with vpunch
    scene bg lycee with hpunch
    "Effrayée, je m'enfuie."
    "Je cours en direction de ma maison."
    "Puis je m'enferme dans ma chambre..."
    scene black with dissolve
    "J'ai foirée quelque part..."
    "Je l'ai pas assez aidée..."
    "J'aurai dû faire plus attention..."
    "Je mérite pas de vivre non plus..."
    stop music fadeout 2.0
    show text "{color=#f00}Bad end..." with dissolve
    pause(2)
    hide text with dissolve
    return

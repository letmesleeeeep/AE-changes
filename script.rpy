define s = Character('Es', color="#FFFFFF")

define m = Character('Me', color="#FFFFFF")



image es angry = "es angry.png"

image es neutral = "es neutral.png"

image es dom = "es dom.png"

image es happy = "es happy.png"

image es left = "es left.png"

image es right = "es right.png"

image es sad = "es sad.png"

image es very happy close = "es very happy close.png"

image es very happy open = "es very happy open.png"



label start:

    $ quick_menu = False

    scene bg library
    with fade

    pause 2
    $ quick_menu = True

    play music "audio/Silence.wav"



s "This is a demonstration of a menu. A very long sentence to see if the current textbox is able to handle it. Blah blah blah blah blah blah blah blah."



"Sprite test"



show es neutral

with dissolve



s "I can only despair."



show es happy

with dissolve



s "I am so happy to see you."



show es angry

with dissolve



s "Stay the fuck back or I will kill you goddamn it!"



show es very happy open

with dissolve



s "C-can you show me your hand. Please..."



show es very happy close

with dissolve



s "Eheheh~"



show es left

with dissolve



s "hmm..."



show es right

with dissolve



s "say..."



show es dom

with dissolve



s "It's time for your pegging session. Bend over."



menu:

    "Yes.":

        jump dommed

    "No.":

        jump undommed



label dommed:

    s "You would be a cripple when I am done with you."

    jump nextlabel



label undommed:

    s "Did I stutter?"



label nextlabel:

    s "there is no use in running."



## Implement an actual menu. Refer to Monika After Story for suggested implementation.

scene black

with dissolve



"THE END OF ALPHA"



return

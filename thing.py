import re;jefioqwjfioqwejfoqe = ""
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
    jefioqwjfioqwejfoqe += "1"
fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo=2;jfiewqojfqiewofeqwfewq = r"11";jifowqjfiqe = re.sub(jfiewqojfqiewofeqwfewq, "10", jefioqwjfioqwejfoqe, 0);print(jifowqjfiqe);jfqweifjeiwqofjweiqojfeiwqojfewqio=1;fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo+=1;fjeqwoifjiqowejfqwejfoewqjfiqowe = jifowqjfiqe;jfiweoqfjieoqwjfiqowejfiowqe = ""
while fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo <= 99:
    for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
        if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == 0 or fewqfqewfjqewifjqweofweqiofjiqowefjoippp%fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo==0:
            jfioewjfioqwejioweqjfioqwefewqfioqew = (fjeqwoifjiqowejfqwejfoewqjfiqowe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp]);
            if jfioewjfioqwejioweqjfioqwefewqfioqew == "1":
                jfiweoqfjieoqwjfiqowejfiowqe+="0";
            else:
                jfiweoqfjieoqwjfiqowejfiowqe+="1";
        else:
            jfiweoqfjieoqwjfiqowejfiowqe+= (fjeqwoifjiqowejfqwejfoewqjfiqowe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp]);
    print(f"{jfiweoqfjieoqwjfiqowejfiowqe}, {fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo}");fjeqwoifjiqowejfqwejfoewqjfiqowe=jfiweoqfjieoqwjfiqowejfiowqe;fdjfiowqejojfwqifjeioqwjfoiqweiofiewqjfiwoqejfioewqjfqweo+=1 ;jfiweoqfjieoqwjfiqowejfiowqe="";
jifowqjfiqe = fjeqwoifjiqowejfqwejfoewqjfiqowe;fjeqwiofqweji=0;fjeqwoifjiqowejfqwejfoewqjfiqowe="";
i=0
fjewqifjiewojfiqowe={}
def jifjeiwoqfjioe(fjewqfeiqwjfiewq):
    if fjewqfeiqwjfiewq % 2 == 0:
        fjewqfeiqwjfiewq = fjewqfeiqwjfiewq/2
    else:
        fjewqfeiqwjfiewq = (fjewqfeiqwjfiewq*3)+1
    return(fjewqfeiqwjfiewq)
x=1
try:
    class jfijweqiofjewi:
        fjeiwoqfjeqwifiowq = SpriteKind.create();fejiwfjqefjqewiof = SpriteKind.create();fjewqiofjwqefjiewqo = SpriteKind.create();jfiqwjfioqwejfoq = SpriteKind.create();jfeiwqojfiewqjif = SpriteKind.create();fjiwqefjiwqefjiwoe = SpriteKind.create()
    """

    Todo: Make health pickups

    """

    def fjeiwoqfqjfiewof(jfiweojfeiowq, fjeiwqofjweqfjioqw):
        info.player2.change_life_by(-1);sprites.destroy(ijfewojfiqewiof);sprites.destroy(sword2)
    sprites.on_overlap(jfijweqiofjewi.fjeiwoqfjeqwifiowq, jfijweqiofjewi.projectile, fjeiwoqfqjfiewof)

    def jiofjiewqjfioewqfqwe():
        global ijfewojfiqewiof
        ijfewojfiqewiof = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                        . . . . . . . . 
                        . c c b b b b . 
                        f 3 d d 5 1 5 b 
                        f 3 d d 5 1 5 b 
                        . c c b b b b .                     . . . . . . . . 
 . . . . . . . .
            """),
            jfioewqjfioweqijfiqwo,
            p2_a,
            0)
        ijfewojfiqewiof.x += p2_b
    controller.player2.on_button_event(ControllerButton.A,
        ControllerButtonEvent.PRESSED,
        jiofjiewqjfioewqfqwe)

    def jfioweqjfewfjeiqwjfioqwejfieqwjfioeqwjioefqwjifweqjfeiowq():
        for index in range(15):
            jfioewqjfioweqijfiqwo.x += 1e+21
    def jfiqoewjfiewjfieqwoi():
        for index2 in range(15):
            jfeiwqjfioqwejfeiowq.x += 1e+21

    def jfqeiwofjiqweofejwiqop(sprite2, otherSprite2):
        info.player1.change_life_by(-1)
        sprites.destroy(ijfewojfiqewiof)
        sprites.destroy(sword2)
    sprites.on_overlap(jfijweqiofjewi.player, jfijweqiofjewi.projectile, jfqeiwofjiqweofejwiqop)

    def jfieowqjfeqwiojfieqwop():
        global p2_a, p2_b
        p2_a = 50
        p2_b = 15
    controller.player2.on_button_event(ControllerButton.RIGHT,
        ControllerButtonEvent.PRESSED,
        jfieowqjfeqwiojfieqwop)

    def jfiqewojfioeqwfjeqwofqw():
        global p2_a, p2_b
        p2_a = -50
        p2_b = -15
    controller.player2.on_button_event(ControllerButton.LEFT,
        ControllerButtonEvent.PRESSED,
        jfiqewojfioeqwfjeqwofqw)

    def jfieoqwjfiowejifpqe():
        global P1_a, P1_b
        P1_a = 50
        P1_b = 15
    controller.player1.on_button_event(ControllerButton.RIGHT,
        ControllerButtonEvent.PRESSED,
        jfieoqwjfiowejifpqe)

    def jfewqiofjewiofwq():
        global ijfewojfiqewiof
        ijfewojfiqewiof = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . . c c b b b b .f 3 d d 5 1 5 b 
f 3 d d 5 1 5 b                        . c c b b b b . 
. . . . . . . .                         . . . . . . . .
            """),
            jfeiwqjfioqwejfeiowq,
            P1_a,
            0)
        ijfewojfiqewiof.x += P1_b
    controller.player1.on_button_event(ControllerButton.A,
        ControllerButtonEvent.PRESSED,
        jfewqiofjewiofwq)

    def jfiewoqjfweioqfewq():
        sprites.destroy(Pointer_1)
        jfiqoewjfiewjfieqwoi()
    info.player1.on_life_zero(jfiewoqjfweioqfewq)

    def on_player2_life_zero():
        sprites.destroy(Pointer_2)
        jfioweqjfewfjeiqwjfioqwejfieqwjfioeqwjioefqwjifweqjfeiowq()
    info.player2.on_life_zero(on_player2_life_zero)

    def on_player2_connected():
        controller.player2.move_sprite(jfioewqjfioweqijfiqwo)
    controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

    def on_player1_button_b_pressed():
        global sword2
        if P1_b > 0:
            sword2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . f f f 
                                . . . . . . . . . . . . f 9 9 f 
                                . . . . . . . . . . . f 9 6 9 f 
                                . . . . . . . . . . f 9 6 9 f . 
                                . . . . . . . . . f 9 6 9 f . . 
                                . . . . . . . . f 9 6 9 f . . . 
                                . . f f . . . f 9 6 9 f . . . . 
. . f 9 f . f 9 6 9 f . . . . . 
                                . . . f 9 f 9 6 9 f . . . . . .                                 . . . f 9 9 f 9 f . . . . . . . 

                                . . . e e f 9 9 f . . . . . . .                                 . . e e e . f f 9 f . . . . . . 
f f e e . . . . f f . . . . . .                                 f 9 f . . . . . . . . . . . . . 
f f f . . . . . . . . . . . . .
                """),
                jfeiwqjfioqwejfeiowq,
                P1_b * 5,
                0)
        else:
            sword2 = sprites.create_projectile_from_sprite(img("""
                    f f f . . . . . . . . . . . . . 
                                f 9 9 f . . . . . . . . . . . . 
                                f 9 6 9 f . . . . . . . . . . . 
                                . f 9 6 9 f . . . . . . . . . . 
                                . . f 9 6 9 f . . . . . . . . . 
                                . . . f 9 6 9 f . . . . . . . . 
                                . . . . f 9 6 9 f . . . f f . . 
                                . . . . . f 9 6 9 f . f 9 f . . 
                                . . . . . . f 9 6 9 f 9 f . . . 
                                . . . . . . . f 9 f 9 9 f . . . 
                                . . . . . . . . f 9 9 f . . . . 
                                . . . . . . . f 9 9 f e e . . . 
                                . . . . . . f 9 f f . e e e . . 
                                . . . . . . f f . . . . e e f f 
                                . . . . . . . . . . . . . f 9 f 
                                . . . . . . . . . . . . . f f f
                """),
                jfeiwqjfioqwejfeiowq,
                P1_b * 5,
                0)
        sword2.x += P1_b;pause(100);sprites.destroy(sword2)

    def on_player1_connected():
        controller.player1.move_sprite(jfeiwqjfioqwejfeiowq)
    controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

    def on_player1_button_left_pressed():
        global P1_a, P1_b;P1_a = -50;P1_b = -15
    controller.player1.on_button_event(ControllerButton.LEFT,
        ControllerButtonEvent.PRESSED,
        on_player1_button_left_pressed)

    P1_a = 0;P1_b = 0;p2_a = 0;p2_b = 0;sword2: Sprite = None;Pointer_2: Sprite = None;Pointer_1: Sprite = None;jfioewqjfioweqijfiqwo: Sprite = None;jfeiwqjfioqwejfeiowq: Sprite = None;ijfewojfiqewiof: Sprite = None;scene.set_background_color(0);ijfewojfiqewiof = sprites.create(img("""
            . . . . . . . . 
                . . . . . . . . 
                . c c b b b b . 
                f 3 d d 5 1 5 b 
                f 3 d d 5 1 5 b 
                . c c b b b b . 
                . . . . . . . . 
                . . . . . . . .
        """),
        jfijweqiofjewi.projectile)
    Arrow_22 = sprites.create(img("""
            . . . . . . . . 
                . . . . . . . . 
                . c c b b b b . 
                f 3 d d 5 1 5 b 
                f 3 d d 5 1 5 b 
                . c c b b b b . 
                . . . . . . . . 
                . . . . . . . .
        """),
        jfijweqiofjewi.fejiwfjqefjqewiof)
    jfeiwqjfioqwejfeiowq = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        jfijweqiofjewi.player)
    jfioewqjfioweqijfiqwo = sprites.create(img("""
            . . . . . f f 4 4 f f . . . . . 
                . . . . f 5 4 5 5 4 5 f . . . . 
                . . . f e 4 5 5 5 5 4 e f . . . 
                . . f b 3 e 4 4 4 4 e 3 b f . . 
                . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                . f 3 3 e b 3 e e 3 b e 3 3 f . 
                . f 3 3 f f e e e e f f 3 3 f . 
                . f b b f b f e e f b f b b f . 
                . f b b e 1 f 4 4 f 1 e b b f . 
                f f b b f 4 4 4 4 4 4 f b b f f 
                f b b f f f e e e e f f f b b f 
                . f e e f b d d d d b f e e f . 
                . . e 4 c d d d d d d c 4 e . . 
                . . e f b d b d b d b b f e . . 
                . . . f f 1 d 1 d 1 d f f . . . 
                . . . . . f f b b f f . . . . .
        """),
        jfijweqiofjewi.fjeiwoqfjeqwifiowq)
    sprites.destroy(ijfewojfiqewiof);sprites.destroy(Arrow_22);Pointer_1 = sprites.create(img("""
            . . 7 . . 
                . . 7 . . 
                7 7 7 7 7 
                . . 7 . . 
                . . 7 . .
        """),
        jfijweqiofjewi.fjewqiofjwqefjiewqo)
    Pointer_2 = sprites.create(img("""
            . . 7 . . 
                . . 7 . . 
                7 7 7 7 7 
                . . 7 . . 
                . . 7 . .
        """),
        jfijweqiofjewi.jfiqwjfioqwejfoq)
    info.player2.set_life(3);info.player1.set_life(3);sword2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        jfijweqiofjewi.fjiwqefjiwqefjiwoe)
    p2_b = 99999999;p2_a = 99999990;P1_b = 9999999;P1_a = 999999999

    def on_forever():
        Pointer_1.set_position(jfeiwqjfioqwejfeiowq.x + P1_b, jfeiwqjfioqwejfeiowq.y)
    forever(on_forever)

    def on_forever2():
        Pointer_2.set_position(jfioewqjfioweqijfiqwo.x + p2_b, jfioewqjfioweqijfiqwo.y)
    forever(on_forever2)
except:
    pass
for jfioweqjfewfewqfew in range(10,100):
    fjewqifjioweqjfoiqw = jfioweqjfewfewqfew
    while jfioweqjfewfewqfew != 1:
        jfioweqjfewfewqfew=jifjeiwoqfjioe(jfioweqjfewfewqfew);i+=1;print(f"{jfioweqjfewfewqfew} {i}")
    fjewqifjiewojfiqowe[fjewqifjioweqjfoiqw]=i;i=0
print(fjewqifjiewojfiqowe);print("\n\n");fjewqifjiewojfiqowe = sorted(fjewqifjiewojfiqowe.items(), key=lambda x: x[1], reverse=False);jfieqwjfweqif=0
for i in fjewqifjiewojfiqowe:
    jfieqwjfweqif+=1;print(str(jfieqwjfweqif)+". | "+str(i[0])+" took "+str(i[1])+" moves")
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in range(100):
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp != 99 or fewqfqewfjqewifjqweofweqiofjiqowefjoippp != 0:
        fjeqwoifjiqowejfqwejfoewqjfiqowe+=jifowqjfiqe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp];
    else:
        if jifowqjfiqe[fewqfqewfjqewifjqweofweqiofjiqowefjoippp] == "1":
            fjeqwoifjiqowejfqwejfoewqjfiqowe+="0";
        else:
            fjeqwoifjiqowejfqwejfoewqjfiqowe+="1";
jifowqjfiqe=fjeqwoifjiqowejfqwejfoewqjfiqowe;

for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in jifowqjfiqe:
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == "1":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} closed lockers.");fjeqwiofqweji=0;
for fewqfqewfjqewifjqweofweqiofjiqowefjoippp in jifowqjfiqe:
    if fewqfqewfjqewifjqweofweqiofjiqowefjoippp == "0":
        fjeqwiofqweji+=1;
print(f"There are {fjeqwiofqweji} open lockers.");

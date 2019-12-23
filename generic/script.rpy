#Title Screen
#define title_image = 1
#$ title_image = renpy.random.randint(1, 3)

#if title_image = 1:

#Funky menu stuff




#Character Definitions
define m = Character("[charname]", color="#b3d9ff", what_color="#b3d9ff")
define p = Character("Phillip", color="#FF4D4D", what_color="#FF4D4D")
define s = Character("Sissel", color="#FFFF66", what_color="#FFFF66")
define o = Character("Owen", color="#FF6600", what_color="#FF6600")
define e = Character("Echo", color="#45FFFF", what_color="#45FFFF")
define c = Character("Mrs. Corlisse", color="#FFFFCC", what_color="#FFFFCC")
define d = Character("Mr.Dolores")
define u = Character("???", color="#cd7e99", what_color="#cd7e99")
define r = Character("Mr. Rokov", color="#ffe0b3", what_color="#ffe0b3")
define rr = Character("Remnant", color="#729ac0", what_color="#729ac0")
define b = Character("Black Cat", color="#c66f6c", what_color="#c66f6c")
define br = Character("???", color="#bbff99", what_color="#bbff99")
define cc = Character("Cecilia", color="#bbff99", what_color="#bbff99")

define he = Character("Heather", color="#FF6600", what_color="#FF6600")
define h = Character("Hershel", color="#ffccb3", what_color="#ffccb3")
define j = Character("Jinny", color="#d580ff", what_color="#d580ff")
define mm = Character("Mimir", color="#e48181", what_color="#e48181")
define l = Character("Leila", color="#ff8c54", what_color="#ff8c54")
define ss = Character("Samuel", color="#d98e57", what_color="#d98e57")
define mo = Character("Morse", color="#e5c1a5", what_color="#e5c1a5")
define ha = Character("Heather", color="#FF6600", what_color="#FF6600")
define ol = Character("Oleander", color="#d1795c", what_color="#d1795c")

#Tarot Cards
image phillip tarot = "phillip-tarot.png"
image owen tarot = "owen-tarot.png"
image sissel tarot = "sissel-tarot.png"
image sissel tarot lake = "sissel-tarot-lake.png"
image sissel tarot b = "sissel-tarot-b.png"

image edelweiss = "edelweiss.png"
image owen tarot 9 = "owen9-tarot-card.png"


#Character Icons 

image euca neutral = "euca-neutral.png"
image euca blush = "euca-blush.png"
image euca frown = "euca-frown.png"

image phillip neutral = "phillip.png" 
image phillip frown = "phillip-frown.png"
image phillip smile shrug = "phillip-smile-shrug.png"
image phillip shrug blush = "phillip-shrug-blush.png"
image phillip shrug tired = "phillip-shrug-tired.png"
image phillip tired frown = "phillip-tired-frown.png"
image phillip tired smile = "phillip-tired-smile.png"
image phillip irritated = "phillip-irritated.png"
image phillip angry = "phillip-angry.png"
image phillip sad = "phillip-sad.png"
image phillip no = "phillip-no.png"
image phillip annoyed = "phillip-annoyed.png"
image phillip annoyed look = "phillip-annoyed-look.png"
image phillip serious = "phillip-serious.png"
image phillip shorts = "phillip-shorts.png"
image phillip smug = "phillip-smug.png"
image phillip smile = "phillip-smile.png"
image phillip concerned = "phillip-concerned.png"
image phillip surprised = "phillip-surprised.png"
image black cat = "black-cat.png"

image echo neutral = "Echo.png"
image echo blurry = "Echo-blurry.png"
image echo cracked = "echo-cracked.png"
image echo wish = "echo-wish.png"
image echo wish smile = "echo-wish-smile.png"
image echo shattered = "echo-shattered.png"
image echo shattered frown = "echo-shattered-frown.png"
image echo shattered 2 = "echo-shattered-2.png"
image echo shattered tired = "echo-shattered-tired.png"

image owen neutral = "Owen.png"
image owen frown = "owen-frown.png"
image owen grin = "owen-grin.png"
image owen grin 2 = "owen-grin-2.png"
image owen grin 3 = "owen-grin-3.png"
image owen grin nervous = "owen-grin-nervous.png"
image owen grin closed = "owen-grin-closed.png"
image owen scratch = "owen-scratch.png"
image owen scratch smile = "owen-scratch-smile.png"
image owen sad = "owen-sad.png"
image owen upset = "owen-upset.png"
image owen upset angry = "owen-upset-angry.png"


image owen shorts = "owen-shorts.png"
image owen shorts grin = "owen-shorts-grin.png"
image owen shorts grin closed = "owen-shorts-grin-closed.png"
image owen naked = "Owen-naked.png"
image owen naked grin = "owen-naked-grin.png"
image owen naked grin closed = "owen-naked-grin-closed.png"
image owen underwear = "Owen-underwear.png"
image owen dance = "owen-dance.png"
image owen dance frown = "owen-frown-dance.png"
image owen dance grin = "owen-grin-dance.png"
image owen dance grin closed = "owen-grin-closed-dance.png"
image owen dance angry = "owen-angry-dance.png"

image sissel neutral = "Sissel.png"
image sissel embarrassed = "Sissel-embarrassed.png"
image sissel surprised = "Sissel-surprised.png"
image sissel shirtless = "sissel-shirtless.png"
image sissel shirtless embarrassed = "sissel-shirtless-embarrassed.png"
image sissel lifejacket = "sissel-lifejacket.png"
image sissel lifejacket embarrassed = "sissel-lifejacket-embarrassed.png"
image sissel neutral uniform = "Sissel-neutral-uniform.png"
image sissel embarrassed uniform = "Sissel-embarrassed-uniform.png"
image sissel surprised uniform = "Sissel-surprised-uniform.png"
image sissel naked = "sissel-naked.png"
image sissel naked embarrassed = "sissel-naked-embarrassed.png"
image sissel dance = "sissel-dance.png"
image sissel dance embarrassed = "sissel-embarrassed-dance.png"
image sissel wtf = "sissel-wtf.png"
image sissel wtf blush = "sissel-wtf-blush.png"
image sissel shocked = "sissel-shocked.png"
image sissel shocked blush = "sissel-shocked-blush.png"
image sissel angry = "sissel-angry.png"
image sissel nervous = "sissel-nervous.png"
image sissel smile = "sissel-smile.png"
image sissel upset = "sissel-upset.png"
image sissel indignant = "sissel-indignant.png"
image sissel annoyed = "sissel-annoyed.png"
image sissel happy = "sissel-happy.png"
image sissel bittersweet = "sissel-bittersweet.png"
image sissel embarrassed jacket = "sissel-embarrassed-jacket.png"
image sissel neutral jacket = "sissel-neutral-jacket.png"
image sissel nervous jacket = "sissel-nervous-jacket.png"
image sissel wtf jacket = "sissel-wtf-jacket.png"
image sissel smile jacket = "sissel-smile-jacket.png"
image sissel indignant jacket = "sissel-indignant-jacket.png"
image sissel surprised jacket = "sissel-surprised-jacket.png"
image sissel happy jacket = "sissel-happy-jacket.png"
image sissel crying = "sissel-crying.png"


image jinny neutral = "jinny-neutral.png"
image jinny angry = "jinny-angry.png"
image jinny thoughtful = "jinny-thoughtful.png"
image jinny thoughtful smile = "jinny-thoughtful-smile.png"
image jinny wtf = "jinny-wtf.png"
image jinny dance = "jinny-dance.png"
image jinny dance frown = "jinny-dance-frown.png"
image jinny shirt = "jinny-shirt.png"
image jinny smirk shirt = "jinny-smirk-shirt.png"

image halley neutral = "halley.png"
image halley smile = "halley-smile.png"
image halley wish = "halley-wish.png"
image halley terrified = "halley-terrified.png"

image hershel = "hershel.png"
image hershel frown = "hershel-frown.png"
image hershel upset = "hershel-upset.png"
image hershel grin = "hershel-grin.png"
image hershel nervous = "hershel-nervous.png"
image hershel crying = "hershel-crying.png"
image hershel sad = "hershel-sad.png"

image cecilia neutral = "cecilia-neutral.png"
image cecilia grin = "cecilia-grin.png"
image cecilia bittersweet = "cecilia-bittersweet.png"

image samuel neutral = "samuel.png"
image samuel smile = "samuel-smile.png"
image samuel awkward = "samuel-awkward.png"
image samuel boxers = "samuel-boxers.png"
image samuel boxers smile = "samuel-boxers-smile.png"
image samuel naked = "samuel-naked.png"

image morse neutral = "morse-neutral.png"

image oleander neutral = "oleander.png"
image oleander frown = "oleander-frown.png"
image oleander frown shrug = "oleander-frown-shrug.png"
image oleander smile shrug = "oleander-smile-shrug.png"

image bradley = "bradley.png"
image bradley faint = im.MatrixColor(
    "bradley.png",
    im.matrix.opacity(.3))
image bradley wish = "bradley-wish.png"

image euca card = "Euca_ID.png"
image newspaper = "newspaper.png"
image poster = "black-cat-poster.png"
image poster 2 = "black-cat-poster2.png"
image jade coin = "jade-coin.png"
image crane = "crane.png"

image remnant = "remnant.png"
image remnant smile = "remnant-smile.png"
image remnant smile violet = "remnant-smile-violet.png"
image remnant smile yellow = "remnant-yellow.png"
image remnant ripped = "remnant-ripped.png"

image pigeon = "pigeon.png"
image pigeon scream = "pigeon-scream.png"
image pigeon screaming:
    "pigeon.png"
    pause 0.1
    "pigeon-scream.png"
    pause 0.1
    repeat

#Postition Variables
init:
    $ farright = Position(xpos = 0.8, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ farleft = Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ offleft = Position(xpos = 0.001)
    $ rcenter = Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

#Variables
define game_end = "false"
define echo_wish = "none"

define encourage_phillip = "none"
define entrance = "door"
define steal_wallet = "false"
define photo_1 = "none"
define fight_dolores = "false"
define day4_item = "none"
define day4_side = "none"
define met_bradley = "false"

define owen_truth = "none"
define sissel_truth = "none"

define seduce_samuel = "false"
define owen_dance_lie = "false"
define owen_snoop = "false"
define owen_blow = "false"

define phillip_pigeon_snoop = 0

define sissel_outfit = "leather"

#Cutscenes
image photograph = im.Sepia("photograph.jpg")
image repeat_screen = "repeat-screen.png"
image skyline = "skyline.jpg"
image possessed1 = "possessed.png"
image possessed2 = "possessed2.png"
image clockwork = "clockwork.jpg"
image shower = "shower.jpg"
image small sissel = "small-sissel.jpg"
image sissel forest = "sissel-forest.jpg"
image sissel forest 2 = "sissel-forest2.jpg"

image owen_rainbow1 = "owen_rainbow1.jpg"
image owen_rainbow2 = "owen_rainbow2.jpg"
image rainbow_stare1 = "rainbow_stare1.jpg"
image rainbow_stare2 = "rainbow_stare2.jpg"


image sunset phillip = "sunset-phillip.jpg"
image sunset owen = "sunset-owen.jpg"
image canoe = "canoe.jpg"
image selfie = "selfie.jpg"
image group photo 1 = "group-photo.jpg"
image group photo 2 = "group-photo2.jpg"

image sissel_volleyball = "volleyball.jpg"
image owen_swimming = "swimming.jpg"

image encouter 1 = "encounter1.jpg"
image encounter 2 = "encounter2.jpg"
image encounter 2 sepia = im.Sepia("encounter2.jpg")

#Cutscenes Day 7
image owen_day7 1 sepia = im.Sepia("owen-day7-1.jpg")
image owen_day7 2 sepia= im.Sepia("owen-day7-2.jpg")
image phillip_day7 1 sepia = im.Sepia("phillip-day7-1.jpg")
image phillip_day7 2 sepia = im.Sepia("phillip-day7-2.jpg")
image phillip_day7 3 sepia = im.Sepia("phillip-day7-3.jpg")
image phillip_day7 4 sepia = im.Sepia("phillip-day7-4.jpg")

image owen_day7 1  = "owen-day7-1.jpg"
image owen_day7 2 = "owen-day7-2.jpg"
image phillip_day7 1  = "phillip-day7-1.jpg"
image phillip_day7 2  = "phillip-day7-2.jpg"
image phillip_day7 3  = "phillip-day7-3.jpg"
image phillip_day7 4  = "phillip-day7-4.jpg"

#Cutscenes Phillip

image phillip_kidnapping = "phillip_kidnapping.jpg"

#Cutscenes Owen
image city_diagram = "city-diagram.jpg"
image silhouette1 = "silhouette1.png"
image silhouette2 = "silhouette2.png"
image owen_familyphoto = "owen-familyphoto.jpg"

image owen_jump1 = "owen_jump1.jpg"
image owen_jump2 = "owen_jump2.jpg"

image heather_fight1 = "heatherfight1.jpg"
image heather_fight2 = "heatherfight2.jpg"
image heather_fight3 = "heatherfight3.jpg"
image heather_fight4 = "heatherfight4.jpg"
image heather_fight5 = "heatherfight5.jpg"

image owen_outcry1 = "owen_outcry1.jpg"
image owen_outcry2 = "owen_outcry2.jpg"
image owen_outcry1 sepia = im.Sepia("owen_outcry1.jpg")


image samuel_seduce = "samuel-seduce.jpg"
image samuel_caught = "caught.jpg"
image samuel_rescue = "rescue.jpg"
image motorbike_crop = "motorbike-crop.jpg"
image motorbike_scene = "motorbike-scene.jpg"
image samuel_gun = "samuel-gun.jpg"
image samuel_gun sepia = im.Sepia("samuel-gun.jpg")

image owen_blow1 = "owen_blow.jpg"
image owen_blow2 = "owen_blow2.jpg"
image owen_blow3 = "owen_blow3.jpg"

#Cutscenes Sissel
image hershel_chainsaw = "hershel-chainsaw.jpg"
image chocolate_sculpture = "chocolate-sculpture.jpg"
image trumpet_scene = "trumpet_scene.jpg"
image broken_sculpture = "broken_sculpture.jpg"

image campfire = "campfire.jpg"
image sissel_dance = "sissel-dance.jpg"
image hershel_photo = "hershel-photo.jpg"
image bradley_alleyway = "bradley-alleyway.jpg"
image bradley_alleyway2 = "bradley-alleyway2.jpg"

image sissel_cafefront = "sissel_cafefront.jpg"
image sissel_bedsharing = "sissel-bedsharing.jpg"
image sissel_euca_scene1 = "Sissel_Euca_scene1.jpg"
image sissel_euca_scene2 = "Sissel_Euca_scene2.jpg"
image sissel_euca_scene3 = "Sissel_Euca_scene3.jpg"
image sissel_euca_scene4 = "Sissel_Euca_scene4.jpg"

image phillip-poster-scene1 = "phillip-poster-scene1.jpg"
image phillip-poster-scene2 = "phillip-poster-scene2.jpg"
image phillip-poster-scene1-scribble1 = "Phillip-poster-scene-scribble1.png" 
image phillip-poster-scene2-scribble2 = "Phillip-poster-scene-scribble2.png" 
image sissel_cafemeetup = "sissel_cafemeetup.jpg"

image remnant_devour = "remnant_devour.jpg"
image remnant_awaken = "remnant_awaken.jpg"

image sissel_log1 = "sissel_log1.jpg"
image sissel_log2 = "sissel_log2.jpg"
image sissel_cassette1 = "sissel_cassette.jpg"
image sissel_cassette2 = "sissel_cassette2.jpg"
image cecilia1 = "cecilia1.jpg"
image cecilia2 = "cecilia2.jpg"
image cecilia3 = "cecilia3.jpg"

image sissel_cry = "sissel_cry.jpg"
image sissel_bone1 = "sissel_bone1.jpg"
image sissel_bone2 = "sissel_bone2.jpg"

image sissel_memoryscene1 = "memory-scene-1.jpg"
image sissel_memoryscene2 = "memory-scene-2.jpg"
image sissel_memoryscene3 = "memory-scene-3.jpg"
image sissel_memoryscene4 = "memory-scene-4.jpg"
image sissel_memoryscene5 = "memory-scene-5.jpg"
image sissel_memoryscene6 = "memory-scene-6.jpg"
image sissel_memoryscene7 = "memory-scene-7.jpg"
image sissel_memoryscene8 = "memory-scene-8.jpg"
image sissel_memoryscene9 = "memory-scene-9.jpg"
image sissel_memoryscene10 = "memory-scene-10.jpg"
image sissel_memoryscene11 = "memory-scene-11.jpg"

image hershel_remnant = "hershel_remnant.jpg"
image sissel_burningbuilding = "sissel_burningbuilding.jpg"
image sissel_burningkitchen = "sissel_burningkitchen.jpg"
image jinny_push = "jinny_push.jpg"
image jinny_window = "jinny_window.jpg"
image afterfire_1 = "afterfire_1.jpg"
image afterfire_2 = "afterfire_2.jpg"
image jinny_sissel_death1 = "jinny_sissel_death1.jpg"
image jinny_sissel_death2 = "jinny_sissel_death2.jpg"
image jinny_sissel_death3 = "jinny_sissel_death3.jpg"
image hershel_hospital = "hershel_hospital.jpg"
image sissel_train = "sissel_train.jpg"
image halley_tear1 = "halley_tear1.jpg"
image halley_tear2 = "halley_tear2.jpg"

image jinny_discovery = "jinny_discovery.jpg"
image jinny_discovery sepia = im.Sepia("jinny_discovery.jpg")

image cecilia_death1 = "cecilia_death1.jpg"
image cecilia_death2 = "cecilia_death2.jpg"
image cecilia_death3 = "cecilia_death3.jpg"
image cecilia_death4 = "cecilia_death4.jpg"
image bradley_request1 = "bradley_request1.jpg"
image bradley_request2 = "bradley_request2.jpg"
image remnant_appearance = "remnant_appearance.jpg"

image halleygrab = "halleygrab.jpg"
image halleylook = "halleylook.jpg"
image remnant_grab = "remnant_grab.jpg"
image halley_transform1 = "halley_transform1.jpg"
image halley_transform2 = "halley_transform2.jpg"
image halley_transform3 = "halley_transform3.jpg"
image sculpture_melted = "sculpture_melted.jpg"
image sissel_repair = "sissel_repair.jpg"
image sculpture_complete = "sculpture_complete.jpg" 

image sissel_formal1 = "sissel_formal1.jpg"
image sissel_formal2 = "sissel_formal2.jpg"
image sissel_formal3 = "sissel_formal3.jpg"
image sissel_leather1 = "sissel_leather1.jpg"
image sissel_leather2 = "sissel_leather2.jpg"
image sissel_leather3 = "sissel_leather3.jpg"
image sissel_stripper1 = "sissel_stripper1.jpg"
image sissel_stripper2 = "sissel_stripper2.jpg"
image sissel_stripper3 = "sissel_stripper3.jpg"
image sissel_voucher_threat = "sissel_voucher_threat.jpg"

image sissel_restaurant_snoop 1 = "sissel_restaurant_snoop1.jpg"
image sissel_restaurant_snoop 2 = "sissel_restaurant_snoop2.jpg"
image sissel_restaurant_snoop 3 = "sissel_restaurant_snoop3.jpg"
image sissel_kiss1 = "sissel_kiss1.jpg"
image sissel_kiss2 = "sissel_kiss2.jpg"


#Background Images
image alleyway = "alleyway.jpg"
image alleyway rain = "alleyway-rain.jpg"
image alleyway rain sepia = im.Sepia("alleyway-rain.jpg")

image school = "school.jpg"
image school sepia = im.Sepia("school.jpg")
image school colorless = im.Grayscale("school.jpg")
image school dusk = "school-dusk.jpg"
image school night = "school-night.jpg"
image school rainy = "school_rainy.jpg"
image black = "#000000"
image white = "#ffffff"
image school back = "school_back_entrance.jpg"
image school back sepia = im.Sepia("school_back_entrance.jpg")
image school back rainy = "school_back_entrance_rainy.jpg"
image school back night = "school_back_entrance_night.jpg"
image school lobby = "school_lobby.jpg"
image school lobby sepia = im.Sepia("school_lobby.jpg")
image library = "library.jpg"
image ballroom = "ballroom.jpg"
image ballroom dark = im.MatrixColor(
    "ballroom.jpg",
    im.matrix.brightness(-.3))

image bubbles = "bubbles.jpg"
image courtyard = "courtyard.jpg"
image courtyard dusk = "courtyard-dusk.jpg"
image lecture hall = "lecture-hall.jpg"

image gym = "gym.jpg"
image gym breakroom = "breakroom.jpg"
image dorm = "dorm.jpg"
image dorm night = "dorm-night.jpg"
image dorm hallway = "dorm-hallway.jpg"
image dorm hallway night = im.MatrixColor(
    "dorm-hallway.jpg",
    im.matrix.brightness(-.3))
image dorm roof = "dorm-roof.jpg"
image dorm roof dusk = "dorm-roof-dusk.jpg"
image dorm roof night = "dorm-roof-night.jpg"
image PO dorm = "Po-dorm.jpg"

image kitchen = "kitchen.jpg"
image kitchen night = "kitchen-night.jpg"
image dining hall = "dining-hall.jpg"

image shower room = "shower_room.jpg"
image hallway = "hallway.jpg"
image hallway sepia = im.Sepia("hallway.jpg")
image art room = "art-room.jpg"
image art room sepia = im.Sepia("art-room.jpg")
image office = "office.jpg"
image office night = "office-night.jpg"
image cafe front = "cafe-front.jpg"
image cafe front-dark = im.MatrixColor(
    "cafe-front.jpg",
    im.matrix.brightness(-.3))
image cafe back = "cafe-back.jpg"
image cafe kitchen = "cafe-kitchen.jpg"
image cafe kitchen-dark = im.MatrixColor(
    "cafe-kitchen.jpg",
    im.matrix.brightness(-.5))
image cafe attic = "cafe-attic.jpg"
image cafe attic-dark = im.MatrixColor(
    "cafe-attic.jpg",
    im.matrix.brightness(-.5))
image cafe attic night = "cafe-attic-night.jpg"
image sisselroom = "sisselbedroom.jpg"
image sisselroom sepia = im.Sepia("sisselbedroom.jpg")
image sisselkitchen = "sisselkitchen.jpg"
image sisselkitchen sepia = im.Sepia("sisselkitchen.jpg")
image sissellawn = "sissellawn.jpg"
image sissellawn sepia = im.Sepia("sissellawn.jpg")

image restaurant exterior = "restaurant-exterior.jpg"
image restaurant interior = "restaurant-interior.jpg"
image buffet = "buffet-table.jpg"
image restaurant burning = "restaurant-burning.jpg"

image lake = "lake.jpg"
image lake night = "lake-night.jpg"
image lake road = "lake-road.jpg"
image lake road night = "lake-road-night.jpg"
image lake water = "lake-water.jpg"
image lake shower = "lake-shower.jpg"
image cottage = "cottage.jpg"
image cottage night = "cottage-night.jpg"
image wishing well = "wishing-well.jpg"
image patreon = "Patreon-page.jpg"

image robins nest exterior = "robins-nest-exterior.jpg"
image robins nest interior = "robins-nest-interior.jpg"
         
image community center = "community-center.jpg"
image community lobby = "community-lobby.jpg"
image ice rink = "rink.jpg"
image pantry = "pantry.jpg"
         
        
image derry street = "derry-street.jpg"
image derry street night ="derry-street-night.jpg"
image derry park = "derry-park.jpg"
image derry park night ="derry-park-night.jpg"

image derry house = "owen-house.jpg"
image derry house sepia = im.Sepia("owen-house.jpg")
image derry house hallway = "derry-house-hallway.jpg"
image crane room = "crane-room.jpg"
image crane room sepia = im.Sepia("crane-room.jpg")
         
#Others:
style button_text:
    text_align 0.5
    drop_shadow (1, 1)
    drop_shadow_color '#424242'
        
        
        
        
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
        
init:
    image confetti = Fixed(
    SnowBlossom("confetti1.png", count=15, border=50, xspeed=(20, 60), yspeed=(100, 250), start=0, horizontal=False),
    SnowBlossom("confetti2.png", count=15, border=50, xspeed=(20, 60), yspeed=(100, 250), start=0, horizontal=False),
    SnowBlossom("confetti3.png", count=15, border=50, xspeed=(20, 60), yspeed=(100, 250), start=0, horizontal=False))
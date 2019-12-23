label day3:
    
$ persistent.current_route = "default"
"{b}Day 3:{/b}{w=.3} Abandoned Wishes"

scene black with Dissolve(2.0)
play music "easy-lemon.mp3" fadein 3 fadeout 3
scene dorm with Dissolve(2.0)

"The morning sun filters through my window.{p=.1}It says, \"Hey! Let's stab this poor kid's eyeballs until he's awake!\""
"With a groan, I sit up and rub the drowsiness from my eyes."
"It seems like my fever's completely gone."

"I hop out of bed and stretch. {p=.3}Huh?{p=.3}It looks like someone left a pile of presents on my table."
"There was a potted plant with brilliant blue flowers.{p=.5}The note next to it reads, \"Hope you feel better soon!\"{p=.3}~Phillip"
"There was also a large pile of hand-baked pastries, obviously from Sissel."
"And then there are...socks?{p=.1}\"Nothing's worse than cold feet when you're sick.\" ~Owen"

m "Aw, that was nice of them-{p=.1}Oof!"

show echo neutral with dissolve

e "[charname]! How are you feeling? Has your fever passed?"
m "Uuuugh Echo, get your hands off my face."
e "Mmm you seem pretty alright. Looks like your friends worried for nothing."
e "They all snuck into your room last night and left a bunch of gifts."
e "Owen tried to give you a goodnight kiss but Sissel and Phillip dragged him away before he could."
m "How....thoughtful."
e "Phillip's choice of flowers is kinda weird though.{p=.1}\"Forget-me-nots\" are usually for funerals."
m "...that kid's got a morbid sense of humor..."
m "They're a pretty shade of blue though. And there are little white clovers growing around the edges too~"
e "Flowers aside, [charname], you better head off to class soon. I think there's an event happening today."
e "Here, I'll help you get dressed."
m "Ugh, I can dress myself Echo! No need to baby me."
e "Heh, if you say so."

scene courtyard
with Dissolve(3.0)
stop music
play music "busy-city-street.mp3" fadein 3 fadeout 3

"A huge crowd of students are gathering around the courtyard. People from all different classes were here. I wonder what's going on?"
"Oh, and Sissel's here too."
show sissel neutral
with dissolve

s "Yo, mornin' [charname]. {p=.1}How are you feeling?"
m "I'm doing great. Thanks for all the pastries this morning! {p=.1}That was really sweet of you."
hide sissel neutral
show sissel embarrassed
s "I'm not sweet. {p=.1}Geez, why do you always talk to me like I'm a little kid?"
m "It's fun seeing you all embarrassed."
hide sissel embarrassed
show sissel neutral
m "By the way, why is everyone gathered here? I thought we were having class."
s "Oh, the school's planned a-"

"Suddenly, Sissel was interrupted by a ugly growl behind us."
"It was the old rat, Mr. Dolores."

d "The school is meeting here for a mandatory team-building activity field trip to Bradley Lake today."
d "Did you incompetents even bother reading the email that the staff sent out?"

"Specks of spit flies from Mr. Dolores' yellow teeth as he spoke."
m "W-well no. I didn't realize-"
d "Pah! You call yourself a student? Damn lazy kids these days-"
"Sissel jumped in front of me and practically snarled."
s "He was ill!! Cut him some slack."
d "Watch your tone brat! Is this how you treat your teacher?"
s "Oh you're a teacher? You sure don't act like it-"

hide sissel neutral
with dissolve

"Mr. Dolores grabbed Sissel roughly by the collar of his shirt and nearly picked him up off the ground."
"Their faces were dangerously close as they glared daggers into each other."
d "Learn some respect, boy. {p=.1}I can kick you out of this academy with a single phone call."
d "Get ready to crawl back into the streets you sick little-"

hide sissel neutral
with dissolve
stop music
c "{size=+10}MR. DORCAS DOLORES.{/size}"

"Everything fell into silence."
"Mrs. Corlisse walked toward us, parting the crowd effortlessly."
"Her stern face seemed to scare even Mr. Dolores, although he still held firm to Sissel's collar."

c "...Surely, you're not threatening my students?"
"Mr. Dolores hissed furiously."
d "Not at all, {i}Corlisse{/i}."
d "I'm simply disciplining rowdy individuals."

"He puffed up angrily, as if trying to intimidate Mrs. Corlisse. {p=.1}But she looked unfazed and held her head high."

c "Mr. Sissel doesn't seem to have done anything wrong."
c "Regardless, unless the rules have changed since the last 20 years I've worked here, man-handling students is against school policy."
c "Unless a certain teacher is unable to let go of trivial prejudices...?"

play music "volatile.mp3" fadein 3

d "{size=+10}You dare accuse me?!!!{/size}"
"Dolores seems to be losing it, puffing his huge ugly face in Mrs. Corlisse's direction."
"Despite being a fragile old lady, Mrs. Corlisse manages to maintain a commanding air about her."
"But still, one swing from Mr. Dolores could easily knock her over. {p=.1}The tension was climbing and Mr.Dolores still has an iron grip on Sissel."
"What should I do?"

menu: 
    "Call for Echo.":
        "I hiss quietly under my breath."
        m "Echo, are you there?!"
        
        play sound "ghost.mp3" fadein 2
        show echo blurry with dissolve
        
        e "Yo [charname], you called?"
        m "Echo, you have to help us out here!"
        m "Can't you use some ghostly voodoo shit and drive Dolores away?"
        
        e "How many times do I have to tell you?{p=.1}I'm not a-"
        m "Yeah yeah, you're not a ghost.{p=.1}But there's gotta be {i}something{/i} you can do!"
        "Echo stares at the struggling figures of Sissel and Mr. Dolores thoughtfully."
        e "...................."
        e "...So you want to drive Mr. Dolores away?"
        m "YES!!"
        e "Very well then."
        play sound "echo-wish.wav"
        
        hide echo blurry
        show echo wish smile
        with Dissolve(3.0)
        
        with dissolve
        e "Your wish is my command."
        
        hide echo wish smile
        with dissolve
        play sound "wind.mp3"
        
        "The wind around the courtyard abruptly picked up, whipping about everyone like a snarling beast."
        "Everyone's hair and hats fluttered about wildly as they struggled to stay composed."
        "In the corner of my eye, something weird flew off the top of Mr. Dolores' head and soared away in the wind."
        stop music fadeout 3
        
        m "...................."
        m ".....Oh wow."
        m "...Uh, Mr. Dolores?"
        d "What do you want brat? Better be important."
        play music "carefree-tune.mp3" fadein 3 fadeout 2
        
        m "...Well, it's not exactly...{p=.1}...But your toupee just flew away."
        
        d "W-wah?!"
        "Mr. Dolores felt the top of his head and let out a high-pitched squeal of horror and panic."
        "I've never seen someone grow so beet red."
        "He dropped Sissel like a sack of potatoes and ran off into the crowd to find his missing hair.{p=.1}(It's probably never coming back)."
        
        play music "cafe-music.mp3" fadein 2
        
        "That went pretty well."
        show sissel neutral
        with dissolve
        "I offered Sissel a hand as he struggled back onto his feet."
        m "You ok Sissel?"
        s "Could be better.{p=.1}I'm feeling fairly homicidal."
        c "Mr. Sissel?{p=.1}I hope you are uninjured."
        "Mrs. Corlisse approaches us, her aged face scrunched up with concern."
        c "I'd like to apologize to you as a staff member for that...episode."
        "Sissel snarls furiously."
        s "Don't appologize for that jackass's attitude!{p=.1}He should be the one who's sorry!"
        c "{i}Language,{/i} Mr. Sissel.{p=.1}{size=-10}However correct you are...{/size}"
        c "Anyways, I believe you and Mr. [charname] should join your classmates now.{p=.1}The school's about ready to depart."
        s "Sure thing."
        "As Mrs. Corlisse turns to walk away, Sissel pulls me over and ruffles my hair with a grin."
    "Start a fight.":
        $ fight_dolores = "true"
        "You know what, this guy is a jackass.{p=.1}Fuck him."
        "I ran up behind Mr. Dolores and send a kick right between his stubby little legs."
        
        stop music
        play sound "bump.mp3"
        "{i}{b}Ding!{/b}{/i}"
        play music "carefree-tune.mp3" fadein 2

        d "Wh-{p=.1}{size=+10}EEAAAAAAAAH-!!{/size}"
        "The bastard's voice jumped an octave as he fell like a sack of potatoes."
        
        show sissel neutral
        with dissolve
        
        "Sissel quickly picks himself off the ground and stares at me with a mix of awe and horror."
        s "Holy shit [charname], I didn't know you had it in you!"
        s "I think he's actually crying."
        "Sure enough, tears were streaming out of Mr. Dolores's squinty eyes and he gasped for air."
        m "Wow, I didn't mean to kick him so hard-"
        stop music
        "Suddenly, a looming shadow covered us.{p=.1}Sissel and I found ourselves face-to-face with the stern figure of Mrs. Corlisse."
        m "M-Mrs. Corlisse!{p=.1}I-I'm sorry! He was- I mean, he grabbed Sissel and I wasn't thinking and-{size=-10}...pleasedon'texpellme...{/size}"
        c ".......Mr. [charname],{p=.5}I believe you and Mr. Sissel should get out of sight before Mr. Dolores regains consciousness."
        m "What-?"
        play music "easy-lemon.mp3" fadein 2
        "Sissel suddenly grabs my wrist and pulls me toward the crowd of other students."
        s "Yes of course! Thanks Mrs. Corlisse!"
        "As the two of us ran away, I think I saw Mrs. Corlisse smile and mouth {i}\"Nice kick.\"{/i}"
        "When we got to a safe distance away from the scene, Sissel turns to me with an ecstatic and amazed grin."



show sissel happy with dissolve
s "Thanks for coming to my rescue, [charname].{p=.1}You're turning into my knight in shining armor."
m "Am I?"
m "That makes you the fair damsel-in-distress, doesn't it?{p=.1}You gotta start wearing a dress to match your part, Sissel."
"Sissel gives me a friendly punch to the arm."
s "You'd probably be into that."
m "Well I certainly wouldn't be complaining-"
s "C'mon, let's join the class. We're gonna be left behind."

scene black with Dissolve(3.0)

if fight_dolores == "false":
    scene school
    with Dissolve(2.0)
    "It turned out that the Academy was too cheap to actually bus us to Bradley Lake and made us walk there on foot."
    "It was only a twenty minute walk though.{p=.1} This gave me time to organize my thoughts from earlier."
    m "....Echo, you still there?"
    
    play sound "ghost.mp3"
    show echo blurry
    with dissolve
        
    e "*cough*cough*"
    e "*ahem*{p=.1}Hello again [charname]. What's up?"
    m "I wanted to thank you for earlier.{p=.1}It was pretty awesome to see you in action!"
    m "I didn't know you could make the wind blow like that."
       
    e "I can't, technically.{p=.1}My powers don't work like that."
    m "What do you mean?"
    e "Eh, it's hard to explain."
    "Echo groans and squeezes his eyes shut, as if to fight off a bad headache."
    e "Wishes...we can twist circumstances and coincidences.{p=.1}The wind just {i}{b}happened{/b}{/i} to blow harder in that moment."
    e "It's a bit like yesterday, when you met that girl."
    e "She made it so that you just {i}{b}happen{/b}{/i} to fall sick with a fever."
        
    m "So...it's kinda like you inflict people with bad luck?"
    e "Something like that."
    e "Most of the time we can't interfere directly, so we force something else to instead."
    e "I should warn you though, everything we do will have consequences.{p=.1}Next time you ask me to do something, think carefully first."
    m "Sounds good to me."
        
    "Echo sighs tiredly."
    "I rub my eyes and squint at him.{p=.1}Is it just my imagination,{w}or is he growing more transparent than usual?"
    e "I'm a bit tired, [charname]. Mind if I rest a little?"
    m "Not at all."
    
    play sound "ghost.mp3"
    hide echo blurry
    with dissolve
        
    "With a smile, Echo steps toward me."
    "He seemed to disappear like dust in the wind and flowed into my chest, where my camera was."
    "With a small smile, I whisper \“Thank you\” and turn to rejoin the crowd of students."
    
    
scene black with Dissolve(2.0)
play music "snowy-street.mp3" fadein 3 fadeout 3
scene school with Dissolve(2.0)


"The school continues to walk through the city streets like a pack of disorganized pigeons."
"Teachers seem to be trying to get students' attention but everyone's chatting too much to give a shit."
"Finally, Mrs. Corlisse summersaults onto a nearby fence and shouts that we're about to arrive at Bradley Lake, and that we're required to participate in at least two teambuilding activities."
"Her announcement was immediately drowned out by applause."

show sissel neutral at Position(xpos = 0.8, xanchor=0.5, ypos=0.5, yanchor=0.5)
with dissolve

s "Wow, Mrs. Corlisse is pretty nimble for someone her age."
s "By the way, [charname], how are you feeling? You were sick as a dog last n-"

"I suddenly feel a rough slap on the back."

show owen neutral
with dissolve
show phillip tired smile at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5)
with dissolve

o "[charname]! How are you doing kiddo?"
p "'Morning [charname]. Feeling better?{p=.1} Here, I got you a coffee."

m "Thanks Phillip.{p=.1}You're the best mother hen."
hide phillip tired smile
show phillip shrug tired at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5)
with dissolve
p "Pfft if you say so."
hide phillip shrug tired
show phillip tired smile at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5)
with dissolve

"Everyone suddenly yelps as I pull them all into one big group hug."
m "Thanks so much for the presents last night, you guys. It was really sweet of you~"
p "Eheh, it's no biggie. It's great to see you up on your feet again."
s "Just stop getting sick, loser."
o "Glad you liked 'em!"

s "...speaking of which, what kind of twat gives people socks?"
o "Hey!{p=.1}Nothing's worse than getting cold feet when you're sick!"
s "Leave it to Owen to leave horrible gifts."
m "I think they were pretty nice."
s "Really?{p=.1}Neon orange socks?"
o "It's so every time [charname] puts them on, he'll think of me!"
s "Is this you admitting you have a foot fetish?"
m "Well, fetish or not, I like them. Thanks Owen."

"Owen grins and puffs out his chest with pride, almost elbowing Phillip in the face."
"He looks a bit dazed this morning actually..."

m "Phillip?"
p ".................."
m "Hellooooo Phillip?"
p "Hm?"
m "You don't look so good, are you getting sick too?"
p "No no...{p=.1}It's just that I didn't get much sleep last night."
p "It happens pretty often, nothing to worry about."
s "Probably can't sleep with Owen snoring all night."
o "H-hey!"
m "Anyway!!"
"I cut in quickly before they can argue again."
m "Interesting choice of flowers, Phillip. I really like that shade of blue~"
p "Oh, the forget-me-nots?{p=.1}I got them so everyone will remember you in case you died."
m "...T-thanks Phillip."

scene black with Dissolve(2.0)
scene lake road with Dissolve(2.0)
"The fresh air of the lakeside felt great after a night of feverish sleep."
"The view here is just beautiful. {p=.1}Who would have thought there'd be such a natural place like this in the big city?"
play sound "ghost.mp3"
stop music fadeout 3
play music "snowdrop.mp3" fadein 2 fadeout 3
"........"
"..............?"
m "What was that just now?"
e "What's wrong, [charname]?"
m "I swore I just felt a chill.{p=.1}It felt like those times I ran into you and that red-eyed girl."
m "Do you think there's another ghost here?"
e "Hm......."
e "I don't sense any malice. It feels fairly weak too.{p=.3}Probably just an abandoned wish still floating about."
m "Abandoned wish?"
e "....When people die or give up on their dreams, they leave their unfulfilled wishes behind."
e "They usually just wander around aimlessly until they either fade away or become corrupted."
e "This one feels like it's on the verge of disappearing, so it's no danger to you."
e "There's nothing to worry about [charname], just go on with your activities."
m "So they just disappear? That just sounds unfair..."
e "Wishes are made and abandoned every day, [charname]."
e "People are fickle."
e "They want something one day,{p=.3}and change their minds the next."
e "If we spent our time worrying about every wish, we'd be wasting our lives away."
m "...But what about you Echo? You're a wish too."
e "........"
e "You don't need to worry about me."
m "But-"
stop music fadeout 2
play music "easy-lemon.mp3" fadein 2 fadeout 3

show sissel neutral with dissolve

s "{size=+15}[charname]!!!{/size}"
m "W-what?!"
s "We've been yelling your name forever. Get your head out of the clouds, will you?"
s "We still need to decide what activity we should do."

show owen neutral at farleft
with dissolve
show phillip neutral at farright
with dissolve

"Activities huh? {w=.3}Sounds kinda wretched.{p=.3}I've never been much of an athlete..."
m "Having a little splash in the lake sounds pretty fun though."
s "Ugh......"
p "Hey Sissel,{w=.3} you feeling alright? {w=.3}You look a bit pale."
"Sissel gave a startled jump before scoffing dismissively."
s "N-nothing's wrong! {p=.3}I'd just rather not get wet."
show owen grin closed with dissolve
o "C'mon man, {w=.3}where's the fun in that?{p=.3}Let's just dive in and let loose!"
o "Heh I can't wait to see Phillip in a skimpy bathing suit~"
"Wow,{w=.3} you'd think he'd be a bit more subtle than that."
show owen neutral with dissolve
o "And you don't need to worry about drowning, Phillip{p=.1}I'll be ready to perform mouth-to-mouth and save you~"
hide phillip neutral
show phillip smile shrug at farright
with dissolve
p "In that case, please let me drown in peace."
m "Well how about kayak racing? {p=.3}It's something we can do in the lake, but it won't get us completely wet."
m "It's a pretty good compromise."


s "W-wah? B-but-!"
hide phillip
show phillip neutral at farright
with dissolve
p "Excellent! {p=.1}Looks like there's only room for 2 people per boat though."
p "[charname], do you want to boat with-"
s "{size=+10}[charname] is boating with me!!{/size}"
"Sissel's voice seemed to rise by an octave or two."
o "That leaves me and you, Phillip."
o "Hehe, looks like we'll be partners!"
p "Eheh...sounds great."
p "Anyway, let's go get changed."
o "Wanna share a stall, Phillip?{p=.1}We can do a bit of teammate bonding-"
hide phillip neutral
show phillip smile shrug at farright
with dissolve
p "Hey Owen! There's this wonderful thing called personal space. Have you heard of it?"

scene lake
with Dissolve(2.0)

show sissel embarrassed

"As Phillip and Owen walk off towards the changing rooms with the rest of the students, I feel Sissel suddenly grab me and pull me aside."
s "[charname], I-I..."
s "I can't swim for shit! What am I going to do?"
s "Can't just quit, I don't wanna lose face in front of Owen of all people."
s "Uuggh, this is terrible..."
m "Hey, there's nothing to worry about Sissel. Nothing's going to go wrong."
m "Even if you do fall in the water, you can just hang on to the kayak.{p=.1}Plus, we're all wearing life jackets anyway."
m "And if anything happens, I can be the one to perform mouth-to-mouth~"
hide sissel
show sissel neutral
s "Erh, you'd probably be into that."
s "J-just, stick close to me, ok?"
m "Like Elmer's glue."

scene lake water
with Dissolve(2.0)

stop music fadeout 2

"Everyone settles into their kayak as the race is about to begin."
"Sissel's sitting in front of me, fidgeting with his life jacket."
"The kayaks are pretty cramped, so I can feel the warmth of his back pressing against my chest..."
"I glance over and see Phillip and Owen struggling into their own boat."
"Owen's a big guy and takes up most of the space. Phillip's practically cradled between his legs."
"Owen looks pleased. Phillip's wearing a strained smile."

show sissel lifejacket
with dissolve

s "Well [charname], you ready?"
m "Not really."
s "Ugh, well aren't you reassuring."

hide sissel
with dissolve

"A whistle sounds in the distance."
c "Everyone get into position!{p=.1} May the best kayaker win! (And please avoid ramming into each other like last year. Insurance rates are going up)"
c "Starting in 3...{p=.1}2...{p=.1}1..."
c "BEGIN!"

play music "happy-music.mp3" fadein 2 fadeout 3

"The sounds of frantic paddling and splashing immediately surrounded us."
"Some boats immediately flip over while others veer off to random directions."
"One team forgot to untie their kayak from the dock and are paddling in place."
"Sissel and I and doing fairly well, paddling in sync."
"It turns out that kayaking really strains your arms though."

show sissel lifejacket
with dissolve

s "...Hey, this actually isn't too bad-"

show owen shorts
play sound "bump.mp3"
o "{size=+10}WAHOOO!!!!{/size}"
"Suddenly the water around us lurches and Owen speeds by."
"His paddles were a blur against the water as he swings them wildly with his big-ass arms."
"Phillip is resting his head against Owen's chest, fast asleep. Owen looks so proud."
hide owen with dissolve
show sissel lifejacket embarrassed

o "See you at the finish line, losers!"
s "That little shit-" 
show sissel lifejacket
s "[charname]! We have to win this!"
s "Paddle faster! We have to kick Owen's ass!"
m "I've got the wimpiest arms in existence though..."
s "{size=+10}DETERMINATION{/size}"
s "{size=+10}JUST DO IT{/size}"

if fight_dolores == "true": 
    hide sissel with dissolve
    play sound "ghost.mp3"
    show echo blurry with dissolve
    "I hear Echo laughing in the back of my mind."
    e "Need any help, lover boy?"
    m "Oh hush up."
    m "Wait, \"lover boy?\""
    e "It's so obvious [charname]. He liiiiiikes you~ <3"
    e "Are you trying to win him over by winning a race together?"
    e "That'd definitely show off your manliness."
    m "You got a wild imagination, dude."
    m "Winning sounds great right about now though.{p=.1}You got any ghostly voodoo tricks that can help us?"
    e "Ugh for the last time, I'm not a ghost!"
    e "But yes, I can help you impress your boyfriend."
    m "HE'S NOT MY-"
    show echo neutral with dissolve
    "Echo materializes next to our boat, gliding along the water's surface."
    "He winks at me with a knowing grin."
    e "Well, one impressed boyfriend coming right up! You owe me for this [charname]."

    play sound "echo-wish.wav"
    show echo wish smile with Dissolve(2.0)
    hide echo with dissolve

    play sound "water-splash.wav"
    play music "carefree-tune.mp3" fadein 2 fadeout 2
    "An abrupt yell echoes across the lake."
    "Huh?"
    "It looks like Owen and Phillip got stuck in some lake weeds."
    "Owen tries to untangle them with his paddle but ends up gracefully falling off the kayak and getting tangled himself."
    "Phillip sighs before diving off the boat to save him."

    show sissel lifejacket with dissolve

    s "C'mon [charname]! This is our chance!"
    "Our kayak glides past a spluttering and indignant Owen with ease."
    "Sissel made sure to flip Owen off as we passed by."

    scene lake
    with Dissolve(2.0)

    "With Owen out of the race, we managed to win by a mile."
    show sissel lifejacket with dissolve
    "As soon as our kayak touched the dock, Sissel leaped back on land ecstatically and shouts profanities at Owen from across the lake."
    s "HA, SUCK IT OWEN!"
    s "[charname], we did it! And I didn't die! This is great!"
    m "You're getting a bit too excite- Ooph!"
    "Sissel suddenly picks me off the ground in a big hug, a huge grin plastered across his face."
    "It was weird to see him so happy."
    "I could feel my face flush red. It's hard not to smile back."

    stop music fadeout 3
    play music "wave-piano.wav" fadein 2 fadeout 3
    scene black
    with Dissolve(2.0)

    scene lake
    with Dissolve(1.0)

    play sound "ghost.mp3"
    show echo blurry with dissolve

    "As the four of us trudged back to the docks, I could hear Echo laughing in the back of my mind."
    e "Congrats on seducing your boyfriend, [charname]~"
    m "W-what? He's not-"
    m "Gah, that's besides the point.
       How did you make Owen's boat get tangled earlier? I didn't know you had powers like that."
    e "I can't, technically.{p=.1}My powers don't work like that."
    m "What do you mean?"
    e "Eh, it's hard to explain."
    "Echo yawns and rubs his eyes."
    e "Wishes...we can twist circumstances and coincidences.{p=.1}The boat just {i}{b}happened{/b}{/i} to get tangled in that moment."
    e "It's a bit like yesterday, when you met that red-eyed girl."
    e "She made it so that you just {i}{b}happen{/b}{/i} to fall sick with a fever."

    m "So...it's kinda like you inflict people with bad luck?"
    e "Something like that."
    e "Most of the time we can't interfere directly, so we force something else to instead."
    e "I should warn you though, everything we do will have consequences.{p=.1}Next time you ask me to do something, think carefully first."
    m "Sounds good to me."

    e "Anyway, helping you seduce your boyfriend really tired me out."
    m "HE'S NOT-"
    e "I'll see myself out. You two play nice now~"
    e "Ta ta."
    play sound "ghost.mp3"
    hide echo with dissolve
    "Echo fades away before I can say another word to him."
    "What an asshole."

if fight_dolores == "false":
    "I half-heartedly paddle faster, but there's no way to catch up to Owen."
    "It's like asking a bar of soap to fight a medieval dragon. It's just ain't happening."

    "Hmm?"
    s "Um, is the kayak supposed to rock around this much?"
    m "The water does feel a bit rougher here."
    m "You feeling ok, Sissel? If you want, we can double back-"
    s "N-no! We're gonna win this!"
    m "Doesn't it feel like the water's getting higher though?"
    s "Just keep paddling, [charname]!"
    m "I thought you were afraid of water?"
    s "If I just pretend everything's not going to shit, it won't.{p=.1}Mind over matter, ok-?"

    play sound "water-splash.wav"
    hide sissel with dissolve
    stop music
    play music "carefree-tune.mp3" fadein 2 fadeout 2

    "Our kayak abruptly capsizes, throwing both of us spluttering into the water."
    "Sissel immediately held onto me with an iron grip."
    s "I'm gonna die, aren't I? This is it, I'm gonna drown and get eaten by the fishes and turn into fish shit-"
    m "Shhhhh, we're going to be fine. This is why we wear life jackets."
    m "Now stop clinging to me like a baby koala and help me flip the kayak back upright."
    s "That's not gonna do any good. There's a hole in the side of the boat. This thing ain't floating."
    m "What?"
    "Sure enough, there was a fist-sized rift in the kayak that slowly drank in the surrounding water."
    "It's sinking faster than our chances of winning this race."
    s "Do you think the school will leave without us?"
    s "We'll be stuck in the middle of the lake together until we rot and die."
    m "How romantic."
    s "Be serious, won't you?!"
    m "How can I be serious with you spewing melodramatic angst every other minute?"
    s "I'M PANICKING OK?!"
    s "And stop laughing at me! It's not funny!"
    "I stifle another giggle as I pet Sissel's head soothingly."
    "Hm?"
    m "Oh look, someone's coming to rescue us."

    show phillip shorts at farright with dissolve
    show owen shorts at farleft with dissolve
    "Sure enough, Phillip and Owen's kayak was paddling its way toward us, with Owen looking particularly reluctant."
    p "[charname]! Sissel! Are you two alright?"
    o "Oh geez, you guys are useless without us."
    s "You're full of shit Owen."
    o "Is that any way to treat someone who's coming to your rescue?"
    p "You were just saying how you wanted to leave them behind."
    o "W-well that's in the past! {p=.1}I'm too kindhearted to abandon these helpless ducklings."
    m "Ducklings?"
    p "Ignore him, [charname]. Here, take my hand. It might get a bit cramped here."
    o "Oh come on Phillip, we can't just let them on without some sort of payment~"
    o "How about you two give each of us a nice, hot bl-"
    p "{i}{b}Ignore him.{/b}{/i}"
    s "I can throw him overboard if you want."
    p "Please don't. He's the one doing most of the paddling."
    o "W-wah? Is that all I am to you Phillip? I thought we had so much together!"

    show owen shorts at farright with dissolve

    "Owen wails dramatically and wraps his arms around Phillip's waist as he helps us onto the kayak."
    p "So much except for personal space, apparently."

    scene black with Dissolve(1.0)
    scene lake water with Dissolve(1.5)

    stop music fadeout 3

    "Sissel and I were jammed tightly in the back of the kayak."
    "I sat in the very back, with Sissel cramped snuggly between me and Owen.{p=.1}His warm back was pressed tightly against my chest and between my calves."
    "The way the boat was rocking made Sissel's hips grind against my crotch rhythmically."
    "Shit, I can feel myself getting hard..."

    show sissel lifejacket embarrassed 
    with dissolve
    s "!!!!!"
    s ".....[charname]? What's poking me?"
    m "Uuh yeah um...sorry about that."
    s "........d-don't worry about it."
    hide sissel with dissolve

    "T-this was getting awkward."
    "Luckily, Phillip and Owen were too preoccupied with paddling to notice."


    play music "easy-lemon.mp3" fadein 3 fadeout 3

    show phillip shorts at farright with dissolve
    show owen shorts at farleft with dissolve
    show sissel lifejacket with dissolve

    p "Sigh...{p=.1}Well, it looks like we're too far behind in the race to actually win."
    o "Don't be so pessimistic! I'm sure we can make it if I paddle through at 100\% (and barrel through a few other teams)."
    p "The chances of that are as high as the chance of us actually kissing."
    o "Was that a challenge?!"
    o "That settles it, we HAVE TO WIN."
    o "You two back there! Put your back into it!"
    o "{size=+10}I HAVE TO WIN MY TRUE LOVE'S KISS{/size}"
    p "Hang on, I never actually promised-"

    hide owen with dissolve

    o "{size=+10}ONWARD!!{/size}"
    "Owen thrashes his paddle into the water wildly, thrusting the kayak forward at breakneck speed."
    "The force of it practically throws Sissel into me, pressing us close together."
    s "SLOW THE FUCK DOWN YOU'LL KILL US ALL"
    o "Haha, wimp!"
    "Hurtling rapidly toward shore, the kayak bashes into and throws several other teams aside. We almost flip over several times."

    play sound "bump.mp3"
    play sound "water-splash.wav"
    hide phillip with dissolve

    "As we approach shore, there was a loud {size=+5}\"WHACK!\"{/size} as Owen accidentally elbows Phillip in the face and throws him overboard."
    s "YOU DUMBASS"
    o "Ah-"
    play sound "water-splash.wav"
    "Owen dives headfirst into the water after Phillip with a panicked shout."
    o "Phillip hold on-!"
    p "Calm down, the water is like 2 feet deep here."
    o "O-oh."
    o "Listen, I'm really sorry! I didn't think-"
    p "Mm, you usually don't."
    p "......."
    p ".......wait."
    stop music fadeout 2
    play music "carefree-tune.mp3" fadein 2 fadeout 2
    p "You two!{p=.1} {size=+10}HURRY UP AND FINISH THE RACE WITHOUT US SO I DON'T HAVE TO KISS HIM!!{/size}"
    m "Aye aye, captain."
    s "Anything to piss off Owen."
    o "What? Wait don't-!"

    play sound "water-splash.wav"

    "Without another word, Sissel and I grab the paddles and thrash our way to shore, leaving Owen behind in our wake."

    scene lake
    with Dissolve(2.5)

    stop music fadeout 2
    play music "easy-lemon.mp3"

    c "Welcome back gentlemen! Congratulations on winning this year's race! (with no casualties)."
    show sissel shirtless with dissolve
    s "............................"
    s "That was the most traumatic experience of my life, [charname] why did you make me do this?"
    m "I think it went fairly well actually."
    s "Fucking twat. I'm going to need therapy after this."
    m "But did ya die?"
    "Sissel groans and punches me on the shoulder."

    show phillip shorts at farright with dissolve
    show owen shorts at farleft with dissolve
    "Behind us, Phillip was wading his way out of the water with Owen following closely behind."
    m "Oh hey! You're alive."
    p "Thanks to you two! Now I don't have to kiss Owen."
    p "I owe you both big time."
    o "Aaaw, I figured you'd be dying to kiss me Phillip~"
    p "Of course."
    o "R-really?"
    p "Yeah, I'd rather die first."
    o "A-ack! You really know how to kill a guy's self-esteem."
    p "You're welcome."




jump day3_activities


label day3_afternoon:
stop music
scene black with Dissolve(3.0)
play music "calm-guitar.mp3"

scene lake road with Dissolve(4.0)

"That was.......an interesting afternoon. {p=.3}My head was still spinning from the warmth bubbling against my chest."
"Mrs. Corlisse is allowing us some time to relax before heading back to the academy."
"It's probably for the best."
"Sissel is trying to stay far, far away from the water while Phillip and Owen were bickering somewhere."
"For now, I just want some time alone and take a peaceful walk through the forest~"

scene cottage
with Dissolve(5.0)
stop music fadeout 2
play music "blue-feather.mp3" fadein 2 fadeout 3

"Hm...?"
"I just kept wandering deeper into the forest, but I didn't expect to find a cottage all the way out here."
"It looks pretty worn down."
"I wonder who used to live here?"
play sound "halley-wish.mp3"
"....???"

play sound "ghost.mp3"
show echo wish with dissolve
e "{size=+10}MOVE!{/size}"
play sound "falling-tree.wav"

"There was a loud crash as a nearby tree falls down, missing me by inches."
"What...?"
play music "blue-feather.mp3" fadein 2 fadeout 2
play sound "ghost.mp3"

show halley wish at right with dissolve
show echo wish at left with dissolve
u "Hm, I missed."
u "Or did your wish block it?{p=.5}Not bad, for something so weak."
m "Wah-?{p=.1}You could have killed me!"
show halley neutral at right with dissolve
u "Just a light concussion actually. Don't be such a drama queen."
m "You just tried to smash me with a tree.{p=.1}Can you really blame me?"
e "That's besides the point.{p=.1}Who are you? Are you here for a fight?"
u "Me? A fight? Nah."
show halley smile with dissolve
u "I'm just here to kill some time until the 13th.{p=.1}Watching [charname] scream like a little baby's quite hilarious."
u "No hard feelings, of course."
m "You've got a few screws loose."
e "Sounds like a fight to me."
show halley neutral with dissolve
u "Not quite.{p=.1}Why would I fight you when the meteor shower is just two days away?"
u "That day's the pinnacle of your strength after all. {p=.1}I don't have a death wish."
show halley smile with dissolve
u "[charname] on the other hand..."
e "Shut up! {p=.1}{size=+10}SHUT UP!!!{/size}"
u "Too soon?"
u "...."
show halley neutral with dissolve
u "Anyway, to answer your previous question, I don't have a name."
$ u = Character("Halley", color="#cd7e99", what_color="#cd7e99")
u "I do vaguely remember someone calling me \"Halley\" at some point though."
m "\"Vaguely remember\"?"
u "Oh, you're a sharp one.{p=.5}Yes, my memories are a tatters as well. Just like you and that lanky wish of yours."
u "That's right Echo, {w=.5}your memory is in shreds too,{w=.2} isn't it?"
u "Stop pretending to be a guide when you know just as little as your wisher."
e "..............."
m "That doesn't answer why you keep trying to ruin me at every turn.{p=.1}Especially if you don't even remember anything."
u "True."
u "To be honest, I don't know why I hate you so much either."
show halley smile with dissolve
u "I just remember seeing you a few days ago and my heart went \"Wow, fuck this guy.\""
m "Geez, is it because I'm ugly?{p=.2}Why can't we all just be friends?"
u "Even if my memory's in tatters, I still remember bits and pieces."
show halley neutral with dissolve
u "All I know is this:{p=1}My wisher deserves the world.{p=1}And you took it from her."
u "That's all the reason I need to hate you."
e "Alright that's it. I'm taking her out."
show halley smile with dissolve
u "Oh?{p=.5}Don't you have any manners? {p=.5}{b}It's rude to fight on somebody else's grave.{/b}"
"Grave...?"
hide echo with dissolve
hide halley with dissolve
"I glanced at the cottage and felt the chills from earlier crawl down my back."
m "Who lives here...?"
"Huh?{p=1}.............{p}She's already gone."
show echo neutral with dissolve
e "...That bitch is crazy."
play sound "halley-wish.mp3"
e "!!!!!!"
show echo wish with dissolve
e "{size=+10}MOVE BACK!{/size}"
play sound "falling-tree.wav"
"There was a rumble as another nearby tree uprooted and nearly crashed into us again."
e "Ok, let's get out of here before she actually kills us."
m "Oof!"
hide echo with dissolve
"Echo grabs me by the wrist and forcefully hauls me down the forest trail."
"As the two of us quietly leave, I turn back and stare at the forest's lonely cottage."
"Just before it goes out of view, I think I heard a soft wail echoing through the woods.{p=.5}It sounded so sad...."
"Maybe it was just my imagination.....?"
"................"
"Whatever, {w=.2}we better get out of here."
play sound "ghost-song.mp3"
"???" "{w=.5}................."

scene black
with Dissolve(3.0)

stop music fadeout 3
play music "snowy-street.mp3" fadein 2 fadeout 2

scene dorm night
with Dissolve(2.0)

"The students returned to the academy without any incident."
"There were no classes today so most of us just crashed back in our dorms for the night."
"It's been a long and confusing day......"
"I'm pretty exhausted too, but I'm feeling up for a midnight snack before hitting the hay."

scene kitchen night
with Dissolve(2.0)

"Hm? Somebody's already here."

show owen grin
with dissolve

o "Yo [charname]! Grabbing a bite to eat?"
m "Yeah, just a quick snack before bed.
What are you doing...?"
show owen neutral with dissolve
"Now that I'm closer, I can see dirty kitchen utensils and scraps of food scattered everywhere."
"This place is looking worse than when Phillip blew up the toaster yesterday."
"...Sissel's going to flip his lid if he sees this."

m "So....why all the carnage?"

show owen scratch smile with dissolve

o "H-hey! It's not as bad as it looks."
m "...................."
show owen neutral with dissolve
o ".....Ok, I admit I might not be the best cook.{p=.1}But that doesn't mean I can't make something halfway decent!"
show owen grin closed with dissolve
o "I even made a bet on it with Sissel earlier.{p=.1}My honor is on the line [charname]!"
m "Smells like your honor's as good as dead."
show owen scratch smile with dissolve
o "Oh c'mon, you're supposed to be cheering me on."
m "Is the sauce pan supposed to be smoking?"
o "W-wah?"
stop music fadeout 2
hide owen with dissolve
o "{size=+10}EVERYTHING'S UNDER CONTROL{/size}"
"Owen dashes across the kitchen to salvage his blackened pasta."



show owen neutral with dissolve
o "...Ugh, I failed again."
m "You don't do this much, do you?"
o "W-well, I usually just go out to eat."
show owen scratch with dissolve
o "And Sissel used to cook for me before our little....fight? Spat?{p=.1}Whatever you wanna call it."
o "*Sigh* I miss the good old days.{p=.1}He used to actually smile at me instead of spearing me with eye lasers."
m "Hey, Sissel's a nice guy under all that yelling. I'm sure you two can make up if you keep working at it."
o "I dunno...I was a pretty big dick...."
play music "easy-lemon.mp3" fadein 2 fadeout 2
show owen grin closed with dissolve

o "...And I also have a pretty big dick-"
m "You know, for a moment I thought I could actually take you seriously."
show owen neutral with dissolve
o "Life's too short to be taken seriously dude. {p=.1}We're all going to be resting on a bed of flowers sooner or later."
o "Anyway, enough of this sentimental mush!{p=.1}I still gotta win my bet with Sissel! And now I have you as my taste-testing guinea pig."
m "Wha-?"
"I was about to retort when I noticed a figure outside the window."
hide owen
with dissolve
m "Speaking of Sissel..."
"Yup, that was him.{p=.1}He was walking rather briskly down the street as if trying to avoid being seen."
m "Why's he going out so late?{p=.1}He's heading toward the run-down side of town."
show owen neutral
with dissolve
o "Eh, Sissel sneaks out a lot. I'm sure he's got his reasons."
o "It's none of our business either way."
show owen grin closed with dissolve
o "Anyway, let's focus back on my pasta-making. You gotta help me out [charname]!"
hide owen 
with dissolve
"As Owen readies the stove again, the smell of burnt cheese fills the room."
"What have I gotten myself into? I just wanted a snack...."
"I was about to give Owen a hand but another figure passing by the door caught my attention."
stop music fadeout 2
show phillip tired smile
with dissolve
m "Oh hello Phillip. Why are you up so late?"
p "-hm? Oh you know, just the usual late-night studying on the roof."
"Phillip seems a little off today...{p=.5}His bag seems more full and heavy than usual too. As he walks into the kitchen, soft metallic clinks can be heard."
show phillip shrug tired with dissolve
p "I see Owen's dragged you into his pasta mess."
m "Any chance you can rescue me?"
p "You're going to have to pray to the pasta gods for that kind of help."
show owen neutral at right with dissolve
show phillip tired frown with dissolve
o "Phillip! Kiddo, how are you doing?{p=.1}You look dead tired."
show owen grin closed with dissolve
o "Hehe, need a little love to wake you up?"
"Owen scoots over to sling a flirty arm over Phillip's shoulder, but Phillip knocks it away."
show phillip tired frown at left with dissolve
show owen scratch with dissolve
p "Personal space."
show phillip tired smile with dissolve
p "Anyway, I have to get going. You two have fun."
p "Good luck [charname]!"
hide phillip with dissolve
stop music fadeout 2
"Hm? That's weird.{p=.1}The hall Phillip's taking doesn't lead to the roof..."
show owen scratch at center with dissolve
"As Phillip disappears, Owen lets out a long groan and slumps down on this chair."
o "................."
m "Hey Owen, you alright?"
o "Hm? Yeah, I'll be fine."
o ".......{p=.5}By the way, you don't have to stay here in my pasta hell."
o "Why don't you just grab your snack and head off to bed?"
play music "happy_lounge.mp3" fadein 2
m "Mm, actually, I don't mind helping you out."
m "Your honor's on the line after all."
show owen neutral with dissolve
o "....!"
show owen scratch smile with dissolve
o "Hehe...thanks [charname].{p=.5}You're probably the nicest person I've ever met."
m "Me? {p=.1}Geez, you've got pretty low standards-"
show owen grin closed with dissolve
o "Please marry me!"
m "-well that's pretty sudden. {p=.1}What's your net worth?"
show owen neutral with dissolve
o "W-wah?! I thought we could share our love together!"
m "I'm afraid I've got no love to give, buddy."
m "Anyway, let's get back to your pasta cooking. {p=.1}You've got a bet to win, don't you?"
show owen closed grin with dissolve
o "R-right!"

hide owen with Dissolve(2.0)
"The two of us spent the rest of the night burning pasta."
"In the end, we managed to make something edible, but just barely."
"It didn't seem to count as much of a success but......{w=.3}Owen seemed really happy."


scene black with Dissolve(4.0)
scene repeat_screen with Dissolve(1.0)
pause(1.5)

scene black with Dissolve(2.0)
show phillip tarot  at farleft with dissolve:
            xzoom .4 yzoom .4
show owen tarot  at rcenter with dissolve:
            xzoom .4 yzoom .4
show sissel tarot  at farright with dissolve:
            xzoom .4 yzoom .4

jump day4
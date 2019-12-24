##DAY 1
label start:
$ persistent.current_route = "default"
    
scene black with Dissolve(2.0)
scene clockwork with Dissolve(3.0)
   
"Hello again,{w=.3} friend. {p=.5}Welcome back to the beginning."
"Do you remember anything?{p=.5}The events that happened before,{w=.5} the tragedies that will {color=#45FFFF}repeat{/color} themselves?"
".........Oh.......I...........{p=.5}........I couldn't bring back your memories....{w=.3}{size=-7}....just like last time....{/size}"
"Don't worry!{p=.5}My memories are kind of shattered too."
"Things will be fine this time around though,{w=.3} I'm sure of it!"
"Just be yourself,{w=.3} and you'll do fine."
".........................."
"Well,{w=.3} it's time for us to depart."
"B-but before we go...{p=.5}Can I tell you something?{p}I've said this many times before,{w=.3} but I want to tell you again..."
"I.........{p=1}...........I'm sorry I couldn't save you."
    
stop music fadeout 2
scene black
with Dissolve(3.0)

"{b}Day 1{/b}:{p=.3}Begin Again"


play music "busy-city-street.mp3" fadein 2 fadeout 2


show skyline at Position(xpos = .5, xanchor="center", ypos= .85, yanchor="center") with Dissolve(3.0)
show skyline at Move((0.5, .85), (0.5, 0.11), 3,
      xanchor="center", yanchor="center") 


pause(2.0)
"Me" "So this is it, huh?"

scene school with Dissolve(3.0)
"The city noise echoes around me as I arrived to my destination."
"I've never been to this side of town before, {w=.3}but it looks like I'll have to get used to living here."
"This is Gerania Academy,{w=.3} a fancy school with a month-long summer program for gifted students."
"I'm going to be spending the next four weeks here, unfortunately."
"Ha, sounds like the opposite of a good time."
"I'd rather be back home sleeping my summer away if I'm being honest.{p=.3}But my parents wanted me out of the house."
"Geez, what a drag..."

"The weather's certainly agreeing with me.{p=.3}It looks as though it might rain any minute."

"I better hurry up and get inside.{p=.5}I doubt strolling in late would leave a good first impression." 

"As I approach the front doors, the air suddenly turns frigid."

scene black with dissolve
stop music

"???"
"What?"

play sound "ghost.mp3"
show echo blurry

"???" "...not that way....."

hide echo blurry
with Dissolve(3.0)

show school
with fade
play music "busy-city-street.mp3" fadein 2 fadeout 2

"A cold shiver rings down my spine. What the hell was that just now?"

play sound "beep.mp3"

"Wait, what?"

play sound "door.mp3"

"Oh crap, the door’s locked!{p=.5}What am I going to do? {w=.3}The teachers are going to rip me a new one if I’m actually late."

"I try slamming the doors to get someone’s attention, but nobody’s there to hear me.{p=.5}Damn! This day can’t get any worse."

show school rainy
stop music
play music "raining.mp3"
pause(1)
"{w=.3}.....................Well shit."
"I’m getting soaked!"
"I try banging on the glass again."

"Me" "Hello! Is anybody there?! Open the door!"

"???" "Um, hey there. {w=.3}Is everything ok?"

"Suddenly, a shadow passed over my head and the rain stopped pelting me."

show phillip neutral with Dissolve(2.0)

"A boy came up behind me nervously gripping an umbrella."
"He looked around my age, and very short. Another student maybe?"

"Me" "Uh, yeah I’m fine.{p=.3}But the door’s locked and nobody’s around. I think I’m missing the introduction orientation too."

"???" "What a coincidence,{w=.3} I got locked out from the side entrance too!{p=.2}{size=-10}W-well actually I kinda broke the door handle{/size}"
"???" "I think we’ll have a better chance getting inside if we tried the back entrance instead."
"???" "Wanna go together?"

"Me" "Sounds better than standing around clueless."
"Me" "Thanks man, you’re a real lifesaver."

p "I’m happy to help!{p=.3}The name’s Phillip by the way,{w=.2} what’s yours?"

$ charname = renpy.input("What is your name?")
$ charname = charname.strip("")

if not charname:
    $ charname = "Euca"

hide phillip neutral
show phillip smile shrug
with dissolve

p "\"[charname]\" huh? Weird name.{w=.3} You sound like a protagonist to a visual novel."

show phillip neutral with dissolve
p "Anywho,{w=.3} I'm kinda glad someone else is stuck in this miserable weather with me."
p "It's better than being miserable alone,{w=.3} at least."

m "Wow, thanks."
p "Well,{w=.3} let’s get going!"

"As we make our way around the building, I stick close under Phillip’s umbrella.{p=.3}I’m glad he’s around, otherwise I would have been soaked." 

"Awkward silence hung between us as we walked closely around the building."
"Phillip was fumbling with his umbrella, glancing at me periodically."

p "...Uh, by the way [charname], what subject are you studying here?"

m "What do you mean?"

p "You mean you forgot? Did you do all that paperwork while half-asleep or something?"

m "Uh well..."

hide phillip neutral
show phillip smile shrug
with dissolve

p "Hey, no worries! You’re not the only one. I pulled an all-nighter myself and finished it last minute eheh..."

"It sounds to me like he's only bringing this up because he couldn't think of anything else to talk about."

hide phillip smile shrug
show phillip neutral
with dissolve

p "It's a bit weird that we can only choose one subject to study here."
p "Maybe they go really in-depth?"
p "It'd be pretty interesting if you actually got into a subject you care about."

m "Oh, I remember something like this.{w=.2} I think I signed up for Photography or something…?"

"Wow, I really did finish that paperwork half asleep."
"Way to go [charname], procrastination hero for future generations."

p "Photography huh?{w=.3} That's a pretty interesting choice."

"I scratched my head awkwardly."
m "I'm pretty sure I only chose it because it sounded like an easy course."

p "Aw,{w=.3} there's no shame in being lazy!"
m "You don't have to say it quite like that..."
m "Though I'm happy to admit I'm a proud couch potato."
p "It's all about finding a good balance really."
show phillip smile shrug with dissolve
p "I've adopted the \"work harder until you drop!\" strategy myself!"

m "That....{w=.3} doesn't sound very healthy."
show phillip serious with dissolve
p ".....yeah,{w=.3} you're probably right."
show phillip neutral with dissolve
p "But work helps keep my mind busy and away from the {i}bad thoughts{/i},{w=.3} you know?"
show phillip smile shrug with dissolve
p "And what better way to deal with stress than keeping yourself busy?"

menu:
    "I dunno, maybe you should find a better way to cope.":
        $ encourage_phillip = "cope"
        m "Working your ass off doesn't really sound like a long-term solution."
        m "Won't you just burn yourself out and get more stressed?"
        m "People have limits,{w=.3} you know."
        
        show phillip serious with dissolve
        p "I don't know..."
        p "Sometimes when I stop,{w=.3} I feel like I'm just making excuses or giving up."
        p "And then I just end up more stressed."
        
        p "Well,{w=.3} what do you do to keep yourself running?"
        
        m "I kinda just eat snacks when I'm stressed.{w=.3} Like a lot of snacks."
        m "Chocolate is a real wonder food."
        
        play music "wacky.mp3" fadein 2
        
        show phillip no with dissolve
        p "Sugar is bad for you."
        m "Are you telling me you don't like {i}chocolate?{/i}"
        show phillip neutral with dissolve
        
        p "Well,{w=.3} I do eat a little bit of dark chocolate on occasions."
        p "Particularly the non-sweetened, bitter variety."
        
        m "I feel like this is a deep look into your psyche."
        p "Ahem.{w=.3} Chocolate preference is not a valid psychiatric evaluation method."
        
        m "I don't trust anyone who claims they don't like chocolate,{w=.3} cuz you know they're liars."
        show phillip smile shrug with dissolve
        p "Welp,{w=.3} I guess I should take my lying ass and {i}umbrella{/i} somewhere else."
        show phillip smile shrug at Move((0.5, 0.5), (-0.5, 0.5), 2.8,
                  xanchor="center", yanchor="center")
        p "Good luck in the rain on your own~!"
        
        m "W-wait!{w=.3} Come back!"
        m "I'm getting soaked out here-!"
        
    "I just take a nap.":
        $ encourage_phillip = "sleep"
        m "Sleeping your problems away is always an option!"
        p "Sleep?{w=.3} What's that?{w=.3} Never heard of it."
        
        m "Dude,{w=.3} maybe that's why you look so stressed and tired."
        m "Your body needs rest and all that good jazz."
        
        show phillip smile shrug with dissolve
        p "Me?{w=.3} Tired?"
        p "That's nonsense.{w=.3} I got an entire hour of sleep last night!"
        
        p "And I had like 3 cups of coffee this morning.{w=.3} I feel great."
        
        m "See,{w=.3} this is exactly what I'm talking about."
        m "You need sleep to live."
        
        show phillip serious with dissolve
        p "I get what you're saying...."
        p "But whenever I close my eyes,{w=.3} my brain wanders to some unpleasant places."
        p "And then I end up never falling asleep."
        
        show phillip neutral with dissolve
        p "I kinda envy you,{w=.3} to be honest."
        p "Napping whenever you'd like sounds great."
        
        play music "wacky.mp3" fadein 2
        m "Worse comes to worse,{w=.3} you can just have someone knock you out with a brick."
        
        show phillip no with dissolve
        p "That...{w=.3} doesn't sound like valid medical advice."
        show phillip smile shrug with dissolve
        p "Is that what you do?{w=.3} That explains the glum face you're always wearing-"
        
        m "Hey! {w=.3}I can fall asleep on my own just fine!"
        m "Anyway,{w=.3} let's hurry up and move.{w=.3} I'm getting soaked."


scene school back rainy with Dissolve(3.0)
play music "raining.mp3" fadein 2 fadeout 2
show phillip neutral with dissolve


"After a short walk,{w=.3} the two of us arrived at the school's back entrance."
p "Oh look, I think there's someone already here."
"I glance out from under Phillip's umbrella."
"There was some weird guy struggling to climb up the side of the building's walls."
m "A burglar?"
show phillip no with dissolve
p "No,{w=.3} I think it's a student."
p "If he's a burglar,{w=.3} he's a pretty bad one."


"As we approached, the weird guy spotted us and grinned before taking a great acrobatic leap and landed in front of us."
p "Ah-!"
play music "batty.mp3" fadein 2 fadeout 2
play sound "slam.wav"
hide phillip
show school back rainy at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)

"And then promptly slipped and toppled onto Phillip."
show owen neutral at right with dissolve
show phillip frown at left with dissolve

"???" "Whoops,{w=.3} sorry there kiddo!{w=.3} Are you alright?"
show phillip shrug smile with dissolve
p "I'm still in one piece, I think."
show owen grin 3 with dissolve
"???" "That's a relief!{p=.3}Were you cuties locked out too?"
m "\"Cuties?\""
show phillip annoyed with dissolve
p "Amazing. {p=.3}He's flirting horribly and he hasn't even introduced himself yet."

show owen_rainbow1 with Dissolve(1.0)
pause(1)
o "Hey now,{w=.3} I was just trying to make you all feel welcome!"
o "Anyway, the name's Owen.{p=.3}Owen Lorelei."
o "I'm a student at Gerania, just like you guys."

show owen_rainbow2 with Dissolve(2.0)
pause(1)
o "Pleasure to meet you~{w=.3} It's always nice to meet a bunch of new folks!"
o "Are you guys from around here?{w=.3} I'd be happy to show you guys around for a good time~"

pause(1)
stop music fadeout 5
show rainbow_stare1 with Dissolve(2.0)
pause(2)

p "..............................................."
m "......................................................................."


m "He's very.......{w=.3}colorful,{w=.3} isn't he?"
p "......................I'm leaving."

play music "wacky.mp3" fadein 3

play sound "surprise.mp3"
show rainbow_stare2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)

m "Wait!{w=.3} Don't go!"
m "I still need your umbrella!"


o "H-hey now,{w=.3} what about me?"
o "Don't just ignore a guy when he's trying to open up to you!"

p "I'd prefer it if you keep it closed,{w=.3} thanks."
o "O-ow."
o "Let it be known that you've murdered the great Owen Lorelei's self-esteem within 10 seconds of meeting him."
p "Tragic."

hide owen_rainbow1
hide owen_rainbow2
hide rainbow_stare1
hide rainbow_stare2 with Dissolve(2.0)

"Phillip suddenly glanced back at the other guy with a frown."
show phillip serious with dissolve
p "Lorelei?"
p "As in that one really shady and rich family?{w=.3} The one that practically owns the school and half the city?"
show owen grin nervous with dissolve
o "Y-yeah, that one."
"Owen mumbles under his breath. He looks a bit uncomfortable."
show phillip neutral with dissolve
p "Hm........"
p "Well,{w=.3} it's nice(?) to meet you I guess."
p "My name's Phillip Tan."
show owen grin 2 with dissolve
o "Phillip Tan?"
o "Hey! We're roommates!"

show phillip frown with dissolve
"Phillip's smile immediately dropped like lead."
p "What?{w=.3} How do you know?"
show owen grin 3 with dissolve
o "I've lived at this academy for like 7 years.{p=.3}'Course I'd have some insider information hehe~"
o "Lookin' forward to it, kiddo!"
p "R-right,{w=.3} likewise."
"Owen turned to me with a wide grin.{w=.3} This guy seems a bit too excited."
o "And what's your name, handsome?"
m "Er, I'm [charname]."
m "A-anyway,{w=.3} why were you trying to climb the building?"

o "Right to the point huh?"
o "Well, the door was locked so I tried to reach the window and climb inside from there!"
m "Uh...."

show phillip annoyed with dissolve
p "Or maybe{w=.5} we could just wait until someone passes by to open the door for us?"
show phillip annoyed look with dissolve
p "You know,{w=.3} like normal people."
o "I already waited like forever though.{w=.3} It'll take an eternity!"

show phillip frown with dissolve
p "Waiting sounds safer than climbing windows."
o "It's not that hard, really!{w=.3} I used to climb these windows all the time!"
o "There's a little ledge over there that we can use and it'll be super quick."
show phillip shrug smile with dissolve
p "Eh, you'll probably break the window and be in a world of \"pane.\""
show phillip neutral with dissolve
show owen grin 2 with dissolve
o "Look here buddy, I'm too suave and handsome to break anything but expectations in bed."
m "In the bad way?"
p "Probably."

show owen grin 3 with dissolve
o "Only ever in the good way!{p=.3}Wanna find out first-hand?"
"Owen leans in close to me and gives me a wink."
m "Um...."
"Phillip coughed behind us."
show phillip no with dissolve
p "Let's find a way inside the building."
p "I mean,{w=.3} you two can have your bedroom experience out here,{w=.3} but I won't help you when you get arrested for public indecency."
m "W-we weren't!"
show owen neutral with dissolve
o "Heh,{w=.3} guess we'll have to save it for later."

show phillip annoyed look with dissolve
"The way Phillip's eyes rolled into the back of his head reminded me of a great white shark going in for the kill."
show phillip neutral with dissolve
p "Anyway [charname],{w=.3} what do you think we should do?"

menu:
    "Climb the window":
        $ entrance = "window"
        play music "raining.mp3" fadein 2 fadeout 2
        show phillip frown with dissolve
        m "Well, waiting here will take forever.{p=.3}This is the back entrance after all."
        m "Climbing the window doesn't {i}look{/i} too difficult either-"
        o "Window climbing it is!"
        o "Hehe I knew you'd be reasonable, [charname]!"
        m "Hey Phillip, are you coming along too?"
        p "I guess so..."
        o "Enough dilly-dallying, we're all late as it is. Let's get going!"
        
        
        hide owen with dissolve
        hide phillip with dissolve
        
        "The three of us hobbled onto the ledge that Owen was climbing earlier and inched our way towards the window."
        "Now that I'm up here,{w=.3} this feels like a really bad idea."
        
        "The rain made every surface wet and slick."
        "I feel like any wrong move and I'll end up slipping and bashing my head on the pavement."
        "Phillip, on the other hand,{w=.3} walked alongside us with the casual grace of a cat."
        "He glanced at us occasionally with slight concern."
        p "Are you doing okay [charname]? {w=.3}You look kinda pale."
        m "I-I mean,{w=.3} we are a little high up-"
        
        "There was a sudden {i}click!{/i} as Owen swung opened the window with a wide grin."
        o "See? Way easier than waiting outside for eternity. {p=.3}Let's go-!"
        "Owen leapt into the window headfirst.{p}He leap was immediately followed by a {size=+10}{i}CRACK{/i}{/size} and a resounding \"Ow!\""
        m "Are you still alive in there?"
        o "Yeah! Perfectly fine, nothing went wrong!"
        p "Except that he broke the window lock. This thing isn't closing anytime soon."
        m "Well at least now we can get out of this rain."
    "Wait outside":
        $ entrance = "door"
        m "Eh, I'm not sure I want to try climbing a building when it's raining out."
        m "We'd probably slip and end up hugging the ground."
        show owen grin nervous with dissolve
        o "Aw you're all a bunch of killjoys.{p=.3}Opportunities to climb windows don't come up everyday you know."
        p "Hey, better safe than sorry after all."
        show phillip shrug smile with dissolve
        p "....I guess you could say we're missing{w=.3} a {i}window of opportunity?{/i}"
        "I groaned and buried my face in my hands."
        show owen scratch with dissolve
        o "Geez, and you think my flirting was bad."
        m "I'd take your flirting over bad puns any day."
        show phillip neutral with dissolve
        p "Don't be mean, that was a good one!"
        m "If you say so."
        show owen neutral with dissolve
        o "Keep dreaming kiddo. You're losing this war."
        m "And all of our respect."
        o "For making us wait outside for all eternity."
        p "Oh geez, you're all so high maintenance."
        show phillip shrug smile with dissolve
        p "Weeelllll, I suppose I {i}could{/i} make this easier and just pick the lock."
        show owen grin
        o "Whoa, you know how to pick locks? That's sick!"
        o "Where did you learn this kinda stuff?"
        show phillip neutral with dissolve
        p "I can't go revealing all of my secrets."
        p "Anyway,{w=.3} give me a few minutes.{w=.3} Lock-picking takes a while."
        show owen neutral
        hide phillip with dissolve
        play music "raining.mp3" fadein 2 fadeout 2
        "Phillip crouches down in front of the door and pulls out some hairpins and tweezers."
        "From the way he's picking at it, you'd think he's done this before."
        
        o "Heh, nice view back here."
        "Phillip just rolled his eyes and continued picking the lock."
        m "Are you always this...{w=.3}flirty?"
        show owen grin closed
        o "Oh are you jealous? Don't worry dude, your type turns me on too-"
        show owen neutral
        "{size=+10}{i}SNAP!{/i}{/size}"
        p "Whoops~"
        p "Well the good news is that I unlocked it.{p=.3}Bad new is that I kinda broke the lock."
        p "This thing ain't staying closed anytime soon."
        m "At least now we can get inside and out from this rain."
            
        
stop music fadeout 2
scene school lobby with Dissolve(3.0)

show phillip neutral at right with dissolve
show owen neutral at left with dissolve

"As the three of us shook the rain from our hair, I glanced around the lobby."
"This school is fancier than I expected.{p=.1}I wonder where we're supposed to go from here?"
o "Mm, the orientation is probably over by now. I think we should probably find a teacher-"
show phillip frown 
play music "seven-off.mp3" fadein 2 fadeout 2
"???" "{size=+10}HEY YOU BRATS!{/size}"
"A large ugly rat hobbles towards us, his face scrunched up in hostility.{p=.1}He looked like the type of guy that constantly started bar fights."
"???" "What do you miscreants think you're doing, entering the building like a bunch of criminals?"
show owen grin nervous with dissolve
o "Oh, hello there Dorcas."
d "That's {i}Mr. Dolores{/i} to you, brat."
o "If you say so."

"The man (I think he's a teacher?) turns towards me and Phillip with an upturned nose."
d "Ah, and you're [charname] and Phillip, I take it?{p=.3}The two that missed the orientation?"
m "Y-yes?{p=.3}Owen was with us too-"
d "Who would have thought Gerania Academy's new students would be snooping in here this way?{p=.3}Guess I shouldn't be surprised-"
show owen neutral
o "Actually, all the entrances were locked and we were stuck in the rain.{p=.3}A system glitch, I guess?"
o "It'd be great if you'd stop yelling at them for something they couldn't help."
"Mr. Dolores huffed and shook his head."
d "Whatever. At least you folks weren't like that other kid that didn't even show up."
d "Here, take your student ID cards and unpack at your dorms. {p=.3}And Owen, make yourself useful and be a tour guide or something."
"Mr. Dolores tossed the ID cards at us and stomped away."
play music "wave-piano.wav" fadein 2 fadeout 2
p "Wow...{w=.3}That guy was...."
m "A douche?"
show owen grin nervous with dissolve
o "Eheh, sorry about the first impression, guys. {p=.3}This is a good school, really."
o "Dolores is just a jackass."
"I heaved a tired sigh. It hasn't even been an hour and this school's already been a crazy experience."
"Shaking my head, I glanced at my ID card."
show euca card with dissolve
"Ugh, I probably shouldn't have sent in a selfie as my ID photo.{p=.3}What was I thinking?"
hide euca card with dissolve
m "By the way Owen, could you show us where our dorms are?"


show owen grin 3 with dissolve
o "Of course!{p=.3}And Phillip and I can get some \"roommate bonding\" time too~"
show phillip annoyed with dissolve
p "What?"
show owen neutral at center with dissolve
o "C'mon buddy, it'll be a good chance to get to know each other!"
"Owen goes to put a friendly arm around Phillip, but the little guy instantly stiffens."
show phillip shrug smile with dissolve
p "Oh!{w=.3} I just remembered that I forgot something.{w=.3} I better go leave and get it!"
o "What did you forget?"
p "Uh....{w=.3}I forgot!"
p "Welp,{w=.3} time for me to leave."

show phillip annoyed look at Move((0.6, 0.5), (-0.5, 0.5), 2.8,
                  xanchor="center", yanchor="center")
p "I'll see you guys around!{p=.3}{size=-15}...I hope the fuck not-{/size}"

"As Phillip strolls away, Owen stares at his retreating back, deep in thought."

"Suddenly, I yelp as Owen elbows me playfully."

o "Heh, what a cute guy. Is he single?"

m "Dude, we just met. I don't know a thing about him."
"(Please don't ask him out.{w=.3} Phillip looked like he might snap.)"

o "Oh bummer. Whatever, I'm sure we'll get to know each other {i}real{/i} well after a while."
o "Well anyway, I better show you the way to your dorm."

m "By the way, why are you the one showing us around? You don't exactly look like a tour guide."

show owen grin nervous with dissolve

o "Mmmm..."

"Owen starts walking down the hall briskly."
"I struggle to keep up with his strides."

o "It's a long story to be honest..."
o "I've been living at this academy for like....{w=.3} 7 years?"
show owen neutral with dissolve
o "Needless to say,{w=.3} I'm pretty familiar with how things work around here,{w=.3} so I run errands for teachers pretty often."
m "7 years?!{w=.3} Why were you at the academy for so long?"

show owen grin nervous with dissolve
o "{size=-5}Oooooh boy,{w=.3} how do I explain this without making it super awkward or TMI?{/size}"
o "Well uh....{w=.3} I kinda ran away from home when I was little."
o "Family trouble and whatnot."

show owen neutral with dissolve
o "So now I'm here!"
o "Any questions of the academy variety?"

menu:
    "Are you doing okay?":
        
        play music "somber.mp3" fadein 3
        m "That sounds....{w=.3} kinda rough."
        m "Are you doing okay?"
        
        "Owen waved his hand dismissively."
        
        show owen grin nervous with dissolve
        o "Me?{w=.3} Oh I'm perfectly fine!"
        o "That stuff happened like forever ago.{w=.3} I don't even think about it nowadays."
        
        show owen grin 3 with dissolve
        o "Nothing but happy thoughts here!"
        
        show owen neutral with dissolve
        o "Sorry to weigh down your first day with all this heavy stuff."
        
        "I glanced at Owen doubtfully."
        "There's a stark difference between his fake smiles and his genuine ones..."
    "*Stay quiet*":
        play music "meloncholy.mp3" fadein 3
        "I stayed quiet for several moments."
        "How do you even respond to something like that?"
        "\"I'm sorry for your loss?\"{p=.3}\"Do you like living at the academy?\""
        "Everything in my head felt too stupid to say out loud."
        
        "Owen must have taken my silence for something else because he let out an uncomfortable laugh and walked faster."
        show owen grin nervous with dissolve
        o "Eh,{w=.3} that must of been weird to hear out of the blue."
        o "Sorry if I made things awkward and stuff-"
        
        m "N-no,{w=.3} that's not what I'm thinking at all!"
        m "I mean,{w=.3} I'm the one who asked in the first place."
        
        "I glanced up and gave Owen an awkward smile."
        m "You're still a big ol' weirdo regardless,{w=.3} but I'm glad to have met you here."
        m "Hope you're holding up okay."
        
        show owen neutral with dissolve
        "There was a stark difference between Owen's forced smiles and his genuine smiles."
        
        o "Thanks [charname]."
        o "You know,{w=.3} you're a pretty swell guy.{w=.3} I like it."
        
        "I feigned a dramatic look of shock."
        m "What's this?"
        m "Actual compliments instead of bad pickup lines?"
        m "Keep this up and I might actually grow interested in your flirting,{w=.3} Owen."
        
        "Owen flushed a little before grinning good-naturedly."
        show owen grin 2 with dissolve
        o "What?{w=.3} You mean you weren't interested already?"
        
        show owen grin 3 with dissolve
        
            

show owen neutral with dissolve
o "Anyway, let's head off to the dorms. Introductory classes are going to start soon."
m "Let's go then."
o "Just try and keep up. The dorm building is right..."



scene dorm
show owen neutral
with Dissolve(3.0)

play music "happy_lounge.mp3" fadein 1 fadeout 2

o "...right here!" 
o "There were an odd number of students this year, so you get a room all to yourself! Lucky guy you are."

m "My own room? Sweet."

o "Well, you better get unpacked quickly,{w=.3} classes start in about 10 minutes."
o "I've got to go myself, so see ya around kiddo."

hide owen neutral with dissolve
pause(1.0)

"I down my bags and sink into the bed, sighing at the comfort."
"So this is where I'll be living for the next month huh?{w=.3} And also learning photography, apparently."
"I hope the people around here don't turn out to be complete weirdos."
"That Phillip kid seems nice enough. He's kinda doofy though; he always looks like he's lost or something."
"Owen is a little too flirty, but whatever. Things could be worse."

"The school seems a little preppy and upper class too. I really don't fit in around here, do I?"
"Not that I fit in at home either..."
"As I sit alone in my room,{w=.3} I could feel my mind wander into uncomfortable places."
"Come to think of it,{w=.3} surrounding myself with other people did a pretty good job of drowning out that sinking feeling in my chest..."
"Well, sitting here contemplating it isn't going to help."
"Better head off to good ol' photography class now."
"I leap off the bed and stretch my arms over my head with a huge sigh."
"Here goes nothing!"


#CHAPTER 1 INTRO PART 2

scene hallway
with fade
play music "snowy-street.mp3" fadein 2 fadeout 2

"Well, according to this pamphlet, Photography class should be somewhere around here."
"This school is like a maze, geez. I hope I'm not late again."

play sound "bump.mp3"

"...Huh? There's something on the floor."
"Looks like someone dropped their wallet."
"...."
"So his name is Sissel? He's probably another student around here."
"I'll hold on to it for safekeeping, I guess."

scene art room
with fade

"The Photography classroom is heavy with the smell of fresh paint."
"It looks like they share a room with the rest of the art students."
"This place is rustling with activity."

"???" "You there."
"???" "Do you happen to be [charname]?"

m "Uh, yes ma'am!"

c "I am Mrs. Corlisse, your Photography teacher for this month. Welcome."
c "Before class starts, I have to make sure all students have possession of their own personal camera."
c "Did you bring one as assigned by the class paperwork,{w=.3} Mr. [charname]?"

m "!!?!!?!"
m "We were supposed to bring our own camera?"

c "You mean to say you don't know?"
c "Did you bother reading the paperwork before coming here,{w=.3} Mr. [charname]?"

m "Uuuuhhhh..."
"Shit, great first impression already."

c "No matter, we have several spares for...less attentive students such as you."

"Do you hear something breaking?{p}Oh wait, it's just my self-esteem. No big deal."

"Mrs. Corlisse rummages through several cabinets before pulling out an old, faded camera."
c "Hm, this will do."
c "Take this, Mr. [charname]. I expect you to take good care of it."

"It feels pretty old and clunky."
"Heck, this thing's probably older than I am."

play sound "ghost.mp3"
stop music
"Student" "H-hey, isn't that the-?"
"Other Student" "Yeah, that's the one alright..."
"Yet another Student" "That thing's cursed! What's Mrs. Corlisse thinking, giving that haunted thing to him?"

c "Nonsense! I will not have any of this \"haunted\" talk in this classroom."
c "That story is just a baseless rumor floating about the school."

m "Cursed? What's that supposed to mean?"

"Student" "Uh, don't worry about it. You'll be fine."
"Another Student" "Y-yeah!"

"Mrs. Corlisse scowls and ignores everyone."
"She starts lecturing on the basics of photography, and the class settles down and starts taking notes."
"Everyone keeps giving me weird looks though."
"What's all this commotion over this old thing?"

show echo neutral
with dissolve
play sound "ghost.mp3"

"???" "Hey, it's not {i}{b}that{/b}{/i} old."

m "{size=+20}AAAAAAAAAAAAAAAHHH!!{/size}"

hide echo neutral 
with dissolve

c "Mr. [charname]! Keep your voice down!"

m "S-sorry!"
m "T-t-this kid just popped out of nowhere."

"The class suddenly begins whispering rampantly."
"Student" "See? It's got him!"
"Another Student" "I knew that thing was haunted!"
"Yet Another Student" "It's the ghost, isn't it?"
"Student" "Do you see him?"

c "........."
c "...Mr. [charname],{p}Let me explain something to you."
c "I will not have any more of this supernatural trash in this classroom."

m "W-what?"

c "Countless other students have tried pulling the same trick you have."
c "There is no ghost child haunting that camera."
c "If I hear another word of this, expect disciplinary action for disturbing my class."
c "Understand?"

m "W-wha-?"

show echo neutral
with dissolve

"???" "It's probably best just to agree with her, [charname]."

m "Huh?"
m "Uuh, yes ma'am."

c "Good, now sit down and take your notes."

"I settle back down at my desk and glare at the kid."
"What the hell is going on?"

play music "wave-piano.wav" fadein 2 fadeout 2

"???" "Sorry [charname], I probably shouldn't have startled you."
"???" "Especially with ol' Corlisse around."
m "Who the hell are you, and why can't anyone else see you?"
m "A-are you really a ghost?"
"???" "Me? Hmm..."
e "You can call me Echo. And no, I'm not a ghost. Nothing sad like that."
e "I guess you can call me a \"wish\"."
m "...That makes no sense. And your face..."


e "Oh, you finally noticed?"
m "You look just like...{p}...me?"
e "Nah, I'm much more handsome thank you very much."
m "Not to mention humble."
m "Why do you look like me? And why are you {i}here?{/i}"

e "...I can't answer those questions at the moment."
m "...Great."
m "Wait, aren't you the one who locked the front doors this morning?"
e "Oh, you're a sharp one."
m "Why did you have to do that?!{p}You made me miss the orientation and late for everything!"
m "Not to mention stranding me outside in the rain."

e "If I didn't lock those doors, would you have met Phillip, or Owen?"
m "W-well..."
e "And if I haven't stolen Sissel's wallet, you wouldn't have met him either."

m "...uh, we haven't met yet, actually."
e "Really? What's taking you so long?"
e "No matter, you'll bump into him sooner or later."

"Why is he smirking like that?"

play sound "ghost.mp3"
hide echo neutral
with dissolve
show echo blurry
e "....!!"


e "Looks like I'm out of time."
e "I'll see you around, [charname]...{p}...Don't lose that camera..."

hide echo blurry
with dissolve
"...he's gone."
"..."
m "...He may be a ghost,{p}but I really want to kick his ass."

"I sighed and glanced down at the camera in my hands."
"A few moments of silence go by before I reluctantly hang the camera around my neck."
"Ghosts and cameras,{p}What could ever go wrong?"

scene hallway
with fade
play music "snowy-street.mp3"

"Photography class ended not a moment too soon. Everyone rushed to get out of that dreaded place."
"The other students keep their distance from me. Probably still wary of that whole \"cursed\" situation."

"My first day at this academy is off to a greaaaat start."
"I yawn and fumble through my schedule tiredly. Huh?"
"Looks like it's lunchtime already!{p}I can almost smell that sweet, sweet freedom."

play sound "bump.mp3"

m "Ow!"

"???" "Watch it, dipshit!"

show sissel neutral
with dissolve

m "O-oh, sorry!"

"???" "You better be."
"???" "{i}*grumble*{/i}."

"Wow, rude."
"The kid ignores me and struts down the hall with contempt."
hide sissel neutral
with dissolve

"He looks like the kind of guy who has \"angry\" as his default state of mind."
"He seems a bit familiar though. Where have I seen him before...?"
"Oh! It's the kid on the wallet!"
"His name is Sissel, I think."
"I reach for it in my pocket but hesitate slightly."
"Should I even bother giving it to him? He's acting like a jackass."

menu:
    "Give him the wallet.":
        "I sigh and pull it out of my pocket."
        "Jackass or not, it's still his wallet."
        m "Hey! Is this yours?"
        
        show sissel neutral
        with dissolve
        
        s "Huh? Oh, my wallet!"
        
        show sissel indignant with dissolve
        "His ears droop in embarrassment as he walks back to grab it from me."
        
        s "Uh...thanks kid."
        
        hide sissel with dissolve
        
        "He rushes back down the hall like he's in a big hurry."
        "Not much of a talker, is he?"
        "Oh wait, he's coming back."
        
        show sissel embarrassed
        with dissolve
        
        s "U-um, uh..."
        s "Sorry for calling you a dipshit earlier."
        s "It's been a bad day." 
        
        m "It's fine, don't worry about it."
        
        s "If you say so..."
        s "Um, well...See you around then."
        
        "Sissel makes his way down the hall again."
        hide sissel embarrassed
        with dissolve
        
        "His ears were still drooping. It's quite adorable."
        "I couldn't help but giggle at his antics."
        "For someone who looks so tough, he sure blushes a lot."
        
        show echo blurry
        with dissolve
        
        e "Well [charname], you really saved him a lot of trouble."
        m "GAH!"
        m "Your voice! Get out of my head!"
        e "Nah, it's nice in here. Very empty and cozy~"
        m "You little shit."
        e "...Did you know? Sissel's the poorest student here at Gerania Academy."
        e "Returning his wallet probably meant a lot to him."
        
        m "...so why did you steal his wallet from him in the first place?"
        e "You'll see, little man."
        m "We're the same exact height-"
        hide echo blurry 
        with dissolve
    "Keep the wallet.":
        $ steal_wallet = "true"
        show sissel neutral with dissolve
        "I retract my hand from my pocket, but not before Sissel saw me."
        
        s "What was that?"
        m "W-what are you talking about?"
        
        "If looks could kill, I'd turn into a shriveled sausage before I hit the ground."
        
        show sissel annoyed with dissolve
        s "What is that in your pocket?!"
        m "It's n-nothing!"
        m "Hey! Don't grab-"
        
        "Sissel leapt at me and shoved his hands inside my pockets."
        "I squirmed in his grip but he managed to get the wallet out. Damn it!"
        
        s "What the hell were you doing with my wallet?"
        m "I-I found it on the floor earlier. I {i}was{/i} going to bring it back!"
        s "Oh shut your trap."
        
        "He did not look impressed."
        "Sissel gave me a rough shove before stomping back down the hall."
        
        hide sissel with dissolve
        "I could almost see the steam pouring out of his ears."
        
        "..."
        "..."
        "Well shit."
        
        show echo blurry
        with dissolve
        
        e "You certainly made a good first impression."
        "Gah, this voice inside my head!"
        m "Shut it! You would have done the same thing! It was a free wallet!"
        e "A free wallet with no money in it?"
        e "The one that you stole from the poorest kid in the school?"
        m "W-what? I didn't-"
        m "You're the one who took his wallet in the first place!"
        e "And you're the one who decided to keep it."
        
        m "Well you know what? You're  a lousy, no good-"
        hide echo blurry
        with dissolve
        
    
play sound "bump.mp3"
p "Oh hey! [charname]! Nice to see you again!"
show phillip neutral
with dissolve

"I jump as Phillip suddenly appears behind me."

p "Want to go to lunch together?{w=.3} I kinda want to stick with people I know..."
"I gave Phillip a friendly smile."
m "Sounds good. I could do with a relaxing lunch."
m "Let's head off to the cafeteria."

p "Actually, I was thinking of going to this local cafe!"
p "A friend of mine recommended it to me.{w=.3} I heard it's really nice and cozy."
p "Plus, Owen kinda gave me an errand to do there."

m "I have no idea where I'm going so you'll have to lead the way."
p "That's a great idea!{p}Let's get lost together!"

play music "cafe-music.mp3" fadein 2 fadeout 2
scene cafe front
with fade


"The cafe was filled with soft rustling of activity."
"The warm smell of coffee and breakfast fills the air."
"It really is nice and cozy in here."

p "Well, we're here!"
p "And we only got lost twice. Thank god for Google Maps."

m "I {i}{b}told{/b}{/i} you we should have stopped and asked for directions."

p "That's the same as giving up."
p "Don't you have any sense of pride [charname]?"

m "Right now, I only care about getting decent food."
p "Haha, I guess we're both pretty hungry."
p "What are you planning on getting?"

show sissel neutral uniform
with dissolve

s "Hello, welcome to Cafe du Coeur. What can I get for-"
s "-Oh!"

if steal_wallet == "true":
    s "It's the wallet-stealing jackass again."
    m "Gah!"
    s "What do you want?"
    s "Hurry up and order, and get out."
    
    m "L-look, I'm sorry I took your wallet earlier."
    m "I really didn't mean to."
    
    s "Excuses."
    s "There wasn't any money in it. I really didn't see why you wanted to steal it."
    s "Besides, you know,{w=.3} being a jackass."
    
    hide sissel neutral uniform
    with dissolve
    show sissel neutral uniform at right 
    with dissolve
    show phillip neutral at left
    with dissolve
    
    p "Um.....{w=.3}Maybe this is all just a misunderstanding?"
    s "-!!!!{p=.3}It's you....."
    p "Huh?"
    p "Oh hey!{w=.3}You're that kid-!"
    s "And you're that cat that's always hanging around that wishing well."
    
    "I glanced between the two of them, {w=.3}slightly bewildered."
    "Did they know each other?"
    
    s "........"
    s "...[charname]."
    
    m "Y-yeah?"
    s "How did a dickwad like you end up with a friend like him?"
    
    "Phillip glanced between the two of use awkwardly and shrugged."
    p "He's been pretty okay so far.{w=.3} Give the guy a chance!"
    
    s "Hmph,{w=.3} I'll have to take your word for it."
    s "But I'll be watching you, [charname]."
    
    p "Oh uh, before I forget,{p}Owen wanted me to give this to you."
    "Phillip handed Sissel a shiny ID card, identical to the ones we received earlier."
    "There was a note attached to it as well."
    "Sissel rolled his eyes at the sight of Owen's name."
    "He glanced up and stared me up and down,{w=.3} as if he was mentally judging me."
    
    s "You know Owen too?{w=.3} You sure surrounded yourself with a weird bunch."
    
    
    m "H-huh?{w=.3} We're not friends, exactly..."
    s "At this point, I don't really care."
    s "Now hurry the fuck up and order your food."
    
    "Despite the aggressive tone,{w=.3} he sounded slightly less hostile this time around..."
    
    scene cafe back
    with fade
    
    "Phillip and I quickly ordered our food and sat down."
    "Far far away from the cash register. I can still feel Sissel glaring down my back."
    
    show phillip neutral
    with dissolve
    m "Eh, thanks for backing me up Phillip."
    p "No problem I guess? I didn't really do much."
    p "But [charname], you really shouldn't take other people's stuff..."
    m "Got it. No more stealing, pinky promise."
    p "Haha, I'll hold you to that."
    show phillip frown with dissolve
    m "By the way,{w=.3} have you met Sissel before?"
    p "Sort of? {p=.3}I've met him a few times by Bradley Lake when I was little."
    p "We talked a little, I never learned his name until now though."
    
    play sound "ghost.mp3"
    hide phillip
    with dissolve
    show echo blurry
    with dissolve
    
    m "Oh great, what do you want?"
    e "Nothing..."
    e "Just wanted to let you know that Sissel charged you extra for that coffee."
    m "....Eh, I guess I kinda deserved it."
    e "...Do you want to make it up to him?"
    
    m "Depends on what you have in mind."
    e "Go buy Sissel something to eat."
    e "The poor kid hasn't eaten since yesterday morning, and he can't really afford anything right now."
    e "Plus it's almost his lunch break."
    
    m "And how do you know that?"
    e "Because I'm nosy like that-"
if steal_wallet == "false":
    hide sissel neutral uniform
    show sissel embarrassed uniform
    with dissolve
    s "It's you again."
    s "Uh, thanks for returning my wallet earlier."
    s "Really, it meant a lot. It's nice to see people being nice for once."
    
    hide sissel embarrassed uniform
    with dissolve
    show sissel neutral uniform at right
    with dissolve
    show phillip neutral at left
    with dissolve
    p "Wow [charname], being a good Samaritan on your first day?"
    m "Ahah, just doing my best."
    s "-!!!!!{p}......It's you."
    p "Huh? {p=.3}Oh! You're that kid who's always by the lake!"
    s "And you're that kid who always hangs out near that old wishing well."
    
    "I glanced between the two of them,{w=.3} a bit bewildered."
    "Did these two know each other?"
    
    "Phillip chuckled before extending an inviting hand towards Sissel."
    
    p "Nice to finally meet you properly.{p=.3}My name's Phillip by the way."
    s "Heh, likewise. {p=.3}The name's Sissel."
    p "Oh!{w=.3} Speaking of which..."
    
    "Phillip handed Sissel an ID card."
    p "You missed orientation earlier, didn't you? {p=.3}Owen asked me to give you your ID card."
    "There was also a note attached to it. Sissel took a moment to read it before looking back to us."
    
    s "...You guys came all the way out here to deliver this?"
    s "By the way, what are your names?"
    
    m "Me? I'm [charname]."
    s "Well [charname] and Phillip, thank you. I appreciate it."
    
    s "Oh, Phillip, you're Owen's roommate right?"
    p "Uh yeah."
    s "Let me know if he ever gives you any trouble."
    s "I'll kick his ass for you."
    
    p "Ha,{w=.3} I might take you up on that offer."
    
    m "I guess you and Owen know each other too?"
    s "We've been friends for a looooooong while."
    s "He's a good guy at heart,{w=.3} but he's also really.......colorful,{w=.3} ya know?"
    s "Sometimes I just want to punch him in that pretty little face of his-"
    s "Anyway, this is still a cafe. What do you want to order?"
    
    scene cafe back with Dissolve(2.0)
    
    "Phillip and I ordered our food and sat in the back of the cafe."
    "My stomach growled happily as I take a bite of my sandwich."
    
    show phillip neutral
    with dissolve
    p "You must be really hungry, huh?"
    m "Today took a lot out of me."
    m "I deserve to satiate my stomach."
    
    p "Yeah, things have been pretty rough so far."
    p "Sissel doesn't look too happy either. Maybe he's having a rough day himself?"
    
    m "Speaking of,{p=.3}How do you know Sissel?{w=.3} Have you two met before?"
    p "Sort of?{w=.3} I hang around this lake pretty often when I was younger,{w=.3} and Sissel's always there as well."
    p "We talked every now and then,{w=.3} but I never knew his name until now."
    
    
    m "Yeesh, I can see why.{p=.3}That's one grumpy kid."
    
    play sound "ghost.mp3"
    hide phillip neutral
    with dissolve
    show echo blurry
    with dissolve
    
    e "True, but he's not a bad person, really."
    m "Damn it, give me some warning when you pop up like that!"
    e "You'll get used to it."
    e "By the way, thought you'd like to know,{p}Sissel gave you a discount on your coffee."
    m "What really?"
    "I checked the receipt and sure enough, the coffee was a dollar off."
    m "Wow, I guess Sissel isn't as terrible as he acts sometimes."
    e "The guy's got a lot on his shoulders."
    e "By the way, do you want to really make his day better?"
    m "I smell ghostly scheming."
    e "It's nothing bad!"
    e "Just go buy Sissel something to eat."
    e "The poor kid hasn't eaten since yesterday morning and probably can't afford anything right now."
    e "Plus, it's almost his lunch break."
    
    m "...you are either a really nice guy, or the nosiest ghost in the world."
    e "Haha, I get it all from you little man."
    m "What-"
                
        
        


hide echo blurry with dissolve
show phillip neutral with dissolve
p "[charname]?"
m "E-eh?!"
p "You were dozing off for a while. Who were you talking to?"
m "N-no one! Just daydreaming!"
p "Alright, if you say so."
m "..."
m "........"


scene cafe front
with fade

show phillip neutral
"After finishing our meals, Phillip and I began heading back to the academy."
"When we got to the door, I stopped myself, a feeling nagging at the back of my mind."
"Well [charname], it's time to be a good person."
m "Hey Phillip, you go head back without me. There's something I gotta do."
p "Hm? Sure thing!"
p "See you back at school then!"
p "If I don't get lost, that is."

hide phillip neutral
with dissolve

"And with that, Phillip left the building,{w=.3} leaving me alone with Sissel."
"I took a long, deep breath before approaching him."

m "Hey Sissel."

show sissel neutral uniform
with dissolve

s "What do you want?"
m "Well uh, i-it's almost your lunch break right?"
m "How about I get you a sandwich or something? My treat."

hide sissel neutral uniform
show sissel surprised uniform
with dissolve

s "W-what-?{p}I-I..."
s "..."

hide sissel surprised uniform
show sissel embarrassed uniform
with dissolve

s "Actually, that would be great."
s "Thanks."

scene cafe back with Dissolve(2.0)

show sissel neutral 

"Wow, Sissel's wolfing down that sandwich like he's never eaten before in his life."

s "*munch*munch*gulp*slurp*"
s "Ah, that really hit the spot."
s "Thanks a bunch [charname]."

m "Eheh, you're welcome."
m "Actually, I'm glad I got you lunch."
m "You looked like you really needed it."

show sissel indignant with dissolve

s "...Did I really look that hungry?"
s "Haha, I guess I should be grateful you noticed."

m "You gotta learn to take care of yourself though."
m "Nobody should starve themselves like that."
 
show sissel neutral with dissolve

s "I'd love to. But it's not that easy."
s "I...I was homeless and living on the streets until a few weeks ago."
s "It's a bit of a difficult adjustment."

m "O-oh wow, I never realized."
m "But it sounds like things are getting better, right?"
m "You have a job and a place at the academy now."

s "True...But then there's assholes like that teacher...{w=.3}Dolores, was it?"
s "He's been warning everyone that I'm a crooked thug."
s "*Sigh*{w=.3} Life's hard enough without judgey people making things more difficult..."

show sissel happy with dissolve

s "By the way [charname], I want to thank you again."
s "I...I haven't been the nicest person to you so far."
s "But you're still kind enough to help me out so uh..."
s "Thank you."

m "Oh h-haha, it's been my pleasure."

hide sissel with dissolve

pause(2.0)

"The two of us stayed at the cafe for a while, exchanging small talk."
"It was surprisingly enjoyable."
"In fact, we didn't even notice it was time to go before Sissel's boss shooed us away."

scene school dusk
with Dissolve(5.0)

"After returning from the cafe, I found myself standing on campus yet again."
"It's the afternoon, and thankfully there are no more classes today."
"No homework either. {p=.1}Just a huge chunk of free time."
"I wonder what I should do?"

menu:
    "Stroll around campus":
        $ photo_1 = "phillip"
        "Well, might as well use this time to familiarize myself with the campus."
        "This place is going to be my home for the next month,{p=.1}I should probably explore around a little."
        
        scene courtyard dusk
        with Dissolve(3.0)
        "It turns out Gerania Academy was huge, almost exactly like a college."
        "The area is pretty calming and serene{p=.1}and despite being in the middle of a big city,{p=.1}there's plenty of greenery everywhere."
        "The school courtyard was a popular chill-out place for students, it seemed."
        "Some were relaxing on the grass while others grouped up around park benches."
        "I can see why people like this courtyard,{p=.1}I haven't felt so stress-free since I arrived here."
        
        "Suddenly, something wet plopped onto my nose and I blink in surprise."
        
        scene bubbles
        with Dissolve(2.0)
        
        "There were bubbles floating down from the sky."
        "I glance up and see a small figure at the roof of my dorm building,{w=.3}blowing gentle trails of bubbles that danced across campus."
        "The bubbles almost seemed to glow, decorating the air with the light of the brilliant sunset."
        
        "Curiosity welled up inside me, and I decided to make my way up to the roof."
        
        scene dorm roof dusk
        with Dissolve(3.0)
        "Wow......{p=.1}The view is beautiful from up here."
        "I made my way to the edge of the roof and see none other than Phillip."
        "He was sitting on a bench with giant piles of textbooks and papers scattered around him."
        "The floor was littered with papers filled to the brim with homework assignments."
        
        show phillip tired frown
        with Dissolve(3.0)
        
        "Phillip notices me approaching and gives me a small, tired smile."
        hide phillip tired frown
        show phillip tired shrug
        with dissolve
        p "Oh hello [charname].{p=.1}How was your date with Sissel?"
        m "W-what?!{p=.1}It wasn't a date! We were just hanging out!"
        p "Haha I'm just joking.{w=.3} Glad to see you guys get along though (I think?)."
        
        hide phillip tired frown
        show phillip tired smile
        with dissolve
        
        "Phillip giggled to himself and continued blowing bubbles over the edge of the roof,{p=.1}descending gently down to onlookers in the courtyard."
        m "So uh...what are you doing up here Phillip?"
        
        play music "parting.mp3" fadein 5 fadeout 5
        
        "He doesn't answer."
        "The two of us watch in silence as Phillip's bubbles float several stories down to other students and visitors,{p=.1}much to their delight."
        "Giggles and laughs echo up to us as some more playful students chase and bat the bubbles."
        "I look to Philip and see his exhausted and worn face break out into a small smile."
        
        p "....I have trouble sleeping sometimes.{w=.3} Too many thoughts in my head."
        p "Sometimes I'd be trying to work on stuff,{w=.3} but then bad thoughts and memeories just crawl into my skull."
        p "Then I'd spend the rest of the day feeling miserable for no good reason."
        
        "My chest lurched slighty.{w=.3} His words hit a little too close for comfort."
        m "That sounds....."
        m "Are you doing okay?"
        "Phillip shrugged tiredly."
        p "I'm fine,{w=.3} it's just a thing I gotta deal with."
        
        scene sunset phillip with Dissolve(2.0)
        pause(2)
        
        "He gestured towards the vast view of the cityscape under the sunset."
        "The sky and horizon was bathed in beautiful shades of red and orange."
        
        p "I like coming up to high places and watching the world go by."
        p "Up here,{w=.3} all the petty thoughts feel so small,{w=.3} you know?"
        m "Is the bubble-blowing a stress relief tactic too?"
        p "Kinda?{w=.3} I just find it plain fun."
        "He laughs and waves a hand toward the courtyard below."
        p "Isn't it great how people's faces just, light up, when they see bubbles fall from the sky?"
        p "It’s a simple thing, but I think the greatest feeling in the world is when I can make someone else smile."
        "I grin and gave Phillip's shoulder a friendly pat."
        m "Well you've certainly managed to make me smile, buddy."
        "Phillip flushes with embarrassment and laughs."
        p "You do the same for me, [charname].{w=.3} Kinda."
        p "It’s been a nice first day here, hasn’t it? I hope the rest of our summer stays just as bright and happy."
        "I nod in agreement."
        "Another long silence followed as the two of us took in the beautiful sight of the setting sun."
        "On a whim, I picked up the camera from around my neck and snapped a picture of the scene."
        "I stare at the resulting photo fondly."
        "If we were to have a bright and happy summer, then I hope my camera records every moment of it."
        scene black
        with Dissolve(3.0)
    "Go to the gym":
        $ photo_1 = "owen"
        "Well, I suppose I should do something healthy for once and head to the gym."
        "Honestly I don't feel like exercising but at least I can pretend I'm making an effort."
        
        scene gym
        with Dissolve(3.0)
        
        "The gym was surprisingly crowded at this hour.{p=.1}Besides a handful who were still working out, most were leaving as I came in."
        
        show owen shorts
        with dissolve
        
        "...Oh hey, there's Owen in the corner.{p=.1}And he's shirtless."
        "The way the evening light shine across his chest as he uses the arm-press really puts his muscles on display."
        "He's got a nice body too...(gulp)."
        "For a moment we made eye contact. {p=.1}Owen breaks into a smile and waves at me enthusiastically."
        o "Oh hey there [charname].{p=.1}How's your first day so far?"
        m "Eh, it's been ok. A bit spoopy though."
        o "Pfft spoopy?{p=.1}Ah I see you got your hands on the so-called cursed camera."
        o "I wouldn't pay too much attention to all those rumors if I were you."
        o "That camera's only been here for a few days. It's not as old or haunted as it looks."
        m "Really? Why does it look so beat up?"
        o "Nobody knows.{p=.1}It kinda just showed up one day in Mrs. Corlisse's office. They figured a former student forgot about it or something."
        m "Well that's not suspicious at all."
        o "It's just a clunky camera. How bad can it be?"
        o "By the way, are you here to work out or just stand there lookin' pretty?"
        
        m "M-me?"
        m "No one's accused me of looking pretty before."
        
        "Owen laughed and gave me a flirty wink."
        o "I'm surprised,{w=.3} you're pretty easy on the eyes~"
        
        m "Uh.......{w=.3}um......."
        "Brain rebooting...Please wait...."
        "I shake my head vigorously before hopping on a nearby treadmill,{p=.1}doing my best to ignore Owen's laughter."
        "As I begin a light jog, I shoot him a wry glare."
        m "Oh shut up.{p=.1}You were the one distracting me with all the camera talk."
        "Owen gave me an amused shrug before going back to his arm-presses."
        "He watched me with interest as I kept jogging. I couldn't help but feel a bit self-conscious."
        m "What are you staring at?"
        o "Oh nothing. Just wondering if you go to the gym much.{p=.1}You have horrible running posture."
        m "Ouch. Thanks for stabbing my self-esteem."
        m "Eh, you're probably right though. I don't do this much."
        o "Just try to land on the middle of your feet and straighten your back a little.{p=.1}Relax your shoulders a bit too."
        m "Like this?"
        o "Yeah, just like that.{p=.1}You'll put too much strain on your calves the way you were before."
        m "Mm, thanks Owen. {p=.1}Do you come to the gym a lot? You seem to know a lot about this."
        o "Me? I guess you can say that.{p=.1}The gym's always been the place I'd go to relax and take my mind off of things."
        
        "I shot him a disbelieving face as I continued to rasp for air on the treadmill."
        m "...huff...'Relaxing' he calls it."
        o "Hey, you're just out of shape.{p=.1}With practice, this place can be pretty chill~"
        m "...hurff...gah...if you say so."
        
        scene gym
        with Fade(2,1,1)
        
        "Hufff....Uuuughhh I've been running for a while now.{p=.1}It feels like hell is burning in my legs."
        "Huff....hufff....."
        "Huh? Looks like I forgot to bring water with me. Damn!"
        "Looks like I'll just die from dehydration here.{p=.1}The world can be so cruel."
        
        "Suddenly something ice cold and wet pressed against the back of my neck."
        m "{size=+10}EEEEEEEEAAAAHHHYYRRRREEEEEEEEEEHHHHHH{/size}"
        
        show owen shorts
        with dissolve
        
        o "Geez, chill out [charname].{p=.1}Just here to give you a bottle of water. Gotta stay hydrated and all that."
        m "You didn't have to scare me like that!"
        o "Heh, but where's the fun in that?"
        "I grabbed the water from him with contempt before gulping the whole thing down."
        "Gaah, that felt better.{p=.1}I let out a long, content sigh before slumping to the ground in exhaustion."
        "But a pair of strong, warm arms crept beneath me a held me up before I could get anywhere comfortable."
        "I glance up and notice how close Owen and I both were. My head was resting on his bare chest, still glistening with sweat."
        o "Hey, it's bad to sit right after exercising, [charname]."
        o "Wanna go on a little walk with me instead?"
        "I groaned and slumped against him."
        m "Guugghh why are you people so healthy?"
        
        scene courtyard dusk
        with Dissolve(3.0)
        
        "The two of us leisurely strolled around the campus.{p=.1}The setting sun shimmered brilliantly in the sky above."
        "It was quite a beautiful scene really. The sharp hues of orange and red really complimented Owen's fur."
        
        show owen neutral
        with dissolve
        
        m "Say, Owen? How long have you been at the academy? You really seem to have a \"lived in\" feel around this place."
        o "Mmm...I've been living here at the academy year-round for about 5 years I think?"
        m "Year-round? Don't you ever get homesick?"
        o "Home?"
        "His face held a wry smile."
        o "My home's kinda empty.{w=.3} Gerania Academy's my new home away from home."
        
        o "Granted, I haven't made many friends here thanks my \"snotty rich kid\" image................."
        o "...and I do get homesick sometimes......"
        m "Don't you get to visit your family sometimes?"
        "Owen fell quiet."
        "There was a regretful and bitter look on his face...."
        "I was silent for a few moments, thinking of a way to respond before something catches my eye."
        m "Oh wow, look!"
        o "Hmm?"
        
        play music "parting.mp3" fadein 5 fadeout 5
        
        scene bubbles
        with Dissolve(2.0)
        
        "Trails upon trails of bubbles floated down from the sky, decorating the crisp afternoon air with reflected hues of the setting sun."
        "The scene was beautiful and breath-taking to behold."
        o "Ah, it looks like someone's blowing bubbles on our dorm roof."
        m "...I...I need to take a picture of this!{p=.1}This is too good of a chance to pass up."
        "I fumbled for my camera and snapped the image, smiling fondly at the resulting photo."
        "The sunset's orange hues painted the photo with a dazzling display of color.{p=.1}Bubbles sparkled in the light like gentle floating stars."
        
        m "..........."
        m "Hey Owen?"
        o "What is it?"
        m "Your home really is beautiful."
        o ".................{p}Yeah, it is."
        scene black
        with Dissolve(4.0)
        

scene dorm night with Dissolve(3.0)
play music "happy_lounge.mp3" fadein 5 fadeout 2

"I fall into my bed with an exhausted slump."
"Boy it's been a long day. Who would have thought so much could happen?"
"Gerania Academy has a few weird quirks, but...{p=.1}things have been pretty nice so far."
"Ghosts or not, I'm going make the most my time here."
"I glanced around my dark room tiredly."
"Being around people for once feels very...{w=.3} uplifting."
"Maybe things will start getting better after all."
"With a long sigh, I close my eyes and let the tides of sleep carry me away."

scene black with Dissolve(2.0)
scene repeat_screen with Dissolve(1.0)
pause(1.5)

scene black with Dissolve(2.0)
show phillip tarot  at farleft with dissolve:
            xzoom .4 yzoom .4
show owen tarot  at rcenter with dissolve:
            xzoom .4 yzoom .4
show sissel tarot  at farright with dissolve:
            xzoom .4 yzoom .4
            
            
jump day2
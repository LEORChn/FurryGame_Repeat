label day8_morning:
    
$ persistent.current_route = "default"
"{b}Day 8:{/b}{w=.5} Edelweiss"

scene black with Dissolve(3.0)
stop music
scene dorm with Dissolve(3.0)

"Monday mornings are the bane of every creature's existence."
"I can feel my lazy bones clinging to the mattress in agonizing protest."
"It's so tempting to sleep in,{w=.3} but Mrs. Corlisse would skin me alive for missing her class...."
"Ugh alright,{w=.3} waking up."


play music "snowy-street.mp3"
scene hallway with Dissolve(3.0)
show phillip neutral with dissolve
p "Huh?{w=.3} Oh hey there [charname]."
p "Are you alright?! You look kinda dead..."
m "That's just my face. {w=.3}Especially in the morning."
m "By the way, {w=.3}what are you doing here? I thought your class was in another building."
p "There were some scheduling changes so apparently I'll be joining your class today instead."
m "A joint class? {w=.3}That doesn't sound like something Mrs. Corlisse would do-"


scene art room with Dissolve(3.0)
"It turns out I was right."
play music "hyperfun.mp3" 
"Mr. Rokov stood in front of the class with a level of enthusiasm that should be illegal this early in the morning."
r "GOOD MORNING CHILDREN!!"
"Half the class reared back in nervous terror."
r "Unfortunately Mrs. Corlisse is busy visiting a family member in the hospital and won't be with us today."
r "Fortunately for you,{w=.3} {b}{i}I{/i}{/b} graciously offered to teach in her stead!"

show phillip annoyed with dissolve
p "Mm,{w=.3} I heard Mr. Rokov used to teach at an elementary school."
m "I can definitely tell."
m "Just how the hell did he end up at Gerania Academy?"
show phillip annoyed look with dissolve
p "They say he got fired for flooding the school? {w=.3}Something about an over-zealous demonstration of the water cycle."
p "It was sewer water too, so the whole school got shut down for being a biohazard."
m "................how badly would Mrs. Corlisse kill us if we skipped this class, just for today?"

hide phillip with dissolve

"We were interrupted Mr. Rokov's exuberant....{i}everything{/i}."

r "Alright class!{w=.3} Rearrange all the desks in a huge circle arround the room! {w=.3}Be sure to create a large empty space in the middle!"

"Our classmates looked at each other wearily before following his instructions."
"Looks like we have no say in our own fate."

"Mr. Rokov was settling down in the center of the circle with a suspiciously large pitcher of water and a rustling shoebox."

r "Have you folks been studying? {p=.3} [charname]! Explain what the term \'gesture\' means in art!"

m "Me?! {p=.3}Ah, um, it's got something to do with a figure's movement in action?"
r "That was an awful description but yes! {w=.3}You are correct!"
r "A gesture drawing or photo is a quick, unrefined sketch that captures a person's movement. {w=.3}We will all be practicing this today!"
r "Photographers will be taking photos while artists will create sketches!"

m "What are we even photographing?"

"Mr. Rokov suddenly flipped open the shoebox."
show pigeon with dissolve

"A ridiculously fat pigeon plopped onto the classroom floor, {w=.3}clucking indignantly."
"Phillip stared between the water pitcher and pigeon suspiciously."
p "Wait, {w=.3}he wouldn't-"

r "{size=+10}BEGIN!!!{/size}"

play sound "water-splash.wav"
play music "batty.mp3"
hide pigeon with dissolve

"The pigeon squawked madly as a gallon of ice water pelted its backside."
"The borb shot across the room  like a possessed pom-pom as Mr. Rokov chased it merrily."
"That's.......{w=.3}probably the most exercise that pigeon's gotten in years."
"The rest of the class was gaping in fascinated horror."
p "W-what?!{w=.3} We can't just let him torture the poor bird like that!"
m "It's not like PETA's gonna rush in to crash an art class-"
r "Get to work,{w=.3} chop chop!"
r "You'll only have a few seconds per photograph or sketch! {w=.3}I'll be grading you all on quantity later!"

"There was a flurry of paper and cameras and the class scrambled to work."
"I sighed an grabbed my camera.{w=.3} Better get to work."

"Good luck little birb.{p=.3}I believe in you."

scene black with Dissolve(2.0)
play music "snowy-street.mp3" fadein 3
scene hallway with Dissolve(3.0)

play sound "bell.wav"
"That class couldn't have ended quickly enough."
"As soon as the bell rang,{w=.3} everyone rushed out the door in a flurry of feathers and photos."

"Mr. Rokov was still shouting merrily from inside the classroom."
r "Remember kids!{w=.3} Visitor's Day will be in two days on the 10th!"
r "Make sure you create lots of art for your friends and family to admire!"


show phillip annoyed with dissolve
p "Oh yes,{w=.3} let's show them our pigeon-torturing methods."
p "Don't question it!.{w=.3} It's art."
m "To be fair, that pigeon could probably use the exercise.{w=.3} That thing's as wide as it is tall."

p "That doesn't mean it deserves to be friggin' {i}waterboarded!{/i}"
m "Well if you put it that way-"

"There was a suddenly rustling sound from Phillip's handbag."
m "Wait,{w=.3} did you steal the pigeon?!"
p "Of course I did!{w=.3} What if Mr. Rokov is teaching culinary arts class next?!"

hide phillip with dissolve
show pigeon with dissolve

"Pigeon" "{size=+10}*SQUAWK!*{/size}"

hide pigeon with dissolve 
show phillip smile shrug with dissolve

p "Isn't he cute?{p=.3}Don't worry little guy,{w=.3} I'm not leaving you with that damn wet napkin-"
m "......you need to work on your insults."
p "{i}Anyway,{/i}{w=.3} where were we?"
show phillip neutral with dissolve
p "Oh yeah{w=.3} is your family coming for Visitor's Day?{w=.3} Mine are probably dying to scrutinize every little thing I do."
m "Visitor's Day?"

"I must have visibly cringed because Phillip gave me a worrying look."
m "Eh,{w=.3} my parents probably don't care much about what I'm doing here."

p "Aw that's a shame.{w=.3} You're doing pretty well for an ameteur photographer."
p "Look on the bright side! {w=.3}You can treat the day as a little vacation from classes~"

m "If you say so."

p "Welp,{w=.3} I better take this little bird back outside.{w=.3} I'll see you later [charname]!"

hide phillip with dissolve
"I waved at Phillip's retreating back absentmindedly and sighed."
"Well,{w=.3} looks like I have the entire afternoon to myself again."
"I don't feel like spending it alone.{w=.3} I wonder where I should go?"

menu:
    "Visit the Cafe":
        "I could probably swing by cafe and see how Sissel's doing.{w=.3} And maybe buy a few chocolates while I'm there too."
        "Chocolate....{w=.3}that's always a perfect mood-fixer."
        "Just thinking about it is making me drool."
        
        scene black with Dissolve(2.0)
        play music "cafe-music.mp3" fadein 3
        scene cafe front with Dissolve(3.0)
        
        "I tentatively peaked into the cafe.{w=.3} It looks like Sissel isn't around."
        "Maybe he's out back in the kitchen somewhere."
        "Meh, {w=.3}I should just find a table and wait for him-"
        
        j "Oh hey!"
        
        scene cafe back with Dissolve(2.0)
        show jinny neutral with dissolve
        
        "I whirled around to see Jinny at a corner table,{w=.3} idly sipping a cup of boba tea."
        j "It's you! {w=.3}The ghostbuster!"
        m "Don't call me a ghostbuster.{w=.3} Some poor writer's probably screaming about copyright infringment right about now."
        j "Heh sorry. {w=.3}It's just the first thing that popped in my head when I saw you."
        j "Fancy seeing you again in here of all places."
        
        "Jinny cheerfully beckoned me to join her table."
        j "So...{w=.3}what was your name again?{w=.3} Your number on my phone is saved as \"ghost whisperer.\""
        m "Gee I feel important.{w=.3} The name's [charname]."
        m "Correct me if I'm wrong,{w=.3} but didn't you say you were under house arrest?"
        m "Why are you sipping boba tea at a cafe?"
        
        j "It's not {i}real{/i} house arrest.{w=.3} I've just got.......{w=.3}strict caretakers?"
        j "Eh, it's complicated."
        j "Even so, could you blame me for sneaking out?{w=.3} This is the best cafe in the city for sweet drinks."
        j "Not to mention one of my best friends work here."
        
        m "Best friend?{w=.3} That wouldn't happen to be-"
        
        
        show jinny at left 
        show sissel neutral at right 
        with dissolve
        
        s "Hey tTeach, I appreciate the visit but you-"
        s "Oh! {w=.3}[charname]! {p=.3}When did you get here?"
        m "I thought I'd come visit and see how you were doing."
        j "Aaaw,{w=.3} isn't that sweet?"
        j "[charname]'s a cute one,{w=.3} I see why you like him so much."
        show sissel indignant with dissolve
        
        s "I don't-!!"
        "Jinny laughed and elbowed me playfully."
        j "Sissel wouldn't stop talking about you for a whole week.{w=.3} I didn't realize you were {i}the{/i} [charname]."
        j "The world's such a small place."
        
        show sissel annoyed with dissolve
        s "Teach,{w=.3} quit talking about me.{w=.3} I'm right here."
        j "Alright.{w=.3} [charname], order a drink or something."
        j "Then we can talk about Sissel when he's not here."
        
        m "An ice mocha sounds pretty good.{w=.3} Gotta get my chocolate fix."
        show sissel indignant with dissolve
        s "[charname], don't just play along!"
        m "How else am I going to get all the good gossip about you?"
        
        s "Ugh..."
        
        hide sissel with dissolve
        "Sissel sulked behind the counter and began mixing drinks while staring at us warily."
        
        show jinny neutral at center with dissolve
        j "Aaw,{w=.3} you guys are adorable.{w=.3} How did you two meet?"
        m "We're just friends and classmates at Gerania."
        j "Just friends? {w=.3}That's questionable at best."
        m "Eh enough about me,{w=.3} what about you?{w=.3} How come Sissel calls you \"teach?\""
        
        "Jinny fondly glanced up at Sissel working at the cafe counter."
        j "I've known Sissel for a loooong time."
        j "I've always wanted to be a teacher,{w=.3} so when I was little I started a little tutoring service outside my \"house.\""
        j "Sissel was my first and only pupil."
        j "I taught him how to read and snuck a bunch of stuff to him when he was still on the street."
        j "In return,{w=.3} he helped me sneak out a lot and gave me a tour of the city."
        m "Wow,{w=.3} you guys seem close..."
        j "Hey, no need to feel jealous!{w=.3} It only takes a pair of eyes to see Sissel has a thing for you~"
        m "T-that's not what I meant!"
        j "Just let me know if you're ready to make a move.{w=.3} I'll be your dedicated wingman!"
        
        show jinny at left with dissolve
        show sissel neutral at right with dissolve
        
        "Sissel approached our table again,{w=.3} eyeing us suspiciously."
        s "Here's your mocha-"
        s "[charname], why is your face red?{p=.3}Whatever she said, {w=.3}it's all lies. {w=.3}All of it."
        j "C'mon Sissel,{w=.3} I haven't even gotten to the good stuff yet."
        j "There's still that stack of embarrassing photos that I need to unleash into the world-"
        show sissel surprised with dissolve
        s "I thought I burned all of them?!"
        j "I have several copies in case you found them.{w=.3} They make excellent gifts for new friends~"
        
        show sissel indignant with dissolve
        s "Ugh, since when were you two so chummy?"
        m "Apparently I helped her sneak into the school a few nights ago."
        s "Oh boy,{w=.3} did she drag you into another one of her little \"adventures?\""
        j "Heh, not yet!{w=.3} I let him get back to sleep after I got into the building."
        s "You're lucky [charname]. {w=.3}One time she dragged me around Bradley Lake to look for ghosts. {w=.3}We got lost for hours!"
        j "We could have just swam back to the main road,{w=.3} {i}but nooooo{/i} someone refused to even touch the water-"
        
        "Sissel groaned in fond exasperation."
        show sissel neutral with dissolve
        s "Aaaaaanyway let's change the subject."
        s "Isn't Visitor's Day coming up at school?{w=.3} Are you going to come along Jinny?"
        j "Are you {i}inviting{/i} me to sneak into the school?"
        j "Excellent, {w=.3}I've taught you well my fine pupil."
        m "What is there even to see on Visitor's Day?"
        s "Besides the formal dance party afterwards?"
        s "Eh, most of it is just the academy showing off to the parents."
        j "Not Sissel though.{w=.3} He's taking a culinary arts course and that means {i}free food.{/i}"
        s "Is that the only reason you're visiting?"
        j "Of course not! {w=.3}I gotta see how my favorite pupil is doing at a real school now!{w=.3} You've grown up so much!"
        
        show sissel embarrassed with dissolve
        "Sissel flushed as Jinny beamed at him proudly."
        s "I uh.......{w=.3}thanks teach."
        s "I'll do my best-"
        
        hide jinny
        hide sissel
        with dissolve
        
        stop music 
        play sound "slam.wav"
        
        "The cafe door suddenly slammed open as a furious Mrs. Corlisse crashed into the building."
        "As she glared in our direction,{w=.3} a sudden inhumane fear seemed to seep into our blood and chill us to the bone."
        play music "batty.mp3" 
        c "{size=+10}JINEVA CORLISSE,{w=.3} HOW DARE YOU SNEAK OUT AGAIN?!!!{/size}"
        show jinny neutral with dissolve
        j "Oh shit,{w=.3} Gran's found me."
        j "Gotta go!"
        hide jinny with dissolve
        "Jinny shot out the door with Mrs. Corlisse sprinting after her in a frenzied chase."
        "For such a tiny old lady,{w=.3} Mrs. Corlisse runs with a ridiculous amount of vigor."
        "Within seconds,{w=.3} the two of them disappeared into the horizon."
        
        stop music
        show sissel neutral with dissolve
        s "........................................those two scare me sometimes."
        play music "cafe-music.mp3" fadein 3
        m "Wait,{w=.3} so Jinny is Mrs. Corlisse's granddaughter?!"
        s "Yeah,{w=.3} wasn't it obvious?"
        s "I mean, they've got the same hair and face and everything...."
        m "Hm, {w=.3}now that you've mentioned it...{w=.3}I can really see the resemblance."
        "(At least I think I do.{w=.3} I've never gotten a good look at Mrs. Corlisse's face for some reason...)"
        s "Speaking of resemblances,{w=.3} I've been meaning to ask."
        s "Are you and Jinny related or something?"
        m "Us? {w=.3}No, I've only just met her a few days ago."
        s "Really? {w=.3}You two look almost identical. {w=.3}I was sure you two were at least relatives or something."
        
        "I huffed indignantly."
        m "Hey Sissel,{w=.3} I met this rabbit the other day. {w=.3}Fluffy tail, long ears.{w=.3} Think you're related?"
        "Sissel chuckled and gave me a friendly punch to the shoulder."
        s "Eh point taken."
        
        
        
        s "Um................{w=.3}so now that you're here...."
        s "Do you want to help me out with some taste testing in the kitchen?"
        s "I'm trying out a few new chocolate recipes-"
        play music "batty.mp3" 
        m "{i}Absolutely.{/i}{w=.3} I'm a complete slut for chocolate."
        m "Sissel you sly dog.{w=.3} You really know how to capture my heart."
        s "Ugh,{w=.3} I'm kinda scared now that you know Jinny."
        s "You two are probably going to end up joining forces and make my life hell."
        m "It'll be a pleasant kind of hell, {w=.3}I promise you~ <3"
        
        "And so we spent the rest of the afternoon sharing sweets and friendly conversation at the cafe."
        "I was right."
        "Chocolate really is the perfect mood-fixer~"
    "Visit Owen/Phillip's Room":
        "It'd be nice to just hang out with Phillip or Owen for the day."
        "Well...{w=.3}Phillip's probably busy with his overloaded class schedule."
        "Maybe Owen will be around?"
        
        play music "calm-guitar.mp3" fadein 3
        scene dorm hallway with Dissolve(3.0)
        
        "I leisurely strolled through the dorm halls towards Owen's dorm."
        "Usually there's the muffled sounds of playful bickering coming from their rooms,{w=.3} but it's surprisingly quiet today."
        
        "I gave their door a soft knock."
        o "Yo,{w=.3} come in!"
        
        scene PO dorm with Dissolve(3.0)
        show owen neutral with dissolve
        o "Oh hey [charname]!{w=.3} For what do I owe this pleasure?"
        m "Nothing much,{w=.3} I just figured we could hang out-"
        m "Wait."
        m "Are you................{w=.3}knitting?"
        
        
        "Sure enough,{w=.3} Owen steadily knitting away at his desk with a large pile of colorful yarn."
        "It looked like he was making some sort of red scarf."
        show owen grin 2 with dissolve
        o "Yup!{w=.3} It's a little hobby of mine."
        show owen neutral with dissolve
        o "Why does everyone look so surprised when they find out?"
        
        m "You have to admit it doesn't really fit your whole athletic jock \"picture\"..."
        m "It seems more like something Phillip would be into."
        
        o "Oh Phillip loves it too.{w=.3} Just for an entirely different reason."
        o "He keeps stealing my yarn balls and rolling around in them!"
        o "Fit {i}that{/i} into your \"picture.\""
        
        m "He actually does that?!"
        m "I thought that kind of thing was mostly cat stereotypes..."
        m "At least he's playing with your balls.{w=.3} Just not in the way you want."
        o "Pffft, there's plenty more where that came from."
        
        o "The other day I was vacuuming our floor and Phillip {i}screamed{/i} and bolted under the bed."
        show owen grin nervous with dissolve
        o "He made me swear to never vacuum around him again."
        show owen grin 2 with dissolve
        o "You should have seen him!{w=.3} His fur was standing straight up. He looked like a complete fluffball~"
        m "It makes me wonder what he'd do if we gave him catnip..."
        show owen grin nervous with dissolve
        o "[charname], no.{w=.3} Phillip would literally kill us."
        m "It's a cause worth dying for."
        o "Eh......{w=.3}I'd like to keep my head on my shoulders thank you very much."
        m "C'mon Owen!{w=.3} Think of the possibilities!"
        m "We could become famous cat video Youtubers!{w=.3} We'll be rich!"
        show owen neutral with dissolve
        o "[charname], I'm kinda already rich..."
        
        "I was only half-listening by now as ideas swam rapidly through my head."
        m "What other things could we do....{w=.3}Do you think Phillip's afraid of cucumbers?"
        m "Or maybe we can get him to snuggle into a cardboard box?"
        m "Or maybe-"
        stop music
        m "-oh shit."
        o "What's the matter?"
        
        m "This morning......{w=.3}Phillip stole this little pigeon from our art class."
        play music "batty.mp3"
        m "What if he's going to eat it?!"
        show owen grin nervous with dissolve
        o "I-I'm sure you're just exaggerating [charname]-"
        m "But WHAT IF??"
        m "Phillip could be enjoying a bloody and fowl feast right now and we're just sitting here doing nothing!"
        o "Oh that poor bird..."
        m "We gotta catch this on camera!"
        show owen neutral with dissolve
        o "What about the bird?!"
        m "Who cares about the bird?{w=.3} There's a million others like it."
        m "I just wanna make a viral video."
        o "[charname], you're horrible."
        
        stop music
        "{i}Click!{/i}"
        "We froze as the doorknob suddenly began turning."
        m "It's Phillip!"
        o "Quick! {w=.3}Hide in the closet!"
        
        hide owen with dissolve
        "Owen and I leapt through the closet door and squeezed ourselves between the coats and jackets."
        "Not a moment too soon.{w=.3} Phillip strolls into the room in an oddly cheerful manner."
        show phillip neutral with dissolve
        p "Owen?{w=.3} Hm, weird. He's usually around this time of day."
        "I strained against my cloth prison to take a closer look at Phillip."
        "Who knew such an innocent little guy could be such a ferocious hunter?"
        m "Wait a second,{w=.3} Owen do you see that-?!"
        o "BLOOD?!!!!"
        
        play music "hyperfun.mp3" 
        show phillip at left
        show owen neutral at right
        with dissolve
        "Owen and I crashed out of the closet and nearly scared Phillip half to death."
        o "Phillip?!! {w=.3}How could you?!!!"
        o "That poor pigeon did nothing wrong!{w=.3} How could you just eat him like a heartless bastard?!"
        o "I know you're a cat but you have to resist those killer instincts!!"
        p "-Wah?!{w=.3} Owen?{w=.3} [charname]?!"
        p "What are you even talking about?"
        m "Explain yourself Phillip!{w=.3} Why are you covered in blood and feathers?!{w=.3} Why did you eat the pigeon?!"
        
        show phillip annoyed look with dissolve
        p ".............you mean this one?"
        show pigeon with dissolve
        "Fat Pigeon" "{size=+10}{i}*SQUAWK!!{/i}{/size}"
        hide pigeon with dissolve
        
        o "I-i-it's alive?!"
        o "T-then why are you covered in blood?!"
        
        show phillip annoyed with dissolve
        p ".......this is red paint.{w=.3} From art class earlier."
        o "..........Oh."
        m "T-then what about the feathers?"
        p "The little birb is shedding at the moment.{w=.3} I helped it with a bit of grooming."
        m "........................Oh."
        
        show phillip annoyed look with dissolve
        p "My turn to ask questions."
        p "Cat? {w=.3}Killer instincts?"
        p "I didn't think you two would peg me with stupid stereotypes."
        o "Ah, we're sorry!{w=.3} We saw you come in with \"blood\" and stuff and we kinda panicked."
        o "P-please forgive us!"
        m "Y-yeah! {w=.3}We're sorry!"
        
        show phillip neutral with dissolve
        p "Kiiiiinda disappointed in you two right now."
        p "Buy me coffee for the week and we'll call it even."
        
        o "Consider it done!"
        m "But Philllip,{w=.3} I've got to ask....{w=.3} is it true that you roll around with yarn balls?"
        stop music 
        
        show phillip serious with dissolve
        p "......................................................"
        p ".....................{w=.3}who told you that?"
        p "Owen did you-?!"
        o "I'm sorry!"
        play music "batty.mp3"
        
        p "{i}OUT OUT OUT!!!{/i}"
        p "{i}YOU TWO ARE SO DEAD!!{/i}"
        
        hide owen with dissolve
        "Us" "WE'RE SORRY!!!!!!"
        hide phillip with dissolve
        "And so Phillip led us on a crazed cat chase for the rest of the afternoon."


scene black with Dissolve(3.0)
play music "lullaby-guitar.mp3"
scene dorm night with Dissolve(3.0)

"The Monday went by a bit more cheerfully than expected."
"By the end of the day, I was completely exhausted.{w=.3} Sleep overtook me as soon as my head hit the pillow."
scene black with Dissolve(2.0)
pause(1.5)
"I was already fast asleep and didn't expect any more interruptions."
"I should have known better."
"Since when did anything go my way?"


play music "blue-feather.mp3" fadein 2
scene dorm night with Dissolve(3.0)
play sound "whisper.wav"

"My eyes instantly fluttered open."
"There was a sound...................{w=.3}something was whispering inside my head........."
"Something was calling for me.{p=.3}Something familiar......"

"S-should I follow it?"
"Y-yeah, probably.{w=.3} These kinds of ghostly things usually don't leave me alone unless I follow through."
"With a tired sigh, {w=.3}I got up and dressed before heading out the door."

scene black with Dissolve(2.0)
scene office night with Dissolve(3.0)

"I followed the voice all the way to the school office building."
"It sounded so weak and fragile,{w=.3} but strongly beckoning at the same time...."
"Where exactly was it coming from?"

"Huh?"
"There was a small potted plant in the office.{w=.3} A flower of some sort."
"Is this..........{w=.3}another wish?"

play sound "whisper.wav"
play music "moonheart.mp3" 
show edelweiss with Dissolve(4.0)

"Edelweiss" "Oh.{w=.3} Why hello there."
"Edelweiss" "I thought I sensed something peculiar within our school's walls."
"Edelweiss" "..........................{w=.3}how curious."
"Edelweiss" "A boy with the eyes of a corpse and a heart full of potential,{w=.3} yet just as dead."

m "W-what are you?"
"Edelweiss" "I am but an old and feeble wish."
"Edelweiss" "But there is yet strength in these withered roots.{w=.3} It is my purpose to help, and it seems you are in dire need of it."
"Edelweiss" "It takes a preposterously strong wish to twist a knot through time itself."
"Edelweiss" "And you are right at the center of it all!{w=.3} Dear boy,{w=.3} you have my greatest condolences."
"Oh great,{w=.3} now I'm talking to a flower that’s spilling meaningless riddles."
"What else could go wrong?"
m "You said you can help.{w=.3} What good can a half-dead flower do?"
"Edelweiss" "I can tell you a story of the flowers surrounding us all."
"Edelweiss" "It is up to you,{w=.3} whether they bloom or wither."
"Edelweiss" "So, what will it be?"
jump day8_menu

label day8_menu:
menu:
    "{b}Orange Rose{/b}":
        "Edelweiss" "Ah,{w=.3} the orange rose."
        "Edelweiss" "For a plant brimming with thorns,{w=.3} he is terribly gentle with those around him, wouldn’t you agree?"
        "Edelweiss" "The cruelty of the world stomps his branches and spit at his leaves,{w=.3} yet he retracts his thorns and forgives."
        "Edelweiss" "Such kindness is almost admirable.{w=.3} And dangerous."
        "Edelweiss" "Teach him to rear his thorns,{w=.3} lest his forgiveness pave the way for his own demise."
        "Edelweiss" "Beware the lily,{w=.3} or see that this orange rose {b}wilts{/b} from their greed."
        jump day8_menu
    "{b}Marigold{/b}":
        "Edelweiss" "Ah,{w=.3} the sweet little marigold that grows by the well."
        "Edelweiss" "Who would have thought there was such unbridled anger within such a small and unassuming flower?"
        "Edelweiss" "Shackled and chained down by his own grudge,{w=.3} he fights and fights and fights,{w=.3} but to what end?"
        "Edelweiss" "What good is a battle,{w=.3} if he dares not to wish for his own happiness?"
        "Edelweiss" "Relieve him and bring him peace,{w=.3} lest this marigold {b}scatters{/b} from his own tired battle."
        jump day8_menu
    "{b}Daffodil{/b}":
        "Edelweiss" "Ah, {w=.3}the worn daffodil that sprouted at the lakeside."
        "Edelweiss" "His suffering and hunger is long behind him,{w=.3} and there is much hope in the road ahead."
        "Edelweiss" "A new beginning,{w=.3} a second chance."
        "Edelweiss" "Will he take it?{w=.3} Or will he race backwards towards the misery he left behind?"
        "Edelweiss" "One could hardly blame him.{w=.3} Orphans cannot help but wonder where they came from,{w=.3} and who left them behind."
        "Edelweiss" "He will not like what he finds."
        "Edelweiss" "However,{w=.3} if he received a second chance,{w=.3} then surely the one who wronged him deserves it too?"
        "Edelweiss" "Fail to convince him,{w=.3} and and watch as this daffodil {b}burns{/b} to ashes in grief."
        jump day8_menu
    "{b}Forget-me-not{/b}":
        "Edelweiss" "Forget-me-nots are for funerals,{w=.3} for grief,{w=.3} and for connections that last through time."
        "Edelweiss" "Your story will not begin until you finish theirs."
        "Edelweiss" "Save them,{w=.3} and in return you will save yourself from this prison in time."
        "Edelweiss" "Seek the truth and look to the past,{w=.3} where this all began."
        "Edelweiss" "Unless you wish to face the noose again?"
        "Edelweiss" "No........{w=.3}no...................{w=.3}don’t do this to yourself."
        "Edelweiss" "Don’t do this to {i}her.{/i}"
        jump day8_menu
    "{b}Morning Glory{/b}":
        "Edelweiss" "The Morning Glory is an odd flower,{w=.3} don’t you think?"
        "Edelweiss" "Death looms at her door,{w=.3} and her memories scattered to the wind."
        "Edelweiss" "Yet she still stands to beckon you towards a brighter path."
        "Edelweiss" "She is the key.{p=.3}Ironic, isn’t it?"
        "Edelweiss" "A girl with the body of a corpse,{w=.3} yet a heart as steeled as any blade."
        jump day8_menu
    "No more questions":
        m "I.......{w=.3}don't think I understood a single word you said."
"Edelweiss" "Nor did I expect you to."
"Edelweiss" "I pray that these words will help you however,{w=.3} when the time comes."

"Edelweiss" "Dawn soon approaches,{w=.3} as does the chosen day."
"Edelweiss" "I pray you make the right choice,{w=.3} {b}wish-granter.{/b}"
        


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

jump day9

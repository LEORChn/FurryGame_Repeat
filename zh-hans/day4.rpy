
#DAY 4 BEGINNING
label day4:

$ persistent.current_route = "default"

"{b}Day 4:{/b}{w=1} False Justice"
scene black with Dissolve(2.0)
stop music fadeout 2
scene dorm with Dissolve(2.0)

"*YAAAAAWWWN*~"
"Another morning, another day.{p=.1}I rub my eyes drowsily as I looked about the room."
"Hm?{w=.6} Looks like someone slid a note under my door."

"\"[charname], it has been brought to my attention that you witnessed a teacher misconduct incident that occurred yesterday.\""
"\"Please meet me in my office this morning to discuss the details of said incident so that proper action may be taken.{p=.5}- Mr. Rokov \(Vice Principal\)\""
".......*sigh*{p=.5}I'm not liking the sound of this."
"Well, let's see what fresh hell awaits me today..." 

play music "snowy-street.mp3" fadein 2 fadeout 2
scene courtyard with Dissolve(3.0)


"As I stumbled across the courtyard toward the teachers' office building, {w=.3}I couldn't help but yawn repeatedly."
"Mmm,{w=.4} I'm really not much of a morning person."
"Now which way is the office.....? {p=.5}Hm?"
m "What the..."
stop music
play sound "wail.wav"
show remnant with Dissolve(3.0)
play music "snowdrop.mp3" fadein 2 fadeout 2

m "What the hell is this thing?"
m "........{w=.5}It's not moving....."
"I wave my hand in front of its.....{w=.5}face?{p=.4}It doesn't move an inch. Is it even alive?"
"Other students were walking around it as if it's not even here."
"Maybe they can't see it, like how they can't see Echo or that ashy girl?"
m "U-um, hello?{p=.5}Can you hear me?"
rr "................................."
"No response again."
m "Eh, it doesn't even have ears."
"I tried poking it, but my finger slips right through like smoke."
m "Hm....{p=.4}Echo? {w=.3}Are you there?"

play sound "ghost.mp3"
e "Yo, [charname].{p=.3}You called?"
m "Yeah, glad to see you're awake inside my head."
e "Just barely, your grogginess makes things kinda difficult.{p=.4}Anyway, what can I do for you?"
m "Well first of all, what is this thing?"
e "-!!!!"
m "Is it dangerous or anything?{p=.1}I don't want some weird ghost wandering around campus and cursing people."
m "One crazy spirit is enough for me."
e "..........It's...{w=.3} a corrupted wish.{p=.5}I think."
e "It must have done something terrible to its wisher to have festered into something like......{w=.3}this."
e "Although, it doesn't feel like it has any real power either.{p=.5}Creepy, but it probably doesn't have the strength to do much damage."
e "Heck, I doubt it can even move on its own."
m "So are we just going to leave it here?"
e "Not much else to do, really.{p=.1}You can't even touch it."
m "I guess you're right.{p=.5}I really hope it doesn't end up hurting people."
m "It's right inside campus too....."
e "Well it can't hurt people if it can't even move.{p=.1}I don't think we have anything to worry about."
e "Anyway, you better get going. {p=.3}You're late."
m "Oh shit! I still gotta meet up with that Mr. Rokov guy!"
stop music fadeout 2
hide remnant with dissolve
"I sprinted down the courtyard, shooting the weird figure one last look.{p=.3}It hasn't budged a bit."
"I sure hope Echo's right about this."
"Well, there's no use worrying. Time to head off to the office."
"...................."

show remnant with Dissolve(3.0)
rr "........................"
rr "................................................"
play sound "wail.wav"
show remnant smile with Dissolve(3.0)
rr "..................she's hereeeeeeeee.........."


scene black with Dissolve(3.0)
play music "snowy-street.mp3" fadein 2 fadeout 2
scene office with Dissolve(2.5)


"I've never been to this side of campus before.{p=.1}Even so, the area that held the all the teachers' offices always felt a little intimidating."
"Now let's see, which one is Mr. Rokov's office? {p=.1}Shouldn't be too hard to find, they're all in alphabetical order."
"Let's see...{w=.3}R....{w=.3}R...."
"Hm? His door is slightly open. I think I can hear someone familiar...?"
"I couldn't help but take a peek inside."

r "-and that's all the assignments.{p=.1}Are you still awake, Phillip?"
p "Hm?{p=.1}Y-yeah, *yaaawn*, of course."
r "Good, because you'll want to hear what's next.{p=.1}I've taken the liberty to remove you from my Law class and transfer you to Mrs. Corlisse's Digital and Studio Art class."
p "W-what?!{w=.3} Why?!{p=.5}Am I failing or-?"
r "Quite the contrary, you're actually at the top of your class and outscored all your peers."
p "Then why are you transferring me?"
r "Would you like the gentle answer or the honest one?"
p "U-um-?"
r "Honest it is then.{p=.5}To be frank, you look absolutely miserable in every waking moment in my class (and those waking moments are quite rare)."
p "That-"
r "Seriously Phillip, I've never had a student look so soul-suckingly numb.{p=.1}It makes me want to break down in tears every morning."
r "You look like the perfect zombie student spreading the sad around."
p "I'm.......{w=.7} sorry-?"
r "Hehe,{w=.5} soul sucking aside, I think you'll be much happier in Mrs. Corlisse's class."
r "Your artwork is quite impressive.{p=.1}More importantly, you seem to actually enjoy it."
p "I can't do that! My mother always pushed me to be a lawyer or a doctor or something more...professional?"
r "You will be the one who lives and breathes your future career, not your mother."
r "You deserve to do something that makes you happy, Phillip."
p "..................."
"There was an awkward pause in the office before Mr. Rokov coughed loudly."
r "Anyway, I believe our little session is almost finished. {p=.1}Onward to the next order of business."
r "I believe our guest has arrived. {p=.1}Why don't you come in, [charname]?"


"I jumped and practically stumbled into the door."
show phillip tired smile with dissolve
p "[charname]? What are you doing here?"
m "O-oh, I got a note that said I was supposed to be here..?{p=.1}I totally wasn't eavesdropping or anything!"
r "Your eavesdropping is forgiven.{p=.5}Anyway, I called you both here to discuss a certain incident yesterday that you both witnessed."
play music "wave-piano.wav" fadein 2 fadeout 2
r "Would you two care to describe what happened between the quarrel between Mr. Dorcas Dolores and the student Sissel?"
"Oh, so that's what's going on.{p=.1}Sounds like Mr. Dolores is finally get the payback he deserves."
"Good riddance too, that guy was an awful teacher."
"Was Phillip at the incident yesterday too? Sure seems like it."
"I told Mr. Rokov everything that happened yesterday, from Mr. Dolores yelling at me to how Sissel stepped in to defend me and got manhandled as a result."
if fight_dolores == "true":
    "I skipped the part where I kicked the old rat in the balls."
    "I don't think Mr. Rokov would take that very well."
    "Phillip gives me a knowing smirk."
if fight_dolores == "false":
    "I couldn't help but grin as I described how red Dolores got when his hair flew away in the wind."
    "Behind me, Phillip tries to muffle his laughter."

p "I'm glad [charname] was there to step in and stop him. {p=.1}You really saved Sissel from Dolores."
"I felt my face grow a little red."
p "I was there too, but I was in the back of the crowd and too tired to do anything."
p "It's a good thing you were there instead."
m "Eheh, I didn't really do much either.{p=.1}I'm glad the school's actually doing something about Mr. Dolores though."
m "There were a ton of other students who witnessed the whole thing so there's no doubt he crossed the line.{p=.1}I hope Dolores gets what's coming to him."
r "Rest assured [charname], the staff and I will make sure Mr. Dorcas Dolores faces the proper-"
play music "close-to-you.mp3" fadein 3 fadeout 2

show phillip irritated with dissolve
"Phillip cuts him off sharply."
p "No, he won't."
p "........{w=.5}In fact, I think this whole meeting is a big waste of time."
"Mr. Rokov coughed awkwardly and tried to regain his composure."
r "And what do you mean by that, Phillip?"
p "What, am I wrong?{p=.1}It's not like Dolores ever gets punished for the crap he pulls."
p "His brother's the head of the school board, after all.{p=.1}He gets away with everything."
r "I assure you Phillip that those rumors floating around aren't necessarily true."

show phillip serious with dissolve
p "Really?"
p "Like how Dolores messed with the student contacts and made sure Sissel didn't receive mail from the academy?"
p "That's why Sissel didn't show up for the orientation on our first day."
p "And what about the time before that?"
p "Dolores pulled a bunch of strings to make sure Sissel didn't receive any scholarships or financial aid."
p "If it wasn't for Sissel's anonymous donor, he wouldn't even be in school right now."
p "After all this, did Dolores receive a single punishment? No."
p "Let's just face it.{p=.1}That rat's not going to face consequences unless he's caught red-handed at something {i}REALLY{/i} bad."

stop music fadeout 2

"A heavy silence hung in the room as Phillip heaved a long, drawn out exhale."
"Mr. Rokov seemed at a loss for words.{p=.1}I don't blame him."
"I don't think I've ever seen Phillip so........cross.{p=.1}He's usually so lighthearted."
r "..........{p=.3}Tell me Phillip, how do you know all of this?"
show phillip frown with dissolve
p "How?"
play music "wave-piano.wav" fadein 2 fadeout 2
show phillip tired shrug with dissolve
p "Hehe, I guess I'm a bit nosey."
show phillip tired smile with dissolve
p "Plus, Sissel's just a good guy trying to get his life back together.{p=.1}He doesn't deserve all this crap."
"Mr. Rokov glanced at his watch before returning to Phillip with a defeated sigh."
r "...Well, I believe we've discussed all we could here.{p=.1}I've kept you two here long enough."
r "Why don't you two go get some breakfast before the dining hall closes?"
"Changing the subject, huh?{p=.1}Despite my growling stomach, I feel a bit reluctant to leave."
"Phillip wasn't as hesitant.{p=.1}He was already halfway to the door."
r "Phillip?"
show phillip tired frown with dissolve
p "...What?"
r "I assure you that the staff and I will do our upmost to make sure justice is served."
p "...........Really?{p=.4}I hope so."
hide phillip with Dissolve(3.0)
"Mr. Rokov stared grimly at Phillip's retreating back until he disappeared from sight."
"After a while, he turned to me.{p=.1}His worried gaze made me slightly anxious."
r "[charname]."
m "Y-yes sir?"
r "Look after you friend for me, will you?"
r "Phillip's a responsible young man, but he's also known to cross the line for certain things."
r "I'm just afraid he'll do something........{w=.6}rash."
r "Make sure to be there for him if he does."
m ".....I'll do my best sir."

scene black with Dissolve(2.0)
play music "snowy-street.mp3" fadein 2 fadeout 2
scene dining hall with Dissolve(3.0)


"By the time we arrived at the dining hall, it was already packed with students massacring each other for tatter tots."
"Thankfully there were still some food left.{p=.3}Phillip and I grabbed all the eggs and toast we could carry and managed to snag an empty table."
"The moment we sat down I smacked my face into the table with an exhausted sigh."
"It's only morning, but things are already too heavy and tiring.{p=.3}Uuuugh what a day..."
"I felt a comforting pat my back and mumbled my thanks."
"Suddenly something freezing pressed against the back of my n-"
play sound "surprise.mp3"
m "{size=+10}-IT'S COLD AS FUCK!!!{/size}"

show phillip shrug smile at left with dissolve
show sissel neutral at right with dissolve

s "Wow, what a wimp."
show phillip neutral with dissolve
p "Pffft, you alright there [charname]?"

"Phillip passed me a glass of ice tea.{p=.3}I glared at it tiredly."
m "Good morning to you too I guess.{p=.3}Sissel, when did you get here?"
s "Phillip dragged me over while you were busy making out with the table."
m "Speaking of which {i}Phillip{/i}, there are better ways of waking me up besides pressing ice tea to my neck..."
show phillip shrug smile with dissolve
p "But you looked like you needed to {i}cool off{/i} a bit hehe~"
"Sissel and I collectively groaned."
s "Ugh it's too early for this shit."
show phillip neutral with dissolve
p "You're all a bunch of killjoys."
"I sighed and took a sip of my tea."
m "It should be illegal to be this cheerful in the morning-{p=.1}{size=+10}PFFFTTTTTTTSCCHHHHHHHHHH{/size}"
play sound "surprise.mp3"
"I spit my tea all over the table and formed a rainbow in the morning sun."
m "{i}This tea is even more bitter than my soul.{/i}{p=.3}Why the hell is it unsweetened?"
"Phillip nonchalantly took a bite of his toast as he opened up a newspaper."
p "Nonsense, sugar is bad for you."
m "You know Phillip, the more I get to know you the more you start sounding like an old man.{p=.3}A newspaper at this day and age?"
p "Hey, I didn't judge you for streaking in the morning a few days ago!"
m "That wasn't-!"
show phillip smile shrug with dissolve
p "Is that how flirting works nowadays? {w=.3}Wow Sissel, you better watch out!"
s "Hah, I'll keep an eye out for him."
m "How could you two be so mean to me? I thought we were friends!"
p "What else are friends for?"

stop music fadeout 4

show phillip neutral with dissolve
"Phillip continued scanning the newspaper with indifference while munching on toast."
"The little guy seems pretty relaxed now that he's out of the office.{p=.3}Who would have thought he'd switch moods so quickly?"
"I'm glad he's settled down though. It was weird seeing Phillip so...quietly furious."

"Sissel was buttering a bagel when someone caught his eye."
s "Hm? Phillip, what's on the front page?"

play music "black-cat.mp3" fadein 4 fadeout 3
show newspaper with Dissolve(3.0)
"I glanced over curiously. The front page showed a large photo of a creepy guy in a hood."

p "It says: \"The Black Cat Strikes Again!\"{p=.3}Apparently he vandalized a corrupt cop's home this time."
hide newspaper with Dissolve(2.0)

m "The Black Cat?"
s "You don't know the Black Cat?"
m "Never heard of him. Is he famous?"
s "Oh right, you're not from this side of town are you, [charname]?"
show poster 2 with Dissolve(2.0)
s "The Black Cat's sorta like a local hero around here."
show phillip frown
p "Hero?{w=.3} The guy's a criminal, Sissel."
play music "fragments.mp3" fadein 3 fadeout 3
s "Who cares? He'll always be a hero in my book!"
show poster with Dissolve(2.0)
s "Anyway [charname], the Black Cat is this guy who pops out the blue every now and then around here."
s "He's sorta like Banksy, but with a skateboard and cooler!{w=.3} And way more aggressive!"
s "He spray paints and vandalizes all houses of these assholes around the neighborhood and exposes them for the shit they do."
s "Sure what he's doing's illegal, but at least he's made some pretty big changes around here."
p "He kind of...{w=.3}sounds like an asshole himself if you really think about it."

hide poster with Dissolve(2.0)

s "Well yeah he does. But...{w=.3}the Black Cat's done a lot of great things for me."
p "L-like what?"
s "Well...this orphanage I used to live at...{p=.3}It's full of jackasses that starved the kids and never really paid attention to them."
s "It was pretty much full on Hunger Games in there if you wanted to stay half alive."
s "I ran away the first chance I could,{w=.3} but I always felt bad for leaving the younger ones back there..."
s "B-but then a few years ago the Black Cat just appeared out of the blue!"
s "He ransacked and painted the building full of words like \"MONSTERS\" and \"PRISON\"."
p "Oh, I think I remember this on the news a few years ago."
p "The West Orphanage Incident.{p=.3}His vandalism caught a lot of media attention."
p "There was a full-on public investigation of the place and it got shut down and reformed, right?"
s "Yeah! A bunch of the twats working there got arrested for child abuse and the city rebuilt the orphanage from the ground up."
s "Sure, I left before any of this happened but one of the kids I know from this orphanage is finally living a happy life thanks to the Black Cat!"
s "He even got to start elementary school a few years ago!"
s "I never even got that chance..."

"The air was heavy as Sissel quietly caught his breath."
show sissel embarrassed with dissolve
"He blinked as if suddenly realizing where he was and flushed red."
s "S-sorry, I rambled on a bit, didn't I?{p=.3}Sorry for ruining the mood."
show sissel neutral with dissolve
s "A-anyway! The Black Cat's a cool dude!{p=.3}You've gotta at least admit he's done some good things!"
play music "easy-lemon.mp3" fadein 4 fadeout 3
show phillip shrug smile with dissolve
p ".....Hehe, anyone who can outrun the cops on a skateboard sounds pretty cool to me."
m "So he's like Batman, but with spray paint? Sounds badass."
s "Sort of-?"
show phillip neutral with dissolve
p "I guess you could say he's...."
show phillip shrug smile with dissolve
p "{i}Catman?{/i}"

"Sissel and I groaned."
m "You're ruining the mood man."
s "Catman doesn't really,{w=.3} uh,{w=.3} roll off the tongue the same way..."
show phillip neutral with dissolve
p "Excuse me?{w=.3} What do you have against cats?!"
p "We're totally cool enough!"

s "Hey, I never said-!"

play sound "bell.wav" fadeout 3

m "{w=1}Welp, looks like it's time for class.{p=.3}Can we save the Cats vs Bats argument for later?"
"Phillip pouted into his toast while Sissel heartily agreed."
"As the three of us headed to class though, Phillip was back to his old grinning self.{p=.7}I sure hope it stays that way..."

scene black with Dissolve(3.0)
stop music fadeout 3
scene lecture hall with Dissolve(2.0)

"I was dreading our Creative Writing class. {p=.3}The thought of seeing Mr. Dolores again already gave me a headache."
"Hm, looks like he isn't here yet. Thank god."

play music "seven-off.mp3" fadein 2 fadeout 2
"As Phillip, Sissel and I plopped onto our seats (in the very back of the lecture hall),{w=.3} Mr. Rokov entered the classroom and approached us."
r "Good morning gentlemen. I hope you are well."
show phillip tired frown at left with dissolve
show sissel neutral at right with dissolve

m "Oh hey Vice Principal-"
p "Have you fired Dolores yet?"

r "I'm afraid I'm here for an entirely different reason."
p ".................................."
r "....erh, Sissel,{w=.3} could you join me in the office right now? {p=.3}There are some matters that require your presence."
s "Sure, I guess?{p=.3}What's it about?"
r "It's quite private. {p=.3}I will explain everything in the office."
hide sissel with Dissolve(2.0)
"Sissel shrugged and followed Mr. Rokov out of the lecture hall with mild confusion."
"I have a bad feeling about this....."
p "........Well I don't want sound pessimistic but...{w=.3}that didn't look too good."
m "Maybe they're trying to get Sissel's side of the story too?{p=.3}Like how they did with us this morning."
p "[charname], you have too much faith in this school system."
m "Or maybe you just have too little?"

"Phillip shrugged nonchalantly."
p "It's not like they've ever proven themselves otherwise-"
play music "easy-lemon.mp3" fadein 2 fadeout 2
play sound "surprise.mp3"
show owen neutral at right 
o "Yooooo cuties how's it going?"

"Owen leisurely plops down on the seat next to Phillip.{p=.3}He winks and lounges his arm around Phillip's shoulders like an arm rest."
"Phillip looked nonplussed."
o "Hm?{w=.3} Am I interrupting something?"
m "Well...."
show phillip shrug smile with dissolve
p "Besides people's personal space?{p=.3}Not at all! Welcome to class Owen."

show owen grin closed with dissolve
o "Daw c'mon little guy, I just missed ya.{p=.3}You're always up so early and come back to the dorm so late."
o "A little affection every now and then wouldn't hurt~"
"Owen leaned over and rested his head on top of Phillip's. {p=.3}He doesn't seem to notice the way Phillip was gritting his teeth with irritation."
show phillip neutral with dissolve
p "Sorry about that.{p=.3}I've had a lot of stuff to do."
o "But hey!{w=.3} At least now can get back to our \"roommate bonding\" amirite~?"
"He leans into Phillip's chair until their cheeks are almost rubbing together.{p=.3}Their whiskers were tickling each other from their close contact."
o "Let me know if you want me to do anything for ya, kiddo~"
o "{i}Anything at all~{/i} <3"

stop music fadeout 2
play music "black-cat.mp3" fadein 2 fadeout 2

show phillip irritated with Dissolve(2.0)

p "......................"
m "Uh Owen, you might want to back down a little."
o "Mm? What, you jealous [charname]-?"

"Phillip let out a feral hiss."
p "Can I have my chair back?"
show owen scratch with dissolve
o "O-oh right,{w=.3} sure..."
o "Why's everyone so grumpy all of a sudden?"
show owen grin closed with dissolve
o "Y'all need to let loose.{p=.3}Live a little, you know?"
p "...........where's the teacher?{p=.3}Isn't class supposed to start right now?"
show owen neutral
o "Ouch, now you're giving me the cold shoulder?{p=.3}You're breaking my heart, man."
"Owen inched a flirty hand onto Phillip's thigh with a wink."
o "I'm sure if you just open up a little more we'd get along fine-"

show phillip angry with Dissolve(2.0)
p ".........................{p=.3}......................................"

show owen scratch with dissolve
o "W-whoa, what's with that look?"
p "That's your hint to piss off, Owen."
p "Or is that not straight forward enough?"

o "Geez, I was just trying to be nice-"

play music "unlight.mp3" fadein 2
#phillip outburst
#owen shocked

p "Nice?{p=.3}{i}Nice?!{/i}"
p "Do you have any idea how much of a pain you've been in the last few days?!"
p "You have zero sense of boundaries.{p=.3}A damn pre-schooler knows how to behave better than you!"

o "I-I didn't think-"
p "You never do.{p=.3}It's a bit irritating actually."

p "I've told you again and again-"

show phillip shrug smile 

p "\"Oh hey Owen, back off a little please?\""
show phillip angry 
#phillip outburst
p "But no!{p=.3}Let's keep creeping up on me! I'm sure I'll like you more then!"
p "Am I just a new toy for you to play around with?{p=.3}Am I just someone for you to experiment and feel up?"
p "{i}Did you even bother to think of me as a person?!{/i}"

p "{i}{size=+10}Give me a fucking break.{/size}{/i}"

play music "black-cat.mp3" fadein 3

o "....................................................."
m "....................................................................."

#phillip surprised
p "........-!!"
show phillip sad with dissolve
p "...................{p=.3}I need some air."


hide phillip with Dissolve(3.0)
"Phillip shakily stood up and stumbled out of the room, as though he had the wind knocked out of him."
"The room was silent and all eyes were on Owen, who looked stunned in disbelief."
"I was shocked myself. {p=.3}But now's not the time to worry about that."

menu:
    "Follow Phillip":
        $ day4_item = "phillip"
        m "I'm going to go after Phillip.{p=.3}Will you alright on your own for a bit, Owen?"
        o "Y-yeah.{w=.3} Go ahead.{p=.7}I'll be fine."
           
        scene courtyard with Dissolve(3.0)
        "Huff.....{w=.3}Huff........."
        "Where is Phillip?{p=.3}I've ran several circles around campus already, but there's no sign of him."
        "He wasn't at his usual spot on the roof either. Where else could he be?"
         
        m "..................{w=.3}Echo!"
        play sound "ghost.mp3"
        show echo blurry with dissolve
          
        e "You called, [charname]?"
        m "Yeah.{p=.3}Echo, you always seem to know a little about what's going on."
        m "Care to do your usual ghostly magic and help me find Phillip?"
        e "Oh for the last time, I'm not a-"
        m "{i}I wish I knew where Phillip is.{/i}"
        e "-!!{p=.7}Haha....{w=.3}now you're getting it."
        e "He's not on campus anymore."
        e "There's a place in the forest by Bradley Lake...{p=.3}A place that Phillip goes to whenever he wishes to be alone."
        e "Think you can find it?"
           
        play sound "ghost.mp3"
        hide echo with Dissolve(2.0)
           
        m "You mean that rickety old cottage?{p=.5}...No,{w=.3} that doesn't sound right."
        m "That place is a bit too creepy to be comforting.{p=.3}Hm...."
        m "God dammit Echo, why do you have to be so cryptic?"
           
        scene lake road with Dissolve(2.0)
            
        m "Huff.....{w=.3}Huff.....{p=.3}Well here's Bradley Lake. {p=.3}There should be a place here where \"he wishes to be alone.\""
        m "Maybe there's-?"
        m ".....hm."
        m "Yesterday there was a fork in the road.{p=.3}When I took a right,{w=.3} I ended up at the creepy cottage.{p=.3}Maybe if I take a left...."
        
        scene wishing well with Dissolve(3.0)
            
        m "{w=.5}A wishing well in a place like this?"
        m "\"Wishing well.\"{p=.3}Oh Phillip, even your cryptic hints are puns- Ah!"
        show phillip sad with Dissolve(2.0)
        "Up ahead laid Phillip, curled up on the ground next to the well.{p=.3}His face was buried in his hands as he pulled at his hair in frustration."
        m "Phillip, are you{w=.3} ok?"
        p "[charname]?"
        p "{size=+5}{i}AAAaaaaaaaugh!!{/i}{/size}{p=.3}I shouldn't have snapped-"
        p "Ugh, is Owen alright?"
        m "He.....{w=.3}looked pretty shaken up when I left."
        
        "Phillip groaned into his hands, shaking his head vigorously."
        p "{i}I'm not that angry,{w=.3} honestly.{/i}"
        p "It's just....{w=.3} ugh."
        stop music fadeout 3
        "As Phillip tried to steady his breathing, I crawled next to him on the forest floor and patted his back comfortingly."
        "After a while, he heaved a long, painful sigh."
        play music "into-thin-air-slow.mp3" fadein 1
        
        show phillip serious with Dissolve(2.)
        p "Sorry about that.{w=.3} The whole yelling thing."
        p "I've just been so frustrated at everything going on around the here..."
        p "And I just sort of....snapped all of it onto Owen."
        p "He's a good guy.{w=.3} Just,{w=.3} {b}really{/b} damn irritating sometimes."
        show phillip sad with dissolve
        p "But he didn't deserve {i}that{/i},{w=.3} I suppose."
        
        "The edges of Phillip's eyes were red as he rested his head against the stone of the wishing well behind us."
        "I reached out a hand and gently ruffled his hair."
        m "You...{w=.3}weren't exactly wrong when you yelled at Owen.{p=.3}He {i}has{/i} been making you uncomfortable these last few days, hasn't he?"
        
        p "......just a little.{p=.3}That doesn't exactly justify exploding in his face, does it?"
        p "Sure he's been a bit annoying,{w=.3} but Owen's been so welcoming and kind to me too."
        p "He has been really nice to me too.{w=.3} And I kept brushing him off."
        "Phillip breathed a low laugh."
        p "How much do you wanna bet he hates me now?"
        
        m "Do you really think he's the type of guy to hold a grudge?"
        m "You just have to go back and sort things out with him."
        m "You've been a bit stressed with everything that's been going on, that's all."
        m "I'm sure Owen will understand. He doesn't hate you."
        
        show phillip serious with Dissolve(2.0)
        "There was a long silence before Phillip looked up from his hands."
        p "...........Should I though?"
        p "I've always been just really....{w=.3} angry, on the inside."
        p "And sometimes it just all pours out to someone around me,{w=.3} even if they don't deserve it."
        p "It'll probably happen again."
        show phillip sad with dissolve
        
        p "Owen's a....{w=.3} pretty good guy, overall."
        p "He's probably better off hanging around someone else."
           
           
        "I sighed and looked Phillip straight in the eyes."
        play music "carefree-tune.mp3" fadein 4
        show phillip frown with dissolve
        "With a sharp tug, I pulled both his cheeks up until his face was scrunched up into a weird chipmunk smile."
        
        p "{i}W-whaffmmmpphppppp??!!{/i}"
        m "Here we go!{p=.3}There's that good ol' Phillip smile we know and love!"
        p "PPPPPP-{p=.3}-PAH!"
        p "What the hell was that for?"
        
        m "Like Owen said earlier, you gotta let loose sometimes, kiddo~"
        "With my golden acting skills, I tried to imitate Owen's famous flirty wink."
        show phillip tired smile with Dissolve(2.0)
        p "...pffft,{w=.3} you really captured his charm."
        show phillip annoyed with dissolve
        p "Or lack thereof."
        m "Thanks~ {p=.3}My beauty is wasted on nobody~"
        
        stop music fadeout 5
        
        m "......in all seriousness though, you need to let things go, Phillip."
        play music "wave-piano.wav" fadein 3
        m "Worrying will get you nowhere.{p=.3}You just have to find the guts to go back and talk to him."
        m "Whatever happens,{w=.3} it's best to sort it out together and communicate,{w=.3} you know?"
        
        show phillip serious with dissolve
        p "................{p=.3}...You make it sound so easy......"
        m "I never said it would be easy.{p=.3}But it's the right thing to do after all, isn't it?"
        m "Phillip, you're a smart guy. I'm sure you'll reach a good conclusion eventually."
        m "I'll be rooting for you, kiddo~"
        
        p "Heh...{p=.3}I'll do my best."
        show phillip neutral with dissolve
        p "..........Thanks for coming all this way to cheer me up, [charname].{p=.3} I might have kept on skulking for hours if you didn't show up."
        
        m "It's been my pleasure~"
        m "By the way, why did you come to this spot?{p=.3}This wishing well looks kinda old."
        
        show phillip neutral with dissolve
        p "Oh this old thing?{p=.3}I guess you could say it's my...{w=3}happy place."
        p "I don't know why but every time I visit this little wishing well, I feel happier than I did before."
        p "It's almost like there's always someone here secretly cheering me up."
        m "Hm....weird."
        m "Oh!{p=.3}Speaking of places to be, we're basically skipping class right now, aren't we?"
        p "Whoops.{p=.3}Guess we better start heading back."
        p "There's a little shortcut down the road over there.{p=.3}You should head back first."
        p "I want to stay here just a little longer."
        
        m "If you say so..."
        p "If you see Owen, tell him I want to talk, ok?"
        m "Will do! {p=.3}Well, see you back in class Phillip!"
        p "Oh wait! Before you leave-"
        hide phillip with dissolve
        show jade coin with Dissolve(3.0)
        "Phillip dug around in his pocket before pulling out a faded, jade coin."
        p "U-um, I want you to have this [charname].{p=.3}As,{w=.3} you know,{w=.3} a thank you."
        p "It's not much, but I hope you like it."
        m "Wow, it's pretty.{p=.3}I can't take something valuable like this!"
        p "Pffft, are you kidding me? This is like a cheap trinket you can find anywhere."
        m "-aaaand my fascination's gone."
        hide jade coin with dissolve
        show phillip neutral with dissolve
        p "But they say it's good luck,{w=.3} so keep it, okay?"
        "I stuffed it into my pocket, where it left a comfortable weight against my leg."
        m "Thanks Phillip, I feel full of luck now.{p=.3}Time to buy a lottery ticket."
        p "Or get back to class before Mr. Dolores rips you a new anus."
        m "Shit! I better head back now.{p=.3}I'll see you soon Phillip!"
        p "See you around."
        
        hide phillip with Dissolve(3.0)
        "As I turn to leave this little clearing, the warm summer wind brushed up against me."
        "I glanced back towards the wishing well and felt my chest lurch a little."
        "What was this feeling?" 
    "Talk to Owen":
        $ day4_item = "owen"
        play music "drift.mp3" fadein 3 fadeout 3
        m "Owen....{w=.3}Are you alright?"
        
        "Owen blinked, still somewhat in a daze."
        o "Y-yeah, I'm fine."
        o "Just a little.....{w=.3}surprised, I guess."
        
        "People around the room were starting to murmur and gossip among themselves."
        "A spark of irritation bubbled in my chest."
        m "Owen, let's go for a walk. {p=.3}You look like you need some fresh air."
        "Owen's eyes stared off into the distance, looking past me."
        o "S-sure..."
        
        scene courtyard with Dissolve(3.0)
        
        "I dragged Owen outside and away from all the chatter and judging eyes."
        "He just stumbled along blindly behind me, still stunned from earlier."
        m "Owen, about earlier...{p=.3}Phillip was just plain harsh."
        m "You didn't deserve that kind of ridicule."
        show owen scratch with dissolve
        o "........................"
        show owen grin nervous with dissolve
        o "Heh.....{w=.3}heheh...."
        o "No, he was just being honest."
        o "It's not like he's wrong.{p=.3}I {i}have{/i} been a pain."
        o "I just never realized how much I was bothering him..."
        o "Hah.{p=.3}It's been a while since someone tried to set me right.{p=.3}It feels strange..."
        m "Feels strange?{p=.3}Back there, you looked like someone stabbed you with a butter knife."
        m "Are you sure you're alright after that?"
        show owen scratch with dissolve
        "Owen heaved a long sigh and hung his head."
        o "I'm.........{w=.3}well......"
        
        o "I've got no right to complain right now."
        o "Either way, I still need to apologize to Phillip.{p=.3}I've been a making life pretty difficult for him."
        o "Hah....{w=.3}I......."
        
        play music "drifting.mp3" fadein 5
        show owen grin nervous with Dissolve(2.0)
        o "I.......{w=.3}sure have a habit of fucking things up."
        "Owen caught sight of my concerned face and tried to keep up a firm smile."
        o "Hey no worries!{w=.3} I'm feeling fine,{w=.3} I should be the one apologizing and whatnot."
        o "B-better go and tell Phillip I'm sorry.{w=.3} He deserves better than this..."
        
        m "Owen,{w=.3} are you sure you're okay?"
        
        show owen grin 2 with dissolve
        o "Yup!{w=.3} Positive!"
        show owen grin 3 with dissolve
        o "I just messed up,{w=.3} that's all.{w=.3} Nothing new here..."
        show owen grin nervous with dissolve
        o "Now to go fix things up....{w=.3} again...."
        
        m "You know Owen.....{w=.3} it's okay to not feel alright sometimes."
        m "You don't have to bottle it all up."
        
        "Owen glanced at me silently before smiling again."
        "That smile's starting to feel awfully strained..."
        o "Are you trying to comfort me,{w=.3} [charname]?"
        show owen grin 2 with dissolve
        o "I'm fine!{w=.3} Stop worrying about me."
        show owen grin nervous with dissolve
        o "Phillip's the wounded party here,{w=.3} you probably should go talk to him instead."
        o "I gotta figure out a proper way to apologize..."
        
        m "But Owen,{w=.3} what about {i}you?{/i}"
        
        show owen neutral with dissolve
        "Owen blinked at me blankly."
        o "What about me?"
        o "Seriously [charname],{w=.3} I'll be fine."
        show owen grin closed with dissolve
        o "I'm always fine."
        
        
        show owen neutral with dissolve
        o "Thanks.....{w=.3} for worrying about me though."
        o "It's nice.{w=.3} I really appreciate it."
        
        m "Of course.{w=.3} Let me know if you ever need to talk."
        "That hollow smile can't keep fooling me, {w=.3}Owen...."
        
        show owen grin nervous with dissolve
        o "I still have to patch things up between me and Phillip though."
        o "C-could you maybe do me a favor and....{w=.5}let me know when he's cooled down a bit?"
        o "I want to at least let him know I'm sorry."
        m "Of course. I'll check up on him later and let you know."
        show owen grin closed with dissolve
        o "Thanks [charname].{p=.3}You're a real bro."
        
        "Owen pulled me into a tight, warm hug.{p=.3}With my face pressed against his chest, I can hear his heart beating rapidly."
        "Despite that grinning face,{w=.3} he's still pretty torn up inside..."
        "I hope I can get things to work between them again...."
        
        show owen neutral with dissolve
        o ".....um, it's probably best we head back inside, huh?"
        o "We did basically skip class."
        m "Ah, good point."
        m "Why don't you head back inside first? I'll go around and make sure Phillip's alright too."
        
        o "Sounds good.{p=.3}I'll see ya around."
        
        hide owen with Dissolve(2.0)
        
        "I let out a long sigh. Things just keep getting heavier around here."
        "As I turn to start my search, Owen calls out from behind me."
        
        show owen neutral with dissolve
        o "[charname]!"
        m "Y-yeah?"
        o "I know this isn't much in terms of thanks, but I want you to have this."
        hide owen with dissolve
        show crane with Dissolve(3.0)
        "Owen handed me a small origami paper crane."
        "Its folds and creases looked perfectly aligned, as if someone had put a lot of time and care into making it."
        hide crane with dissolve
        show owen scratch smile with dissolve
        o "My mum always said these things bring good luck.{p=.3}I figure you should have it eheh~"
        "I took the little orange crane and held it in my hands delicately."
        m "Did you make this yourself?"
        m "Hehe, who would have thought you'd have such a dainty little hobby."
        show owen grin 2 with dissolve
        o "I'll let you know that I'm the daintiest guy you'll ever meet."
        m "Thanks Owen,{w=.3} I'll take good care of it."
        show owen grin 3 with dissolve
        o "You better! It's a thousand years of bad luck if you loose it!"
        show owen neutral with dissolve
        o "Anyway, I'll see you back in class."
        o "Thanks again, for earlier, [charname]!"
        
        hide owen with Dissolve(2.0)
        
        "Owen was grinning as he left for class."
        "His retreating back looked a lot more optimistic in the morning sun..."
        

    

stop music 
scene black with Dissolve(3.0)
play music "easy-lemon.mp3" fadein 2 
scene courtyard with Dissolve(3.0)

#scene where you realize the remnant is gone
"I made my way towards the English building where the Creative Writing class stood, my mind cluttered with quiet thoughts."
"Problems just keep popping up today, don't they?"
"I wonder how Sissel is doing too. He's been at Mr. Rokov's office this whole time."
"Hopefully he hasn't run into any bad luck and drama like I have..."

stop music
play sound "ghost.mp3"
show echo blurry with dissolve

e "[charname]! {p=.3}We've got a problem!"
m "W-whoa, give me a warning before you pop up like that."

play music "seven-off.mp3" fadein 3

e "That corrupted wish from earlier!{p=.3}It's gone!"

"A hushed silence rang in my ears as I looked about the courtyard."
"There wasn't a single trace of the strange figure from this morning."
m "W-where could it have gone?{p=.3}Didn't you say it was too weak to move on its own?"
e "This is bad..."
m "W-well it's not like a thing with no arms can do much damage, right?"
e "Are you kidding? {w=.3}It's a wish, [charname]."
e "That thing can twist circumstances and bring disaster or fortune, just like me."
e "Hell, it's probably bringing misfortune with its presence alone."
e "I doubt it's a coincidence that problems have been popping up for you and your friends around the same time it showed up."
m "That corrupted wish is what's causing all of our problems?"
e "More like the problems are already there,{w=.3} and he's making them much worse."
e "Causing Phillip to feel more stressed....{w=.5} forcing Dolores to act more aggressive... {w=.3}encouraging the school faculty's apathy..."

m "Is there anything we can do to get rid of it?{p=.3}We can't have that thing walking around cursing people left and right!"
e "There's not much we {i}can{/i} do...."
e ".......................-!!"
e "[charname]! You better go find Sissel at Mr. Rokov's office."
e "We should at least make sure no other problems are popping up."
m "Got it."

hide echo with dissolve

"Without a second thought, I raced off towards the faculty office building."
"Please, {i}please{/i} be alright...."

    

scene black with Dissolve(3.0)    
play music "ultralounge.mp3" fadein 3
scene office with Dissolve(3.0)

"I snuck quietly through the halls of the office building and inched my way toward Rokov's room."
"As I turned the corner, I was shocked to find-"

#show phillip surprised
p "-[charname]?!"
m "Phillip?!{p=.3}What are you doing here-"

show phillip irritated with dissolve
p "{i}Shhhhhhhhh!{/i}{p=.3}They might hear you!"
"Phillip grabbed my shoulder and pulled me down low."
show phillip neutral with dissolve
p "Welp, looks like I wasn't the only one who was worried."
p "Now that you're here, we might as well be eavesdroppers together."
m "Sounds like a plan."
"Together, we crawled towards Mr. Rokov's office.{p=.3}The door was slightly cracked open, revealing voices inside."
"Phillip and I pressed our ears against the door, straining our ears."
"Sounds like several people were arguing loudly in there."

m "Wait, that voice sounds familiar."
show phillip irritated with dissolve
"Phillip hissed."
p "Dolores. {p=.3}I figured it was weird how he didn't show up to class earlier..."

hide phillip with dissolve
"The voices inside the office began rising in volume as their conversation got more aggressive."
stop music

d "-there's no question about it!{p=.3}This brat stole it!"
play music "unlight.mp3" fadein 3
"Another familiar voice cut in angrily."
s "What the hell are you even talking about?{p=.3}I literally have {i}nothing{/i} to do with this!"
s "You dragged me all the way here to accuse me of random shit out of the blue?!"   
c "{i}Language{/i}, {w=.3}Mr. Sissel."
c "However, I will have to agree with you."
c "Mr. Dolores, {w=.3} you really have no evidence that Mr. Sissel stole the academy funds besides your own words-"
"There was a sharp {i}\"ptfff!\"{/i}, as if Dolores just spat in Mrs. Corlisse's face."
"Sissel snarled and almost lunged at him, but was stopped by Mrs. Corlisse placing a hand on his shoulder."

"From outside the room, I blinked in confusion as the weight of the situation set in."
"Someone stole money from the school? And from the sound of it, a pretty large sum too."
"This sounds bad. {p=.3}If Dolores manages to pin this all on Sissel, there'd probably be severe legal action against him."

"Dolores was shouting again, his irritating voice dragging me out of my daze."
d "Who the hell needs evidence with a scumbag like him?{p=.3}Let's hurry up and lock him back in prison!"
d "This...{w=.3}{i}{b}rag{/b}{/i},{w=.3} is barely scraping by as it is."
d "Some students even reported seeing him sneak out last night."
d "Given his criminal background, is there really anyone else who would have the nerve to steal from the school's funding?"

"Mr. Rokov coughed hesitantly in the background."
r "Really, Dolores.{p=.3}That is just pure speculation."
r "Sissel has clearly turned a new leaf before I admitted him into Gerania Academy, and I have full confidence-"
d "-And now you're short \$10,000 dollars in funds.{p=.3}Great choice Rokov!"
d "I {i}told{/i} you that you should have rejected this sack of shit before-"

stop music
play sound "slam.wav"
"{size=+15}{i}{b}SLAM!!!!!{\i}{\b}"

show phillip angry with Dissolve(2.0)
"Everyone" "............................"
p "............................................"
s "Phillip?"
"The room was silent as Phillip quietly walked in, with me awkwardly behind him."
r ".....Erm,{w=.3} may I help you Phillip and [charname]?"
"Mr. Dolores sneered at us from the back of the office."
d "Eavesdropping on faculty meetings are you?"
d "Brat, if I were the principal at this wretched academy, I would have you expelled-"

show phillip shrug smile with dissolve
p "I apologize for eavesdropping! {w=.3}Really, I'm quite sorry!"
p "But really,{w=.3} you can hardly call it eavesdropping when half the campus can hear your shouting."
show phillip neutral with dissolve
p "Shall we expel all of them as well, {w=.3}Mr. Dolores?"
d "W-well, erm-"
r "That aside, Phillip, it was very rude and inappropriate of you to interrupt."
p "I asssure you it's for a good reason."
p "I may have an idea of who stole the funds,{w=.3} Mr. Rokov."

"Another silence echoed as everyone stared dumbfounded."
play music "close-to-you.mp3" fadein 3
r "W-what?!"
c "Mr. Phillip, {w=.3}is this true?"
d "Tch, {w=.3}that's just plain bluffing."

c "Any sort of lead would be most helpful.{p=.3}More helpful than wild accusations, at the very least."
c "I'd like to hear what Phillip has to say."

"Mrs. Corlisse gave us an affirming nod."
"I couldn't help but stare nervously towards Phillip. {p=.3}Did he really know something about this?"
"This is an actual crime.{p=.3}We can't half-ass our way with lies and bluffs."
"Phillip sent me a reassuring smile before taking a deep breath."

p "This morning, as I was coming to your office for my meeting with Mr. Rokov...."
p "I passed by Mr. Dolores' house at the edge of campus and noticed something strange."

r "Strange? {p=.3}In what way?"
"Eyes were trained on Mr. Dolores. who suddenly looked rather nervous."
p "There were huge red words spray-painted all across his walls."
p "Words like \"THIEF\",{w=.3} \"HYPOCRITE\",{w=.3} and \"SWINDLER.\""
show phillip neutral at left with Dissolve(.3)
show sissel neutral at right with Dissolve(.3)
s "He got marked by the Black Cat!"

d "T-those are just the lies of another criminal!{p=.3}I've been framed!"
d "Really,{w=.3} are we actually going to listen to the {i}Black Cat{/i} of all people?"
d "He's wanted by the police for Pete's sake! {p=.3}He could be the one who stole it for all we know!"

c "At the same time...{p=.3}The Black Cat's marks do have the history of being quite....{w=.3}accurate."
d "W-what are you saying?!"

p "Well, I think it'd be worth a shot to call campus security and have them check out your home."
d "B-but-!"
show phillip shrug smile with dissolve
p "Being the honorable type of teacher you are,{w=.3} Mr. Dolores, {w=.3}you should have nothing to hide~"
p "Security just has to make sure you don't have the money sitting in your house."
p "It'll be quite quick and painless if you aren't the thief."

show phillip neutral with dissolve
p "I don't see why you would refuse them, {w=.3}unless you really {i}are{/i} the-"
d "Alright alright fine!{p=.3}I'll do it!"
d "This is just a big waste of time."
d "Just make sure they don't mess up anything!"

"Everyone glanced over at Mr. Rokov expectantly."
"The Vice Principal blinked in stunned silence before reaching for the phone with a sigh."
r "Very well, I will call campus security and have them search Dolores' home."
r "Today certainly has taken the turn towards the unexpected....."

stop music fadeout 5
scene black with Dissolve(3.0)
scene office with Dissolve(2.0)

"We all waited silently in the office, tension hanging high."
"Sissel, Phillip and I sat in the corner and occasionally glancing at each other nervously."
"Will Phillip's claims actually throw suspicion off of Sissel?{p=.3}He could actually go to jail for this."
"This is quite the mess we've found ourselves in...."

play sound "phone.wav"

"{i}Riiiiiingggggg!{/i}"
"Everyone jumped as Mr. Rokov hesitantly picked up the phone."

r "Hello....?{p=.5}Yes....Really? Alright."
"Mr. Rokov hung up the phone and looked at Mr. Dolores grimly."
d "Well...?"
play music "seven-off.mp3" fadein 3
r "Well for one, your house is a mess of spray-painted words at the moment."
r "More importantly, they found all the school's cash funds stashed under your sofa, Dolores."
r "What do you have to say for yourself?"

d "W-WHAT?!{p=.3}I-I never stole the money! I swear!"
d "I'm being framed I tell you!"

"There was a knock at the door as campus security stormed in and surrounded Dolores."
"His face was beet-red with fury and indignation."
d "This is madness!{p=.3}You can't do this to me!"
r "If you have any explanations, I'd love to hear them."
r "In the meantime, {w=.3}Phillip and [charname], thank you for your help."
r "Please leave the office and allow us to deal with this."

s "What about me?"
r "Stay here Sissel, we may still need you."

"Phillip and I made our way to the door, looking back at Sissel nervously."
"Will things really be alright like this?"

scene black with Dissolve(2.0)
play music "wave-piano.wav" fadein 3
scene courtyard with Dissolve(3.0)

"We didn't say a word until we got outside."
"I finally let out a breath I didn't realize I was holding."

m "That was....{w=.3}interesting."
m "A lot happened in that short time...."
show phillip neutral with dissolve
p "Hey, least they caught thief, right?"
show phillip shrug smile with dissolve
p "Now we don't have to worry about Sissel being thrown in jail for something he didn't do!"
p "And Dolores is definitely getting fired for this,{w=.3} so he'll finally be out of our hair."
show phillip neutral with dissolve
p "He won't be able to hurt Sissel anymore.{p=.3}All's well that ends well I guess."
m "I'm glad that things got settled quickly,{w=.3} but something about this whole thing feels little off to me..."
p "Oh [charname], you're just overthinking it. {p=.3}It's pretty simple."
p "Dolores stole the money and tried to pin it on Sissel so that he could get away with it.{p}But instead he got caught red-handed."
p "Mystery solved!"

m "I suppose it's just karma at work."
p "Yup, beautiful karma...{p=.3}Hm?"

stop music fadeout 2
show phillip neutral at right with dissolve
show owen scratch at left with Dissolve(3.0)

"Owen was approaching us, his face grim."
"Phillip fidgeted nervously, but tried to keep a smiling face."
p "O-oh, hey Owen!{p=.3}Um....about earlier-"
play music "fragments.mp3" fadein 3
o "Heh, let's set that aside for now. {p=.3}There are more important things to talk about."
o "I overheard everything at the office."
o "Phillip, how could you?"
show phillip irritated with dissolve
p "What do you mean?"
"Owen sighed and scratched his head apprehensively."
o "......{w=.3}last night, you said you'd be studying on the roof."
o "But you didn't, did you?{p=.3}You snuck out and didn't come back until dawn."
"Something clicked in my mind as I stared from Owen to Phillip."
m "No way...{p=.3}Phillip, did you-?"
p "I don't know what you're talking about."
o "...........{w=.3}Alright, I'll put it plainly."
o "You stole the funds and framed Dolores, {w=.3}didn't you Phillip?"

show phillip shrug smile with dissolve
p "{w=.3}Really?"
p "Just because I snuck out doesn't mean I did it.{p}Sissel snuck out too. I don't see you questioning him."
p "Is this your way of getting even with me?"
o "Geez, do I look that petty?"
m "Phillip,{w=.3} you did show up at the meeting at a pretty convenient time..."
show phillip irritated with Dissolve(1.0)
p "Heh, even you [charname]?"
p "................{w=.3}fine fine, I admit it.{p}I was the one who stole the money and pinned it on Dolores."
p "But can you honestly say he doesn't deserve it?"

o "Deserve it? You're losing him his job!"
#show phillip furious
show phillip angry with dissolve
p "He was {i}{b}abusing{/b}{/i} his job!"
p "That prick attacked and sabotaged students! {w=.5}He practically {i}choked{/i} Sissel!"
p "Do you honestly think this guy {i}deserves his job?!{/i}"
p "I'm doing everyone a favor here!"
o "What you're doing makes you no different than Dolores!"
o "Phillip,{w=.3} do you realize you're breaking the law and ruining someone's life?"
stop music
p "{i}{b}What is the point of the law if it can't even protect the people who need it most?!{/b}{/i}"
p "{i}The last thing I want to hear is some stuck-up preaching from a rich and spoiled brat!{/i}"

play music "snowdrop.mp3" fadein 2 fadeout 2
"Owen blinks and his lips tremble for a moment."
"He stumbles a step back as Phillip continues to hiss heavily in rage."
".......{w=.3}W-what should I do here...?"

menu:
    "Side with Phillip":
        $ day4_side = "Phillip"
        "The heavy silence felt suffocating until I gingerly broke it with a stutter."
        m "I'd hate to say it Owen, but Phillip's got a point."
        m "I mean, look at the way Mr. Dolores has treated Sissel."
        m "It's kind of a relief to not have to worry about him hurting people."
        m "Sure, what Phillip did was......{w=.3}unethical."
        m "But nothing would have been fixed unless he did something about it."
        "Owen sighed and ran his hand tiredly through his hair."
        "He didn't look angry, only.....{w=.3}disappointed."
        o "Phillip's breaking the rules to deal with a rule-breaker."
        o "He's pretty much become a mini-Dolores,{w=.3} don't you think?"
        p "What?{p=.3}{i}I'm nothing like-{/i}"
        o "Really?"
        o "You're bitter, spiteful, and lash out at people you don't like.{p=.5}Sound familiar?"
        show phillip irritated with dissolve
        p "...................{p=.3}At least I'm trying to help someone."
        p "The system isn't going to do anything to fix the problem-"
        play music "drifting.mp3" fadein 2 fadeout 3
        show owen neutral with dissolve
        o "{i}Then change the system!{/i}"
        o "Your heart is in the right place Phillip, {w=.3}and you work harder than anyone to make things right."
        o "But don't you think it would be more fitting to change the rules for the better, {w=.3}instead of constantly breaking them in a fit of useless anger?"
        #show phillip sad
        p "I.....I........."
        show owen scratch smile with dissolve
    "Side with Owen":
        $ day4_side = "Owen"
        "The heavy silence felt suffocating until I gingerly broke it with a stutter."
        m "Phillip, I know you mean well but....{w=.3} Owen's right about this."
        "Owen looked up with a surprised, grateful smile."
        "Phillip shot me a poisonous glare instead.{p}I gulped audibly before continuing."
        m "I-I mean, shouldn't you leave it up to the school faculty to handle this mess?"
        m "You literally broke into Mr. Dolores' home and vandalized his property."
        m "And you even stole $10,000 just to frame him and throw him into jail."
        m "No matter the intention, what you did was just plain hypocritical and {i}wrong{/i}."
        show phillip irritated with dissolve
        "Phillip shoots me a wry but knowing smile."
        p "No more wrong that all the shit Dolores pulled."
        p "Do you know what would have happened if I left things the way they were?"
        #show phillip glare
        p "The school faculty would do nothing."
        p "Dolores would find a way to kick Sissel out of the academy he fought tooth-and-nail to get into."
        p "And finally Sissel will be thrown back into the streets to rot."
        #phillip closed grin
        p "................"
        #phillip open grin
        p "Hell will freeze over before I let the system completely fail someone like that again."
        o "...That's nothing but pessimistic presumptions."
        "Phillip scoffed and gritted his teeth."
        #phillip glare
        p "Presumptuous?{w=.3} No. {p}I've lived it."
        p "And I won't let it happen again."
        


show owen scratch smile with dissolve
"Owen sighed and shook his head tiredly."
o "Heh, nothing I say will make you change your mind, will it?"
p "....Doubtful."
o "........I see."

"Owen scratched his head thoughtfully and began to walk away, with Phillip staring after him curiously."

p "Where do you think you're going?"
o "Well, I guess I'm aiming for a middle ground here."
play music "drift.mp3" fadein 2
o "So I'm going to tell Rokov that I stole the money."
m "{i}What?!{/i} You can't!"
p "...What are you playing at?"
o "Out of everyone here, I'd probably get into the least trouble."
o "I'm Owen Lorelei after all.{p=.3}My father practically owns the school."
o "Not to mention how my family's a huge benefactor with the local police."
o "I'll just call my pops and ask for a few favors."
m "Won't he get angry though?"
show owen grin closed with dissolve
o "I'd be surprised if he even replies. But hey, he wouldn't leave me hanging."
show owen neutral with dissolve
o "He's got a family reputation to uphold, after all."
o "Can't let a outcast like me to ruin our good name hehe~"

"A hiss crawled from Phillip's throat."
p "You're taking the blow for something you didn't do."
o "And Mr. Dolores is getting arrested for a crime he didn't commit."
o "I don't really want to see you arrested either."
#owen resigned
o "So all in all,{w=.3} this is the best possible outcome."
hide owen with Dissolve(3.0)
"With a determined nod, Owen turned and made his way toward the office building."
"It never really occurred to me Owen was the son of a practically aristocratic family until now."
"His retreating back was held with a sense of esteem, almost knightly."

"Phillip groans besides me and buries his face in his hands."
p "....I've made quite a mess, haven't I?"
p "............{p}[charname], I'm going to...{w=.4}Fix this."
p "Could you do me a favor and distract Owen for a bit?{p=.4}Don't let him into the office building."

m "I'll do my best, but Phillip...{w=.4}Stay safe, ok?"
p "Not likely."
hide phillip with Dissolve(3.0)
"With that, he turns and sprints out of sight,{w=.4} leaving me alone in the courtyard."
"How did things come to this?"

scene black with Dissolve(3.0)
scene courtyard with Dissolve(2.0)

play music "close-to-you.mp3" fadein 2 fadeout 2
m "Owen!{w=.3} Wait up!"
show owen neutral with dissolve
o "Yo, [charname]."
o "You're not coming to stop me, are you?"
m "Well essentially, yes."
m "I can't just let a friend throw himself into the frier like this."
o "I'm just doing what I think is right."
o "Heh, did Phillip send you here to buy time-?"
"With a yell, I leapt at Owen and trapped his arms in a bear hug."
m "Yup.{p=.3}I'm not supposed to let you into the office."
"Owen laughed and tried to pat me on the head."
o "Nice try, [charname], I appreciate the concern."
o "But I've got to do this so nobody gets hurt."
m "But {i}you{/i} will get hurt."
show owen scratch smile with dissolve
o "...? {p}Since when did I matter?"
m "Huh-?"
"Before I could question him, Owen began marching toward the office."
"As tightly as I was hugging him, I ended up getting dragged along too."
m "Owen-"

stop music
play sound "glass-break.mp3"

"A crash suddenly rang out from inside the office building."
m "What was that?"
show owen scratch with dissolve
#owen serious
o "...oh no,{w=.3} he didn't."


scene office with Dissolve(2.0)



"Owen and I rushed inside. {p=.3}There was shouting and screaming from the other end of the building."
"What was going on-?"

play sound "slam.wav"
"Ooph!"

m "Ow, sorry about that-"
show black cat with Dissolve(3.0)
b "............................."
o "........{w=.3}Phillip?"
b "....................................................."

show black cat at Move((0.5, 0.5), (1.5, .5), .3,
              xanchor="center", yanchor="center")
"Suddenly more furious shouting and footsteps came barreling our way."
play music "black-vortex.mp3" fadein 2 fadeout 2
d "It was him! I saw it with my own two eyes!{p=.3}The Black Cat!"
d "I'm going to kill that little fucker-"
c "Dolores, calm yourself!"
m "What's going on here?"

show black cat at Move((0.0, .5), (1.5, .5), .5,
              xanchor="center", yanchor="center")
"Suddenly, the black hooded figure shot past us in the hallway, his skateboard whirling as he sped out the door."
"A small crowd of security officers chased after him in close pursuit."

"Behind us, Mr. Dolores came huffing and puffing with absolute fury."
d "I caught that criminal trying to steal the money they recovered from my house!"
d "It was him!{p=.3}The Black Cat!"
d "I {i}told{/i} you fools that I was being framed! {p=.3}Absolute garbage, the lot of you!"

show owen scratch with dissolve
o "The Black Cat?"
"Owen tugged at his hair in frustration and grumbled under his breath."
o "He didn't need to go that far!"
o "I could have fixed this!{p=.3}Now he's got a hoard of police chasing him."
o "Phillip...."
m "He...{w=.3}just didn't want you the take the blame for him-"
hide owen with dissolve

play sound "gunshot.wav"

d "He's getting away!"
c "Dolores, {i}is that a gun?!{/i}"
d "Oh calm your tats, woman. This is a tranquilizer."
d "There's no way in hell that I'm going to let that little shit get away from making a fool out of me."
c "Wait, stop-!"

"With that, Mr. Dolores stormed out the building, chasing after the Black Cat in a mad rampage."

play sound "ghost.mp3"
show echo neutral with Dissolve(2.0)

e "Isn't a tranquilizer of that grade used for elephants?"
e "If Phillip gets hit with one of those,{w=.3} he ain't waking up."

m "Echo!"
m "Can you chase after them and make sure not a single bullet hits its mark?"

play sound "echo-wish.wav"
show echo wish with dissolve
e "Can do, boss."
e "They're heading for the lake."
e "You better hurry up if you want to catch up to them."
hide echo with dissolve

"As Echo disappears, I heaved an exhausted sigh."
"Ugh, why can't things ever be easy?"
"I took a deep breath before making a mad dash towards the lake."

scene black with Dissolve(2.0)
scene lake road with Dissolve(3.0)

"Huff....huff....."
"I feel like I've been running forever..."
"Where are did they run off to?"

"Rapid gunshots echoed in the distance.{p=.3}The left!"


scene cottage with Dissolve(3.0)
stop music fadeout 3

"It's the creepy old cottage from before."
"For some reason, {w=.3}just being here sends a frigid chill down my spine..."
"Didn't even that ashy girl dislike this place too?"
"Abruptly,{w=.3} the nearby bushes rustle as someone steps out from the bramble."
 
show black cat with Dissolve(2.0)
b "{w=.4}Tch,{w=.3} wrong turn."
m "Phillip!"
play sound "falling-tree.wav"
"A crash rang out as Dolores came barreling out of the woods."
d "Huff...huff....{p=.3}Hah, finally caught you little shit!"

m "Hey! Leave him alone!"
"Before I knew it, Dolores was cornering the Black Cat against the cottage wall."
"Next to them, Echo laid on the ground in an exhausted heap."
hide black cat with dissolve

play sound "ghost.mp3"
show echo wish with Dissolve(2.0)
e "Ugh, [charname].{p=.3}Took you long enough."
e "I made sure all the bullets missed but ugh..."
"Echo shuttered and pants heavily, as if he was having trouble breathing."
"He looks so...{w=.3}faint at the edges,{w=.3} like an overexposed photograph."
hide echo with dissolve
play sound "gunshot.wav"
"Another missed shot."

"I gritted my teeth and roared at Dolores."
m "What is wrong with you?{p=.3}Have you gone insane?!"
m "You're shooting at a defenseless-"

d "SHUT YOUR TRAP!"
d "Arrogant brats like you need a beating to learn anything around here!"

play music "blue-feather.mp3"
"This guy...{p=.3}Why is he being so unreasonably aggressive?"
"What if...?"
"On a whim, I grab my camera and peered at Dolores through the lens."

show possessed1 with Dissolve(3.0)

"I swear I saw something-"
"No way.........."

play sound "wail.wav"
show possessed2 with Dissolve(3.0)
hide possessed1
"This is...{w=.3}the corrupt wish from earlier?!"
"No,{w=.3} this is just a faint shadow of it."
"Its maniacal grin is almost painful to look at."
"Is this what Echo meant when he said that the Remnant could affect the people around it?"
"It must be the reason why Dolores has been acting so irrational today-"
hide possessed2 with dissolve
play music "hitman.mp3"
"I snap back into reality as Dolores takes another shot at the Black Cat."


show black cat at Move((0.0, .5), (1.5, .5), .3,
              xanchor="center", yanchor="center")


"For someone who looks so fragile,{w=.3} Phillip's incredibly nimble on a skateboard."
show black cat at Move((1.5, .5),(-0.5, .5), .3,
              xanchor="center", yanchor="center")
"The Black Cat acrobatically darts around every which way, making aiming at him almost impossible."

d "Oh stay still you little-"
"Suddenly Dolores' face splits into a delirious grin."
"{w=.5}With a click, he swings over and points his gun at me."

b "!!!!"


show black cat at Move((1.5, 0.5), (.5, .5), .3,
              xanchor="center", yanchor="center")
stop music
pause(.3)
play sound "gunshot.wav"
scene black 
pause(2.0)

"I couldn't even register what was happening before another gunshot rang out."

scene cottage with dissolve
show black cat
b "...ugh......"
hide black cat with Dissolve(2.0)


"Phillip collapses into my arms, his breathing slowing rapidly."
"He felt limp, not moving an inch."

d "Haha, finally got him."
play music "hitman.mp3" fadein 2 fadeout 2
m "Wha-{p=.4}{size=+10}WHAT IS WRONG WITH YOU?!{/size}"

"Dolores spat on the ground and chuckled coarsely."
d "He's a {i}criminal{/i}, kid."
d "This hoodlum deserves what he got."

"With another {i}clank!{/i} of metal, he points his gun at my forehead."
d "Now hand him over if you don't want to join him."

"My heart was pounding like a hammer against my chest."
"What could I {i}even do{/i} in a situation like this?"
"Echo's too exhausted to help; I can't just leave Phillip here-"
"Maybe I could fight back-?"

menu:
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    "{b}It’s rude to fight on somebody else’s grave.{/b}":
        jump day4_bradley
    
    
label day4_bradley:
stop music 
play sound "ghost-song.mp3" fadein 1
"A low whispering wail suddenly echoed through the woods.{w=.3} A woman’s voice."
"It almost sounds as if it's coming from the earth itself."
"The sound threads its way through my chest like a heartrending song,{w=.3} almost taking my breath away."
"Dolores doesn't seem to notice it, as if he couldn't even hear the sound reverberating throughout the entire forest."
"The sickening grin on his face only widens as he pulls the trigger."

play sound "gunshot.wav"
scene black 
pause(3.0)


"I squeeze my eyes shut, but no pain comes."
"Hesitantly, I look up."

scene cottage with Dissolve(2.0)
play sound "ghost-wail.mp3"
show bradley with Dissolve(4.0)

"There was a woman standing in front of me,{w=.3} her hair dark as the lake under the night sky."
"The wind howls unnaturally around her.{p=.3}This isn't a normal person..."
"Could she be{w=.3} a wish?"

"Dolores stares through her, his eyes not registering her presence whatsoever."

d "What?! How did I miss?"

"The woman turns towards him dispassionately."
play sound "ghost-wail.mp3"
show bradley wish with dissolve

"Abruptly her eyes shone with an eerie, blue glow."
play music "hitman.mp3"
hide bradley with Dissolve(2.0)

"Almost at her command, hundreds upon hundreds of crows flocked out of the surrounding trees."
d "W-what is this?!"

play sound "crows.mp3"
"The mobs of crows surrounded Dolores in a blanket of black feathers."
"They pecked and clawed at every speck of flesh they could reach, with Dolores screaming and batting uselessly beneath them."
"Dolores's savaged cries of pain echoed through the forest as he writhed on the ground."

stop music fadeout 4
"After several long, painful minutes, the crows dispersed, {w=.3}leaving Dolores on the forest floor in a broken heap."
"I couldn't help but stare in shock."
"Is this what wishes are capable of?"

play music "blue-feather.mp3" 
show bradley with Dissolve(2.0)
"The woman turns towards us slowly, her hair swaying like ash in the wind."
"She reaches out a long,{w=.3} bony hand and brushed Phillip's unconscious head softly."
br "{size=-10}.................{w=.3}my debt is repaid.{/size}"
m "U-um,{w=.3} who exactly are you?"

"Underneath the mess of black hair, I swear I saw a small smile creep up."
stop music fadeout 3
play sound "ghost-song.mp3"
show bradley wish with dissolve

"Suddenly a wave of drowsiness hits me like a truck, sleep taking over me in seconds."
"The eerie song of the forest echoed through my head before I began slipping away from consciousness."
        
scene black with Dissolve(4.0)

pause(3.0)
"Someone was running their hand through my hair, gently massaging through the knots."
"It felt rather warm and comforting."
"With a groan, my eyes flutter open."
  
scene PO dorm with Dissolve(3.0)

"This is......{w=.3}a dorm room?"
"There was someone at my bedside.{p=.3}I rub my groggy eyes and tried to peer through the evening light."
play music "cafe-music.mp3" fadein 2
show owen neutral with dissolve
o "Oh [charname]!{w=.3} You're finally awake!"
o "How are you feeling?"
"I groan,{w=.3} the drowsy blanket of sleep still thick in my head."
"Peering to the side, I could see Phillip laying unconscious on the other bed."
m "...ugh....{p=.3}What happened?"
o "Campus security found you and Phillip passed out in the forest. {p=.3}You've been out cold all afternoon!"
o "Oh, {w=.3}and they found Dolores too."
show owen scratch smile with dissolve
o "He's pretty badly hurt from...{w=.3}...a freak bird attack?"
o "We have no idea what happened,{w=.3} but he's been arrested for shooting students and whatnot."
show owen neutral with dissolve

o "Looks like the school board can't protect him from something like {i}this{i}."
m "Haha...Phillip would probably be delighted."
m "Oh! Speaking of-{p=.3}Is Phillip doing alright?"
show owen grin nervous with dissolve
o "Philip's....eh...."

"Owen gestured towards Phillip's bed weakly."
o "Phillip's....{w=.3} alright in the long run.{p=.3}He woke up a little while ago actually!"
o "But that tranquilizer made him really sick. He kept throwing up and falling back asleep."
show owen grin closed with dissolve
o "Welp, I think we better count our blessings though.{p=.3}It's a medical miracle that he survived at all."
show owen neutral with dissolve

m "Whew, that's good to hear."
m "I really need to thank him for taking the hit for me..."
m "Wait, is Phillip going to be alright legally?"
m "He is, {w=.3}you know,{w=.3} the most wanted vandal in the city..."

"Owen grins and thrusts his chest out proudly."
o "Hehe,{w=.3} there's nothing to worry about."
o "I managed to pull a few strings with my family influence~"
show owen scratch with dissolve
o "Granted, my father never replied to my messages-"
show owen grin 2 with dissolve
o "But you'd be surprised how much influence I can get from regularly donating to {size=-10}(and sleeping with){/size} the local police~"
show owen neutral with dissolve
o "Officially,{w=.3} the Black Cat escaped and Dolores went gun-ho crazy after him,{w=.3} resulting in two innocent student victims."
o "Nobody beside you and me know the Black Cat's true identity."
o "Officers were supposed to come interrogate you two,{w=.3} but Sissel made a scene and drove them all away."
o "Something about \"Give those two a fucking break they just got fucking shot!\""
m "Heheh, let him know I said thanks.{p=.3}I could use a break after all that happened."

stop music fadeout 3

"Owen was quiet for a while, staring between me and Phillip, {w=.3}who was still unconscious in the other bed."
o "......................"
show owen sad with dissolve
o "*sigh*{w=.3} I should have gotten to the office sooner."
o "If only I took the blame more quickly-"

"A grumble sounded from the other bed as Phillip shook himself awake."
p "I swear to god if you took the blame, {w=.3}I would have strangled you."
show owen neutral with dissolve
o "Oh Phillip you're awake-!"

play music "easy-lemon.mp3" fadein 2

"There was a strangled gurgle as Phillip suddenly leapt out of the room and hurtled himself towards the bathroom."
"Sickly vomit sounds could be heard down the hall."

show owen scratch smile with dissolve
o "Ooh, that sounds bad."
o "He's probably going to feel like that for the next few days."

show owen neutral at left with dissolve
show phillip irritated at right with dissolve

"After a bit, Phillip stumbled back into the room and collapsed onto the bed."
p "Uugh.....{w=.3}my head feels like it's splitting in half...."
m "Phillip....{w=.3}I don't think I thanked you yet for taking the hit for me-"
p "It's a given."
p "I'm not letting a friend take the fall for something I'm responsible for."

p "That includes you, {w=.3}Owen.{p=.3}Don't be a dumbass."
stop music fadeout 3 

show owen scratch smile with dissolve
o "O-oh! {w=.3}We're still....{w=.3}friends?"
"Phillip was fidgeting again before releasing a long, tired sigh."

show phillip sad with dissolve
p "Um.... I.........."
play music "phillip-theme-slow.mp3" fadein 3
p "Owen, I....{w=.3}I'm sorry for everything I said this morning."
p "You're a really nice guy.{p=.3}I've just been really frustrated these last few days and snapped all of it onto you..."
p "It was a bit unfair to you and um....{w=.3}I'm not sure what else to say other than I'm sorry."

show owen grin closed with dissolve
"Owen chuckles and gives Phillip his usual grin."
o "You're still worried about that?{p=.3}Don't worry about it Phillip,{w=.3} you've got nothing to be sorry for."
show owen scratch smile with dissolve
o "Heck, I've got a lot to apologize for too."
o "All that flirting and groping I did probably got annoying after a while. Sorry about that."
show owen scratch smile with dissolve
o "I guess I just...{w=.3}got really excited."
o "I've just been a little.....{w=.3}lonely, you know?"
show owen neutral with dissolve
o "B-but I hope you stick around though!{w=.3} If that's alright with you."
p "............."
show phillip neutral with dissolve
p "Heheh,{w=.3} of course."
show owen scratch smile with dissolve
o "U-um,{w=.3} I'd like to give you a hug now, if that's alright...?"
show phillip shrug blush with dissolve
p "I might throw up on you,{w=.3} but sure."


"I stare at the two of them and couldn't help but chuckle to myself."
"Looks like they're both going to be fine."

m "Welp, I'll head back to my room before things get too mushy here."
m "Good luck with your roommate bonding!"

p "H-hey, it's not like that!"

"I laugh as I stride out of the room, narrowly dodging a thrown sock."

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

jump day5
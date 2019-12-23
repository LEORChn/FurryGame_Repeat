label day9_sissel:
$ persistent.current_route = "default"
play music "lullaby-guitar.mp3" fadein 2 fadeout 2
"My thoughts instantly went to Sissel."
"He acts tough and angry,{w=.3} but there's a vulnerable side to him that I just can't ignore."
"It's decided then.{w=.3} I'll be there for Sissel."

"Speaking of which,{w=.3} where was the guy?"
"I can't \"be there for him\" if I can't even find him."
"Time to go search."

scene black with Dissolve(2.0)
scene courtyard with Dissolve(2.0)

"About half an hour crawled by before I remembered something vitally important."
"My sense of direction {i}sucks utter ass.{/i}{w=.3} In the bad way."
"Curse my incompetence!{w=.3} How the hell am I going to find Sissel?"
"I guess I could just call him.{w=.3} But what would I say?"

"\"Hey man where are you?\""
"\"Oh nothing, I just crave your warm embrace wanna spend the rest of the day stuck to you like a baby koala.\""
"That'll work out."

"???" "What's this about baby koalas?"

show jinny neutral with dissolve
"I leaped up to find Jinny staring at me like I grew a second head."
m "Jinny! {w=.3}What are you doing here?!"

j "I was about to ask you the same thing."
j "Why were you mumbling to yourself and wandering around the courtyard like a lost puppy?"

m "I was looking for Sissel actually.{w=.3} You got any idea where he is?"
j "Aaaw, {w=.3}is it because you \"crave his warm embrace?\""
m "Shit, you heard that?!"
j "It was hard not to.{w=.3} You mumble {i}pretty{/i} loudly."

j "Anywho,{w=.3} Sis is probably in the office signing up for the contest tomorrow."
m "Contest?{w=.3} What contest?"


j "You don't know?{w=.3} Sissel's participating in Gerania's Culinary Arts contest."
j "It's half the reason why he's even studying at here."
j "The winner of the contest receives a massive scholarship and tons of offers from culinary colleges around the country."

m "Wow,{w=.3} I didn't know he was so passionate about baking."

"Jinny chewed on her index finger while lost in thought."
j "This could be his biggest chance to get accepted into a decent college too."
j "A lot is weighing on this contest...."
j "So you better show up to cheer him on in the preliminary rounds tomorrow!"
j "Sis needs all the support he can get!"

m "Can do.{w=.3} As a matter of fact, I'm going to find him right now."
m "Thanks for the tip Jinny!"

j "Pfft, good luck to you too."
"She waved her arms in a goofy hugging motion."
j "Feel the koala.{p=.3}{i}{b}Be{/b} the koala.{/i}"
"I promptly left before my humiliation crippled me further."

scene black with Dissolve(2.0)
play music "snowy-street.mp3" fadein 3
scene office with Dissolve(2.0)

"The office was mostly empty at this hour."
"Most of the teachers have scrambled home as soon as their shift ended."
"As expected,{w=.3} Mrs. Corlisse was the exception."

"I found her and Sissel wading through a pile of paperwork in the corner of the office."

c "-now you'll want to sign here, Mr. Sissel, to allow scholarship offers to be mailed to you-"
s "Right here?"
c "Yes." 
"Mrs. Corlisse gave a hearty chuckle as she shuffled the papers about."
c "I remember like it was yesterday when you climbed through my granddaughter's window and begged her to teach you how to read."
s "Yeah.{w=.3} Then you chased me out with a broom."
c "But you came back!{w=.3} And look how fair you've gotten since then."
c "If you manage to make a good impression in this contest,{w=.3} I'm sure you'll catch the attention of many recruiters."

s "I'm not sure how a homeless kid dressed in rags is going to make a \"good impression.\""
c "Sissel,{w=.3} you don't give yourself enough credit."
c "It's a good thing that your friends are here to provide support-"
c "Even if they are particularly nosy and have yet learned the ancient art of knocking on doors."
c "{i}Isn't that right,{w=.3} [charname]?{/i}"

"I jumped and stumbled inside the office awkwardly."
m "Oh hiiiiiiii,{w=.3} I was just, um,{w=.3} seeing how Sissel's doing and whatnot-"


show sissel neutral with dissolve
s "[charname]?"
s "What are you doing here?"
m "I-{p=.3}-Um."

$ sissel_truth = renpy.input("\"There's something I want to tell you.\"")
$ sissel_truth = sissel_truth.strip("")

if not sissel_truth:
    $ sissel_truth = "none"

"Static buzzed through my mind as my brain activity suddenly flatlined."
m "Oh nothing,{w=.3} I just craved your warm embrace wanna spend the rest of the day stuck to you like a baby koala."

show sissel wtf blush with dissolve
s "......{w=.3}are you.......{w=.3}high right now?"
m "-ANYWAY!!"

"My voice pitched several octaves higher as I tried to change the subject."
m "So what's this contest all about?"
show sissel neutral with dissolve
s "Well it's pretty much a baking contest with fancy themes."
s "I bake a thing and try to impress a few judges.{w=.3} And then I get judged."
play music "somber.mp3" fadein 3 fadeout 3
s "And probably fail."

c "Sissel,{w=.3} we discussed this already."
c "Keep your chin up,{w=.3} and self esteem even higher."
c "This self-deprication isn't good for your health."

s "But just look at me!"
s "I'm a raggity kid who hasn't even completed pre-school!" 
s "And I'll be competing against rich ass kids who are coming from around the country!"
s "How am I suppose to even {i}compare{/i}?"

"I placed a comforting hand on Sissel's shoulder,{w=.3} and he relaxed somewhat."
m "C'mon Sissel, {w=.3}you'll do fine."
m "Don't let the pre-performance anxiety get to you."
s "Hff, easier said than done."
stop music fadeout 3

hide sissel with dissolve

"Mrs. Corlisse tapped her chin thoughtfully as she peered across the office walls."
c "Do not think this is impossible, Sissel.{w=.3} You're not the first one to face such odds."
s "What do you mean?"
c "I remember a constest winner about 20 years ago with a similar background to you."
c "She was a student of mine, actually."
"She pointed at a dusty golden trophy hidden away on a top bookshelf."
c "[charname],{w=.3} be a dear and grab that for me, will you?"
"I mumbled reluctantly as I crawled onto a chair."
m "Sure,{w=.3} tell the clumsy one to climb up there.{p=.3}Real nice plan."

"I stood on my toes and strained my arms to try and grab the dusty trophy."

play sound "door.mp3"
m "-ACK!!"

play sound "slam.wav"

"......"

play music "wacky.mp3" fadein 3 fadeout 3
"Good news:{w=.3} I got the trophy."
"Bad news:{w=.3} I fell."

"More good news:{w=.3} I fell on something soft and surprisingly comfortable."
"Even more bad news:{w=.3} That very soft something was Sissel."

show sissel wtf with dissolve

s "Y-you mind getting off of me?"
m "R-right,{w=.3} just let me-"
m "Oh."

show sissel wtf blush with dissolve
"Other good news:{w=.3} I'm straddling his hips."
"Really bad news:{w=.3} Mr. Corlisse was watching with an exasperated \"Kids these days...\" plastered across her face."

c "I'll just.......{w=.3}take the trophy while you and Sissel......{w=.3}untangle yourselves."

"Sissel and I awkwardly scrambled apart, {w=.3}both red in the face as Mrs. Corlisse dusted off the trophy."
m "S-sorry about that."
show sissel embarrassed with dissolve
s "D-don't worry about it."
"I noticed Sissel not-so-subtlely adjusting his pants."
s "{size=-10}I hope he didn't feel that...{/size}"
m "What was that?"
s "N-nothing!{w=.3} It was nothing!"
m "Heh,{w=.3} maybe should try falling on you more often."
show sissel shocked blush with dissolve
s "W-w-what are you s-saying-?"

"Mrs. Corlisse suddenly cleared her throat loudly."
c "Are you boys done?"
show sissel embarrassed with dissolve
"Sissel and [charname]" "Y-yeah!"

stop music fadeout 3 
hide sissel with dissolve
"Mrs. Corlisse inhaled deeply as if to gather all her remaining patience."
"The two of us shuffled apart awkwardly as she set the trophy on her desk."



"It was in the shape of a regal-looking cup,{w=.3} with golden swirls and arches flowing off the edge."
play music "little-dark.mp3" fadein 3 fadeout 3
"A name was enscribed at the bottom,{w=.3} written in proud gold lettering:"
"\"{i}Gerania Culinary Arts Mastery Winner:{p=.3}{b}Celia Bradley{/b}{/i}"

show sissel neutral with dissolve
"Sissel eyed the name with a weird look."

s "....\"Bradley.\"{p=.3} Like the lake?"
"Mrs. Corlisse chuckled as she wiped off the trophy fondly."
c "Yes,{w=.3} she grew up in the woods near Bradley Lake,{w=.3} just like you."
c "Her parents were rather......{w=.3}dangerous.{w=.3} Home life was practically unliveable for her."
c "So young Celia ran away from home and single-handedly built a small cottage by Bradley Lake."
c "Later on, {w=.3}she changed her surname to \"Bradley,\" to match her new home."

c "All the while, {w=.3}she continued with her studies while working several jobs."
c "Sound familiar?"

s ".......................{w=.3}did she really win?"
stop music fadeout 2
"Mrs. Corlisse smiled with a sparkle in her eye."

play music "hyperfun.mp3" fadein 2
show sissel wtf with dissolve
"She suddenly leapt onto the desk and shook the trophy high above her head in a victory-drunk haze."
c "Celia did more than win,{w=.3} she wiped the floor with the competition!"
c "That's my favorite student for ya!"
c "Her work made everyone else's look like utter garbage!"
c "She {i}destroyed{/i} the other contestants and crushed their dreams!{w=.3} They all scrambled home in shameful tears!"
c "The judges were on their knees,{w=.3} {i}bowing{/i} to her in reverence and respect!"
c "{i}Celia Bradley,{w=.3} my very own student,{w=.3} became a {b}legend!{/b}{/i}"

stop music fadeout 3

s "....................................."
m "...................................................."
m "*whispers*{w=.3} Old folks sure like to exagerate their stories, huh?"

play music "cafe-music.mp3" fadein 3
"Mrs. Corlisse cleared her throat loudly and placed the trophy onto her desk."
c "The {i}point{/i} is that Sissel shouldn't worry about his personal history or background."
c "You only need to put in your best effort, and create something you can be proud of."
c "That's what my dear Celia did."

show sissel neutral with dissolve
s "...Heh,{w=.3} thanks Mrs. Corlisse."
s "That helped.{w=.3} I think."

"Sissel picked up Celia's trophy and gazed at it optimistically."
"There was a sense of recogniton and kinship in his eyes as he thumbed over the gold-encrusted \"Bradley.\""


scene black with Dissolve(3.0)
play music "calm-guitar.mp3"
scene courtyard with Dissolve(2.0)

"After filling out all the contest forms,{w=.3} Sissel and I strolled leisurely through the courtyard."
"The sun hung low in the sky when Sissel looked up from the paperwork in his hands."

show sissel neutral with dissolve
s "Say [charname],{w=.3} you never actually answered my question."
m "Hm?"
s "Why were you looking for me in the office earlier?{w=.3} Did you need something?"
"I cringed at the memory of my koala shtick from earlier."
"My arm hung around Sissel's shoulder amicably as I tried to laugh it off."
m "Can't a guy just hang out with his friends without being questioned?"
s "Sure, but you were acting weird and suspicious."

m "Well a friendly ghost told me that you needed my love and support today."
m "So I quickly raced over like the great friend I am.{w=.3} You should be grateful!"
"Sissel's eyebrow perked up suspiciously,{w=.3} but then turned away with a small smile."
s "You're a weird kid,{w=.3} you know that?"

s "If you're so free today,{w=.3} why don't you come over to the cafe and have a look at my contest entry?"
s "It's almost done,{w=.3} and I could use a few outside opinions."
s "You can even eat some of the leftover chocolate if you-"

show sissel wtf with dissolve
"My grip on Sissel instantly tightened as I pressed my face close with an intense glare."
m "Did you just say......{w=.3}chocolate?"
s "Y-yes?"
m "Take me."
m "My body is ready."
show sissel wtf blush with dissolve
s "Fine!{w=.3} Just let go of me!"

scene black with Dissolve(2.0)
scene cafe front with Dissolve(2.0)

"It took only a fifteen minute walk to arrive at the cafe."
"During the whole walk, Sissel's eyes darted between me and the ground with nervous excitement."
"I guess it's still unnerving for him to show his work to people,{w=.3} even if he's trying hard to hide it."

m "So what is your contest entry exactly?"
show sissel neutral with dissolve
s "You'll see!"
s "I-it's not too impressive at the moment,{w=.3} but I've put a lot of work into it."
s "Our entries have to follow a theme for each round of the contest."
s "Tomorrow's the preliminary round,{w=.3} with the theme \"History.\""
"I wrinkled my nose like I smelled something unsettling."
m "That's a pretty lame theme."
s "Pfft,{w=.3} tell me about it."
s "It took me and Teach almost a whole week just to come up with an idea for it-"

"The kitchen doors suddenly flew open to reveal a tall and jolly man sporting a welcoming grin."
show sissel neutral at left with dissolve
show hershel at right with dissolve
h "Well what do ya know,{w=.3} here comes ma favorite employee!"
h "Ya here to work on yer contest entry,{w=.3} Sissy?"
"Sissel groaned,{w=.3} his cheeks pink as he made his way behind the counter."
s "I'm your only employee,{w=.3} Boss."
s "And stop calling me that."
h "Don't matter none,{w=.3} still makes ya my fave."

"Hershel laughed and ruffled Sissel's hair amicably."
"He suddenly caught sight of me and gave an exaggerated gasp."

h "What's this?!{w=.3} Sissy,{w=.3} did you finally bring home a man?!{w=.3}"
show sissel embarrassed with dissolve
"Heat instantly flared up in both of our faces."
m "Oh um, {w=.3}we're not-"
s "Goddamnit Boss,{w=.3} stop embarrassing every friend I bring over!"
h "'Tis my job.{w=.3} Gotta make sure yer hangin' out with the fun folks."

show sissel neutral with dissolve
s "Ugh, {w=.3}whatever."
s "[charname],{w=.3} wait here for a bit.{w=.3} Boss and I are gonna get things set up before showing you my little project."
h "Aaaw,{w=.3} lil Sissel is excited!"
show sissel embarrassed with dissolve
s "Just shut up and help me take the project out of the fridge."

hide sissel with dissolve
hide hershel with dissolve
"I had to stifle a laugh as the two of them disappeared through the kitchen doors."
"It's rather amusing to see someone else giving Sissel so much grief.{w=.3} Those two are quite the pair."
"While I waited,{w=.3} I pulled out an empty chair and took in the view of cafe's interior."

"The place was humble and small,{w=.3} but the air was warm with the smell of pastries."
"It's a pretty cozy place to hang out.{w=.3} Makes me wonder why I don't come here more often."

"My thoughts were interrupted by the sound of the front doors swinging open."

show jinny neutral with dissolve
j "Oh hey there [charname].{w=.3} Did Sissel invite you to see his project too?"
m "Y-yeah,{w=.3} I didn't know you invited you too."

j "Well of course.{w=.3} Sissel and I have known each other since we were little beans."
j "I'm more surprised he'd bring you along.{w=.3} He's usually pretty self-conscious about his work."

"My chest fluttered a bit.{w=.3} I guess Sissel was pretty comfortable around me."
m "Makes me wonder what this project is.{w=.3} Sissel mentioned something about taking it out of the fridge..."

stop music fadeout 3

"Jinny suddenly grinned with an evil glint in her eye."
play music "scheming.mp3" fadein 2
j "You mean you didn't know?"
j "Sissel lured you here."
j "Hershel needs to consume the bodies of the young to try and heal his hideous bald spot."
m "He has a bald spot?!"
j "That's my theory at least."
j "Why else would he wear a bandana all the time?"
j "Anyway, back to the point."
j "{i}Dead bodies.{w=.3} Fridge.{/i}"
j "C'mon dude,{w=.3} act scared or at least intrigued."

"I scoffed and crossed my arms."
m "You're a pretty bad liar.{w=.3} Stop trying to mess with me."
"Jinny grinned ominously and jabbed her thumb towards the kitchen."
j "You can go check it out yourself if you don't believe me."

m "Challenge accepted!"
j "Wow, you agreed that easily?"
j "If you were in a horror movie,{w=.3} you'd be the first to die."
"I perked my chin up defiantly as I march into the kitchen."
m "But it's {i}not{/i} a horror movie and Sissel's probably just making something delicious and chocolatey for the contest."
"Jinny shook her head woefully."
j "Spoken like a true victim."

scene black with Dissolve(2.0)
scene cafe kitchen with Dissolve(2.0)

"The first thing I noticed upon entering the kitchen was a loud mechanical grinding noise coming from the walk-in fridge."
m "I wonder what all the racket is..."
show jinny neutral with dissolve
j "It's probably just Hershel sawing his victims into manageable,{w=.3} bite-sized pieces."
m "Or {i}maybe{/i} it's just Hershel using a blender or something."
j "Oh you're right!{w=.3} His victims are probably more consumable in liquid form."
m "Goddamnit Jinny,{w=.3} stop trying to freak me out."
j "Hey I'm just trying to be a responsible citizen and give you a fair warning."
j "Don't be surprised when Hershel suddenly jumps out at you with a chainsaw."
m "{i}Riiiiiiight,{/i}{w=.3} and the cafe's suddenly going to combust into satanic flames too.{p=.3}Get real-"

stop music
scene black
play sound "slam.wav"

"The walk-in fridge's doors suddenly flew open."

play music "batty.mp3"

show hershel_chainsaw with dissolve
pause(2)
"My high-pitched scream shook the cafe as I tumbled onto the floor like a crippled infant."

"I flailed my legs blindly as I scrambled to get away from Hershel and his fucking chainsaw-"
"My heart was ready to leap out of my throat-"
"{w=.3}-but then I noticed Jinny and Hershel laughing hysterically and exchanging a triumphant high-five."
scene cafe kitchen with dissolve

"Realization slowly sunk in."
m "{size=+10}{i}YOU TWO ARE TOTAL DICKS!!!{/i}{/size}"
"Jinny was wheezing and steadying herself on a table."
show jinny neutral at left with dissolve
show hershel at right with dissolve
j "Oh my {i}god,{/i}{w=.3} you should have seen your face!"
h "No need to thank us.{w=.3} Seeing ya almost shit yerself is its own reward."

"The fridge doors suddenly flew open again to reveal an exasperated Sissel."
show jinny neutral at farleft with dissolve
show hershel at farright with dissolve
show sissel wtf with dissolve
s "God damnit you guys,{w=.3} stop messing with every friend I invite over!"

h "Daw Sis,{w=.3} you ain't no fun anymore."
j "Hershel's right.{w=.3} How else are we going to check if he's boyfriend-worthy material?"

show sissel wtf blush with dissolve
s "{size=+10}{i}I told you not to mention that!{/i}{/size}"
h "Funny!{w=.3} Cuz you wouldn't shut up about [charname] whenever you came back from school-"

play sound "slam.wav"
hide hershel 
hide jinny 

"Sissel grabbed a nearby muffin and shoved it down Hershel's throat."
"He turned to me with a face as red as the sun."
show sissel wtf blush at Position(xpos = .5, xanchor=.5, ypos=.6, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
        
s "{i}{b}You heard nothing.{w=.3} You got that?{p=.3}Nothing.{/b}{/i}"
m "S-sure...?"
show sissel wtf blush at center with dissolve:
            xzoom 1 yzoom 1
            
s "Aaaanyway!{w=.3} I still gotta show you my contest entry!"
hide sissel with dissolve
"Sissel ran back into the walk-in fridge,{w=.3} face still burning red."

play music "peace.mp3" fadein 4
show jinny neutral at left with dissolve
show hershel at right with dissolve

"Jinny was still recovering from a mad laughing fit behind me as Hershel struggled to swallow his muffin."
j "Ah,{w=.3} messing with Sis has never been more fun."
j "You really need to hang out with us more often [charname]."

m "You two are gonna be the death of him one of these days."
"Hershel snorted as he wiped his mouth."
h "Daaaaw it ain't nothin' to worry about."
h "We're practically the kid's family,{w=.3} 'tis our job to take a jab at him every now and again."
j "Or every chance we get."
h "Yup."

"The two exchanged another triumphant high-five."
"The three of us looked up as the sound of a metal cart echoed out of the fridge."

"Jinny bounded over to me and elbowed my sides excitedly."
j "Alrighty,{w=.3} Sissel's about to show off his project."
j "Be as supportive as you can [charname]!"
show hershel frown with dissolve
"Hershel cracked his knuckles threateningly."
h "Or else."
j "Sshhhh! {w=.3}Here he comes!"
hide jinny with dissolve
hide hershel with dissolve
stop music fadeout 5

"The creeking of the metal cart grew louder as Sissel finally came out of the fridge."
show sissel embarrassed with dissolve
s "A-alright,{w=.3} h-here's my project!"
"I stared in amazement as the object slowly came into view."
m "Is that....?"

play music "little-dark.mp3" fadein 2
show chocolate_sculpture with Dissolve(2.0)
pause(2)
"...chocolate?"
"Sissel puffed his chest out in nervous pride."
s "Yup! {w=.3}A solid, white chocolate sculpture!"
"I stared at the sculpture in awe."
"It was a perfect replica of the Capitol House."
"The level of detail was completely breathtaking.{w=.3} Every pillar, every inch of the replica was alive with delicately carved design."
"It must have taken Sissel {i}days{/i} to finish this."
m "Sissel,{w=.3} this is {i}{b}amazing{/i}{/b}."
s "Y-you think so?"
m "But please tell me."

stop music fadeout 3
hide chocolate_sculpture with dissolve
"I jammed an accusing finger towards Hershel."
play music "calm-guitar.mp3" fadein 3
m "{i}What the bloody fuck is that chainsaw for?!{/i}"

show hershel at farright with dissolve
h "Loooooong story, mate.{w=.3} Culinary arts is complicated."

show sissel neutral at center with dissolve
s "It's not {i}that{/i} complicated."
s "Chocolate melts really easily,{w=.3} especially from the friction from sculpting."
s "So we froze a solid block of it in the fridge so that it's as hard as rock."
s "But because it was as hard as rock,{w=.3} we had to use a chainsaw to lob off huge chunks of it before I could work on the little details."
m "I can't believe it."
s "Huh?"
m "{i}You're a huge chocolate nerd.{/i}"
show sissel embarrassed with dissolve
s "H-hey, that's not really a bad thing."

show jinny neutral at farleft with dissolve
j "Don't sell yourself short Sis."
j "You'll pass the preliminary rounds tomorrow for sure.{w=.3} Ya big nerd."

show sissel neutral with dissolve
s "Maybe.{w=.3} I mean, this whole thing is just made of a pile of leftover white chocolate.{w=.3} Food-wise, it's nothing special."
m "You gotta stop being so humble dude.{w=.3} This is a real piece of art."

show hershel frown with dissolve
h "I'd hate to break the mood,{w=.3} but ya gotta be careful with this thing tomorrow, Sis."
h "Gerania's Culinary Arts contest is known for its cut-throat participants and aggressive sabotages."
h "Better keep a close eye on this thing if ya plan to pass the preliminary rounds."
s "Right right,{w=.3} I'll be careful."

s "Oh!{w=.3} And before I forget-"
"Sissel dug through a few drawers and pulled out a large paper bag that shuffled in its own weight."
s "Here's a bunch of leftover chocolate [charname],{w=.3} as promised."
s "Thanks for coming all this way just to look at my work man."
s "It means a lot to me-"
"I cradled the bag of chocolate in my arms like a newborn child."
"That's a lot of chocolate."
m "Sissel.{w=.3} I fucking love you."
show sissel wtf blush with dissolve
s "W-wha-?!"

scene black with Dissolve(3.0)
play music "meloncholy.mp3" fadein 2
scene cafe front with Dissolve(2.0)

"The sun was halfway under the horizon by the time we got ready to return to the dorms."
"Jinny had left early so that no one would notice she escaped her \"house arrest.\""

"As Sissel completed a few finishing touches on his sculpture,{w=.3} Hershel pulled me aside into a quiet part of the cafe."

show hershel with dissolve
h "Say [charname],{w=.3} mind if I have a word with ya?"
m "S-sure,{w=.3} what's up?"
h "I just wanted to thank ya for being such a good mate to Sissel.{w=.3} God knows the kid needs it."
m "Heh,{w=.3} it's no problem at all.{w=.3} Being his friend has its perks."

show hershel frown with dissolve
h "Could ya do me a favor while yer at it?"
h "The boy's got a bad habit of refusin' to ask fer help until shit hits the fan."
h "If you notice him strugglin' with anything,{w=.3} let me know."
h "'m always ready to give a helpin' hand."
h "Jinny tries to help whenever she can,{w=.3} but she's..........{w=.3} not always around."
show hershel with dissolve
h "So ya mind givin' me a heads up in her stead?"

"I chuckled at Hershel's anxious face."
m "Of course."
m "Sissel's pretty lucky to have such a caring boss."
m "..........say,{w=.3} sorry if this sound presumptuous,{w=.3} but are you and Sissel related by any chance?"
m "You two kinda look similar-"

show hershel frown with dissolve
"Hershel gave an exasperated scoff."
h "Why?{w=.3} Is it cuz we're both rabbits?"
h "That's kinda racist man,{w=.3} real uncool of ya."

"The two of us jumped as Sissel came out of the kitchen."
show hershel at right with dissolve
show sissel neutral at left with dissolve
s "Yo [charname],{w=.3} I'm all set."
s "Ready to head back?"
m "Y-yeah.{p=.3} Let's go."

s "See ya later boss!"
"Hershel's expression softened as he cheerfully ruffled Sissel's hair."
h "See ya around,{w=.3} ya rascal."

scene black with Dissolve(2.5)
"With that, the two of us left the cafe and made our way home."
"Even as we walked down the street,{w=.3} I could feel Hershel's gaze on us."
"He didn't look away until we turned the corner and went out of sight."

pause(1.0)
show sissel tarot lake at rcenter with Dissolve(2):
            xzoom .4 yzoom .4
            

jump day10_sissel

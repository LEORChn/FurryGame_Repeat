#Owen Day 10 rewrite
label day9_owen_rewrite:

play music "lullaby-guitar.mp3" fadein 2 fadeout 2
"Owen. {p=.3}There was a painful gnawing at my chest as I thought about that constantly-smiling doofus."
"There was always something odd about him...{w=.3} I hope he's alright."
"Speaking of which, {w=.3}where was he?{p=.3}I haven't seen a peep of him today."

"Well,{w=.3} sitting here on my ass isn't going to help."
"Time to search."

scene black with Dissolve(2.0)
scene school with Dissolve(3.0)

"The entire school was filled with students getting ready for Vistor's Day.{w=.3} But Owen was nowhere in sight."
"I ran around checking every classroom,{w=.3} dorm lounge,{w=.3} gym room,{w=.3} and even the showers."
"But no luck."
"I sighed as I trudged outside into the afternoon sun."
"Maybe Owen was hiding from the big crowds that Visitor's Day would probably bring."
"After all,{w=.3} his family reputation doesn't exactly make him well-loved around here..."


stop music 
"There was a sudden flash of orange in the corner of my eye."
"Speak of the devil."
play music "blue-feather.mp3" fadein 7
"I blinked as a frenzied Owen tore down the street and made a mad dash around the corner."
"Snarling close to his heels were a gang of four or five shifty-looking men,{w=.3} none of whom looked friendly."
"The men dressed like something straight out of an '80s greaser gang movie,{w=.3} with uncomfortably tight leather jackets and cheap Wal-mart sunglasses."
"It was almost hard to take them seriously if it weren't for the obvious gun pouches at their belts."

"I gulped and stared as the group chased Owen down a small alleyway."
"I have no godly idea what's going on but I can't just leave Owen stranded on his own."

"Steeling myself with a deep breath, {w=.3} I took off after them.{w=.3} Quietly."

scene black with Dissolve(3.0)
scene alleyway with Dissolve(2.0)


"My heart was thumbing rapidly against my chest as I peeked around the corner."
"The men had Owen surrounded, {w=.3} pressing his head roughly against the brick wall of the alley."
"Owen looked surprisingly calm despite the bruise that's slowly swelling on his forehead."
"He turned towards the men and grinned as though he's been through this a hundred times before."

show owen grin nervous with dissolve
o "Why hello gentlemen,{w=.3} it's been a while."
o "I know you folks like to play rough,{w=.3} but what's with the guns this time around?"

"One of the men growled and held the sharp end of a broken bottle dangerously close to Owen's face."
"Owen didn't bat an eye."
"Thug" "Sorry 'lil Lorelei,{w=.3} but looks like things are over for ya."
"Thug" "We've had a good time these few years,{w=.3} but yer family finally wanted to put an end to ya for good."
"Thug" "No hard feelings kiddo."

"Owen laughed and playfully booped the thug on the nose."
"That earned him a swift kick to the chest, {w=.3} but he barely flinched."

show owen grin 2 with dissolve
o "My {i}\'family\'{/i} hires you guys to rough me up every now and again as a {i}{b}formality.{/b}{/i}"
o "It's their loving way of saying,{w=.3} {i}\"We still have our eye on you.{/i}\""
show owen neutral with dissolve
o "Usually they just send you guys to beat me up a bit."
o "A black eye here,{w=.3} a broken bone there.{w=.3} Nothing more than that."
o "I've been careful to not provoke my family in years.{w=.3} Why would they want me dead now?"

"The leader of the thugs gave him a non-commital shrug."

"Thug" "Hell if I know what your family of psychos is thinking."
"Thug" "We're just doing what we're paid to do."

show owen upset with dissolve
"Owen scratched his chin thoughtfully whilst mumbling to himself."
o "They actually want me out of the picture now?{w=.3} This isn't good...."
o "Something's changed in the family.{w=.3} Someone sees me as an obstacle now...."
show owen neutral with dissolve
"Owen sighed begrudgingly."
o "They could at least hire some actual hitmen instead of street thugs-"

"Other Thug" "Oi,{w=.3} watch your mouth kid!"
"Other Thug" "Just cuz you're about to die doesn't mean we're gonna take any shit from you-"

"Owen gave the thugs an appologetic grin before casually rolling his shoulders and neck."
o "Sorry fellas,{w=.3} but I don't plan on dying today."
show owen upset angry with dissolve
o "{i}No hard feelings.{/i}"

play music "decisions.mp3" fadein 7
play sound "slam.wav"
hide owen
show alleyway behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"His movements were swift with practiced force."
"In a split second,{w=.3} Owen elbows one of the men in the face."
play sound "slam.wav"
show alleyway behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"The shock and surprise of the crowd gave him time to roundhouse kick another one and lock a third in a choke hold."

"The remaining thugs scrambled to aim their guns at Owen,{w=.3} who was using the thug in his choke hold as a shield."
"I gulped from my hiding spot around the corner as I watched the scene unfold."

"Owen's handling them surprisingly well.{w=.3} It's like he's done this frequently before."
"I'm not sure if that's good or not."
"The thug Owen elbowed was writhing on ground while holding his bleeding nose."

"Shit,{w=.3} he was coming this way-"
"I sucked in a nervous breath and quietly lodged myself behind a trash can as the thugs stumbled past me."
"Oh good,{w=.3} he didn't see me."
show owen upset with dissolve
"I peeked around the corner again to see Owen chucking another thug over his shoulder like a ragged doll."
"At this point the two remaining men suddenly remembered they were holding guns and began to firing blindly."
play sound "gunshot.wav"
hide owen with dissolve
"Sharp gunfire rang out as Owen swore loudly and dove behind a trash bin."

"This isn't looking good."
"From his current hiding spot,{w=.3} Owen can't move anywhere without being filled with holes."

"I ducked back behind cover again and took a deep breath."
m "Hey Echo!{w=.3} You there?"

play sound "ghost.mp3"
show echo shattered with dissolve
pause(.4)

e "Why do you always call for me when there's a gunfight going on?"
m "It's not like I {i}planned{/i} for this!"

play sound "gunshot.wav"
"More gunfire echoed down the alleyway as the two thugs approached Owen's hiding place."
"They've got another 10 steps before they get a clear shot of him."

"A sharp rain of {i}{b}crack!{/b}{/i} echoed through the alleyway as more bullets snapped against Owen's trash bin."
"I gulped.{w=.3} There's no time-"

m "Can't you do something?{w=.3} You're a ghost,{w=.3} you should be able help us somehow!"
show echo shattered frown with dissolve
e "While looking like this?{w=.3} [charname],{w=.3} my face is literally flaking off."
e "I'm not exactly strong enough to pull off another miracle."
m "There's gotta be {i}something!{/i}"
show echo shattered with dissolve
e "The best I can do right now is make you less noticable."
m "Good enough.{w=.3} Lay it on me!"

play sound "echo-wish.wav"
hide echo shattered with Dissolve(2.0)

"A cool breeze suddenly caressed across my face."
"My body felt a little lighter.{w=.3} Was this Echo working his magic?"

"No time to think,{w=.3} gotta move!"
"I shook my head furiously and took off running down the alleyway."
"I got closer and closer to the two thugs approaching Owen,{w=.3} but neither of them heard me coming."

"That's about when I realized I didn't think of a way to take them down."
"I came to a screeching halt, dumbfounded."
m "Well shit,{w=.3} what was I thinking-?"

play music "um.mp3" fadein 5
"To hell with thinking."
"I grabbed a nearby heavy-looking recycling bin and slammed it onto one of their heads."
play sound "slam.wav"
show alleyway behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"Thug" "OUGH-!!"
"Other Thug" "What the f-"
play sound "slam.wav"
show alleyway behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"With a graceful turn,{w=.3} I sent a flying kick straight in between the other mans legs."

stop music fadeout 10
"They both dropped like sacks of potatoes."
"Owen slowly peeked out from his trash bin,{w=.3} gaping in shock as I stood over the prone bodies almost heroically."
"Or stupidly.{w=.3} Depends on how you look at it."

show owen frown with Dissolve(2.0)
o "Holy shit [charname],{w=.3} where the hell did you come from?!"

"I didn't bother answering him before grabbing his hand and dragging him down the alleyway."
m "Hurry up and run before they wake up!"
"Owen blinked blankly as he followed me back towards the school."
o "O-oh,{w=.3} right."

scene black with Dissolve(3.0)
play music "snowdrop.mp3" fadein 7
scene kitchen with Dissolve(2.0)

"I dragged Owen all the way back to the dorm,{w=.3} where we both instantly collapsed in the kitchen."
"My head was still rushing with adrenaline as I struggled to catch my breath."
"This was certainly an unexpected turn of events..."

show owen neutral with Dissolve(2.0)
"Owen looked lost in his own thoughts as he sank into a kitchen chair."
"The two of us just sat in the kitchen for several minutes, {w=.3}letting our ragged breathing slowly die down."

"After a while,{w=.3} I glanced up at Owen quietly,{w=.3} wondering how to breach the silence."
m ".....so."
show owen grin nervous with dissolve
o "....so."
m "Are you going to tell me what the hell happened back there?"
m "Why were those thugs trying to kill you?{w=.3} And why did {i}{b}your family{/b}{/i} of all people hire them?"

"Owen pursed his lips as he searched for the first aid kit in the kitchen's drawers."
"After a few moments of silence,{w=.3} looked up at me reluctantly."
show owen scratch with dissolve
o "I guess I do owe you a {i}little{/i} explaination after you Captain America-ed those last two guys."

"Owen chewed on his lips thoughtfully as he applied hydrogen peroxide to the cut on his forehead."
"He dabbed at it with practiced ease."
"Did he do this regularly?{w=.3} Patching himself up after numberous fights?"
"The thought made my stomach turn uncomfortably."

o "I guess I should start by asking you a question."
o "How much do you know about the Lorelei and Adlai families?"
m "The Lorelei and Adlai families?"
m "Not much really."

o "Good.{w=.3} It's probably best if it stays that way,{w=.3} for your own good."
m "That's not much of an explaination."
show owen grin nervous with dissolve
o "I did say a \'little\' explaination,{w=.3} didn't I?"
m "Aw,{w=.3} at least give me a GoodReads synopsis."
m "I knocked out two grown men for you!"

"I only got more silence in response."
"Owen rolled up his sleeves and started whistling while sloppily bandaging up his arms."
"I sighed and grabbed the bandages out of his hands before pulling him closer."
m "Here,{w=.3} let me do it for you."
m "You're still hurt, after all."

play music "cafe-music.mp3" fadein 15
o "Aaaaw,{w=.3} thanks [charname]!"
o "Think you can get my back too?"
show owen shorts with dissolve
"With that,{w=.3} Owen pulled off his jacket with a grin and waggled his eyebrows suggestively."
"It was a nice view,{w=.3} I had to admit.{w=.3} But the myriad of cuts and bruises littering his body made it hard to indulge."
"I scoffed and grabbed the hydrogen peroxide off the kitchen table."

m "Don't think you can just change the subject by stripping."
"Owen shrugged."
o "Eh,{w=.3} it was worth a shot."
"I kneeled down close to Owen's abdomen and gently dabbed at the canvas of cuts that littered his body."
"Now that I'm up close,{w=.3} I could clearly see the mess of old scars that were well-hidden under his fur."
"It made me feel a little sick."

m "So,{w=.3} your family's trying to kill you?"
m "Isn't this something you'd want to tell the police?"
o "What do you know about the Lorelei's?"
m "Well they're one of the oldest and richest families in the city.{w=.3} They're a huge family,{w=.3} and have a lot of influence..."
o "Not just any kind of influence."
o "Political influence,{w=.3} business influence,{w=.3} and criminal influence."
o "Not to mention how they basically {b}own{/b} the police in the city."
o "Reporting them to the cops wouldn't do me much good."
m "Oh...."

"I gingerly applied medical cream to Owen's bruised arms."
m "So why does your family want you dead?{w=.3} You're just a kid."
"Owen grumbled uncomfortably."
o "That's a looooooong story that I'm not going to talk about."
o "Here's your GoodReads synopsis:"
o "I'm in a.......{w=.3}\'strained\' relationship with the rest of my family."
o "I try to stay out of their way most of the time,{w=.3} and usually they ignore me in turn."
o "But now they want to fill me with bullet holes for some reason."

"Owen speaks so cheerfully that I almost thought he was joking."
o "Aaaaand that conclude my 'little' explaination."
o "It's probably best if you didn't ask any more questions."
"I sighed heavily as I finished bandaging him up."
m "If you say so......"

o "I {i}do{/i} say so.{w=.3} Let's go back to simpler times where we just blindly flirted at each other."
o "Speaking of which-"
"Owen smirked seductively again."
o "I've got something else that needs your medical attention...."
"I glanced down to see the growing bulge in Owen's pants."
"Again,{w=.3} it's a nice view.{w=.3} But he's just doing this to change the subject."
"I reached down and gave the bulge a light flick."
play sound "surprise.mp3"
show kitchen behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"Owen nearly jumps out of his seat with a wince."

o "[charname],{w=.3} how could you?!{w=.3} You don't mess with a man's treasure like that!"
m "That's what you get for being so secretive and whatnot."

show owen grin nervous with dissolve
"Owen begrudgingly put his jacket back on before standing up and stretching lazily."
"After adjusting his bandages slightly,{w=.3} Owen made his way towards the door."
o "Well,{w=.3} thanks for patching me up [charname],{w=.3} but I gotta go now."

o "I've got a few things I need to check on. {w=.3} Privately."
m "Are you talking about your dick or your secretive stuff?"
show owen grin 2 with dissolve
o "Why not both?"
"I sighed and gave him a stern stare."
m "Just make sure to stay safe,{w=.3} okay?{w=.3} I don't want to find you all beat up again."
show owen grin 3 with dissolve
o "Will do."

hide owen with dissolve
"Owen gave me a not-so-reassuring thumbs up before disappearing down the hall."
"I sat alone in the kitchen with the first aid kit weighing heavily on my lap."

"There were still so many unanswered questions........"
"If Owen won't give me any answers,{w=.3} I'll have to find them somewhere else."

scene black with Dissolve(2.0)
play music "lullaby-guitar.mp3" fadein 4
scene hallway with Dissolve(2.0)

"The gears in my brain were grinding steadily as I strolled down the school hallways."
"Teachers and students were scurrying around me in preparation for Visitor's Day,{w=.3} but they were just background noise in my mind."

"The more pressing issue was that Owen was in danger."
"I can't just ignore what happened today just because Owen asked nicely."
"What I need now is more information about the families Owen was talking about:{w=.3} the Lorelei's and Adlai's."
"Apparently they were in some deep criminal activity that Owen didn't want to talk about."
"Luckily,{w=.3} I think I know someone who might have some answers...."
"Now if only I can find the class he's usually in......{w=.3}here it is!"

"Oh good,{w=.3} it's mostly empty too."
"Here goes nothing."

scene black with Dissolve(2.0)
scene lecture hall with Dissolve(2.0)

"There were only two people in the room as I quietly slid inside."
"Their familiar voices were hushed in deep conversation."
"My ears perked as I approached them curiously."

#START
j "-well I gotta do {i}something{/i} with these Black Cat fan letters!"

play music "calm-guitar.mp3" fadein 3
show jinny neutral at left with dissolve
show phillip annoyed at right with dissolve

p "{i}\"Something\"{/i} doesn't technically mean \"give them to Phillip.\" {w=.3}Ever heard of paper mache?"
j "You mean you don't actually read them?!{w=.3} What did you do with the last batch of letters I left you?"
show phillip annoyed look with dissolve
p "Where do you think all those paper planes I launched through your window came from?"
p "I'm not gracing these people with a response.{w=.3} Most of them are creepers anyhow."
j "I see what you mean.{w=.3} This one's return address is a badly drawn stick figure humping a beer bottle."

show phillip neutral with dissolve
p "Oh that's from Morse.{w=.3} I'll take it."
j "His drawings of dicks aren't exactly anatomically correct."
p "{i}That's{/i} what you're concerned about?{w=.3} Pfft, I'll let Morse know when I see him again."
j "That guy needs to work on his-"

"Jinny suddenly spots me listening in and beams, {w=.3}waving at me enthusiastically."
j "Oh hey there ghostbuster!{w=.3} Nice to see you still alive!"

m "Uh, hi Jinny.{w=.3} Nice to see you trespassing around the school again."
j "Hey!{w=.3} I had Phillip \'invite\' me on campus this time around, see?"
j "I'm an official guest now."
j "No harm no foul!"
show phillip irritated with dissolve
p "Except your doctor will probably shit a brick if he knew you snuck out again."
j "He's got enough bricks to build a shit castle by now.{w=.3} He should be used to it."

"I stared between Phillip and Jinny curiously.{w=.3} They seem awfully familiar with each other."
m "I didn't realize you were close.{w=.3} How did that happen?"
j "Oh I've been a close friend/occasional nuisance to Phillip since forever. {w=.3}It's a long story."

"Jinny elbowed Phillip to add to said \"story.\" {w=.3}He sighed and shrugged."
show phillip neutral with dissolve
p "I broke my wrist when I was little.{w=.3} Jinny and I ended up sharing a hospital room together."
p "She's been dragging me into her little \"adventures\" ever since."

"Jinny grinned and jabbed an eager finger against my chest."
j "Speaking of adventures,{w=.3} you still owe me a tour of the school after our little ghostbusting fiasco."
p "Oh great, she's captured you too [charname]?"
p "Good luck.{w=.3} Most of her adventures end in bruised skin and dignity."

stop music fadeout 5

m "Speaking of bruised skin,{w=.3} I need to ask a favor..."
"I glanced between the two of them,{w=.3} carefully picking my words."
m "So Phillip,{w=.3} you're the Black Cat."

play music "blue-feather.mp3" 
show phillip annoyed with dissolve
show jinny angry with dissolve
"Jinny feigned a confused look while Phillip raised an eyebrow suspiciously."
j "Phillip?{w=.3} The Black Cat?{w=.3} There's no way!"
j "Is this about the conversation from earlier?{w=.3} We were just joking around you know-"

show phillip annoyed look with dissolve
p "Jinny.{w=.3} He knows."
"Jinny blinked at me in surprise."
j "Really?{w=.3} [charname] knows?{w=.3} When did {i}that{/i} happen?"
show phillip neutral with dissolve
p "I kinda got shot by our old English teacher."
show jinny neutral with dissolve
j "Ooooooh,{w=.3} you mean the old rat Dolores?{w=.3} I always knew there was something fishy about that guy...."
j "I'm glad to hear he's finally behind bars now."
show phillip irritated with dissolve
p "Anyway,{w=.3} why bring this up?{w=.3} What's this favor you're talking about?"

"I swallowed hard as I stared between Phillip and Jinny."
"The two of them suddenly looked very...........{w=.3}experienced."
m "Well I think Owen might be in danger...."
p "Danger?{w=.3} Explain."

"I slowly recalled the events of this morning to the two of them."
"Their faces were knotted with worry as I described how secretive yet casual Owen was acting despite the situation."


m "In short,{w=.3} I was wondering if you two knew anything about the Lorelei and Adlai families."
m "Since you're the Black Cat and all,{w=.3} I kinda figured you'd know something about a huge family with criminal connections."

"Phillip and Jinny looked at each other in contemplation."
show phillip serious with dissolve
p "Sure,{w=.3} we know a thing or two about the families.{w=.3} It's kinda common knowledge for anyone who's worked for the city's.....{w=.3}seedier side."
p "I'm not surprised Owen's in a sticky situation if I'm being honest."
p "The two families were known to be pretty brutal."

show jinny thoughtful with dissolve
j "But [charname],{w=.3} are you sure you want to get involved?"
j "You might get sucked into things you're not ready for."
"I stared at my feet in silence for a few moments."
m "Yeah,{w=.3} I know."
m "But I can't just stand around and do nothing while Owen fights for his life in the background,{w=.3} you know?"
m "I want to help however I can."

"Phillip nodded quietly."
p "I like your drive,{w=.3} [charname]."
p "So,{w=.3} you want to know about the two most powerful families in the city's underworld?"

scene black with Dissolve(3.0)
play music "fragments.mp3" fadein 2
scene city_diagram with Dissolve(2.0)

p "Since the beginning of this city's development,{w=.3} there were two powerful families that influenced its development."
show silhouette1 at Position(xpos = .5, xanchor=.5, ypos=.5, yanchor=.5) with Dissolve(2.0):
    xzoom .7 yzoom .7
show silhouette1 at Move((0.5, 0.5), (.2, .5), 3,
              xanchor= .5, yanchor= .5)

show silhouette2 at Position(xpos = .5, xanchor=.5, ypos=.5, yanchor=.5) with Dissolve(2.0):
    xzoom .7 yzoom .7
show silhouette2 at Move((0.5, 0.5), (.75, .5), 3,
              xanchor= .5, yanchor= .5)
p "The Lorelei family,{w=.3} and the Adlai family."
p "They were pretty much two massive crime syndicates that constantly fought to gain the upper hand in the city’s political and business environment."
p "The two families rose to power through wits,{w=.3} bribery,{w=.3} brutality,{w=.3} and exploiting government officials.{w=.3} The list goes on."

j "You can probably already tell,{w=.3} but the two families absolutely hated each other."
j "They were practically two rival empires,{w=.3} with roots throughout the city's government and business sectors."
j "The law means absolutely nothing to them."
p "Hell,{w=.3} they probably believe that they {i}are{/i} the law."
p "The Lorelei family had no qualms when gathering thugs to smash the Adlai's businesses and slash up their family members."

p "The Adlai's would then gather hitmen to take out government officials supporting the Lorelei's."
p "And so the cycle continues."
j "It's a pretty bloody relationship,{w=.3} and it lasted for decades."
p "It's also probably why crime is so widespread in the city.{w=.3} There's never a shortage of employers."

"I scratched my head with a frown as I slowly tried to take in all this new information."
m "Quick question..."
m "I've definitely head of the Lorelei's here and there,{w=.3} but I've never heard anyone mention the Adlai family until today."
m "Whatever happened to them?"
p "Really?{w=.3} You don't know?"
j "You should read the newspapers more often [charname]."
m "H-hey,{w=.3} I read the comics section occasionally...."
j "Unfortunately,{w=.3} there was an incident about 20 years ago."
j "There was a huge Aldai family reunion party or something of the sort."
j "The Lorelei family took this opportunity to raid the whole place and then blow up the building."

j "Only one Adlai survived the incident."
hide silhouette2 with Dissolve(2.0)
p "She later mysteriously died of illness several years later."
m "So that means...."
show silhouette1 at Move((0.2, 0.5), (.5, .5), 3,
              xanchor= .5, yanchor= .5)

p "Yup.{w=.3} The Lorelei's are the only ones running the city now."
show silhouette1 at Position(xpos = .48, xanchor=.5, ypos=.8, yanchor=.5) with Dissolve(2.0):
    xzoom 1.3 yzoom 1.3
p "It's kinda shitty how they can do whatever they want,{w=.3} but there's been a steady decrease of violence in the city since the rivalry ended."
m "Say that to Owen and the thugs that keep chasing after him....."
p "I never said the violence completely stopped."
p "But I have to admit, {w=.3}the city's become a lot more peaceful since the whole rivalry thing disappeared."
scene black with Dissolve(2.0)
stop music fadeout 10
scene lecture hall with Dissolve(2.0)

m "Not peaceful enough if you ask me."
"If the Lorelei family is such a huge power in the city,{w=.3} that means they are uncontested in anything they do."
"My hopes of helping Owen in any way were slowly deminishing."
m "I guess this whole situation is a bit out of our league, {w=.3}isn't it?"

play music "lullaby-guitar.mp3"
show jinny neutral at left with dissolve
show phillip irritated at right with dissolve
j "Hey,{w=.3} don't look so worried.{w=.3} There's still a way we can help."
show phillip neutral with dissolve
p "Yes.{w=.3} Please quit moping [charname],{w=.3} you're bringing down the mood."

"I shot the two of them a wry smile."
m "You two got a plan?"
show phillip serious with dissolve
p "Half of a plan, {w=.3} really."
p "In these situations, {w=.3}information is our main form of currency."
p "Right now,{w=.3} we need to know {b}why{/b} the Lorelei family suddenly wants Owen dead after years of ignoring him."
p "Once we know why,{w=.3} we can start figuring out a way to change their minds."

"I nodded slowly. {w=.3}Phillip does have a point..."
m "But how are we going to find this information?"
show phillip smile shrug with dissolve
p "I'm the Black Cat,{w=.3} remember?"
show phillip neutral with dissolve
p "I have a partner-in-crime who works as an informant.{w=.3} A very reputable and respected one, actually."
p "He buys and sells information for a living after all.{w=.3} He'll be able to help us out."
p "I'll ask him to pull a few favors for us."

m "That's good to hear."
m "Is there anything I can do to help right now?"

"Phillip grimaced and stared between me and Jinny."
p "No.{p=.3}Just sit tight and don't do anything stupid."
j "Seriously?"
show phillip irritated with dissolve
p "Knowing you two,{w=.3} you'll probably do something rash and end up ass-deep into trouble."
p "Just stay out of things until we know more about the situation,{w=.3} okay?"

"Jinny made a face that just screamed 'oh great,{w=.3} here comes mother hen.'"
"She gave Phillip a thumbs-up.{w=.3} It was the kind of thumbs-up you'd give to placate a fussy parent."
"It was also the kind of thumbs-up that contained zero reassurance whatsoever."
j "Sure boss,{w=.3} whatever you say."
j "Now go talk to your \'informant\',{w=.3} I need a word with [charname]."
show phillip neutral with dissolve
p "What,{w=.3} right now?"
j "Yes,{w=.3} now!{p=.3}Time is of the essence!"

hide phillip with dissolve
show jinny at center with dissolve
"Jinny playfully nudged a reluctant Phillip out the door and shut it behind him."
"I raised an eyebrow as she turned towards me."

m "What's that all about?"
j "It's about Owen."
"Jinny glanced towards the door to make sure Phillip was gone before returning to me."
j "You wanted to help,{w=.3} right?"
j "I want you to stay with Owen until this whole thing is over."
j "Like a little bodyguard, {w=.3} if you will."

m "Me?{w=.3} A bodyguard?"
"I glanced down incredulously at my noodle arms and then back up at Jinny."
j "Well, not in the physical sense."
j "I've known Owen for years,{w=.3} and he's always bottled things up without telling anyone."
j "Don't let that handsome grinning face fool you,{w=.3} Owen's actually a pretty gloomy dude."

j "Let me guess,{w=.3} did he act super secretive today?"
j "Did he refuse to answer questions and have a 'I'll handle it myself' kinda attitude?"

"I thought back to our conversation in the kitchen this morning and sighed."
m "That about sums it up."
j "There's a lot of pressure from being born a Lorelei.{w=.3} I think it'll do him some good to have a friend by his side."

m "Why me specifically?"
j "Who else is there?"
j "Phillip is emotionally constipated, {w=.3}and Sissel will probably strangle Owen sooner or later."
j "And I'm under 'house arrest.'{w=.3} I can't exactly stay with him for very long."

m "Fair enough.{w=.3} I'll do my best."
"Jinny nodded at me, satisfied."
"Guess I'll be sticking with Owen for a good while."
"I just hope he's alright."
"The thought of having a bright red target painted on your back is frightening to say the least."

scene black with Dissolve(2.0)
play music "calm-guitar.mp3" fadein 3
scene school with Dissolve(2.0)

"The countless things I've learned today could fill a mile-long list."
"'Owen is very good at avoiding people' can now be added to the list."
"'[charname]'s legs were not made to run around campus for hours to look for Owen' can also be added to said list."

"I panted heavily as I sat my tired ass onto the pavement,{w=.3} my legs burning with overuse."
"Maybe bodyguarding isn't a good career path for me."
"I probably looked like roadkill right now."

o "Wow,{w=.3} you look terrible."

show owen neutral with dissolve
"My head shot up to see Owen strolling dejectedly down the street."
m "Where the hell have you been?!{w=.3} I've been looking everywhere for you!"

show owen grin 2 with dissolve
o "Aw,{w=.3} you missed me?"
m "You practically have the words 'Shoot me!' tattooed on your forehead.{w=.3} Shouldn't you be hiding?"

show owen grin 3 with dissolve
o "I'm not too worried at the moment."
o "If they were in a real hurry,{w=.3} they wouldn't be hiring street thugs instead of the usual professionals."
o "They're either being real cheap,{w=.3} or they don't have the resources."

o "I should be fine for now."

m "Well I'll have you know that I've been designated as your treasured bodyguard."
m "I'll be staying with you from now on to make sure you don't die."

show owen neutral with dissolve
o "You?{w=.3} My bodyguard?"
"Owen glanced down at me.{w=.3} He towered above me by at least a foot,{w=.3} dwarfing me by comparison."
o "Ah,{w=.3} I can tell.{w=.3} You'll really scare off the Lorelei's with your thin noodle arms."
m "I-I'll let you know I've got a very talented skillset."
o "What are you gonna do,{w=.3} seduce the killers?"
"I tipped my chin up defiantly."
m "You never know!{w=.3} Maybe I will!"

show owen grin 3 with dissolve
o "Yeah,{w=.3} if we're lucky, the killers will have a thing for the short and scrawny type-"
m "-Anyway,{w=.3} where have you been all day?{w=.3} It's kinda weird for you to run off right after getting jumped by a gang."

show owen neutral with dissolve
"Owen glanced around the empty streets cautiously before motioning me to follow him inside the school."
o "I'd love to have a chat but it's best we do it indoors."
o "Being out in the open makes me a bit paranoid now."
o "Now come along Mr. Bodyguard."
m "Any chance I can get paid for this?"
show owen grin closed with dissolve
o "Who knows?{w=.3} Maybe if you satisfy all my 'needs~'"
"I cut him off with a deadpan groan."
m "-Let's head inside."

scene black with Dissolve(2.0)
play music "easy-lemon.mp3" fadein 2
scene dining hall with Dissolve(2.0)

"Owen and I decided to grab lunch (Dinner?{w=.3} Lunch?{w=.3} {i}Dunch?{/i}) in the school dining hall."
"Being sheltered by the walls of Gerania took a little weight off my chest."
"Watching Owen pour ketchup on his mac and cheese returned that weight with a crushing vengence."

show owen neutral with dissolve
o "...[charname],{w=.3} you okay there?"
"I tore my horrified gaze away from the cheesy ketchup mess on his plate,{w=.3} my face pale with disappointment."
m "I am disgusted."
o "Hey,{w=.3} don't knock it till you try it."
m "I'll just......{w=.3}take your word for it."
m "Anyway,{w=.3} you were in the middle of telling me where you were today?"
o "Oh right.{w=.3} Uh......"

show owen grin nervous with dissolve
"Owen sheepishly stuffed a forkful of pasta into his mouth,{w=.3} chewing slowly."
o "I uh.....{w=.3} got kicked out of a bar."
m "What really?{w=.3} You never seemed like the drinking type-"
show owen neutral with dissolve
o "I wasn't there to drink!"
o "I've heard that there's a reputable criminal informant hiding in the bar."
o "Someone going by the name of 'Morse.'"
m "That can't possibly be his real name.{w=.3} Unless his parents have really bad taste..."
o "I wouldn't be surprised.{w=.3} Everybody in the business uses fake identities to some degree."

o "I wanted to see if this Morse could help me find out why my family's suddenly so trigger-happy."
show owen grin nervous with dissolve
o "Unfortunately I'm not old enough to get into the bar.{w=.3} I tried bribing them but the bouncer didn't take the bait."
show owen neutral with dissolve
o "There goes that plan.{w=.3} Getting a meeting with the most reliable informant in the city was more difficult than I thought."

"I frowned.{w=.3} Owen's casual tone when talking about 'criminal informants' and 'trigger-happy families' still felt rather unsettling."
m "You seem awfully well-versed in this whole business."
m "Is this what growing up with rival crime syndicate families does to you?"

stop music fadeout 5
show owen upset with Dissolve(2.0)
"Owen stopped mid-bite of another disgusting ketchup mess.{w=.3} His brows furrowed with mild frustration."
o "You found out about this already? {w=.3}That was quick."
o "Where did you hear it from?"
m "I um....{w=.3} had my sources."
m "Sorry if this upsets you.{w=.3} I know you wanted me to stay out of it...."

play music "compassion.mp3"
show owen grin nervous with Dissolve(2.0)
o "No no,{w=.3} it's fine."
o "I'm kinda jealous actually."
m "Jealous?{w=.3} Of me?"

show owen scratch smile with dissolve
o "Sorta."
o "Growing up,{w=.3} I was ignorant of everything going on around me."
o "The families,{w=.3} the crime,{w=.3} everything."
o "My mum and butler did their damn best to keep me in the dark."
o "I know they were just trying to keep me safe but......{w=.3} it got a bit frustrating after a while."

m ".......{w=.3}What was it like,{w=.3} growing up as a Lorelei?"
show owen neutral with dissolve
o "Not too bad actually."
o "Oh! {w=.3} I actually have a picture I can show you!"

show owen_familyphoto with Dissolve(3.0)
pause(2.0)
"Owen dug out his wallet and showed me a small photo tucked neatly inside."
"Four smiling faces beamed back at me.{w=.3} Well........{w=.3} almost four."
"The sight of a tiny grinning Owen put a wide smile on my own face."
"Sitting next to him was the kind face of his mother.{w=.3} She looked rather tired,{w=.3} with stress wrinkles lining her eyes."
"Still,{w=.3} something about her presence exuded a sense of noble grace..."

"Standing behind them were........{w=.3} is that Owen's father?"
"Nah,{w=.3} couldn't be."
"They wore the same shit-eating grin but they looked too different to be related."
"A servant, maybe?"

"And that man standing behind them..."
"His hawk-like eyes glare back at me through the photo."
"I had a feeling he was someone you shouldn't mess with."

hide owen_familyphoto with Dissolve(3.0)

"I glanced up to see Owen beaming as I studied the family portrait."
m "They look surpisingly nice."

o "My mum was the most wonderful lady in the world.{w=.3} She was always super patient with my immature ass."
o "Spoiled me quite a bit actually.{w=.3} But she always taught me to be compassionate and kind to everyone around me."
o "And my butler was also the coolest badass you'll ever meet."

show owen grin 2 with dissolve
o "On my tenth birthday,{w=.3} he sneakily bought me a big orange motorcycle and tried to teach me how to drive it."
show owen grin 3 with dissolve
o "We almost died.{w=.3} Twice."
o "And mum nearly skinned us alive."
show owen grin 2 with dissolve
o "Totally worth it though."

show owen upset with Dissolve(2.0)
o "But....................{w=.3}it sucked, being kept in the dark."
o "I always wondered why gunmen were breaking into the house every few weeks while my mother locked me in a saferoom."
o "My mum and butler would come home with bullet wounds and tell me that they were off 'slaying dragons.'"
o "No matter how much I asked,{w=.3} I never got an answer."

o "'Just sit tight and wait for us to save the day!'{w=.3} my butler would say."
o "I had to fight tooth and nail to even know what was happening around me."

show owen neutral with dissolve
o "My weird uncle was the only one who didn't beat around the bush."
"Owen jabbed a finger towards the frowning man in the corner of the portrait."
o "He's got eyes like a hawk,{w=.3} that one."
o "He always had that look,{w=.3} as though he quietly knew everything there was possible to know."
o "Whenever we were alone,{w=.3} I'd ask him questions."
o "And he'd tell me straight-forward answers."
show owen upset with dissolve
o "It's a little disheartening to hear that your mother was born into a criminal family and your butler and uncle used to kill people for a living."
o "But it's better than knowing nothing at all."
o "But by the time I got answers.............."

"Owen blinked and stuffed his wallet back into his pocket hastily."
show owen grin nervous with dissolve
o "Well,{w=.3} that's all in the past now.{w=.3} Nothing to worry about."

"I studied Owen's face carefully.{w=.3} He looked so vulnerable when talking about his family like this...."
"With a soft smile on my face,{w=.3} I reached up and gave him a gentle pat on the shoulder."
m "Thanks for trusting me enough to tell me all this."
m "It's nice learning more about you."

show owen scratch smile with dissolve
"A slight tint of pink flushed across Owen's face as he coughed sheepishly."
o "God damnit [charname],{w=.3} you're embarrassing me."
m "Oh my,{w=.3} did I just manage to make the great Owen Lorelei {i}blush?{/i}"
m "I should mark my calender."
"Owen gave a flustered laugh before quickly excusing himself from the table."

show owen neutral with dissolve
o "While you do that,{w=.3} I'm gonna use the bathroom real quick."
o "Be back in a bit."

hide owen neutral with dissolve
stop music fadeout 10

"I watched Owen's retreating back,{w=.3} feeling a little warmth in my chest."
"It was nice,{w=.3} being trusted like this."
"I feel like I understand Owen just a little bit more now."

"Except....."
"I quickly grabbed Owen's offending plate of ketchupy mac and cheese and tossed it triumphantly into the trash."
"That guy has horrible taste."

play sound "ghost.mp3" 
show echo shattered with Dissolve(3.0)

m "ACK!"
"I nearly jumped out of my chair as Echo's cracked form appeared floating above my table."
m "What the hell Echo,{w=.3} give me some warning next time!"
e "Sorry little man,{w=.3} I didn't want to interrupt your bonding session with Owen."
e "But there's something I think you should know."
m "What do you mean?"

play music "tranquil.mp3" fadein 3
show echo shattered frown with dissolve
e "That photo Owen showed you.....{w=.3}he has a lot of strong feelings towards it."
e "I can sense his thoughts clearly."

m "What do you mean?"
e ".........................................."
e "{i}\"Half the people in that photo are dead.\"{/i}"
e "That's what he was thinking."
"My chest knotted with dread."
"I looked down the hall where Owen retreated towards.{w=.3} No wonder why he didn't talk about himself often."
m "I hope he's okay......"

show echo shattered with dissolve
e "Owen's a strong kid.{w=.3} He'll be fine."
e "But [charname],{w=.3} if you're going to stay close to him,{w=.3} you'll have to be careful."
e "I'm not strong enough to protect you every time you dive into a gunfight."

e "One of these days,{w=.3} you might end up as another photo for Owen to grieve over."
"I gulped,{w=.3} my stomach lurched uncomfortably against my chest."
m "I guess I'll just have to be more careful then."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "calm-guitar.mp3" fadein 3
scene dining hall with Dissolve(3.0)

show owen grin 2 with dissolve 
"Owen returned from the bathroom and clapped his hands together with an excited grimace."
"He wore a face that screamed {i}\'Alright, let’s go do something stupid!\'{/i}"
"Oh boy,{w=.3} here we go."

show owen grin 3 with dissolve
o "So."
m "...so?"
o "As my faithful and selfless bodyguard,{w=.3} can I count on you to help me with something?"

m "Well I’m not getting paid for this,{w=.3} so selflessness is going to be in limited supply."
m "What are you planning?"

o "Nothing dangerous!"
show owen scratch smile with dissolve
o "It’s just that........{w=.3}umm,{w=.3} how should I explain it?"
"Owen tapped his chin thoughtfully.{w=.3} And suspiciously."
show owen neutral with dissolve
o "I um,{w=.3} have a mission for you!{w=.3} I mean, us!"
m "A \'mission.\'"

show owen grin 2 with dissolve
o "Yes,{w=.3} a mission!{w=.3} We are going to infiltrate a very important house on Derry Street!"
show owen grin 3 with dissolve
o "The goal is to.....{w=.3}um, {w=.3}check on the status of a certain someone."
o "Yup,{w=.3} that's the mission!"

"I stared at Owen with a dull expression,{w=.3} one eyebrow raised in an unimpressed {i}\'really?\'{/i}"
"This guy's even worse at lying than I am."

m "And who's this certain \'someone?\'"
show owen neutral with dissolve
o "He's this big guy named Samuel."
o "He's the kind of guy who looks like he can snap you in half with just his fingertips,{w=.3} but don't worry though!"
o "Samuel's actually a sweet little teddy bear on the inside."

m "Right..."
m "So why are we checking on this teddy-bear-man?"

show owen grin nervous with dissolve
"Owen's grin faltered slightly."
o "I just want to make sure the Lorelei family hasn't done anything to him."
o "He's....{w=.3}uh....{w=.3} someone close to me."
show owen neutral with dissolve
o "Gotta make sure he hasn't been caught up in my troubles."

"I scrutinized Owen's nervous face for a moment."
m "If you guys are so close,{w=.3} why are you \"infiltrating\' his house?"
m "Why not just go up to him and say \"Yo Samuel!{w=.3} Still alive there buddy?{w=.3} Yes?{w=.3} Alright, cool.\""
"Owen looked bitterly amused at the idea."

show owen grin nervous with dissolve
o "Well um........{w=.3}it's a looooong story, but I fucked up and the two of us aren't exactly on speaking terms."
o "At least I don't think so."

m "Are you going to try to......unfuck it anytime soon?"
m "It's probably better to actually talk to the guy than to sneak around his house."

show owen frown with dissolve
"Owen let out a heavy sigh and shook his head rapidly, as if to ward off unwelcome thoughts."
o "Look [charname],{w=.3} I just want to go make sure he’s safe."
o "Will you come with me or not?"

"I studied Owen’s grim face with worry."
"I don't completely agree with this plan,{w=.3} but at the same time there's a lot I don't know about the situation."
"More importantly, Owen clearly doesn’t want to face this ‘Samuel’ on his own."
"I sighed and gently reached up on my toes to pat Owen on the head."

m "Of course I’m coming,{w=.3} I’m your bodyguard after all."
m "We're heading to Derry Street right?{w=.3} Just lead the way."
"Owen smiled and nodded gratefully."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "soothing-rain.mp3" fadein 3
scene derry street with Dissolve(3.0)

#rewriting shit again begins here

"It turns out Derry Street was {i}{b}not{/b}{/i} nearby."
"I bent over my burning calves and rasped for precious air as we finally reached our destination."
"Owen hardly broke a sweat as he casually strolled down the sidewalk beside me."

show owen neutral with dissolve
o "Geez, you really have to work out more.{w=.3} We’ve only been walking for half an hour."
o "Need me to carry you?"

"I shot him a wry glare as I steadied myself upright."
"It sounded tempting, and my last remaining shred of pride was the only thing stopping me from collapsing myself onto Owen."

m "I can’t just let myself be carried! What kind of bodyguard would I be?"

show owen grin 3 with dissolve
o "You’d be a mascot.{w=.3} Cute, but ultimately useless."
m "Damn Owen, that's cold.{w=.3} You wound me."

hide owen with dissolve
"Owen chuckled as I sulked downed the sidewalk with him."
"Now that I had a moment to catch my breath,{w=.3} I finally had the chance to take in my surroundings."
"Wow,{w=.3} so this is Derry Street.{p=.3} I've never been to this side of town before and now I can see why."
"The street is lined with pretentiously gaudy houses and painfully green lawns."
"There are even fences that scream \"You ain't good enough to live here\" to us common folk."
"At least it was fairly quiet here. {w=.3}There's barely any traffic or people around."

stop music fadeout 5
show owen neutral with dissolve
o "And there's the house!"
"Owen suddenly elbowed me and gestured towards a surprisingly small and modest house."
"The lawn was rather unkept, but the home looked cozy and inviting."

play sound "whisper.mp3" 
"A frigid chill suddenly slid down my spine as I glanced upward."
"There was a flock of small birds circling the house,{w=.3} their wings shimmering a brilliant klaedescope of colors."
"They don't look.....{w=.3}natural."

m "Hey Owen,{w=.3} do you see those birds?"
o "Hm?{w=.3} What birds?"
m "How can you miss them?{w=.3} They're right-"
"I blinked,{w=.3} confused."
"The flock of birds were suddenly nowhere to be found,{w=.3} disappearing just as quickly as them came."
"I swear I saw....{p=.3}Hm,{w=.3} might have been just my imagination."

"I focused my attention back on the house of this \"Samuel.\""
"The house's neighbors have barricaded it with offensively large white fences,{w=.3} as if to ward off its inhabitants."
"Whoever lived here had given up on taming the weeds plaguing the lawn,{w=.3} and instead tried to outshine it with brilliant orange rose bushes."

play music "scheming.mp3" fadein 4
"There was also an incredibly ugly orange motorcycle parked in the driveway."
"I squinted at the hideous atrocity.{w=.3} Its over-saturated mess of colors stared back,{w=.3} as if to taunt me."
"I stumbled backwards in disgust."
m "That,{w=.3} is the ugly damn motorcycle I have ever seen."
"Owen looked utterly offended."

show owen grin 3 with dissolve
o "What are you talking about?{w=.3} She's a beaut~"
m "Maybe you should borrow Phillip's glasses.{w=.3} That {i}thing{/i} is a crime against nature."
m "Who actually picks orange as the color for their bike?"
o "I'll have you know orange is the classiest of colors and I love it."

m "Well maybe you got bad taste-"
"I suddenly froze as the realization hit me."
m "Wait,{w=.3} is this your motorcycle?"
"Owen spluttered,{w=.3} crossing his arms and refusing to look my way."

show owen grin nervous with dissolve
o "N-not at all!{w=.3} I just like orange."
m "You mentioned your butler bought you an orange motorcycle earlier-"
m "Wait-{p=.3}Is this your house?!"
o "-um-"
m "-Is Samuel your butler?!{p=.3}He's the big scruffy one from your photo isn't he?!"

stop music fadeout 7
o "Well maybe..."
m "C'mon Owen,{w=.3} you suck at lying."
m "Why were you trying to hide this the whole time?"
m "\"Infiltration\" my ass,{w=.3} you're sneaking into your own house."

play music "somber.mp3" fadein 7
show owen scratch with dissolve

"Owen sighed and scratched his head tiredly."
o "I was hoping to get this done and over with without bringing it up."
o "Just didn't want to think about it,{w=.3} really."


show owen frown with dissolve
o "I uh........{w=.3}ran away from home when I was 12.{w=.3} And I haven't come back for 7 years."

m "What? {w=.3}Why did you run away?"
o "My mum had just fallen ill and passed away.{w=.3} And my uncle got arrested and murdered in prison.{w=.3} It was a tough time for everyone in the family."

"Owen paused for a bit."
o "{i}{b}My {/b}family.{/i} Not the Lorelei's."
o "Nobody would tell me what was going on.{w=.3} Nobody explained why my family just fell apart out of the blue."
o "I only had Samuel left, {w=.3}and even he was barely coping with it."

"Owen sighed and stuffed his hands into his pockets before staring off into the distance."
"There was a look of shame on his face."
o "You know how when you're angry,{w=.3} you shout and yell and scream things you'll end up regretting later?"
o "Like the frustration just takes over and you end up hurting people close to you?"

o "Yeah,{w=.3} I did that."
o "To Samuel."
o "He probably hates my ungrateful ass now and I don't blame him."
o "But I still want to make sure he's alright,{w=.3} you know?"
o "He's all I got left."


"I reached up to place a hand on Owen's shoulder.{p=.3}He shook it off."
m "Have you tried talking to him?"
o "Honestly,{w=.3} I'm too scared shitless to talk to him."
o "I really messed up [charname]."

m "C'mon Owen,{w=.3} you gotta at least try."
m "You can't just leave stuff like this hanging forever.{w=.3} It's been {b}7 years.{/b}"
m "If you care about Samuel that much,{w=.3} you have to at least give him some closure."

"Owen sighed heavily and rubbed the bridge of his nose."

o "I'll try.{w=.3} No promises though."
stop music fadeout 10
"Owen shook his head furiously to clear his thoughts before making his way down the street."
o "C'mon [charname],{w=.3} gotta make sure he's still alive first."

scene black with Dissolve(2.0)
play music "clear-air.mp3" fadein 10
scene derry street with Dissolve(2.0)

"As we approached the house,{w=.3} Owen's eyes glazed over with nostalgia."
show owen neutral with dissolve
o "Man this brings back memories. I kinda miss the good old days where I was still ignorant of everything..."
show owen frown with dissolve
"Owen sighed bitterly as he stepped onto the driveway."

show owen grin closed with dissolve
o "The neighbors haven’t changed much either.{w=.3} I remember once my mother got into a fist fight with this PTA lady next door because she said I was a wild hooligan."

m "Yikes, not exactly a friendly neighbor."
show owen grin nervous with dissolve
o "Oh our house was infamous on Derry Street."
o "My mum and uncle -{w=.3} well he wasn’t my real uncle, but he might as well be {w=.3}- hated all the neighbors.{w=.3} They were all pretty nosey and intrusive."

o "{i}\‘Oh my goodness Heather! {w=.3}You’re married, but are living without your husband and with {i}{b}two other men?{/b}{i}{w=.3} Scandalous!’{/i}"
"Owen’s attempt at imitating a high pitched old lady was ridiculous."

show owen grin 2 with dissolve
o "So my mum and uncle went out of their way to annoy the shit out of everyone."

o "They’d sneak out in the middle of the night to blast country music around the street."
show owen grin 3 with dissolve
o "Another time they decorated our house with so many Christmas lights that the neighbors called the fire department on us."

m "I take it everyone on Derry Street stayed the hell away from you guys?"
show owen neutral with dissolve
o "Pfft, pretty much. My home was the definition of private.{w=.3} The neighbors would walk around the block just to avoid us."

"Owen’s grin faltered slightly."
show owen scratch with dissolve
o "Now that I think about it, mum probably intended for that to happen....."

"He sighed and shook his head before forcing himself to grin."
show owen neutral with dissolve
o "Anyway, {w=.3}let's sneak inside!"

"He peered into one of the windows and frowned."
show owen frown with dissolve
o "Hmmm,{w=.3} looks like no one's home."
"Owen bit his lip in slight worry."
m "Samuel probably went out to grab groceries or something.{w=.3} Nothing to worry about."
o "Yeah,{w=.3} I hope so."
o "Alright, let's go."

m "Are we going to sneak through a window?{w=.3} Or maybe pick the lock on the backdoor?"
show owen neutral with dissolve
o "Dude, it's {i}my house{/i}.{w=.3} I've got the keys to the front door."
m "Well that's just boring."



scene black with Dissolve(2.0)
scene derry house with Dissolve(2.0)

"The house smelled light and lemony, {w=.3}as if someone repeatedly scrubbed it down with soap."
"I quietly closed the door behind us and peeked around. {w=.3} Looks like we were alone here."
"I gotta admit,{w=.3} this was not how I imagined Owen would take me home to the family."
"Owen sighed as he wandered around the rooms,{w=.3} eyes unfocused in a nostalgic haze."

show owen neutral with dissolve
o "This place hasn't changed a bit."
show owen grin closed with dissolve
o "Heh,{w=.3} that burn mark where mum blew up the kitchen still there!"

m "Uh Owen,{w=.3} why is there a gun hanging from the coat rack?"
show owen grin nervous with dissolve
o "Oh,{w=.3} that must be one of mum's \"precautions.\""
m "Precautions?"
"Owen shrugged, {w=.3} as if that explained everything."
o "C'mon [charname],{w=.3} let's check if Samuel's been around."

hide owen with dissolve
"Owen and I strolled around the kitchen,{w=.3} slowly taking in our surroundings."
"The house definitely felt lived in."
"The coffee machine was still warm and there was a pit of unwashed dishes in the sink."
show owen frown with dissolve
o "Samuel's getting sloppy.{w=.3} Uncle Graham usually badgers the hell out of him until he gets the chores done."
m "I kinda expected something perfect and clean from a house with an actual butler."
m "At least we know he's still alive and well,{w=.3} right?"

show owen scratch with dissolve
o "Maybe.{w=.3} But I'm not leaving until we catch sight of him in the flesh-"
"I looked up from poking at the dishes with dismay."
m "Why is there a knife taped under the kitchen sink?"
show owen neutral with dissolve
o "{i}Precautions.{/i}"
m "....Right."
m "Did people break into your house often?{w=.3} Why the hell would you need so many \"precautions?\""

show owen scratch with dissolve
"Owen grabbed a chair from the kitchen table before sinking into it with an exhausted slouch."
o "That's exactly why.{w=.3} I always wondered why people liked targeting our house specificly when I was little."
o "I always figured it was because my mother was so wealthy."

stop music fadeout 7

"Owen hung his head back and stared at the ceiling with half-lidded eyes."
"The empty house was silent for several long moments."
"I shifted around uncomfortably.{w=.3} I felt like an outsider here,{w=.3} like someone seeing something meant for other eyes."

play music "tranquil.mp3" fadein 5
"My ears perked up when Owen finally spoke."
o "{w=.3}This is going to sound horrible but............"
o "......{w=.3}what if the Lorelei family just......."
o "...........{w=.3}disappeared?"
o "No more fighting,{w=.3} no more guns,{w=.3} no more schemes."
o "Just.........{w=.3}disappear."

"My stomach twisted in a painful knot as I slowly processed those words."
m "....{w=.3}like how the Adlai family disappeared?"
o "Yeah."
m "Owen,{w=.3} that's kinda....{w=.3}horrible."
o "...yeah."
o "...but it'd be for the greater good,{w=.3} you know?{p=.3}More importantly......"

stop music fadeout 10

"Owen sighed and closed his eyes."
o "I just want my family back."

pause(1.5)

play sound "slam.wav"
hide owen

scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"Owen and I nearly jump out of our skins as the front door suddenly rattled open."
o "Shit,{w=.3} he's home!"
"Heavy footsteps echoed through the empty house,{w=.3} slowly making its way towards the kitchen."

m ".....uh,{w=.3} do we just go up to him and say hello or-?"
o "{i}Shhhhhhh!{/i}"

hide owen with dissolve
"Owen suddenly grabbed me by the hand."
"The two of us squeezed ourselves into a nearby cubboard just in time to hide from the massive man entering the kitchen."

play music "water-lily.mp3" fadein 5
show samuel neutral with Dissolve(2.0)
ss "........Hm."
"I was pressed up tightly against Owen in our cramped hiding place,{w=.3} both holding our breath in suspense."
"We squinted through the tiny crack at the door as the man scanned around the room cautiously."
"Samuel hasn't changed much from the Owen's photo."

"There were a few more age lines under his eyes,{w=.3} and the shit-eating grin of the photo has been replaced with tired scowl."
"He circled around the kitchen table quietly before setting down his groceries on the chair Owen sat in moments ago."

ss "............."
ss "....I'm home."

"Samuel mumbled out to no one in particular.{w=.3} His greeting echoed quietly through the empty house."
"I felt Owen's grip on my hand tighten."
"He was shaking behind me,{w=.3} as if to stop himself from reaching out to his only surviving family."

m "{size=-10}Are you okay?{/size}"
"Owen merely nodded quietly."

stop music 
play sound "slam.wav" 
"There was a suddenly {i}CLANK!{/i} as his head hit a box of ramen noodles behind him."
"The two of us froze."

play music "decisions.mp3" fadein 5
"Samuel gave a startled yelp and leapt to his feet.{w=.3} He grabbed the cubboard door and swung it open."
"And then his jaws dropped in shock."

show samuel at left with dissolve
show owen grin nervous at right with dissolve
ss "{i}{b}Owen?!{/b}{/i}"
o "H-hey Samuel!{w=.3} Been a while!"
ss "How did you-?!"

"Samuel didn't get to finish."
play sound "slam.wav"
hide samuel with dissolve
"Owen grabbed a small cardboard box from the cubboard and threw it over the butler's head."

m "Wah-{w=.3} Why did you-?!"
o "{i}Don't ask,{w=.3} just run!{/i}"

"Before I knew it,{w=.3} Owen grabbed in my hand in a panicked haze and dragged me upstairs,{w=.3} leaving behind a bewildered Samuel."

scene black with Dissolve(2.0)
scene derry house hallway with Dissolve(2.0)

"Owen and I panted heavily as we dashed around the house and up the stairs."
"Samuel's heavy and confused footsteps were following quickly behind us."

"I glanced up at Owen as he grabbed my hand again and dragged me down the hall."
m "What the hell was that?!{w=.3} Why did you throw a box over your butler's head?!"
m "I thought you said you would talk to him!"
show owen grin nervous with dissolve
o "{size=+10}{i}I'm sorry!!!{w=.3} I panicked,{w=.3} okay?!{/i}{/size}"
m "What do we do now?"
show owen scratch smile with dissolve
o "{i}I have no godly idea I didn't exactly plan this far-{/i}"

play sound "surprise.mp3"
hide owen 
scene derry house hallway at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
ss "{size=+10}{i}OWEN YOU LITTLE SHIT GET BACK HERE WE GOTTA TALK{/i}{/size}"

show owen neutral with dissolve
o "Oh shit here he comes."
"Owen and I jump into a nearby bedroom and slammed the door shut,{w=.3} the two of us utterly winded."
"I can hear Samuel's footsteps thundering up the stairs."
o "Alright, {w=.3}I think I got a plan."
m "I'm not sure I much faith in your planning skills anymore."
show owen grin nervous with dissolve
o "No no,{w=.3} this one's a good one!"
o "You're going to.....{w=.3}uh,{w=.3} distract Samuel for half a second while I make my getaway!"
m "What?!"
show owen grin 2 with dissolve
o "I mean,{w=.3} you {i}are{/i} my bodyguard-"
m "Why don't you just talk to the poor guy?"
m "This isn't bodyguarding!{w=.3} You're using me as a meatshield!"

show owen neutral with dissolve
o "Hey,{w=.3} Samuel would never hurt you!"
o "To be honest,{w=.3} he'd probably treat you like a guest and cook you dinner or something-"
o "-But me?{w=.3} Ohoh,{w=.3} that's a whole other story."

"The house shook as Samuel hurtled down the hallway towards this room.{w=.3} I gulped."
m "Owen,{w=.3} you're the worst."
o "I'll make it up to you later!"
o "Just hold him off for a bit!"

stop music fadeout 5
hide owen with dissolve

"There was a sudden,{w=.3} surprisingly gentle knock on the door as Samuel skid to a stop outside."
"I stare at the doorknob like a deer caught in headlights as Owen leapt to the other side of the room."
o "{size=-10}You can do it,{w=.3} I believe in you!{/size}"
"I promptly flipped him the bird."
"The things I do for this guy."
"Alright [charname],{w=.3} here we go-{p=.3}With a sigh, I slowly opened the door."

play music "scheming.mp3" fadein 3
show owen_jump1 with Dissolve(3.0)
m "Oh {i}hellooooooo{/i} there!{w=.3} You must be Samuel!"
m "It's a pleasure to meet you!"

"Samuel was absolutely intimidating as towered over me with a raised eyebrow."
ss "You one of Owen's friends?"
m "Y-yes?"
"Samuel sighed.{w=.3} To my surprise,{w=.3} he reached down and gave me a gentle pat on the head."
ss "Brave little fella aren't you?"
ss "Let me guess,{w=.3} Owen said something like {i}\"Hold him off for me!\"{/i} while he went into hiding?"
m "Uh,{w=.3} something like that."
m "You guys really should have taught him a little more chivalry when he was younger."
"Samuel smirked and glanced around the room."
ss "Yeah,{w=.3} we did spoil him quite a bit."

ss "Anyway,{w=.3} where is the little brat?{w=.3} I've got a few words I'd like to share with him."

"There was a loud rustling from the other end of the room."
"I glanced over my should and gulped."
m "Actually-"
play sound "slam.wav"
play sound "glass-break.mp3"
play music "hyperfun.mp3"
show owen_jump2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
pause(1.5)

m "-he just left."

"Samuel gaped as Owen soared out the window and landed on what sounded like a bush in the neightbor's yard."
"There was more rustling,{w=.3} followed by the sound of an elderly lady screaming as Owen dashed down the street as quickly as his legs could take him."

play sound "surprise.mp3"
show owen_jump2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
ss "{i}Oi!{w=.3} That's expensive!{/i}"
"Samuel scrambled across the room and stuck his head out the broken window to scream at Owen's retreating figure."
play sound "surprise.mp3"
show owen_jump2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
ss "You could've just snuck around-{p=.3}{size=+5}{i}Fixing windows ain't cheap you little shit!!!{/i}{/size}"
o "{size=-10}{i}Put it on my tab!{/i}{/size}"

scene derry house hallway with Dissolve(2.0)

show samuel neutral with dissolve
"Samuel sighed tiredly as Owen sped off into the sunset."
ss "That little shit hasn't changed much,{w=.3} has he?"
ss "Always running away with his tail tucked between his legs."

"He turned towards me. {w=.3}I gave Samuel my most innocent smile."
m "This is a weird family."
show samuel smile with dissolve
"Samuel snorted."
ss "You have no idea."
ss "Anywho,{w=.3} you want to join me downstairs for tea? {w=.3}Haven't entertain a guest in a while."
"I blinked in surprise,{w=.3} but hastily nodded in agreement."

m "Wow, Owen was right.{w=.3} You really are as nice as a teddy-bear."
show samuel neutral with dissolve
"Samuel rolled his eyes and grumbled as he lead me downstairs."
ss "I'm a doberman,{w=.3} not a teddy bear.{p=.3}Why does everyone keep saying that?"

scene black with Dissolve(2.0)
play music "clear-air.mp3" fadein 2
scene derry house with Dissolve(2.0)

"Samuel made his tea by letting it simmer before adding milk and mint."
"He said it was the \"Owen-style\" tea,{w=.3} as it was Owen's favorite since he was a kid."

"I splutter slightly when I took my first sip.{w=.3} The taste was sharp and {i}very{/i} sweet."
"It wasn't bad,{w=.3} but definitely not what I was used to."

show samuel neutral with dissolve
"Samuel settles into a chair at the kitchen table,{w=.3} gently blowing at his steaming cup."
ss "So,{w=.3} you're Owen's friend?{w=.3} Didn't quite catch your name before."
m "Just call me [charname]."
ss "Alright [charname],{w=.3} hope I didn't scare you earlier."
ss "Just a little surprised, you know?{w=.3} I guarded this house all alone for 7 years.{w=.3} No calls,{w=.3} no letters,{w=.3} no nothing."

show samuel smile with dissolve
ss "Then suddenly Owen pops out of a closet with another man!"

"Samuel jerks an eyebrow up at me suspiciously.{w=.3} I laughed nervously and buried my face into my steaming teacup."
ss "Speaking of{w=.3} how's the little rascal doing after 7 years away from home?"
"I took another sip from my cup thoughtfully {w=.3}(and dully wondering what the tea would taste like if I added a bit of choclate)."

m "He's been doing pretty well.{w=.3} We've been living at Gerania Academy together."
ss "Gerania?{w=.3} So that's where he's been hiding."
ss "Funny,{w=.3} I studied there a long time ago too."
ss "That's where I met Owen's mother,{w=.3} Heather."

stop music fadeout 5
"My ears perked up at the mention of the name."
m "Um,{w=.3} I've heard that Owen's got a weird family history."
m "Owen's mom.....{w=.3}what was she like?"
m "And how did you end up working for her?"
play music "compassion.mp3" fadein 10
show samuel neutral with dissolve

"Samuel sighed into his cup,{w=.3} his eyes glazed over with a nostalgic haze."
ss "Heather Adlai is-{p=.3}....was,{w=.3} the most brilliant and noble woman I have ever met."
ss "I didn't originally plan to go to Gerania Academy.{w=.3} I was too deep in debt and gang activity to even consider it."
ss "Never was very bright."

show samuel smile with dissolve
ss "But then Heather Adlai pops out of the blue and says {i}\"You've got a good heart.{w=.3} I like you.\"{/i}"
ss "Suddenly I was attending Gerania Academy,{w=.3} tuition totally paid and getting an education and all that good jazz."
ss "She was a good woman,{w=.3} that Heather...."

"Samuel's teacup rattled against the kitchen table with a sharp {i}clink!{/i}"
show samuel neutral with dissolve
ss "Too bad she gave opportunities to the wrong people."
m "Did something happen?"
ss "Shit goes wrong kid,{w=.3} as they do."
ss "I got accused of murder and went into hiding with my best friend."
ss "We got mixed with my old gang activities all over again.{w=.3} Completely wasted her efforts."

ss "We didn't see Heather for years.{w=.3} Then suddenly out of the blue,{w=.3} Heather shows up with the Lorelei family breathing down her neck."
ss "She was pregnant with Owen and needed protection.{w=.3} So I offered it."
ss "And that's how I ended up being a butler/bodyguard for this little household."

stop music fadeout 10
"Samuel sighed again,{w=.3} suddenly sounding very old."
ss "Oh,{w=.3} I rambled on for a bit there didn't I?"
ss "Sorry if I bored you kid,{w=.3} I haven't had anyone to talk to in a long time."
"His voiced echoed through the empty house,{w=.3} as if proving his point."

play music "clear-air.mp3" fadein 5
show samuel smile with dissolve 
ss "That's enough from me though.{w=.3} What about you?"
m "Me?"
ss "How did you end up in my closet with Owen?"
m "Oh,{w=.3} that."
m "As a matter of fact,{w=.3} I'm Owen's new bodyguard!"

"Samuel took one look at my tiny frame before spitting out his tea laughing."
ss "Y-you?!{w=.3} A bodyguard?!"
ss "You've got balls kid,{w=.3} but no muscle to back it up."

"I huffed indignantly."
m "I'll have you know I took down two thugs coming after Owen today."
m "Granted,{w=.3} all I did was kick one in the balls but it was still a job well done!"

play music "somber.mp3" fadein 10
show samuel neutral with dissolve
"Samuel's grin suddenly dropped as his eyes narrowed."
ss "Thugs?{w=.3} After Owen?"
m "Oh yeah,{w=.3} apparently the Lorelei family has been targeting Owen lately."
m "Like,{w=.3} the dead kind of target.{w=.3} With guns."
m "I was wondering if you had any idea why they'd want Owen dead."

"Samuel's brow wrinkled into a worried scowl as he tapped the kitchen table thoughtfully."
ss "That's not good.....{w=.3}but I have a hunch."
ss "Owen's the son of Heather Adlai and Oleander Lorelei,{w=.3} both of whom are powerful figures in their respective families."
ss "And Heather was the last surviving heir of her family after the Adlai massacre almost 20 years ago."
m "...wait,{w=.3} that means when she passed away,{w=.3} Owen inherited the entire Adlai fortune?"

ss "Spot on."
ss "And how old is Owen right now?{w=.3} 19?{p=.3}Definitely of age."
ss "If he happens to meet an unfortunate end,{w=.3} his fortune would pass along to his only surviving family member:{p=.3}Oleander Lorelei."
ss "A lot of people would kill for such a massive amount of money...."

m "So now what?{w=.3} Is there anything we can do to stop them?"
"Sameul drooped his head down,{w=.3} staring at his teacup mournfully."
ss "{i}{size=-10}Graham would know what to do if he was still alive..........{/size}{/i}"
m "What?"
ss "Hm?{w=.3} Oh, nothing."
ss "Leave it to the adults,{w=.3} kid.{p=.3}I'll figure something out."

m "But I want to try and help if possible...."
ss "Hate to break it to you kid,{w=.3} but this is a bit out of your league."
ss "But let me know if you notice anything strange going on around Owen."

"Samuel huffed grumpily as he got up from his seat."
ss "If only the little brat would actually talk to me again...."
"I perked up,{w=.3} an idea slowly forming in my head."
m "Tomorrow's Vistor's Day at Gerania Academy!{w=.3} You'll probably find a chance to talk to Owen there!"
ss "Really now?"
m "Yeah,{w=.3} I'll invite you as my guest!{w=.3} Then you and Owen can sit down and talk out whatever problems you have."
m "He misses you a lot too.{w=.3} He's just too chicken to actually break the ice."

"The butler's face softened into a tender smile as he nodded his thanks."
ss "Sounds like a plan.{w=.3} You're not bad for a half-baked bodyguard."
m "Hey,{w=.3} I'm doing pretty well for someone who's not getting paid."
"Samuel barked a laugh as he collected my empty teacup."

ss "Well in that case you're a mighty good friend.{w=.3} I'm glad Owen's got people looking out for him."
ss "Anyway,{w=.3} it's getting late.{w=.3} I should probably get you a ride home-"

play sound "thunder.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
play music "raining.mp3"

"The two of us jumped as a clap of lightning suddenly streaked across the sky."
"We exchanged surprised glances before peaking out the window."

scene derry street night with Dissolve(3.0)
"It was raining buckets outside,{w=.3} the dark sky roaring as thunder and torrents of water streaked down."
"Samuel and I grimaced at the sight."

show samuel neutral with dissolve

ss "...{w=.3}Well shit."
ss "Hate to break it to you kid,{w=.3} but I've only got a motorcycle."
ss "If we drive to Gerania on that thing,{w=.3} we'd probably be utterly soaked."
m "And with my luck,{w=.3} struck by lightning."
m "Wait,{w=.3} is that {i}hail?{/i}"

"I groaned and tugged at my hair.{w=.3} Mrs. Corlisse would skin me alive if I didn't make it back to the dorms before curfew."
show samuel smile with dissolve
ss "Don't worry about it kid,{w=.3} you can stay with me for the night.{p=.3}There's plenty of room in the house."
m "R-really?{w=.3} I don't want to intrude-"
ss "Nah,{w=.3} you're fine.{w=.3} You're actually doing me a favor.{w=.3} The house gets awfully depressing when it's just me on my own."
ss "Haven't cooked dinner for anyone else in a long while anyway.{w=.3} Time to see how rusty I've gotten."
m "A-ah okay.{w=.3} Thank you so much sir!"
hide samuel with Dissolve(2.0)
"I continued to stare out the rain-soaked window as Samuel moved away towards the kitchen."
"Owen was right,{w=.3} Samuel really was just a big friendly teddy-bear."
"It feels a bit weird to be sleeping in someone else's house for the night,{w=.3} but I'll take what I can get."

play sound "ghost.mp3" 
show echo shattered with Dissolve(2.0)


"I wasn't even surprised when Echo suddenly materialized at my side.{w=.3} The cold chill down my spine felt familiar and comforting by now."

e "[charname],{w=.3} you doing okay?"
m "Sure, I'm trapped by the rain.{w=.3} But I'm also getting cooked a fancy dinner by a handsome butler in a rich neighborhood."
m "In terms of bad situations,{w=.3} this is pretty nice."
m "I might even thank Owen when we get back to Gerania."
show echo shattered frown with dissolve
e "Don't get too comfortable.{w=.3} There's something strange about this house......."
"My hands fiddled with the camera hanging from my neck carefully."
m "Yeah...{p=.3}Those birds flying over the house when we first arrived.{w=.3} Did you notice?"
show echo shattered with dissolve
e "There's no doubt.{w=.3} There's a wish residing here."
e "It's weak and lacks any real power,{w=.3} so we don't have to worry about it doing anything dangerous."
e "But still,{w=.3} we should keep an eye out."

"I nodded and tapped the window thoughtfully."
m "This rainstorm showed up right as Samuel offered to drive me back to Gerania.{w=.3} A coincidence?{w=.3} Or is the wish trying to keep us here?"
m "I wonder........."
e "Do you have something in mind?"
"I grinned and turned around,{w=.3} scanning the interior of this empty, echoing house."
m "I think we've got some snooping to do tonight."

scene black with Dissolve(2.0)
play music "cafe-music.mp3" fadein 2
scene derry house with Dissolve(2.0)

"Dinner was absolutely delicious."
"Samuel was an excellent cook and whipped up a fancy steamed salmon dish full of expensive-looking spices."
"He fussed around me like a mother hen while I cheerfully wolfed down my food."
"I was afraid of intruding at first,{w=.3} but the butler seemed happy to have someone around for once."

"Samuel's ears perked up from washing the dishes as I let out a burp from the kitchen table."

show samuel smile with dissolve
ss "Hope my cooking suited your taste.{w=.3} I might have grown a bit rusty over the years."
m "No no,{w=.3} this was great!{w=.3} Thank you so much for having me over Samuel!"
show samuel neutral with dissolve
ss "Speaking of having you over,{w=.3} shouldn't you make a call to your teachers at Gerania?"
m "Oh shit,{w=.3} I knew I was forgetting something."

hide samuel with dissolve
"I fumbled for my phone frantically,{w=.3} scrolling through my contacts for Mrs. Corlisse's number."
"Maybe she'll be too worried to be pissed at me."

play sound "phone.wav"
"{i}Bzzzzzzzzz..............{w=.3}Bzzzzzzzzzzzzzzz.........{/i}"
"{i}Bzzzzz-{/i}"

play music "scheming.mp3"
play sound "surprise.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
c "{size=+15}{i}{b}-IS THIS [charname]?!!{w=.3} DEAR ARE YOU ALRIGHT???!!!!{/i}{/b}{/size}"
"I immediately yanked the speaker away from my ear."
"Sweet jesus, for such an old lady,{w=.3} Mrs. Corlisse sure had a strong set of pipes."

play sound "surprise.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
c "{size=+15}{i}{b}-I FOUND OWEN LIMPING BACK TO CAMPUS TODAY LIKE HE JUST RAN FOR HIS LIFE THROUGH THE RAIN-{/i}{/b}{/size}"
c "{size=+15}{i}{b}-AND THEN YOU HAVEN'T COME HOME PAST CURFEW-{/i}{/b}{/size}"
m "-Mrs. Corlisse,{w=.3} I'm fine-"
play sound "surprise.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
c "{size=+15}{i}{b}HAS SOMETHING HAPPENED???!!!{w=.3} PLEASE [charname] DO NOT MAKE ME WORRIED LIKE-{/i}{/b}{/size}"

"There was a rush of faint voices under Mrs. Corlisse's booming shouts.{w=.3} It sounded like someone was trying to take the phone from her."
"A jumble of shouts and yelps rang out from the speaker as multiple people wrestled for the phone."
j "{size=-10}-Gran,{w=.3} you're overreacting. I'm sure he's fine-{/size}"
play sound "surprise.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
c "{size=+15}{i}-I ASSURE YOU THIS IS A PERFECTLY REASONABLE REACTION!!{w=.3} I WAS WORRIED SICK-{/b}{/size}"
o "{size=-10}Wait is [charname] still at my house?{w=.3} Can I talk to him real quick?{/size}"
c "{size=-10}Hands off children!{w=.3} This is {i}my{/i} phone-{/size}"
j "{size=-10}{i}-give me the damn phone Gran!{/i}{/size}"

"There was another {i}CRASH!{/i} from the speaker as someone knocked over a chair."
s "{size=-15}-what the hell is going on in there???{/size}"
j "{size=-15}-go back to bed, Sis!{/size}"

j "-yes,{w=.3} got it!"
j "Yo ghostbuster,{w=.3} you hear me?!"
"I stifled a laugh as I held the speaker close to my ear again."
m "Sounds like I heard a little too much if you ask me."
j "Oh hush,{w=.3} everyone was worried sick about you.{w=.3} We pretty much formed a prayer circle in the dorm kitchen waiting for you to come back."
"I felt a small pang of guilt in my chest.{w=.3} I didn't think they'd be so worried."
j "So where are you right now?{w=.3} Safe from the rain,{w=.3} I hope."
m "I'm chilling at Owen's house.{w=.3} His butler Samuel's taking good care of me,{w=.3} so no worries."

c "{size=-10}Samuel?{w=.3} As in Samuel Clark?{/size}"
c "{size=-10}He's an old student of mine!{w=.3} Oh,{w=.3} it's good to know [charname] is in good hands.{/size}"
j "So you're {i}not{/i} in immediate danger,{w=.3} and we can all go to sleep without worrying?"
m "Uh,{w=.3} yeah."
j "Sweet!{w=.3} Good to know!"

"Jinny's voice turned faint as she announced my status to the rest of the room."
"I could hear a collective sigh of relief."
j "Now that we've gotten that out of the way-"
play sound "surprise.mp3"
scene derry house at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
j "{size=-10}{i}GET OVER HERE AND APPOLOGIZE YOU LITTLE SHIT!!{/i}{/size}"
o "{size=-10}{i}Ow ow!{w=.3} Geez Jinny I just got beat up this morning,{w=.3} can't you be a little gentler-{/i}{/size}"
j "{size=-10}{i}You ditched [charname] and ran for your life because you couldn't talk to your {b}own damn butler!{/b} {w=.3}Don't be a wuss!{/i}{/size}"

"There was another muffled rattle and thud as someone shoved the phone into another's face."
o "H-hey there [charname]!{w=.3} H-how you doing?"
m "Hello there Owen.{w=.3} Your butler's a wonderful dude by the way.{w=.3} And excellent cook too."
o "O-oh really?{w=.3} See?{w=.3} I told you he's just a sweet teddy-bear on the inside-!"

stop music fadeout 10
j "{size=-10}Damnit Owen,{w=.3}{i} appologize.{/i}{/size}"
"Owen sighed with a hint of shame."
o "I'm sorry I ditched you at my house [charname].{w=.3} I should've just stayed and talked to Samuel."
o "I was just......{w=.3}scared,{w=.3} you know?"
o "I was terrible to him when I left home and I said terrible things...."
"Another sigh."
o "I'm just scared."
"Owen sounded so.......{w=.3}vulnerable.{w=.3} My breath caught in my throat as I wondered how to reply."


"Someone suddenly tapped on my shoulder and I jumped up in surprise."
show samuel neutral with Dissolve(2.0)
ss "{size=-10}.......is that Owen?"
"I stared at him blankly for a moment before nodding quietly."
"Samuel motioned for me to hand him the phone."

play music "my-oath-to-you(slow).mp3" fadein 5
ss ".......Hey there kid."

o "S-Samuel?"
"There was a clatter from the speaker like someone had just dropped the phone."
"Samuel waited patiently as Owen scrambled to pick it back up."
o "L-listen Samuel,{w=.3} I-"
o "I-I'm so sorry for what I said when I left,{w=.3} I was just so angry and-"
ss "........shhhhhhhhh."
ss "I'm not angry.{w=.3} It's fine."
o "B-but it's not fine-!"
ss ".......shhhhhhhhh."
"Owen fell silent as Samuel slowly cleared his throat."

ss "I won't deny you were being a little piece of shit when you left.{w=.3} And then didn't come back home for {i}7 years.{/i}"
ss "You had me real worried,{w=.3} you know that?"
o "{size=-10}...sorry.{/size}"
ss "But I'll also admit I was being a shit too.{w=.3} Things were rough when your mum and Graham passed."
ss "I should have been a bit more understanding."

"There was a heavy pause as Samuel tried to catch his breath."
"I could hear Owen's pitched breathing from the phone as he tried to keep himself from tearing up."

ss "You're my last family, {w=.3}Owen."
ss "I miss ya."
o "{size=-10}......yeah.{w=.3} I miss you too.{/size}"

ss "So how's this?{w=.3} I'll be heading over to Gerania for Visitor's Day tomorrow,{w=.3} and we'll finally have a proper chat."
ss "No more secrets,{w=.3} no more running.{p=.3}Let's just talk."
ss "You up for that?"

"The phone rustled quietly,{w=.3} as though Owen was nodding."
o ".....y-yeah,{w=.3} I'd like that."
o "......I promise not to run this time."
stop music fadeout 8
"Samuel let out a low chuckle."

ss "Better not.{w=.3} I can catch up to you this time."

play sound "bump.mp3"
"There was a clatter from the other side of the phone."
play music "sapphire.mp3" fadein 3
j "{size=-10}{i}We'll strap him down to a chair if we have to!{/i}{/size}"

"A round of stumped chuckles echoed through the phone as Samuel laughed for real this time."
o "Damn it Jinny,{w=.3} we were having a moment."
j "{size=-10}Well you're hogging Gran's phone and it's gonna out of minutes any time now-"
o "-Well shit."
c "You can talk to Samuel in person tomorrow.{w=.3} It's good to hear you two are making up."
"Samuel's ears drooped in embarrassment."
ss "Wait,{w=.3} was I on speakerphone?{w=.3} Did everyone hear that?"
c "Pretty much."

"There was another clatter from the phone as someone opened a door."
s "{size=-15}{i}-what the hell is going on in here?{w=.3} It's 1AM???{/i}{/size}"
s "{size=-15}{i}-and why is Owen crying??{/i}{/size}"
o "God damnit guys."

play sound "bump.mp3" 
"The phone suddenly cut off and disconnected."
"Samuel let out a hearty laugh as he handed my cellphone back to me."
ss "Well,{w=.3} looks like I'll get to talk to Owen after all."
ss "......{w=.3}Thanks for being here,{w=.3} [charname]."
m "It's my pleasure-"

"I yawned and covered my mouth drowsily."
show samuel smile with dissolve
ss "Haha,{w=.3} it's been a long day for you,{w=.3} hasn't it?{w=.3} Probably best you get to bed."
ss "You can use the guest room and showers upstairs.{w=.3} I'll get you a change of clothes."

m "*yawn*{w=.3} Thanks Samuel."
m "You're the best."
ss "I know~"
hide samuel with Dissolve(2.0)

scene derry house hallway with Dissolve(2.0)
"And so I gave in to my exhaustion and allowed Samuel to lead me upstairs."
"I didn't remember much afterwards,{w=.3} only that sleep took me as soon as my head hit the incredibly comfortable pillow."
"This was a nice ending to such a hectic day......."

scene black with Dissolve(3.0)
scene repeat_screen with Dissolve(1.0)
pause(1.5)

scene black with Dissolve(2.0)

show owen tarot 9 at rcenter with Dissolve(2.0):
            xzoom .6 yzoom .6



jump day10_owen_rewrite







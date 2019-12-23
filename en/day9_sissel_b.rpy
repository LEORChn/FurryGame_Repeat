label day9_sissel_b:


play music "asphodel.mp3"
scene white with Dissolve(2.0)
pause(1.5)
$ persistent.current_route = "sissel_b"

"I was falling."
"An endless, surreal world of clockwork mechanisms and little pieces of time swirled past me."
"Whispers and broken conversations buzz all around me,{w=.3} but I couldn't make any sense of it all."
"It feel like I've been falling for hours…..."

"All the while, her words echoed in the back of my head:"
"???" "I'll see you again soon,{w=.3} [charname]."

pause(2.0)

play sound "slam.wav"
stop music
scene cafe front-dark
show cafe front-dark at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)

m "{i}{b}{size=+15}Ooomph!{/size}{/b}{/i}"
"I faceplanted right onto the cold, tiled floor of Hershel's cafe."
"The room was still spinning in nauseous circles as I flipped onto my back and groaned."
"I feel like I was just thrown into a washing machine set to \"heavy cleaning.\""


s "Holy shit,{w=.3} [charname],{w=.3} you alright?"
j "Oof,{w=.3} I think his nose is bleeding."
"I squinted at the ceiling as my vision slowly returned to me."

play music "water-lily.mp3" fadein 3
show jinny neutral at farleft
show sissel surprised at center
show hershel frown behind sissel at farright 
with Dissolve(2.0)
"Three figures stood over me with varying expressions of concern."

"Sissel reached down and helped pull me back onto my wobbly feet."
"My brain still felt like cotton balls as I stared at them in bewilderment,{w=.3} a warm river of red dripping down my bruised nose."

m "-w{w=.3} -wah?"
m "What happened…?"

show sissel neutral with dissolve
s "Dude,{w=.3} I was about to ask you the same thing."
s "You just keeled over and smashed your face onto the floor.."

"He pressed a hand against my forehead worriedly."
s "You feeling alright?{w=.3} Did you get a heatstroke on our way here?"
m "No, no,{w=.3} I'm fine."
m "Just got a little tired all of a sudden…."
"I felt someone smoosh a handful of napkins against my face."
"Jinny hovered over me as she gently dabbed at my bloodied nose."
j "That was one hell of a fall, [charname]!"
j "I pass out all the time and even I don't manage to bash my face this hard."

show hershel with dissolve
h "Ya need any water kiddo?{w=.3} Maybe ya should go 'n sit down fer a while."

"I glanced up and blinked in confusion."
m "Hershel?{w=.3} What are you doing here?"

stop music fadeout 7
"Hershel let out a hearty laugh."
show hershel grin with dissolve
h "What do ya mean?{w=.3} This is {b}{i}my{/i}{/b} cafe after all."
"I blinked."

m "B-but didn't the cafe burn down……?"
"I blinked again and fumbled around the cafe in utter confusion."
"The whole cafe was intact,{w=.3} like nothing ever happened."

show hershel frown with dissolve
h "Burned down?{w=.3} I mean,{w=.3} there was this small kitchen fire a couple years ago but nothing too bad.."

m "-and Hershel…"
play music "blue-feather.mp3"
"He was completely healthy."
"Not a single scratch or bruise from when I last saw him in his hospital room...."
m "-what? {w=.3}But didn't this place….?"
"I shook my head vigorously and slapped myself in the face."
"What the hell is going on?"

s "Dude,{w=.3} are you feeling alright?"
s "Maybe I should take you back to the dorms and we can call it a night."

m "You! {w=.3}Sissel!"
s "Yeah,{w=.3} that's my name."
s "Glad we got that part sorted out."

m "W-"
m "Why are you here?"
m "I thought you got mad at Hershel and left!"

"Sissel scratched his head awkwardly."
s "Why would I be mad at Boss?"
s "I work here.{w=.3} Plus he's been helping me out to prepare for the culinary competition for Visitor's Day tomorrow."
s "Besides him calling me \"Sissy\" all the damn time,{w=.3} there's not much to be mad about."

m "But you just found out his sister is your-"

stop music
show hershel sad with dissolve
"I stopped myself in time to see Hershel turn absolutely pale."
"Sissel doesn't know?"

"But…."

m "-wait,{w=.3} Visitor's Day?"
m "What day is it today?"
j "It's August 9th,{w=.3} the day before Visitor's Day."

play music "moonheart.mp3" fadein 3
"A quick glance at my phone confirmed that it was indeed,{w=.3} August 9th."
"A whole 6 days before everything ended in misery."

"I'm having trouble believing it but........"
"Time had reset."
"Events are now repeating upon itself."
"Wait a moment…"

"...Is this the {b}\"second chance\"{/b} the voice in the Clockwork World was talking about?"
"A chance to make things right."

"Memories of all the horrible things that happened suddenly washed over me."
"A sense of determination builds up in my chest."
"This isn't the end though,{w=.3} there's still a chance to make things right!"
"I could fix everything, {w=.3} make things better."
"There was no way anyone was happy with how things turned out in the previous timeline…"

show sissel nervous with dissolve
s "Um,{w=.3} [charname]?"
s "You doing okay?{w=.3} You've got this really intense look on your face."

hide jinny
hide hershel 
with dissolve
"I roughly grabbed Sissel's shoulder's and stared him straight in the eyes."
m "Sissel,{w=.3} listen."
m "Tomorrow?{w=.3} At the competition?"
m "You'll do fucking great."

show sissel indignant with dissolve
s "Uh,{w=.3} t-thanks?"
s "{size=-10}We're a little close right now…{/size}"

m "If anyone messes with you,{w=.3} {i}I'll fucking kick their ass.{/size}"
m "You've got my full support,{w=.3} no saboteur is gonna get anywhere near you."
m "{size=+10}{i}You're gonna fucking {b}win{/b}.{/i}{/size}"

show sissel happy with dissolve
"Sissel's face was tinged with red."
s "Um.........."
s "U-uh sure…!"
s "Of course I'm gonna win this,{w=.3} just you wait and see!"

hide sissel with Dissolve(2.0)
"He will."
"And I'll make sure of it."
"There's a lot of work to do if I want to guarantee Sissel's brighter future."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "lullaby-guitar.mp3" fadein 2
scene cafe front-dark with Dissolve(2.0)

"I spent the next half hour trying to convince Sissel and Hershel that I was,{w=.3} indeed,{w=.3} not going insane. "
"The waning river of blood pouring out my bruised nose did not help."
"The two of the all but forced me to lie down and hydrate myself until the bleeding stopped."
"Strangely enough,{w=.3} Jinny did not need much coaxing."
"She simply nodded with that knowing smile she always wears."
"It’s a little unsettling,{w=.3} to be honest."

"Even stranger still,{w=.3} she seemed to sense that I wanted to speak with Hershel alone."
"As Sissel continued to fuss over me like a mother hen,{w=.3} Jinny pulled him aside."

show jinny neutral at left 
show sissel neutral at right
with Dissolve(2.0)
j "Alrighty,{w=.3} quit smothering him Sissel."
j "Let's give the guy some space."

show sissel indignant with dissolve
s "I'm just making sure he's not sick! {w=.3}He still looks pretty nauseous."
j "That's just his face, dude.{w=.3} [charname] can't help how he looks."
m "{size=-10}H-hey,{w=.3} I can still hear you guys...{/size}"

j "C'mon,{w=.3} let's go to the kitchen and get him some hot chocolate or something."
j "Once [charname]'s feeling steady again,{w=.3} you can help him back to his dorm."
"With that,{w=.3} Jinny grabbed Sissel by the hem of his shirt and dragged him towards the kitchen."
show sissel surprised with dissolve
s "H-hey,{w=.3} careful with the shirt!"
s "It's ripped enough as it is!"

stop music fadeout 7
hide jinny with dissolve
hide sissel with dissolve
"Jinny gave me a discreet thumbs up as she pushed Sissel into the kitchen."
"Now there's only me and Hershel in the room."

show hershel sad with Dissolve(2.0)
"He sat in the booth across from me,{w=.3} as pale as a ghost and deathly nervous."
"A heavy silence hung in the air as he spent several minutes avoiding my eyes."

play music "meloncholy.mp3" fadein 3
h ".......S-say,{w=.3} 'bout that weird stuff you blurted out earlier…."
h "'Bout my sister."
h "H-how did you…?"

show hershel frown with dissolve
"I held up a hand and Hershel fell silent."
"Deep breaths,{w=.3} [charname]."
"Deep breaths."

pause(1.0)
m "I know that you're Sissel's uncle."
"Hershel swallowed,{w=.3} his knuckles clenched tightly."
m "I know that Sissel's mother is Cecilia Bradley."
m "You stole money from her to fund your trip to the national culinary competition,{w=.3} which caused Cecilia's debtors to kill her and leave Sissel orphaned."

show hershel sad with dissolve
h "H-how-?"
m "Don't ask how I know,{w=.3} just that {b}I know.{/b}"
"Hershel nodded and swallowed again,{w=.3} his brow heavy with sweat."
"His eyes darted towards the kitchen where Sissel was still clearly out of earshot."

m "I haven't told Sissel yet."
m "I don't want to throw this bombshell at him right before his competition."
m "But I won't leave this secret alone for long."
m "Sissel deserves to know the truth.{w=.3} Why he grew up alone on the streets,{w=.3} what kind of people his family was-"
m "-And that his mother loved him very much."
m "{i}He deserves to know.{/i}"

"I looked Hershel straight in the eyes."
m "And you need to tell him yourself,{w=.3} or I will.{w=.3} And it won't be pretty."
m "Understood?"

"Hershel took a deep breath and nodded."
show hershel frown with dissolve
h "...alright."
show hershel sad with dissolve
h "Just……{w=.3}just give me some time."

"He looked so vulnerable in that moment,{w=.3} his face a mess of emotion."
"Guilt,{w=.3} shame,{w=.3} anxiety,{w=.3} relief...."

"I reached across the table and gave Hershel a gentle pat on his shoulder."
m "Listen Hershel…{w=.3} I still think you're a decent guy,{w=.3} and I'm sure you've been through a lot."
m "But there is no way things can stay the way they are now."
m "I just….{w=.3}really care about Sissel."
m "I don't want to hurt him any more than absolutely necessary."
m "And I think you feel the same way."

show hershel frown with dissolve
"There was a weak smile across Hershel's face as he slowly nods."
h "Yer right 'bout that…{w=.3} I'd do anything to keep the little bugger happy."
"He turned towards the kitchen where Sissel was with a fond look."

h "Ya know…"
h "Sis made a good choice in friends when he chose you."
h "You've got this bite about you now,{w=.3} it's a little scary."

"Hershel sighed."
h "I'll keep up my end of the deal.{w=.3} I'll tell him everything once this whole mess of a culinary compeitition is over."
h "But you…{w=.3} you gotta promise to keep Sis safe,{w=.3} alright?"
h "He's gonna need someone to lean on."

"I nodded."

"Several long minutes of silence followed.{w=.3} Neither of us knew what to say."
"Finally,{w=.3} I stood up with a sigh and headed towards the cafe front doors."

m "I think I need some air."

stop music fadeout 5
scene black with Dissolve(3.0)
scene school night with Dissolve(2.0)

"The cool night air hit my face like a cold shower."
"I took a deep breath and sighed."

"There's so much happening at once,{w=.3} it's a little hard to take in…......."

pause(2)
play sound "door.mp3"
"The door behind me creaked open."

j "Sissel's grabbing you a to-go cup of hot chocolate."
j "That should help warm you back to your senses."

play music "grateful.mp3" fadein 2
show jinny neutral with Dissolve(2.0)
"Jinny slid out of the cafe and slowly approached."
"My heart gnawed against my chest quietly as I watched her."
"The last time I saw of her was her charred corpse under the remains of the collapsed cafe."
"And now she's standing in front of me again,{w=.3} alive and well."

"I squeezed my eyes shut."
"The world just doesn't make sense anymore."

j "How are you holding up,{w=.3} buddy?"
"I just stared at her,{w=.3} unsure of what to say."

stop music 
m "I saw you die."
"My mouth blurted it out before my brain could even catch up."

show jinny thoughtful smile with dissolve
"To my surprise,{w=.3} Jinny's expression soften into that sad,{w=.3} knowing smile."
"She opened her mouth as if to say something,{w=.3} and then closed it."
"After a long moment of hesistation,{w=.3} she spoke."
j "Yeah,{w=.3} I know."
j "Me too."

scene white
play sound "noise.mp3"
scene jinny_discovery sepia with Dissolve(1.0)
$ renpy.pause(1.0, hard='True')
show jinny_discovery with Dissolve(1.0)
$ renpy.pause(2.0, hard='True')
scene white with Dissolve(2.0)

play music "tranquil.mp3" fadein 5
scene school night
show jinny thoughtful
with Dissolve(2.0)
pause(1.0)

j "We've both been given a lot of second chances."
show jinny neutral with dissolve
j "Let's do our best this time around,{w=.3} shall we?"

hide jinny with Dissolve(3.0)
"She turned and walked away,{w=.3} slowly disappearing down the dark streets."
"I watched with my mouth agape."
"W-what.........?"

"Jinny…{w=.3} have you been through all of this before?"
".........................the world suddenly felt fragile and cruel."

play sound "ghost.mp3"
"I sighed yet again at a familiar shiver down my spine."
"I just can't catch a break today,{w=.3} can I?"

show halley neutral with Dissolve(2.0)
"Halley's ghostly form appears behind me,{w=.3} arms crossed and looking very impatient."
m "What do you want?"
show halley smile with dissolve
u "And here I thought I'd be nice and comfort you."
u "I guess not."

m "Since when were you ever nice?"
show halley neutral with dissolve
u "I'm trying.{w=.3} You make it very hard."

"Halley glanced at me and wrinkled her nose."
u "Anyway,{w=.3} congrats on being given a second chance to make everything right."
u "You're welcome.{p=.3}You best take care to use this chance wisely."

m "Are you just-"
"I took a deep breath and swallowed my irritation."
"As annoyed as I was,{w=.3} it's probably better to stay on her good side."
"If she even has one."

m "*sigh*{w=.3} Why are you here, Halley?"
m "And why are you helping me?"
u "I…..{w=.3}was asked to be nicer to you."
u "So here I am,{w=.3} babysitting you again."
u "You're going to need it after your little wish got devoured by that creepy muppet-face."

m "Wait,{w=.3} what do you mean?"
m "Time reset,{w=.3} and I'm back in August 9th,{w=.3} before Echo got….{w=.3}devoured."
m "He should be back,{w=.3} right?"

"Halley massaged her temples impatiently."

u "I'm flattered that you think I'm such a powerful wish that I can fully reset time without consequences."
u "But sure."
u "Call for your wish.{w=.3} Let's see if he answers."
stop music fadeout 5
"I gave her and indignant glare before clearing my throat."
m "Ahem."
m "Echo?{w=.3} Are you there?"
".........................................................................................................................."

m "Echo?"
"My voice caught in my throat."
m "C'mon man,{w=.3} I know you're still there-"

u "He's gone, {w=.3}you daft idiot."
"Halley glanced at my torn face and muttered to herself."

play music "water-lily.mp3"
u "Look,{w=.3} I'm sure you're dealing with a lot right now."
u "Lots of trauma and….{w=.3}{i}{b}feelings{/b}{/i} that you mortals always whine about."

u "But you gotta stay functional if you want things to work out this time,{w=.3} got it?"
"She reached over and awkwardly thumped her hand on my head."
"It felt like she was attempting to pet an upset,{w=.3} but very smelly dog."
m "You suck at comforting people."
"Halley settled on smacking me across the head instead."

u "Anyway,{w=.3} every time I reset,{w=.3} there's always some {b}\"spill-over.\"{/b}"
u "Some people might remember bits and pieces from previous cycles,{w=.3} like….{w=.3}Jinny there."
u "Some events might vary drastically."

u "And most importantly,{w=.3} wishes and their actions tend to spill over more easily."
u "That includes the Remnant devouring your wish and becoming empowered."
u "It's still out there somewhere,{w=.3} hunting you down."

"Halley groaned and tugged at her hair in frustration."
u "I could probably reset that part too if I took us back all the way to August 1st,{w=.3} but chances are that you'll forget everything."
u "So we're stuck here,{w=.3} on August 9th."

"Halley made a vague gesture towards the sky."
u "Here’s your second chance.{w=.3} Make things right,{w=.3} change the future,{w=.3} etc."
u "Got any plans?"
u "I sure hope you know what you’re doing,{w=.3} because bringing you back was a massive hassle."

"I scratched my chin thoughtfully, slowly processing Halley’s words."
m "I have some ideas…."

stop music fadeout 8
m "But I’m going to need to talk to talk to someone first…"
m "Someone more connected to this entire situation........"

scene black with Dissolve(2.0)
play music "cafe-music.mp3" fadein 4
scene lake road night with Dissolve(2.0)

"The familiar night scenery of Bradley Woods loomed overhead as I traversed the forest trail."
"The place felt much less scary after our little camping night here."
"The camping trip that.....{w=.3} didn't happen anymore,{w=.3} I guess."
"Halley hovered behind me with a skeptical expression."

show halley neutral with dissolve
u "Why are you looking for the old lake witch again?"
u "If you're looking for a wish,{w=.3} I have all the strength you need if trouble shows rears its head."
m "The Black Lady of Bradley Lake has close ties with both Sissel and Hershel."
m "She's our best bet in sorting out this mess."
m "Plus….{w=.3} I'm not even sure what our goal is."

"Halley frowned."
u "You're trying to reconcile your friend and his uncle,{w=.3} are you not?"
m "That's just the thing."
m "Hershel {i}did{/i} hurt Sissel and his mother in the past.{w=.3} That's a fact."
m "Sissel doesn't really owe him forgiveness."

m "The best we can do is just....{w=.3} get the truth out in the open."
m "The whole truth."
m "From there,{w=.3} we'll just have to let their hearts decide."

"Halley scratched her head and scowled."
u "You mortals are always so complicated…"

stop music fadeout 8
scene cottage night with Dissolve(3.0)

"We walked for a few more minutes in silence."
"Soon,{w=.3} we reached the depths of Bradley Woods."

"As we approached,{w=.3} the dark waters rippled as a large figure slowly rose from the deep."

play sound "ghost-song.mp3" 
pause(1)
show bradley with Dissolve(3.0)
br "I have been expecting you."
"I frowned,{w=.3} puzzled."

m "You have?"

play music "mellow-flute.mp3" fadein 8

br "Yes…"
br "I……{w=.3} remember everything."
br "Hershel's cafe burning down…….. {w=.3}your friend's death……..{w=.3}Sissel running away……"

br "And then I felt the pull of an immensely powerful wish that twisted the world's time back to its previous state."
br "But I can feel some scars remain…"

"She pointed a long,{w=.3} skeletal finger at me."
br "You are one of those scars,{w=.3} as am I."
br "You remember as well,{w=.3} do you not?"

"I nodded slowly."
m "Yeah,{w=.3} I do."
m "And I've been wondering…."

m "Who {i}{b}are{/b}{/i} you exactly?"
m "You're a wish,{w=.3} but who is your wisher?"
m "At first I thought it was Sissel since you're so protective of him…"
m "But the more I think about it,{w=.3} the less sense it makes."

m "Who are you,{w=.3} truly?{w=.3}"
m "Are you an actual ghost of Sissel's mother?"

stop music fadeout 8
"Bradley tilted her head,{w=.3} looking a bit hesitant."
"And then she raised one of her thin,{w=.3} skeletal hands from her mass of hair and gently placed it on my forehead."
"And then the world went white."

scene white with Dissolve(3.0)
pause(3)
play music "mother.mp3" fadein 5
scene cecilia_death1 with Dissolve(5.0)
pause(3)

"The waters of Bradley Lake were stained red."
"Water filled her lungs as she slowly bled out,{w=.3} sinking deeper into the water's depths."
"Her arms wouldn't move…{w=.3} She was not even sure if her legs were present anymore..."

scene cecilia_death2 with Dissolve(4.0)
pause(3)
"There was no more fight left in these bones."
"Cecilia strained her head towards the surface,{w=.3} squinting through the cloudy water."

"They say that at the brink of death,{w=.3} one's life flashes before their eyes."
"Cecilia wonders if she's ever done anything truly worthwhile."
"All she could see were regrets."

"She could never be the sister that Hershel needed,{w=.3} or the mother that her child deserved…"
"And now she would never have the chance to."

scene cecilia_death3 with Dissolve(4.0)
pause(3.0)

"What remained of her heart lutched against her chest as she closed her eyes."
cc ".....Sissel…"
cc ".....You deserve more than a future stained by my mistakes."
cc "I hope you live a happy,{w=.3} fulfilling life..........{w=.3} even if I can't be there for you."
"The world was growing dark and cold."
"Cecilia could feel the last bit of warmth drain from her."
"Sleep slowly threatened to pull her under....."
"........................"
pause(2)
cc "For what it's worth....{w=.1}I love you."

scene cecilia_death4 with Dissolve(4.0)
pause(3)

scene white with Dissolve(2.0)
pause(2)

"I breathed in sharply and stumbled backwards."
"I looked up at Bradley."

scene bradley_request1 with Dissolve(3.0)
pause(3)
"She looked down at me and gently pressed her hand against her own chest."

br "I am the last,{w=.3} dying breath of Cecilia Bradley."
br "Her last words.{w=.3} Her dying wish."

br "She wanted to protect her son and give him a happy,{w=.3} fulfilling life."
br "But….{w=.3} I've always felt like a failure of a wish."
br "I am bound to the waters of Bradley Lake,{w=.3} and as he grew older,{w=.3} Sissel was constantly out of my reach."
br "I could never give him the guidance he needed,{w=.3} nor the parental affection he craved."

br ".................."
br "All I could do was watch him suffer from afar."

scene bradley_request2 with Dissolve(2.0)
pause(1)

"She bowed her head shamefully."

br "Please,{w=.3} I need your help to fulfill my duty as a wish,{w=.3} dear wish-granter."
br "I have failed long enough,{w=.3} I cannot do this alone…."

scene black with Dissolve(2.0)
scene cottage night with Dissolve(2.0)

show bradley with dissolve
"Bradley looked so vulnerable in this moment."
"I smiled softly and gently held her hand."

m "I understand….{w=.3} I love Sissel a whole lot too."
m "You have my word,{w=.3} I will do everything I can to make this right."

"I swear I could almost see a grateful smile under that mass of tangled hair."
br "Thank you…..{w=.3} thank you so much…"

"I stared up at her with a determined grin."
m "And I think I have a plan…."

show bradley at left with dissolve
show halley neutral at right with dissolve
u "You {i}think{/i} you have a plan?"
"I glared behind me at Halley."

m "Do you mind?"
m "We were having a moment."

"Halley shrugged nonchalantly."
u "Oh right,{w=.3} you were having \"feelings.\""
u "Forgot that was a thing."
u "Doesn't matter either way,{w=.3} I don't really trust your planning skills."

m "Well I don't see you coming up with anything-"

"Bradley awkwardly raised her hand like a student in a kindergarten class."
br "I also have a plan if you all are willing to listen….."

"Halley and I exchanged surprised glances,{w=.3} but turned towards Bradley and nodded."

scene black with Dissolve(3.0)
scene repeat_screen with Dissolve(1.0)
pause(1.5)

scene black with Dissolve(2.0)

show sissel tarot b at rcenter with Dissolve(2.0):
            xzoom .5 yzoom .5
pause(3)


jump day10_sissel_b
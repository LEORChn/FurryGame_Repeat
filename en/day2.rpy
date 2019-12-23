#DAY 2
label day2:
$ persistent.current_route = "default"
"{b}Day 2{/b}:{w=.5} Unknown Entity"

stop music fadeout 2
scene black with Dissolve(3.0)

e "{size=-10}...[charname]...{/size}"
e "{size=-10}..............[charname], wake up.{/size}"
e "{size=-10}...ugh, you always do this.{/size}"
e "{size=-10}Where's the mini-fridge...?{/size}"
"..."
"........"

play sound "water-splash.wav"
play music "carefree-tune.mp3"
m "{i}{size=+20}-HOLY SHIT IT'S FUCKING COLD!!!!!!!!!!!!!!!{/size}{/i}"

scene dorm with dissolve 
show echo neutral with dissolve

e "Good morning [charname]. Did you sleep well?"

m "{i}What the hell is wrong with you?!{/i}"

e "You weren't waking up and your fourth alarm clock went off already."
e "I'm just looking out for you, little man."

m "I'm soaked! {i}Again!{/i}"
m "And you poured it all over my crotch too!"

e "You're going to shower in a bit anyways, so why does it matter?"
e "Plus you might want to find Phillip before he burns down the whole building."

hide echo neutral
with dissolve
show echo blurry with dissolve
hide echo blurry with dissolve

m "What?"

"Now that he mentioned it, the air was thick with the smell of burnt toast."
"Like, suffocatingly thick."

m "Ugh, is every morning going to be like this?"

"I climbed out of my (wet) bed and hobbled across the dorm to grab my clothes."
"Guess it's time to go shower. And save the dorm from Phillip's breakfast."
"Ugh, stupid ghosts."

scene dorm hallway
with dissolve

show phillip neutral
with dissolve

p "Oh good morning [charname]! Sorry, did the smell wake you up-?"
show phillip no with dissolve
p "...uh, why are your boxers soaked?"

m "Ugh, don't remind me. It's not what you think it is."
show phillip neutral with dissolve
p "Ooookay, if you say so~"
m "Anyway, why does it smell like a bakery-fire in here?"

p "It's a loooong story."
show phillip annoyed with dissolve
p "Well first of all, it turns out that Owen sleeps nude."

m "What does that have to do with anything?"

show phillip annoyed look with dissolve
p "He shows off.{w=.3} Like, a lot."

show phillip neutral with dissolve
p "So I woke up early to make breakfast."
p "But I was half asleep so I wasn't really paying attention-"
p "And then the toaster caught fire for whatever reason, so I had to put it out."

m "....wow. You're a mess."

p "Hey, cut me some slack,{w=.3} this was my first time using a toaster."
p "And there's nothing to worry about. The fire alarms didn't go off!"

m "I'm not sure how safe I feel about that."
p "Eh sorry. I've never been a good cook back at home."

menu:
    "You gotta {i}rise{/i} to the occasion, it's the {i}yeast{/i} you can do.":
        m "You gotta {i}rise{/i} to the occasion, it's the {i}yeast{/i} you can do."
    "Sounds like you {i}knead{/i} some practice.":
        m "Sounds like you {i}knead{/i} some practice."
    "There's always a little {i}margarine{/i} for error.":
        m "There's always a little {i}margarine{/i} for error."


p "Wow, and you say my puns are bad."
m "All puns are bad, period."

hide phillip neutral
show phillip smile shrug
with dissolve

p "I do {i}relish{/i} the fact that you've {i}mustard{/i} the strength to {i}ketchup{/i} to me."
m "That was physically painful to listen to."
p "Haha, weakling."

play sound "bump.mp3"

show phillip no with dissolve

"Phillip suddenly jumps as one of the dorm rooms opens behind him."
p "Oh, that would be Owen."
"Phillip speedwalks down the hall with a deadpan look on his face."

p "I'll see you around [charname]!"
"I think I heard him whisper \"Good luck!\" under his breath. That poor kid."

hide phillip neutral with dissolve

stop music fadeout 2
play music "happy_lounge.mp3"

show owen underwear at left 
with Dissolve(2.0)

o "Mornin' [charname]. How's it going?"
o "....and why are your boxers all wet?"

m "It's not pee if that's what you're thinking."

o "Ooooh, I see~ Had some sweet dreams last night, didn't you?"
m "THAT'S NOT IT EITHER"
o "Hey don't worry about it man. Your secret's safe with me."

m "Ugh, I don't even know where to start with you."
m "Are you always this flirty?"

o "That's just how I roll."

show sissel annoyed at right
with Dissolve(2)

s "Will you people put some fucking clothes on?"
o "Oh, mornin' to you too Sissel."
"Owen grinned and winked.{w=.3} I guess that's just his normal morning greeting."

s "Oh damn it,{w=.3} you're here too?"
s "Do you always have to lounge around like you own the place?"
o "Well I've lived here for like 7 years,{w=.3} might as well make myself comfortable."
o "Welcome to Gerania by the way!{w=.3} Glad to see you off the streets and rejoining civilization."

show sissel neutral with dissolve
s "...You're a fucking twat,{w=.3} you know that?"
o "What?{w=.3} I was just trying to be friendly!"
o "By the way,{w=.3} we gotta go on a shopping trip sometime."
o "You need to wear something other than ripped rags, my dude.{w=.3} I know this really good shop downtown-"

"Sissel growled and stomped his way down the hall."
s "I forgot how irritating it was to hang around you."
o "W-wait,{w=.3} I didn't mean anything by it-"
hide sissel with Dissolve(2.0)

o "-Aaaaaand he's gone."


"Wow, that went as well as expected."
"Maybe I should follow Sissel?{w=.3} Then again, it might be better to have a word with Owen too."

menu:
    "Go check on Sissel":
        m "Uh, I'll see you around Owen!"
        o "'Kay, good luck [charname]."
        
        hide owen underwear
        with dissolve
        
        "I jog down the hall in the direction Sissel went, but man that guy was fast."
        "It took a few loops around our floor, but I finally found Sissel sulking in the lounge area."
        
        m "Sissel!{w=.3} Wait up!"
        
        show sissel neutral with dissolve
        s "What do you want-"
        
        show sissel wtf with dissolve
        s "Actually, {w=.3}you mind putting some clothes on first?"
        show sissel wtf blush with dissolve
        s "I don't need to see you bumbling down the hall in your underwear first thing in the morning."
        
        m "Gah, I forgot.{w=.3} I was about to shower before I got caught up between you and Owen."
        
        show sissel neutral with dissolve
        s "Then go shower and stop bothering me."
        s "Teach always warned me to never talk to strange,{w=.3} naked men."
        
        m "Hey,{w=.3} I'm not {i}that{/i} strange..."
        m "I was just a little worried about you,{w=.3} that's all!"
        m "You looked awfully upset when you left me and Owen earlier."
        
        show sissel upset with dissolve
        s "Well that's because Owen's just an insensitive dumbass sometimes."
        s "His rich-ass family background doesn't make it any easier."
        s "It's all deep pockets and shallow thoughts with that one."
        
        show sissel annoyed with dissolve
        s "{i}\"Oh let me constantly remind you that you're dirt poor and at the bottom of the barrel~!\"{/i}"
        s "{i}\"You look awful!{w=.3} Here's some money. That'll fix you right up!\"{/i}"
        
        show sissel upset with dissolve
        s "I mean for fuck's sakes,{w=.3} I'm trying to turn a new leaf here."
        s "I don't need him to play the philanthropist card all the time,{w=.3} I can do things on my own."
        "Sissel eyed me suspisciously."
        
        m "Well I guess Owen was being a little tactless back there..."
        m "But I think he's got his heart in the right place.{w=.3} He's just kinda bad at showing it?"
        
        s "Yeah,{w=.3} I {i}know{/i} he's a nice guy.{w=.3} I've known him since we were kids."
        s "It's just- {w=.3}AAAAAAAAAH he really pisses me off sometimes,{w=.3} you know-?"
        
        show sissel neutral with dissolve
        "Sissel seemed to suddenly catch himself in the middle of his outburst and glanced at me suspiciously."
        
        if steal_wallet == "true":
            s "Why do you care?"
            s "You stole my wallet yesterday and now you pretend to be all sentimental?"
            s "I don't buy it."
        if steal_wallet == "false":
            s "You're being awfully.....{w=.3} nice."
            s "First you return my wallet,{w=.3} now you're trying to play peace-maker?"
            m "Well,{w=.3} you're being awfully suspicious."
            
        m "I'm just trying to be a good person and make friends and whatnot!"
        m "You looked upset and I figured you might want someone to vent to."
        
        s "I guess it's nice to have someone listen to my yapping but..."
        "Sissel glared at me warily."
        
        show sissel indignant with dissolve
        "Then he realized he was staring at my half-naked body and quickly looked away."
        s "A-anyway,{w=.3} I don't care!{w=.3} You can do whatever you want."
        s "I'll be heading to the kitchen and making breakfast."
        
        "Hmm,{w=.3} food does sound pretty good right about now."
        "My stomach suddenly let out a high-pitched growl."
        
        show sissel neutral with dissolve
        
        s "Hungry,{w=.3} aren'tcha?"
        s "Tell you what,{w=.3} come along with me.{w=.3} I'll whip up one of my famous omelettes for you."
        m "R-really?!"
        
        s "Consider it thanks for buying me that sandwich yesterday."
        s "I guess I'll try out that whole....\"be a good person and make friends\" schtick of yours."
        
        m "I think I'm in love."
        
        show sissel embarrassed with dissolve
        s "Alright, you can shut up now.{w=.3} You're making it weird."
        
        scene kitchen
        with Dissolve(2.0)
        play music "cafe-music.mp3" fadein 2 fadeout 2
        
        "Sissel and I walked in to find a complete mess. The kitchen looked like a warzone."
        "There was a huge back burn mark where the toaster was, and the air was thick with the smell of burnt toast."
        
        show sissel neutral
        with dissolve
        
        "Sissel looked horrified as he ran to open a window."
        m "Oh right, Phillip totally wrecked the place earlier."
        s "How the hell do you manage to blow up a toaster?!"
        s "Well at least the kitchen's still usable.{w=.3} You ready for this?"
        
        "Sissel opens the fridge and grabs a few eggs and strips of bacon."
        s "Huh, Owen restocked all the food in the fridge again.{p}Probably the only good that twat's ever done."
        m "He seems like a pretty okay guy..."
        "Sissel gave me a nonchalant shrug before continuing making breakfast."
        
        "He moved so naturally when he's mixing and cooking the ingredients. He's probably done this quite a bit before."
        "It was mesmerizing to watch really, the graceful way he transitions from chopping tomatoes to flipping eggs."
        "Sissel's usually frowning face is absent, replaced by a soft look of content."
        
        s "Your omelette and bacon is done, [charname]."
        s "I would have made toast too if Phillip didn't blow up the toaster."
        "Sissel bowed while trying to hide a proud smirk."
        s "Prepared to be blown away by my handiwork."
        
        m "I'm prepared to be blown."
        "Sissel shot me an exasperated look."
        s "You really are a shameless twat."
        m "Shameless and proud."
        s "Just eat your damn food."
        
        "Sissel began forking his first bite of his fabled omelette and I followed suit."
        
        m "W-wow, this is actually pretty good."
        s "Damn right it is."
        
        "Sissel's trying to play it cool but his face is flushed with pride.{p}He looks so happy."
        "It seems like he doesn't get the chance to cook for other people much."
        m "How did you learn to cook so well? This tastes practically professional!"
        
        show sissel happy with dissolve
        s "I-it's not {i}that{/i} good, is it?"
        s "I've worked a ton of jobs as a kid, and the longest one I've held was at this bakery."
        s "My Boss taught me a lot of stuff about cooking and baking and whatnot."
        s "I owe a lot to him.{w=.3} He kinda just grabbed me off the street as a kid and took me under his wing."
        m "He sounds like a pretty good Boss."
        "There was a fond look on Sissel's face, but with a hint of sadness too."
        "I wonder if he's alright..."
        
        play sound "bump.mp3"
        
        show phillip neutral with dissolve
        
        p "Hey guys,{w=.3} have you seen my bag? I think I left it in here-"
        show phillip no with dissolve
        play music "carefree-tune.mp3" fadein 2
        
        p "Wow,{w=.3} nice lack of clothes there,{w=.3} [charname]."
        p "Sorry if I interrupted something."
        
        hide phillip with dissolve
        "Before we could say anything,{w=.3} Phillip quickly grabbed his bag and ran out."
        
        m "What was that about?"
        
        play sound "bump.mp3"
        show phillip annoyed look with dissolve
        
        "Phillip suddenly ducked his head back through the door."
        p "There better not be sinning in the kitchen."
        
        show sissel surprised with dissolve
        s "Wait no,{w=.3} it's not what it looks like-"
        p "-if sinning occured,{w=.3} I expect every surface here to be desantised twice over when you're done."
        
        hide phillip with dissolve
        "And then he was gone."
        
        "Sissel's face looked like a very angry tomato.{w=.3} Did I miss something-?"
        "And then the realization hit me."
        "I was still in my boxers.{w=.3} From Phillip's view to the table, it probably looked like I was naked."
        
        show sissel embarrassed with dissolve
        s "I-I-I'm gonna go."
        s "Better explain to Phillip before he gets any weird ideas."
        s "Enjoy your food [charname]."
        
        hide sissel with dissolve
        
        "And with that, Sissel ran out the room in a flustered mess,{w=.3} leaving only me and my half-eaten breakfast."
    "Stay and talk with Owen":
        show owen underwear at center with dissolve
        
        m "What's going on between you two?"
        m "Sissel looked about ready to deck in you in the mouth."
        o "Eeh,{w=.3} it's always been like this between us."
        o "Believe it or not,{w=.3} Sissel and I used to be pretty buddy-buddy~"
        
        m "That's a little hard to believe..."
        o "No seriously!{w=.3} We used to hang out all the time as kids."
        o "He was one of my only friends.{w=.3} The two of us were pretty inseperable!"
        
        m "You two look pretty seperated at the moment."
        m "Did something happen?"
        
        "Owen scratched his head awkwardly."
        
        o "Life happened,{w=.3} I guess."
        o "Sissel kept working a bunch of different jobs,{w=.3} and I kinda did my own thing."
        o "We hung out a lot less and eventually not at all..."
        
        o "I guess we just kept rubbing each other the wrong way."
        m "Maybe you should stop mentioning stuff that makes him angry."
        m "You two could benefit from a little heart-to-heart."
        
        "Owen laughs with a defeated grin."
        o "Ha!{w=.3} You're not the first to tell me that."
        o "One of our other friends kept trying to get us back together too."
        o "That's hard to do when Sissel glares daggers into me every time he sees me."
        
        
        "He shook his head dismissively before looking up at me with a smirk."
        o "Anyway!"
        o "Enough talk about other people [charname],{w=.3} let's talk about {i}us{/i}"
        
        "I blinked at him blankly."
        m "Us?"
        
        o "Two guys hanging out wearing nothing but their underwear?"
        o "This could go in quite a few directions~"
        "As he says this, Owen stretches his arms over his head and leans back."
        "His boxers slipped down his waist slightly,{w=.3} revealing more of his lower naval."
        "My face flushed with heat."
        
        stop music
        play music "carefree-tune.mp3"
        
        o "Yo [charname], my eyes are up here."
        m "W-w-what? Sorry! I wasn't-"
        
        "Owen winked at me."
        o "Wanna shower together?{w=.3} You have to clean up your boxers anyway."
        
        m "DEFINITELY NOT."
        m "Although a shower does sound pretty good right about now..."
        
        o "Heh, I knew you couldn't resist-"
        
        m "{size=+10}WE'RE SHOWERING SEPERATELY{/size}."
        
        scene shower room
        with Dissolve(2.0)
        stop music fadeout 3
        
        "The shower room was pretty clean and crisp for a school dorm."
        "I groan and finally strip off my soaked boxers. That damn camera ghost is more trouble than he's worth."
        "As the steamy warm water rains down on me, I give a happy sigh and reach for the soap."
        "I really needed this."
        
        "Suddenly a movement catches my eye and I glance around behind me."
        play music "in-your-arms.mp3" fadein 5 fadeout 3
        "E-E-EH?!!"
        "I-it looks like Owen didn't bother to close his shower curtain."
        "He's practically on display here! Isn't he worried someone might see?!"
        
        "Mmmph, I-I probably won't get another chance like this. Should I sneak a peek?"
        
        menu:
                "Peek at Owen.":
                    "I took a deep breath. C'mon [charname], this is a once in a lifetime opportunity."
                    "Sticking my head out of my shower stall, I squint through the thick steam in the room."
                    
                    
                    show shower at Position(xpos = 1, xanchor=1, ypos= 1, yanchor=1) with Dissolve(2.0)
                    show shower at Move((1, 1), (.5, .6), 20,
                        xanchor="center", yanchor="center")
                    
                    
                    "W-wow, Owen really does have a nice body.{p=.3}With that much muscle, he probably works out a lot."
                    "He's pretty well-hung too. I guess all that swagger isn't there just for overcompensation."
                    "Owen reaches for the shower sponge and begins rubbing soap all over himself."
                    "I can feel a bit of drool pool in my mouth as he lathers all over his crotch region."
                    
                    show shower at Position(xpos = .5, xanchor=.5, ypos=.5, yanchor=.5)with Dissolve(1.5):
                        xzoom .5 yzoom .5
                    
                    pause(1.5)
                    
                    "Owen's dick hardens and almost as if to tease me, he grabs it and gives it a few strokes."
                    "Slowly, his glistening cock grows to full mast as his lewd pumping continues, pre beginning to leak from the tip."
                    "I could hear Owen let out a low, {w=.3}husky groan as he slides down the shower wall, completely soaked in his own pleasure."
                    "His dick was throbbing in rhythm with his hand, a steady stream of pre-cum leaking onto the shower floor."
                    "The stroking quickens as Owen groans louder. {w=.3}He was growing close."
                    "Abruptly, Owen lets out a whimper as shot after shot of cum erupts,{w=.3} splattering the shower walls."
                    
                    stop music fadeout 3
                    scene shower room with Dissolve(2.0)
                    
                    m "W-wow, that's a whole lot..."
                    
                    
                    show owen naked with dissolve
                    o "Enjoying the show, aren't ya?"
                    play music "hyperfun.mp3"
                    m "IIiiiiIIiiiieeeeehhhyaaaaaaaaaaaaaaaaaaa-!!!!"
                    
                    "Owen was suddenly leaning close to me, resting a seductive arm on my shoulder."
                    o "Wow [charname], {w=.3}I didn't know you were such a perverted peeping tom~"
                    m "I-I-I-!!!"
                    "I think my brain just flat-lined."
                    m "P-pervert?! {p=.3}I should be saying that to you!"
                    o "But hey, {w=.3}at least I actually admit to it hehe~"
                    o "Say [charname], {w=.3}if you ever want any fun together,{w=.3} no strings attached, let me know~"
                    o "Being a pervert is no fun when you're alone <3"
                    hide owen with dissolve
                    "Owen winks and nuzzles my cheek before returning to this shower."
                    
                    
                    "I duck back into my own shower stall, my heart hammering in my chest."
                    "Ookaaaay [charname], that's enough for one day."
                    "Owen was humming away loudly in the other stall as I quickly finished up my own shower."
                    "Once I got out, I groaned and smacked my head against the shower room wall."
                    "This is going to be a long day..."
                "Go to church and pray for forgiveness.":
                    jump dont_peek
                "Don't peek.":
                    jump dont_peek
                    
                    
                    label dont_peek:
                        "Nah, it's best that I don't risk it. If Owen catches me, I'd never hear the end of it."
                        "I focus back on my own shower and wash off the morning daze."
                        "I'm going to need it if today's anything like yesterday's fiascos."
                        
                        o "Yo [charname]!"
                        m "H-huh?!"
                        
                        "I jump as Owen's voice rings out from across the shower room."
                        o "Are you sure you don't want a peek buddy? Haha I saw you sticking your head out!"
                        m "Wah-?! I didn't-! GAH!"
                        
                        "Owen's laugh echoed through the shower rooms and stayed in my head throughout the rest of the morning."
                        "I groaned and smacked my head against the shower room wall."
                        "This is going to be a long day..."
                        jump day2_morning

    
label day2_morning:
    
stop music fadeout 2
scene black
with Dissolve(5.0)

play music "snowy-street.mp3" fadein 2 fadeout 3
scene lecture hall
with Dissolve(2.0)

"Writing workshop was a class required for all students,{p}which is why I'm listening to an incredibly boring lecture{p=.1}while my sanity slowly drained away."
"Students with various core subjects were stuffed together into one big lecture hall,{p=.2}many of whom are yawning violently into the morning sun."
"I really don't blame them."
"The teacher of the class was Mr. Dorcas Dolores,{p=.1}and God does he have a monotone voice."
"It's taking 110\% of my concentration to stay awake.{p=.1}But what I really need is something to kill this boredom."
"Distractions, pranks, conversations, just give me SOMETHING!"

"With a sigh, I glance at the other students in the room."
"Conveniently, I was seated at the center.{p=.1}Just far enough that the teacher won't bother me, but too close to actually take a nap."
"Sitting next to me was Phillip,{p=.1}who (like everyone else) was ignoring everything Mr. Dolores was saying.{p=.1}He's just happily doodling in his notebook."
"The little guy looks like he's having the time of his life. {p} I wish I had that kind of strength."
"I think Sissel is sitting somewhere in the front.{p=.1}His head is resting on his arm, fast asleep."

"Meanwhile, Owen's at the back of the class. {p}Why is he staring at his own glowing crotch?"
"Oh wait, that's his phone. He's hiding it under his desk.{p} I think.{p} {i}I hope.{/i}"

"Welp, sitting here observing isn't going to cure my boredom."
"What should I do?"

menu:
    "Stare at Phillip creepily until he notices.":
        "I turn around and scrunch up my face,{p=.1}boring into Phillip's forehead with my eyes."
        "Wow, I really am going insane."
        "Phillip doesn't notice at first, but he squirms and frowns at his notebook."
        "After a while, he glances up at me with great concern."

        show phillip annoyed with dissolve
        p "[charname], are you ok? You look constipated."
        m "W-what? Nah,{w=.3} I was just wondering what you were drawing!"
        m "And I'm kinda bored out of my mind.{w=.3} This class is unbearably boring."
        
        show phillip neutral with dissolve
        p "Well you're right about that."
        show phillip annoyed look with dissolve
        p "This teacher...{w=.3} Dorcas Dolores was it?{w=.3} He's got the most monotone voice I've ever heard."
        p "He's just reading word-for-word out of the textbook too!{w=.3} Does this even count as teaching?"
        
        "I glanced up at the classroom."
        m "Isn't he that really rude teacher who yelled at us yesterday?"
        m "He kinda gives off that \"I don't even want to work here\" vibe."
        m "Makes you wonder why he even became a teacher in the first place."
        show phillip neutral with dissolve
        p "Summer holidays, probably."
        p "Or maybe his parents didn't love him as a child."
        
        show phillip annoyed look with dissolve
        p "You can tell because his name is Dorcas Dolores."
        p "{i}Who names their kid that?!{/i}"
        p "No wonder why he grew up to be a cranky old rat."
        
        m "You sound like you {i}really{/i} don't like him."
        show phillip serious with dissolve
        
        p "Authority figures who are awful for no reason just really annoy me."
        p "I mean,{w=.3} it's so easy to not be an asshole!"
        
        play sound "slam.wav"
        stop music
        show lecture hall at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        hide phillip
        "There was a sudden ruckus at the front of the classroom."
        "Apparently Mr. Dolores caught Sissel sleeping in class and smacked his desk with a textbook."
        
        d "Slacking off in class,{w=.3} are you?!"
        d "God knows why the academy accepted a street rat like you when you're clearly incapable of even paying attention-"
        
        show sissel upset with dissolve
        s "Well it ain't my fault you're as dull as a brick."
        s "This ain't exactly a good class when you can just replace your talking with a Youtube video-"
        
        "Mr. Dolores slammed his fists against the desk and glared at Sissel dangerously."
        d "Listen hard,{w=.3} kid."
        d "This is my classroom,{w=.3} and you will follow {b}my{/b} rules while you're in here."
        d "And I say:{w=.3} Any student who isn't worth my time will {i}leave{/i}."
        d "Got it?"
        
        "Sissel looked like he wanted to argue back,{w=.3} but thought against it."
        hide sissel with Dissolve(2.0)
        "The class silently watched as he grabbed his bag and stomped out of the room."
        
        d "....Anyway,{w=.3} where were we before we were so rudely interrupted-?"
        
        m "Wow,{w=.3} what a dickbag."
        show phillip serious with dissolve
        p "....that guy's got some nerve......."
        p "I've got just the thing-"
        p "Huh?"
        
        "Phillip rummaged his pockets with a frustrated huff."
        show phillip neutral with dissolve
        
        p "Hey [charname],{w=.3} you wouldn't happen to have a penny I can borrow?"
        m "A penny?"
        m "Yeah,{w=.3} I've got one here."
        m "What do you need it for?"
        
        show phillip smile shrug with dissolve
        p "Sweet karma and justice."
        
        show phillip serious with dissolve
        
        "Phillip flipped the coin into the air before catching it in a closed palm and whispering quietly into his hand."
        "I watched with fascination."
        "What was he doing?"
        
        hide phillip with dissolve
        
        show echo blurry with Dissolve(1.5)
        play sound "ghost.mp3"
        e "[charname]!"
        
        m "W-what?!"
        m "Holy fuck,{w=.3} don't pop out of the blue like that!"
        m "You scared the hell out of me."
        
        e "Do you feel it?{w=.3} There's something here..."
        e "Something unnatural...."
        
        hide echo with dissolve
        
        "What was he talking about?"
        "Was there another ghost thing around-?"
        
        play sound "chains.mp3" 
        "My mind was suddenly echoing with the faint sound of chains clattering together."
        "What the hell is going on...?"
        
        play sound "bell.wav"
        play music "scheming.mp3" 
        "The classroom suddenly shook as the fire alarms began roaring to life."
        "As we all automatically scambled onto our feet,{w=.3} something weird happened."
        
        "A single sprinkler at the front of the class went off and showered Mr. Dolores with ice-cold water."
        
        play sound "surprise.mp3"
        show lecture hall at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        "As the cranky teacher screamed in dismay,{w=.3} a ceiling tile fell and crashed onto him,{w=.3} showering him in grim and dust."
        "The debris clung onto his wet skin,{w=.3} making Mr.Dolores look like a wet blob of white dough."
        
        "The class collectively snickered to themselves before quickly filing out of the room."
        "Mr. Dolores began shouting and spluttering about the incompetence of the maintenence staff as we all left him behind."
        
        "I spared a glance back at Phillip just in time to hear him whispering something under his breath."
        show phillip neutral with dissolve
        
        p "{size=-15}Nicely done, Mimir...{/size}"
        
        m "What the-"
        m "How did you do that?!"
        
        show phillip smile shrug with dissolve
        
        p "Huh?{w=.3} Do what?"
        p "I have no idea what you're talking about."
        m "But-"
        
        show phillip neutral with dissolve
        p "Anyway,{w=.3} the fire alarm's ringing [charname]!"
        p "Let's hurry up and get out of here!"
        
        m "Wah?"
        m "B-b-but-???"
        
        "I remained speechless as Phillip laughed and dragged me out of the lecture hall."

        
    "Text Owen.":
        "I sigh and pull out my phone discreetly under my desk."
        "Luckily, Owen gave me his number yesterday in case I needed anything."
        "I'm sure he was just trying to helpful {i}without any ulterior motives whatsoever."
        
        "With a sigh and a click, I sent him a text."
        m "{i}Help I'm dying."
        
        "After a few moments my phone buzzed in reply."
        o "{i}Need some mouth-to-mouth resuscitation, bud? ;)"
        m "{i}No, my death by boredom is imminent."
        m "{i}There is only one cure.{p=.1}I demand you tell me an amusing story."
        o "{i}Haha I'm not much of a storyteller."
        m "{i}Are you going to leave me helpless and dying? So cruel."
        o "{i}Ok ok, so a good story..."
        
        o "{i}Once upon a time, there was a handsome young prince who lived in the kingdom of Gerania."
        o "{i}He was the most handsome and charming man there ever was."
        
        m "{i}Does his name happen to be Owen?"
        
        o "{i}DON'T INTERRUPT"
        o "{i}But yea, his name happens to be Owen.{p=.1}Nice guess."
        o "{i}Anyway, Prince Owen was strolling about his kingdom when he happened upon a looming tower."
        
        o "{i}Upon approaching this mysterious tower,{p=.1} an ugly old man by the name of Dorcas Dolores stood in his way."
        o "{i}(He is in no way related to our Writing Workshop teacher btw.)"
        
        m "{i}Of course."
        
        o "{i}Anyway, our noble and handsome prince approached the ugly hag."
        o "{i}\"I demand you tell me the purpose of this tower!\" the handsome Owen shouted."
        o "{i}\"Shut up and do your homework,\" the hag replied."
        
        o "{i}Prince Owen was enraged. How dare this ugly man suggest such a demeaning activity?"
        m "{i}I'm starting to get a good picture of your study habits."
        
        o "{i}[charname], what did I say about interrupting?"
        m "{i}Whoops sry"
        
        o "{i}Back to my amazing story:"
        o "{i}\"I will rescue the fair princesses from your clutches!\" Prince Owen roared and drew his awesome sword."
        o "{i}\"Call your parents and apologize for being such a disappointment,\" the Dolores hag hissed.{p=.1}Prince Owen cried a little."
        m "{i}Ouch, that's harsh."
        o "{i}I know, right?"
        
        o "{i}Suddenly Dorcas Dolores swelled and transformed into a giant disgusting rat,{p=.1}with wrinkly skin like an oak tree and stinky yellowed teeth."
        o "{i}His hair was a tangled serpentine mess and his chin grew to look like a shapely ballsack."
        o "{i}Upon reflection, Owen didn't think the Dolores looked all that different from before."
        
        m "{i}That's just cruel."
        o "{i}You know it's true."
        
        o "{i}The hag lunged at the noble prince,{p=.1}but Owen was much too quick."
        o "{i}With a quick stab of his golden sword, Owen pierced the beast in the heart."
        o "{i}It died."
        
        m "{i}That's a bit anti-climatic."
        
        o "{i}ITS SCREAMS ECHOED THROUGHOUT THE WHOLE KINGDOM AS BLOOD SEEPED FROM ITS LAST WOUND.{p=.1}THE HAG SLUMPED TO PRINCE OWEN'S FEET AND RASPED \"NOBLE PRINCE, YOU'VE BESTED ME.\""
        o "{i}And then it died."
        
        m "{i}That's a lot of sass in one text message."
        
        o "{i}Prince Owen entered the tower to search for the princesses and immediately went to the basement."
        o "{i}Cuz the top of the tower was too obvious a place to look."
        m "{i}Of course."
        
        o "{i}He found the pretty princess Sissel and he immediately leapt into the prince's arms."
        o "{i}\"Oh noble prince!\" princess Sissel cried. \"You are the bravest among men! I am so sorry I broke your ribs last summer!\""
        o "{i}\"It's fine please get off of me,\" the fair prince said."
        o "{i}\"Oh prince Owen!\" Sissel cried again. \"Come closer so I may touch your glorious body~!\""
        o "{i}Prince Owen was, at this point, totally creeped out.{p=.1}So he left the weird-ass princess in the basement and went to the top of the tower instead."
        
        o "{i}Oh,{w=.3} and the castle basement spontaneously combusted into flames.{/i}"
        o "{i}There's fire everywhere.{/i}"
        o "{i}Let's hope he finds the fire exit.{/i}"
        
        m "{i}Sissel's going to murder you."
        o "{i}He's never going to find out."
        
        o "{i}Anyway, at the top of the tower,{p=.1}the noble Owen found the beautiful princess Phillip standing on the edge of the balcony."
        o "{i}\"Oh cruel world,\" the princess sobbed. \"Will I ever be free from this torture? Perhaps I should just jump and end it all...\""
        o "{i}\"No fair princess!\" Owen cried. \"I will free you! Together, we will live in peace and happiness!\""
        o "{i}Princess Phillip gratefully accepted.{p=.1}And so they rode off into the sunset and lived happily ever after."
        m "{i}That was actually a pretty good story."
        o "{i}And then the two had hardcore sex for the rest of the night."
        m "{i}You just had to ruin it, didn't you?"
        
        o "{i}That's my job [charname] :P"
        
        "My phone suddenly buzzed again, but this time the message was not from Owen."
        
        play music "carefree-tune.mp3" fadein 1
        
        s "{i}Do you twats realize that you've been sending group messages this entire time?"
        p "{i}I don't think I can room with Owen peacefully anymore."
        s "{i}\"COME CLOSER SO I MAY TOUCH YOUR GLORIOUS BODY???!??!?!\""
        s "{i}DO YOU HAVE A FUCKING DEATH WISH?!"
        p "{i}I would have just jumped."
        s "{i}WHY THE FUCK ARE WE THE PRINCESSES?!!"
        o "{i}B-b-but you gotta admit it was a good story!"
        p "{i}At least I got the happy ending. Sort of."
        o "{i}See? Phillip agrees!"
        s "{i}GOOD STORY MY ASS YOU'RE DEAD AS SOON AS THE BELL RINGS YOU SHIT EATING-"
        
        "At that point I turned my phone on mute and sighed. That was one hell of a journey."
        "I turned to see Phillip covering his mouth with stifled laughter{p=.1}while Sissel was furiously texting in front of the classroom, {w=.3} much to Mr. Dorcas' dismay."
        "Owen didn't even bother trying to hide his laughter."
        "It echoed through the classroom, drawing attention from both confused classmates and an angry Mr. Dolores.{p=.1}This guy is just too much."

 
stop music fadeout 3
scene black with Dissolve(5.0)
    
scene art room with dissolve
play music "easy-lemon.mp3" fadein 2 fadeout 2

"I groaned as I stared at the photography assignment I was damned with for the next 3 days."
c "Do not use that tone with me, Mr. [charname].{p=.1}This is an important photography exercise that tests your understanding of lighting."
c "During the next 3 days, everyone will take 3 photographs that pertain to the theme of \"Time.\""
c "You may photograph moments that highlight the different times of day,{p=.1} or be creative and think outside the box."
c "I look forward to seeing everyone's work."


"I glared at the paper in my hands and sighed."
m "I'm not a photographer or an artist!{p=.1}How am I supposed to deal with this?"
m "Ugh, I shouldn't have picked a class I didn't know shit about..."

play sound "ghost.mp3"
show echo blurry with Dissolve(2)

e "You should put some more faith in yourself, [charname]."
e "I'm sure you'll dish out at least one half-decent photo."

m "Eh, thanks."
m "Hey wait!{p=.1}You're a camera ghost, aren't you?{p=.1}Can't you teach me any photography tricks for the assignment?"
e "First of all, I'm not a ghost."
e "Second, shouldn't you try and learn about things on your own before I tell you?"
m "But it's haaaaaarrrrrddddd.{p=.1}You useless camera ghost."
e "Like I said, I'm not a ghost!{p=.1}Why don't you ask Phillip or your other friends instead? They're bound to have ideas."

m "Don't you know that's the same as giving up?"
m "Welp, I guess I'll limp through this assignment on my own..."

hide echo blurry
with dissolve

c "Mr. [charname]? I couldn't help but notice your moping from across the room."
c "Is this assignment truly difficult for you?"
m "'Course it is!{p=.1}I've got no background as an artist, and I sure as hell don't think like one."
c "{i}Language{/i}, Mr. [charname]."
c "Perhaps you should think of it another way."
c "Time is a cycle that you live through, day in and day out.{p=.1}Think about the small moments that make them worth living."
c "Photographs, after all,{p=.1}are just little pieces of time."

m "Wow Mrs. Corlisse, I didn't know you were a poet too."
c "I don't appreciate that sass, Mr. [charname]."

scene hallway
with Dissolve(3.0)

"After mulling over the assignment for the entire class,{p=.1}I decided I'll just wing it."
"The plan: take photos wherever I go and pick three that looks half decent."
"What could possibly go wrong?{p=.1}Mrs. Corlisse can't say I didn't at least try."

play sound "bump.mp3"

m "Oof!{p=.1}Sorry about that."
m "Huh?{p=.1}.....{p=.1}Nobody's there...."

stop music
m "Huh?"
"A cold chill flows down my spine.{p=.1}{i}Really cold.{/i}"
"Compared to this,{p=.1}my first meeting with Echo felt like a warm summer breeze."
"What is going on?"

play music "ghost2.mp3" 
show halley neutral
with Dissolve(5.0)

u "..........{p=1}...So you're back,{w=.3} [charname]."
show halley smile with dissolve
u "I wonder what kind of mess you'll get into this time around."
m "W-who are you?"
show halley neutral with dissolve
u "You don't remember?{p=.3}Tch, can't even bother to keep your memories in one piece, can you?"
u "Or is it because you're too ashamed to face your failures?"

m "What are you even talking about?"
u ".........{p=.3}...don't worry about it."
u "Say, [charname]?"
u "That's quite an old camera you have.{p}Don't you think it's time to get rid of that rickety old thing?"
m ".......{p}...I'm quite fond of it, actually."
u "Hmph..."
u "You'll regret holding on to it for so long.{p=.3}It will only bring you more pain."
u "There's only so far you can go{p=.3}with a broken camera and a broken wish."

stop music fadeout 5
hide halley neutral
with Dissolve(3.0)

"....{p}......She's gone."
"My head's throbbing painfully{p=.1}like I had just been spinning around nonstop."
"Urph, I think I'm going to be sick..."

play music "wave-piano.wav" fadein 3 fadeout 2
play sound "ghost.mp3"
show echo neutral
with Dissolve(3.0)

e "[charname]!{p=.1}Are you alright?!"
e "What happened?{p=.1}I lost contact with you for a moment."
m "...ugh...I'm fine."
e "Are you sure? You look so pale.{p=.3}M-maybe it's best you go to the nurse's office..."
m "No, no, I'm just really tired all of a sudden."
m "Haha, I guess my second day of classes took a lot out of me.{p=.3}I'll just head back to the dorm and get some rest."
e "...Alright, but let me know if you need anything.{p=.3}Anything at all."
e "I'm here to keep you safe."
m "I will, thanks for worrying Echo."
e ".................."

hide echo neutral
with Dissolve(3.0)

m "....."
scene dorm night
with Dissolve(5.0)

"I feel exhausted,{p=.1}like I was slowly recovering from a high fever."
"What is going on?{p=.5}That girl that appeared earlier..."
"For some reason, I really want to keep her away from Echo.{p=.1}She felt like someone to never cross."
"I feel kind of bad for keeping Echo in the dark about this too.{p=.1}He looked so worried about me, even though the two of us only just met..."
"With a deep sigh, I turn over in my bed{p=.1}and cover my head."
"Enough with all this thinking...{p=.1}What I really need now{w=1} is sleep."
pass

scene black
with Dissolve(5.0)
scene dorm night
with dissolve

"Uuughh....."
"I've probably tossed and turned in my bed for hours now, but still can't get any decent sleep."
"It feels like my fever's gotten worse too.{p=.1}My whole body's aching like it's on fire."
"I groan and try to sit up.{p=.1}My exhausted body promptly pitches forward and almost fall off the bed."
"A pair of strong hands hold me up just before I faceplant into the dorm floor."

play sound "ghost.mp3" fadein 3
show echo neutral
with Dissolve(3.0)



e "[charname]! Are you alright?{p=.1}You don't look so good."

"I let out a feverish giggle and poke at Echo's sides."
"Huh?{p=.1}My finger slides right through him.{p=.1}It looks like he can physically touch things, but just barely..."
"As Echo helped me back on the bed,{w=.3} his face plastered with a concerned frown."
e "[charname], you're really hot."
m "Heheh, gee thanks~{p=.1}I'm always one smokin' hell of a man~"
"I feel his hand press against my heated forehead.{p=.1}Echo lets out an agitated hiss."

e "You've been cursed!{p=.1}When did this-"
e "!!!!"
e "This afternoon in the hallway! When I lost contact with you for a moment!"

"Echo's voice was a frightening mix of bitter anger and fear.{p=.1}I've never seen him so agitated before."
e "[charname]!{p=.1}Did you meet {i}{b}her?{/b}{/i}"
"\"Her\"? Did he mean...?"
m "W-well, I did bump into this weird girl this afternoon.{p=.1}She had these creepy red eyes and ashy skin."
"Echo groans loudly and pulls at his hair in frustration."
e "She's dangerous, [charname].{p=.1}You {i}have{/i} to stay away from her."
m "Who is she exactly?"
e "...She's very much like me, but leagues stronger than anything I can muster."
e "She can cast curses, cause disaster, bring bad luck....{p=.1}You're lucky the curse you're infected with is pretty weak."
"His fingers brush against my burning forehead again."
e "In fact, it's pretty half-hearted too.{p=.1}Feels like a warning more than anything else."
e "You should recover with a good night's sleep."
m "Why would she curse me of all people?{p=.1}I've never done anything wrong."
e "You could see her, right?"
e "Usually only their wishers could see them.{p=.1}She must have seen you as a threat."
e "..................{p=.1}I wonder if you can see anyone else's wishes too...."
m "What was that?"
e "Hm?{p=.1}Oh nothing, don't worry about it.{p=.1}Just focus on getting some rest."
e "And if you ever see her again, call for me.{p=.1}I'll make sure she can't hurt you."

m ".............................."
"A long, sickly silence stretched between us."
"I reached a weak hand up to poke Echo on the nose, but my fingers slide right through him. Like a ghost."

m "Echo...I've been dragged through the most bizarre things the last few days."
m "Cameras...ghosts....curses....and now I feel like I'm frying on the sun."
m "After all that's happened, don't you think you owe me an explanation?{p=.1}Who are you, and why do you care so much about me? We've only just met."

"Echo stays silent and instead runs his fingers softly through my hair."
"He's got that bittersweet smile back on his face again..."

e "You dork.{p=.1}Like I said before, I'm not a ghost."
e "I'm a wish, and I'm here to keep you safe."
"There was another pause as Echo pulls me into a warm hug."
e "And you might not realize it, but I've known you for practically your whole life, [charname]."
e "You're dear to me, so that's why I'll always be there for you."

m "................"
m "...The hug feels pretty nice....{p=.1}....But nothing you just said made any sense..."
e "I promise you that it will, someday."
"I yelped as Echo suddenly poked my nose."
e "Anyway, it doesn't look like you'll be sleeping anytime soon.{p=.1}How about we get you something to eat, or maybe some fresh air?"
m "I-I don't think I'm well enough to walk anywhere, to tell you the truth."
e "No worries little man, I'll carry you."
e "So, where do you want to go?"

menu: 
    "The kitchen":
        m "Well, I guess I'm feeling a bit hungry right now."
        e "The kitchen it is then."
        e "Here, hold on to my shoulder. I'll carry you there."
        "As I reach up, Echo placed his arm firmly around my waist as I climbed onto my wobbly legs."
        "My head feels a bit dizzy being upright, but it's nice to be out of bed."
        e "Alright, let's go, one step at a time..."
        m "Geez, I feel like an elderly granny being helped across the street."
        e "Pfft, you're not sweet and tiny enough to be a granny."
        m "Are you just gonna let me lie in the middle of road and get hit by a truck?"
        m "Get a move on ya whippersnapper~"
        e "Got it grandpa."
        
        scene black
        with Dissolve(3.0)
        
        "We entered the kitchen and Echo carefully led me to a seat at the kitchen table."
        "It's pretty damn dark in here. I can barely see a thing."
        "...?"
        m "H-hey, I think I hear someone coming.{p=.1}Maybe you should hide yourself or something?"
        e "Don't worry about it [charname].{p=.1}You're the only one who can see me anyway."
        
        play sound "bump.mp3"
        scene kitchen night
        with dissolve
        
        "Suddenly the lights flicked on as someone strolls into the room."
        m "Oh hello Sissel."
        
        play music "cafe-music.mp3" fadein 3 fadeout 3
        
        s "{size=+10}-WAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH?????!?!?!???!?!?!?!?!{/size}"
        "Sissel jumps a foot in the air and stumbles comically onto his back."
        "Heheh, he's flailing like a turtle."
        
        show sissel surprised 
        with dissolve
        s "W-w-wha?"
        hide sissel surprised
        show sissel embarrassed
        with dissolve
        
        s "For fuck's sake [charname], give me some warning!"
        m "All I did was say hello."
        s "W-w-well I didn't expect you to be here at the dead of night!"
        m "Pffft, you're like an angry slice of pie."
        s "W-what? Stop laughing you jackass!"
        "I couldn't help but snicker at his outburst."
        hide sissel embarrassed
        with dissolve
        "My laughing abruptly turned into a hacking cough as the room suddenly started spinning."
        "A pair of arms caught me just before my face hit the floor."
        show sissel neutral
        with dissolve
        s "...that was a close one.{p=.1}[charname], you feeling alright? You don't look so good."
        
        "I only reply with a feverish giggle."
        m "The floor and I are madly in love, Sissel.{p=.1}Why must you get in the way of our sweet embrace?"
        s "Ok, I'll take that as a no."
        m "You can't break us up like this! I'm in love!"
        s "'Fraid I love you more.{p=.1}Let's elope back to your seat."
        "Sissel pulls me back onto my chair and feels my forehead with concern."
        s "Whoa, you're burning up."
        s "...you know what, stay right there.{p=.1}I'll cook up something for you. That'll push the fever away."
        m "Eeeh Sissel, you're not my mom. Stop fussing over meeeeee~"
        m "You'll lose all your punk cred."
        s "I'll lose {i}all{/i} cred if I leave a sick friend to die on MY kitchen floor."
        m "Bleeeh, now you're just being a drama queen."
        s "Yes I am. Now settle down at the table.{p=.1}I'll make you some soup."
        m "Thank you, your highness~"
        
        hide sissel neutral 
        with dissolve
        "Sissel grabbed his apron and got straight to work."
        "Within a few minutes, the stove was purring away as the room warmed with the smell of delicious broth."
        "My head's starting to feel a bit less loopy, but I still had an awfully large grin on my face as I watched Sissel work."
        
        m "...heheh~"
        show sissel neutral
        with dissolve
        s "...What are you laughing about, idiot?"
        m "Nothing~{p=.1}It's just that you'd make the perfect wife."
        hide sissel neutral
        show sissel embarrassed
        s "W-wh-"
        s "Ugh, that fever's really scrambling your brain."
        m "Well it's true~!"
        m "You can cook awesomely and you have a great caring side~{p=.1}Sure you're a tough punk-ish sort of guy, but I still think you'd be a great wife~"
        
        play music "little-dark.mp3" fadein 9 fadeout 2
        
        hide sissel embarrassed
        show sissel neutral
        with Dissolve(3.0)
        

        
        s "...........{p=.5}........................."
        s "...Thanks [charname], that's pretty flattering."
        s "But I don't think I'll ever be getting married or find love anytime soon..."
        m "Why not?"
        m "Geez,{w=.3} you're not perfect but I'm sure a sweet girl or guy will be completely smitten by-"
        s "No, you're wrong."
        "I rub at my tired eyes and try to look at Sissel's face.{p=.1}He seemed so uncomfortable..."
        "Was there something he's hiding?"
        "........"
        "With a sigh, I wobble onto my feet and limp over to him."
        
        
        hide sissel neutral
        show sissel surprised
        with dissolve
        
        s "[charname]! You shouldn't be up-"
        m "Sshhhhhhhhhhh..."
        "I pull him into a hug and start petting his hair, ignoring his embarrassed splutters."
        hide sissel surprised
        show sissel embarrassed
        with dissolve
        
        m "Hey Sissel?"
        s "What?"
        m "You're loooooved, you adorable slice of pie. Loved~{p=.1}Now accept it or you're going to piss off your very sick friend."
        hide sissel embarrassed
        show sissel neutral
        with dissolve
        s "........[charname], you don't know me very well."
        s "...I........I'm broke.{w=.3} I've got nothing to show for myself.{w=.3} I'm barely educated enough to even be at the academy."
        s "There's always gonna be someone more worthwhile than me..."
        m "You can say that about anybody,{w=.3} to be honest."
        m "It's too late Sissel, you're already loved.{p=.1}Didn't you say earlier that you'd elope with me?"
        hide sissel neutral 
        show sissel embarrassed
        with dissolve
        s "T-that was just a joke."
        m "And I'm here to tell you that you're no joke Sissel. You deserve all the love in the world, and don't you dare deny it."
        s "...................."
        
        
        
        s "You're such a shameless twat, [charname]."
        m "I know."
        "I gave Sissel a goofy grin. He only responded with an exasperated groan."
        "I couldn't help but laugh nonsensically at him."
        "My feet suddenly gave out and I clung onto Sissel's shoulders for dear life."
        m ".....Uh, could you carry me back to the table? My feet are growing a bit sore."
        
        
        
        "Sissel let out a mix of a laugh and a sigh before gently carrying me to the table."
        hide sissel embarrassed
        with Dissolve(3.0)

        "We spent the rest of the night quietly together, drinking delicious soup and sharing meaningless small talk."
        "It reminded me of our lunch together at the cafe. The chatter filled up the silence from before nicely."
        "We didn't mention what happened earlier again and it almost felt like our whole conversation from before didn't happen."
        "But Sissel seemed more relaxed and content that night. I think it was the first time I've seen him truly smile."
    "The roof":
        m "Some fresh air sounds pretty good right about now.{p=.1}How about the roof?"
        e "The roof it is then~"
        e "Here, hold on to my shoulder. I'll carry you there."
        "As I reach up, Echo placed his arm firmly around my waist as I climbed onto my wobbly legs."
        "My head feels a bit dizzy being upright, but it's nice to be out of bed."
        e "Alright, let's go, one step at a time..."
        m "Geez, I feel like an elderly granny being helped across the street."
        e "Pfft, you're not sweet and tiny enough to be a granny."
        m "Are you just gonna let me lie in the middle of road and get hit by a truck?"
        m "Get a move on ya whippersnapper~"
        e "Got it grandpa."
        
        scene dorm roof night
        with Dissolve(3.0)
        
        
        show echo neutral
        with dissolve
        "The cool night breeze felt heavenly compared to the heat from earlier."
        "Stars twinkled above in the dark sky like a thousand diamonds. The tranquil view definitely put my mind at ease."
        "As the two of us limped onto the roof, I let out a sigh of relief."
        m "This is nice..."
        "Echo was staring up at the sky rather wistfully. He looked a bit sad, actually."
        m "Hey Echo, are you-"
        e "Mm, there's someone already here."
        m "Is it alright for you to be here?"
        e "Don't worry about it [charname].{p=.1}Remember, nobody can see me but you."
        "He gently helped me into one of the chairs, and I'm finally close enough to see who the other person was."
        
        hide echo neutral
        show phillip neutral
        with dissolve
        
        m "Oh hey there Phillip."
        p "Mm? Good evening-"
        hide phillip neutral
        show phillip frown
        with dissolve
        p "Whoa! [charname] are you alright? You look like you just woke from the dead!"
        m "Gee thanks Phillip. You really know how to up a guy's self-esteem."
        p "Nevermind that, wait right here.{p=.1}I'll go get you some tea and aspirin."
        
        scene dorm roof night
        with fade
        
        show phillip neutral
        with dissolve
        
        "A few minutes later, Phillip came running back with a steaming kettle of fresh tea and a bottle of fever medicine."
        m "You know, usually my parents give me nice, cold ice cream to cool down a fever."
        p "Nonsense, sugar is bad for you."
        p "Now drink your tea. You'll feel better."
        m "Who knew you'd be such a mother hen?"
        "Phillip gave me a wry smile as I took a sip."
        "Hm?"
        m "Wow, this stuff's actually pretty good."
        "The fresh, lightly bitter taste was rather refreshing on the tongue."
        "I took another sip as Phillip takes a cool towel to wipe the sweat off my forehead."
        
        p "Well at least you're staying hydrated after sweating so much."
        p "I usually drink tea whenever I'm feeling unwell and it always manages to relax me."
        p "Heheh, maybe I can convert you into a tea fanatic too."
        m "Pffft, I definitely wouldn't mind."
        
        "Phillip lays a cool towel on my forehead, wiping away the sweat and grime that had built up."
        p "Why don't you lie down a bit while I towel you off?{p=.1}The chairs recline."
        m "Mm, sure."
        m "....Ah, that feels a lot better."
        p "I'm just going to wipe off all the sweat you have going on here."
        p "Err, I'm going to have to undo your pajama shirt. Is that alright?"
        m "I don't mind~"
        
        "Phillip kneels down in front of me and slowly unbuttons the front of my shirt.{p=.1}Having him this close to my exposed chest is a bit embarrassing."
        "He takes his wet towel and began wiping away the gross film of sweat that had built up on my front and back."
        "The cool water felt pretty nice against the refreshing night breeze."
        
        "...............We've gotten rather intimately close to each other.{p=.1}Phillip doesn't seem to have noticed, or if he has, he's ignoring it."
        "His fingers worked his way against my back muscles, massaging away the pain."
        
        m "Mmmm, have you done this before? This feels great."
        p "Giving massages to sick people on school roofs in the middle of the night?{p=.1}Nope, can't say I have."
        m "Why are you even up here so late, anyway?"
        p "I'm just finishing up some work for my classes."
        "Sure enough, there were papers and notebooks scattered everywhere on the ground. How have I not noticed?"
        m "Geez, it's only the second day. How many classes are you taking?"
        hide phillip neutral
        show phillip shrug tired
        with dissolve
        
        p "A fair few. It's not as bad as it looks actually."
        m "Your brain's going to turn into mush and fall out of your ears."
        hide phillip shrug tired
        show phillip neutral
        with dissolve
        p "Aw now you're just exaggerating."
        m "If you don't get some sleep, you're going to end up as sick as I am."
        p "Why don't you just worry about yourself for now, oh sick one."
        
        "Another long silence passes by before Phillip mumbles softly under his breath."
        hide phillip neutral
        show phillip frown
        with dissolve
        
        play music "relaxing_piano.mp3" fadein 2 fadeout 2
        
        p "Well, I guess I'm also up here because I'm still avoiding my roommate."
        m "Oh about that.{p=.1}Why do you dislike Owen so much? Does he bother you?"
        "Phillip let out a frustrated huff."
        p "I don't really dislike him, per se.{p=.1}He's just a bit too \"touchy-feely\"."
        p "He grabs and hugs me whenever he gets the chance, even when I tell him I don't want it."
        p "Owen's got no sense of personal space, you know?"
        m "Pffft, speak for yourself.{p=.1}You're the one who's groping my chest and backside."
        hide phillip frown
        show phillip shrug blush
        with dissolve
        p "Hey, I asked for permission before groping.{p=.1}This is all on you."
        hide phillip shrug blush
        show phillip neutral
        with dissolve
        p "Also, I'm all finished. You're now sweat-free and as good as new."
        m "Mm it's nice tha-a-anks~"
        "I break out into a yawn as I sit up and stretch."
        p "Getting sleepy? Looks like the medicine's doing its job."
        p "Let's get you back to bed now."
        
        scene dorm night
        with Dissolve(3.0)
        
        "Phillip walks me back to my dorm, with me limping along weakly the whole way."
        "The fever's gone down a bit, but I still feel like roadkill.{p=.1}Sleep takes me as soon as my head hits the pillow."
        "Before I completely drift off, I felt Phillip give me a gentle hug, and whispered softly."
        p "Sweet dreams, [charname]."
        
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
            
jump day3
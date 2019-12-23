#DAY 5 
label day5:
$ persistent.current_route = "default"

"{b}Day 5{/b}:{w=.5} The Broken Star"

play music "happy_lounge.mp3" fadein 3 fadeout 3
scene dorm with Dissolve(3.0)
"Yaaaaawwn, {w=.3}is it really morning already?"
"I blinked through my drowsiness. I was half expecting Echo wake me up in some rude way again."
"Where is the guy?"

play music "fragments.mp3"
show echo cracked with Dissolve(3.0)
e "Heh,{w=.3} did you have a nice nap [charname]?"
m "E-Echo! {p=.3}You're-"
"There was a painful-looking crack running across his chest, like he was made of glass."
"A wave of guilt washed over my chest."
m "Are you ok? {p=.3}D-did this happen because you pushed yourself too hard yesterday?"
e "Oh this is nothing to worry about. {w=.3}I'll be perfectly fine~"
e "Luckily, there's a meteor shower tonight.{p=.3}It'll help me recover."
m "How does a meteor shower help you recover?"
e "Oh you know,{w=.3} \"ghostly voodoo shit\" as you elegantly put it."
e "More importantly, you've got to be more careful from now on."
e "That Remnant thing is still out there, {w=.3}and we still don't know what it's capable of."
m "I guess I'll keep an eye out for any armless blobs."
m "But are you really sure you're alright?"
e "Ugh, yes. I should be ok by tonight.{p=.3}Anyway shoo! You've got to get to class."

hide echo with Dissolve(3.0)
"With a dismissive wave of a hand, Echo poofed and disappeared."
m "I hope he's really ok....."

scene black with Dissolve(3.0)
play music "snowy-street.mp3" fadein 3
scene dorm hallway with Dissolve(3.0)

"As I pass by Phillip and Owen's room, I could still hear Phillip's painful retching."
"I really need to thank him for taking a bullet for me..."
"At least I know Owen's going to take good care of him."
"With a tired mumble, I shook my head furiously."
"Alright [charname], focus!{p=.3}You've got classes to attend and photos to take!"

scene art room with Dissolve(3.0)

"Back to good old Photography class, huh? {w=.3}I can't help but feel like I'm forgetting something..."
"The usual class clamoring and chatting immediately stopped when Mrs. Corlisse entered the room."
"She wore her usual stern look as she flipped through all her teacher notes."
c "Good morning ladies and gentlemen,{w=.3} I hope everyone remembered to take their three photographs for the Time assignment."
"Huh? What assignment-{p=.3}{size=+10}SHIT SHIT SHIT SHIT SHIT SHIT SHIT{/size}"
"Mrs. Corlisse shot me a knowing look."
c "For those less....{w=.3}attentive students who forgot to print their photos, there is a photo printer in the back of the room."
c "You will have 10 minutes to prepare before presentations begin. {w=.3}Please organize yourselves accordingly."

"Aaaaaaaaaaahhh I totally forgot about this."
"Sweat collected on my forehead as I rummaged through my camera madly."
"Usually I wouldn't give a damn about my grades, but knowing the disappointed look Corlisse will give me..."
"Ugh, there's got to be {i}something{/i} in here I can bullshit into a presentation!"
"I-I'll just print out every photo I have and pick something half-decent!"

scene black with Dissolve(2.0)
scene art room with Dissolve(1.5)

"Gulp, looks like my presentation is next. {p=.3}H-hope this goes well."
c "And next is Mr. [charname]. What three photographs have you taken?"
"I stumbled to the front of the class hesitantly."
m "W-well, this is my first photo-"

if photo_1 == "none":
    $ photo_1 = "phillip"
    pass


if photo_1 == "phillip":
    show sunset phillip with dissolve
    pause(2.0)
    m "T-this is a photo I took on my first day here at the academy..."
    m "A-a-and it has to do with the \"Time\" theme because...{w=.3}um...{w=.3}you know."
    m "Sunsets."
    "Mrs. Corlisse nodded approvingly, sending a wave of relief down my spine."
    c "Well, despite Mr. [charname]'s lackluster description, this is a wonderfully composed photograph."
    c "I'm surprised you managed to take a photo during the golden hour with such skill."
    c "Well done."
    m "T-thank you!"
    hide sunset with Dissolve(2.0)
    
if photo_1 == "owen":
    show sunset owen with dissolve
    pause(2.0)
    m "U-uh, this is a photo I took on my first day at the academy..."
    "A surge of heat rushed through my cheeks as Mrs. Corlisse scanned me with a raised eyebrow."
    m "A-a-and it as to do with the \"Time\" theme because.....{w=.3}y-you know."
    m "Sunsets."
    "There was an amused smirk on Mrs. Corlisse's face as she scribbled something on a clipboard."
    c "This is a fine photo of the sunset, [charname]."
    c "However, I have a sneaking suspicion that the sunset was not what you were focusing on."
    m "R-really? I have no idea what you m-m-mean!"
    c "I'm sure you don't."
    hide sunset with Dissolve(2.0)


c "Anyway, show us your next photo, [charname]."
m "O-oh, um.....{p=.3}The next one's a little......"
c "I assure you Mr. [charname], no matter the quality of your work, there will be no harsh judgement in this class."
m "I-if you say so. {p=.3}H-here it is:"
stop music fadeout 2

show canoe with dissolve
pause(2.0)
c "........................"
m ".....................................u-um...I can explain...."
play music "hyperfun.mp3" fadein 2
c "I wholeheartedly take back my previous statement."
"A wave of snickers rang through the class.{p=.3}Even Mrs. Corlisse wore a humorously exasperated look on her face."
c "Anywho, would you be so kind as to describe your photograph?"
m "W-w-w-well I took this during the canoe race the other day and uh......"
m "It's definitely related to the theme!{p=.3}Because it's taken midday! And it's summer-ish and active and stuff...?"
c "Of course it is."
"Mrs. Corlisse turned to address the class."
c "I believe Mr. [charname]'s photo is a fine example of what you youngsters call...{w=.3}a \"crotch shot.\""
"Heat instantly flared through my cheeks."
m "I-I-I JUST THOUGHT THE COMPOSITION WAS NICE!!"
m "T-this photo was taken in the name of science!{p=.3}No ulterior motive whatsoever!!"
hide canoe with Dissolve(2.0)


"Mrs. Corlisse chuckled as she scribbled a few notes on her clipboard."
c "Ah yes, science. {w=.3}Of course."
c "Anyway, on to your last photo please. {p=.3}I certainly hope it's more family friendly."
m "Alright my last photo is:"
show selfie with dissolve
pause(2.0)
c "And what is this?"
m "It's a selfie!{w=.3} I took this like 5 minutes ago!"
m "It represents procrastination and how time is constantly running out!"
c "I see.....{p=.3}Well I suppose this does follow the assignment's theme."
m "Yes!"
hide selfie with Dissolve(2.0)
c "However,{w=.3} Mr. [charname], it would be wonderful if you could put more effort into your work from now on."
c "Last minute improvising will not always be effective.{w=.3} Only careful preparation will guarantee success."
m "Y-yes ma'am, I'll try harder next time."

stop music fadeout 2

"A sigh of relief poured out every one of my veins as I returned to my seat, away from the judging eyes of the classroom."
"I collapsed onto my desk with a sigh."
"That was a close one. {p=.3}I'm glad Mrs. Corlisse is more lenient than she lets on."
"I really should start taking more photos though-{p=.3}Huh?"
stop music
"I dig through my pile of photographs curiously."
"What's this?"
play music "moon-fragment.mp3" fadein 3
show group photo 1 with Dissolve(2.0)
pause(2.0)

"My heart abruptly wrenched painfully against my chest for some reason."
"It's a photo of Owen, {w=.2}Phillip, {w=.2}Sissel, {w=.2}me..........{w=.5}and someone I've never seen before."
"I don't remember taking this photo.{p=.3}That girl looks so familiar though...{w=.3} I swear I know her from somewhere..."

play sound "ghost.mp3"
show group photo 2 with Dissolve(3.0)
pause(2.0)

"H-huh?"
"A thick fog of drowsiness trudged through my mind."
"I shook my head furiously and blinked."
"W-what was I doing again?{p=.3}Hm?"
"Why was I holding this photograph? {w=.3}Weird, there's this blotch that looks like it could've been a person..."
"Was it always so blotchy?"
"No wait, I-{p=.3}Ugh, headache."
"I swear there's something......{w=.3}I'm forgetting something important.......{p=.3}What was it.....?"

stop music fadeout 4
scene black with Dissolve(4.0)

play music "snowy-street.mp3" fadein 2
scene courtyard with Dissolve(2.0)

"A nice,{w=.3} quiet, Friday afternoon with no classes.{p=.3}Gosh this feels relaxing..."
"I wonder what I should do with all this free time."
play sound "beep.mp3"
"My phone suddenly buzzes with a text."
"Oh it's Phillip."

p "'{i}YOU'VE GOT TO HELP ME THIS IS AN EMERGENCY{/i}'"
m "'{i}What is it?!'"
p "'{i}Owen is a fantastic singer.'"
"I blinked blankly at my phone screen."
m "'{i}That's....good?'"
p "'{i}He won't stop singing country music.'"
p "'{i}Nothing but country music{w=.3} for the last 6 hours.'"
p "'{i}[charname] you've got to help me please have mercy I'm begging you'"

menu:
    "Leave Phillip to his doom and enjoy your Friday afternoon.":
        m "'{i}Well Phillip, {w=.3}karma is a cruel cruel mistress and only the sweet embrace of death remains.'"
        p "'{i}{size=+10}I SAVED YOUR ASS FROM BULLET HELL YESTERDAY YOU CAN'T JUST DITCH ME LIKE THIS'{/size}"
        m "'{i}Life ain't fair Phillip, {w=.3}but may our paths cross once again!'"
        
        "With that, I clicked my phone shut."
        "Sorry Phillip, but Friday afternoons are a sacred time."
        "That being said, what should I even do?{w=.3} Ugh, I really need to spend my time wisely now that I've sacrificed one of my friends."
        
        "Welp, I guess I could go visit Sissel. {w=.3}I think he's working at his cafe right now."
        "Now if only I can remember where it is...."
        
        scene black with Dissolve(2.0)
        play music "cafe-music.mp3" fadein 3
        scene cafe front with Dissolve(2.0)
        
        "I arrived at Sissel's cafe without much trouble."
        "It's pretty quiet at this hour.{p=.3}I'm practically the only customer here."
        "Now,{w=.3} where is Sissel...?"
        "???" "Well hello there!"
        "A booming voice pulls me out of my thoughts."
        show hershel with Dissolve(2.0)
        "A large man suddenly pops up behind the counter wearing a friendly, jovial grin."
        h "G'day there kiddo!{p=.3}The name's Hershel, {w=.3}I'm the boss around here."
        h "How can I help you?"
        "W-wow, he's pretty tall for a rabbit."
        "Granted, even Sissel is taller than me but this guy's slightly more intimidating..."
        "I do my best to smile politely."
        m "H-hello! {w=.3}I was wondering if Sissel's around."
        h "You're looking for lil' Sissel huh? {w=.3}He's out back in the kitchen."
        "The large man eyeballed me for a few moments before his grin became wider."
        h "Ohoo,{w=.3} you must be one of the classmates he couldn't stop yakkin' about."
        
        if steal_wallet == "true":
            stop music
            show hershel frown with dissolve
            h "So which one are you? {w=.3}The flower cat or the wallet thief?"
            m "W-what?"
            "I jumped. {p=.3}Hershel's jolly grin disappeared as he silently leaned closer until he loomed over me."
            "When he finally spoke, {w=.3} his voice was a low growl."
            h "Listen here ya little drongo.{p=.3}I've heard mixed messages so I'll give you the benefit of the doubt."
            h "But if ya mess with my boy Sissel, {w=.3}yer gonna have to deal with me."
            h "Got it?"
            m "Y-y-yessir!"
            show hershel with dissolve
            play music "cafe-music.mp3" fadein 2
            "Hershel suddenly grins, his intimidating air disappearing as quickly as it came."
            h "That's what I like to hear! {p=.3}You and me are gonna get along juuuuuuust fine~"
            "There was rustling from a door behind the counter as a voice called out."
            s "Boss! What's with all the racket?"
            h "Oh Sissy! {w=.3}Perfect timing, you've got a visitor!"
            s "{i}{b}I TOLD YOU TO NEVER CALL ME THAT!{/b}{/i}"
            show hershel at left with dissolve
            show sissel neutral at right with dissolve
            "The backroom door creaked open as Sissel peered out suspiciously."
            s "Oh hey [charname]! {p=.3}Nice to see you're still alive after the mess yesterday."
            hide hershel with dissolve
            show sissel neutral uniform at center with dissolve
            "Hershel peered between us carefully before returning to his jovial grin and trotted out of sight."
            h "Heh, I've still got work to do. {w=.3}Ya anklebiters play nice while I'm gone!"
            s "Boss! {w=.3}I'm not a kid anymore!"
            "Sissel sighed and shook his head tiredly as he turned towards me."
            
        if steal_wallet == "false":
            h "So which one are you? {w=.3}The flower cat or the cute photographer?"
            "A flush heat shot through my cheeks."
            m "W-what?!"
            "Hershel looks me up and down with a raised eyebrow."
            h "Hm, for how much Sissel rambles about you, {w=.3}yer pretty average."
            m "Sissel talks about me?"
            h "Oh please, the kid's won't shut about how cute y-"
            s "{size=+10}{i}BOSS {w=.3}YOU BETTER SHUT YOUR MOUTH!{/i}{/size}"
            show hershel at left with dissolve
            show sissel embarrassed uniform at right with dissolve
            "Sissel stormed out of the backroom, his face glowing like a tomato."
            h "Chill kiddo, I was just messin' with ya~"
            hide hershel with dissolve
            show sissel at center with dissolve
            "Hershel gave me a sly wink before retreating to the backroom of the cafe, leaving me alone with a red-faced Sissel."

        
        show sissel neutral uniform with dissolve
        s "Well, I guess you've met my boss...?{p=.3}Don't mind him, he's just a big ol' twat."
        m "Hershel seems pretty nice."
        m "He kind of reminds me of you, actually.{p=.3}Are you two related?"
        s "Really? {w=.3}Just because we're both rabbits?"
        s "Geez [charname], I didn't know you were one of {i}those{/i} people-"
        m "N-no no I didn't mean-"
        s "Chill dude,{w=.3} I was just joking.{p=.3}People confuse me for Hersh's kid all the time."
        s "But he's just my boss, {w=.3}no blood relation or anything like that."
        s "He'd make a terrible parent anyway."
        s "Oh whoops, I started rambling again, didn't I?"
        s "You better take a seat and make yourself comfortable before boss fires me for bad customer service."
        
        
        m "Oh? And what kind of \"services\" are you offering?"
        "I winked at Sissel teasingly and he groaned in exasperation."
        s "Just sit down you twat."
        m "Oh,{w=.3} I'm not particularly hungry at the moment.{p=.3}I just came here to see how you were doing."
        "Sissel sighed and scratched his head."
        s "I appreciate the sentiment,{w=.3} but I don't have time to entertain you right now.{p=.3}I've got a job to do."
        m "Well,{w=.3} I guess I could help out in the kitchen if you want."
        s "[charname], you don't have to waste your Friday afternoon here.{w=.3} Don't you have anything better to do?"
        m "Hey I {i}want{/i} to spend my afternoon here.{p=.3}I enjoy your company Sissel."
        show sissel embarrassed uniform with dissolve
        s "W-wah-?"
        "Sissel's face flushed red as he digested what I just said."
        s "Don't say shit like that with a straight face-!"
        
        "Hershel suddenly popped out from the kitchen door."
        show sissel at left with dissolve
        show hershel at right with dissolve
        h "Hey kiddo, {w=.3}yer free to pitch in if you want. {w=.3}I'll take all the help I can get~"
        h "As long as you don't burn anything or make a mess,{w=.3} you're good."
        hide hershel with dissolve
        
        show sissel neutral uniform
        s "Well.....{w=.3}I guess an extra pair of hands wouldn't hurt."
        s "Why don't you come with me to the kitchen?"
        
        scene cafe kitchen with Dissolve(3.0)
        
        m "Wow, {w=.3}this place is surprisingly fancy."
        show sissel neutral uniform with dissolve
        s "Of course it is.{p=.3}Don't let the cafe's small size fool you,{w=.3} this place is well known for having the best pastries in the city!"
        m "That makes me wonder,{w=.3} how did you end up working here?"
        s "It's a bit weird to be honest.{p=.3}Boss just found me on the side of the road and offered me a job out of the blue."
        s "I accepted immediately, of course.{p=.3}I've always wanted to be a successful baker ever since I was little~"
        show sissel embarrassed uniform with dissolve
        s "I know that sounds dumb coming from someone who ate out of trash cans for years, but-"
        show sissel neutral uniform at left with dissolve
        show hershel at right with dissolve
        h "Kiddo, what did I say about talkin' shit about yourself?"
        "Sissel sighs and scratches his head awkwardly."
        s "Right right,{w=.3} I'll stop."
        h "Good to hear~"
        
        hide hershel with dissolve
        show sissel neutral uniform at center with dissolve
        
        m "Hershel sure likes to pop in and out."
        s "Well, {w=.3}I guess we should put you to work."
        s "I'd feel like a dick if I just made you wash dishes the entire time..."
        s "Hmm.....{w=.3}would you like to help us taste-test our experimental chocolates?"
        m "D-d-d-did you just say chocolate?"
        s "I mean they're experimental,{w=.3} so some of them might taste weird-"
        m "I don't care.{p=.3}{i}{b}I'm a total slut for chocolate{/b}{/i}."
        m "{i}I'd wash a thousand dishes for you if it means getting chocolate!!{/i}"
        s "Whoa I didn't know you were a chocolate addict."
        m "Addict and proud! {p=.3}And I need my next fix of chocolate soon before I get withdrawal symptoms."
        m "{i}Feeeeeeeed meeeeeeeeeeeeeeee{/i}"
        s "I've created a monster."
        
        scene black with Dissolve(2.0)
        play music "easy-lemon.mp3" fadein 2
        scene cafe kitchen with Dissolve(2.0)
        
        "And so,{w=.3} I spent the next hour or so helping clean up dishes while Sissel mixed several bowls of molten chocolate behind me."
        "Every so often, {w=.3}he'd pop one in my mouth while I'm scrubbing the plates."
        
        m "Mmmm, {w=.3}my god this stuff tastes like heaven~"
        show sissel neutral uniform with dissolve
        s "That one had a bit of hazelnut and caramel mixed in.{w=.3} I hope it wasn't too sweet-"
        m "It's perfect, {w=.3}all of your recipes are perfect aaaaaaah~"
        s "[charname] I need actual feedback on my recipes,{w=.3} not just the sound of you moaning sensually."
        m "It's true though! All of these chocolates just melt perfectly in the mouth and mix together like ice cream."
        m "It's almost as good as sex <3"
        s "Ugh, you're just as bad as Owen."
        
        m "Hey I'm scrubbing hundreds of plates for these chocolates!{p=.3} I deserve to enjoy them to the fullest!"
        s "If you say so."
        s "Anyway, what about this one?"
        "Sissel plucked another blissful looking chocolate off of a tray and pressed it to my mouth as I pulled the drain on the sink."
        "I engulfed immediately and rejoiced at the sensation of liquid sweetness pour over my taste buds."
        "My tongue swished it around my mouth a few times as I tried to uncover all the flavors."
        "There seems to be a hint of orange,{w=.3} and some lemon as well. {p=.3}A citrus combo, huh?"
        "The chocolate was delicious, but the texture seems a little weird....."
        
        stop music
        show sissel embarrassed uniform with dissolve
        s "Uh...........{p=.3}.................[charname]?"
        s "Could you.........{w=.3}stop sucking on my fingers?"
        play music "hyperfun.mp3" 
        m "Huh?!"
        "I immediately opened my mouth and allowed Sissel to retract his hand."
        "Apparently I did an excellent job at suckling his fingers,{w=.3} they were completely wet with saliva and chocolate."
        
        m "S-sorry about that! {w=.3}I got a little carried away-"
        s "I-i-i-it's fine!"
        "Sissel's face was beet red as he hastily wiped his hand on his apron."
        "Speaking of which, {w=.3}part of the apron at his waist was sporting a rather noticeable tent."
        "Heh, did I really turn him on?"
        
        m "Pfft, {w=.3}looks like I wasn't the only one who enjoyed himself~"
        s "S-Shut up! {w=.3}You're such a shameless little-"
        s "Ugh, {w=.3}my shift is almost over.{p=.3}We better pack up and go home."
        m "Aaaaw admit it, {w=.3}you liked my sucking skills~"
        s "{size=+10}{b}THAT'S IT{w=.3}, NO MORE CHOCOLATE FOR YOU!{/b}{/size}"
        hide sissel with dissolve
        m "W-wait Sissel!{p=.3}Come baaaack!"
    "Rescue Phillip from country music hell.":
        m "'{i}On my way Phillip, just hold on a little longer!'"
        p "'{i}It's too late [charname], my sanity is already dead."
        "'{i}*RedHotPanda has joined the conversation'"
        o "'{i}Hey, my singing isn't {b}that{/b} bad!'"
        p "'{i}No that's just the thing, he's got a gorgeous voice.'"
        o "'{i}Aaaw Phillip that's so sweet of you!'"
        p "'{i}Too bad he's wasting it singing about trucks, booze, and hot women.'"
        p "'{i}Well, hot men in this case. Definitely not helping my headache.'"
        o "'{i}Alright then, what genre would you like to hear in my gorgeous voice? Any requests? ;)'"
        p "'{i}How about something classical?{p=.3}Like John Cage's 4'33\"'"
        o "'{i}Excellent! (wait let me look that one up rly quick)'"
        
        
        "I stared at their bickering and grinned. {p=.3}Looks like those two are back to their usual selves."
        "I better get to their dorm before Phillip strangles Owen though."
        
        
        if day4_item == "owen":
            "Mailman" "Hey! Excuse me!"
            m "Huh?"
            "I looked up to see a man in a post office uniform jog up to me."
            "Mailman" "Are you a student here?{p=.3}Sorry, but do you know where an Owen Lorelei lives?"
            "Mailman" "It's my first day on the job and this campus is huge!"
            m "Oh Owen lives-"
            play music "drift.mp3" fadein 1 fadeout 2
            "Mailman" "Wouldn't have expect anything less rich and over-the-top though. {p=.3}One of the Lorelei's goes here after all."
            "My words were caught in my throat."
            "The man almost spat as he spoke the name.{p=.3}What was his problem?"
            "He was clutching a brick-sized cardboard box bounded together with rubber bands. {p=.3}Was that for Owen?"
            m "................."
            m "Owen lives in the same dorm as me. {w=.3}It's the one towards the north end of campus, over there."
            "Mailman" "Huh? You {i}live{/i} with the little scamp? Dude, that sucks."
            "Mailman" "Hate to push this onto you, but could you give him this package instead?{p=.3}I don't want to be anywhere near a filthy Lorelei."
            "Before I could even respond, the mailman roughly tosses me the box before driving away in his mail-van."
            "I could only stare after him, dumbfounded as he drove out of sight..."
        
        scene black with Dissolve(4.0)
        play music "easy-lemon.mp3" fadein 6
        scene dorm hallway with Dissolve(2.0)
        
        "I reach the dorms just in time to hear-"
        o "JOHN CAGE'S 4'33\" IS JUST FOUR MINUTES OF SILENCE-"
        p "Are you not capable of that?"
        o "But I wanna sinnngggggggg-"
        
        scene PO dorm with Dissolve(2.0)
        show owen neutral at left 
        show phillip neutral at right 
        
        m "Yo Phillip, you still alive?"
        p "No,{w=.3} my everything hurts and I have half a dozen country songs stuck in my head."
        m "That's horrible! {p=.3}Owen, how could you?"
        o "Hey, I've been taking care of our little Phillip for the entire morning!{p=.3}I deserve a little fun~"
        "Phillip groans and buries his face into his pillow."
        m "Speaking of which, how are you feeling Phillip?"
        "I was answered with a pillow-muffled groan."
        show owen grin 3 with dissolve
        o "He's been doing a lot better than yesterday.{p=.3}Less vomit and whatnot."
        o "His appetite's recovered and he's been sassing me every other minute. {w=.3}That's definitely a sign of recovery, right?"
        
        p "And Owen's made nothing but burnt spaghetti."
        show owen neutral with dissolve
        o "Hey! At least it's edible!"
        "Despite Phillip's disgruntled tone, I couldn't help but notice the empty plate by his bedside."
        "Burnt or not, Phillip still ate all of Owen's cooking,{w=.3} didn't he?"
        "For all of his complaining,{w=.3} Phillip still cares enough to not waste Owen's efforts."
        "I couldn't help but smile softly.{p=.3}It's good to see them get along again."
        
        if day4_item == "none":
            $ day4_item = "phillip"
        
        if day4_item == "phillip":
            $ met_bradley = "true"
            "A thought suddenly struck me as I turned towards Phillip."
            play music "black-cat.mp3" fadein 2
            m "By the way, I've been meaning to ask...."
            m "How did you end up being the Black Cat? {p=.3}If you don't mind telling us."
            
            show phillip irritated with dissolve
            "Phillip sighed and fidgeted uncomfortably."
            p "Eh....{w=.3}it's a bit of a long story.{p=.3}I don't really want to talk about it."
            show owen grin closed with dissolve
            o "Aw, {w=.3} so we don't get to hear your superhero origin story?"
            show phillip serious with dissolve
            p "It's not as impressive as you'd think it is..."
            show owen grin 2 with dissolve
            o "I'm 90\% sure you're just being modest again."
            "Well that was disappointing. {p=3}I was looking forward to hear how Phillip went from such a well-mannered kid to a famous graffiti vandal."
            m "Well...{w=.3}could you maybe tell us more about that wishing well you visited?"
            show phillip neutral with dissolve
            p "Geez, what is this?{w=.3} An interview?"
            show owen neutral with dissolve
            o "I've got to admit, I'm kinda curious to know more about you too."
            o "I mean just a few days ago you were a sweet and polite little thing, {w=.3}and suddenly you turn into this stone-cold vigilante."
            p "Hey hey, {w=.3} even with all that Black Cat stuff, {w=.3}I'm still just me."
            p "What you see is what you get."
            
            play music "wave-piano.wav" fadein 2
            
            "Phillip giggled and flopped back onto his bed."
            p "But I suppose I can still answer your wishing well question.{w=.3} Not that it has anything to do with the Black Cat."
            p "I've been visiting that well for years.{w=.3} It's like my little place of comfort."
            p "It's also a pretty good reading spot!{p=.3}When I read out loud there,{w=.3} it always felt like someone curious was listening intently."
            p "It's probably just my own voice echoing down the well,{w=.3} but it's nice to pretend that someone was there to enjoy my company~"
            p "Come to think of it,{w=.3} I've kind of stopped going there as much ever since-"
            show phillip irritated with dissolve
            "Phillip suddenly snapped his mouth shut, as if he'd bitten his tongue."
            "Looks like we were approaching some dangerous territory. {w=.3}We better steer away for now."
            m "Hey, {w=.3}this might be completely off subject but...{w=.3}have you ever felt like that well was....{w=.3}haunted in any way?"
            
            show phillip neutral with dissolve
            p "Pffft, {w=.3}don't be silly [charname]. {p=.3}Ghosts aren't real."
            o "Hey, you don't know that!"
            m "W-well don't you think that area's a bit creepy or weird?"
            p "Geez, you've been watching too many scary movies."
            o "That,{w=.3} or you've been listening to people gossiping about urban legends around here."
            m "Urban legends?"
            o "Oh right,{w=.3} I keep forgetting you're not from this side of the city."
            o "There's this creepy story surround Bradley Lake that's pretty well-known around here."
            p "I remember I had to write a report about it in middle school. {w=.3}Ugh, they're all just a bunch nonsense."
            o "The Bradley Lake story actually has a bit of real history to it,{w=.3} you know."
            
            
            "I scratched my head in confusion before raising a hand like I was in class."
            m "You guys mind explaining it to an outsider like me?"
            show owen grin closed with dissolve
            "Owen clasped his hands together excitedly."
            o "Of course!{p=.3}Phillip, go turn out the lights! It's story time!"
            p "Geez, a bit overdramatic, aren't you?"
            
            scene black with Dissolve(3.0)
            stop music
            pause(2.0)
            o "So................."
            play music "fragments.mp3" fadein 2
            o "Have you ever head of \"{b}The Black Lady of Bradley Lake?{/b}\""
            "I shook my head, but then realized they couldn't see me in the dark."
            m "Nope, never heard of it."
            o "It's a pretty infamous story around here."
            p "Kinda sad story too."
            o "Once upon a time......"
            p "AKA a few decades ago."
            o "Phillip no interrupting! You're ruining the mood!"
            p "Fine fine, yeesh."
            
            o "As I was saying:{p=.3}Once upon a time,{w=.3} a young couple moved into the cottage near Bradley Lake."
            o "They were a happy couple, {w=.3}proud parents to their newborn child and living a life of peace."
            o "Until one day....{w=.5}the husband left without a word,{w=.5} and his wife was left to take care of their child all alone."
            
            o "The young mother worked tirelessly night and day to raise her child well."
            o "They stayed at the cottage for many months,{w=.3} hoping for their husband and father to come home...."
            play music "blue-feather.mp3" fadein 2
            o "......{w=.5}........but nobody came."
            
            o "One day, {w=.3}a group of burglars and low-lives happened upon the cottage and robbed the place bare of any valuables."
            o "They brutally raped the mother and stole everything she had,{w=.3} even whisking away the basket containing her baby."
            o "The mother was utterly heartbroken and humiliated,{w=.3} left once again,{w=.3} all alone."
            o "But she never gave up hope. {p=.3}She searched day and night for her child for many years......"
            o "Until one fateful day,{w=.3} a storm swept across the Bradley Lake and the subsequent flood washed her away."
            o "They say her body still rests at the bottom of Bradley Lake,{w=.3} rising on occasion to continue her search for her lost child..."
            o "People who visit the lake at night sometimes even hear the ghostly soft voice of a mother,{w=.3} singing her child to sleep...."
            
            "D-d-did he say \"sing?\""
            m "W-wow, {w=.3}that's quite the story...."
            o "It's not as mythical as you'd think.{p=.3}I think the story originated from a real incident that happened about 20 years ago."
            m "You mean it's real-??"
            "I suddenly jump out out of my skin as I felt ice-cold finger slide around my neck-"
            play music "hyperfun.mp3" 
            
            m "{size=+10}-IT'S COLD AS FUCK!!!{/size}"
            
            scene PO dorm with dissolve
            show phillip shrug smile at left
            show owen grin 2 at right
            
            "I smashed the lights on to find Phillip behind me,{w=.3} laughing his ass off."
            p "Oh my god you should have seen your face!"
            m "PHILLIP YOU {i}JACKASS!!{/i}"
            show phillip neutral with dissolve
            p "Hey it's not my fault you scare so easily!"
            play music "easy-lemon.mp3" fadein 2
            p "That story's full of baloney anyway.{p=.3}Just something to keep little kids from sneaking out to the lake at night."
            p "Kinda sad that you're both falling for it."
            
            o "It's nice to see the locals gain a sense of creativity though."
            
            "I force a smile and laugh along with them, {w=.3}but my chest lurched at the memory of the cottage at the lake."
            "There's definitely more to this story than meets the eye....."
        
        
        if day4_item == "owen":
            show phillip serious with dissolve
            "Phillip suddenly pressed a hand against his forehead and squeezed his eyes shut."
            p "Speaking of food,{w=.3} I'm feeling a bit nauseous again."
            show owen neutral with dissolve
            o "You need any help there buddy?"
            "Phillip shook his head slowly before heading out the door."
            p "I can walk to the bathroom on my own, thanks."
            hide phillip with Dissolve(2.0)
            show owen at center with dissolve
            
            "Owen and I stare after him with concern."
            m "Is he...{w=.3}going to be alright?"
            o "Phillip's a tough kid,{w=.3} I wouldn't worry too much."
            show owen grin 2 with dissolve
            o "After all, he's got the great Owen Lorelei to look after him!"
            m "Oh!{w=.3} That reminds me-"
            "I pulled out the package I got from earlier."
            m "Some grumpy mailman guy asked me to give this to you."
            show owen neutral with dissolve
            o "Oh! A delivery for me?"
            
            "As I handed Owen the package, {w=.3}I noticed his face immediately brighten when seeing the sender's name."
            "The package read {w=.3}   \"{b}From: Oleander Lorelei{/b}\"{p=.3}A relative, maybe?"
            
            "Owen hastily opens up the cardboard box and lifted the lid."
            
            play music "drift.mp3" 
            show owen upset with dissolve
            
            "His smile instantly disappeared when he saw whatever was inside."
            "I tried to take a peek, {w=.3}but he quickly closed the box and set it aside."
            show owen grin 3 with dissolve
            o "Thanks for the delivery, [charname]. {p=.3}Hope it wasn't too much trouble for you."
            m "It's no problem.{p=.3}What was inside though?"
            "Owen shrugged,{w=.3} his face unreadable past his forced grin."
            o "Stuff...{w=.3}and things...."
            o "Anyway, I better go check up on Phillip and see if he's doing ok."
            o "I'll be right back!"
            hide owen with Dissolve(2.0)
            
            "As Owen left the room, {w=.3}my eyes were drawn to the cardboard box laying on his desk."
            "I quickly glanced around to see if he's gone."
            "He'd probably get angry if I looked through his mail but..."
            "My hands were prying the box open before my brain could comprehend my decisions."
            
            "The box.....{w=.3}was filled to the brim with letters."
            "Most of them looked really old, {w=.3}some of them even dating back 7 years ago."
            "They were all written by Owen....{w=.3}and addressed to \"Dad\""
            "Not a single letter had been opened."
            "I stared wide-eyed at a sticky note stuck to the inside of the cardboard box. {p=.3}It read: \"Do not contact me again\""
            "This is............"
            "I suddenly felt a gentle hand rest on my shoulder as Owen closed the box lid."
            show owen neutral with dissolve
            o "[charname],{w=.3} it's rude to look through other people's mail, you know."
            m "I'm so sorry!{p=.3}I got a bit curious and..."
            m "............................{p=.3}...........Owen,{w=.3} are you alright?"
            o "Huh? {p=.3}Hehe, are you worried about me?"
            m "Of course I am!"
            "Owen looked taken aback for a moment,{w=.3} but smiled reassuringly."
            show owen grin 3 with dissolve
            o "I'm fine,{w=.3} [charname]."
            show owen neutral with dissolve
            o "This kind of thing's been going on for years. It's nothing new.{p=.3}I'm totally used to it by now."
            o "So no worries, {w=.3}ok?"
            m "It's not healthy to bottle things up like that, {w=.3}Owen."
            m "If you don't want to tell me,{w=.3} can you at least promise to talk to {i}someone?{/i}"
            
            show owen grin nervous with dissolve
            "Owen's face scrunched up with constrained discomfort."
            o "[charname], {w=.3}there are some things that are better left unsaid."
            m "But ignoring your problems won't make them go away-"
            o "Facing them head-on isn't always an option either."
            show owen neutral with dissolve
            o "I'm glad you're worried about me, {w=.3}but talking about it will just dig up bad memories."
            o "So just leave it be,{w=.3} alright?"
            m "Are you sure?"
            "Owen takes a deep breath and forces a wide grin."
            o "Yes [charname]. {w=.3}I'm sure."
            o "Now with that out of the way, let's go make dinner for Phillip."
            show owen grin 2 with dissolve 
            o "I could sure use some help. I'm pretty sure Phillip's getting sick of having burnt spaghetti for his last 3 meals."
            "He's changing the subject."
            "I stare at him unconvinced, but decided not to push it."
            scene black with Dissolve(3.0)
            stop music
            "As I let Owen drag me into the kitchen, I couldn't help but wonder..."
            "How many of those happy-go-lucky smiles are genuine?"
        
        
scene black with Dissolve(5.0)
play music "wave-piano.wav" fadein 3
scene dorm night with Dissolve(2.0)
pause(2.0)

"Today ended rather calmly...{p=.3}It's a nice change after everything that happened yesterday."
"It's good to see everyone back to their normal, cheerful selves~"
"Except......."
"I glanced out the window, {w=.3}my heart skipping a beat."
"Streaks of white soared through the night sky like gentle dust in the wind."
"It's the meteor shower that Echo mentioned earlier today..."

m "Echo! {p=.3}Hey, are you there?"

"There was no answer.{p=.3}Where could he be?"
"With a huff, I trudged out of my room and made my way towards the roof."

scene black with Dissolve(2.0)
scene dorm roof night with Dissolve(2.0)
play music "moonheart.mp3" fadein 2

m "Wow,{w=.3} the view is beautiful up here."
"The shooting stars broke through the blackness of the night in a serene shower of light."
"This scene feels so familiar to me,{w=.3} somehow....."

play sound "ghost.mp3" 
show echo cracked with Dissolve(2.0)

e "Hey there [charname], {w=.3}enjoying the view?"
m "Echo!{w=.3} You're here!"
e "Yup."
e "Heh, why don't we have a seat and enjoy the night together?{p=.3}I'm sure you'd need it after a long day."
m "If you say so....."

"I sat down at one of the tables and stared at Echo."
"His body seemed to shimmer in time with the falling stars, {w=.3}the little cracks on his chest slowly closing up with each falling star."

play sound "ghost.mp3" 
show echo neutral with Dissolve(3.0)
e "Ah, that's much better."

m "Echo...?"
"With that, Echo hopped into a chair beside me and the two of us stared into the trailing night sky."
"There was a gentle but pleasant silence between us,{w=.3} Echo's eyes filled with nostalgia."
"It still astounds me how little I know about him, {w=.3}but at the same time I feel like I've known him since forever..."
"The silence was hanging heavier between the two of us...."
"Finally, Echo spoke."

e "Hey [charname]?"
m "Yeah?"
e "What do you wish?"

$ echo_wish = renpy.input("What do you wish?")
$ echo_wish = echo_wish.strip()

if not echo_wish:
     $ echo_wish = "none"
     
if echo_wish == "Owen Cut Content":
    jump day9_owen
#if echo_wish == "Y'ALL BEST NOT BE DATAMINING' THIS SHIT YO, OR Y'ALL GONNA GET YO ASS CURSED TO HELL BY HALLEY":
    
m "Well...{p=.3}I wish that-"
e "Ssshhhhhhhhhhhhhhhh!{p=.3}It won't come true if you say it out loud, silly!"
m "Then why did you bother asking?"
e "Well I guess......"
e "You know what, {w=.3}how about I tell you a little story instead?"
m "A story?"
e "Yeah,{w=.3} my story."
"Echo closed his eyes and sat back on his chair.{p=.3}He looked so tired....."
e "Once upon a time,{w=.3} a long long time ago, {w=.3}a little star fell from the sky."
e "That star was very bitter. He hated people. {p=.5}They were always demanding stars for selfish things."
e "More wealth, {w=.5}more vanity, {w=.5}more attention....."
e "The little shooting star dreaded what kind of person would wish upon him."
e "Someone selfish?{w=.5} Someone pretentiously good-willed? {w=.5}Or would no one wish upon him at all?"

e "As it turns out, {w=.3}a little six-year-old boy wished upon the star,{w=.3} and that little boy's wish broke his heart."
e "It was a wish no one should have made, {w=.3}especially not a child."
e "...........................it was a quite a foolish wish.................."
e "........................................."
play music "hyperfun.mp3" 
e "No seriously, [charname],{w=.3} it was a {b}really{/b} stupid wish.{p=.3}I was inches away from punching you in the face."
m "W-what?!"
m "I don't remember this at all!"
e "Course you don't, {w=.3}you were six.{p=.3}But that doesn't excuse your stupidity."
m "But what did I even wish for?"

e "I'm not gracing you with an answer. {p=.3}Just thinking about it makes me want to throw you off the roof."
m "Geez, {w=.3}it couldn't have been that bad...."

play music "wave-piano.wav" fadein 3

e "Well, {w=.3}I'll tell you one thing...."
e "I'm still here.{p=.3}That means a part of you still wants that wish to be granted."
e "I'm glad that I've stay with you for so long.....{p=.3}but for your sake,{w=.3} I hope I'll never be granted."
"Echo sighed and placed a comforting hand on my shoulder.{p=.3}His skin was cool to the touch, like a refreshing spring breeze..."
e ".........{w=.3}I have an odd feeling that terrible things will start happening to you and those around you."
e "Enjoy your summer while you can, {w=.3}[charname].{p=.5}It won't last forever."

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

jump day6_morning
label day7_morning:

$ persistent.current_route = "default"
"{b}Day 7:{/b}{w=.5} \"Little Pieces of Time\""

scene black with Dissolve(3.0)
play music "cafe-music.mp3" fadein 3
scene dorm with Dissolve(3.0)

"Waking up on Sunday mornings are supposed to be relaxing,{w=.3} but all I feel is exhaustion."
"I'm still trying to ignore all the confusing things that happened last night."
"It all felt like a tangled story that I don't have all the pieces to."
"It's probably best not to dwell on things I don't understand. {w=.3}Ignorance is bliss,{w=.3} right?"

"Let's go back to normal things,{w=.3} like hanging out with friends-"
"Oh right, everyone's at work today."

"I groaned and turned over in my bed."
"I don't want to just show up and bother them at their jobs.{w=.3} It's tempting to just stay in bed all day."
".................................."
"Sometimes,{w=.3} during these quiet moments,{w=.3} I just feel no energy to do anything."
"Time just simply ticks by..."
"......................sigh,{w=.3} maybe some fresh air can help clear my mind."

play music "snowy-street.mp3" fadein 3
scene courtyard with Dissolve(4.0)
"I strolled around the courtyard absentmindedly.{w=.3} The whole campus felt especially empty on Sundays."
"Everyone's busy with their lives.{w=.3} It makes me wonder why I even came to Gerania Academy in the first place."



play sound "slam.wav" 
"There was a crash and I turned around to find Mrs. Corlisse stumbling over a comically large pile of cardboard boxes."
m "Oh hey Mrs. Corlisse.{w=.3} You ok?"
c "I am fine [charname], {w=.3}thank you.{w=.3} I was just a little careless."
"I bent down and gathered a few boxes for her.{w=.3} They felt rather heavy."
"Should an old woman like her be carrying things like this?"
m "How about I help you move these?{w=.3} I've got nothing better to do."
c "I will accept that offer with graditude.{w=.3} Thank you again, [charname]."

scene office with Dissolve(4.0)
"I helped Mrs. Corlisse carry her boxes all the way to the office building."
"At least I was somewhat useful today."
c "I must say [charname],{w=.3} you are rather kind for such an unmotivated young man."
m "H-hey! {w=.3}I'm not {i}that{/i} unmotivated."
c "Oh? Your classroom participation grade says otherwise."
 
m "Eheh,{w=.3} whoops."
c "Nonetheless,{w=.3} I truly enjoy having you in my classroom."
c "You have much potential [charname]. {w=.3}'Tis only a shame you are not utilizing it."
m "I'm.........{w=.3}ugh."
m "Look teach,{w=.3} Gerania Academy is for rich and honor roll kids."
m "I only got here because I accidentally won a free scholarship and my parents wanted me out of the house."
m "There are a lot of people who deserve to be here more.{w=.3} I was just lucky."

"Mrs. Corlisse observed me carefully before placing a hand on my shoulder.{w=.3} It felt comforting, but firm."
c "If that is what you believe,{w=.3} then you should better yourself into a person that {i}does{/i} deserve it."

c "You have much room to grow,{w=.3} [charname].{w=.3} Don't squander it by feeling bad for yourself all the time."

m "..........................{p=.3}Is this just a big ploy to get me to work harder in your Photography class?"
"Mrs. Corlisse actually laughed."
c "I was speaking of your life choices in general,{w=.3} but more participation in my class would be nice too."
c "Photographs are rather pleasant in that regard.{w=.3} Looking back at them reminds us of how much we've grown."
m "....................\"little pieces of time.\""
 
c "Precisely!{w=.3} I'm impressed [charname],{w=.3} you really do pay attention in my class."
m "That phrase has been popping up a lot lately."
c "Funny you'd say that.{w=.3} I first heard that phrase from my granddaughter."
c "She should be around your age by now.{w=.3} Your attitude certainly reminds me of her."
 
m "I'll take that as a compliment.{w=.3} I think."

c "Haha,{w=.3} it depends on how you look at it."
c "Either way [charname],{w=.3} I hope you will spend your time wisely while at Gerania Acadmey."
m "Sure, I guess.{w=.3} I'll try."
 
 
scene black with Dissolve(3.0)
play music "cafe-music.mp3" fadein 4 fadeout 4
scene dorm roof with Dissolve(3.0)


"Despite Mrs. Corlisse's whole repremanding, {w=.3}I ended up just wandering about the dorm the whole afternoon."
"It was just one of those dead motivation days, I guess."
"The roof was a relaxing place, but all that productivity talk kept bugging me in the back of my mind."
 
m "Ugh, alright fine,{w=.3} maybe I'll try doing something for once."
"I fiddled with the camera hanging from my neck,{w=.3} turning it this way and that."
"Ever since last night,{w=.3} the camera seemed to pulse with warmth."
"Whenever I held it in my hands,{w=.3} it felt like I'm suddenly submerged with soothing hot bathwater."
".......that didn't sound as elegant as it felt."
"Maybe Mrs. Corlisse was right,{w=.3} I should play around with photography more."
m "But what kind of photo should I take?"
m "-oh wait."

 
if day4_item == "owen":
    show crane with Dissolve(2.0)
    "I pulled out the tiny origami crane that Owen gave to me a few days ago."
    m "This might make a good picture."
    "Maybe I could photograph it and make it look all artsy or something."
    "The photo might make a nice little thank-you present to Owen for giving it to me."
    
    "I position the paper crane on the table and carefully adjust the lense on my camera."
    "Here goes nothing."
    
    play sound "camera.wav"
    scene white with Dissolve(2.0)
    play music "noise.mp3"
    
    show photograph with Dissolve(1.5)
    pause(2.0)
    
    "I was falling."
    "Memories and images flashed rapidly like a bursting array of film."
    "Voices were echoing like a distant radio."
    "Where am I?"
    "Who...................{w=.3}..........am..................??????"
    
    stop music 
    play music "rise.mp3" fadeout 7
    scene black with Dissolve(3.0)
    pause(1)
    
    "It was a warm summer afternoon, like any other."
    "Mum was feeling sick again,{w=.3} so he spent the week cheering her up and listening to her stories."
    "Today, she was teaching him how to fold paper into fun little shapes."
    "He liked the bird one."
     
     
    
    scene white with Dissolve(2.0)
    show owen_day7 1 sepia with Dissolve(3.0)
    
    "Owen sat on his mothers lap,{w=.3} watching his mother's hands intently."
    o "W-wow mum! {w=.3}That looks amazing!"
    o "So you just fold it a few times and {i}poof!{/i} {w=.3}It's a birdie!"
    
    "Mother" "Not quite so simple,{w=.3} but that's the gist of it."
    "Mother" "Would you like to learn how to do it yourself?"
    show owen_day7 1 with Dissolve(2.0)
    
    o "Of course! {w=.3}I want to make lots and lots of them!{w=.3} With lots of different colors too!"
    o "They can keep you company in your room until you feel better, mum!"
    
    "Mother" "Haha,{w=.3} you're always so sweet Owen."
    "Mother" "You know,{w=.3} this reminds me of an old story."
    "Mother" "They say that if you make a thousand of these paper cranes,{w=.3} one of your wishes will come true."
    o "R-really?!"
    "Owen pondered this for a moment,{w=.3} and then grinned excitedly up at his mother."
    o "Then I'll do it!{w=.3} I'll fold a thousand paper cranes!"
    
    "Mother" "Oh?{w=.3} And what would you wish for, dear?"
    o "I'd wish for you to feel better soon!"
    o "And then we can call dad back home and do family stuff together."
    o "We'd have dinner and go on picnics and tell stories!{w=.3} It'll be great!"
    
    play sound "noise.mp3"
    show photograph with dissolve
    pause(2.0)
    
    scene black with Dissolve(3.0)
    show owen_day7 2 sepia with Dissolve(3.0)
    pause(2.0)
    
    o "I-it'll be alright.{p=.3}E-e-everything's going to be ok!"
    o "I-I just have to make a thousand a-a-and my wish will come true a-and mum will get better. {w=.3}Everything will be better!"
    show owen_day7 2 with Dissolve(3.0)
    o "I j-just have to make a thousand........."
    
    play sound "noise.mp3"
    scene photograph with Dissolve(1.5)
    scene black with Dissolve(3.0)
    
    stop music
    
    scene dorm roof night with Dissolve(3.0)
    play music "wave-piano.wav" fadein 5 fadeout 5
    
    
    "I fell out of my chair and scrambled across the floor,{w=.3} my heart hammering rapidly against my chest."
    "W-what the hell was that?!"
    "W-was that.............{w=.3}Owen's memories?"
    "D-did I just see Owen's past?!{p=.3} And I did it by just snapping a photo?!"
    "No no no,{w=.3} this can't be real."
    "I took plently of photos before this one and no crazy flashbacks happened before!"
    "Why now?"
    
    play sound "ghost.mp3"
    show encounter 2 sepia with Dissolve(1.0)
    pause(1.0)
    hide encounter 2 sepia with Dissolve(2.0)
    
    "Last night,{w=.3} when I ran into Jinny............{w=.3}my camera started glowing along with hers."
    "Is that was triggered all of this flashback nonsense?"
    
    
    "What should I tell Owen?"
    "..........no,{w=.3} it'd probably best that I keep this to myself."
    "...................................."
    "I-I......I need some rest.{p=.3} Maybe some sleep."
    "Yeah, {w=.3}I just need to sleep it all off. {w=.3}Everything will be fine."
if day4_item == "phillip":
    show jade coin with Dissolve(2.0)
    "I pulled out the tiny jade coin that Phillip gave to me a few days ago."
    m "This might make a good picture."
    "Maybe I could photograph it and make it look all artsy or something."
    "The photo might make a nice little thank-you present to Phillip for giving it to me."
    
    "I position the jade coin on the table and carefully adjust the lense on my camera."
    "Here goes nothing."
    
    play sound "camera.wav"
    scene white with Dissolve(2.0)
    play music "noise.mp3"
    
    show photograph with Dissolve(1.5)
    pause(2.0)
    
    "I was falling."
    "Memories and images flashed rapidly like a bursting array of film."
    "Voices were echoing like a distant radio."
    "Where am I?"
    "Who...................{w=.3}..........am..................??????"
    
    stop music 
    play music "into-thin-air-slow.mp3" fadeout 7
    scene black with Dissolve(3.0)
    pause(1)
    
    "It was a warm summer day by the lake, {w=.3}and he was all alone again."
    "Except not truly."
    "The cool breeze swept through the woods and ruffled the pages on the book he was reading."
    
    scene white with Dissolve(2.0)
    show phillip_day7 1 sepia with Dissolve(3.0)
    
    "Phillip was sitting in his favorite reading spot again,{w=.3} next to the old wishing well."
    p "\"And so the prince finally rescued his love and they lived happily ever after.\"{p=.3}   The end."
    p ".........how did you like this one, {w=.3}Mimir?"
    
    play sound "chains.mp3"
    show phillip_day7 2 sepia with Dissolve(3.0)
    
    mm "..................{w=.3}This one sucks."
    mm "Real life almost never ever ends that neatly. {w=.3}It's always messy with dead ends."
    mm "More often than not,{w=.3} the bad guys wins."
    
    show phillip_day7 2 with Dissolve(2.0)
    p "Oh c'mon, don't be such a pessimist Mimir!"
    p "Everything works out in the end if you keep your chin up."
    p "Sometimes you just gotta let things work themselves out!"
    
    
    mm "And sometimes you get chained to a filthy well for 300 years."
    mm "Hate to break it to ya kiddo,{w=.3} real life ain't pretty."
    p "Maybe you're just getting old and senile."
    mm "Hey,{w=.3} watch it kid."
    mm "Show some respect to your elders.{w=.3} Plus, you still owe me after stealing all the coins from my well."
    p "I gave you a new coin,{w=.3} didn't I?"
    mm "A tiny little jade coin?{w=.3} Are you kidding me?"
    mm "Back in the day,{w=.3} people used to offer me coins of gold and silver."
    
    p "Oh pfffft,{w=.3} what's a ghost going to do with money?{w=.3} It's the thought that counts!"
    mm "Kid, {w=.3}how many times do I have to tell you? {p=.3}I'm a wish."
    mm "And I'm {i}still{/i} waiting for you to wish for something!"
    mm "Your jade coin is a terrible offering,{w=.3} but at least tell me what you want!"
    p "Hmmmm........{w=.3}I'm pretty happy at the moment."
    p "I'll tell you when I think of something."
    mm "Ugh,{w=.3} alright kiddo."
    mm "I'll be here whenever you need me,{w=.3} especially if the bad guys of the world start catching up to you."
    p "Don't be silly Mimir."
    p "I'll be perfectly fine!"
    
    stop music
    play sound "noise.mp3"
    play music "horror.mp3" fadeout 5
    show photograph with dissolve
    pause(2.0)
    
    scene black with Dissolve(3.0)
    show phillip_day7 3 sepia with Dissolve(3.0)
    pause(2.0)
    
    "???" "Oh it's adorable how much you struggle.{w=.3} I could just eat you up."
    "???" "We're going to have so much fun."
    p ".........................................................."
    "He felt a hand on his thigh.{w=.3} The sickly warmth made his stomach curl with a thousand needles."
    "???" "Come now, {w=.3}work with me sweetheart."
    "???" "This can be fun for both of us if you just play along.{w=.3} How about it?"
    show phillip_day7 3 with Dissolve(2.0)
    p ".................................................................."
    "???" "Is this how you're going to be, sweetheart? {w=.3}I think you need another beating to put you in your place-"
    p "Don't touch me."
    
    play sound "slam.wav" 
    "Another blow cracked across his face.{w=.3} It stung,{w=.3} this time drawing blood."
    "Phillip spat red spit at him. {w=.3}He was too tired.{w=.3} It missed."
    p "Let. {w=.3}Me. {w=.3}Go."
    
    "???" "How dare you even {i}think{/i} of telling me what to do."
    "???" "Who do you think you are?"

    
    play sound "chains.mp3"
    show phillip_day7 4 with Dissolve(2.0)
    pause(1.0)
    
    p "Are you deaf?"
    p "I said:{p=.3}{size=+10}{i}{b}Let. {w=.5}Me. {w=.5}Go."
    pause(1.0)
    
    play sound "noise.mp3"
    scene photograph with Dissolve(1.5)
    scene black with Dissolve(3.0)
    stop music
    
    scene dorm roof night with Dissolve(3.0)
    play music "wave-piano.wav" fadein 5 fadeout 5
    
    
    "I fell out of my chair and scrambled across the floor,{w=.3} my heart hammering rapidly against my chest."
    "W-what the hell was that?!"
    "W-was that.............{w=.3}Phillip's memories?"
    "D-did I just see Phillip's past?!{p=.3} And I did it by just snapping a photo?!"
    "No no no,{w=.3} this can't be real."
    "I took plently of photos before this one and no crazy flashbacks happened before!"
    "Why now?"
    
    play sound "ghost.mp3"
    show encounter 2 sepia with Dissolve(1.0)
    pause(1.0)
    hide encounter 2 sepia with Dissolve(2.0)
    
    "Last night,{w=.3} when I ran into Jinny............{w=.3}my camera started glowing along with hers."
    "Is that was triggered all of this flashback nonsense?"
    
    
    "What should I tell Phillip?"
    "..........no,{w=.3} it'd probably best that I keep this to myself."
    "...................................."
    "I-I......I need some rest.{p=.3} Maybe some sleep."
    "Yeah, {w=.3}I just need to sleep it all off. {w=.3}Everything will be fine."



scene black with Dissolve(3.0)
stop music
scene dorm night with Dissolve(3.0)

pause(1)
"............Sleep just won't come, will it?"
"There's an uncomfortable weight digging into my chest.{w=.3} It felt so wrong to just pry open other people's secrets like this...."
"Hm?"
"A familiar chill swept through the room.{w=.3} I sighed and sat up on my bed."
m "Halley,{w=.3} what do you want?"

play sound "ghost.mp3"
play music "asphodel.mp3" fadein 3
show halley neutral with Dissolve(2)

u "Oh good,{w=.2} you're not dead yet."
u "I need to talk to you."
m "Could you knock the next time you barge into my room?"
u "Absolutely not,{w=.3} that would imply I respect you in some vague manner."
u "Back to the point, {w=.3}where is your wish?"
m "Huh?"
u "Ugh, did you forget already? {w=.3}That puny shooting star that's always following you around."
m "You mean Echo?{w=.3} I haven't seen him since yesterday morning."
m "He kinda just comes and goes whenever he likes."

u "Shirking his duty,{w=.3} figures."
u "Quite suspicious too."
"Halley crosses her arms and tapped her feet thoughtfully."

u "Tell me [charname],{w=.3} what is Echo's center?"
m "Center?"
u "Ugh, why are you so clueless?"
u "A center is a wish's core. {w=.3}It's the desire that evoked his creation. His bond to you as his wisher."

"Mm......{w=.3}now that I think about it......"
m "I don't know.{w=.3} He never told me what I wished for when I was younger. Although I do have an aching suspicion...."
stop music
"Halley frowned and gave me a calculating look."
u "Listen closely [charname], {w=.3}I'll only say this once."
play music "fragments.mp3" fadein 2
u "Do not trust Echo."

m "What?"
u "Think about it."
u "He pops into your life out of nowhere but claims to have known you."
u "He tells you close to nothing about why he's here, and you know nothing about his intentions."
u "Not to mention how he's never around when you actually need him."
u "Can you really trust someone like that?"

m "I could say the same about you, Halley."
u "True, {w=.3}but my point still stands."
m "Did you come all this way just to give me a bullshit warning?"
u "Certainly not,{w=.3} I came all this way to give you {b}{i}two{/i}{/b} bullshit warnings."
u "In two days on the 9th,{w=.3} you will need to make a choice.{p=.3} A difficult one."
u "Your friends need your aid.{w=.3} But are you capable enough to provide it?"

play sound "ghost.mp3" 
hide halley with Dissolve(3.0)

"......................and she's gone."
"I sighed and buried myself into the mattress again.{w=.3} Why does everyone have to speak in riddles?"
"Too tired to think about it now.{w=.3} It's best I get some sleep...."

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

jump day8_morning
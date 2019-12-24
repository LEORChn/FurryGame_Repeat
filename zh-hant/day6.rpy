label day6_morning:
$ persistent.current_route = "default"
"{b}Day 6:{/b}{w=1} Polarized"

play music "calm-guitar.mp3" fadein 3
scene kitchen with Dissolve(3.0)
pause(2.0)

"The Saturday sunlight streamed through the window as I tried to keep my eyes open at the kitchen table."
"Everyone was up early for some ungodly reason,{w=.3} but at least Sissel was cooking up a delicious breakfast for us."
"We all decided Owen was forbidden from cooking anything.{p=.3}The kid was like a walking fire hazard."
"Sissel gave Phillip an earful for blowing up the toaster a few days ago too."
"He's pretty protective of his kitchen..."

m "My first weekend here at the academy huh....{p=.3}I'm not even sure there's anything to do."
m "What plans do you guys have? {w=.3}Wanna hang out or something?"

show phillip smile shrug at farleft with dissolve
show sissel neutral at farright with dissolve
show owen neutral at center with dissolve

p "The boredom's already taken hold, huh?"
show phillip neutral with dissolve
p "Sorry but I can't hang out much today. {w=.3}I've got a job at the local community center."
show owen grin with dissolve
o "Wait, the one at the West end of town? {p=.3}I work there too!"
"Aw,{w=.3} it looks like everyone's busy today-"
m "-wait."
s "-what?!"
p "-seriously?!"

hide phillip
hide sissel

"Everyone" "{size=+15}YOU HAVE A JOB?!!?!?!{/size}"

show phillip no at farleft with dissolve
show sissel wtf at farright with dissolve

show owen grin nervous with dissolve

o "Geez, is it that much of a surprise?"
m "B-b-but you're rich!"
s "You sure you didn't hit your head this morning?"
p "I didn't think you had much of a work ethic to be honest..."

o "Ouch you guys are breaking my heart."
show owen neutral with dissolve
o "I guess you're all sorta right though. {p=.3}It's more volunteer work than a job~"
m "Wow Owen, that's pretty altruistic of you."
show owen grin 2 with dissolve
o "It's also a great place to pick up cute guys!{p=.3}You all should drop by sometimes,{w=.3} maybe I could introduce you heh~"
"There was a collective groan of exasperation across the room."
show phillip smile shrug with dissolve
p "Just when you were accidentally cool there for a moment..."
show phillip neutral with dissolve
p "Well,{w=.3} I better head off to work now. {p=.3}See you all around!"
hide phillip with dissolve
show owen neutral with dissolve
o "W-what Phillip! {p=.3}What do you mean \"accidentally cool??\""
hide owen with dissolve
show sissel neutral at center with dissolve

"And there they go. {p=.3}The dorm space feels pretty empy and quiet with the two of them gone."
m "I guess you're busy at the cafe today too?"
s "Actually no,{w=.3} I'm stupidly free today."
"Sissel was mumbling under his breath as he cleaned up the dishes at the kitchen sink."
s "Boss insisted I get a day off."
s "Something like \"I'm the one paying ya!{w=.3} If I say yer getting a break,{w=.3} yer getting a break!\""
m "At least you get some time to relax now."
s "Ugh,{w=.3} what am I even supposed to do with an entire day?"
"Sissel finished rinsing the rest of the dishes and made his way out the door with a huff."
s "Well I'm heading off too. {p=.3}See ya around [charname]."

hide sissel with dissolve

"I was alone in the kitchen now."
"..............................................."
"There's something really hollow when you're all alone while your friends are busy doing other things."
"Tugging at my hair, {w=.3}I leaned back on my chair and stared blankly at the ceiling."
"Weekends were a time of peace and relaxation,{w=.3} but noooo everyone had to get a job."
"The only other guy to have the day off doesn't even know how to relax!"

"What am I even doing today?"


menu:
    "Visit the community center.":
        "Getting to know this side of the city sounds somewhat appealing."
        "It might be fun to see Owen and Phillip at work too.{w=.3} I wonder what they do there?"
        
        "I pushed myself off my lazy ass and headed out the door."
        
        
        scene community center with Dissolve(4.0)
        
        "I spent a good hour wandering lost around the neighborhood searching for this place."
        "The community center huh? {w=.3}It's a bit bigger than I expected."
        
        "As I made my way towards the entrance, {w=.3}I noticed something odd bobbling around the sidewalk."
        show pigeon with Dissolve(2.0)
        "It was...............{w=.3}an incredibly fat pigeon."
        "The literal borb was waddling around, pecking at bread crumbs that the community center visitors no doubt left for it."
        "What a lazy bird,{w=.3} I wouldn't be surprised if it was too fat to fly."
        "As I walked past it,{w=.3} the pigeon looked up at me expectantly, {w=.3}as if I was going to contribute to its food hoard."
        m "What? {w=.3}I've got nothing for you buddy."
        
        "The pigeon gave an indignant chirp before returning its attention to its crumbs. {w=.3}What a lazy little-"
        m "Ugh, fucking- {w=.3}get a job."
        
        "Fat Pigeon ruffled its feathers in the bird equivalent of an eye roll."
        "In hindsight I should probably take my own advice."
        "With a depressed sigh, I left the bird alone and entered the community center."
        
        
        scene community lobby with Dissolve(4.0)
        
        "Wow, the inside of this place was quite cozy.{w=3} It turns out this place offers a lot of services too."
        "There were offices for medical assistance,{w=.3} a food pantry,{w=.3} and even a public ice skating rink at the far end of the hall."
        "I wonder where I should go."
        
        menu: 
            "Ice skating rink":
                "I almost walk past the ice rink entrance, {w=.3}but a familiar echo of laughter grabbed my attention."
                "Curiousity building,{w=.3} I followed that laughter down the hall."
                
                
                scene ice rink with Dissolve(4.0)
                
                "The ice rink was huge! {w=.3}I didn't expect a place like this inside a community center of all places."
                "I leaned over the edge of the arena,{w=.3} scanning the place closely.{p=.3}There!"
                "Phillip was dancing his way across the ice, accompanied by a small group of elementary-school aged students."
                "The little guys were following him like a pack of ducklings."
                "While most were still wobbly on their feet,{w=.3} Phillip was laughed and gliding backwards around them with a kind of grace most people lacked even on solid ground."
                
                "It suddenly dawns on me that he was teaching a class."
                
                
                "Phillip claps sharply to catch the class's attention."
                show phillip neutral with dissolve
                p "Alright guys, great job today!{w=.3} That wraps up today's lesson!"
                p "Everyone's improved so much, {w=.3}y'all should be proud!"
                "I snickered.{w=.3} That was a lot of praise for a bunch of wobbling knees."
                "Despite this,{w=.3} there was a triumphant cheer from the class."
                "The kids beam at Phillip like he's the star of their little ice-skating world."
                
                p "Ok guys, {w=.3}make sure to sign out before you leave with your parents-"
                "Kid" "Wait wait!{w=.3} Mr. Phil,{w=.3} you promised to show us a swirly jump!"
                "The rest of the class joined in with pleading shouts."
                p "Haha alright alright,{w=.3} you win."
                p "Here I go..."
                
                hide phillip with dissolve
                
                "Phillip takes a running (skating?) start, {w=.3} expertly gaining speed with the slightest movements."
                "He circled the rink once with arms outstretched, {w=.3}his every move flowing with the grace of a swan."
                "Suddenly he was airborne, {w=.3}twirling smoothly with balletic control."
                "I blinked in awe and almost forgot to breathe."
                "Phillip landed on one leg, {w=.3}the other outstretched behind him."
                "Even when landing,{w=.3} he was light as a feather. {p=.3}With one last graceful spin, Phillip slowed to a halt before bowing to his cheering class."
                play sound "bell.wav"
                
                "The class's eruption of awed yells were interrupted by the ringing bell."
                show phillip smile shrug with dissolve
                p "Whoops,{w=.3} looks like it's time to go!{w=.3} Single file line everyone, be careful when leaving the rink."
                p "Hm?"
                show phillip shrug blush with dissolve
                "Phillip suddenly seems me standing in the background and waves cheerfully."
                "I try to wave back in the most impressed manner I could. {w=.3}I think Phillip blushed a little."
                "Kid" "Hey Mr. Phil! {w=.3}Who's that?"
                "Other Kid" "I know! I know!{w=.3} It's your boyfriend!"
                show phillip neutral with dissolve
                "Phillip laughed good-naturedly."
                p "No, no,{w=.3} that's just a friend from school."
                p "He's a cool photographer."
                
                stop music 
                
                "This elicits a gasp of horror from one of the students."
                play music "batty.mp3"
                "Kid" "Oh no!{w=.3} He's a paparazzi!{w=.3} My mum says they're evil!"
                "Yet Another Kid" "What's a \"papa-razzi?\""
                "Kid" "They invade your privates!"
                "There was a gasp of horror from the class."
                "Phillip looks to me with an appologetic smile."
                p "I think you mean \"privacy-\""
                "Other Kid" "Quick everyone, {w=.3}we have to protect Mr. Phil's privates!"
                "The entire class suddenly turns and glares at me like a pack of ferocious piranhas."
                "I gulped."
                
                scene black with Dissolve(3.0)
                play music "lullaby-guitar.mp3" fadein 3
                scene community lobby with Dissolve(3.0)
                
                "Kids were terrifying."
                "I had to dodge half a dozen sneakers and lunchboxes before I managed to reach Phillip at the edge of the ice rink."
                "A few kids even tackled me and tried to bite my fingers off."
                "A small army of parents had to rescue me and wrestle the pile of children thrashing on top of me."
                "I couldn't help but smile even through this traumatizing ordeal.{w=.3} At least all the kids were loyal to Phillip."
                "He wields a scary amount of power here."
                
                
                "I give a sigh of relief as I finally catch up with Phillip."
                show phillip neutral with dissolve
                "Phillip looked up from helping a kid untie his ice skates."
                p "[charname],{w=.3} did you survive-?"
                p "Whoa, that's one hell of a black eye."
                
                "The kid suddenly gapes, {w=.3}bug-eyed."
                "Kid" "Mr. Phil said a bad word!{w=.3} You're not supposed to say the h-word!"
                "Phillip lets out a guilty laugh."
                p "Oh no, {w=.3}the paparazzi's evilness is rubbing off on me!"
                m "Hey!{w=.3} Don't throw me under the bus!"
                "The kid glares at me,{w=.3} and with the most serious possible face,{w=.3} said:"
                "Kid" "I'm going to kill you in your sleep."
                "My insides froze in terror.{w=.3} What the hell was wrong with these kids?!"
                
                p "Now now Arnold,{w=.3} don't be mean. {w=.3}Go on and sign out before your parents get tired of waiting."
                "Kid" "Aw alright.{w=.3} See you next week Mr. Phil!"
                "As the student wandered off,{w=.3} Phillip dusted himself off and grins."
                p "Sweet kids,{w=.3} aren't they?"
                m "{b}{i}They're demon spawn.{/i}{/b}"
                p "Aw don’t be so negative [charname],{w=.3} you were once like that too!"
                m "I was never that aggressive!{w=.3} I just hid in my room all day and refused to interact with the outside world."
                p "Boy, that’s a sad,{w=.3} sad childhood [charname]."
                p "Tell you what, there’s still some time before my next class.{w=.3} How about we unwind with a little ice skating session?"
                m "Uh, I’ve never ice-skated before…"
                p "Hey no worries!{w=.3} I get paid to teach people this stuff.{w=.3} It’ll be fun!"
                m "Ack,{w=.3} if you insist Mr. Phil."
                p "Eh don’t call me that.{w=.3} It feels weird coming from you."
                
                scene ice rink with Dissolve(4.0)
                
                "Phillip coaxes me into a pair of rental ice skates and steers me onto the rink."
                "I stumbled around like a newborn calf,{w=.3} but Phillip holds firm to my hands, skating backwards as he does so."
                "As we waddled forward,{w=.3} his grip held gentle but firm.{w=.3} His hands felt rather cold though…"
                show phillip smile shrug with dissolve
                p "See?{w=.3} You’re getting the hang of it!"
                m "Gee thanks.{w=.3} I almost fell on my face twice."
                "Phillip only laughed and nudged me to go faster."
                show phillip neutral with dissolve
                p "You know,{w=.3} sometimes pain is the best teacher."
                m "Easy for you to say-{w=.3} OOF!!"
                "My face hurtled toward the icy floor yet again."
                "I felt a rough tug at my shoulders as Phillip twirls me back onto my feet." 
                p "See,{w=.3} that wasn’t so bad was it?"
                p "I didn’t have to catch you nearly as much as most of my students."
                "I studied Phillip for a moment,{w=.3} an odd thought striking me."
                p "Hm?{w=.3} What’s with that look?{w=.3} Do I have something on my face?"
                m "No...{w=.3}no."
                m "It’s just that,{w=.3} it feels kinda weird seeing you be so gentle and friendly."
                m "Especially after how ferocious you were at Mr. Dolores a few days ago.{w=.3} It’s like you’re a whole different person..."
                
                show phillip serious with dissolve
                "Phillip was quiet for a moment."
                p ".....Everyone wears masks to hide parts of themselves, {w=.3}[charname]."
                p "We’ve all got something to hide.{w=.3} Can you honestly say that you’re comfortable with every part of yourself?"
                m "No......{w=.3}but I don’t have a secret identity."
                show phillip neutral with dissolve
                p "Haha,{w=.3} I was talking metaphorically,{w=.3} but yeah you’re right."
                p "Sometimes I’m Phillip,{w=.3} sometimes I’m the Black Cat."
                p "But in the end,{w=.3} I’m still just me."
                p "I hope we can still be friends though."
                m "O-of course!{w=.3} I’m just not really used to seeing you act so....{w=.3}differently?"
                m "Why did you adopt a vigilante alter-ego?{w=.3} Sounds like something out of a comic book."
                p ".....It's a long story."
                p "I guess once you’ve been hurt once,{w=.3} you can’t help but see how much hurt is in the world."
                p "There’s just so much corruption in the system."
                p "Like Mr. Dolores.{w=.3} And the West Orphanage incident."
                p "I just.....{w=.3}can’t stand idle and watch it just happen,{w=.3} you know?"
                p "I don’t want other people to get hurt too."
                m "That’s......{w=.3}very brave of you actually."
                p "Brave is one word for it.....{w=.3}Other people would call it stupid."
                "Phillip looked up at me and smiled.{w=.3} He squeezed my hands gently."
                p "Thank you though, [charname].{w=.3} It’s nice to hear you’re not weirded out yet."
                p "Are we still friends?"
                "His voice sounded so fragile as he stared up at me,{w=.3} waiting for a response."
                "I gripped his hands and gently squeezed back."
                m "Of course,{w=.3} still friends."
            "Food pantry":
                "The food pantry looked pretty inviting. {w=.3}There were plenty of people bustling around."
                "Maybe one of them will know where Owen or Phillip works."
                
                scene pantry with Dissolve(4.0)
                "Whoa,{w=.3} this place was full of people."
                "Workers were running around,{w=.3} organizing boxes and handing out bags of food to the needy."
                "It was like a crazy scurrying assembly line,{w=.3} everyone busy with their own little job."
                m "Oh hey,{w=.3} isn't that-"
                "Yup, {w=.3}that's Owen."
                "He's carrying an enormous crate of canned food and dodging other workers as he made his way towards the shelves."
                 
                show owen neutral with dissolve
                o "Oh! {w=.3}Hey there [charname]!"
                m "Owen! {w=.3}What are you doing here?"
                o "Haha did you forget already? {w=.3}I work here every weekend as a volunteer."
                m "Like,{w=.3} for extra credit for school or something?"
                o "No, no,{w=.3} none of that. {w=.3}I just want to help people out!"
                o "This might be a big city,{w=.3} but there are still a lot of starving people out there on the streets."
                o "......Sissel used to be one of them."
                show owen grin 2 with dissolve
                o "I just gotta do my part to make sure there's less of that in the world,{w=.3} you know?"
                "I grinned and reached up to give Owen a pat on the back."
                m "You're doing good work Owen.{w=.3} I'm proud of you."
                show owen neutral with dissolve
                o "Heheh,{w=.3} you really think so?"
                "If it wasn't for his bright orange fur, {w=.3}I would have sworn Owen just blushed."
                m "Of course!{w=.3} I never really expected a rich guy like you to be so charitable."
                m "The world could use more people like you."
                m "Speaking of which,{w=.3} do you need any help here? {w=.3}I've got some free time."
                
                stop music
                o "............um{w=.3}..................."
                play music "groove.mp3" fadein 3
                o "I dunno.......{p=.3}I mean,{w=.3} I'm doing most of the dirty work here."
                
                "Now that he mentioned it,{w=.3} I noticed Owen was organizing the biggest boxes around. {w=.3}His pile of crates was much larger than anyone else's."
                "In comparison, the other volunteers' piles might as well be grains of sand."
                "I peered up at Owen. {w=.3}His face was strained with sweat and fatigue as he heaved another box of canned food onto the shelves."
                m "But why-"
                
                "I jumped.{w=.3} The old oafish manager behind us suddenly gave a gruff shout."
                "Manager" "Oi Lorelei!{w=.3} Quit slacking off and get back to work!"
                o "Yessir-"
                stop music
                play sound "slam.wav"
                o "-OOPH!!"
                
                "The manager chucked a nearby can at Owen. {w=.3}The metal can bounced off the back of his head with a blunt {i}thud!{/i} and splattered open on the floor."
                "Manager" "Well,{w=.3} what are you waiting for Lorelei?!{w=.3} Clean up your mess!!"
                play music "snowdrop.mp3"
                o "................yes sir."
                
                "Owen simply shrugs and made his way toward a nearby mop."
                "The other volunteers around us snickered and sneered amoungst themselves."
                "I heard one of them whisper to another \"Filthy Lorelei\" before I finally snapped."
                
                m "{i}You there, {w=.3}shut the fuck up!{/i}"
                m "You think it's funny?{w=.3} I don't see you being nearly as productive."
                m "{i}Quit your staring and get the hell back to work!{/i}"
                
                "There was a startled silence in the room before everyone scrambled back to their duties, {w=.3}their heads tucked down and avoiding eye contact."
                "My heart was hammering furiously against my chest as I turned back towards Owen."
                "He blinked at me,{w=.3} completely bewildered."
                
                "With a sigh,{w=.3} I leaned up to inspect the back of his head."
                m "You doing alright there, big guy?"
                show owen grin nervous with dissolve
                o "Y-yeah,{w=.3} I'm fine!"
                
                "Sure enough,{w=.3} his head only looked slightly bruised.{w=.3} Still looked painful though."
                m "Need me to grab you an ice pack?"
                
                show owen neutral with dissolve
                o "No no,{w=.3} it doesn't hurt much."
                m "If you say so."
                
                "I grabbed the mop out of his hands and start cleaning up the mess on the floor."
                "Seriously,{w=.3} what is wrong with these people?"
                "Owen awkwardly watched me finish cleaning the floors,{w=.3} not sure what to do."
                m "So,{w=.3} as I was saying,{w=.3} do you need any more help with anything?"
                o "Oh,{w=.3} um..."
                
                "I sighed and grabbed a crate from his pile.{w=.3} The box strains painfully under my grip."
                "How the hell does Owen do this all day?"
                
                m "Owen....{w=.3}what the hell was that?"
                m "How can you just stand their and take people's shit all day? {w=.3}Doesn't it bother you at all?"
                show owen grin nervous with dissolve
                
                o "Don't worry about it!{w=.3} I'm totally used to it."
                "There was a loud thud as I slid the box into a nearby shelf."
                m "You know,{w=.3} I'm not sure if that's supposed to be comforting."
                
                show owen neutral with dissolve
                o "Seriously [charname],{w=.3} don't worry about it.{w=.3} It'd be a miracle to find someone who doesn't hate my family these days."
                o "It's not like their hatred isn't justified."
                o "My family's aggressive and shady business decisions ruined a lot of lives."
                
                show owen upset with Dissolve(2.0)
                
                o "...There's this street downtown I used to go to all the time when I was younger."
                o "It used to bustling with life and shops.{w=.3} Everyone there knew each other and where thriving in their own little way."
                show owen neutral with dissolve
                o "The ice cream lady at one shop even used to give me and Sissel free sundaes on weekends."
                o "I loved that place."
                
                show owen upset with dissolve
                o "....................................."
                o ".....{w=.3}Now that street is a ghost town."
                o "Every single shop closed.{w=.3} Every family moved out."
                o "Because of my family's actions."
                o "They reaped the rewards while the little people were run out of business."
                
                m "But you're not your family!{w=.3} You didn't do anything to these people!"
                m "Hell,{w=.3} you're {i}volunteering to help!{/i}{p=.3}They're just being assholes."
                o "You can't deny that my family's bank account is full and thriving thanks to their misfortune though."
                show owen grin 2 with dissolve
                o "Don't worry [charname],{w=.3} I'm working here only because I want to."
                m "They could at least thank you for your work-"
                m "Wait,{w=.3} are you working here to pay penance for your family's decisions?{w=.3} That's fucked up Owen-"
                show owen neutral with dissolve
                o "{i}I'm here because I chose to be here.{/i}"
                
                "Owen raised his voice but his expression didn't change.{w=.3} I took a step back."
                "His constant smile suddenly felt a bit unsettling."
                
                "Owen sighed and scratched his head awkwardly."
                show owen grin nervous with dissolve
                o "....Look [charname],{w=.3} my family took a lot from this city."
                o "I just want to do my part to give back in whatever way I can."
                m "But-"
                show owen neutral with dissolve
                o "[charname] just drop it."
                o "You don't hate me.{w=.3} That's good enough for now."
                
                "I drew a resigned breath before reaching out to grab Owen's hand,{w=.3} squeezing it gently."
                m "Alright,{w=.3} I'll stop bringing this up."
                m "But just remember that I'm your friend.{w=.3} If you ever need anything,{w=.3} just tell me and I'll come running."
                "Owen's hands squeezed back and he laughed."
                "For a moment,{w=.3} his eyes were wet around the edges."
                o "Hearing that from you means more than you can imagine."
                o ".............{w=.3}thanks, [charname]."
    "Follow Sissel.":
        m "Wait Sissel!"
    
        scene dorm hallway with Dissolve(3.0)
        
        "I bounded down the hall after Sissel's retreating back."
        show sissel neutral with dissolve
        s "Hm?{w=.3} What do you want?"
        m "I was wondering, {w=.3}uh, {w=.3}if I could just hang out with you today."
        s "Wha?{p=.3}You could literally be doing anything else."
        m "But I figured we could spend some time together!"
        show sissel embarrassed with dissolve
        s "Ugh,{w=.3} there you go with that mushy shit again."
        show sissel neutral with dissolve
        s "Fine,{w=.3} but I'm not doing anything particularly interesting."
        s "So just follow along,{w=.3} I guess."
        
        play music "lullaby-guitar.mp3" fadein 3
        scene lake road with Dissolve(4.0)
        
        "Sissel and I ended up taking a long,{w=.3} relaxing stroll down around Bradley Lake." 
        "It sounded boring at first,{w=.3} but it was nice to spend time just leisurely chatting."
        "Sissel also said something about coming here for \"old times sake\"."
        
        show sissel neutral with dissolve
        s "You know,{w=.3} I never had anyone to just relax and talk to like this when I was younger."
        s "This is kind of nice..."
        m "What were things like when you were younger?{p=.3}If you don't mind me asking."
        s "Pretty nosy,{w=.3} are you?"
        s "Well I guess I did bring the topic up."
        m "Eh, sorry.{p=.3}You don't have to tell me anything if you don't want to."
        s "No....{w=.3}It'd do me some good to talk about it."
        s "Just don't laugh, {w=.3}got it?"
        m "Of course."
        s "Well for starters,{w=.3} I lived here in my homeless days after I ran away from the West Orphanage."
        m "Here? {w=.3}At the lake?"
        s "Specifically that old cottage deeper in the woods."
        s "It was abandoned and I needed a place to stay.{p=.3}The place might look creepy, but things are actually rather cozy on the inside."
        s "Kept me dry from the rain at least."
        
        
        play music "blue-feather.mp3" fadein 3
        "The old cottage huh?"
        "My thoughts flickered back to the incident a few days ago. {p=.3}That abandoned wish showed up in front of the cottage,{w=.3} didn't it?"
        if met_bradley == "true":
            m "Hey Sissel? {w=.3}Have you ever heard of the \"Black Lady of Bradley Lake?\""
            "Sissel rolled his eyes as I spoke."
            s "Oh that old ghost story?{p=.3}It's nothing but bullshit you know."
            m "But I heard the story's based off of a real incident that happened there years ago."
            s "Not sure about the \"real incident\" bit, {w=.3}but there sure ain't any ghosts there."
            s "I should know,{w=.3} I lived there for {i}years{/i}.{p=.3}There was never anything particularly weird, {w=.3}and no people in general."
            s "Just me."
        if met_bradley == "false":
            m "Hey Sissel?{p=.3}While you were staying at the cottage...{w=.3}did anything odd ever happen to you?"
            m "Like um....{w=.3}ghosts and such?"
            "Sissel scoffed at me in disbelief."
            s "Geez [charname],{w=.3} you've been listening to too much gossip."
            s "What,{w=.3} did you hear about that bullshit ghost story about the \"Black Lady of Bradley Lake\" or whatever it's called?"
            m "The what?"
            s "Just an old local legend people use to scare little kids away from the woods at night."
            s "Something about a singing dead lady looking for her child.{p=.3}Which is ridiculous to even think about."
            m "\"Singing.....?\""
            s "Eh don't worry about it,{w=.3} I lived there for {i}years{/i}.{p=.3}There was never anything particularly weird, {w=.3}and no people in general."
            s "Just me."
        s "There were some really pretty fireflies here at night though."
        s "Maybe I could show you sometime~"
        m "Heh,{w=.3} that sounds lovely."
        
        play music "easy-lemon.mp3" fadein 3
        scene cottage with Dissolve(4.0)
        
        "As the two of us continued our long walk, {w=.3}we found ourselves at the cottage in question."
        "Sissel stared at the broken-down building for several long minutes,{w=.3} looking rather nostalgic."
        
        s "You know....{w=.3}now that you brought up that ghostly shit,{w=.3} it kind of reminds me of something."
        m "What is it?"
        "My mind was still wandering after our conversation earlier."
        "Was that black-haired lady I met a few days ago really a wish?{p=.3} If that were true,{w=.3} someone would have had to wish for her."
        "She looked powerful,{w=.3} but so ragged and worn....{p=.5}Something odd happened here, I'm sure of it."
        
        "I turned my attention back to Sissel, {w=.3}who was scratching his head thoughtfully."
        s "The first time I ever came to this cottage was on this rainy day......"
        
        show black with Dissolve(2.0)
        play music "raining.mp3" 
        show small sissel with Dissolve(4.0)
        hide black
        
        s "It was a few days after I ran away from West Orphanage. {w=.3}Things were pretty rough."
        s "I hadn't eaten in days and I had nowhere to go.{p=.3}Everyone I ran into treated me like a street rat and chased me away."
        s "Honestly....{w=.3}I really felt like giving up then and there..."
        
        show sissel forest with Dissolve(3.0)
        hide small sissel
        
        s "So there I was.{p=.3}A little toddler all alone in the woods in the middle of pouring rain."
        s "There wasn't much hope for me.............."
        s "I don't remember what happened afterwards clearly but-"
        
        play music "little-dark.mp3" fadein 3
        show sissel forest 2 with Dissolve(4.0)
        s "I remember there was a woman holding an umbrella."
        s "I didn't even notice her at first. {w=.3}She just stood there next to me without saying anything."
        s "After a while, {w=.3}she sort of motioned me to follow her and eventually{w=.3} she led me to the abandoned cottage."
        
        s "The place was old, {w=.3}but there was a lived-in feeling to it."
        s "There were old dry towels, and even some canned food that managed to keep me going for a while."
        s "I never saw her again but if it weren't for that lady, {w=.5}I probably would have frozen or starved to death."
        
        hide sissel forest 2 with Dissolve(3.0)
        
        show sissel neutral with dissolve
        s "You know,{w=.3} for some reason I can't even vaguely remember what she looked like."
        s "I wonder how she's doing now..."
        
        "Sissel stared at the cottage for a few more moments before chuckling to himself softly."
        m "What is it?"
        show sissel happy with dissolve
        s "I'm still kinda in shock."
        s "Just a few years ago I was living in a broken down shack and starving to death. {w=.5}Now I'm going to school and making a living for myself."
        s "Time really flies, {w=.3}doesn't it?"
        
        "He turns to me with a slight smile on his face before throwing a friendly punch at my shoulder."
        show sissel neutral with dissolve
        s "I've never really told anybody about this before."
        s "Thanks for listening [charname], {w=.3}it means a lot to me."
        
        m "Anytime Sissel."
        "It warmed my heart to see him like this. {p=.3}Is this what it felt like to be trusted?"
        "..........................."
        stop music 
        "I blinked at him oddly for a moment,{w=.3} a strange thought nagged at the back of my mind."
        m "......Hey Sissel?{p=.3}Mind of I ask you something?"
        s "What is it?"
        m "I don't mean any offense when I say this but.....{w=.3}you've been {i}really{/i} nice to me since we've met."
        m "Not that it's a bad thing,{w=.3} I really appreciate it! {p=.3}But...{w=.3} it feels a bit unusual."
        if steal_wallet == "true":
            m "Especially since I stole your wallet the first time we've met."
        m "It's just,{w=.3} why do you trust me so much even though we just met a week ago?"
        
        s "Heh, {w=.3}is it really hard to believe that you're a nice person?"
        "Sissel looked at me thoughtfully.{p=.5}I could feel his eyes scrutinize me for almost a full minute before he spoke."
        play music "grateful.mp3" fadein 3
        s "You know, {w=.3}now that you've mentioned it,{w=.3} you {i}do{/i} remind me of someone I know."
        m "Someone you know?"
        s "Yeah,{w=.3} a friend of mine. {p=.3}Well, more like a mentor actually."
        s "You two look kind of alike.{p=.3}You've got the same color eyes and a thing for photography."
        s "You're both goofy as fuck and good at lending an ear to people to need it."
        s "Wow you two are practically a spitting image of each other, {w=.3}why haven't I seen it before?"
        
        "A spitting image?"
        "Suddenly, {w=.3}I felt the camera I hung around my neck almost exhale warmth against my chest."
        "I held the camera in my hands, {w=.3}inspecting it carefully."
        "Was it just my own pulse,{w=.3} or did the camera have a heartbeat of its own?"
        

    
scene black with Dissolve(5.0)
play music "lullaby-guitar.mp3"
scene dorm night with Dissolve(3.0)

"Night was looming over the horizon,{w=.3} but I still had thoughts swimming wildly through my head."
"Like a feeling of dread that just won't go away."
"Is there something I'm missing? {w=.3}Echo said to enjoy my summer,{w=.3} but it's a bit hard to do that when everyone around me seems to be hiding something."
"Or was it all just in my head?"

play sound "beep.mp3"
stop music

"Hm?{p=.3}A text message?"
"I flipped through my phone idly. {w=.3}It's from a someone I  don't know. {w=.3}Maybe a wrong number?"

"???" "{i}Hey Gran? {w=.3}Don't get angry,{w=.3} but I'm outside Gerania Academy right now.{/i}"
"???" "{i}I know I'm not supposed to be outside, {w=.3}but I really wanted to check out the school!{/i}"
"???" "{i}The problem is.......{w=.3}um........{/i}"
"???" "{i}I'm kinda locked outside at the moment.{/i}"

play music "blue-feather.mp3"
"???" "{i}And there's this creepy guy following me around campus.{p=.3}I might be going crazy,{w=.3} but it looks like he doesn't have arms or a face.{/i}"
"My heart instantly jumped to my throat."
"No arms or a face? {w=.3}That sounds like the Remnant that I saw two days ago!"
"Why was it following this person specifically?{w=.3} Were they important in some way?"

play sound "beep.mp3"
"???" "{i}Whoops wrong number! {w=.3}Sorry that must have been awkward.{/i}"
m "{i}Hey I'm a student at Gerania. {w=.3}Do you want me to let you inside?{/i}"
m "{i}It's probably safer than staying out there with a stalker.{/i}"

"There was a long pause before the next text."
"???" "{i}That would be great actually, {w=.3}I'd love to stay alive. {w=.3}Thanks!{/i}"
"???" "{i}I'm sitting at the back entrance. {w=.3}Thanks a bunch, friend!{/i}"
m "{i}Well that's settled then.{p=.3}I'm on my way!{/i}"
"I jumped into my shoes and socks and glanced around the room."
m "Echo! {w=.3}Did you hear all that?"
"............................{w=.3}there was no answer."
m "Echo?"
"Looks like he isn't here. {w=.3}Where did he run off to?"

u "Useless wish,{w=.3} isn't he?"
m "W-what?"

play sound "ghost.mp3"
show halley neutral with Dissolve(2.0)
m "H-Halley?"
u "Hm,{w=.3} looks like I'll have to babysit you for tonight."
u "I can't let you run off and get yourself killed."

m "W-where's Echo? {w=.3}And why do you even care?"
u "How should I know where your wish is?{w=.3} I have better things to do."
u "He's probably off on what you mortals call,{w=.3} a \"lunch break.\""
m "It's night time right now."
"Halley shrugs dismissively."
u "As for your second question,{w=.3} of course I care."
u "I may loathe everything about you,{w=.3} but you're useless to me dead."
u "Now hurry up and let that person inside."
u "I'll make sure you don't suffer lethal damage along the way."

m "Eh......{w=.3}thanks?"
"Whatever.{p=.3}I better go get that person inside and away from the Remnant."
"It's probably safer to have Halley with me than to go alone."


scene black with Dissolve(3.0)
scene school back night with Dissolve(3.0)

"The school feels a bit spookier at night.{w=.3} There was an odd chill in the summer air."
"Now,{w=.3} where was that person? {w=.3}I hope the Remnant hasn't caught up to them."

m "Hello? {w=.3}Are you out there-"
stop music
play sound "slam.wav"
m "-OOOOPH!"

"Something suddenly slapped across my face,{w=.3} sending me reeling to the ground. {w=.3}What the hell?!"

"???" "Oh my gosh I'm sorry!{w=.3} I thought you were the stalker."
"???" "Are you alright?"
m "I'm fine.{w=.3} You could have given some warning before backhanding me though..."
"???" "Eheh, sorry about that. {w=.3}It's a bit scary out here at night."
"???" "Here, {w=.3}let me help you up."

m "Thanks-"

"I looked up and instantly froze."

play music "grateful.mp3" fadein 2
show encouter 1 with Dissolve(4.0)
pause(1.0)

m "Y-you?"
"???" "......{w=.3}huh? {p=.3}Sorry, have we met before?"
"My heart was lurching painfully against my chest.{w=.3} Why were tears welling up in my eyes?"
"I don't even know this person..........{w=.3}but it almost feels like I've reunited with an old friend."
show encounter 2 with Dissolve(2.0)
pause (3.0)
"The cameras we wore around our necks suddenly kindled into a warm glow."
"Emotions welled up inside me and an overwhelming sense of regret enveloped my heart,{w=.3} almost like memories from another lifetime."

scene school back night with Dissolve(3.0)
play music "lullaby-guitar.mp3" fadein 5
show jinny neutral with Dissolve(2.0)

"???" "Hello?{w=.3} Helloooooo?"
"???" "Did I hit your head too hard?{w=.3} You're kinda zoning out."
m "Wha?{w=.3} S-sorry, I don't know what got over me."
"I rubbed my eyes and shook my head from my thoughts. {w=.3}I feel like a mess...."

"As I stumbled back onto my feet,{w=.3} the girl watched me like she was holding back a laugh."
"???" "So you're the guy who's supposed to be rescuing me? {w=.3}Eh, I thought you'd be taller."
"???" "Or maybe look a little more heroic."
m "Hey!{w=.3} Would you rather I left you outside?"

"???" "Hey don't get me wrong,{w=.3} I'm totally grateful!"
"???" "I just figured from your bold texts that you'd be a little more-"
"???" "Eh nevermind."
j "Anyway,{w=.3} the name's Jinny.{p=.3}It's a pleasure to not be killed by a stalker tonight."
m "I'm [charname]. {w=.3}Nice to meet you too I guess...."
j "Oh hey! {w=.3}That's a nice camera!"
"Jinny pointed at the camera hanging from my neck gleefully."
j "I remember buying one just like it forever ago!{w=.3} Are you into photography?"
m "Sort of? {w=.3}I kinda just picked Photography at Gerania Academy for an easy grade."
j "That's no way to live.{w=.3} You should try and enjoy it more,{w=.3} especially if you're attending a prestigious school like Gerania."
j "Take tons of photos!{w=.3} Capture every important moment!{w=.3} Life is too short to just let time slip by."
j "Photographs, after all, {w=.3}are just little pieces of time."

"\"Little pieces of time?\" {p=.3}I swear I've heard that somewhere before."
m "Hm?{w=.3} That reminds me,{w=.3} why are you sneaking onto campus this late at night?"
m "People usually try and sneak {i}away{/i} from school."
m "You could just come here during visitor hours or something...?"
"Jinny gave a mournful sigh and stared up at Gerania Academy's many buildings."
j "You know,{w=.3} I've always wanted to come to school here.{p=.3}But I can't."
j "I'm sorta kinda under house arrest?"
j "Well,{w=.3} not actual house arrest but I'm not allowed to roam around willy nilly."

m "And so you decided to sneak out and go to a school of all places."
j "Hey! {w=.3}Some people aren't lucky like you. {w=.3}I've never even been in an actual classroom before."
j "By the way,{w=.3} what's it like studying here?"
j "You know,{w=.3} besides the crazy armless stalkers that follow you at night?"

m "Well.......{w=.3}there's tranquilizer-wielding teachers with chins that look like shapely ballsacks."
m "Then there are the cute bunnies  and vandal classmates riding skateboards.{w=.3} Besides that,{w=.3} classes are pretty boring."
j "Oh that sounds wonderful!{w=.3} I can't wait to sneak here more often!"
hide jinny with Dissolve(2.0)
"Jinny was absolutely giddy as she skipped around the parking lot,{w=.3} taking in every detail around her."
"What an odd girl..."
stop music
play sound "ghost.mp3"
play music "asphodel.mp3" fadein 3
show halley neutral with Dissolve(3.0)
u "...........s-{w=.3}she's here."
m "-Whoa! {w=.3}Give me some warning before you pop up like that!"

play music "asphodel.mp3" fadein 3
"Halley ignored me, {w=.3}her eyes trained onto Jinny."
"She was staring at her,{w=.3} barely breathing.{w=.3} Her eyes were wide with what looked like terrified hope."
"Halley reaches out to Jinny,{w=.3} hands shaking violently as if the world would collapse around her at any moment."
m "Halley?{w=.3} What are you-"
u "......c-can she.................{w=.3}can she see me-?"
play sound "ghost.mp3"
show halley terrified with dissolve

stop music
u "-!!!!!!!!!!!"

"Jinny suddenly walked right though Halley as though she was made of smoke,{w=.3} not even noticing she was there."
"Halley fell to her knees, {w=.3}choking through a shocked sob."
"I quickly scrambled to her side."
m "Halley!{w=.3} Are you alright?!"
u "........................................."
show halley neutral with dissolve
u "...............no,{w=.3} I'm not."
"Halley forced herself to take a deep breath before stumbling back onto her feet."
u "Nevermind me.{w=.3} You two should get indoors before your faceless friend finds us-"

hide halley

play sound "wail.wav"
play music "hitman.mp3"
pause(1.5)

"Everyone froze as an eerie laughter echoed through the night."
show jinny neutral with dissolve
j "[charname]!{p=.3}Look over there!"
hide jinny with dissolve
"There was an unsettling shadow teetering across the parking lot,{w=.3} its jointless legs spasming with each stride."
"Even its movements felt unnatural and inhumane."

show jinny neutral with dissolve
j "T-that's the thing that's been following me!"
m "Wait,{w=.3} you can see it too?"
hide jinny with dissolve
"But she can't see Halley for some reason....."
u "Oi coward. {w=.3}Is this really the time to be pondering things?"
m "R-right! {w=.3}We better head inside!"
m "Jinny follow me!"

"I grabbed the door handle,{w=.3} but it wouldn't budge an inch."
"Was it locked?!"
"No,{w=.3} it feels as though it's unnaturally sealed shut."

play sound "wail.wav"
show remnant smile with Dissolve(3.0)

"The Remnant approached closer,{w=.3} its maniacal grin coming into view."
"The air felt heavy and charged."
"Suddenly, my knees gave out and I fell to the floor."
"My heart was hammering against my chest. {w=.3}I felt so tired, as if every inch of my body were weighed down by lead."
j "[charname]!{w=.3} You alright?!"

"H-huh?{w=.3} Jinny seemed completely unaffected,{w=.3} looking down at me with concern."

rr ".......................{w=.3}found.........................{w=.3}you..................."
j "Looks like I'm not crazy.{w=.3} You're actually missing a face."
m "Jinny,{w=.3} stay away from it!{w=.3} It's dangerous-!"

play sound "glitch.wav"
show remnant smile violet with Dissolve(2.0)


"The Remnant suddenly roars,{w=.3} one of its countless eyes snapping open."
"Its one open eye zeroes onto Jinny,{w=.3} jittering in a mad dance against its socket."

j "..................{w=.3}.....Well,{w=.3} this is quite the {i}eye-opener.{/i}"
"In spite of the situation,{w=.3} I couldn't help but groan."
m "Please no,{w=.3} one punny friend is enough."
j "Hehe sorry,{w=.3} I couldn't resist."

rr ".............yOuR mEmoRieS lAY sCAttEred...................."
rr ".............................cAn'T rEMemBer???.......{w=.3}...............yOuR oTHer lIFetIMEs?????"
rr "..........pITY."

j "Oooooh,{w=.3} so it's armless,{w=.3} faceless,{w=.3} {i}and{/i} crazy."
m "W-what do you want from us?"

play sound "glitch.wav"

rr "..............tHE fiRsT tIme yOu cAMe heRE [charname].............{w=.3}i fInaLLy gRAnTeD yOUR wISh.............."
rr ".....................i fInALLy gAvE yOU wHAt yOu wANteD..................."
play sound "glitch.wav"

rr "..............teLL mE giRL,{w=.3} wHY dId yOu iNterFere?????"
rr ".............................aNd {b}[charname]{/b},{w=.3} wHY dID yOu rETurN tO tHE bEgiNninG????????"


hide remnant with dissolve

show jinny neutral with dissolve

j "..........so,{w=.3} do you have any idea what it's talking about?"
m "I can barely understand what it's saying,{w=.3} let alone what it means."
j "It looks like it knows your name though.{w=.3} Are you two friends?"
m "Hell no!{p=.3}I want nothing to do with it."

hide jinny with dissolve

play sound "ghost.mp3"
show halley neutral with Dissolve(2.0)

u "That's enough talk.{w=.3} I'm putting an end to this."

hide halley with dissolve

play sound "wail.wav" 
show remnant smile violet with Dissolve(2.0)

rr "..................oH thE liNGeRinG cOMet stILL lIVes.........."
rr ".......................aRE yoU sTiLL tRYing tO sAVe thEM?????{w=.3} tRY aLL yOu lIKe.............."
play sound "rosies.mp3" fadein 3
rr ".................yOU aRe tHE bLAcK dEAth,{w=.3} yOu cANnot bRinG anYthiNG bUT miSforTUne."
pause(1.5)
rr "......................dO yOu heAr thEM-??????????"


hide remnant 


show halley terrified with dissolve

u "......shut up...{p=.4}{size=+10}-SHUT UP!!!!"
play sound "halley-wish.mp3"
show halley wish with dissolve

"Halley's eyes flared."


scene white with Dissolve(0.6)
stop music

"Suddenly, {w=.3} every electrical fixure in the city seemed to glare with blinding light."
"It was abruptly as bright as day,{w=.3} with lights shining from every streetlamp,{w=.3} every building."
"Jinny and I had to cover our eyes to stop ourselves from going blind."

play sound "glitch.wav"
"The Remnant was shrieking with earsplitting pain,{w=.3} its cries echoing through the night."
"................................"

scene school back night with Dissolve(4.0)
pause(2.0)

"Soon,{w=.3} the light subsided and the Remnant was gone,{w=.3} leaving us alone in the night."
"It looks like it doesn't handle bright light too well.{w=.3} Maybe that's why it wasn't moving when I saw it in plain daylight?"
#halley sad
show halley neutral with dissolve
"Halley was knelt over on the ground,{w=.3} burying her furious face in her hands."
"Her breathing was reduced to ragged gasps."

m "...........Halley,{w=.3} are you-?"
u "You.{w=.3} Take Jinny and bring her inside."
u "I've unsealed the door."
m "But-"
u "{i}{b}Leave.{/b}{/i}"

m ".....................O-okay.{p=.3}We'll leave."


scene school lobby with Dissolve(4.0)

"The lights were still on in the lobby. {w=.3}That's a relief."
show jinny neutral with dissolve
j "So,{w=.3} is this type of thing normal around here?"
m "Oh yes,{w=.3} it's totally normal to have ghosts and spirity shit haunt us around here.{w=.3} It's a time-honored tradition."
j "I'll take that as a no."
m "Do you even believe in ghosts?"
j "......{w=.3}no, I don't really."
j "Dying should be short and sweet,{w=.3} not drawn out like floaty spirits.{w=.3} That can't be very comfortable."

play sound "slam.wav"

"We suddenly jump as footsteps came scrambling our way."
j "-shit it's her.{p=.3}Hide me!"
m "What-?"
hide jinny with dissolve
"Jinny lunges behind a counter as the footsteps draw closer."
"The footsteps turn into deafening thumps as Mrs. Corlisse barrels around the corner with the fury of a charging rhinosaurus."


play sound "slam.wav"
pause(.3)
c "[charname]."
m "H-h-hey Mrs. Corlisse!{w=.3} How are you doing?"
c "It is one o'clock in the morning [charname]. {p=.3}Why. Are. You. Out. Of. Bed?"
m "I-I-I-!!{p=.3} Well you see.....??"
m "Wait a second, {w=.3}are you wearing a bathrobe?"
play music "batty.mp3"
"Now that she's up close,{w=.3} it looks like Mrs. Corlisse scrambled out of bed just moments ago."
"Her bright yellow crocs gleamed against the floor as her haircurls quivered dangerously from her still wet hair."
m "........{w=.3}this image is going to be burned into my mind,{w=.3} isn't it?"
c "Instead of questioning my fashion sense, {w=.3}I suggest you explain why you are wandering around campus at the dead of night?"
m "Well you see, {w=.3}this faceless ghost was attacking this poor passersby and I did my duty as a protagonist to rescue the poor thing-"
c "Oh [charname], {w=.3}if only you showed this kind of creativity in my classroom."
"O-ouch."


c "It'd be nice if you had just told the truth."
c "I was once young, too. {w=.3}I know how you youngsters often sneak out to meet up with whatever boyfriend or girlfriend you have hidden away-"
m "N-no no no!{w=.3} It's nothing like that!!"
c "-Just remember that protection is a must.{w=.3} STDs are a real problem and not something that just happens to \"someone else.\""
c "I believe Mr. Rokov has pamphlets with diagrams in his office-"
m "Mrs. Corlisse I promise you that I'm not sneaking out to sleep with-"
c "-Also remember that \"love at first sight\" is a lie.{w=.3} Romeo and Juliet claimed to have it and they {b}died three days later{/b}."
"I buried my reddening face into my hands."
play music "wacky.mp3" fadein 3
m "Yes, {w=.3}yes,{w=.3} I'll take your advice to heart Mrs. Corlisse."
c "Excellent.{w=.3} Now hurry off to bed and {i}do not get caught again.{/i}"
c "I will not be so lenient next time."

"With a huff, {w=.3}Mrs. Corlisse turned and walked off,{w=.3} leaving me alone with my embarrassment."
"Well, almost."
show jinny neutral with Dissolve(2.0)
play music "cafe-music.mp3"
j "That was rather educational."
"I only groaned,{w=.3} face still buried."
j "Was that your first time getting \"the talk?\"{w=.3} Your face was priceless!"
m "Ugh,{w=.3} my parents never cared.{w=.3} I thought I'd be free from this experience."
j "It's a rite of passage.{w=.3} You can't escape it."
j "Anyway,{w=.3} thank you for letting me into the school!"
j "I think I'll stick around and explore the place a bit."
m "You'd still stick around even after a ghost attacked you?"
j "Hey! {w=.3}You can't live life without a bit of adventure.{w=.3} I'd ask you to be my tour guide,{w=.3} but I don't want you to get into any more trouble."

j "Well,{w=.3} I'll see you around.{w=.3} Have a good night [charname]!"

hide jinny with Dissolve(3.0)


"And so Jinny waltzed off and disappeared down the hall."
"I sighed and ran my fingers tiredly through my hair."
"It's been one hell of a night.{w=.3} Why do I let myself get dragged into these kinds of things?"

play music "asphodel.mp3"
m "Huh?"
"I reached up and clutched the camera hanging against my chest."
"It felt.........{w=.3}warm."
"Was I just feeling my own pulse against my palms,{w=.3} or did the camera have its own heartbeat?"
"No......{w=.3}something has definitely changed."

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



jump day7_morning
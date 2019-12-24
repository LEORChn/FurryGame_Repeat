label day3_activities:
scene lake with Dissolve(3.0)
"That kayaking experience was a shipwreck waiting to happen, {w=.3}but I'm glad things worked out in the end."
"Mrs. Corlisse allowed everyone a quick break before announcing that the second session of activities was about to begin."
m "More activities already?"

show sissel shirtless at center with dissolve

s "Please,{w=.3} no more.{p=.3}I can't afford the therapy I'd need to recover from this shit."
s "What's the point of doing all this anyway?!{p=.3}What does this even have to do with school?!"
"Mrs. Corlisse gave Sissel a sad nod and patted him on the shoulder."
c "I completely agree with you,{w=.3} Mr. Sissel. {p=.3}Your time is much better spent in the classroom."
c "Unfortunately the schoolboard deemed that group activities like this would help the student body get along."
show phillip shorts at farleft with dissolve
p "I'm pretty sure half the kayaking teams tried to kill each other."
"Mrs. Corlisse actually snorted in amusement."
c "I never said the schoolboard was right."
c "I don't make the rules though,{w=.3} so  everyone will have to play along in these mandatory fun sessions whether they like it or not."
p "\"Mandatory fun....?\""
show owen shorts grin closed at farright with dissolve
o "Well we might as well make the most of it! {p=.3}We could all use some fresh air anyway."
p "It's not like we don't have air indoors...."
show owen shorts with dissolve
o "Anyway, what other activities do you have planned for us?"
"Mrs. Corlisse dug through her clipboard with a sigh."
c "It seems like you folks have the option to either go for a swim, {w=.3}or play several rounds of volleyball."
c "I'm sure you'll find both activities to be equally beneficial to your education."
"Her voice was dripping with heavy sarcasm. {p=.3}I guess the great outdoors isn't exactly her thing.{w=.3} At least we have something in common."
"Welp,{w=.3} time to decide what to do with the rest of our time:"

menu:
    "Play Volleyball.":
        m "I'm not exactly a sports guy,{w=.3} but a few rounds of volleyball sounds simple enough."
        m "Plus Sissel looks like he's going die if he gets wet again."
        "Sissel beamed at me like I just told him Christmas came early."
        "I yelped as he swings an arm over my shoulders into a grateful half-hug. {w=.3}I guess he was too tired to full-hugs."
        s "[charname],{w=.3} you are a true life-saver."
        m "Pffft if you say so."
        
        scene black with Dissolve(3.0)
        play music "calm-guitar.mp3" fadein 3
        scene lake with Dissolve(2.0)
        
        "We made our way towards the volleyball net, which was situated in a particularly sandy area alongside the lake."
        "Owen jumps into the sand with his usual bombastic excitement."
        
        show owen shorts at left 
        show phillip shorts at right 
        
        o "Alright let's get this show on the road! {w=.3}I say we make this a 2v2 game."
        p "Great, I'll team-"
        "Owen suddenly pulls Phillip close to his chest with a wink."
        o "I call being on Phillip's team!"
        p "{w=.5}....yay."
        
        
        hide owen with dissolve
        hide phillip with dissolve
        
        show sissel shirtless with dissolve
        
        s "Looks like we'll be teaming up again. {p=.3}You ready for this?"
        m "Absolutely not. {w=.3}Does it look like I'm a sports kind of guy?"
        s "C'mon [charname],{w=.3} show a little more spunk! {w=.3}We can't just let Owen win!"
        
        "Sissel's eyes were shining with competitive determination as he pointed a daring finger at Owen,{w=.3} who the other side of the volleyball net."
        s "Don't expect us to go easy on you!"
        m "Don't expect me to do anything useful...."
        
        s "Hey don't sweat it [charname]! {w=.3}You might be useless at sports but I'll pick up the slack!"
        m "....thanks?"
        m "At least Phillip doesn't look too athletic either. {w=.3}We might actually stand a chance."
        
        hide sissel with dissolve
        show phillip shorts with dissolve
        
        p "Heh,{w=.3} if you want to think that way then go ahead."
        show phillip shorts at Position(xpos = .5, xanchor=.5, ypos=.6, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
        p "I'll be showing you no mercy~"
        show phillip shorts at center with dissolve:
            xzoom 1 yzoom 1
        
        "Gulp.{p}L-looks like Phillip's got a competitive side too."
        "It's kinda hard to be intimidated by the shortest guy around though..."
        
        hide phillip with dissolve
            
        
        
        "Welp, {w=.3}looks like I'll be serving the ball first.{p=.5}Here goes nothing."  
        "I toss the ball straight into the air with perfect form as I leapt up and....{w=.5}{size=+10}PAH!!{/size}"
        stop music
        "The ball spikes straight into the net."
        play music "wacky.mp3" fadein 2
        "Everyone" "................................"
        "Everyone's pitiful stares speared me through the heart.{p=.3}I drop to my knees and hang my head in shame."
        
        show sissel shirtless with dissolve
        "Sissel pats my head awkwardly."
        s "That was a shit serve, man."
        m "Aren't you supposed to be comforting me?!"
        s "Sugarcoating it ain't going to fix your bad aim [charname]."
        
        "O-ow,{w=.3} such brutal honesty."
        
        "Owen laughs from the other side of the net as he tosses the ball into the air. {w=.3}Was he serving now? {w=.3}How does volleyball even work?"
        o "Better luck next time kiddo!"
        "He hit the ball with a resounding {i}BANG!{/i}"
        hide sissel
        play sound "slam.wav"
        s "-!!!!?"
        "Before I knew what was happening,{w=.3} the ball rockets across the court and smacks Sissel over the head."
        
        play music "in-your-arms.mp3" fadein 2
        show sissel shirtless embarrassed at Position(xpos = .5, xanchor=.5, ypos=.6, yanchor=.5) with Dissolve(2.0):
            xzoom 1.7 yzoom 1.7
            
        "The lights went out when he lands on top of me,{w=.5} accidentally straddling my hips as his face falls dangerously close to my own."
        "G-gulp.{p}I could feel his warm breath against my cheek."
        "If I just lean a {i}little{/i} bit closer-"
        
        show sissel shirtless at center with dissolve:
            xzoom 1 yzoom 1
            
        s "{i}Owen you jackass!{/i} {p=.3}Watch where you're hitting that thing!"    
        "Sissel immediately sits up and away from my face.{p=.3}A small whine of disappointment grumbles from my throat, {w=.3}but thankfully he didn't seem to notice."
        
        "As he continued to spew colorful language towards the other side of the net,{w=.5} I shiver as I feel Sissel accidentally grind against my crotch."
        s "Hm?{w=.3} You alright there [charname]-{p=.3}-!!!???!?"
        show sissel shirtless embarrassed with dissolve
        "Whoops,{w=.3} I guess I accidentally began grinding back."
        "Both our faces were equally beet red as we scrambled back onto our feet,{w=.3} totally avoiding each other's eyes."
        s "Ahem......{w=.3}um.....{w=.3}you alright [charname]?"
        m "{size=+15}I'M FINE!{/size}"
        "My voice was an octave higher than I intended."
        
        scene black with Dissolve(2.0)
        play music "batty.mp3" fadein 3
        scene lake with Dissolve(3.0)
        
        "As the volleyball match went on,{w=.3} Sissel and I found ourselves in a frequent tangle of limbs."
        "I swear Owen was doing this on purpose."
        "For the last twenty minutes, {w=.3}every time Owen hit the ball it somehow knocked the two of us into enough intimate positions to fill a kamasutra."
        ".....{w=3}or maybe it's because I'm a sore loser and we're losing the game 2 - 15."
        "It's so unfair though! Owen hits the ball so hard it's difficult to follow where it's flying to next."
        "And Phillip. {p}He didn't hit very hard but he was fucking {i}fast{/i}."
        
        show phillip shorts with dissolve
        p "Hey [charname]! {w=.3}Sissel!{p=.3}Are you two doing ok?"
        p "You're looking really red."
        hide phillip with dissolve
        
        
        m "W-we're fine!{p=.3}I-It's just really hot out today!"
        show sissel shirtless embarrassed with dissolve
        s "Y-yeah!{w=.3} J-j-just the weather!"
        
        "We're a total mess.{p=.3}Our faces were glowing like overripe tomatoes,{w=.3} not to mention the large tents growing in both of our shorts."
        "Sissel either hasn't noticed me staring, {w=.3}or was ignoring it.{p=.3}Either way, I'm thankful."
        
        hide sissel with dissolve
        
        p "Um,{w=.3} if you say so."
        p "I'll go ahead and serve the ball then."
        
        "I finally pull my eyes away from Sissel's neither region to focus back on the game."
        "The ball was soaring over the net."
        m "I got it!"
        "And I actually did it!{p=.3}With an awkward swing, I smack the volleyball all the way to the opposite corner of the court."
        "There was a blur.{p=.3}Phillip shot across the sand like a missile and saved it at the very last moment."
        "Owen's got the ball now."
        "G-gulp."
        "He sends me a sly wink before spiking the ball towards me."
        
        play sound "slam.wav"
        stop music 
        "{size=+20}SMACK!!!{/size}"
        
        "......................................."
        "I caught the ball.{p}With my face."
        "I instantly wheeled around and there was a soft \"oof!\" as I knocked Sissel over along with me."
        
        "My face lands on something warm and hard."
        play music "in-your-arms.mp3" fadein 6
        "A wiff of musk suddenly fills my nostrils and I couldn't help but inhale the sweet scent deeply."
        "The thing pulses with warmth as I involunarily rubbed against it with my cheek."
        
        show sissel shirtless embarrassed at Position(xpos = .5, xanchor=.5, ypos=.6, yanchor=.5) with dissolve:
            xzoom 1.7 yzoom 1.7
        s "[charname]! {p=.3}G-get off!"
        "Oh I landed on Sissel's crotch. {p}What a tragedy."
        
        hide sissel with dissolve
        "As I climb off of Sissel,{w=.3} Owen and Phillip came prancing over with victorious grins on their faces."
        
        show owen shorts grin closed at farleft with dissolve
        show phillip shorts at farright with dissolve
        o "Aaaaand that's the match!{w=.3} It's a shame you guys lost,{w=.3} but hey!"
        show owen shorts grin with dissolve
        o "It looked like you two were having fun anyway~"
        
        "He gave us another wink.{p}That bastard."
        play music "calm-guitar.mp3" fadein 5
        
        "Phillip glances over at Sissel with concern."
        
        p "Whoa Sissel,{w=.3} your fur is a mess."
        "That was an understatement."
        show sissel shirtless at center with dissolve:
            xzoom 1 yzoom 1
        "Sissel's fur was already wet from the kayaking fiasco earlier,{w=.3} but now it was caked in thick layers of sand."
        "He practically looked like an angry sand sculpture."
        
        s "Ugh,{w=.3}I'll be fine."
        s "I think there's a public shower thing around here. {p=.3}I'll go try and wash all this off."
        hide sissel with dissolve

        "Sissel stomps away and disappears into the forest trail. {p=.3}I stared after him,{w=.3} my head still spinning from our intimate collisions earlier."
        "I wonder if I should...."
        
        menu:
            "Go join Sissel in the shower and have some fun~.":
                p "Eh,{w=.3} that's gotta be pretty uncomfortable."
                p "Rabbit fur is really thick and isn't supposed to get wet in the first place.{w=.3} It must be a whole lot worse with sand matted into it."
                
                
                m "You think he needs help?"
                p "Well-"
                show owen shorts grin closed with dissolve
                o "He probably doesn't,{w=.5} but he'd probably appreciate a \"helping hand~\""
                m "W-wah?"
                o "C'mon [charname],{w=.3} I know you wanna go after him! {p=.3}Just tell him you wanna help wash his back~"
                m "M-me? {p=.3}I......er......"
                "I glance over at the shower cabin.{p=.3}This could be a once-in-a-lifetime opportunity."
                "I gulped again."
                m "I-I-I'm going to shower off too! S-see you guys in a bit!"
                
                "As I leave the volleyball area,{w=.3} I could hear Owen and Phillip whispering behind me."
                show owen shorts with dissolve
                o "Heh,{w=.3} our little [charname] is growing up~"
                p "\"Grow up\" huh?{p=.3}You could learn a thing or two from him Owen."
                o "O-ouch..."
                
                stop music
                scene lake shower with Dissolve(4.0)
                
                "The lake \"showers\" was just a tiny wooden stall with running water inside." 
                "The small shack didn't exactly scream privacy."
                "I could see Sissel's feet under the stall walls as he tries to wash all the sand out of his fur."
                
                play music "heartbeat.mp3" fadein 4
                "My heart was beating rapidly against my chest as I cautiously stepped into the stall."
                "The water was already running. {p=.3}Sissel had his back towards me and didn't seem to notice me.{p=.3}My breath caught in my throat at the sight of his sleek, naked body."
                "Was I really going to do this?"
                
                "With a deep breath,{w=.3} I slid off my shorts and stepped closer to him."
                
                show sissel naked with Dissolve(2.0)
                s "Hm-?"
                m "H-hey Sissel!"
                stop music
                hide sissel
                play music "groove.mp3" fadein 3
                s "{size=+40}AAAAAAAAAAAAHHHHHHHHHHHHHHH{/size}"
                show sissel naked embarrassed with dissolve
                
                s "[charname]?! {p=.3}What the fuck are you doing in here?!"
                
                "I could feel his eyes trail down my bare body.{p=.3}His face was growing redder by the minute."
                "Heh I can't blame him though, {w=.3}I was getting quite the eyefull myself. {p=.3}Sissel was pretty well-hung."
                m "W-well I figured you'd need some help washing off that fur of yours."
                show sissel naked with dissolve
                s "So you just waltz in here without knocking? {w=.3}Twat."
                m "If it makes you uncomfortable, I can leave-"
                s "Uh-{p=.3}No, stay."
                show sissel naked embarrassed with dissolve
                s "I could use some help with my back.......{w=.5}if you want to."
                m "Heh, it'll be my pleasure~"
                
                hide sissel with dissolve
                "Sissel hesistantly turns around and exposes his back to me."
                "It was caked in sand from our various volleyball collissions."
                "Hesistantly,{w=.3} I ran my hands through the soft, velvety fur and massaged my fingers against the warm skin underneath."
                "I could feel Sissel shivering as I began traveling lower down his back, {w=.3}one of my hands resting not-so-subtly on his hips."
                
                m "Whoa, {w=.3}your fur is {i}really{/i} soft."
                show sissel naked embarrassed with dissolve
                s "Is that what you're here for? {w=.3}To feel me up?"
                m "N-no! {p=.3}I'm here to help you out of the goodness of my heart!"
                s "Sure you did.{p=.3}You twat."
                hide sissel with dissolve
                
                
                "I pouted and massaged Sissel's muscles more aggressively,{w=.3} relishing every inch of contact."
                "He was letting out small moans and whimpers now.{p=.3}Heh, looks like I'm doing a good job."
                "Out of the corner of my eye,{w=.3} I saw something moving."
                "I glanced down Sissel's front and saw his large,{w=.3} uncut cock slowly hardening while Sissel had his eyes clamped shut, biting back moans."
                m "Heh, {w=.3}for someone who complained so much, you sure are enjoying it."
                s "S-shut up!"
                m "................hey Sissel.{p}Do you want me to....... give you a hand with that?"
                s "I-I-I.........{p=.5}S-sure, {w=.3}if you want to."
                
                show sissel_volleyball at Position(xpos = 1, xanchor=1, ypos= 1, yanchor=1) with Dissolve(2.0):
                    xzoom 1.5 yzoom 1.5
                show sissel_volleyball at Move((0.75, 0.75), (0.3, 0.5), 20,
                    xanchor="center", yanchor="center"):
                
                "I could feel my heart thumping as I grinded my hips against Sissel's backside, {w=.3}pressing our bodies together."
                "My hands slowly snaked down Sissel's chest,{w=.3} caressing his abs before sliding down to his long hardening cock."
                
                "Sissel whimpered as I softly gripped his dick, {w=.3}giving it some gentle strokes."
                s "Ah [charname].........."
                "I groaned at the sound of my name and buried my face into the back of his neck.{w=.3} He smelled so nice."
                
                "My grip tightened as I began stroking in earnest, {w=.3} rubbing a finger across his tip whenever his foreskin pulled back."
                "Sissel was moaning loudly with no restraint,{w=.3} grinding back at my hips in rhythm of my stroking."
                
                show sissel_volleyball at center with Dissolve(2.0):
                    xzoom 1 yzoom 1
                
                pause(2.0)
                    
                s "Ah.......{w=.3}[charname]..........."
                s "I'm getting close............"
                
                m "Mmmph..."
                
                "I moaned against his shoulder and began pumping his meat harder,{w=.3} my own hips humping against Sissel's as I relished the warm friction between us."
                
                "My own dick was rubbing feverishly against Sissel's butt cheeks,{w=.3} the whole lewdness of the situation quickly driving me close to the edge."
                m "Aah Sissel.......{w=.3}I'm gonna......"
                
                "Sissel whimpered in reply."
                "Abruptly,{w=.3} his dick pulsed against my fingers as squirts upon squirts of hot cum erupted from his tip and soaked down my hands."
                "I groaned and gave one last hump,{w=.3} my cock dripping warm seed down Sissel's inner thighs."
                
                stop music 
                hide sissel_volleyball with Dissolve(3.0)
                
                "Haah......haah......."
                "Both of us were panting as we slowly tried to catch our breaths."
                
                show sissel naked embarrassed with dissolve
                s "Ha.....ha......."
                s "That was................{w=.3}nice."
                m "Heh,{w=.3} we should do that again sometime~"
                s "[charname]............{w=.3}you shameless pervert."
                m "Heh, {w=.3} we better get cleaned up now. {p=.3}We've made a pretty big mess."
                "Sissel suddenly squealed as I gave his softening cock another squeeze."
                m "Hehe, sorry.{p=.3}I couldn't resist."
            "Try and make things less awkward.":
                m "That was probably the most awkward twenty-minutes of my life."
                o "Aw,{w=.3} c'mon man, I know you enjoyed it."
                m "No seriously Owen,{w=.3} what the hell were you thinking?"
                show owen shorts with dissolve
                "Owen looked taken aback and scratched his head in dismay."
                o "Geez it was just a joke.{w=.3}I figured I'd make things more interesting."
                o "I'm pretty sure Sissel's got a little crush on you,{w=.3} I was just trying to help things along! {w=.3}Nothing wrong with that~"
                
                p "It's called {i}tact{/i},{w=.3} Owen. {p=.3}You should learn it sometime."
                
                o "O-ouch."
                o "A-alright, {w=.3} I guess I did go a little overboard back there. {w=.3}Sorry about that."
                
                "I sigh and rub my eyes tiredly."
                m "It's fine,{w=.3} I just hope Sissel's not too upset with me."
                o "Oh our little cottontail's probably fine! {w=.3}Sissel been through way worse before~"
                o "He's not mad or anything. {w=.3}He's just being his usual annoyed self."
                
                m "I hope so."
                m "I'm going to try and patch things up before it gets too awkward between us though."
                "I turned to trek my way towards the shower stalls."
                p "Good luck [charname]!"
                
                
                play music "lullaby-guitar.mp3" fadein 4
                scene lake shower with Dissolve(4.0)

                
                show sissel shirtless with dissolve
                "After a long walk (aimless wandering for half an hour),{w=.3} I stumbled onto Sissel in front of the shower stalls."
                "He was trying to dry himself with a hairbrush and battery-powered hairdryer, {w=.3} but didn't seem to have much luck."
                m "Hey Sissel,{w=.3} how's it going?"
                show sissel shirtless embarrassed with dissolve
                s "Oh [charname]."
                show sissel shirtless with dissolve
                s "I could be doing better.{w=.3} My fur's going to take forever to dry out. {w=.3}Ugh, I can still feel sand in some spots."
                m "That's weird. {w=.3}It usually only takes a few minutes for my fur to dry out after a shower."
                
                s "It's different for rabbits."
                s "Our undercoat is ridiculously thick and traps water like a sponge."
                s "Not to mention how it basically sucks the warmth out of my skin when it's damp."
                "I could help but chuckled slightly at the sudden mental image."
                m "It must be a really fluffy and soft coat~"
                
                s "Oh har har,{w=.3} let's all laugh at my misery."
                
                "Sissel rolls his eyes and goes back to drying his fur,{w=.3} albeit with little success."
                "He seems to be having trouble reaching his back."
                
                m "Uh,{w=.3} do you need any help with that?"
                show sissel shirtless embarrassed with dissolve
                s "Huh?{w=.3} W-well, I guess..."
                s "Could you get the sandy spots on my back?"
                "I armed myself with the brush and hairdryer."
                "I gently began smoothing out the sand deep inside Sissel's undercoat while blowing it dry."
                m "Wow,{w=.3} it's like brushing a warm and fluffy cloud."
                s "Oh shut up."
                "Sissel's face was flushed slightly,{w=.3} but he relaxed and leaned into my brushing."
                "This was surprisingly intimate...."
                
                "A stray though struck me as I made my way down Sissel's back."
                m "Say, {w=.3}where did you get the brush and hairdryer?"
                m "You couldn't even afford your own meals a few days ago-"
                show sissel shirtless with dissolve
                s "What are you trying to say? {w=.3}I didn't steal it!"
                "I flinched at the sudden snap of anger."
                m "S-sorry! {w=.3}I didn't mean it like that,{w=.3} I was just curious."
                s ".................."
                "Sissel sighed and relaxed a bit."
                s "Sorry for snapping,{w=.3} it's just that most people assume....{w=.3}nevermind."
                s "My mentor's the one who gave me the brush and dryer."
                "There was a small pause and Sissel's face edged into a small grin."
                
                s "{i}She's{/i} the one who stole it from a supply closet."
                s "I mean,{w=.3} the stuff was being donated to the needy anyway."
                s "I {i}was{/i} kinda needy at the time so.....{w=.3}ugh, nevermind."
                
                "I gave Sissel an encouraging smile and gently brushed his head."
                m "Hey,{w=.3} we've all had our share of misfortunes."
                m "You've got nothing to be ashamed of."
                s "Sure........{w=.3}I guess."
                
                "It didn't sound like he took my words to heart."
                
                "...Our little brushing session continued for a while.{w=.3} Sissel kept leaning closer and closer to me as I cleared out his fur."
                m "Heh,{w=.3} getting comfortable, aren't we?"
                "Sissel laughed and playfully elbowed me in the stomach."
                s "You're just good at what you do."
                s "I've always wanted someone to brush me like this.....{w=.3}kinda like siblings or family."
                s "It's feels pretty cozy....."
                
                m "Oh that reminds me."
                m "I wanted to apologize about the whole \"touchy-feely\" part of our volleyball game."
                m "I hope things aren't too awkward between us."
                
                "Sissel scoffed and poked me on the nose."
                s "Don't worry about it, {w=.3}Owen was just being a horny dick."
                show sissel shirtless embarrassed with dissolve
                s "Wait, {w=.3} that didn't come out right."
                show sissel shirtless with dissolve
                s "But you get the point!"
                
                m "Heh,{w=.3} whatever you say Sissel."
                
                "I stood up and dusted myself off."
                m "There,{w=.3} all done. {p=.3}You're officially sand-free!"
                s "Thanks [charname]."
                
                "There was a slow pause between us as Sissel scratched his head nervously."
                show sissel shirtless embarrassed with dissolve
                s "S-say,{w=.3} if it's not too much to ask...."
                s "Could you...{w=.3}brush me again sometime?"
                s "I-I mean having someone else around makes things easier! {w=.3}A-a-and-"
                
                "It was my turn to laugh as I gave Sissel a friendly punch to the shoulder."
                m "Of course Sissel. {p=.3}Anytime."
    "Go Swimming.":
        "I grinned and gave Sissel the evil eye."
        m "We're all wet anyway, {w=.3}why not go for a swim?"
        s "[charname],{w=.3} I will {i}drown{/i} you-"
        show owen shorts grin closed with dissolve
        o "Whoohoo! {w=.3}Swimming time!{p=.3}I knew you would pick the best choice!"
        "Phillip peered at Owen suspiciously."
        p "You sound a bit too excited for this."
        show owen shorts grin with dissolve
        o "You don't have to sound so paranoid~{p=.3}I just like swimming!"
        o "The water's pretty rough though. {p=.3}You never know if the current's going to \"accidentally\" sweep away your swim trunks."
        "There was a husky edge to his voice.{p=.5}Oh Owen,{w=.3} you pervert."
        
        s "You're not seriously going to try and pants anyone, right?{p=.3}That's like a middle-schooler move."
        show owen shorts with dissolve
        o "Only if you're slow enough to be a victim!"
        o "Or you know.{w=.3} If you're a scaredy-cat that can't swim."
        o "....erh,{w=.3} no offense Phillip.{w=.3} That was for Sissel."
        
        s "Who said I couldn't swIM?!!"
        o "You were white as a sheet when you got on your kayak kiddo~"
        s "I was just a little motion-sick! {w=.3}That's all!"
        o "Reeeaaally now?"
        
        play music "batty.mp3" fadein 3
        show owen shorts grin with dissolve
        o "How about a little race? {w=.3}The first one to get to the opposite end of the cove wins!"
        s "Y-you're on!"
        
        show owen shorts grin closed with dissolve
        o "The loser will have to strip naked for everyone to oogle though!"
        s "What kind of fucked up rule is that?!!"
        o "Ready?"
        s "Wait I never said-!"
        play sound "water-splash.wav"
        hide owen with dissolve
        o "{size=+25}GO!!!{/size}"
        s "OWEN YOU PIECE OF SHIT GET BACK HERE!!"
        play sound "water-splash.wav"
        hide sissel with dissolve
        show phillip at center with dissolve
        "And off they go. {p=.3}Owen was gliding through the water like a sleek little dolphin. {w=.3}Welp,{w=.3} he was already a quarter of the way there."
        "And Sissel..............{w=.3}well,{w=.3} Sissel's doomed."
        p "Um, I don't think you're supposed to bend you arm like that."
        m "He's not moving very fast, is he?"
        p "Or floating. {w=.3}At all."
        
        scene lake road with Dissolve(3.0)
        "Phillip and I ended up jogging along the forest path to follow Owen and Sissel's little race."
        "Sissel was lagging behind,{w=.3} flapping wildly in the water in his attempts to catch up."
        
        show phillip shorts with dissolve
        p "I feel kind of bad for him now.....{w=.3}not that I want to see Owen's junk,{w=.3} but I'd rather Sissel wins."
        m "I don't mind seeing either of them naked but I kinda agree."
        "Phillip shoots me an exasperated grin as we kept running to catch up with them."
        hide phillip with dissolve
        "You know....maybe there was something I could do to help Sissel out."
        m "Echo! {w=.3}You there?"
        
        play sound "ghost.mp3"
        show echo neutral with Dissolve(2.0)
        
        e "Yo [charname], {w=.3} what's up?"
        m "Say....{w=.3}you mentioned that you could manipulate circumstances and situations right?"
        e "I suppose you want me to do something stupid for you, {w=.3}right?"
        e "Like helping Sissel win this little swimming race?"
        m "You read my mind!"
        e "Here you have phenomenal supernatural powers at your fingertips,{w=.3} and you're using them to get a chance to see Owen's dick."
        "I nodded sagely."
        m "That about sums it up~"
        "Echo sighs and scratches his head awkwardly."
        e "Well I guess I could give Sissel a hand."
        show echo wish smile with dissolve
        e "Here it goes-"
        stop music
        show echo wish with dissolve
        e "!!!!!????"
        
        play music "blue-feather.mp3" fadein 2
        e "Someone's here!"
        hide echo with dissolve
        "A cold shiver curls down my spine.{w=.3} This feeling...{w=.3}there was a wish here."
        play sound "chains.mp3"
        "What's that sound? {w=.3}Rattling.....{w=.3}chains?"
        play music "calm-guitar.mp3" fadein 3
        p "[charname],{w=.3} look at that!"
        m "Huh?"
        
        "The lake waters suddenly seemed to shift.{w=.3} A rushing current sweeps under Sissel and firmly pushes him down the cove."
        s "W-what is this?"
        o "Huh?"
        "The waters almost seemed to carry him gently along."
        "In no time at all,{w=.3} Sissel sailed past Owen's lead and reached the other end of the cove and winning the race."
        "I stared in shock and glanced behind me suspiciously."
        show phillip shorts with dissolve
        p "Whoa [charname],{w=.3} did you see that?"
        p "Sissel really did win!"
        
        m "Phillip,{w=.3} did you just......?"
        p "Hm?{w=.3} What is it?"
        m "Hm...............................{w=.5}nevermind."
        "I must have just imagined it,{w=.3} but I swear Phillip just-"
        "Nah."
        m "Anyway, let's go catch up with them!"

        
        scene lake water with Dissolve(3.0)
        
        "We found Sissel and Owen on the other side of the cove,{w=.3} bickering wildly among themselves."
        
        show sissel shirtless at farleft with dissolve
        show owen shorts at farright with dissolve
        
        s "HA! {w=.3}I won!"
        s "Who's the scaredy-cat now, twat?!"
        
        o "That was a fluke! {w=.3}You barely swam at all!"
        o "Some weird current carried you here!"
        
        show phillip shorts at center with dissolve
        p "Oh Owen,{w=.3} don't be a sore loser.{p=.3}Sissel beat you fair and square."
        
        "Owen sighs and slumps down into the water,{w=.3} ears drooping."
        m "Aaw,{w=.3} well I think you did a good job Owen."
        "He instantly perks up with a grin."
        show owen shorts grin with dissolve
        o "Well I'm glad someone appreciates my efforts."
        
        play music "in-your-arms.mp3" fadein 5
        o "Oh that reminds me!{p=.3}I guess a deal's a deal."
        o "This gives me a good excuse to go skinny dipping at least~"
        p "Wait,{w=.3} please don't-"
        
        show owen naked with Dissolve(2.0)
        "Owen's fingers hook against the waistband of his swim trunks before he slowly pulled them down,{w=.3} revealing himself in all his glory."
        "His bare body was completely exposed.{w=.3} Anyone passing by could catch an eyefull of him,{w=.3} yet he wasn't the least bit shy."
        o "Hehe, {w=.3}how's that?{p=.3} Like what you see?"
        
        "Owen winks at us expectantly,{w=.3} making a show of seductively licking his lips."
        stop music 
        p "............................."
        s "................................................."
        
        play music "wacky.mp3" 
        s "..........{w=.3}Well I'm getting out of the water now."
        p "I'll come with you!{w=.3} It doesn't look like there's many interesting things to see here anyway."
        
        o "H-hey! {w=.3}Wait! W-w-what about-?"
        
        hide sissel with dissolve
        hide phillip with dissolve
        
        show owen at center with dissolve
        o "-they left."
        "Owen slumped down again,{w=.3} his spirit utterly broken."
        "I walked up to him and patted his head in encouragement."
        m "Don't feel so down Owen,{w=.3} I think you're pretty hot."
        
        o "B-but doesn't anyone get hot and bothered anymore?!"
        o "All those pornos aren't realistic at all!"
        "Owen suddenly threw his arms around me in an exaggerated wail of despair."
        o "[charname]!{p=.3}What am I going to do?!{w=.3} What's the point of working out all the time if no one's going to impressed by it?!"
        
        play music "calm-guitar.mp3" fadein 4
        
        "I sighed patted his back patiently."
        m "I'm pretty sure everyone knows you have a good physique.{p=.3}They just don't want to inflate your ego anymore than it already has."
        o "Y-you think?"
        m "Pffft,{w=.3} oh Owen."
        m "Why do you always act so pompous? {w=.3}You're easily the most insecure guy around."
        play music "groove.mp3" fadein 2
        o "I-I-I just....."
        "Owen exhaled deeply and leaned against me.{p=.3}My face flushed a little as I felt the bulk of his body heat radiate against me."
        o "I just want to be appreciated just a little bit."
        o "It's kind of hard to get friendly with people around here,{w=.3} especially with my whole family thing...."
        
        menu:
            "Get \"friendly\" with Owen~":
                "I was only half-listening to Owen's little confession,{w=.3} a bit distracted by other things at the moment."
                "I was suddenly hit with the realization that a very naked Owen was pressing so close to me."
                m "Well I appreciate you....."
                "I subtly push my hips against Owen's front,{w=.3} the warm friction coaxing a small groan from his throat."
                
                "Owen chuckled and I felt his hands caressing down my back,{w=.3} fingertips tracing my spine lightly."
                "Something hot and wet was pushing against my thigh.{w=.3} Owen glanced down at me with a sheepish grin."
                
                o "Heh,{w=.3} looks like I'm not the only one trying to get friendly."
                m "Like I said before,{w=.3} I really do think you're hot Owen."
                m "Speaking of which,{w=.3} do you need some help down there{w=.3} big guy?"
                o "If you insist~"
                
                "We were out in the open right now.{p=.3}Anyone walking by could see our little session,{w=.3} but I didn't care."
                "With shakened breath,{w=.3} I sank down to my knees,{w=.3} trailing my hands down Owen's chiseled front as I do so."
                
                show owen_swimming at Position(xpos = 1, xanchor=1, ypos= 1, yanchor=1) with Dissolve(2.0):
                    xzoom 1.5 yzoom 1.5
                show owen_swimming at Move((0.75, 0.75), (0.3, 0.5), 20,
                    xanchor="center", yanchor="center"):
                
                "His cock was already hard and dripping with pre as I slid my hand around it and gave it a small squeeze."
                "Owen's masculine musk filled my nose as I pressed my nose against him,{w=.3} inhaling deeply."
                "Hesitantly,{w=.3} I gave the head a small lick and coaxed an approving moan from above."
                
                o "You're pretty good at this [charname]~"
                o "You sure you've never done this before?"
                
                "I sent him a sly smirk and swallowed down half of his cock in one motion.{p=.3}Owen instantly turned into a moaning puddle."
                
                show owen_swimming at center with Dissolve(2.0):
                    xzoom 1 yzoom 1
                    
                "His cock was pulsing with warmth against my tongue."
                "The salty scent of musk filled my mouth and I eagerly swallowed down any pre-cum,{w=.3} massaging the head against the back of my throat."
                "I began milking him slowly,{w=.3} sliding his meat in and out as I sucked any cream that leaked its way out."
                "While I bobbed my head on his dick,{w=.3} Owen massaged his fingers through my hair,{w=.3} pushing me to go faster."
                "Before long,{w=.3} he was forcefully humping against my mouth,{w=.3} a steady stream of pre flowing down my throat."
                "I was moaning helplessly{w=.3} too far gone in the feeling of being so roughly used."
                play sound "heartbeat.mp3" 
                o "Aah...{w=.3}[charname]....."
                o "I'm getting close................."
                
                "I slide a hand around grasped his rump teasingly,{w=.3} another caressing his plump family jewels."
                "Better make it a good one~"
                
                "With a lusty groan,{w=.3} Owen thrusted deep into my throat."
                "I shivered as I felt shot after shot of hot cum spill into me.{p=.3}I swallowed against his cock hungrily,{w=.3} making sure not to spill a single drop."
                
                hide owen_swimming with Dissolve(3.0)
                
                "After a long while,{w=.3} Owen finally pulled out."
                "We were both panting heavily,{w=.3} trying to catch our breath."
                "I swished my tongue around my mouth and relished the taste of the musky cum I had just swallowed down."
                
                o "Heh.......{w=.3}that was great [charname]."
                o "We should do this more often~"
                
                "I leaned forward and gave Owen's cock one last,{w=.3} good lick before grinning up at him."
                "Owen almost purred."
                
                m "Anytime big guy~"
            "Pull your pants up and let's go for a walk.":
                play music "lullaby-guitar.mp3" fadein 3
                m "Well first of all,{w=.3} you better pull your pants up before someone sees you."
                m "Not that I don't appreciate seeing your butt and all,{w=.3} but getting arrested for public nudity doesn't sound too fun."
                show owen shorts with dissolve
                o "...aaw fine."
                
                scene lake road with Dissolve(4.0)
                "Owen and I ended up taking a long relaxing walk around the lake."
                "Well, relaxing to me anyway."
                "Owen was still sulking and mumbing to himself."
                show owen shorts with dissolve
                o "You'd think at least {i}someone{/i} would be interested..."
                
                m "You know,{w=.3} for a spoiled rich kid,{w=.3} you sure are attention starved."
                m "Why can't you just be friendly without all the groping and touching?"
                
                o "You're starting to sound like Phillip, you know."
                m "Not very surprised. {w=.3}I'd watch out if I were you,{w=.3} he's going to snap one of these days and it won't be pretty."
                o "Fiiiine I'll keep that in mind."
                o "........................."
                o ".............do I really act that spoiled?"
                m "Well...{w=.3}sorta?"
                m "You jump into people's personal space without a second thought and expect them to like you right away."
                o "Well if I didn't,{w=.3} most people would just assume \"Oh!{w=.3} He's a Lorelei,{w=.3} so he must be a greedy stone-cold bitch!\""
                
                m "Do people really hate your family that much?"
                
                o "My dad comes from a rich family of CEOs,{w=.3} and my mum was a pretty successful businesswoman herself."
                o "It's just that....{w=.3} the Lorelei family's been known to operate in a.....{w=.3} moral gray area."
                
                o "A lot of local businesses got ruined because of how ruthless my father's company was."
                o "I mean,{w=.3} the hate is kinda justified but...."
                
                o "It'd be nice to have some friends."
                m "Heh,{w=.3} you've got me and Phillip."
                m "Sure Phillip's patience is a bit limited but I'm sure he still likes having you around."
                o "Are you kidding?{w=.3} He spears me with eye-lasers every time I get close!"
                m "I doubt he's judging you because of your family."
                m "He still laughs at your terrible jokes. {w=.3}And you......{w=.3}tolerate his puns."
                m "I'd say that's a good start!"
                m "Oh and speaking of Phillip-"
                
                show owen at right with dissolve
                show phillip neutral at left with dissolve
                p "[charname]! Owen!"
                p "...Oh good,{w=.3} you're wearing something for once."
                p "We're leaving in about 40 minutes. {w=.3}Mrs. Corlisse says we can take a break until then."
                
                m "Sounds good."
                o "Hey Phillip! {w=.3}I gotta ask you something,{w=.3} be honest."
                p "........sure?"
                o "What do you think about me?"
                
                "Owen stares at Phillip,{w=.3} anxiously awaiting an answer."
                show phillip irritated with dissolve
                p ".........um,{w=.3} you sure you want an honest answer?"
                o "Y-yes!"
                "Phillip sighs, {w=.3} sounding a bit exasperated."
                p "You're a tactless idiot with zero respect for personal space. {w=.3} You can't seem to take no for an answer and you need to stop making innuendos at every opportunity."
                o "O-ouch."
                o "W-what about my family?"
                p "Oh don't even get me started with the Lorelei's."
                p "Your dickbag of a family drove my mom out of at least 3 jobs and forced almost every ma 'n pop store on my street go bankrupt."
                p "Not a big fan."
                
                o ".......O-oh."
                
                show phillip neutral with Dissolve(2.0)
                p "Buuuuuut........."
                p "You're also kind and generous sometimes,{w=.3} and you keep things pretty lively and friendly."
                p "You've been very welcoming to everyone around you,{w=.3} even when they treat you terribly."
                p "It'd be nice to see you stand up for yourself,{w=.3} but you're by far the most tolerable Lorelei I've ever met."
                "Phillip paused and took a deep breath."
                p "Also,{w=.3} you're not your family."
                p "You're capable of being something different."
                p "I hope you'll take advantage of that fact someday."
                
                o ".....T-thanks Phillip,{w=.3} I really needed to hear that."
                show phillip smile shrug with dissolve
                p "Aaand...{w=.3}sometimes when you're not being such a perv, {w=.3}you're quite charming.{p}{i}Sometimes{/i}."
                
                show phillip behind owen
                show owen shorts grin closed at left with dissolve
                o "Oh Phillip you're the best friend anyone could ask for! {w=.3}Please marry me!"
                show phillip annoyed look at farright with dissolve
                p "Personal space."
                o "O-oh, right."
                
                hide owen with dissolve
                hide phillip with dissolve
                "I grinned as I looked between the two before creeping ahead and leaving them to their own devices."
                "Owen was back to his old grinning self and Phillip didn't look half as murderous as he did a while ago."
                "The two of them were back to bickering about small and stupid things,{w=.3} as they should be."
                "Looks like peace is finally restored."
    
jump day3_afternoon 
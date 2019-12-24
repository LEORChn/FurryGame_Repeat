label day11_sissel_b:
$ persistent.current_route = "sissel_b"


"{b}Day 11:{/b}{w=.5} Not Your Typical Date"

stop music fadeout 3
scene black with Dissolve(3.0)
scene dorm night with Dissolve(2.0)

"After a long Visitor's Day,{w=.3} everyone retreated back to their rooms, completely exhausted."

"I haven't seen Sissel since he retreated from the ballroom in a flustered huff."
"Hope he's doing okay…"
"All in all, things went fairly smoothly today."
"Sissel won the regional competition and has a shot at the nationals."
"The Remnant was nowhere to be seen after Halley tackled him out a window."
"And Echo...."
"I sighed and buried my face into my pillow."
"I guess all that's left is to help Hershel confess everything to Sissel."
"It was something I was not looking forward to."

play sound "euca-ringtone.mp3"
"Suddenly,{w=.3} my phone rang."
"Fumbling around blindly,{w=.3} I caught the sound of Jinny's voice."
"She sounded very….. shifty."

play music "scheming.mp3" fadein 3

j "Hey [charname],{w=.3} I have a hypothetical question."
j "Hypothetically,{w=.3} if a guy asked you out,{w=.3} what's the sexiest outfit he could wear to persuade you?"
j "Like, what kinda outfit just makes you go \"hot damn!\""
j "Asking for a friend."
j "Uuhh….. hypothetically,{w=.3} of course."
m "Well.... it'd depend on who's asking-"

j "C'mon [charname],{w=.3} throw me a bone here!"
j "My uh -{w=.3} hypothetical friend -{w=.3} needs a confidence booster here."
m "Well let me think…..{w=.3} A hot outfit, huh?"

menu:
    "Leather jacket with tight pants.":
        $ sissel_outfit = "leather"
        m "Well probably a sexy black leather jacket with nothing underneath."
        m "Gotta show off that chest,{w=.3} you know?"
        j "Uh huh…."
        "There was a scribbling sound,{w=.3} as though she was taking notes."
        m "And he's gotta be swaggering around in tight leather pants."
        m "Top it off with a suave smile,{w=.3} and I'm open to a date..."
        m "...hypothetically."
        j "Of course."
        
        "There was a sharp {i}click!{/i} of a pen."
        j "So you've got a thing for hot men in leather huh?"
        j "That sounds pretty doable…"
        "A second voice rang out frantically in the background of the phone call."
        s "{size=-10}-but I don't HAVE any leather!{/size}"
        m "Huh?{w=.3} Is someone there with you?"
        j "What? Of course not!"
        j "Why would there be some hypothetical person with me?"
        s "{size=-10}Oh shit, did he hear me-?"
        
        play sound "surprise.mp3"
        show dorm night at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        j "{i}{b}Shut up.{/b}{/i}"
        m "Who-?"
        j "Nobody's here!{w=.3} This conversation never happened!"
        j "Goodnight!!!"
        
    "Fancy formal-wear with a cute bow-tie.":
        $ sissel_outfit = "formal"
        m "Mm…..{w=.3} maybe something on the fancier and formal side."
        m "I like me some well-dressed men."

        j "You are so old-fashioned."
        j "How fancy and formal are we talking here?"
        m "Probably a nice tuxedo and a cute tie."
        m "But he should be handsomely disheveled!"
        m "The jacket should be unbuttoned a little to expose {i}juuuust{/i} enough chest."
        m "Be fancy,{w=.3} but just saucy enough to show off some confidence, you know?"
        m "Like a prince charming coming to sweep me off my feet!"
        j "Really?{w=.3} A tuxedo?"
        j "Dude,{w=.3} it's like 95 degrees out this week."
        j "Prince Charming's gonna die from heatstroke and y'all can join me in the hospital."
        m "Well I guess he can take it off after asking me out…"

        "There was a scribbling sound on the phone,{w=.3} as though Jinny was taking notes."
        j "{i}Ask him out in a tux….{w=.3} and then strip during the date.{/i}"
        j "Man, you're more blunt and forward than I expected-"
        
        play sound "surprise.mp3"
        show dorm night at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        m "THAT'S NOT WHAT I SAID-"
        j "-sounds like a fun date though!"
        j "Let me know how it goes!"
        j "....hypothetically, of course."
        m "Wait Jinny I didn't mean-!"
        m "Hello? Jinny?!"
    
    "A lewd stripper outfit.":
        $ sissel_outfit = "stripper"
        m "A stripper outfit."
        j "Excuse me?!"
        m "You heard me."
        m "My date better come swaggering up to me in the skimpiest underwear and give me a lap dance."
        m "Maybe throw in a cute little bow tie and waiter cuffs for flavor."
        j "Man, you've got some weird taste."
        m "The fastest way to my heart is through my boner."
        
        "There was some scribbling sounds, as though Jinny was taking notes."
        j "It sounds pretty easy to pull off at least, but….."
        j "{size=-10}-hey are you doing okay? {w=.3} You look REALLY red-{/size}"
        "More rustling."
        "And then a soft {i}\"thump!\"{/i},{w=.3} as though a body just hit the floor."
        j "Ummm…{w=.3} would you still say yes to the date if the stripper fainted from embarrassment?"
        m "That sounds hecking cute,{w=.3} so yeah."
        j "Eh,{w=.3} good enough for me."
        j "Thank you for your hypothetical answers to my hypothetical questions."
        j "Just pretend this never happened, alrighty?"
        m "Uh sure?"

stop music fadeout 10
"The phone fell silent."
"I was left pondering what kind of madman calls at 2AM to ask these kinds of weird questions."
"Still groggy,{w=.3} I flopped back into my bed and closed my eyes."
"I'll worry about it in the morning."

play sound "ghost.mp3" 
"As soon as the first waves of sleep washed over me,{w=.3} I felt a faint shiver travel down my spine."
"I groaned and sat up to see Halley floating at the foot of my bed."


m "Can't a guy catch some sleep in peace?"
m "What do you want?"

play sound "ghost.mp3" 
play music "somber.mp3" fadein 3
show halley neutral with Dissolve(2.0)
"Halley rolled her eyes as she dusted off her shoulders."
u "I see you survived the day after I handled the Remnant."
u "You're welcome, by the way.{w=.3} You're ever the grateful one."

"Handled the…?"
"The image of Halley tackling the Remnant out the window came to mind."
"I sighed and stared at her begrudgingly."
m "Thanks,{w=.3} for taking care of us today."
m "What ended up happening to the Remnant?"

"Halley stretched her shoulders and shrugged."
u "He's handled."
u "A little piece of him here,{w=.3} a little piece of him over there."
u "Honestly,{w=.3} most troublesome people are much more manageable when divided into tiny bits."

"I stared."
u "It's not dead, of course."
u "Cursed wishes don't just die. {w=.3}You have to either fulfill them, or cause the wisher to give up on the wish entirely."
u "I simply bought you more time,{w=.3} at most.{w=.3} It'll reform sooner or later."

hide halley with dissolve
u "Speaking of reforming,{w=.3} I found a little something for you--"
"Halley dug around her pockets before pulling out what looks like a small shard of glass."
"She gingerly placed it on the palm of my outstretched hand."

m "What's this?"

show halley neutral with dissolve
u "It's your wish--{w=.3} what was his name?{w=.3} Echo?"
u "Well,{w=.3} it's what's left of him at least."
u "I found this shard after I ripped open the Remnant's stomach."

"I felt a little nauseous at the thought."
"The little shard of glass glistened in my hand as I caressed it gently."
m "So....{w=.3} this is a piece of Echo?"
u "Yes.{w=.3} Keep it with you, and it should help Echo reform."
u "Hypothetically,{w=.3} at least."

"My heart twisted painfully at the sight of his reduced form."
"I held him close to my ear and whispered to him gently--"
m "{size=-5}...Hello? {w=.3}Echo….{w=.3} you still there?{/size}"
"In the quiet of the dark night,{w=.3} I swore I heard a small voice whisper back a small {size=-10}\"....hello.\"{i}{/size}"

"Smiling in spite of myself,{w=.3} I held the little shard close to my chest."
"With a small glow,{w=.3} the little piece of shooting star sank into my camera,{w=.3} like a pebble dropped in water."
m "...It's good to have you back,{w=.3} buddy."

"Halley sighed and stood up to leave."
u "That should take care of most of our problems for the time being."
m "....thanks Halley.{w=.3} It's nice to have you on our side."

stop music fadeout 5
"I stared at her a little closely and frowned."
m "Are you feeling alright?"
m "You look upset… {w=.3}more so than usual."

"Halley turned around sharply and snapped."
show dorm night behind halley at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
u "I don't {i}{b}feel.{/b}{/i}"
m "Could have fooled me."
m "What do you mean you don't feel? {w=.3}All the other wishes seem to get pretty emotional."

"Halley fell silent."

play music "asphodel2.mp3" fadein 3
u "I once felt all sorts of things."
u "Compassion being one of them."
u "But…{w=.3} feeling {b}hurt.{/b}"
u "Seeing the one you love fall again and again,{w=.3} {i}{b}hurt.{/b}{/i}"
u "It hurt a lot."

u "I had a job to do and the hurt got in the way of things."
u "So I turned it off."
m "Turn it off??"
m "What,{w=.3} did you flick a little switch that goes{i} \"beep boop,{w=.3} parameters recognized,{w=.3} no more feelies for me\"?{/i}"
"I paused suddenly and strained my ears."
"Faintly,{w=.3} in the thick bedroom silence,{w=.3} I heard a faint {i}\"tick,{w=.3} tick, {w=.3}tick…\"{/i}"
"Like a mechanical heart."

"Halley scowled at me and turned to leave."
u "You're an ass."
u "It was stupid to even talk to {i}you{/i} of all people about this."

stop music fadeout 5
"With that,{w=.3} she disappeared into the air,{w=.3} leaving me alone in my dark bedroom."

scene black with Dissolve(3.0)
pause(2)
play music "calm-guitar.mp3"
scene dorm with Dissolve(2.0)

"This morning went as normally as mornings could at Gerania Academy."
"My alarm started screaming,{w=.3} thoroughly testing my will to live as I wormed my way out of bed."
"That is to say,{w=.3} mornings are horrendous at Gerania Academy."
"Or anywhere else."


scene kitchen with Dissolve(2.0)

"I was halfway through microwaving pop-tarts (chocolate) when Phillip and Owen slid into the kitchen cheerfully."

show phillip annoyed at left
show owen neutral at right 
with Dissolve(1.0)

pause(1.5)

hide phillip
hide owen 
with dissolve

"The two of them casually greeted me before settling down at the other end of the room."
"No sarcastic quips,{w=.3} no bickering,{w=.3} no flirting."
"Perfectly well-behaved,{w=.3} like two young gentlemen being watched by their parents."
"My bullshit radar immediately began screaming like my morning alarm."

m "Alright, what's the cheese? {w=.3}What are you two hiding?"
"I squinted and jabbed my half-eaten pop tart at them suspiciously."

show phillip annoyed at left
show owen neutral at right 
with Dissolve(1.0)

"Phillip shrugged."
o "What do you mean?"

show owen grin 2 with dissolve
o "We're just innocently enjoying our breakfast from a respectable distance!"
m "It's suspicious.{w=.3} You'd usually make half a dozen innuendos at Phillip by now."
"Phillip snickered into his morning coffee."

show phillip smile with dissolve
p "Good point.{w=.3} I'm really enjoying this change of pace, actually."
"Owen scooted closer to Phillip and whispered frantically."

show owen grin nervous with dissolve
o "{size=-10}Dude we're supposed to act natural!{/size}"
"Owen turned back towards me nervously."

show owen grin 2 with dissolve
o "Uh, {w=.3}Phillip and I are just getting along super well these days!"
o "Been working through our problems together,{w=.3} taking down emotional walls,{w=.3} etc"

show owen grin 3 with dissolve
o "We're real bros now,{w=.3} right man?"
"Owen hung a friendly arm over Phillip's shoulder."
"For once,{w=.3} Phillip didn't brush him off as he continued sipping his coffee."

show phillip annoyed with dissolve
p "Well I wouldn't go {i}that{/i} far."
show phillip annoyed look with dissolve
p "At most,{w=.3} I've learned to tolerate you a little more."
"Owen looked as though Christmas came early and all his dreams came true."

play sound "surprise.mp3"
show owen grin 2 
show kitchen behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
o "Did you hear that?!"

play sound "surprise.mp3"
show kitchen behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
o "He tolerates me now! <3"

stop music fadeout 5
hide owen 
hide phillip 
with dissolve
"The kitchen door suddenly swung open and an excited Jinny pranced inside."

show jinny neutral with dissolve
j "Yo he's all dressed and ready!"
j "Is [charname] here yet--?"
"Jinny caught sight of me.{w=.3} Her grin grew even wider."
"It was kinda scary, {w=.3}really."

play music "scheming.mp3"
m "Jinny? {w=.3} Aren't you supposed to be under house arrest?"
j "Well it's technically not {i}real{/i} house arrest--"
m "--And how did you get inside the dorm building?{w=.3} You don't even go here!"
j "I stole the keys from Gran.{w=.3} She should really guard her purse a little better…"
j "Anyway,{w=.3} I just wanted to spend a morning with my BEST friends,{w=.3} nothing wrong or suspicious about that!"

m "That's exactly what a suspicious person would say."

hide jinny with dissolve

show phillip annoyed at farleft
show owen neutral
show jinny neutral at farright 
with dissolve
"Jinny ignored me and slid across the room to join Phillip and Owen at the table."
"They all glanced between me and the door expectantly.{w=.3} Like a circus audience waiting for the tutu elephant to start dancing."
"At this point my bullshit radar was ringing at maximum capacity."
m "....y'all are acting real fishy right now……"
"There was suddenly a knock at the door."
"Everyone fell silent and stared."
"Three pairs of expectant eyes fell upon me as the knocking continued."
j "Well [charname]?"
j "Aren't you going to get that?"
m "Who the hell knocks on the kitchen door??"
m "Just come in."

show owen grin 2 with dissolve
o "I dunno,{w=.3} looks like they really want someone to answer the door."
o "You can't just leave them waiting!"

stop music fadeout 5
"The three of them continued staring at me intensely."
"....................."

hide owen
hide phillip
hide jinny 
with dissolve
"{i}\"Peer-pressure's a bitch,\"{/i}{w=.3} I thought as I grabbed the doorknob."

play sound "slam.wav"
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
"As soon as the door opened,{w=.3} I felt a hand roughly shove me backwards."
m "Hey! {w=.3}What was that for--?"
"Sissel unceremoniously waltzed in,{w=.3} swept me off my feet,{w=.3} and then pinned me against the kitchen wall with a suave grin."
"He moved so smoothly that it was obvious he rehearsed this dozens of times before doing it to me."
"I lifted my head and suddenly caught sight of what he was wearing."
play music "jazz.mp3" fadein 3

if sissel_outfit == "formal":
    scene sissel_formal1 with Dissolve(2.0)
    pause(2)
if sissel_outfit == "leather":
    scene sissel_leather1 with Dissolve(2.0)
    pause(2)
if sissel_outfit == "stripper":
    scene sissel_stripper1 with Dissolve(2.0)
    pause(2)


s "Mornin' [charname]~!"
s "Whew,{w=.3} is it hot in here,{w=.3} or is it just you?"
"I just stood there gaping like a speechless goldfish."
s "You know what's on the menu tonight?{w=.3} Me 'n u~"
m "..........................................."
s "Uh….."
s "You want raisins for dinner tonight? {w=.3}Cuz we can make it a date………..{w=.5}.............?"
m "..........................."
s "I-"
s "I-I'm uh…… asking you out….? I think?"

stop music fadeout 5
"More silence."
s "Y-y-you wanna go on a date w-w-with me tonight?"
s "I-I uh… got this fancy dinner reservation and um… it'd be cool if you could come with me…?"
s "I just kinda really like you a lot a-a-and--"

m "...pfft--"
play music "batty.mp3"


if sissel_outfit == "formal":
    play sound "surprise.mp3"
    show sissel_formal2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    pause(2)
if sissel_outfit == "leather":
    play sound "surprise.mp3"
    show sissel_leather2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    pause(2)
if sissel_outfit == "stripper":
    play sound "surprise.mp3"
    show sissel_stripper2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    pause(2)

m "{i}HAHAHAHAHAHAHA--{/i}"

"At this point, I burst out laughing hysterically."
m "Oh my god, you actually wore the damn outfit!!"
"I managed to hack out a few words between gasping laughs."
"Sissel's face was a whole new level of red."

s "W-well you said you thought dudes wearing this kinda stuff was hot!"
s "Aaaaah fuck, {w=.3}I knew this was a stupid idea--"
"Sissel hung his head in embarrassment."

if sissel_outfit == "formal":
    scene sissel_formal3 with Dissolve(2.0)
    pause(2)
if sissel_outfit == "leather":
    scene sissel_leather3 with Dissolve(2.0)
    pause(2)
if sissel_outfit == "stripper":
    scene sissel_stripper3 with Dissolve(2.0)
    pause(2)

"I swiftly cupped Sissel's cheek and raised his head up to look him in the eyes."
m "Hey now,{w=.3} I never said \"no,\"{w=.3} now did I?"
"Sissel's ears perked up."
s "You mean..?"
m "Hell yeah I'd go on a date with you!"
m "Couldn't have asked for a better guy to be with!"
"If possible,{w=.3} Sissel's face transcended the color spectrum into an entirely new shade of pink."
"A genuine, happy smile spread across his face."
s "T-thanks [charname]...."

play music "soothing-rain.mp3" 
play sound "surprise.mp3"
o "WHOOHOO!"
o "You did it!"

show confetti

"Behind us,{w=.3} Phillip, Owen, and Jinny all cheered while gleefully tossing fistfulls of confetti into the air."
"Sissel chuckled and scratched his head bashfully."

m "I guess I have those three to thank for arranging all this."
m "I'm still shocked that you wore what I mentioned!"

if sissel_outfit == "leather":
    m "The leather jacket looks real good on you."
    m "Definitely makes you one badass boyfriend~"
    s "It does give out a cool punk vibe--"
    s "But it's kinda really itchy,{w=.3} to be honest…"
    "My hands brush across his spiked belt and traced the lining of his leather pants."
    "Sissel squeaked when I groped the tight leather hugging his ass."
    m "I dunno,{w=.3} you look like one tasty package~"
    "Sissel almost melted into my grip before he realized where he was and coughed loudly."
    s "A-ah t-thanks man,{w=.3} but people are w-watching--!!"
    "I let go of his butt with a disappointed sigh."
    m "Well I guess we'll have to save it for the date tonight."
    s "Y-yeah, definitely!{w=.3} Meet me at the parking lot at 6 and--"

if sissel_outfit == "formal":
    m "This ain't a full tuxedo,{w=.3} but you nailed the \"handsomely disheveled\" look."
    m "Prince charming has successfully swept me off my feet~"
    s "Ahaha thanks, I'm glad to hear that~"
    s "I didn't have anything fancy to wear so I panicked for a while."
    s "Thankfully Boss let me borrow some of his clothes from his younger days."
    m "You wear it better than he does~"
    "I pulled him closer by his tie and gave him a light smooch on the cheek."
    "He flushed and glanced across the room at Jinny and Owen,{w=.3} who were cheering and clapping furiously."
    "Phillip just gave us a thumbs up and sipped his coffee."
    s "Eheh, let's save things for the date,{w=.3} when we have a little more privacy."
    m "You gonna do that stripping part I mentioned during the phone call~?"
    s "N-no!"
    s "I-I mean-- m-maybe?"
    o "Need me to teach you how to do a strip tease?"
    s "SHHHHHHHH!"
    s "A-anyway! {w=.3}Meet me at the parking lot later at 6 and we'll--"

if sissel_outfit == "stripper":
    m "Might I say,{w=.3} you look reaaaaal fine~"
    "I trail my hand down his front and fiddle with the thin band of the jockstrap he was wearing."
    "Sissel's face was utterly flushed, {w=.3}but he didn't move to stop me."
    s "I had to walk down the hall wearing this!!"
    s "What if Mrs. Corlisse caught me or something?!"
    m "That's a risk I'm willing to take."
    m "You look so damn cute in this little thing!"
    m "Where did you get this stripper outfit anyway?"
    s "Well uh….."
    o "He got it from me actually!"
    "Owen beams proudly from across the room."
    o "I wore this when I won Amateur's Night at the downtown strip club last year!"
    o "Honestly though,{w=.3} I think Sissel wears it better than I do."
    "Sissel's blush practically encompassed his entire upper body at this point."
    s "Dude, why do you even have so many lewd outfits--?"
    
    play sound "surprise.mp3"
    show sissel_stripper3 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    s "EEP!"
    "I gave Sissel a sly grin as I gently traced my finger down the tight bulge of his underwear."
    "So warm.{w=.3} I can feel it growing bigger too…"
    s "Alright!{w=.3} Let's save this for the date tonight! {w=.3}Where these three aren't watching!"
    m "I'm holding you to that~"
    "As Sissel turned to leave, {w=.3}I gave his butt a quick spank."
    "He squeaked loudly before darting out of this room."
    "This is gonna be a fun night~"
stop music fadeout 5
scene black with Dissolve(3.0)
pause(2)
scene restaurant exterior with Dissolve(2.0)

play music "jazz.mp3"

"Later that night,{w=.3} Sissel lead me to the richer part of the city where he made a dinner reservation at a fancy restaurant."
"Even from a distance,{w=.3} it looked absolutely dazzling."
"Massive glass windows revealed rows and rows of exquisitely decorated seating areas."
"The architecture just screamed that rich and gaudy people dined here with their pinkies outstretched and wallets stuffed."
"The peak of 5-star restaurant elegance."
m "W-whoa……"
"My heart felt fluttery.{w=.3} How did Sissel afford to take me to a place like this?"

"As we approached,{w=.3} a well-lit sign with the restaurant's name came into view."
play sound "record-scratch.mp3"
"I immediately did a double-take."

m ".......{i}\"Very Legal Seafoods.\"{/i}"

show sissel happy with dissolve
s "D-do you like it?{w=.3} It's the fanciest 5-star restaurant in the city!"
s "It's ranked among the best of the best all-you-can-eat buffet around these parts."
s "Which works out great,{w=.3} cuz I always get confused when there are too many fancy options on the menu."
m "That sounds great but…."
m "That restaurant name worries me."

"I jabbed a doubtful finger at the glowing \"Very Legal Seafoods.\""
m "It's like strolling up to a police station exclaiming {w=.3}{i}\"Why hello officer!\"{/i}" 
m "{i}\"Good day,{w=.3} I just wanted to mention that I did NOT commit murder today!{w=.3} Have a good one!\"{/i}"

show sissel indignant with dissolve
s "Maybe they just like to be extra reassuring?"
s "It's still a famous and very expensive restaurant for a reason."

"Sissel watched me intently,{w=.3} as though hoping to impress me with all this luxurious splendor."
"I squinted at the restaurant's gaudy sign suspiciously."
m "Expensive doesn't always equate to good…."
m "How did you afford to take us here?"

show sissel happy with dissolve
"Sissel scratched his head with a hint of embarrassment."
s "Uh…{w=.3} a friend of mine managed to hook me up with some meal vouchers for this place."
m "I'm surprised this place even offers meal vouchers."
m "How did you friends get their hands on them?"
s "Honestly, I've got no idea."


play music "batty.mp3" 

show sissel_voucher_threat with moveinright

pause(1.0)
#ART- SQUAD THREATENING - SLIDE IN
#Pan over to scene where Phillip and Jinny are threatening a waiter with a taser and a knife. Jinny's doing finger guns. Owen is rifling through his wallet in the background.


"Waiter" "P-please sir,{w=.3} for the last time,{w=.3} we don't offer vouchers or coupons at Very Legal Seafoods--!"
j "{i}--you do {b}now.{/b}{/i}"
"Phillip's taser cackled menacingly while Jinny threatened the poor waiter with finger guns."
o "We're not robbing you,{w=.3} there'll be fair compensation."
o "Just pretend you're accepting vouchers from our friend this one night."
o "Treat him like an honored guest."
"Waiter" "Can't you just give money to your friend…?"
o "He gets really self-conscious and insecure when taking money."
o "Anyway, {w=.3} how much is this gonna be…?"

hide sissel_voucher_threat with moveoutright
play music "<from 20>jazz.mp3"

m "You've got some very good friends."
s "D-do you still wanna go?"
m "Of course!{w=.3} I'd never say no to a free buffet with handsome company."
"Sissel flushed as I grabbed his hand and marched towards the entrance."
m "By the way,{w=.3} not that I'm complaining,{w=.3} but why did you wait until this morning to ask me out?"
m "Weren't you going to ask me right after the competition yesterday?"

"Sissel's face instantly heated up as he looked anywhere but my direction."

show sissel indignant with dissolve
s "Well uh….."
s "I was planning to!"
s "It just…{w=.3}didn't feel good enough, you know?"
show sissel upset with dissolve
s "Or maybe I just didn't feel confident enough…."

"He looked down with a sheepish smile on his face."
show sissel embarrassed with dissolve
s "In all the books and movies,{w=.3} all the guys put on such a romantic show when they ask people out!"
s "Like a burst of flowers,{w=.3} or dancing by candlelight or--"
"Sissel coughed awkwardly."

s "A-anyway!"
s "Just straight up asking you didn't feel good enough,{w=.3} so I figured I'd make it more flashy!"
s "{size=-10}...I was still half-expecting you to say \"no\"……..{/size}"

m "Wah?{w=.3} Of course I'd say yes!"
m "Not that I didn't enjoy the show this morning,{w=.3} but I would have said yes regardless of how you asked."
m "You're such a sweet guy~{w=.3} Plus, I've had my eyes on you for a while."
m "The way you worry so much about impressing me is {i}adorable.{/i}"
"Sissel's ears twitched as he tried to look displeased."

show sissel indignant with dissolve
show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
s "I'm not \"adorable!\""
s "I'm a tough and cool punk!"

m "Sure you are."
"I patted Sissel's head like a puppy."
"He grumbled and tried to hide his smile."
m "It's a shame you didn't wear your outfit from this morning though."
m "That would have really sealed the deal for me."

if sissel_outfit == "leather":
    show sissel surprised
    show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
    s "I can't come here wearing an open leather jacket and tight pants!"
    s "This place is full of uptight prudes!"
    s "If I showed up dressed like that,{w=.3} they'd kick me out in an instant."
    m "Didn't you say you were a cool punk?{w=.3} Be rebellious!{w=.3} The tight leather was perfect for you!"
    show sissel indignant with dissolve
    s "W-well maybe the world isn't ready for my punk..."
    m "Yeah,{w=.3} you're right."
    m "They wouldn't be able to handle your hot leather ass."
    
    show sissel surprised
    show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
    s "W-wha--?{w=.3} I-I mean--"
    
    show sissel indignant with dissolve
    s "Uh- t-thanks…"
    s "A-anyway!"

if sissel_outfit == "formal":
    m "Your dress shirt would have fit right in with this fancy atmosphere."
    m "Just disheveled enough to be handsomely charming,{w=.3} but not gaudy enough to be too uptight."
    m "Truly a Prince Charming to sweep me off my feet~"
    "Sissel blushed and puffed out his cheeks."
    show sissel happy with dissolve
    s "Eheh…{w=.3} thanks [charname]~"
    s "But that dress shirt was itchy as hell and my tie kept getting undone."
    m "Oh,{w=.3} I thought you left it undone for the aesthetic."
    m "It looked great!"
    s "Uh…{w=.3} y-y-yeah!"
    show sissel wtf blush with dissolve
    s "I left it undone on purpose! {size=-10}(and not because I don't know how to tie ties…){/size}"
    show sissel indignant with dissolve
    s "A-a-anyway,{w=.3} I'm glad you liked the outfit, but…"

if sissel_outfit == "stripper":
    "Sissel's face ignited with red at the memory."
    
    play sound "surprise.mp3"
    show sissel surprised
    show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15) 
    s "YOU WANT ME TO TAKE YOU TO A RESTAURANT WEARING {b}THAT{/b}???"
    m "Well it'd definitely make the night more interesting~"
    
    show sissel surprised
    show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15) 
    s "The doorman would kick me out on sight!"
    m "Or maybe they'd think one of the rich people ordered a stripper! {w=.3}I hear they get pretty crazy at parties--"
    show sissel wtf blush with dissolve
    s "Absolutely not."
    m "Aaaaw, I was looking forward to seeing you wearing it again."
    "I pouted."
    "Sissel looked flustered and scratched his head bashfully."
    show sissel indignant with dissolve
    s "W-well if you want to see it again,{w=.3} I-I might be willing to dress up again s-sometime…."
    m "Really?!"
    play sound "surprise.mp3"
    show sissel annoyed 
    show restaurant exterior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15) 
    s "{size=+10}PRIVATELY.{/size}"
    
    show sissel indignant with dissolve
    s "A-a-anyways!!!"

s "If I'm coming on a date, I'm gonna go dressed as myself."
s "Gotta be genuine on your first date, r-right?"
m "Hehe,{w=.3} I like your spirit."
m "C'mon, let's hurry up and get inside!"

scene black with Dissolve(2.0)
scene restaurant interior with Dissolve(2.0)

"The restaurant was so brightly lit,{w=.3} it felt like staring into the sun."
"All around us where pristine marble floors and shimmering chandeliers,{w=.3} as far as the eye could see."

"Calling it \"beautiful\" would be doing the restaurant a disservice."
"However…{w=.3} I couldn't help but sense a little...{w=.3} nasty edge to this place."

"As soon as we walked through the front door,{w=.3} the staff member at the front desk immediately scrunched his nose at Sissel's unkept appearance."
"It was the kind of face someone would make at a dirty animal."
"I opened my mouth,{w=.3} ready with some sassy retort but I felt Sissel place a hand on my shoulder."
"He laughed apologetically."

show sissel happy with dissolve
s "Hey,{w=.3} don't worry about it."
s "Let's just try to have some fun tonight."
m "But…"
"I sighed with a huff."

stop music fadeout 8
"Alright, snobby desk clerk.{w=.3} You may live."
"{i}For now.{/i}"

scene black with Dissolve(2.0)
play music "cafe-music.mp3" 
scene restaurant interior with Dissolve(2.0)

"The waiter soon lead us to our table."
"The seats were cushy and incredibly comfortable,{w=.3} and our table was lined with napkins folded into the shape of birds."
"Small candles flickered gently at every table of the restaurant,{w=.3} their light flickering gently above the fancy tablecloth."
"Sissel tried to be gentlemanly and pull the seat out for me,{w=.3} but then realized the chairs were stuck to the floor."
"He coughed awkwardly and sank into his seat."

m "Remember what I said earlier about being adorable?"
show sissel indignant with dissolve
s "I ain't adorable,{w=.3} I'm {i}cool.{/i}"

hide sissel with dissolve
"I laughed as I continued to take in my surroundings."
"The restaurant was gorgeous but…."
"My bullshit radar was definitely buzzing with a low \"something's fishy here.\" {p=.3}And it's not the seafood."

"I can't quite put my finger on it,{w=.3} but something was amiss here…"

"A fruit fly buzzed near my ear and I batted it away in irritation."
"C'mon [charname],{w=.3} focus!"
"You're supposed to enjoy your time with Sissel.{w=.3} Don't get distracted by the little things."
"Sissel asked you on a date and damn it, {w=.3} you're going to have a great time."

"Waiter" "Good evening{w=.3} dear guests."
"A waiter with perfect posture placed a small basket of bread at our table and smiled politely."
"Waiter" "May I get you two gentlemen something to drink?"

stop music fadeout 10
show sissel surprised with dissolve
"Sissel perked up and almost knocked over a candle."
"He grabbed the menu and fumbled through it in a small panic."

show sissel upset with dissolve
s "Oh um….."
s "{size=-8}Ugh I don't know any of these fancy drink names--{w=.3} Maybe I should just get a cola or a water?{/size}"
s "{size=-10}No no,{w=.3} don't wanna look like a basic bitch.{w=.3} What's something cool--?"

"There was a nasty look on the waiter's face."
"Waiter" "Ah apologies!{w=.3} I should have realized this restaurant's quality and taste would…. befuddle a guest like you."
"Waiter" "Perhaps you would like a simple glass of water?"

show sissel surprised with dissolve
pause(1)
show sissel nervous with dissolve
"Sissel shrunk in his seat and gave a small nod."
"He stared at the floor,{w=.3} almost ashamed."

hide sissel with dissolve
"The waiter turned to me with a patronizing smile."
"Waiter" "What about you,{w=.3} sir--?"

play sound "surprise.mp3" 
play music "scheming.mp3" 
show restaurant interior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
m "I would like a large cup of coffee with 2 teaspoons of sugar, 1.2 cc of Splenda, with 0.5 pints of 2\% milk mixed with almond milk, 5 tablespoons of cocoa powder, with exactly 4 ice cubes. Shake the whole thing until there's just 0.2 inches of frothy bubbles at the top and serve it with an organic cherry on top drizzled with Swiss chocolate syrup in the shape of a cactus {i}{b}please.{/b}{/i}"

"Waiter" "Wha-?"
m "And if you get the slightest bit off,{w=.3} I will send it back in to be remade along with a stern note for your manager."
m "Surely,{w=.3} a high-class restaurant of this caliber can manage this?"

"I was practically seething venom as the waiter frantically jotted everything down on a small notebook."
"Waiter" "W-why yes, of course-"
m "That will be all,{w=.3} thank you."

"I waved a hand dismissively at him and turned back to Sissel."
"As soon as the waiter was out of earshot, {w=.3} I let out an infuriated groan."

m "The {i}nerve{/i} of that guy!"

show sissel happy with dissolve
s "Eheh,{w=.3} don't worry about it,{w=.3} I'm used to this kinda stuff."
s "Don't let it rile you up--"

play sound "surprise.mp3" 
show sissel surprised 
show restaurant interior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)

m "I was defending your honor!"

s "...................................."
show sissel happy with dissolve
"Sissel blinked silently for a moment before bursting out into snickers of laughter."
m "What's so funny?!"
s "Pfft-{w=.3} ha--!"
play sound "surprise.mp3" 
show sissel smile
show restaurant interior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
s "It's just that --{w=.3} I've never seen you so angry before!"
s "And you got so mad you turned full-on suburban mom on the waiter just because he was a little rude to me-"
"Sissel cackled hysterically."

"I grumbled and tossed a chunk of bread at him."
hide sissel with easeoutbottom
"He gracelessly ducked out of the way between his laughs."
m "Well I just wanted to stick up for my date.{w=.3} There's nothing wrong with that!"
m "And you!"
m "You shouldn't take bullshit like that sitting down!"
show sissel happy with easeinbottom
s "I'll be sure to stand up the next time you roast someone in my honor."
stop music
"One of the restaurant patrons behind us suddenly cleared their throat loudly."
"Sissel stopped laughed and glanced around."
"Everyone was staring at us."

show sissel nervous with dissolve
s "O-oh, sorry."
s "Were we being too loud?"

"One of the patrons let out a pompous \"hmph!\" before turning back to their respective, quiet conversations."

play music "water-lily.mp3" fadein 3 
"All around us were tables filled with well-dressed gentlemen and ladies with frilly dresses and pristine suits."
"Sissel's frayed shirt and patched-up shorts stood out like a sore thumb against all the extravagance."
"He shrunk back into his seat dejectedly."

m "Yeesh,{w=.3} these people are more uptight than I expected."
m "Are you doing alright, Sis?"

s "Y-yeah, I'm fine."
"Sissel mumbled half-heartedly and stuffed a breadstick in his mouth."
s "The bread's pretty good."

"I gave him a wistful look."
"This was going to be a tough night."

m "Hey Sissel….{w=.3} are you sure you want to be here--?"

stop music
play sound "euca-ringtone.mp3"
pause(2)

"My phone suddenly pinged with a new text message."

play music "scheming.mp3"
j "{i}The bread's actually pretty good,{w=.3} you should try it!{/i}"
m "How the fuck--"

scene sissel_restaurant_snoop 1 at Position(xpos=0.6) with Dissolve(2.0)

s "Hm?{w=.3} [charname],{w=.3} is something wrong?"
m "N-no,{w=.3} everything's great!"
"Sissel did not look convinced."
s "Hey,{w=.3} I'm sorry if the date got off to a weird start…..{w=.3} but I'm sure we're gonna have a blast here."
s "Just think of all the great food!"

m "Haha,{w=.3} any time spent with a cute guy like you is a blast ~"
"-but seriously though,{w=.3} how does Jinny know about the bread?"

show sissel_restaurant_snoop 1:
         xpos 0.6
         linear 2.0 xalign 0.9
pause(3.0)

play music "wacky.mp3"
"...............wow."
show sissel_restaurant_snoop 2 with Dissolve(1.0)
m "This restaurant has some very interesting guests."
s "I know right?{w=.3} There's so many snobby rich people around."
m "Yeah,{w=.3} with dumb top hats and twirly mustaches."

"I squinted at Phillip's pigeon,{w=.3} who was busy pecking furiously at the tea leaves in his cup."

"My phone buzzed again."

play sound "surprise.mp3"
show sissel_restaurant_snoop 3 at Shake((0.9, 1.0, 0.9, 1.0), 1.0, dist=15)

j "{i}Dude, you're supposed to be enjoying your date!{/i}"
j "{i}Keep your eyes on your man!{/i}"

"A waiter suddenly approached their table looking very stern."
"Waiter" "{size=-6}Sir,{w=.3} I'm afraid we don't allow pets here at {i}Very Legal Seafoods.{/i}"
p "{size=-6}Excuse me?{/size}"
p "{size=-6}You don't understand,{w=.3} this pigeon is my daughter--{/size}"

play sound "surprise.mp3"
show sissel_restaurant_snoop 3 at Shake((0.9, 1.0, 0.9, 1.0), 1.0, dist=15)

"I gaped in utter bewilderment as a loud argument broke out behind us."

s "Man,{w=.3} the customers are pretty rowdy around here."
s "What is happening back there?"
m "N-nothing!{w=.3} Just a bunch of patrons being persnickety."
m "Wanna go grab some food before something bad happens?"

"Sissel brightened up as he stood up from out table,{w=.3} completely oblivious to Phillip wrestling a waiter behind him with a pigeon squawking furiously on his shoulder."

s "Sounds good to me!{w=.3} I'm starving!"

stop music fadeout 3
scene black with Dissolve(2.0)
play music "calm-guitar.mp3" fadein 2
scene buffet with Dissolve(3.0)

"The selection of food at {i}Very Legal Seafoods{/i} was truly massive."
"Rows and rows of buffet tables steamed with the mouth-watering scene of exotic seafood,{w=.3} most of which we've never even heard of."

"Sissel pulled me into the buffet area with a wide grin,{w=.3} but quickly grew overwhelmed by all the different choices."

show sissel happy with dissolve
s "I've never seen so much food in one place before."
s "What are you gonna get, [charname]?"

m "I've got no idea."
m "All the food labels are in fancy french."
m "I'm probably gonna look around first before committing to something."

s "O-oh,{w=.3} sounds good!"
"As the two of us wandered through the buffet tables,{w=.3} I catch Sissel nervously stealing occasional glances in my direction,{w=.3} as though to check that I'm still enjoying myself."
"I smiled encouragingly every time."

scene black with dissolve
scene buffet with Dissolve(2.0)

"At some point we ended up getting separated in the crowd of frilly dresses and overly-expensive tuxedos."
"I ducked my head in and out of the crowd aimlessly,{w=.3} searching for a glimpse of those familiar rabbit ears."

play sound "surprise.mp3"
show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
m "--oof!"
m "Sorry-{p=.3}Wait,{w=.3} Owen?"

show owen grin 2 with dissolve
o "Yo! [charname]!"
show owen grin 3 with dissolve
o "The food here's pretty fishy,{w=.3} huh?"
o "Don't get the caviar,{w=.3} it tastes like weird knockoff boba from a bubble tea shop."

"Owen popped a caviar into his mouth and grimaced."
show owen grin nervous with dissolve
o "Actually,{w=.3} I'm pretty sure that's exactly what is it."
o "{i}Very Legal Seafoods,{/i} indeed."

o "I think one of my rich cousins owns this place actually…"
m "Nevermind that!{w=.3} What are you and everyone else doing here?!"

show owen grin 2 with dissolve
o "Why, {w=.3} we're chaperoning your date of course!"
show owen grin 3 with dissolve
o "Gotta make sure everything's running smoothly for you guys! <3"

m "I guess we've got you guys to thank for those \"meal vouchers?\""
m "Gotta be honest though,{w=.3} this place feels a little out of character for Sissel."

stop music fadeout 6
o "Well Sissel kept insisting on bringing you to the biggest and most expensive place in the city!"
o "He kept saying you deserved more than what a poor guy like him can give."

m "That's not true at all!"
m "Sissel's great just the way he is."

play music "cafe-music.mp3"
show owen grin nervous with dissolve
o "Hah,{w=.3} try convincing Sissel of that."
o "Gotta warn ya,{w=.3} fancy shmancy rich places like this tend to make him super self-conscious,"
o "Do try to make him more comfortable,{w=.3} yeah?"

show phillip annoyed at left with dissolve
p "Hey."
show owen grin 2 at right with dissolve
o "Oh Phillip!{w=.3} Did you win your fight with the waiter?"


"Phillip rolled his eyes and grabbed Owen by the hood of his sweater."
show phillip annoyed look with dissolve
p "This ain't your date.{w=.3} Let them mingle in peace."
"The pigeon perched on Phillip's shoulder chirped in agreement as he dragged Owen away."

play sound "surprise.mp3"
show owen grin nervous
show buffet behind owen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
o "W-wait!{w=.3} I haven't gotten to try the oysters yet!"

show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
hide phillip
hide owen 
with moveoutright

"I watched them disappear into the crowd,{w=.3} Owen's words still echoing in my mind."
m "Sissel's worrying too much…"
show sissel happy with dissolve
s "Yo,{w=.3} you called?"
m "Whoa!{w=.3} There you are!"
m "Did you get any cool food?"

show sissel indignant with dissolve
s "Eheh,{w=.3} nah not yet."
s "There's too many choices,{w=.3} I can't pick a single one!"
s "Plus all the labels are in some fancy cursive that I can barely read."
show sissel happy with dissolve
s "I just decided to grab the same of whatever you're getting.{w=.3} Has anything caught your eye yet?"

menu sissel_date_food:
    "Oyster noodle stir-fry":
        m "Well,{w=.3} we're at {i}Very Legal Seafoods,{/i}{w=.3} might as well try some seafood right?"
        m "The oyster stir-fry looks pretty good!"

        "I began shoveling heaps of food onto my plate in inappropriate and obscene proportions,{w=.3} earning looks of disgust from nearby customers."
        
        show sissel wtf with dissolve
        s "Damn,{w=.3} you must be hungry."
        m "Listen,{w=.3} this is an {i}all you can eat{/i} buffet and I'm not letting a single plate go to waste."
        m "Buffets ain't about grace,{w=.3} it's about {i}eating.{/i}"
        "More customers grimaced as I forked several oysters into my mouth as I continued shoveling stir-fry onto my plate."
        "There is no honor on this battlefield."

        "Sissel leaned over and caught a whiff of the sweet,{w=.3} buttery-garlic smell of the oysters and his mouth began to water."
        
        show sissel happy with dissolve
        s "That {i}does{/i} smell pretty good."
        m "It's pretty great,{w=.3} wanna try some?"
        
        
        "I grinned and gently held up a fork full of stir-fry up to Sissel's mouth."
        "He spluttered and flushed a bright shade of pink."
        
        show sissel indignant with dissolve
        s "I'm an adult,{w=.3} I don't need you to hand feed me!"
        s "Especially not {i}here.{/i}"

        "Sissel glanced anxiously at the crowd of customers surrounding us."
        "Most of them pretended not to see us,{w=.3} while others openly scoffed at us."
        
        m "Eh,{w=.3} who cares what they think?{w=.3} I'm having fun~"
        m "Plus,{w=.3} isn't this the kind of cute, romantic stuff people do during dates?"
        
        "Sissel paused,{w=.3} pondering my words for a moment before turning even more red."
        s "I-I mean,{w=.3} I'm open to it if you want me to--"
        m "Not gonna lie,{w=.3} it'd be super cute if you did."
        
        "I winked."
        "He gulped and stared at the fork I waved enticingly in front of him."
        "Sissel sighed,{w=.3} closed his eyes,{w=.3} and leaned forward."
        
        show sissel indignant at Position(xpos = .5, xanchor=.5, ypos=.6, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
        "His mouth closed around my fork rather intimately before he snatched the oyster and hastily retreated."
        "His eyes actively avoided me as he chewed his food in embarrassment."
        show sissel indignant at center with Dissolve(2.0):
            xzoom 1 yzoom 1
        s "Mmmmph…"
        
        show sissel happy with dissolve
        s "It's uh….{w=.3} pretty good."
        s "Tastes kinda tingly though."

        m "You are too damn {i}adorable.{/i}"
        
        show sissel indignant with dissolve
        s "This is embarrassing."
        "There was a smile on his as he scratched his head bashfully."
        "Sissel suddenly grimaced and scratched his neck a little harder,{w=.3} a mildly uncomfortable expression settling across his face."
        
        stop music fadeout 3
        show sissel nervous with dissolve
        s "Is it just me or is it getting warm in here?"
        m "Is that supposed to be another pick-up line?"
        s "N-no,{w=.3} it's just--"
        s "I'm feeling tingly all of a sudden…"
        
        
        "A growl of frustration escaped his throat as he pulled at his shirt and continued scratching."
        m "You're feeling tingly-?"
        "Realization suddenly dawned on me."
        
        
        play music "scheming.mp3"
        m "Wait,{w=.3} are you allergic to oysters?"
        "Sissel's neck was red with hives and scratch marks.{w=.3} His eyes widened with a mixture of panic and embarrassment."
        
        play sound "surprise.mp3"
        show buffet behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        show sissel surprised
        s "I-I don't know!{w=.3} I've never eaten oysters before!"


        "One of the restaurant patrons behind us let out a haughty laugh."
        "Customer" "Oh dear,{w=.3} it looks like our high class food is disagreeing with you."
        "Customer" "Perhaps you should go to a restaurant at your calibur instead?"

        m "Oh {i}{b}shut up.{/b}{/i}"
        "I knocked the patron aside and hastily pulled Sissel to a chair."
        "His face was beginning to swell like puff chipmunk cheeks while he tried to hide himself in embarrassment."
        
        show sissel nervous with dissolve
        s "U-ugh,{w=.3} I look awful."
        s "T-this wasn't how the date was supposed to go--"
        s "I-I'm making us look like idiots--"

        m "Nevermind the date!"
        m "Can you still breathe properly?{w=.3} Should I call the ambulance for you?"

        "Sissel's eyes,{w=.3} which were already partially hidden behind his swollen eyelids,{w=.3} widened in even further panic."
        
        stop music fadeout 3
        play sound "surprise.mp3"
        show buffet behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        show sissel surprised
        s "I--{i}*wheeze*{/i}-- {w=.3}can't afford an ambulance!{w=.3} The med bills would ruin me!"
        s "S-sorry,{w=.3} I {i}--*gasp*--{/i}{w=.3} shouldn't have even asked you {i}--*wheeze*--{/i}"
        
        hide sissel with dissolve
        
        "Sissel hunched over,{w=.3} rasping harshly against his swollen throat."
        "{i}Shit shit shit--{/i}"
        "What should I do--?!"

        o "Stay calm,{w=.3} stay calm,{w=.3} I've got this--"
        "A small sense of relief washed over me at the sight of Owen,{w=.3} Phillip,{w=.3} and Jinny shoving their way through the crowd."
        
        show owen frown with dissolve
        o "I've got an Epipen,{w=.3} this should keep the swelling around his windpipe clear for now--"
        o "Here,{w=.3} roll up your pant leg--"

        "I helped lift Sissel's leg and comforted him through his wheezing as Owen pulled out a bright orange injector and pressed it firmly against his exposed thigh."
        o "Alright,{w=.3} one… two… three… {i}*click*{/i}"
        stop music fadeout 3
        scene black with Dissolve(2.0)

        "After administering the Epipen,{w=.3} Owen called an ambulance and dragged Sissel to the hospital despite his protests ({i}\"I'll cover the cost,{w=.3} just relax.\"{/i})"

        "I wanted to come along,{w=.3} but the EMTs wouldn\'t let me."
        "The rest of the night was spent anxiously waiting for news of how Sissel's doing."
        "This certainly wasn't how I expected the date to go--"
        
        play music "cafe-music.mp3" fadein 3
        play sound "euca-ringtone.mp3"
        pause(2.0)

        m "H-hello?!"
        o "Oh hey [charname].{w=.3} Just calling to let you know that Sissel's doing just fine."
        o "His face still looks like a flattened football but he's breathing and functioning again,{w=.3} so there's some good news."
        m "Whew,{w=.3} that's good to hear."
        "I paused."
        m "I-is there bad news too?"

        "Owen sighed and hesitated."
        o "Well uh…{w=.3} kinda."
        o "Remember what I said about Sissel being insecure in these kinda places?"
        o "Well he's convinced that he made a total embarrassment of you in front of all the people in the restaurant and basically feels like shit--{w=.3} especially since it happened during your first date."

        m "Who cares what the restaurant people think?!{w=.3} I'm just happy he's alright!"
        o "Yeah, {w=.3}\"not caring\" is easier said than done."
        o "Sissel's uh…{w=.3} basically avoiding you like the plague at the moment."
        o "He says you probably don't want anything to do with him anymore and he doesn't want to embarrass you further…"
        o "Sooooo yeah,{w=.3} that's the gist of  things so far!"
        m "What?!"
        m "That's not true at all!"
        m "Tell him to pick up the phone,{w=.3} I need to talk to him!"

        o "I totally would,{w=.3} but Sis is being a little hysterical at the moment."
        o "You know how he gets."

        "The image of Sissel's stuttering and panicking face flashed in my mind."
        m "Y-yeah…"
        o "I think it's best we let him cool off and relax for a bit before you talk to him again."
        o "I'll call you if anything comes up."
        stop music fadeout 4
        "*click*"

        "I stared at my phone for several long moments before heaving a long sigh."
        "This couldn't have gone worse."

        u "You're just being dramatic."
        
        play sound "ghost.mp3" 
        show halley neutral with Dissolve(2.0)

        u "Just talk to the guy after a few days."
        u "Everything should be fine."

        m "But we still gotta get him to listen to Hershel's confession!"
        m "And he's definitely not gonna take it well when he's frazzled like this--"
        m "Plus,{w=.3} our date night's ruined!"

        u "You sure have your priorities set."

        "I buried my face in my hands and sighed for several long moments."
        "And then I looked up at Halley."
        "I stared."

        u "....................?"
        u "What are you staring at--"
        play music "scheming.mp3"
        "She suddenly looked deadpanned."
        u "No."
        u "No, no, {i}no.{/i}"

        m "But you've done it before!"
        u "I am not turning back time for you to redo your fucking {i}date night.{/i}"
        u "Do you have any idea what the cost--"
        m "Come on Halley,{w=.3} think of the greater good!"

        m "We have to keep Sissel's confidence up if we want him to make it through this whole mess!"
        m "We can't give up now!"

        u "This is the {i}stupidest{/i} nonsense I have ever heard."
        m "You know it's true though!"

        u "It is not--!"
        "Halley opened her mouth,{w=.3} halted mid-thought,{w=.3} and reluctantly closed it."

        u "You…."
        m "Please…?"
        "I gave her my best puppy-dog eyes."
        "She looked at me with even more disgust."

        u "{i}Fine{/i}." 
        u "Just this once."
        u "You better not be wasting our time--"
        
        hide halley with dissolve
        "Halley suddenly grabbed me by the collar and {i}yanked.{/i}"
        stop music fadeout 4
        play sound "glass-break.mp3"

        "My face smashed into the fracturing opening of the clockwork world with an indignant {i}CRACK{/i} and I instantly blacked out."


        scene white with Dissolve(2.0)

        "Falling….."
        "Falling……………."
        "W-where am I again--?"
        
        play sound "slam.wav"
        scene buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        play music "cafe-music.mp3" 
        
        "{i}{b}{size=+10}THUD!!!{/size}{/b}{/i}"

        m "Ooof--!"
        
        show sissel surprised with dissolve
        s "Oh geez [charname],{w=.3} you keep falling on your face days."
        s "Are you alright?"

        m "Y-yeah,{w=.3} I'm fine!"
        m "W-what were we doing again?"
        
        show sissel indignant with dissolve
        s "Uh,{w=.3} we were grabbing food from the buffet."
        s "Are you sure you don't wanna sit down and grab a glass of water or something?"
        m "I'm fine I'm fine!"
        m "A-anyway,{w=.3} time to choose what to eat--"

        jump sissel_date_food
    "Caviar":
        m "Since it's a fancy restaurant,{w=.3} we might as well try the fanciest thing they've got,{w=.3} right?"
        s "You mean that weird bubbly stuff?"
        m "It's {i}caviar,{/i} it's like THE fanciest thing among fancy things!"
        "Sissel poked the container of caviar at the buffet table suspiciously."
        s "It looks kinda weird, honestly.{w=.3} But might as well try some new things while we're here."

        scene black with Dissolve(2.0)
        scene restaurant interior with Dissolve(2.0)
        
        show sissel nervous with dissolve
        "Sissel and I grimaced and simultaneously put our spoons down,{w=.3} most of our food remaining untouched."
        s "This uh….{w=.3} tastes like……."
        m "Stale jizz."
        "I poked the caviar with my spoon.{w=.3} The little bubbles burst with a satisfying {i}pop!{/i}"

        "Sissel flushed pink."
        show sissel wtf blush with dissolve
        s "How do you know what that tastes like--?"
        "I gave him a wink.{w=.3} The red on Sissel's face spread all the way up to his ears."

        m "I can give you a demonstration later tonight if you'd like~"
        show sissel surprised with dissolve
        s "W-we s-s-should probably get some more food first!"
        s "Y-you know,{w=.3} real food!{w=.3} Since you don't like this stuff and whatnot--"
        m "Yeah,{w=.3} it does taste pretty bad."
        "Sissel's ears drooped a little."
        
        show sissel nervous with dissolve
        s "Y-yeah,{w=.3} I probably should have asked what kinda food you liked first before bringing you on a date--"
        m "Hey now,{w=.3} just because the caviar tastes like wet socks doesn't mean I'm not having a good time."
        m "They're fun to squish.{w=.3} Like bubble wrap."

        "Another ball of caviar burst under my spoon with a {i}pop!{/i}"
        "A restaurant patron sitting behind us suddenly scoffed loudly."
        "I glanced at her tiredly.{w=.3} Her oversized hat and puffy dress loomed over us threateningly,{w=.3} like an over-inflated pufferfish caught in a net of seaweed."
        "In hindsight,{w=.3} this was a rather fitting sight at {i}Very Legal Seafoods.{/i}"

        "Patron" "Of course an uncouth peasant in rags wouldn't recognize true finery when they see it."

        s "O-oh,{w=.3} sorry, we didn't mean any offence--"
        "Patron" "Why did you even come to this establishment if it's so obviously out of your league?"
        "Sissel's face flushed and he sank deeper into his seat,{w=.3} suddenly fascinated by the candles."

        "Patron" "Ohoh, that's much more befitting behavior for you--"
        
        play music "scheming.mp3"
        hide sissel with dissolve
        m "Yo pufferfish lady,{w=.3} did you know it costs $0 to shut your trap?"
        m "My boy is perfect and you can shove your finery up your ass.{w=.3} Maybe pull your head out while you're there."

        "The patron gaped at me with an utterly scandalized expression."
        
        show sissel surprised with dissolve
        s "{size=-8}H-hey,{w=.3} maybe you shouldn't mess with the rich folks around here--"

        "The pufferfish patron with red with fury."
        "She turned towards the front desk,{w=.3} no doubt ready to complain to the restaurant staff."

        "Without thinking,{w=.3} I grabbed the straw from my ridiculous coffee drink and spitballed a piece of caviar with all my strength."
        
        stop music 
        play sound "surprise.mp3"
        show restaurant interior at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        "The wad of caviar sailed across the restaurant with master precision and hucks right into the pufferfish lady's throat."
        
        play music "wacky.mp3"
        "Sissel stared in shock as the patron fell to the floor,{w=.3} gagging and choking like a flopping landlocked fish."

        m "Oh dear,{w=.3} it seems like the fancy caviar is disagreeing with our good friend here."
        m "Might one of you waiters escort her away to some medical professionals?"

        "I realized my attempt at fancy-speak must have sounded like shit when Sissel started cackling hysterically."
        
        show sissel happy with dissolve
        s "What's with the accent all of a sudden?"
        m "'Tis how prim and proper folk speak,{w=.3} is it not?"
        m "Forgive me,{w=.3} I am not very fluent in asshole."
        
        s "You sound like you've got a frog stuck in your throat."
        
        play sound "surprise.mp3"
        show restaurant interior behind sissel at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
        "Patron" "{i}*HACK* *COUGH* C-call the ambul-- *COUGH*"
        
        show sissel wtf with dissolve
        s "Nevermind, {w=.3}she sounds worse."
        s "S-shouldn't we call for help?{w=.3} It'd be a bummer if you got arrested for murder on our first date."

        m "I guess…"
        m "Wanna grab some more food while we're at it?"
        m "This caviar is fun,{w=.3} but not really filling."
        show sissel happy with dissolve
        s "Sounds good,{w=.3} I'm still pretty hungry."
        hide sissel with dissolve

        "I glowered over the pufferfish lady hauntingly as we got up from our table."
        m "{i}{b}Being rich has made you weak.{/b}{/i}"
        
        show sissel wtf with dissolve
        s "[charname],{w=.3} please stop harassing the rich."

        m "No promises."

stop music fadeout 3
scene black with Dissolve(3.0)
scene restaurant exterior with Dissolve(2.0)
$ renpy.pause(2.0, hard='True')

play sound "ghost.mp3"
show halley neutral with Dissolve(2.0)

"The night air outside {i}Very Legal Seafoods{/i} wafted over the streets with a comfortable chill."
"Halley stood outside the entrance,{w=.3} staring vacantly at the stars as the minutes slowly ticked by."

play music "meloncholy.mp3"
"She sighed and took a seat on the sidewalk."
"There was probably no need to stand watch."
"The Remnant was shredded to pieces yesterday,{w=.3} it was unlikely to cause them any trouble tonight."
"No…"
"Perhaps she just didn't want to sit and watch Jinny and her friends goofing off on their little date."
"The sight of everyone laughing together…{w=.3} Halley felt the gears in her mechanical heart grind uncomfortably in her chest."
"There was a time when she was by Jinny's side like they were,{w=.3} laughing and…{w=.3} feeling the bubbly warmth of joy thumbing in her chest."

"Now there was only a dull metallic chill."

"Halley sighed again."
"One day,{w=.3} this repeating nightmare will end."
"And her days of joy with Jinny will be reality again…"

play sound "laugh2.mp3"
play music "snowdrop.mp3"

"A gurgling laugh suddenly cut into the night."
"Halley was instantly on her feet and alert."

u "Where--?"
u "Oh {i}you have got to be joking--{/i}"

show halley at left with dissolve
play sound "laugh3.mp3"
show remnant ripped at right with Dissolve(2.0)

"The disembodied head of the Remnant dragged itself down the street towards her."
"There were still raw tears in its skull,{w=.3} which was barely attached to its neck and stubble of a torso."
"Still,{w=.3} it cackled maniacally as it dragged itself across the ground with its chin."
u "It's been barely a day!{w=.3} How do you regenerate so quickly?!"

"The Remnant merely laughed from its pathetic position on the ground."
rr "You can't change the events of time that easily."
rr "The daffodil will {i}{b}burn{/b}{/i},{w=.3} just as before!"
rr "This night will be cursed hence!"
rr "There is nothing you can do to change it--"

u "...................."
u "You know,{w=.3} I'd be more intimidated if you weren't basically a talking soccer ball crawling on the ground."

hide halley with moveoutleft
rr "Silly words won't help you this time--"
show halley neutral at right with moveinleft
play music "scheming.mp3" 
play sound "slam.wav"
show restaurant exterior at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
hide remnant with easeoutright
play sound "scream.mp3"

"Halley's foot connected with the Remnant's face with a satisfying {i}{b}CRUNCH!!{/b}{/i}."
"A small content smile spread across Halley's face as she watched its head sail into the night sky,{w=.3} over the distant treeline,{w=.3} and finally out of sight."

"A few more moments passed before the Remnant's screaming abruptly stopped with a soft \"thud!\""
"Halley dusted herself off sighed."
"Ah,{w=.3} finally."
stop music fadeout 3
"Peace and quiet."

j "My my,{w=.3} if I didn't know any better,{w=.3} I'd think you got your sense of humor back."
"The world seemed to slow to a halt."
"Halley turned around to see Jinny stroll out of the restaurant with a wry laugh and a root beer float in hand."

show halley at left with dissolve
play music "moonheart-guitar.mp3" 
show jinny neutral at right with Dissolve(2.0)
u "Jinny…."
u "......You can see me again?"

j "Something about dying over and over again really jogs my memory."

"Jinny shrugged and took a sip of her root beer."
j "Anyway,{w=.3} how are you holding up?"

"Halley swallowed the lump in her throat and stared at her wisher for several long moments."
u "I…."
u "I'm still here."
u "Still failing."

u "And you're still here too."
"Halley buried her face in her hands."
"She wasn't supposed to be {i}feeling{/i} anything, damnit!"

"Jinny sighed and pulled a paper bag out of her jacket."
j "I've got some of that free bread from the restaurant."
j "You want any?"

u "Will you please take this seriously?!"
u "You're going to die {i}again!{/i}"

j "Hey,{w=.3} it ain't all bad."
j "I got to eat at a 5-star restaurant this time around."

"Halley pulled at her own hair in frustration."

"She was always like this,{w=.3} {i}every damn time.{/i}"
"Jinny took another sip of her soda and sat down next to Halley on the sidewalk."
j "..........hey."
j "........why didn't you do anything to help [charname] in the previous timeline?"

"Halley growled."
u "You know why."
j "Because you like being uptight?"
u "{i}I'm keeping you alive.{/i}"
u "Every action I take as a wish reduces what little time you have left."
u "I shouldn't have even fought the Remnant yesterday,{w=.3} my transformation easily took off a good chunk of your lifespan--"

j "If you didn't step in,{w=.3} things would have gone horribly wrong,{w=.3} just like last time."
j "You did the right thing."
u "Even at your expense?"
j "Yes."

"Halley fell quiet."
"The night air was heavy and silent while Jinny cheerfully sipped on her soda."

j "So,{w=.3} what are you gonna do tonight?"
u "...?"
j "The Remnant was just here,{w=.3} wasn't he?"
j "He said he \"cursed\" this night.{w=.3} Something bad is gonna happen,{w=.3} isn't it?"

u "........."
u "......yeah."
u "\"The daffodil will burn.\""
"Halley let out a frustrated sigh."
u "This is why I hate prophecy-type wishes."
u "Once they say something will happen,{w=.3} there's not much I can do to change things."

"Jinny finished her soda and shrugged."
j "You know what's fun about prophecies?{w=.3} They're like dumb fortune cookies."
j "You can interpret them however you want and no matter what happens,{w=.3} they'll {i}still{/i} somehow make sense."

j "Even horrible endings can have some upsides too,{w=.3} right?"
j "Everyone dies at some point,{w=.3} but life's still worth living."

"She gave Halley a friendly slap on the back before turning to stroll back inside the restaurant."
j "Try and have fun with it,{w=.3} will ya?" 

hide jinny with Dissolve(2.0)
show halley at center with dissolve
"Halley watched her retreating back until it disappeared into the shining doors of the luxury restaurant."
"Her gaze rose up to stare at the extravagant facade of {i}Very Legal Seafoods.{/i}"
"\"Have fun with it,\"{w=.3} huh?"
"A small idea began forming in her mind…"
"The constant {i}tick...{w=.3} tick...{w=.3} tick...{/i} inside her chest suddenly sped up and Halley almost laughed."

"She supposed her sense of humor might be coming back after all."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "calm-guitar.mp3"
scene buffet with Dissolve(2.0)

"At some point Sissel and I got separated while perusing the sea of buffet tables again."
"Despite my attempts to fully enjoy my night,{w=.3} the longer I stayed at this restaurant, the shadier the place felt."
"There were ants crawling underneath the tables,{w=.3} the food looked just {i}slightly{/i} too old to be healthy,{w=.3} not the mention the overworked waiters with massive eye bags."
"Poor things."

"Speaking of suspicious…"

show jinny neutral at right
show phillip annoyed at left
with Dissolve(2.0)

j "Yo [charname]!{w=.3} How's your date going?"
"Jinny and Phillip cheerfully shoved their way through the crowd of disgruntled restaurant patrons."
"Many shot disgusted looks at the fluffy pigeon perched on Phillip's shoulder."
"Phillip nonchalantly flipped them off while feeding his pigeon scraps from the buffet table."

m "Hey guys."
m "The date's….{w=.3}going."
m "Sissel's so sweet,{w=.3} but everyone at this restaurant's treating him like shit."
m "Plus,{w=.3} this whole place just feels very…….{w=.3}fishy."

j "Well yeah,{w=.3} it's a seafood restaurant."

play sound "badum-tiss.mp3"
show phillip smug 
"Phillip and Jinny instantly exchanged high-fives."
"Ah, puns.{w=.3} You've achieved comedy."
"The pigeon on Phillip's shoulder squawked in disappointment."

show phillip annoyed look with dissolve
p "Well [charname]'s not wrong about the fishy part."
p "Owen and I got bored and started digging up some dirt on this restaurant."
p "Apparently it's owned by one of the Loreleis,{w=.3} one of Owen's distant layabout cousins."

p "He buys seafood from illegitimate sources for cheap and then pays off the health inspectors when they show up here."
j "Oh,{w=.3} that explains why I found a moth in my salad!"
m "That's not even seafood!{w=.3} That's just lettuce!"

p "Can't say I'm totally mad though."
show phillip smug with dissolve
p "I'd be more angry if he wasn't duping all the rich people into paying bank for cheap garbage."
show phillip serious with dissolve
p "But then again,{w=.3} it's the {i}Loreleis.{/i}"
p "Owen's probably the only one with semi-functional morals in that mess of a family."

m "Say,{w=.3} you and Owen seem to be getting along real well nowadays."
m "Should I expect to chaperone a date for you two anytime soon?"

"Phillip snorted in surprise."
show phillip surprised with dissolve
p "Me?{w=.3} And Owen?"

show phillip smile with dissolve
p "Well, I guess crazier things have happened.."
show phillip serious with dissolve
p "Nothing's going on between us,{w=.3} I've just been helping him with…{w=.3} family stuff lately."
show phillip smile with dissolve
p "We have grown pretty chummy though…"


show pigeon at center with dissolve
"Phillip pondered the idea absent-mindedly while handing a chunk of crab leg to his pigeon."
play sound "surprise.mp3"
show pigeon scream at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
"I watched in fascination as the bird choked it down,{w=.3} shell and all."
"What was this thing made of??"

hide pigeon with dissolve
j "ANYWAY,{w=.3} enough about Phillip!"
j "You got any plans for the rest of your date?"
j "You two look like you're having fun but I gotta admit,{w=.3} the mood's been feeling a bit down on Sissel's end."

play sound "surprise.mp3"
show buffet behind jinny at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
m "That's because the fucking restaurant's full of garbage people!"
m "God,{w=.3} I bet we'd have more fun if the two of us just spent the rest of the date tearing this place down!"

"Phillip nodded sagely in agreement."
p "There's nothing quite as cathartic as making rich people uncomfortable."
j "Don't you wanna grab some more food while you're here though--?"

play sound "siren.mp3"
"Jinny was interrupted by the sharp wail of an ambulance siren."
"The three of us stared as a team of EMTs hastily ushered one of the patrons out the door whilst yelling something about food poisoning."

show jinny wtf
show phillip no
with Dissolve(2.00)
j "...on second thought,{w=.3} maybe don't."

stop music fadeout 3
scene black with Dissolve(3.0)
play music "meloncholy.mp3" 
scene restaurant interior with Dissolve(2.0)

"It was starting to rain outside."
"The sound of heavy raindrops soon filled the restaurant as occasional flashes of thunder flittered across the night sky."
"The place was starting to feel dreary…{w=.3} And Sissel was still nowhere to be found."

"After some worried searching,{w=.3} I spotted Sissel standing off in a lonely corner of the restaurant."

show sissel upset with Dissolve(2.0)
"He was staring up at the ceiling,{w=.3} completely lost in thought."
"I anxiously hurried to his side."

m "Hey man,{w=.3} is everything alright?"
m "What are you looking at--?"

"I followed his gaze and stuttered to a halt."
m "..............{w=.3}is that a wasp nest on the ceiling?"

"There was,{w=.3} indeed,{w=.3} a wasp nest on the ceiling of {i}Very Legal Seafoods{/i},{w=.3} and a surprisingly large one at that."
"Now that we were further away from the low hum of the buffet tables,{w=.3} I could clearly hear the sharp buzz of angry paper wasps."
"How did nobody at the restaurant notice this?!"

"I let out an impressed whistle."

m "Damn,{w=.3} this place is a disaster."
"Sissel drooped his head almost shamefully."

s "Yeah….."
show sissel nervous with dissolve
s "Hey listen…{w=.3} sorry for how shitty the night's been."

m "H-huh? {w=.3}What are you talking about?"

show sissel annoyed with dissolve
s "Basically everything!"
show sissel upset with dissolve
s "I thought I'd impress you with all this fancy stuff,{w=.3} but all I've done is bring you to a crap restaurant filled with awkward rich people and shitty food."
s "We were gonna have a nice night together but nothing's been going right...."
"He sighed and slumped down on a nearby chair."

s "I…{w=.3} I've been wanting to ask you out for a while now,{w=.3} but never really got the confidence."
s "There's just not much impressive about me,{w=.3} you know?"

s "Yeah,{w=.3} I won a small culinary contest.{w=.3} {i}Big deal.{/i}"
s "I was too chicken to ask you out like a normal person."
s "I'm too poor to take you to fun places without help,{w=.3} I'll probably never get a big fancy job like {i}these{/i} guys--"

"Sissel waved a hand towards the myriad of handsomely dressed men and women in the restaurant."
"He turned towards me,{w=.3} a mixture of confusion and bitterness swimming across his face."

show sissel bittersweet with dissolve
s "I've got nothing,{w=.3} to be honest."
s "I'm not worth {i}this.{/i}"
s "What do you even see in me?"

"I stood by Sissel's side in a still silence for several moments."
"He couldn't meet my gaze,{w=.3} his head slumped and staring at his feet dejectedly."

m ".......you know,{w=.3} you're probably right."

show sissel nervous with dissolve
s ".................."
m "This restaurant's kinda shit,{w=.3} your clothes are kinda old--"
m "--and you're probably never gonna be rich enough to be my sugar daddy--"
s "H-hey now--"

play music "little_something-slow.mp3" 
m "Didn't stop me from having fun with you tonight."
m "I've been having a great time."

"Sissel's ears twitched and he slowly raised his head."
"I grinned and plopped down on the seat next to him."

m "You know what I like most about you Sissel?"
m "It's not money or fancy food,{w=.3} or you winning a big trophy."
m "It's despite life dealing you a bad hand again and again,{w=.3} you still work {i}so damn hard{/i} to move forward."
m "It's admirable really."

show sissel indignant with dissolve
"Sissel opened his mouth in protest but I quickly {i}booped{/i} him on the nose."

m "You keep saying that you're not worth this,{w=.3} but when I see you working so hard to improve your life--"
m "--caring so much that you'd take me to the fanciest restaurant in the city--"
m "--and even dressing up in whatever silly thing I suggested just to make me laugh…"

m "...I feel like the luckiest guy alive to be by your side,{w=.3} you know?"

"I grasped Sissel's hand and leaned forward,{w=.3} making sure he couldn't look away from me."
"With a big goofy smile on my face,{w=.3} I pressed our foreheads together with a laugh."

m "You're worth everything to me,{w=.3} Sissel."
m "Don't ever doubt it."

"Sissel's eyes widened."
"He stuttered for a moment before smiling at me bashfully."

show sissel happy with dissolve
s "Y-you really mean it?"
s "....T-thanks,{w=.3} [charname]."
s "H-honestly,{w=.3} I-I wanted to say the same thing to you for so long......"
s "So much shit has been happening in my life,{w=.3} but you've always been by my side supporting me."
s "I was always afraid there was nothing about me worth supporting..."
s "B-but being around you makes me feel......{w=.3} braver."

"He scratched his head and blushed."
s "Yeah,{w=.3} I know that sounded fucking cheesy but--"

show sissel smile with dissolve
s "You make me feel braver.{w=.3} Brave enough to just be {i}me.{/i}"
s "Like someone worth {i}{b}being.{/b}{/i}"

"He let out a shy laugh."
s "I guess I've been to scared to embrace it until now."
"He leaned forward and pulled me into a tight,{w=.3} warm hug."

"We stood there for several long minutes,{w=.3} just embracing each other's presence,{w=.3} wide smiles beaming on our faces."

"After a moment,{w=.3} Sissel let go and glanced at the clock excitedly."

stop music fadeout 5
show sissel happy with dissolve
s "Well the night's still young."
s "You wanna ditch this lame place and go somewhere else?"
s "Let's restarted this date in a more honest way and do things we both love!"

m "I'd love to!"
m "But…"

"I gave Sissel a sly grin."
m "But first,{w=.3} I wanna get kicked out of here in a spectacular fashion."
s "H-huh?"

"I pulled out a large chunk of free bread from my pocket while eyeing the wasp nest."
play music "scheming.mp3" 
m "How good is your throwing arm?"
show sissel surprised with dissolve
"Sissel gaped at me in utter disbelief."

show sissel wtf with dissolve
s "You're not serious, are you?"
m "Dude,{w=.3} listen."
m "Every single goddamn waiter,{w=.3} staff, {w=.3}and customer at this place has been an unspeakable asshole to you and I've had it."
m "Tonight,{w=.3} {i}Very Legal Seafoods{/i} is going {i}{b}DOWN.{/b}{/i}"

"Sissel glanced between me and the buzzing wasp nest,{w=.3} clearly tempted by the thought of sweet revenge."

show sissel happy with dissolve
s "We're gonna get in so much trouble if we get caught…"
m "It'll make one hell of a first date."

s "I'd feel kinda bad for everyone here though--"
"He paused,{w=.3} as though replaying all the events of tonight through his head."
"All the snide remarks,{w=.3} the upturned noses,{w=.3} the pompous sneers…"

show sissel upset with dissolve
s "--on second thought,{w=.3} this place kinda deserves it."
stop music fadeout 2
"And then Sissel chucked the bread at the ceiling as hard as he could."
"The effect was immediate."

play sound "slam.wav"
hide sissel
show restaurant interior at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)

play music "batty.mp3"
"The bread roll smacked the hive with an aggressive {i}{size=+10}THWACK!!{/size}{/i},{w=.3} smashing it instantly."

"Bits of hive innards showered the dessert table where several well-dressed customers were poking about."
"Screams and clouds of angry wasps filled the restaurant as all the patrons shrieked and scrambled over each other in panic."

play sound "surprise.mp3"
show restaurant interior at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
"Customer" "{size=+10}{i}THERE ARE BEES IN MY HAIR!!!!{/i}{/size}"

m "They're wasps, you uncultured swine."
"They apparently couldn't hear me over the ruckus of fleeing customers and clattering of silverware as half the restaurant's tables were overturned in a customer stampede."
"Serves them right."
"I grabbed Sissel's hand,{w=.3} the two of us exchanging mischievous grins as we discreetly scooted towards the exit."
"I could see Phillip, Owen, and Jinny watching us from a distance in disbelief."
"The three of them quickly scrambled after us towards the exit,{w=.3} narrowly dodging the stampede of screaming and wasp-stung customers."

show buffet with Dissolve(2.0)
"At this point,{w=.3} the dining area was a panic zone of shrieking patrons and scattered food."
"Several patrons slipped on the food splattered across the floor,{w=.3} which further fueled the ruckus."

"The restaurant staff did their best to calm the people down,{w=.3} but to no avail."

play sound "surprise.mp3"
show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
"Staff" "Sirs!{w=.3} Ma'ams!"
"Staff" "Please remain calm,{w=.3} they are just bees!"
"Staff" "They're quite friendly so long as you don't swat--"

"Wasps."
"They were wasps."
"And unlike bees,{w=.3} wasps were infernal creatures who do not understand the concept of mercy."

"Any sense of order has collapsed as customers and staff alike shrieked and scrambled toward the exit like headless chickens while the cloud of angry wasps chased after them in hot pursuit."
"Despite the mayhem,{w=.3} Sissel and I couldn't help but laugh at the once prim and proper guests running for their lives."

"Speaking of which,{w=.3} we should probably get out of here."
"We were almost out the door when suddenly an anguished wail echoed through the building."

play sound "surprise.mp3"
show phillip surprised at left
show buffet behind phillip at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)

p "My daughter!{w=.3} I forgot my daughter!!"
o "You mean your bird--?"
play sound "surprise.mp3"
show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
p "{i}{size=+7}MY DAUGHTER!!{/size}{/i}"


hide phillip
hide owen
with Dissolve(2.0)
"I glanced over my shoulder."
"Phillip's pigeon was still at their table,{w=.3} neck-deep in a glass of red wine that it was using as a make-shift bird bath."

"A frantic staff member suddenly stepped on the tablecloth,{w=.3} pulling it down and causing the pigeon to tumble out of its drink with the grace of a wet sponge."

show pigeon with Dissolve(2.0)
"Pigeon" "{i}*hiccup*{/i}"
"Pigeon" "......................................................."

show pigeon screaming
play sound "surprise.mp3"
show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
"Pigeon" "{i}{b}{size=+10}*SQUAAAAAAAAAAAWWWK!!!{/size}{/b}{/i}"

"The pigeon puffed up with as much indignity a pigeon its size could muster."

play sound "surprise.mp3"
show buffet at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
hide pigeon with easeoutleft
"In a drunken rage,{w=.3} it flew over every single dining table in the restaurant and knocked over every candle it could find."
show pigeon screaming with easeinleft
pause(1)
hide pigeon with easeoutright
"The restaurant was suddenly alight a wall of flames that spilled over the dinning area like the ocean tide."

"One of the restaurant managers broke down in tears and let out an anguished cry."
show pigeon screaming with easeinright
"Satisfied with its work,{w=.3} the pigeon flapped towards the exit and landed boastfully on Phillip's shoulder."

show phillip smile at left 
show pigeon at center behind phillip
show owen neutral at right
with dissolve
p "Oh thank god you're safe Holly!"
"Pigeon" "{i}*hiccup*{w=.3} SQWUAAAK!!{/i}"

show owen grin nervous with dissolve
o "Your bird is a menace."
p "I know right?{w=.3} Isn't she great?"
o "She's probably gonna be charged with murder and get thrown in bird jail."

"Phillip shrugged."
show phillip annoyed with dissolve
p "It's fine,{w=.3} it's starting to rain outside anyway."
p "Nobody's gonna die."
show phillip annoyed look with dissolve
p "...................I think."

hide phillip
hide owen
hide pigeon
with Dissolve(2.0)
"At this point,{w=.3} all the restaurant guests and staff made the smart decision of evacuating the whole building."
"All that was left was a mass of angry wasps and sea of fire that spread across what remained of the dining hall."

"Sissel and I were already outside,{w=.3} staring at our handiwork through a window."
m "This first date went waaaaay better than I first thought."
m "I fucking love you, man."

show sissel happy with dissolve
s "Hehe,{w=.3} love you too [charname]~"
s "But uh…."
show sissel wtf with dissolve
s "The fire's spreading towards the liquor table."
m "Ooh yeah,{w=.3} we should probably move back a bit--"

stop music
play sound "thunder.mp3"
scene white with vpunch
play music "little_something-slow.mp3" fadein 3
"{i}{b}{size=+15}BOOOOOOM!!{/size}{/b}{/i}"

pause(3.0)
u "......................."
u ".................hehe."
u "\"Burn\" indeed."

scene restaurant burning with Dissolve(3.0)
$ renpy.pause(2.0, hard='True')

"That night,{w=.3} on our first date,{w=.3} Sissel and I put an end to {i}Very Legal Seafoods.{/i}"
"The fire danced against the night sky in a romantic glow as ashes and embers of the ruined restaurant slowly drifted down to earth."
"Sissel and I fled the building safely along with the rest of the customers,{w=.3} laughing gleefully the entire way."

"Nothing else in the world seemed to matter anymore."
"No judgement,{w=.3} no expectations,{w=.3} and especially not that accursed restaurant."
"It was just the two of us having the time of our lives."

"A clap of thunder shook the air as rain fell from the sky,{w=.3} soaking the two of us in a wet embrace."
"My hands were still firmly clasped in Sissel's as I turned to stare at him,{w=.3} my heart skipping a beat."
stop music fadeout 2
show sissel happy with Dissolve(2.0)
"Sissel stared back with a silly grin on his face."
"Suddenly,{w=.3} he pulled me close to him as he leaned over me,{w=.3} his face soft with a fond look."


play music "little-something-vocals.mp3" fadein 8
scene sissel_kiss1 with Dissolve(3.0)
$ renpy.pause(1.0, hard='True')
m "So….{w=.3} that was one hell of a first date,{w=.3} huh?"
m  "I had a blast,{w=.3} thanks for bringing me out here Sis~"
s "O-of course! {w=.3} I'm always happy to be with you, [charname]..."

"Sissel let out a shy laugh before leaning closer to me."
s "But you know…{w=.3} there's still a little something we can do to make it even more romantic."
s "And a little something I still need to say to you."
m "Haha,{w=.3} smooth~"
m "I think I know what you're getting at."
"I chuckled and pulled Sissel a little closer."

"The two of us simply stared at each other for a solid minute,{w=.3} too shy to make the first move."
"There was a long pause before Sissel laughed and finally pulled me closer to his chest."
s "..........hey [charname]?"
s "...I love you."

scene sissel_kiss2 with Dissolve(5.0)
$ renpy.pause(3.0, hard='True')
"Sissel blushed a bright pink before leaning forward and planting a light kiss on my lips as {i}Very Legal Seafoods{/i} burned to the ground behind us."
"I leaned into his kiss,{w=.3} blind to the embers and rain that fell from the sky around us,{w=.3} focusing only on the wonderful man in front of me."

"This was truly the most beautiful night."
"Fire and all."

scene restaurant burning with Dissolve(2.0)

show sissel happy with Dissolve(2.0)

"The two of us broke out of our kiss,{w=.3} breathlessly staring at each other before breaking out in hearty laughter."
s "......................."

s "That....{w=.3} that felt really nice."
m "Hehe,{w=.3} you're too darn cute."

scene black with dissolve
scene restaurant burning with dissolve

show phillip smile at farleft
show owen grin 3 at center
show jinny neutral at farright
with Dissolve(2.0)
$ renpy.pause(1.0, hard='True')

"Meanwhile,{w=.3} Jinny, Phillip, and Owen watched us from a distance,{w=.3} a satisfied smile settling across their faces."
j "Hehe,{w=.3} look at the two of them~"
j "Looks like Sissel's finally starting to grow a healthier sense of self-worth."
j "All thanks to [charname]."
j "Overall,{w=.3} I'd say we chaperones did a pretty good job tonight!"

show phillip annoyed with dissolve
p "Jinny.{w=.3} Everything's on fire."
show owen grin 2 with dissolve
o "Eh,{w=.3} it's a restaurant owned by my family."
o "The damn thing deserves to go down."
show owen grin 3 with dissolve
o "Plus,{w=.3} nobody died! {w=.3} That's a pretty good strong positive!"
show phillip smile with dissolve

p "Fine fine,{w=.3} I guess the night went pretty well,{w=.3} all things considered."
p "I don't think I've ever seen Sissel or [charname] so happy before."
"Phillip glanced at me and Sissel in the distance with a smile before pulling Jinny and Owen away."
p "Let's leave those two lovebirds alone for now.{w=.3} They deserve their privacy."

hide phillip
hide owen
hide jinny
with Dissolve(1.0)

scene black with dissolve
scene restaurant burning with dissolve
show sissel happy with dissolve
$ renpy.pause(1.0, hard='True')
"I wasn't sure how long Sissel and I stood together,{w=.3} simply melting into each other's embrace."
"All I knew was that he felt warm and safe,{w=.3} and everything felt {i}right.{/i}"
"Sissel laughed and pulled me into a closer hug,{w=.3} nuzzling my neck fondly."
s "...so uh….{w=.3} we didn't actually eat much during that date,{w=.3} did we?"
s "Wanna drop by the cafe and grab a bite to eat?"
s "And then maybe we can do some more fun stuff together~"

"I grinned and gave Sissel a light peck on the cheek."
"We both blushed and laughed."
m "That sounds like a great way to end the night."
m "Lead the way Sis~"





jump credits
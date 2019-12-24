label day10_owen_rewrite:
$ persistent.current_route = "default"
"{b}Day 10:{/b}{w=.5} A Family of Lies"

scene black with Dissolve(3.0)
play music "wave-piano.wav" fadein 2



"Sleep was peaceful.{w=.3} I was dreaming of a flock of birds soaring through the warm summer sky......."
e "{size=-10}[charname],{w=.3} wake up.{/size}"
m "Mmmm.......{w=.3}five more minutes......."
e "{size=-10}You literally said that ten minutes ago.{/size}"
e "Aw c'mon,{w=.3} get up!{w=.3} Didn't you say you had snooping to do?"

"Suddenly I felt a pair of ice-cold fingers pinch around my nose and pull me off my warm,{w=.3} comfortable pillow."
scene derry house hallway with Dissolve(2.0)
"My eyes shot open to see Echo hovering uncomfortably close to my face."
"It felt like I was pressing my cheeks against a very cold window."

play sound "ghost.mp3"
show echo shattered with Dissolve(2.0)
e "You are possibly the laziest person I have ever met."
"I yawned heavily and rubbed my eyes."
m "You're waking me at the dead of night,{w=.3} did you expect me to jump out of bed with the sun shining out of my ass?"

e "You were the one who was so excited about snooping around the house at this hour.{w=.3} Don't blame the messenger, dude."
e "Now are we gonna do this or not?"
m "Alright alright,{w=.3} I'm getting up."

scene black with Dissolve(2.0)
scene derry house hallway with Dissolve(2.0)
"Another yawn stretched from my open mouth as I stumbled out into the hallway."
"I strained my ears and felt a wave of relief at the sound of Samuel snoring from the other room."
"Good,{w=.3} looks like we'll be able to explore uninterrupted."

play sound "ghost.mp3" 
show echo shattered with Dissolve(2.0)
e "So what's the plan,{w=.3} [charname]?"
e "Hope your planning skills are better than Owen's."

m "There's definitely something fishy about this house,{w=.3} and this family in general."
m "I'm going to snoop around a fair bit to see if I can dig up any information."
e "Is that all?"

"My footsteps were light as I made my way across the hall,{w=.3} doing my best to make as little noise as possible."
m "Phillip was right earlier today."
m "This kind of situation is way out of our league,{w=.3} but information is our best form of currency."

m "Plus,{w=.3} I'm curious why there's a wish haunting around this place."
m "Ghostly things like this don't exactly leave me alone until I take a poke at it."
"Echo rubbed his temples doubtfully."
e "Your planning skills suck worse than Owen's,{w=.3} but it's better than nothing I guess."
e "Where are you going to snoop around first?"

m "Well obviously the most important looking room around so......"
hide echo with dissolve
"I wriggled my finger down the hallway dramatically,{w=.3} peeking door to door."
m ".......{w=.3}how about this one?"

"I pointed at a particularly fancy-looking door."
"The heavy door frame was massive and lined with ornate carvings.{w=.3} The entire thing was built to be sturdy with handsome and expensive wood finish."
"A master bedroom?{w=.3} Or maybe even an office?"

m "Alright,{w=.3} let's see what we find-"
m "...................{p=.3}...........it's locked."
m "Great, now what?"

play sound "ghost.mp3" 
show echo shattered with Dissolve(2.0)
e "Leave this to me."
e "I may be falling apart,{w=.3} but cracking a simple lock shouldn't be a problem."

play sound "bump.mp3"
"Echo lightly tapped the lock,{w=.3} his eyes glowing brighter for a split second."
"A soft {i}click!{/i} later,{w=.3} the heavy door swung open."
m "Sweet,{w=.3} let's see what we have here......"

scene black with Dissolve(2.0)
stop music fadeout 3
scene crane room with Dissolve(3.0)
pause(.7)

"A gentle cool breeze caressed my cheek as I walked into the room,{w=.3} stunned by the sudden spectacle of colors."
"For a moment I forgot to breath."

play music "drifting.mp3" fadein 2
"This was...............{w=.3}beautiful."
"I stared wide-eyed at the hundreds upon hundreds of hand-folded paper cranes hanging throughout the room,{w=.3} each meticulously made with love and care."
"Someone obviously put a lot of time into making each bird perfectly."

"Each bird fluttered slightly as I walked past them,{w=.3} almost as though they were alive."
"I tore my eyes away from the colorful spectacle and took in the rest of the room."
"The walls were lined with ceiling-high expensive bookshelves,{w=.3} with a large desk sitting at the center."
"An eerily empty bed was situated at the end of the room.{w=.3} It felt rather uncomfortable to look at amongst the flock of soaring paper cranes....."

m "Is this a......{w=.3}bedroom?"
m "Maybe it belonged to Owen's mom."

"Owen's mom,{w=.3} who died from an illness."
"My throat felt dry as I slowly took in the sight of the hundreds of paper cranes Owen must have made to comfort his dying mother."
"The empty bed in the room looked cold and unused in a very long time....."

stop music fadeout 10
play sound "ghost.mp3" 
show echo shattered with Dissolve(2.0)
e "Hey [charname],{w=.3} you doing alright?"
"I nodded numbly."
play music "water-lily.mp3" fadein 5
m "Yeah,{w=.3} but I feel kinda shitty for intruding here."
e "That's a given when it comes to snooping into people's private lives."

m "I suppose..............."
"I shook my head furiously to clear my head of thoughts."
"We're here to get information,{w=.3} and we're going to need it."
"C'mon [charname], focus!"

hide echo with Dissolve(2.0)

"My eyes traveled from the large desk at the center of the room to the towering bookshelves around me."
"What should I look at first?"



menu owen_snoop_menu:
    "Bookshelves.":
        "Owen's mother must have been a big book lover.{w=.3} There's enough here to fill a library."
        "All the books here looked well-worn too and not just placed as decoration to make the homeowner look smart."
        "Hm.....{w=.3}I wonder where I should start looking?"
        menu owen_snoop_bookshelf:
            "Top Shelf":
                "I had to stand on a nearby stool to actually reach the top shelves."
                "They were packed with homeschooling textbooks and education guides.{w=.3} The practice workbooks were all fully completed with impressive marks."
                "There was a note stuck to the inside of the shelf that read:{w=.3} {i}\"Samuel,{w=.3} maybe we should move the books lower where Owen can actually reach them.\"{/i}"
                "It looks like Samuel wrote a reply on the bottom of the note: {w=.3}{i}\"I'll do it later!\"{/i}"
                "..................{w=.3}the books are still on the top shelf."
                jump owen_snoop_bookshelf
            "Middle Shelf":
                "I peered around the bookshelves curiously."
                "A copy of {i}\"Parenting for Dumbasses\"{/i} was shoved into one of the eye-level shelves."
                "There appears to be a copious amount of notes scribbled on the inside,{w=.3} and the book itself was chock full of sticky-notes."
                "One of them read:{w=.3} {i}\"The great Heather Adlai can face off against armed gunmen, but still can't hold a fucking baby properly.\"{/i}"
                "The note under it,{w=.3} written in incredibly neat and sophisticated cursive, read:{w=.3} {i}\"Shut up Graham.\"{/i}"
                "The rest of the book was littered with similar snide remarks from its readers."
                jump owen_snoop_bookshelf
            "Bottom Shelf":
                "Nearby,{w=.3} there were several psychological self-help guides scattered along the bottom shelf."
                "One in particular,{w=.3} {i}\"A Study on Empathy\"{/i},{w=.3} contained well-worn pages,{w=.3} as though it has been read and re-read countless times."
                jump owen_snoop_bookshelf
            "Exit Bookshelf":
                jump owen_snoop_menu
    "Desk":
        "The desk at the center of the room was covered in a thick layer of dust that has been undisturbed for years." 
        "Across the top of it were complicated-looking files and folders that I couldn't make heads or tails of."
        "I kinda felt like an archeologist trying to unearth fossils without disturbing anything."
        e "Find anything interesting yet?"
        m "I don't think so.{w=.3} Most of these files are written in such thick legal-jargon I can barely tell if it's actually English."
        m "Hm?"
        "I ducked under the desk and sighed."
        m "There's a kitchen knife taped under this desk too.{w=.3} Owen's family sure likes to take their \"precautions\" seriously."
        e "I mean,{w=.3} they apparently dealt with criminals fairly often.{w=.3} I don't blame them for being careful."
        
        m "Do you think they actually used any of these in a fight?"
        e "I don't really want to know...."
        
        "An idea flashed in my head.{w=.3} I carefully pulled the small knife out from its hiding place and set it on the desk."
        e "W-what are you doing?"
        m "I wonder if my camera's memory snapshot would work on this."
        e "You're going to try and dive into a memory?{w=.3} Right here?"
        e "You tend to pass out right after you take photos like this..."
        m "Well it's a good thing you're here to watch over my sleeping body while I'm gone."
        e "Just warning you,{w=.3} I might be tempted to draw on your face while you sleep."
        m "That's a price I'm willing to pay."
        
        "I clicked the switch on my camera to \"On\" and carefully pointed it at the knife laying on the desk."
        "My camera felt unusually heavy in my hands today...."
        m "Alright,{w=.3} here goes nothing."
        
        play sound "camera.wav"
        scene white with Dissolve(2.0)
        play music "noise.mp3"
        
        show photograph with Dissolve(1.5)
        pause(2.0)
        
        "I was falling."
        "People were talking.{w=.3} Footsteps."
        "Secrets were whispered from ear to ear in hushed voices."
        "Where am I?"
        "Who...................{w=.3}..........are..................??????"
        
        stop music 
        play music "tranquil.mp3" fadeout 7
        scene black with Dissolve(3.0)
        pause(1)
        "{i}\"Owen,{w=.3} go to the saferoom and stay there until we come get you.\"{/i}"
        "{i}\"Owen,{w=.3} there's no need to worry.{w=.3} Mum will take care of everything.\"{/i}"
        "{i}\"We need you to stay very quiet Owen.{w=.3} Shhhh,{w=.3} please.\"{/i}"
        
        "It had always been like this."
        "There'd be a crash at the door,{w=.3} the sound of broken glass echoing through the house."
        "Mum or Samuel would rush me to the saferoom,{w=.3} where the thick metal walls would keep me safe."
        "Safe from what?{w=.3} They never said."
        
        "I would wait and wonder."
        "Why is Samuel hurt again?{w=.3} Why is mum covered in red?{w=.3} Who keeps breaking into the house?"
        "I never got any answers.{p=.3} I got tired of waiting."
        
        "This time as mum and Samuel closed the saferoom door and rushed away,{w=.3} I dug out the key I had hidden in my pocket."
        "I'll just take a small peek.{w=.3} I had to know who keeps hurting my family."
        
        show derry house sepia with Dissolve(3.0)
        "I crept quietly down the hall towards the kitchen."
        "It sounded like uncle Graham and Samuel were outside with several other people.{w=.3} There where shouts and gunfire."
        play sound "glass-break.mp3" 
        "There was a heavy {i}CRASH!{/i} as another person broke through the kitchen window."
        "My heart was thumping heavily against my chest."
        "I took a deep breath,{w=.3} and peeked around the corner."
        
        show heather_fight1 at Position(xpos = 0, xanchor=.5, ypos= .9, yanchor=.5) with Dissolve(3.0)
        show heather_fight1 at Move((0, .9), (0, .7), 30,
                        xanchor=.5, yanchor=.5)
                    
        "Mum stood tall and unfazed,{w=.3} her head held high like an immovable statue."
        "The man who broke in snarled and pointed a gun at her.{w=.3} She stared at it with disinterest."
        
        he "The Lorelei family is quite persistent,{w=.3} aren't they?"
        he "You are...what?{w=.3} The 40th henchman sent to kill us?"
        "The gunman twitched,{w=.3} a bit unnerved by Heather Adlai's calm composure."
        "Gunman" "Just shut up and die, darling."
        
        "Heather sighed and rubbed her temple tiredly."
        he ".......I don't suppose I could convince you to leave us unharmed?"
        "The gunman actually laughed."
        stop music fadeout 3
        "Gunman" "The price on your head is enough to buy a country, darling."
        "Gunman" "I ain't leaving until that money is filling my pockets."
        
        show heather_fight1 at center with Dissolve(2.0):
            xzoom .5 yzoom .5
        pause(1)
        
        "Heather Adlai sighed heavily before raising a hand slowly above her head."
        play music "beastsonata.mp3" fadein 3
        he "I'd hate to disappoint you,{w=.3} but I don't plan on dying anytime soon."
        he "Now get out of my house."
        
        
        play sound "slam.wav" 
        show heather_fight2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
        pause(2)
        "Heather suddenly slammed her fist onto the kitchen table,{w=.3} sending a knife flying through the air."
        "Time seemed to slow as she took her first step forward."
        
        play sound "slam.wav"
        show heather_fight3 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
        pause(2)
        "Heather grabs the knife, her hair fluttering wildly behind her."
        "Her movements were swift with practiced precision."
        "The gunman stumbled backwards in surprise as she {i}{b}lunged{/b}{/i} at him with inhumane speed."
        
        play sound "gunshot.wav" 
        show heather_fight4 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
        pause(2)
        "He shot at her,{w=.3} but Heather side-stepped it with ease."
        "He struggles to aim again,{w=.3} but she was already too close."
        "Two more steps forward, as fluid as a dancer."
        "The gunman cocks his gun forward again,{w=.3} but now she's close enough to knock it away."
        "There wasn't a single moment of hesitation before she thrusts the knife straight into the man's throat."
        
        show heather_fight5 with Dissolve(3.0)
        pause(2)
        stop music fadeout 15
        "Red.{w=.3} The room was painted red."
        "Heather Adlai's stone facade remained unfaltered and unmoved as the man slumped to the ground,{w=.3} the blood of his throat slowly soaking into the carpet."
        "She tosses the knife into the kitchen sink and glared at the mess reproachfully."
        
        scene derry house sepia with Dissolve(2.0)
        "There was a {i}bang!{/i} as Samuel rushes back inside the kitchen,{w=.3} panting heavily."
        ss "I-I'm back!{w=.3} Is everyone alri-"
        "His jaw dropped at the growing pool on the kitchen floor."
        ss "Whoa,{w=.3} the hell happened here?"
        he "You and Graham missed one.{w=.3} He broke through the kitchen window."
        ss "S-sorry,{w=.3} we should have been more careful. {w=.3} We took care of the four outside though."
        he "It's fine,{w=.3} so long as everyone's safe."
        he "Let's hurry and clean up this mess.{w=.3} I don't want Owen to see any of this."
        
        "From the corner in the kitchen hallway,{w=.3} I sucked in a breath of shaky air and tip-toed quietly back towards the saferoom."
        "It will be a while before I stopped shaking."
        
        play sound "noise.mp3"
        scene photograph with Dissolve(1.5)
        scene black with Dissolve(3.0)
        stop music
        
        play music "water-lily.mp3" fadein 3
        scene crane room with Dissolve(3.0)
        
        "My eyes shot open as I suddenly gasped for air."
        "Echo floated above my head with a worried frown."
        play sound "ghost.mp3" 
        show echo shattered frown with Dissolve(2.0)
        
        e "You okay there [charname]?{w=.3} You've been out of it for like 20 minutes."
        m "I-I think I'm okay.{w=.3} J-just a bit shaken."
        "I wasn't sure what I expected,{w=.3} but it certainly wasn't.......{w=.3}{i}that.{/i}"
        e "What did you see?"
        "I pulled myself off the floor and tried to shake off the incoming headache."
        m "I saw Owen's mother fighting with the Lorelei's.{w=.3} Samuel and Owen's uncle was there too."
        m "It sounded like they did this pretty often."
        "My slowed breathing finally returned to normal, even pace.{w=.3} I rubbed my blurry eyes with exhaustion."
        m "I can't blame Owen for being frustrated with not knowing anything when things like {i}{b}this{/b}{/i} were happened to him every day."
        m "A-anyway,{w=.3} I think I'm fine now."
        m "Let's keep searching."
        hide echo with Dissolve(2.0)


        jump owen_snoop_menu
    "The Drawers":
        play music "meloncholy.mp3" fadein 5
        "Gingerly,{w=.3} I opened up one of the bigger drawers in the large desk sitting in the room."
        m "Hm?"
        e "What is it?"
        m "There's a little journal here.{w=.3} Looks like it's bounded by a lock though."
        "The journal was bounded in handsome leather and aged paper.{w=.3} It has the look of something heavy with history."
        m "Hey Echo,{w=.3} any chance you can unlock it for me?"
        e "What am I,{w=.3} your personal lockpicker now?"
        "With a sigh, Echo snapped his fingers melodramatically.{w=.3} The lock on the journal opened up with a sharp {i}click!{/i}"
        "Let's see what we have here........"
        menu owen_snoop_journal:
            "Entry #1":
                he "{s}Dear Diary-{/s}{p=.3}(no no,{w=.3} too juvenille)."
                he "{s}Hello{/s}{p=.3}(too dull)."
                he "Well fuck you too:"
                he "Apparently writing in a journal helps one mediate their thoughts."
                he "I'd schedule an appointment with my psychiatrist instead,{w=.3} but poor Dr Handson was found murdered in his office several days ago."
                he "Looks like the Loreleis finally caught up with him."
                he ".......I still believe keeping a journal is a major security risk,{w=.3} but Samuel insisted that I look after my mental wellbeing."
                he "Oh speaking of,{w=.3} I have officially hired Samuel Clark and Graham Belladona as my protectors today."
                he "The Aldai slaughter incident was only a few weeks ago,{w=.3} so it wouldn't hurt to stay on high alert."
                he "Samuel is famed for the skill of his craft,{w=.3} and takes care of any dangers swiftly."
                he "The way he almost worships me like a hero is rather tiring,{w=.3} but I am safe with Samuel protecting me."
                he "Graham on the other hand........."
                he "He still does not trust me.{w=.3} Probably never will."
                
                "There was a large gap on the page under this entry,{w=.3} as if Heather stopped writing for a little bit."
                he "PS:{w=.3} I finally got rid of Samuel's horrible \"punk\" haircut this afternoon."
                he "Graham held him down while I trimmed away that god-awful mohawk.{w=.3} Success!"
                he "I wish Samuel screamed a little less though.{w=.3} The neighbors called the cops on us."
                jump owen_snoop_journal
            "Entry #2":
                he "It still astounds and shocks me that I will be a mother soon."
                he "Me.{w=.3} Someone with as much blood on their hands as I should never be near children,{w=.3} but here I am."
                he "It scares me to wonder what kind of person my child will grow up to be,{w=.3} but one thing is certain:"
                he "I will raise and groom him to be free of the Lorelei and Adlai families' influences."
                he "He will grow up to be a kind and compassionate young man,{w=.3} someone who will use his heritage for the greater good and perhaps end the mess that is the two families."
                he "Someone his mother could never be."
                
                he "I've arranged our home on Derry Street so that my child would not encounter any information about the two families."
                he "I made it clear to dear Oleander that any attempts to contact my child will be met with retaliation."
                he "He will be born into an unforgiving world,{w=.3} but the least I can do is ensure he enjoys an untainted childhood."
                jump owen_snoop_journal
            "Entry #3":
                he "My child is due within a month or two,{w=.3} but we're still struggling to name him."
                he "I made it clear that {i}\"Samuel the 2nd\"{/i} is out of the question.{p=.3} Samuel was heartbroken."
                he "I suggested an older name like \"Fleamont\",{w=.3} but when I mentioned it Graham choked on his morning coffee and flipped me off."
                he "I guess that's also a bust."
                
                "There was a small sentence scribbled lightly on the bottom of the page:"
                he "PS:{w=.3} Oleander sent me a letter this afternoon and suggested \"Owen\".{w=.3} Interesting........"
                jump owen_snoop_journal
            "Entry #4":
                he "Babies are disgusting."
                he "Please stop crying."
                jump owen_snoop_journal
            "Entry #5":
                he "Graham sat me and Samuel down this afternoon to throughly demonstrate how to hold a baby."
                he "Owen is much cuter when he's not screaming at the top of his lungs."
                he "He also threw up on Graham a minute later.{w=.3} I've never been more proud."
                
                "Someone had interrupted the entry by scribbling under it in aggressive red ink:"
                "{i}\"Without me,{w=.3} this household would slide into the fucking ocean.{/i}\""
                he "Graham I swear to god if you interrupt one more time I'll fucking castrate you."
                "{i}\"'Fraid that ain't possible darling.{w=.3} Good try though.\"{/i}"
                jump owen_snoop_journal
            "Entry #6":
                he "Owen began teething today.{w=.3} Apparently babies have exceptionally strong jaws."
                he "We rushed Samuel to the hospital this afternoon to stitch up his finger."
                he "Owen looked very smug the whole time.{w=.3} Graham joked that he inherited his mother's ferocity."
                he "Hearing this saddens me somewhat."
                he "I was hoping he'd take after his father."
                jump owen_snoop_journal
            "Entry #7":
                he "Today was Owen's 10th birthday."
                he "Samuel bought him a motorcycle,{w=.3} which was a terrible idea in itself,{w=.3} but that is not the worst part."
                he "He searched through the entire city,{w=.3} pointed at the ugliest vehicle in existence,{w=.3} and said {i}\"I want that one.\"{/i}"
                he "This............{w=.3}{i}{b}thing.{/b}{/i}"
                he "It taunts me.{p=.3}That hideous shade of orange with clown-shoes yellow handles,{w=.3} it is proof that God has a sick sense of humor."
                he "I allowed Samuel and Owen to keep it,{w=.3} if only to hope that they crash it as soon as possible."
                
                he "PS:{p=.3}It has been a week."
                he "Samuel and Owen crashed the motorcycle into our neighbor's house.{w=.3} I rejoiced!"
                he "Nobody got hurt ( much.{w=.3} Samuel needed stitches again){w=.3} and that.........{w=.3}{i}{b}thing{/b}{/i} was completely crushed."
                he "Imagine my horror when I found it standing in our driveway this morning,{w=.3} fully repaired and threatening me with its existence."
                
                he "It turns out Graham had it fixed."
                he "{i}\"I liked it,{w=.3} it always managed to piss you off more than I ever could.\"{/i}"
                he "This man is going to be the death of me.{w=.3} At least Owen seems happy about it."
                jump owen_snoop_journal
            "Entry #8":
                he "Owen snuck out of the house this morning and we didn't find him until tonight."
                he "He is quite the adventurous fellow.{w=.3} I'd be proud if it didn't worry me so much."
                he "It's dangerous for him to wander out of the house with the Lorelei's still targeting us."
                he "Still,{w=.3} it's good to see him go out and make friends in the world."
                he "Graham found Owen playing with a small homeless boy and a sickly little girl outside the hospital this afternoon.{w=.3} They've become fast friends."
                he "Owen's begging me to let him go back and play with them."
                he "I was tempted to say yes,{w=.3} but Owen's safety takes priority."
                he "He was very disappointed."
                
                "There was a little more writing on the other side of this page."
                he "PS:{w=.3} Later today, Owen stole my credit card and attempted to pay for his new friends' hospital bills and school supplies."
                he "I pretended to not notice."
                jump owen_snoop_journal
            "Entry #9":
                stop music fadeout 10
                he "The Lorelei's attacks on our household have become increasingly frequent lately."
                he "Samuel and Graham have become exhausted in their constant vigilance.{w=.3} We've had Owen retreat to the safe room practically every day to ensure his safety."
                he "The Lorelei's are growing bolder,{w=.3} breaking into the house in broad daylight and armed to the teeth."
                he "I've managed to keep Owen in the dark about his heritage and situation,{w=.3} but he's grown frustrated with all the unanswered questions."
                he "I'm not sure how long we can keep this charade going."
                
                he "..............................."
                he "........................................................"
                play music "my-oath-to-you(slow).mp3" fadein 5
                
                he "..........{w=.3}it just hit me that I've been living with Owen, Samuel, and Graham for almost 12 years."
                he "12 years,{w=.3} with just the four of us."
                he "Growing up in the Adlai family was strange.{w=.3} I never had people to just sit down with at a dinner table and vent the day's frustrations to."
                he "I never had anyone to (attempt to) cook for,{w=.3} or knit sweaters for,{w=.3} or terrorize the neighbors with."
                he "We've fought together,{w=.3} laughed together,{w=.3} and.............it's been nice."
                he "Raising Owen with these two has been a privilege."
                he "Since the beginning, I did not once believe that this home would last forever.{w=.3} But....."
                he "When it is over,{w=.3} I'm going to miss this."
                he "I am going to miss this family."
                $ owen_snoop = "true"
                jump owen_snoop_journal
            "Stop reading":
                jump owen_snoop_menu
    "Paper Cranes" if owen_snoop == "true":
            "I glanced up at the paper cranes hanging around the room like a glittering cascade."
            "As we searched through the room,{w=.3} I had the sneaking suspicion they were almost watching our every move."
            "Each one glowed lightly when I turned towards them."
            m "H-hello?"
            m "Can you hear me?"
            
            play sound "leila.mp3"
            "Suddenly, the room was alive with hundreds of tiny,{w=.3} whispering voices."
            "Each paper crane spoke to the other in hushed voices, watching me intently."
            
            "Suddenly,{w=.3} one of the cranes broke off from its string and gently fluttered down onto the palm of my hand."
            "It looked fragile,{w=.3} like a stray wind could accidentally tear it beyond repair."
            
            play sound "ghost.mp3" 
            show echo shattered with Dissolve(2.0)
            e "Hm, they're trying to tell you something."
            e "They are saying that........{w=.3}they are the formless wish of Owen Lorelei."
            "Echo cocked his head to the side, {w=.3} as if listening intently to a silent speaker."
            e "They said to.........{w=.3}that their name is \"Leila.\""
            
            "I blinked at the tiny origami in my hands."
            m "Formless wish?"
            e "It means they don't have an actual body like I do."
            e "They exist as a formless entity within all these paper cranes."
            
            "The cranes in the room suddenly hissed angrily at Echo's appearance,{w=.3} their tiny bodies thrashing against their strings."
            "Echo laughed awkwardly and took a few steps backwards."
            e "Oh boy,{w=.3} they don't like the fact that I'm here."
            e "They want me to leave."
            
            m "What? Why?"
            "I glanced up at the overhanging origami with a frown."
            m "Hey guys,{w=.3} you can trust Echo here!{w=.3} He's a nice guy, I promise!"
            
            
            e "No no, it's fine.{w=.3} I don't blame them for being fidgety."
            e "To them, {w=.3}I uh....{w=.3}smell kinda bad."
            m "Well I think you smell fine and that you should {i}stay.{/i}"
            
            "The paper cranes' thrashing reluctantly died down as they turned their attention back to me."
            "Echo's ears twitched as more whispering hazed through the silence of the room."
            show echo shattered frown with dissolve
            e "They're saying that......{w=.3}they need your help."
            e "Leila says they want you to help grant Owen's wish."
            
            m "I want to help but I'm not even sure what Owen wished for....."
            
            play sound "leila.mp3" 
            
            "The origami birds fluttered lightly in reply."
            "Echo glanced up at them uneasily."
            
            e "A memory."
            e "They said they want to show you a memory.{w=.3} They want you to use your camera on them like you did earlier."
            
            m "You don't say?"           
            "The cascade of paper cranes rustled, as if in agreement."
            
            m "I get pretty tired when I do this,{w=.3} but I guess I can take another shot."
            
            hide echo with dissolve
            "I fiddled with the camera hanging from my neck and pointed it at the mass of paper in the room."
            "If it meanings helping Owen,{w=.3} another quick memory dive wouldn't hurt."
            "Here goes nothing."
            
            play sound "camera.wav"
            scene white with Dissolve(2.0)
            play music "noise.mp3"
            
            show photograph with Dissolve(1.5)
            pause(2.0)
            
            "Everyone was gone."
            "Questions clawed at the back of my mind. {w=.3}No answers came."
            "Secrets secrets secrets. {w=.3}What good are they when you're dead?"
            "Who are you?"
            "Who...................{w=.3}..........am..................??????"
            
            stop music 
            play music "rise.mp3" fadein 7
            scene black with Dissolve(3.0)
            pause(1)
            
            "I huddled in the blankets of my mum's bed,{w=.3} closed off from the rest of the world."
            "She was here just a few days ago.{w=.3} Now she's gone."
            "Uncle Graham disappeared too.{w=.3} We haven't seen him for weeks."
            
            "I don't understand.{p=.2}Why do things keep going wrong?"
            "Samuel never answered any of my questions.{w=.3} He never did."
            "Did he miss mum and uncle Graham as much as I did?{w=.3} Or was he too busy keeping secrets to care?"
            "I'm growing tired."
            
            "There was a knock at the door before Samuel slowly peeked inside."
            
            scene crane room sepia with Dissolve(2.0)
            ss "Hey kid,{w=.3} you doing alright in there?"
            "His voice sounded ragged,{w=.3} as though he had been crying too."
            "I didn't answer him.{w=.3} I pulled the sheets closer and huddled into a tighter ball on my mother's bed."
            
            "There were footsteps as Samuel walked over and tried to pat me on the head."
            "I recoiled back."
            
            o "......................."
            o "..........Samuel,{w=.3} can I ask you some questions?"
            "Samuel sighed tiredly,{w=.3} like he always did when I brought this up."
            "I pushed further."
            o "Who are you really?"
            "Samuel stayed silent.{w=.3} No answer, as usual."
            "I try again."
            o "Why do people keep trying to hurt me and mum?{w=.3} Who are they?"
            "No answer."
            o "Why did mum have to die-?!"
            ss "Look kid-"
            
            "Samuel rubbed the bridge of his nose,{w=.3} his one good eye squeezed shut in a poor attempt to hide his grief."
            ss "I know it's a hard thing to hear,{w=.3} but your mother never wanted to you know these things."
            ss "So I'm going to respect her wishes.{w=.3} I think it's best if-"
            
            o "{i}{b}My mother is dead.{/b}{/i}"
            "Something inside me snapped."
            
            show owen_outcry1 sepia with Dissolve(2.0)
            "I threw off the covers and landed heavily on my feet."
            o "{i}{b}My mother is dead,{w=.3} and I have no idea why.{/b}{/i}"
            o "{i}{b}My mother is dead,{w=.3} and I'm being told not to ask questions!{/b}{/i}"
            
            "Tears threatened to escape from my eyes as I shouted blindly into the room."
            o "{i}Who am I really?!{w=.3} Why do people want me dead-?{/i}"
            "Samuel snarled,{w=.3} his one sleep-deprived eye snapping with frustration."
            ss "Finding out the truth doesn't always work out for the best!"
            
            show owen_outcry1 with Dissolve(2.0)
            o "What makes you so sure of that?!"
            o "I hardly know my own life, {w=.3}{i}what is so wrong with wanting some answers?!{/i}"
            
            ss "Look kid,{w=.3} this isn't the sort of thing-"
            ss "I'll tell you when you're older-"
            
            o "What difference will that make?{w=.3} Everyone's already dead."
            "Samuel's frustration finally got the better of him."
            "He snarled."
            ss "{i}You're not the only one who lost someone kid.{p=.3}I lost my family too-!{/i}"
            o "Well you can lose one more!{w=.3} I'm {i}{b}leaving.{/b}{/i}"
            
            ss "Where the hell do you think you're going?!"
            
            "I was already halfway through the door."
            
            
    
            "The paper cranes hanging above our heads suddenly seemed to spring to life,{w=.3} spiraling through the room as though caught by a freak wind."
            "I turned back towards Samuel,{w=.3} breathless and weeping."
            o "Somebody out there has the answers I'm looking for."
            o "If I can't get them from my own family,{w=.3} I'll get them from someone else."
            
            show owen_outcry2 at Position(xpos = .5, xanchor=.5, ypos= .75, yanchor=.5) with Dissolve(3.0)
            show owen_outcry2 at Move((.5, .75), (.5, .25), 15,
                        xanchor=.5, yanchor=.5)
            "I slammed the door shut behind me and weakly fell to my knees."
            "My breath was ragged as I knelt over and let out a broken and feral scream."
            "I was tired.{p=.3}So tired."
            pause(3)
            
            o "{i}I want my life back.........{/i}"
            o "{i}I want my family back...................{/i}"
            
            scene black with Dissolve(4)
            play sound "noise.mp3"
            scene photograph with Dissolve(1.5)
            scene black with Dissolve(3.0)
            stop music
            
            play music "moonlit-melody.mp3" fadein 3
            scene crane room with Dissolve(3.0)
            
            "My eyes snapped open as I found myself lying prone on the bedroom floor."
            "The paper cranes fluttered above me patiently as I struggled to sit upright."
            
            play sound "ghost.mp3" 
            show echo shattered with Dissolve(2.0)
            e "[charname],{w=.3} are you alright?{w=.3} Did you see what Owen's wish was?"
            
            "I nodded numbly and rubbed my head."
            m "Yeah,{w=.3} I did."
            m "But I'm not sure if I can help Owen with something so.....{w=.3}vague?"
            m "He said he wants his family back,{w=.3} but I'm not sure there's a way I can help him with that when half his family is dead...."
            m "I'm just one person.{w=.3} How am I supposed to help?"
            
            
            
            play sound "leila.mp3" 
            hide echo with dissolve
            "Leila hummed lightly,{w=.3} their wings fluttering against the walls."
            "I strained my ears against the silence."
            "I swear I can almost hear a faint little voice......."
            play sound "leila.mp3"
            l "{size=-8}{i}There is more to this family than meets the eye.{/i}{/size}"
            l "{size=-8}{i}Each have left secrets and ambitions that lasted beyond the grave.{/i}{/size}"
            l "{size=-8}{i}Owen will never find peace in this family until each of those secrets have been brought to light.{/i}{/size}"
            l "{size=-8}{i}Will you help us uncover them?{/i}{/size}"
            
            "I pressed my hand gently against the camera hanging from my neck.{w=.3} It felt very warm."
            m "I'll do my best.{w=.3} For Owen."
            
            "The paper cranes in the room slowly stopped fluttering,{w=.3} the house becoming silent once more."
            l "..................................."
            l "{size=-8}{i}{b}This is a family built upon lies and good intentions.{/b}{/i}{/size}"
            l "{size=-8}{i}Owen will not like what he finds.{/i}{/size}"
            
stop music fadeout 4
scene black with Dissolve(4.0)
pause(2.0)
play music "calm-guitar.mp3"
scene derry house with Dissolve(2.0)


show samuel neutral with Dissolve(2.0)
ss "Kid, {w=.3}you doing okay?"

"I blinked and nearly jumped out of my skin as Samuel waved a hand in front of my face."
m "I'm alive! {w=.3}I-I....."
"A huge yawn escaped my throat as I sat up straight at the breakfast table."
"Once again,{w=.3} Samuel proved to be an excellent cook."
"I'm going to miss having a butler serving me at every meal."
"My mind wandered back to all the information I gathered last night.{w=.3} It was hard to believe Samuel was such a dangerous man in the past."
"It was even harder to believe that bloody fights had broken out in this very kitchen."
"And to think this family could be keeping more secrets from Owen...{w=.3}my head hurts just wondering about it."
"I stared at Samuel's back absentmindedly.{w=.3}This man was once a killer......"
"Now he's cooking breakfast for me in an eerily empty house....."


"Another exhausted yawn escaped me as I poked at my half-finished bacon."
m "...I might not be as alive as I thought."

show samuel smile with dissolve
ss "Those bags under your eyes seem to agree."
ss "Did you not sleep well last night?{w=.3} Maybe I should change the sheets in the guest room again..."
"I smiled gratefully as Samuel poured me another cup of coffee."
m "No no it's fine!{w=.3} The thunder and rain kept me up,{w=.3} that's all."

"{i}And I also snooped around the house and invaded your privacy.{p=.2}...but he didn't need to know that.{/i}"
"Samuel hummed cheerfully as he collected my dishes."
"He looked rather excited today."
stop music fadeout 3

ss "I finally get to see the kid again after so long..."
ss "I wonder what kind of person he's grown into."
ss "Hey [charname],{w=.3} you're good friends with Owen right?{w=.3} Think you can sum up what kind of man he's become?"

"I chewed on my fork thoughtfully.{w=.3} What's the best way to describe Owen, anyway?"
m "He really sucks at flirting."

play music "scheming.mp3" fadein 3
show samuel neutral with dissolve
ss "W-what do you mean?"
m "Oh god,{w=.3} you don't know?{w=.3} Owen's one big wannabe playboy now."
m "He tried hitting on me like 5 seconds after we met with the {i}cheesiest{/i} pickup lines I've ever heard."
m "And then a few days later he got roasted by his roommate for groping him all the time."
m "He flaunts his good looks, {w=.3}but has no idea how to properly flirt for someone's attention."
m "Like a {i}big,{w=.2} {b}gay,{w=.2}{size=+10} peacock.{/b}{/i}{/size}"

show samuel awkward with dissolve
ss "{i}{size=-10}Oh boy I really shouldn't have given the kid dating advice back in the day-{/size}{/i}"

play sound "surprise.mp3"
show samuel awkward at Shake((.5, .1, 0.5, 1), 1.0, dist=10)
m "Who the hell did he even learn this from?{w=.3} They must have been a horrible influence."
play sound "surprise.mp3"
show samuel awkward at Shake((.5, .3, 0.5, 1), 1.0, dist=10)
m "It's like they think if they flail their figurative dick around, {w=.3}they'll get all the ladies and guys-"
play sound "surprise.mp3"
show samuel awkward at Shake((.5, .6, 0.5, 1), 1.0, dist=10)
m "Owen could have been the perfect man but now he's cursed and influenced by garbage flirting skills. {w=.3}{i}Sigh...{/i}"


ss "Y-yeah!{w=.3} Who c-could that possibly be???"
ss "I don't have a clue!"
ss "M-must have been a p-pretty bad influence though!"

show samuel awkward at Move((.8, 1), (.01, 1), 3)
ss "{i}A-anyway!{/i}{w=.3} [charname], are you all packed up?{w=.3} We should get you back to school soon!"

m "But I haven't finished my bacon."
ss "Chop chop! {w=.3}Your education waits for no one!"
m "W-wait up!"

stop music fadeout 2
scene black with Dissolve(2.0)
play music "snowy-street.mp3" fadein 2
scene school with Dissolve(2.0)

"After breakfast,{w=.3} Samuel had stuffed a helmet onto my head and drove me back to Gerania on his hideous motorbike."
"The old bike spluttered in protest as Samuel barreled through the city like a madman,{w=.3} whooping gleefully at every turn."
"My stomach was also whooping (with dispair) as I clung on for dear life."
"By the time we skidded to a halt at Gerania's doors,{w=.3} I felt the bacon threatening to escape my throat."

show samuel smile with dissolve
ss "Gerania ho!{w=.3} It's been a while since I've been back here."
ss "The place hasn't changed a bit, have it?"

m "I dunno,{w=.3} everything looks a bit green and blurry today."
"I stumbled off the motorbike before politely vomiting into a nearby trashcan."
"Nearby visitors and parents took one look at me and retreated in disgust."

"Samuel laughed and patted my head in comfort."
ss "I didn't think Owen's so-called bodyguard would have such a weak stomach."
ss "You gotta toughen up there, buddy.{w=.3} Nothing makes you feel more alive than a wild motorcyle ride."
m "I'm kinda feeling the opposite of alive right now."
ss "You need to live life on the edge!{w=.3} Breathe in that adrenaline and danger!"
m "Mmmmmm,{w=.3} smells like dead pedestrians."

"I gumbled and lifted my head from the trash can."
"There were crowds of visitors around us being herded about by the teachers and students."

show samuel neutral with dissolve
"Samuel nervously followed my gaze,{w=.3} as if trying to spot Owen in the flood of people."
ss "You think the kid's going to come out to greet us?"
m "I kinda doubt it if I'm being honest.{w=.3} Owen's a bit of a chicken when it comes to this sort of thing."
"Samuel snorted in amusement."
ss "True enough."
show samuel smile with dissolve
ss "C'mon [charname], {w=.3} let's get going-"

c "{i}Why if it isn't Samuel Clark!{/i}"

play sound "slam.wav" 
show school at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
show samuel smile at Move((.2, 0), (1.5, 0), .25)
ss "Wha-{w=.3} {i}{b}OOOPH!{/b}{/i}"
"Mrs. Corlisse suddenly came barreling down the street and crushing Samuel into a bone-cracking bear hug."
c "Oh dearie,{w=.3} it's so good to see you again alive and well!"
ss "M-Mrs.C you're b-breaking my back-!"
c "It feels like centuries since you last attended my class. {w=.3}I see you've grown up quite a bit since!"
c "And you finally got rid of that horrid haircut as well.{w=.3} It looks like miracles {i}are{/i} possible!"
m "It's a {i}miracle{/i} that we arrived to school in one piece."
c "Ah [charname]!{w=.3} I'm glad to see you home safe and sound as well."
c "{size=-10}I suppose Samuel's driving skills haven't improved much these past 20 years...{/size}"
ss "{i}M-M-Mrs.C my spine-{/i}"

"I stared nonchalantly as Samuel twitched lifelessly in Mrs. Corlisse's vice grip.{w=.3} Karma never looked so sweet."
"It's surprising how easily such a tiny old lady can manhandle someone twice her size."
"Mrs. Corlisse finally finished her hug as Samuel collapsed onto the floor like a sack of potatoes."

show samuel awkward at center with dissolve
"His legs twitched like a squished bug as he struggled to stand."
ss "N-nice to see you too Mrs. C....{p=.3}Y-you haven't changed a bit."
c "In that I'm still an old lady who's single-handedly keeping the Gerania art department afloat?"
show samuel smile with dissolve
ss "I meant you're still as youthful as ever. {w=.3}Sorry about the art department though, you deserve a raise."
"Mrs. Corlisse laughed and patted Samuel on the cheek."
c "Keep the flattery coming dear,{w=.3} lord knows I'll need it."
ss "By the way, {w=.3}how's Owen doing?{w=.3} I was looking forward to meeting him today."
"Mrs. Corlisse snorted with the expression of someone who's been babysitting for too long."
"I blinked curiously as she dug a phone out of her pocket.{w=.3} It was holding an on-going call."
c "Did you hear that Owen?{w=.3} Samuel is here to see you."
c "Why don't you come out and meet him?"

"Owen's panicking voice stuttered through the speakerphone."
o "O-oh god,{w=.3} he's here a-already???!!"
o "I-I'm not mentally ready for this yet!"
m "7 years wasn't enough time to get ready?"
o "I-I got used to being a disappointment for 7 years!{w=.3} This is a very difficult change!"
m "It's gotta happen sooner or later, right?{w=.3} Why not just come out and get it over with?"

o "You underestimate how much I procrastinate, {w=.3}[charname]."
o "U-um, Samuel?{w=.3} You still there?"
"Samuel chuckled quietly at Owen's spluttering distress."
ss "I'm here kiddo.{w=.3} Glad to hear you haven't changed much in the bravery department."
ss "Let's hope you don't have to break a window every time we try to meet."
o "No promises there."
o "B-but um,{w=.3} would you mind if we uh.....{w=.3}met later tonight instead?"
"Samuel blinked in surprise."
ss "Later tonight?{w=.3} What for?"
o "It'll give me time to mentally prepare!"
o "P-plus there's a Visitor's Day dance tonight!{w=.3} We'll all be nicely dressed and make good impressions!"
"I frowned.{w=.3} Owen is trying to keep his voice lighthearted,{w=.3} but there was a heavy untone of honest anxiety."
"Samuel seemed to catch on to this as well."
ss "Alright fine.{w=.3} I'll see you tonight at this....Visitor's Day dance."
ss "I've waited 7 years.{w=.3} An afternoon isn't going to kill me."
m "This is pretty unfair though Owen."
m "I mean, Samuel won't have a dance partner.{w=.3} What's the guy even supposed to do?"
o "Nobody actually dances at dances anymore.{w=.3} They just waddle and bounce on their feet like a flock of pigeons."
o "A-anywho, I'll see you tonight!{w=.3} L-looking forward to it!"

"And with a click,{w=.3} Owen hung up."
"Samuel sighed and rubbed his temples in exasperation."
ss "Looks like our little reunion got postponed."
ss "I wish I raised Owen to be less of a chicken-shit when he was younger."
c "{i}Language,{/i} Samuel."
"Mrs. Corlisse smiled fondly as Samuel climbed back onto his abomination of a motorcycle."
c "If I remember correctly,{w=.3} you were also quite the chicken-shit back in the day."
"Samuel barked a laugh."
show samuel smile with dissolve
ss "I grew out of it eventually.{w=.3} Hopefully Owen will too."
"Samuel grinned and waved a quick goodbye."
hide samuel with Dissolve(2.0)
"His motorcycle let out a honk of despair before barreling down the street and disappearing around a corner."
"Mrs. Corlisse sighed and patted me on the shoulder."
c "[charname],{w=.3} you must be exhausted from your trip."
c "Why don't you go back to your dorm and rest for a while?"

"I yawned again before nodding in agreement."
m "Yeah, rest sounds nice."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "easy-lemon.mp3" fadein 2
scene dorm hallway with Dissolve(2.0)

"I swam through a sea of parents and visitors on my way back to my dorm.{w=.3} There was a surprising amount of people coming to Gerania today."
"I felt a wave of relief as I closed the dorm doors behind me and silenced the chattering crowd outside."
"It was good to be home."
"Owen's house was comfy,{w=.3} but I missed my dorm building with its smell of old coffee and burnt toast."
"With a soft sigh and a smile,{w=.3} I made my way upstairs towards the kitchen."

scene kitchen with Dissolve(2.0)
"I poked my head into the kitchen and grinned at the smell of sizzling omelettes and sweet pancakes."
m "That smells so {i}good{/i}."
m "Is Sissel making breakfast again?"

show sissel neutral with dissolve
"Sissel looked up from gracefully flipping omlettes with a surprised smile."
s "Yo [charname].{w=.3} Glad to see you back."
s "Everyone had their knickers in a twist the whole night waiting for you."
m "I could tell from the phone call last night.{w=.3} Sorry for worrying you guys."
"Sissel scoffed and returned his attention to the stove."
s "I ain't worried one bit.{w=.3} You're a grown ass man,{w=.3} you can take care of yourself."
s "No idea why Teach and Owen made such a big deal out of it." 
hide sissel with dissolve 

"Meanwhile,{w=.3} Jinny waved a greeting from the breakfast table where she and Owen were sitting."
"Well,{w=.3} \"sitting\" is putting it generously."
"Owen was a collapsed mess on the table.{w=.3} His face was buried next to the salt and pepper while he tore at his hair in an restless frenzy."
"Jinny sighed and patted the back of Owen's head."

show jinny neutral with dissolve
j "Heyo ghostbuster!"
m "Jinny?{w=.3} What are you doing here?"
j "It's Visitor's Day isn't it?{w=.3} I can finally walk around Gerania's campus without feeling like a trespasser."
j "Oh, and don't mind Owen much, he's been stressing out the whole night.{w=.3} Barely slept a wink as far as I know."
"Owen let out a noncommittal groan in greeting as I sat down at the table."
"At least, I think it's a greeting."
m "You doing okay there, dude?"
hide jinny with dissolve


play sound "surprise.mp3"
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"Owen promptly let out a muffled scream into the kitchen table."
show jinny neutral at left with dissolve
show owen scratch at right with dissolve
o "Oh god I'm not ready.{w=.3} I'm not ready!"
m "Still nervous about meeting up with Samuel?"
o "I snapped at him so badly when I left home.{w=.3} I was a complete little shit!"
o "What if I mess things up again this time around?"
o "Oh god, what do I do??"

"Owen finally lifted his head from the table."
"He looked like an absolute mess."
"There were heavy, sleep-deprived bags under his eyes and his hair was a tangled mess from his pulling at it."
"For a moment,{w=.3} I was glad Owen convinced Samuel to postpone their reunion."
j "Stop chewing on your fingernails, dude.{w=.3} It's not sanitary."
o "I really,{w=.3} {i}really{/i} don't care right now Jinny."
o "Got other things on my mind at the moment."

"The delicious smell of breakfast suddenly caught our attention as Sissel carried several plates of food to the table."
show jinny neutral at farleft with dissolve
show owen scratch at center with dissolve
show sissel neutral at farright with dissolve
s "Alright you sad fuck,{w=.3} eat up.{w=.3} It'll make you feel better."
s "Or at the very least you won't be sad {i}and{/i} hungry."
"Owen grumbled his thanks and began poking numbly at his omlette."
"Sissel frowned at the apparent lack of eating."
s "What?{w=.3} My cooking not good enough for you all of a sudden now that you have your butler back?"
o "N-no, not at all!{w=.3} I just.....{w=.3} don't have much of an appetite right now."
j "C'mon Owen,{w=.3} you gotta unclench and relax a bit."
j "You're stressing about this more than you need to."
stop music fadeout 5
o "Easy for you to say."
o "I ran away from home and avoided Samuel for 7 years.{w=.3} {i}7 years!{/i}"
o "And this was right after my family fell apart too."
o "I'm still in shock he's willing to see me.{w=.3} What if I fuck things up again?"
"Owen pulled at his hair again and let out another anxious groan."
"There was a deep {i}thud!{/i} as he slammed his forhead onto the table."
o ".............{p=.3}..........................{w=.3}I just really,{w=.3}{i} really{/i} don't want to fuck this up."

play music "meloncholy.mp3" fadein 5
"A long silence hung in the kitchen.{w=.3} Jinny, Sissel and I exchanged helpless looks."
"I suddenly yelped as Jinny kicked me from under the table."
"She subtlely jerked her head towards Owen and mouthed {i}'Say something to him!\"{/i}"
"Looks like I can add \"emotional support\" under my bodyguarding duties."
hide jinny
hide sissel
with dissolve
"I turned towards Owen with a small smile."
m "Well Owen,{w=.3} you don't have to worry too much about meeting up with Samuel."
show owen frown with dissolve
o "What do you mean?"
m "I mean,{w=.3} that's the man who changed your diapers as a kid.{w=.3} He'll still love you even if you're a massive disappointment."
"Owen cracked a small smile in spite of himself."
show owen grin nervous with dissolve
o "I'm.......{w=.3}not sure how to feel about that."
show owen scratch with dissolve
o "Even so,{w=.3} there's still a chance I'll fuck things up-"
m "You're finally meeting and speaking and getting awkward with Samuel after {i}7 years.{/i}"
m "That's better than no contact at all."
m "Even if you do fuck it up,{w=.3} you're still making progress!"
m "And if things so south,{w=.3} you'll have plenty of chances to unfuck it later."
m "So just chill out,{w=.3} give this a chance,{w=.3} and stop being a chicken shit, okay?"
"I gingerly patted Owen on the shoulder."
stop music fadeout 5
show owen neutral with Dissolve(2.0)
"Owen let out a deep breath.{w=.3} He face finally relaxed into a small smile."
o ".....thanks [charname].{w=.3} I'll try not to fuck it up."

play music "clear-air.mp3" fadein 3
"We were interrupted with a sharp {i}clink!{/i} as Jinny stabbed her omlette with distaste."
show jinny neutral at farleft with dissolve
show sissel neutral at farright with dissolve
j "There's too much talk about fucking at the breakfast table. {w=.3}Now {i}I'm{/i} losing my appetite."
s "I'll take both of your omlettes if you're having appetite problems."
"Owen and Jinny exchanged looks before simulatiously shoving half their omlettes down their throat."
show sissel wtf with dissolve
s "...okay nevermind."
j "Sorry Sis,{w=.3} your cooking's too good to pass up."
show sissel neutral with dissolve
s "Glad to hear it, {w=.3}cuz you're all doing the dishes this time.{w=.3} I've got to go to work now."
o "Aw, really?"
s "I would have left earlier,{w=.3} but I didn't want to leave Teach alone to deal with your moping session."
o "I wasn't moping {i}that{/i} much..."
"Sissel scoffed as he made his way towards the door."
s "We had to listen to you cry melodramatically the whole night.{w=.3} When will you ever grow up?"
s "Anyway, {w=.3}there better not be another mess in the sink when I come home."
s "See ya'll later."

hide sissel with dissolve
show jinny at left with dissolve
show owen at right with dissolve

"I stared Sissel's retreating back as he disappeared down the hall."
m "Hey Owen.{w=.3} Sissel was worried about you too,{w=.3} even if he doesn't show it."
show owen grin nervous with dissolve
o "Yeah.....{w=.3}I know."
m "In all seriousness,{w=.3} it's good to see you feeling okay again."
m "It's weird to see you all anxious and mopey."
show owen neutral with dissolve
o "Yeah,{w=.3} sorry about that.{w=.3} I'll try not to worry you guys again."
m "Haha, no you won't."
j "Speaking of being anxious,{w=.3} how's that whole \"The Lorelie's are trying to kill me\" thing going?"
show owen frown with dissolve
"Owen blinked in surprise."
o "Wait,{w=.3} how did you know about that?"
m "Erm........{w=.3}uh.............."
m "I....{w=.3}{i}might{/i} have mentioned it to her yesterday."
"Owen stared at me dully,{w=.3} as if to say {i}\"Really?\"{/i}"
m "W-well I needed to know the whole situation with the Adlai's and Lorelei's,{w=.3} and you kept your mouth shut for the most part."
m "Phillip's the Black Cat,{w=.3} so I figured he'd know something about a big ol' criminal mafia family."
m "So naturally, I asked him about it and he gave me answers."
m "And uh....{w=.3}Jinny's apparently his accomplice?"
m "Phillip said he can get more info on your family though,{w=.3} so I guess it turned out to be a good thing."
"Owen rubbed his temples and sighed."
o "Fair enough.{w=.3} It's a bit weird to have all my friends know that people are trying to kill me-"
stop music fadeout 2
j "{i}{b}-oh shit.{/b}{/i}"
o "Hm?"
m "What is it?"
"Jinny stared at us in sudden realization."
j "We totally forgot about Phillip-"

play sound "slam.wav"
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
play music "scheming.mp3" fadein 3
hide owen
hide jinny

"The three of us nearly jumped out of our seats as the kitchen door slammed open."
show phillip no with Dissolve(3.0)

"Phillip limped into the kitchen,{w=.3} staring at each of us with an expression that could only be described as the walking manifestation of {i}\"Fuck you.\""
"There were dark heavy bags under his eyes,{w=.3} as though he hasn't slept in years."
"His hair was a tangled mess and the poor guy looked like he was in desperate need of a relaxing shower."

p "..............................."
show jinny neutral at farleft with dissolve
show owen grin nervous at farright with dissolve
m "Uh.........{w=.3}hi Phillip?"
o "You doing okay there buddy?"
p "Oh I see how it is."
p "When [charname] disappears into the night, ya'll stay up till 1AM to make sure he's still alive and well-"
play sound "surprise.mp3"
show jinny at Shake((.2, .1, 0.5, 1), 1.0, dist=10)
show owen at Shake((.8, .1, 0.5, 1), 1.0, dist=10)
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
p "-But when I go MIA , {i}I don't even get a phone call????{/i}"
o "W-well to be fair, you sneak out pretty often-"
p "Oh look!{w=.3} Owen's sad!"
play sound "surprise.mp3"
show jinny at Shake((.2, .3, 0.5, 1), 1.0, dist=10)
show owen at Shake((.8, .3, 0.5, 1), 1.0, dist=10)
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
p "Let's spend the next 12 hours coddling him like a child while {i}I stay up investigating the people who want to kill you.{/i}"
j "{size=-10}Owen's kinda a baby in the \"handling anxiety\" department though...{/size}"
p "And let's not forget to leave Phillip out the {i}one day Sissel decides to cook us breakfast again."
play sound "surprise.mp3"
show jinny at Shake((.2, .6, 0.5, 1), 1.0, dist=10)
show owen at Shake((.8, .6, 0.5, 1), 1.0, dist=10)
show kitchen at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
p "{i}{b}I'm sure he's totally not tired or starving after not sleeping for the last 36 hours while he was doing you favors.{/b}{/i}"

"Jinny, Owen and I shrank under the kitchen table,{w=.3} cowering under Phillip's merciless gaze."
"The three of us exchanged guilty looks and mumbled \"sorry\" as Phillip wobbled across the kitchen to sit down at the table."
o "Y-you doing okay there Phillip?{w=.3} You don't look so good."
p "I feel like every organ in my body is trying to kill me.{w=.3} God help me."
"Phillip's eye twitched as he reached across the breakfast table."
p "I'm stealing the rest of your omlettes."
p "Bad friends don't get to eat omlettes."
j "Eh,{w=.3} fair enough."

stop music fadeout 2
scene black with Dissolve(2.0)
play music "easy-lemon.mp3" fadein 2
scene kitchen with Dissolve(2.0)

show jinny neutral at farleft with dissolve
show phillip no with dissolve
show owen neutral at farright with dissolve

"Two and a half omlettes later,{w=.3} Phillip looked significantly less exhausted and homocidal."
"Watching a sleep-deprived and starving man eat breakfast was quite the savage sight."
m "Uh...{w=.3}are you feeling any better Phillip?"
m "I made you some coffee{w=.3} (as a peace offering)."
p "I still feel dead. {w=.3}People aren't suppose to be conscious for this long-"
"Phillip took a sip of my coffee and immediately spat it across the table to form a rainbow in the morning sun."
p "W-what is this???"
m "I'm pretty sure it's just coffee.{w=.3} With cream and sugar."
"Phillip wrinkled his nose at the offending cup as though it personally insulted him."
p "Sugar is bad for you."


"Jinny snapped her fingers impatiently to catch our attention."
j "Your taste in coffee aside,{w=.3} did you get any new information on Owen's family?"
j "You did spend the entire night investigating after all."
show phillip irritated with dissolve
p "I tried.{w=.3} Morse is keeping a tight lid for some reason..."


show owen frown with dissolve
o "Morse?{w=.3} You mean that famous criminal informant?"
o "They say he knows everything about {i}everything.{/i}{w=.3} That he never fails to find what he wants to know."
o "He actually lets you talk to him??"
show phillip neutral with dissolve
p "He better.{w=.3} The man owes me enough favors to become my indentured servant."
p "Did you try to contact him yourself?"
"Owen rubbed his temples tiredly."
o "Yeah...{w=.3}I tried getting into his rumored hideout yesterday,{w=.3} that bar called \"The Robin's Nest.\""
show owen scratch smile with dissolve
o "The bouncer kicked me out after he caught me sneaking through the window."
m "What is with you and exiting through windows?"
show owen neutral with dissolve
o "It's not like I could just waltz through the front door."

p "Well here's some good news:{w=.3} you don't have to crawl through windows to speak with him anymore."
stop music fadeout 5
"Phillip glanced at the door, as though to make sure it was closed."
"He pulled out his cell phone and began flipping through the numbers."
p "Surprisingly,{w=.3} he wants to talk to us directly this time around."
p "Not sure if he's going to cooperate though.{w=.3} He's a pretty difficult guy."

play music "water-lily.mp3" fadein 3
"Phillip switched the call onto speakerphone and placed it onto the table."
play sound "phone.wav"
"The dial tone played for several long seconds before a deep,{w=.3} pitched voice crackled back."
mo "....................{w=2}took you long enough.{w=.3} Is everyone here?"
"I blinked in surprise.{w=1} The voice sounded like it was put through a thick robotic filter to disguise its owner."
mo "Owen Lorelei,{w=.3} Jinny Corlisse,{w=.3} Phillip Tan............"
mo "Oh,{w=.3} and that other kid.{w=.3} [charname] or whatever."
m "Wow, that really boosts my self-esteem."
mo "I don't really care about you kid.{w=.3}"
mo "Especially after how you snooped around that house last night,{w=.3} sticking your nose where it doesn't belong."
m "H-how did you know about that?"
mo "I have eyes everywhere.{w=.3} It's my job to know."
p "C'mon Morse,{w=.3} stop giving people a hard time and just answer our questions already."

"I could practically hear him roll his eyes from behind the speaker."
"There was the sound of rustling paper, as though Morse was rummaging through some files."
mo "Ahem.{w=.3} So I guess I should introduce myself first."
mo "The name's Morse.{w=.3} I buy and sell secrets from big people for a living."
mo "The only reason I'm helping you shrimps is because I owe the Black Cat a few favors-"
p "A \"few?\""
mo "{i}Ahem!{/i}"

mo "Anyway, you want to know why the Lorelei family is suddenly interested in killing Owen Lorelei."
"I grumbled under my breath.{w=.3} This guy sounded so damn cocky."
m "We kinda already have a good idea."
m "Samuel mentioned that they're probably after the Adlai fortune that Owen inherited from his mom."
m "If he dies,{w=.3} his fortune will probably be taken by his father in the Lorelei family-"

"Morse suddenly claps his hands in fake applause."
mo "Wowee, the kid's figured it out! {w=.3}Looks like you don't need me here anymore-"
show owen frown with dissolve
o "W-wait!{w=.3} Don't hang up!"
o "There's more to this, {w=.3}isn't there?"

"Morse scoffed."
play music "fragments.mp3" fadein 3
mo "Obviously."
o "This can't be about my family fortune.{w=.3} I have a will written out and everything-"
"Owen was cut off by the sound of rustling paper again."
mo "Oh look,{w=.3} I have a copy of your will right here."
mo "It states that in the event of Owen Lorelei's passing,{w=.3} all his assets will be donated across 50 institutions and charities throughout the city."
mo "Ugh,{w=.3} your mother told you to write this, didn't she?{w=.3} That hag."
o "W-well, it's the right move..."
mo "Heather Adlai is a {i}snake.{/i}"
mo "{i}\"Hey honey, you're still too young to understand, but make sure to clean up after yourself in case you get your ass murdered!\"{/i}"
"Jinny cleared her throat impatiently."

show jinny angry with dissolve
j "Wait,{w=.3} this means Owen's fortune couldn't be the motive."
j "The Adlai family fortune is financially locked, even if Owen dies."
mo "Of course."
mo "If the Adlai fortune ended up empowering the Lorelei's,{w=.3} Heather Adlai would be rolling in her grave."
mo "The moment Owen dies,{w=.3} the Adlai fortune becomes untouchable by the Lorelei family."
j "So this means they want Owen dead,{w=.3} but not for the purpose of taking his fortune...."
mo "Yes, thank you captain obvious."
show phillip irritated with dissolve
p "Have you figured out what that motive is yet?"
mo "I have a hunch.{w=.3} I'll tell you kids when I have evidence to back it up."
mo "Now if you'll all stop playing detective and get on with your lives, {w=.3}that'll be great."

show phillip neutral with dissolve
p "Heh, you're just salty because you don't have all the information yet."
mo "{i}\"Yet\"{/i} is the key word."
stop music fadeout 8
mo "Now onto the next order of business:"
mo "Owen, get the hell out of the room.{w=.3} I need to talk to the other three in private."
o "W-wah,{w=.3} why?"
o "This is my life on the line here-"
mo "Shoo.{w=.3} Leave.{w=.3} Out."
mo "I'm not talking until you're gone."

"Owen grumbled under his breath in annoyance."
show owen scratch with dissolve
o "Fine.{w=.3} I'll hit the gym for now, I guess."
o "I'll see you guys later."
play music "somber.mp3" fadein 2
hide owen with Dissolve(2.0)
"The room was silent as Owen reluctantly left and shut the door behind him."

show jinny angry at left with dissolve
show phillip irritated at right with dissolve
mo "Is he gone?{w=.3} Great, let's get to the important stuff."
mo "The Lorelei family's probably going to try and make a move at Owen tonight."

m "What?!{w=.3} Why tonight?"
mo "It's Visitor's Day.{w=.3} Giant crowds of adults are moving around campus all day."
mo "It's the perfect time to strike.{w=.3} You can't seriously tell me you didn't see this coming."
mo "I caught word that Owen's old man is coming to Gerania.{w=.3} Good ol' Oleander Lorelei.{w=.3} He'll probably try to make contact with Owen."
p "I don't like this.{w=.3} It sounds fishy..."
mo "Exactly.{w=.3} So here's what I need you all to do:"
mo "Uh......{w=.3} what was that kid's name again?{w=.3} The unimportant one."
j "Oh it's [charname]."
m "Hey!"
mo "[charname]!{w=.3} Since you're so chummy with Owen, I need you to stay with him and try to keep him away from his father if possible."
mo "Make sure Owen stays in secure campus buildings and avoid any dangerous places."
m "...you don't want Owen to know his father is coming?"
mo "God no.{w=.3} Owen will probably get all sentimental and attached. It'll be a mess."
mo "It's best we try to keep them from making contact at all if possible."
mo "Owen's planning to meet up with Samuel tonight right?{w=.3} Make sure they stick to each other like glue."
mo "He'll be safer with the big oaf around him."
m "Makes sense. I'll try my best."


mo "And now for Phillip and Jinny."
mo "As far as I know,{w=.3} Oleander Lorelei is pretty spineless and probably won't try anything dangerous."
mo "I'm not taking any chances though. {w=.3}That's why I need you two to somehow take everything off his person."
j "\"Everything off his person?\""
mo "He could be hiding weapons or something dangerous up his sleeve.{w=.3} You guys want to make sure Owen stays safe, don't you?"
p "How the hell are we supposed to take everything off the guy though?"
mo "Make him strip."

play music "wacky.mp3" fadein 2
show jinny wtf with dissolve
show phillip no with dissolve

p "What."
j "Excuse me?"

mo "It's a good solution.{w=.3} Oleander can't hide anything if he's forced to leave everything behind-"
p "How the flying fuck are we supposed to do that without getting arrested for sexual assault?"
mo "I don't know.{w=.3} You better come up with something though,{w=.3} it's for the sake of everyone's safety."
j "You just want to humiliate him in front of all the other parents."
mo "Pfft you can't prove anything."
mo "Well,{w=.3} good luck kids.{w=.3} Sounds like you're all in for a rough night."
p "Wait - don't hang up you shit! You can't just leave us with some vague instructions-"

play sound "beep.mp3"
"The phone beeped before lapsing into an insulting dial tone."
p "................................."
p "....I hate this guy sometimes."
j "Why does [charname] get the easy job?{w=.3} You just have to hang out with Owen and make sure he doesn't do anything stupid."
m "It's a very difficult job,{w=.3} let me tell you."
m "Only a talented bodyguard would fit the bill."
"Phillip and Jinny both looked like they were considering strangling me.{w=.3} Guess this is my cue to leave."
"With sigh,{w=.3} I stood up from my seat while ignoring the two's withering gaze."

m "Welp!{w=.3} Looks like it's time for me to return to my bodyguarding duties."
m "Best of luck to you, friends!"
j "\"Welp\" isn't a word."
m "I say what I want."
m "Welp, toodles!{w=.3} Good luck on stripping Oleander Lorelei!"
"Phillip and Jinny simultaneously flipped me the bird as I left the kitchen."

stop music fadeout 3
scene black with Dissolve(3.0)
play music "cafe-music.mp3" fadein 3
scene gym with Dissolve(2.0)


"I poked my head into the school gym and reveled in the wave of AC that hit my face."
"Owen mentioned he was going to hit the gym earlier, {w=.3}right?"
"It shouldn't be too hard to find him.{w=.3} It's pretty empty in here after all-"

play sound "slam.wav" 
show gym at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"I jumped at the sound of slamming fists echoing through the building."
"Curious,{w=.3} I made my way around the corner to find Owen beating the living daylights out of a poor punching bag."
"The bag creeked in protest as it swung from its chains in the ceiling."

play sound "slam.wav" 
show gym at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
"Owen let out a frustrated yell and smashed fist after fist into the punching bag.{w=.3} I winced at the painful sound of impact."
m "That can't feel too good for your fists..."
"Owen looked up from his massacre in surprise."
"Sweat dripped down his brow as he turn towards me with a grin."

show owen shorts with dissolve
o "Oh [charname].{w=.3} Didn't see you there."
m "I'm surprised you heard me with all the noise you were making.{w=.3} Do you do this often?"
m "No wonder you're so in shape."
show owen shorts grin closed with dissolve
o "You think these muscles came from a healthy lifestyle?"
o "Nah man.{w=.3} I work myself to death to keep my mind off the looming pit of anxiety in my life."

show owen shorts with dissolve
o "This is a nice way to let off some steam.{w=.3} Hope I didn't scare you at all. I wasn't expecting you to follow me."
m "A good bodyguard is always there when you need him."

stop music fadeout 3
o "Heh,{w=.3} you have been doing a good job with that whole bodyguard thing..."
o "That reminds me,{w=.3} I never got around to thanking you."
m "Thanking me?{w=.3} For what?"

play music "compassion.mp3" fadein 3
o "Well, for everything."
o "You listened to me mope about my life issues without any judgement.{w=.3} And then you took to time to encourage me every time I got anxious."
o "It felt really..........{w=.3}nice{w=.3}, to just have someone to talk to."
o "After all that,{w=.3} you somehow managed to arrange a reunion between Samuel and me."
o "It means a lot,{w=.3} to have someone close who cares so much."
o "So uh......{w=.3}thanks for taking care of me."
o "You make a good bodyguard."
"Owen gave me a grateful smile and ruffled my hair.{w=.3} My chest suddenly felt very warm."
m "W-well somebody had to.{w=.3} You'd be a mess without me."
m "Oh!{w=.3} Speaking of which,{w=.3} I have something for you."
"I dug my hands into my pockets before pulling out a small, leather journal."
m "This is your mother's journal.{w=.3} I think you should have it."
m "Uh....{w=.3}don't get mad but I kinda snooped around your house to get this."

"Owen looked touched as he took the journal from my hands and examined it carefully."
o "You stole my mother's journal?{w=.3} How did you even open the lock on this?"
m "I'm a very good lockpicker."
"For a moment I heard Echo cough sarcastically in the back of my head."
m "Ahem."
m "Anyway, I figured you deserved to know the whole truth about your family.{w=.3} This should be a good first step."
m "I'll try and help you the best I can.{w=.3} I'm a nosy photographer after all, it's what I do best."

"Owen brushed a hand slowly over the journal's worn cover.{w=.3} A bittersweet smile formed on his face."
stop music fadeout 3
o "Mum's would get pissed if she knew I was digging through her stuff."
o "But it's about time I hit my rebellious stage."

play music "scheming.mp3" 
m "Didn't you do that already when you ran away from home?"
o "Really dude?"
m "Whoops,{w=.3} too soon?"
o "Well....I guess I kinda deserve it after ditching you with Samuel yesterday."
o "Sorry about that. I'm a bit of a chicken shit sometimes."
m "Damn right.{w=.3} Samuel's a scary dude. That was not a warm first impression."
m "You owe me big time after all I did for you."

o "Well................"
"Owen glanced around the near-empty gym for a moment before returning to me with a sly grin."
show owen shorts at Position(xpos = .5, xanchor=.5, ypos=.7, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
"He leaned in suspiciously close to whisper in my ear."
o "I could give you some \"service\" as an appology if you want~"
"I suddenly felt very hot under my jacket."
m "Dude really?{w=.3} Right here?!"
show owen shorts at center with dissolve:
            xzoom 1 yzoom 1
"Owen threw an arm over my shoulder and winked."
o "There's a break room out back that no one uses.{w=.3} We'll have plenty of privacy."
o "Plus it'll help me blow off all the stress from this morning.{w=.3} It's a win-win!"
o "C'mon,{w=.3} you can't say no to a free blowjob~{w=.3} I assure you I have excellent technique~"
o "Or you know,{w=.3} I could appologize the old fashion way and then treat you to dinner or something."
o "But c'mon, {w=.3} this is way more fun!"
o "What do you say?"

menu:
    "Treat me to dinner.{w=.3} I can't say no to free food.":
        m "Dude,{w=.3} you can't just offer a blowjob before taking the person out to dinner first."
        m "I've got standards man."
        o "Oh fine.{w=.3} I'll make sure it'll be the best damn dinner you've ever had."
        m "You better not be the one cooking."
        o "Nah, {w=.3}it'll be a nice spot in an extravagant and expensive restaurant.{w=.3} It'll be a date~"
        m "I just want a large platter of fries to be honest..."
        o "Oh.{w=.3} I kinda imagined dates to be all candle-lit and romantic or something like that..."
        m "I just want food man.{w=.3} Those expensive restaurants always serve you a huge plate with a tiny bit of food in the middle."
        m "It's such a waste!"
        m "I get more bang for my buck at McDonalds."
        o "Image telling your friends {i}\"My first date with this guy I kinda like was at a McDonalds.\"{/i}"
        m "I know right?{w=.3} Isn't it great?"
        m "-wait."
        m "Aaaaaaw you like me? {w=.3}Kinda?"
        "A dumb grin instantly stretched across my face."
        "Owen chuckled and scratched the back of his head awkwardly."
        o "I thought I made it pretty obvious.{w=.3} I've been sending flirty remarks your day for days now."
        m "You send flirty remarks to everyone.{w=.3} It was hard to tell if these were genuine to be honest..."
        m "Your flirting skills need work."
        o "{size=-10}I'm going to have a talk to Samuel about all that flirting advice when I was younger...{/size}"
        m "I'll admit you {i}do{/i} have a weird kind of charm though."
        m "So yes,{w=.3} I'd like to spend a nice dinner with you sometime."
        o "Yes!"
        o "I-I mean, of course!{w=.3} I'll make sure you have a good time!"
        
        "Both of our cheeks flushed a bit of pink as we laughed awkwardly."
        o "A-anyway,{w=.3} I better go shower real quick."
        o "Gotta g-get ready for the dance later tonight, right?"
        m "Of course."
        hide owen with Dissolve(2.0)
        "Owen looked absolutely giddy as he turned to make his way towards the gym showers."
        "My chest felt equally bubbly.{w=.3} I couldn't stop smiling as I watched him go."
        "What a dork."
    "Show me what you've got <3":
        m "Well I do deserve a good reward after all my work....."
        o "Heh, I'll make it worth your while,{w=.3} I'm promise~"
        "Owen nuzzled his face against my neck before beckoning me to follow him."
        o "C'mon,{w=.3} let's find ourselves some privacy."
        
        stop music fadeout 2
        scene black with Dissolve(2.0)
        scene gym breakroom with Dissolve(2.0)
        
        "My heart was thumping in my chest as I peeked around the gym break room."
        "It does look rather empty and private."
        m "This shouldn't be too bad-"
        
        play music "jazz.mp3" fadein 3
        "I yelped.{w=.3} Owen was suddenly behind me and pulled me into a rather close hug."
        "My back as flush against him as he snaked a warm hand up my shirt to caress my front.{w=.3} I could feel his bulge pressing against my back as he leaned down to whisper in my ear."
        show owen shorts at Position(xpos = .5, xanchor=.5, ypos=.7, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
        o "Hope you're comfortable down there~"
        m "Y-you're such a horn dog, Owen."
        o "Aw admit it,{w=.3} you love that about me."
        "Owen gingerly peeled off my jacket while nibbling at my neck.{w=.3} Every inch of my body felt hot and sensitive to the touch."
        "Owen's breath was warm against my neck as he tugged off my tank top and tossed it onto a nearby chair."
        o "C'mon,{w=.3} let's get those awful clothes off of you.{w=.3} I wanna see more from my bodyguard~"
        m "I-it's just a blowjob,{w=.3} I-I don't need to take {i}everything{/i} off for this..."
        o "Aw why are you suddenly so shy?"
        "I wrapped my arms self-consciously around my bare chest and glanced at the closed door behind us."
        m "I'm getting naked in the back of a very public gym.{w=.3} I-I am a bit nervous....aren't you?"
        show owen shorts at center with dissolve:
            xzoom 1 yzoom 1
            
        "Owen grinned before taking a step back."
        show owen naked with dissolve
        "He slowly hooked his thumbs under his gym shorts before pulling them down and dramatically throwing them across the room."
        "His dick was already semi-hard and dripping drops of pre onto the tiled floor."
        "My face felt even hotter as Owen gave me a sly wink and approached me again."
        o "There~{w=.3} Now you won't be the only naked one in the room."
        o "Hope you like what you see~"
        m "Y-you need any help with that down there?"
        show owen naked at Position(xpos = .5, xanchor=.5, ypos=.7, yanchor=.5) with Dissolve(2.0):
            xzoom 1.5 yzoom 1.5
        "Owen chuckled pulling me close and smooched me on the nose."
        o "Nah,{w=.3} today I'm the one who's servicing you.{w=.3} So just sit back and relax, buddy."
        hide owen with Dissolve(2.0)
        "I gulped as Owen knelt down,{w=.3} trailing a hand slowly down my front before undoing my belt.{w=.3} My shorts soon joined the rest of our clothes in the corner of the room."
        "Owen held both hands on my hips, with his face was so close that I could feel his hot breath on my dick. {w=.3}My head was a mess of embarrassed heat."
        "There was a long pause for a moment before Owen suddenly wrapped his arms around my waist and picked me up off the floor."
        "I yelped and grabbed onto Owen's head as he carried me across the room like I weighed nothing."
        m "W-what are you doing?"
        o "Finding a better position.{w=.3} I can't really see your face from down there."
        m "H-hold on!"
        
        play music "groove.mp3" fadein 3
        show owen_blow1 at Move((.6, .4), (.4, .6), 15,
                        xanchor=.5, yanchor=.5) with Dissolve(3.0)
        pause(2)
        "Suddenly I found myself sprawled across a breakroom table with Owen grinning up at me from between my legs."
        "His strong arms wrapped around my thighs and kept them spread as he gave slow, tantalizing licks down my length."
        o "This is much better.{w=.3} Are you ready?"
        "I tried not to gasp as his hot tongue teased around my tip and coaxed another stream of pre to drip out."
        "I never felt so exposed before.{w=.3} This was strangely turning me on...."
        show owen_blow2 at Move((.5, .6), (.5, .4), 15,
                        xanchor=.5, yanchor=.5) with Dissolve(3.0)
        pause(2)
        "A moan escaped my throat when Owen wrapped his lips around my dick and began to suck earnestly."
        "His mouth felt unbearable hot as he bobbed up and down,{w=.3} his tongue teasing my head at every chance."
        "I squeezed my eyes shut and spread my legs wider, {w=.3} panting at the sensation of that hot mouth."
        "I must have been making a lot of noise.{w=.3} Owen glanced up at me and chuckled,{w=.3} sending sweet vibrations down the head of my dick."
        "There wasn't much room to think.{w=.3} My hips humped into Owen's mouth as I struggled to breath through the mess of pleasure clouding my brain."
        "This only made Owen suck harder, milking my dick for every drop of pre.{w=.3} I felt his throat swallowing against my tip with every bob of his head."
        "Owen stuck a finger into his mouth and gathered a coating of pre and saliva."
        "I shivered at the sudden feeling of something probing my pucker."
        "I let out another moan when Owen gently pushed,{w=.3} his hot fingers searching through my insides as his sucked feverishly."
        "Another wave of pleasure washed down my spine as Owen massaged my prostate in time with my thrusts,{w=.3} pushing me towards the edge."
        show owen_blow3 with Dissolve(3.0)
        pause(2)
        "I gave one final thrust before erupting into Owen's mouth,{w=.3} my pucker squeezing tightly around his fingers as he pushed against my prostate, milking every drop."
        "Owen moaned swallowing squirts before pulling back."
        "His mouth was open in an eager grin as ropes of hot cum splattered across his face and onto my stomach."
        "My legs suddenly gave out and I collapsed onto the table,{w=.3} shaking and struggling to catch my breath in the afterglow."
        "Owen looked pleased with himself with his face covered in cum."
        "I yelped as he traced lazy circles around my sensitive tip with a slick finger."
        o "Well what do you think?{w=.3} Is my bodyguard pleased with my performance?"
        "I struggled to sit up,{w=.3} still shaking and utterly exhausted."
        m "T-that was.......{w=.3}wow."
        o "Hehe, {w=.3}glad you enjoyed yourself."
        o "Let me know if you want some more \"service\" in the future.{w=.3} I don't mind keeping my bodyguard happy~"
        m "Haha.......I wouldn't mind being serviced more often."
        m "You better clean up though.{w=.3} You can't walk out with your face like that."
        o "It's evidence of a job well done!{w=.3} I'd gladly wear this outside."
        m "{i}No, you won't.{/i}"
        $ owen_blow == "true"
        scene gym breakroom with Dissolve(2.0)
        
        show owen naked with dissolve
        o "Alright alright fine,{w=.3} I'll wash it off."
        o "Gotta shower after my gym workout anyway."
        "Owen chuckled as he got up to gather our clothes from the corner of the room."
        o "Are you just going to stay there like that?"
        m "What do you mean?"
        o "You look so hot sitting there.{w=.3} Just sprawled naked across a table with your legs spread like that."
        o "I'm glad I got someone like like you for a bodyguard~"
        "My face flushed.{w=.3} I grabbed a nearby pair of shorts and tossed in into Owen's face."
        m "J-just go get yourself cleaned up!"
        "Owen laughed as he ducked out of the room."
        o "Alright I'm going, I'm going!"
        m "{i}Put your pants back on first!{/i}"
        
stop music fadeout 2
scene black with Dissolve(3.0)
play music "clear-air.mp3" fadein 2
scene gym with Dissolve(2.0)


"I sat by the window of the gym and stared outside into the courtyard absentmindedly."
"Owen sure is taking forever to shower."
"Being in a gym makes the waiting worse.{w=.3} I feel like a fish out of water here."
"A fish that's aggressively allergic to physical exercise."

m "Hm?"
"Two familiar figures outside suddenly caught my eye."
"Jinny and Phillip were scuttling across the courtyard in possibly the most suspicious way possible."
"They were tailing a rather oblivious and absent-minded parent wandering aimlessly through the courtyard."
"Upon closer inspection,{w=.3} Phillip and Jinny looked equally clueless as they hid behind a shrub and spied on the parent not-so-subtlely."

"Curiosity and boredom got the better of me.{w=.3} I reached for my phone and quietly dialed their number."
play sound "phone.wav"
"....................................."
p "-Oh god,{w=.3} who is it now?"
j "Calm down it's just [charname]."
j "Heyo ghostbuster!{w=.3} Are you finally considering giving us a hand?"
m "Nah, I saw you guys floundering around from my window and wanted to see how you were doing."
p "If you're so close then why don't you come out and help us?"
m "I've got my duties as a loyal bodyguard! {w=.3}I can't just abandon Owen in his time of need!"
m "Anywho, how's the search for Owen's dad going?"

scene courtyard dusk with Dissolve(2.0)

show jinny neutral at left
show phillip no at right
with dissolve

j "Well do you want the good news or the bad news?"
p "We have good news?"
m "Let's try and stay positive, fellas."
j "The good news is that we found Oleander Lorelei!{w=.3} He's standing right over there in the courtyard."
j "And the bad news is that I have no earthly idea how we're going to pull this off."
j "Haha get it?{w=.3} {i}Pull{/i} this off?{w=.3} As in, we're suppose to make him-"
show phillip neutral with dissolve
p "Punning is {i}my{/i} job."
p "In all seriousness,{w=.3} how the hell does Morse expect us to take everything off his person?"
j "We could try knocking him out and stuffing him in a broom closet somewhere."
p "This man is the leader of a mafia family who practically owns half the city. {w=.3} We're gonna die if he catches us."
j "We'll just do it from behind so he doesn't see us!{w=.3} One brick to the head and we're good to go!"
show phillip no with dissolve
p "We're here to steal all his shit,{w=.3} not murder him."
p "Look at this old fart! {w=.3}He's like a withered stick!{w=.3} Does it look like he'd survive a blow to the head?"
p "He dresses like an old fart too.{w=.3} How many layers is he wearing under that suit?{w=.3} And he's talking on a flip-phone too."
j "Are we sure he's even the right guy?{w=.3} Owen's dad is supposed to be in his late 40s or something right?"
j "This guy looks ancient.{w=.3} And kinda underwhelming to be honest."

m "You guys are being awful to the poor man.{w=.3} It's not his fault he's old."
j "Old...?"
j "Wait!{w=.3} I got an idea!"
p "...I don't really trust your ideas, Jinny."
j "It'll be perfect!{w=.3} Just follow my lead hehe...."


jump credits
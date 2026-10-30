MW="moodboards/web/"
R="renders/r2/"
P=[]
def piece(**k): P.append(k)

piece(id="S1",lane="Streetwear",name="It Came From the Great Salt Lake",
 idea="A half-inch brine shrimp blown up into a 1950s creature-feature monster rearing out of the pink north arm toward an all-ages crowd with X's on their hands. Band-merch logic, two inks, faded.",
 sketch=R+"streetwear-02-it-came-from-the-great-salt-lake-tee.jpg",
 design_refs=[(MW+"streetwear/04-online-ceramics-slaughterhouse-longsleeve.jpg","style ref: horror type, red on black, sleeve hits"),(MW+"streetwear/01-online-ceramics-grateful-60-longsleeve.jpg","style ref: lot-tee illustration density"),(MW+"streetwear/29-flickr-flyer-a.jpg","style ref: hand-lettered flyer, marker on pink"),(MW+"objects/50-brine-shrimp-dwr.jpg","subject ref: the real animal")],
 mj="vintage screen print t-shirt graphic, 1950s drive-in creature feature poster crossed with a xeroxed 1980s punk show flyer, a gigantic brine shrimp (Artemia, segmented translucent body, feathery leaf-like legs, two eyes on stalks, forked tail) rearing out of a pink salt lake, low desert mountains, a crowd of tiny punks below with X's on the backs of their raised hands, loose gnarly brush and ink, heavy halftone, photocopier grain, two inks only black and faded salmon pink, drippy hand-lettered title \"IT CAME FROM THE GREAT SALT LAKE\", flat artwork on plain off-white paper, no garment",
 mj_params="--ar 4:5 --v 7 --style raw --stylize 250 --sref [upload the 3 style refs] --sw 300",
 shot_refs=[(MW+"streetwear/07-pleasures-suburbs-longsleeve-lookbook.jpg","on-body framing"),(MW+"streetwear/09-stray-rats-homepage-2026.jpg","flash, worn not styled")],
 gemini=["Take the attached graphic (image 1) and print it as a 2-color water-based screen print, slightly cracked and sun-faded, across the front of a heavyweight boxy cream 7 oz t-shirt. Shoot it as a flat lay on pale concrete in soft window light, like a premium vintage-band-tee product page. Keep every letter of the title exactly as in the graphic. No other text, no logos.",
         "Same shirt, worn: a skinny 20-something with a buzzcut standing against a sticker-covered venue door at night, on-camera flash, candid, styled like the attached reference (image 2). The print must match image 1 exactly. Salt Lake mountains faintly visible down the street."],
 text="IT CAME FROM THE GREAT SALT LAKE",
 note="If Midjourney garbles the title, run it without text and have Gemini add the title in drippy B-movie hand lettering.")

piece(id="S2",lane="Streetwear",name="Nothing To Do In Salt Lake (hoodie, one phrase only)",
 idea="One sentence in the layout of the SLC Punk! poster: a black title bar with NOTHING TO DO, an empty electric-blue flood, IN SALT LAKE along its bottom edge. The empty blue is the nothing. Ink body, blue-lined hood. Only this phrase, per your note.",
 sketch=R+"streetwear-03-nothing-to-do-in-salt-lake-hoodie.jpg",
 design_refs=[(MW+"streetwear/36-slc-punk-poster.jpg","layout and palette ref"),(MW+"streetwear/08-pleasures-freak-tee-glitter.jpg","phrase-first single hit"),(MW+"streetwear/05-brain-dead-sunn-o-tee.jpg","print texture")],
 mj="screen print chest graphic for a black hoodie, late 1990s indie punk movie poster layout, a thick black title bar with two thin cream rules beneath it, condensed bold cream letters \"NOTHING TO DO\", below it a large flat electric royal blue rectangle with a dry brushed uneven screen-print edge left intentionally empty, small condensed cream letters \"IN SALT LAKE\" along the bottom edge of the blue, slightly cracked plastisol texture, flat artwork on black, no garment",
 mj_params="--ar 4:5 --v 7 --style raw --stylize 100 --sref [upload the poster ref] --sw 200",
 shot_refs=[(MW+"streetwear/07-pleasures-suburbs-longsleeve-lookbook.jpg","lookbook framing"),(MW+"streetwear/22-flickr-kilby-c.jpg","grainy black and white load-in mood")],
 gemini=["Print the attached graphic (image 1) on the chest of a washed near-black 14 oz heavyweight hoodie with an electric royal-blue fleece-lined hood. Flat lay on pale concrete, soft window light, real fleece texture, premium streetwear product photo. Letters must read exactly NOTHING TO DO and IN SALT LAKE. No other text.",
         "Same hoodie worn by someone carrying an amp through a sticker-covered back door of a small all-ages venue, hood down so the blue lining shows, grainy flash photo like the attached reference (image 2). The print must match image 1 exactly."],
 text="NOTHING TO DO / IN SALT LAKE",
 note="GPT image already nailed a version of this one (deck/mockups/model/02-nothing-to-do-hoodie-gpt-a.png). Use it as a fallback design source if Midjourney's type is weak.")

piece(id="P1",lane="Performance",name="Five A.M.",
 idea="\"Nobody is watching at 5 a.m. That is the point.\" stacked huge across the chest of a bonded technical longsleeve in reflective film: grey on navy by day, white in a headlamp. The garment only says it when nobody is watching.",
 sketch=R+"performance-01-five-am-bonded-longsleeve.jpg",
 design_refs=[(MW+"performance/49-nike-1990-group-therapy-ad.jpg","copy layout ref: stacked condensed type"),(MW+"performance/50-nike-1990-stress-management-ad.jpg","copy voice ref"),(MW+"performance/24-satisfy-mothtech-logo-detail.jpg","technical fabric ref")],
 mj="typographic chest graphic for a running shirt, 1990 Wieden+Kennedy Nike print ad style, five stacked lines of very bold extra-condensed sans serif caps \"NOBODY / IS WATCHING / AT 5 A.M. / THAT IS / THE POINT.\" ragged center, printed in silver-grey retroreflective film, flat artwork on deep navy, no garment, no logo",
 mj_params="--ar 4:5 --v 7 --style raw --stylize 50 --sref [upload the two 1990 Nike ads] --sw 150",
 shot_refs=[(MW+"performance/07-district-vision-lab-tights-film.jpg","flat cold film light"),(MW+"performance/20-bst-trail-runner-deseret-2025.jpg","the Bonneville Shoreline above the grid")],
 gemini=["Apply the attached type (image 1) as a reflective heat-transfer print across the chest of a slim navy bonded technical longsleeve running shirt with laser-perforated underarm panels. Daylight product shot on a hanger against a concrete wall, cold flat light, film grain like image 2. The type reads exactly as in image 1 and looks quiet silver-grey by day.",
         "Same shirt worn by a runner on a dirt trail above Salt Lake City before dawn, city lights below, mountains dark behind, photographed with a headlamp and on-camera flash so the reflective type on the chest blazes bright white. Documentary running photography. Text exactly as image 1."],
 text="NOBODY IS WATCHING AT 5 A.M. THAT IS THE POINT.",
 note="Make both the day shot and the headlamp shot. The flip between them is the product.")

piece(id="P2",lane="Performance",name="Gain",
 idea="An Alpha Direct quarter-zip in Rodeo Red with one bonded strip running hem to collar beside the zip. The only type is 4,807, set tall and reading upward: the vertical from the valley floor to Mount Olympus.",
 sketch=R+"performance-02-gain-alpha-pullover.jpg",
 design_refs=[(MW+"performance/21-polartec-alpha-direct-swatch.jpg","the fabric: lofted grid"),(MW+"performance/36-nike-acg-lava-loft-official.jpg","hot technical color, serif-free restraint"),(MW+"performance/03-arcteryx-system-a-drop6-fieldmag.jpg","design-forward technical")],
 mj="product design concept, a lofted grid-fleece quarter-zip pullover in rodeo red (#A42F2C), Polartec Alpha Direct open-grid knit visible, raglan sleeves, a single narrow cream bonded nylon strip running vertically from the hem to the collar beside the zipper, on the strip the number \"4,807\" set tall in a condensed sans and rotated to read upward, nothing else printed, studio product photo on light grey",
 mj_params="--ar 4:5 --v 7 --style raw --stylize 100 --sref [upload ACG Lava Loft and Arc'teryx System_A] --sw 150",
 shot_refs=[(MW+"performance/03-arcteryx-system-a-drop6-fieldmag.jpg","movement, design-led outdoor"),(MW+"performance/43-blackdiamond-lcc-home-crag.jpg","Little Cottonwood granite")],
 gemini=["Use the garment in image 1. Product photo on a hanger against warm grey, the lofted grid fabric shown honestly with a macro inset of the strip. The number reads exactly 4,807, reading upward. No other text or logos.",
         "Same pullover worn by a climber at the base of the granite walls of Little Cottonwood Canyon, Utah, mid-movement, cold morning light, editorial outdoor photography like image 2. Strip and number exactly as image 1."],
 text="4,807",note="")

piece(id="O1",lane="Objects",name="Two Arms (board rack with a fossil pattern)",
 idea="A 30-inch white oak wall rail with two felt-topped arms holding a snowboard. Per your note: a pattern of local fossils lines the whole rail face, the brine shrimp is one of many.",
 sketch=R+"objects-01-two-arms-rack.jpg",
 design_refs=[(MW+"objects/50-brine-shrimp-dwr.jpg","the shrimp, one of the fossils"),(MW+"objects/32-great-salt-lake-salt-crystals-imaggeo.jpg","lake material"),(MW+"objects/23-loewe-craft-prize-2025-winner-aoki.jpg","craft object quality")],
 mj="seamless horizontal repeat pattern of natural history fossil engravings for laser engraving on wood: Lake Bonneville freshwater snails and clams, a fossil fish, a mammoth tooth, an Allosaurus claw, brine shrimp cysts and a brine shrimp, fine 19th century zoological plate linework, single color dark brown burn on pale white oak, evenly spaced, long strip format",
 mj_params="--ar 12:1 --v 7 --style raw --tile --stylize 150",
 shot_refs=[(MW+"objects/06-parksproject-brass-french-press.jpg","hero-object still life"),(MW+"objects/47-district-vision-annapurna-eyewear-pouch.jpg","clean premium product light")],
 gemini=["Make a product photograph of a 30-inch solid white oak wall rail with two felt-topped oak arms, mounted on a plaster wall, holding a snowboard laid across it. The front face of the rail is laser-engraved along its full length with the attached fossil pattern (image 1), a warm brown burn into pale oak. Soft daylight, premium home-goods still life like image 2.",
         "Close-up of the same rail face, the engraved fossils filling the frame, raking light so the burn reads as texture."],
 text="(none)",note="Midjourney's --tile makes the pattern repeat cleanly. Verify which fossils are truly from the Salt Lake area before the hangtag copy; Allosaurus is Utah's state fossil but comes from Emery County.")

piece(id="O2a",lane="Objects",name="Field Recordings, Great Salt Lake: Version A, Spiral Jetty wrap",
 idea="A 12-inch LP of ten real Salt Lake sounds. Per your note: the Spiral Jetty spiral wraps around the whole sleeve, not an inset. Split pink-over-blue vinyl.",
 sketch=R+"objects-02-field-recordings-lp.jpg",
 design_refs=[(MW+"objects/31-spiral-jetty-uibel-aerial.jpg","subject: the jetty from above"),(MW+"objects/21-nasa-iss-great-salt-lake.jpg","palette: pink north arm, blue south arm"),(MW+"objects/54-a24-primetime-vinyl.jpg","sleeve restraint")],
 mj="12 inch vinyl record sleeve design, square, an aerial view of a basalt rock spiral in pink salt water, the spiral wraps around the whole cover and continues off the edges, salt crust white on its rim, small restrained serif title \"Field Recordings, Great Salt Lake\" set in the lower corner, art book sleeve, matte uncoated paper",
 mj_params="--ar 1:1 --v 7 --style raw --stylize 200 --sref [upload the jetty aerial and the NASA lake] --sw 200",
 shot_refs=[(MW+"objects/54-a24-primetime-vinyl.jpg","record product shot")],
 gemini=["Product photo of a 12-inch LP: the sleeve uses the attached cover art (image 1) exactly, with the record half pulled out showing split pink-over-blue colored vinyl and a center label with a small spiral. On a wooden record console in soft afternoon light, styled like image 2. Title text exactly as in image 1."],
 text="Field Recordings, Great Salt Lake",note="Needs Holt/Smithson Foundation permission before it ships. Version B is the no-permission fallback.")

piece(id="O2b",lane="Objects",name="Field Recordings, Great Salt Lake: Version B, Wasatch overhead",
 idea="The Salt Lake County-specific alternate you asked for: an overhead view of the Wasatch as texture, forest green on the high slopes, desert tan below the old Bonneville shoreline, the canyons cut through it.",
 sketch=R+"objects-02-field-recordings-lp.jpg",
 design_refs=[(MW+"performance/17-nasa-lake-effect-slc-2001.jpg","satellite view of the Wasatch Front"),(MW+"objects/21-nasa-iss-great-salt-lake.jpg","overhead palette")],
 mj="12 inch vinyl record sleeve design, square, a satellite overhead view of the Wasatch mountains above Salt Lake County as an abstract texture, dark forest green on the high slopes fading to pale desert tan along a sharp horizontal bench line, deep canyons cutting through, faint city grid at the valley edge, topographic and painterly, small restrained serif title \"Field Recordings, Great Salt Lake\" in a corner, matte uncoated paper",
 mj_params="--ar 1:1 --v 7 --style raw --stylize 250 --sref [upload the NASA Wasatch image] --sw 150",
 shot_refs=[(MW+"objects/54-a24-primetime-vinyl.jpg","record product shot")],
 gemini=["Product photo of a 12-inch LP with the attached sleeve (image 1), record half pulled out showing split green-over-tan colored vinyl, on a wooden console, soft afternoon light, styled like image 2. Title exactly as in image 1."],
 text="Field Recordings, Great Salt Lake",note="")

piece(id="O3",lane="Objects",name="Artemia (keys and transit pouch)",
 idea="A veg-tan leather zip pouch whose only mark is a natural-history drawing of Artemia franciscana, blind-debossed. No ink, no logo.",
 sketch=R+"objects-03-artemia-pouch.jpg",
 design_refs=[(MW+"objects/50-brine-shrimp-dwr.jpg","the real animal"),(MW+"objects/36-ald-leather-keychain-pouch.jpg","product form")],
 mj="19th century zoological engraving plate of a single brine shrimp Artemia franciscana in profile, eleven pairs of leaf-shaped legs fanned along the body, eyes on stalks, long tapering forked tail, ultra fine copperplate linework, black ink on white, no text, isolated",
 mj_params="--ar 3:1 --v 7 --style raw --stylize 100",
 shot_refs=[(MW+"objects/36-ald-leather-keychain-pouch.jpg","ALD pouch still life"),(MW+"objects/47-district-vision-annapurna-eyewear-pouch.jpg","premium accessory light")],
 gemini=["Blind-deboss the attached engraving (image 1) into the front of a small natural vegetable-tanned leather zip pouch with a brass zipper and swivel hook. No ink, no foil, the impression slightly darker and catching highlight on its edges. On linen with brass keys and a transit card, styled like image 2. No text."],
 text="(none)",note="GPT image already made a strong version (deck/mockups/model/03-artemia-pouch-gpt-a.png). Use it as a shot reference.")

piece(id="W1",lane="Neo-Western",name="Paintbrush Yoke Shirt",
 idea="A Mountain Navy brushed-twill snap shirt with one chain-stitched cluster of Indian paintbrush and lupine on the back yoke, and nothing else. Albion Basin stitched in script inside the left cuff.",
 sketch=R+"western-01-paintbrush-yoke-shirt.jpg",
 design_refs=[(MW+"western/11-fort-lonesome-chainstitch-machine.jpg","chain-stitch craft"),(MW+"western/23-albion-basin-indian-paintbrush.jpg","the real flowers"),(MW+"western/06-fort-lonesome-texas-suit.jpg","chain-stitch density")],
 mj="chain stitch embroidery design, a small cluster of Indian paintbrush flowers in red and orange and purple-blue lupine with sage green stems, looped chain stitch texture following each petal, western yoke motif, embroidered on deep navy brushed twill, close-up",
 mj_params="--ar 4:3 --v 7 --style raw --stylize 200 --sref [upload Fort Lonesome refs] --sw 250",
 shot_refs=[(MW+"western/03-ginew-western-snap-chambray.jpg","golden hour, back of the shirt"),(MW+"western/18-ginew-gently-strikes-wild-rag-portrait.jpg","natural-light portrait")],
 gemini=["Put the attached chain-stitch embroidery (image 1), about 4.5 inches wide, centered on the back yoke of a Mountain Navy brushed-twill western snap shirt with pearl snaps. Shot from behind on a person at golden hour in a mountain meadow with wildflowers, like image 2. The front of the shirt is plain. No text."],
 text="(none; cuff script 'Albion Basin' is a detail shot)",note="Optional detail shot: the rolled left cuff showing 'Albion Basin' chain-stitched in script.")

piece(id="W2",lane="Neo-Western",name="Island Herd Chore Coat",
 idea="A plain waxed Forest canvas chore coat. Open it and the lining is a half-square-triangle quilt in Cream, Sego Lily, Aspen Gold, Terracotta and Rodeo Red. One leather patch: a bison, Antelope Island, 1893.",
 sketch=R+"western-02-island-herd-chore-coat.jpg",
 design_refs=[(MW+"western/05-bode-homer-quilt-jacket.jpg","quilt logic"),(MW+"western/22-antelope-island-roundup-riders-herd.jpg","the herd")],
 mj="half-square-triangle patchwork quilt pattern, cream, pale sego yellow, aspen gold, terracotta and rodeo red cotton, hand-quilted channel stitching, slightly faded antique quilt, flat lay, seamless",
 mj_params="--ar 1:1 --v 7 --style raw --tile --stylize 150 --sref [upload the Bode quilt jacket] --sw 200",
 shot_refs=[(MW+"western/05-bode-homer-quilt-jacket.jpg","Bode product shot"),(MW+"western/08-tecovas-boot-truck-window.jpg","faceless lifestyle framing")],
 gemini=["Product photo of a waxed cotton canvas chore coat in deep forest green, hung open on a wooden hanger against a cedar plank wall so the lining shows: the lining is the attached quilt (image 1). A small debossed veg-tan leather patch on the chest pocket with a bison silhouette and the words 'ANTELOPE ISLAND' and '1893'. Natural light, styled like image 2.",
         "Same coat worn closed by a rancher leaning on a truck, faceless crop, quilt lining peeking at the open hem, Great Salt Lake flats behind."],
 text="ANTELOPE ISLAND · 1893",note="1893 is the year bison came to the island.")

piece(id="W3",lane="Neo-Western",name="Main Street Drive Wild Rag (green)",
 idea="A 22-inch wild rag with one single-color drawing: longhorns and riders coming down Main Street, downtown towers and the Wasatch behind. Sage line on Forest ground, the colorway you preferred.",
 sketch=R+"western-03-main-street-drive-wild-rag.jpg",
 design_refs=[(MW+"western/22-antelope-island-roundup-riders-herd.jpg","riders and herd"),(MW+"western/21-antelope-island-roundup-rider-glove.jpg","detail-first craft")],
 mj="single color line illustration for a silk scarf, a herd of longhorn cattle driven down a wide city main street by cowboys on horseback, downtown towers and two rugged mountain ridgelines behind, dust in the air, old western engraving linework, sage green ink on deep forest green ground, square scarf with a thin border, the words \"PIONEER DAY\" small in a western serif in one corner",
 mj_params="--ar 1:1 --v 7 --style raw --stylize 200",
 shot_refs=[(MW+"western/18-ginew-gently-strikes-wild-rag-portrait.jpg","the wild rag as the color hit")],
 gemini=["Print the attached art (image 1) on a 22-inch square silk twill wild rag, sage green on forest green. Show it tied loosely at the throat of a person in a plain chambray shirt, natural light portrait outdoors, styled like image 2. Also show a flat lay of the full square. Text exactly 'PIONEER DAY'."],
 text="PIONEER DAY",note="The real drive photo on the mood board was a bad scrape; if you have the Church News gallery image, add it as a subject reference.")

piece(id="L1",lane="Latino",name="Club Deportivo Salt Lake jersey (home and alt)",
 idea="A supporters' jersey for a club that is the city itself: crest with a brine shrimp over the Wasatch ridge, 801 at the foot, neighborhood stars on the sleeves, SALT LAKE arched over 801 on the back. Home is Salt Pink and Forest, the colorway you preferred; also make the Rodeo Red and Navy alt.",
 sketch=R+"latino-01-club-deportivo-salt-lake-jersey.jpg",
 design_refs=[(MW+"latino/09-paisaboys-club-deportivo-tee.jpg","club-badge logic"),(MW+"latino/03-bxr-worldwide-mexico.jpg","jersey numbering"),(MW+"latino/07-koi-nike-jersey.jpg","jersey as fashion")],
 mj="football supporters jersey design, salt pink body with deep forest green collar and trim, an embroidered circular club crest on the chest with a stylized brine shrimp over a mountain ridge and the number 801, small stars on the sleeves, the back with \"SALT LAKE\" arched in blackletter over a big tackle-twill \"801\", front and back flat lay",
 mj_params="--ar 4:5 --v 7 --style raw --stylize 150 --sref [upload Paisa Boys and Born x Raised refs] --sw 200",
 shot_refs=[(MW+"latino/13-estevan-oriol-lamag.jpg","high-contrast portrait, car in frame"),(MW+"latino/19-sltrib-lowrider-urban-arts-2019.jpg","lowrider downtown with the city behind")],
 gemini=["Make the jersey in image 1 a real garment: salt pink mesh with forest green trim, embroidered crest, tackle-twill SALT LAKE and 801 on the back. Worn by someone leaning on a lowrider in downtown Salt Lake City with the mountains behind, high-contrast portrait in the style of image 2. Text exactly SALT LAKE and 801.",
         "Flat lay of the home jersey next to the alt: rodeo red body with mountain navy trim, same crest and numbering."],
 text="SALT LAKE · 801",note="Starting brief for Latino designers from Salt Lake County; La Barra Real in the room before a sample.")

piece(id="L2",lane="Latino",name="Vecino",
 idea="One word, neighbor, across the chest in a single fine hand-drawn line in the Mister Cartoon tradition. Vecina on the women's cut. 801 at the back neck.",
 sketch=R+"latino-02-vecino-fine-line-tee.jpg",
 design_refs=[(MW+"latino/25-mister-cartoon-by-oriol-1994.jpg","fine-line lettering hand"),(MW+"latino/01-bxr-hyna-tee.jpg","one word, set huge")],
 mj="hand lettered fine line script word \"Vecino\", single weight hairline chicano tattoo lettering, elegant flourishes, the tail of the last letter swinging under the word as an underline, white ink on black, flat",
 mj_params="--ar 3:1 --v 7 --style raw --stylize 150 --sref [upload the Mister Cartoon ref] --sw 250",
 shot_refs=[(MW+"latino/13-estevan-oriol-lamag.jpg","black and white Oriol portrait"),(MW+"latino/20-ksl-utah-lowrider-community.jpg","real families, lowrider culture")],
 gemini=["Print the attached lettering (image 1) across the chest of a heavyweight black t-shirt in white water-based ink. Black and white portrait of a man in his 30s in a front yard in West Valley, Utah, a lowrider in the driveway, shot in the style of image 2. The word reads exactly Vecino.",
         "Same design on a women's cut reading Vecina, flat lay."],
 text="Vecino / Vecina",note="A community letterer draws the final; this is direction.")

piece(id="L3",lane="Latino",name="Lotería Salt Lake",
 idea="Six lotería cards on the back of a black tee, every card a Salt Lake thing: El Trax, La Montaña, El Taco, La Sal, El Camarón, La Troca. El Camarón alone on the chest.",
 sketch=R+"latino-03-loteria-salt-lake-tee.jpg",
 design_refs=[(MW+"latino/47-loteria-boards.jpg","card format"),(MW+"latino/26-cdmx-rotulos-zocalo.jpg","rótulo lettering and color")],
 mj="a grid of six illustrated lotería cards, traditional Don Clemente style, flat bright spot colors, each card numbered top left with its name in a lotería serif at the bottom: \"EL TRAX\" a light rail train, \"LA MONTAÑA\" a snowy mountain, \"EL TACO\" a street taco, \"LA SAL\" a salt crystal, \"EL CAMARÓN\" a brine shrimp, \"LA TROCA\" a lowrider pickup, card stock texture",
 mj_params="--ar 3:2 --v 7 --style raw --stylize 200 --sref [upload the lotería boards] --sw 250",
 shot_refs=[(MW+"latino/46-fuerza-regida-kidsuper-paris.jpg","norteño meets streetwear"),(MW+"latino/12-vivalabonita-alacrana-tee.jpg","brand product shot")],
 gemini=["Print the attached card grid (image 1) as a multi-color screen print on the back of a heavyweight black t-shirt. Back view, worn at a Mexican Independence Day celebration in Salt Lake City at dusk, string lights, candid, styled like image 2. Card names spelled exactly as in image 1.",
         "Flat lay of the front: a single El Camarón card on the left chest."],
 text="EL TRAX · LA MONTAÑA · EL TACO · LA SAL · EL CAMARÓN · LA TROCA",note="If the illustrator isn't from here, cut it.")

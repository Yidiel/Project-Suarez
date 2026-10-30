# Mockup log

## S1, It Came From the Great Salt Lake

Status: done. Design, flat lay and worn shot all pass.

Files: `S1-mj.png` (Midjourney design, 1920x2400), `S1-shot-1.png` (flat lay), `S1-shot-2.png` (worn), `S1-sketch-crop.jpg` (image prompt).

### Midjourney

Image prompt: `S1-sketch-crop.jpg`, a crop of just the poster art from `renders/r2/streetwear-02-it-came-from-the-great-salt-lake-tee.jpg`. The full presentation board includes a headline, body copy and garment outlines that would bleed into the design, so only the art panel was used.

Run 1 (failed). Prompt as on the card, style refs `29-flickr-flyer-a`, `04-online-ceramics-slaughterhouse-longsleeve`, `01-online-ceramics-grateful-60-longsleeve`, `--sw 300`. Title garbled, the Grateful 60 ref pulled in fake sponsor logos and a blue third ink, and two of four came out as shirt photos.
Job: https://www.midjourney.com/jobs/dbc0e716-3881-4178-80f5-31c371a3b38c

Run 2 (picked). Dropped the Grateful 60 ref, lowered style weight, removed the title so Gemini could set it exactly (per the card note):

```
flat vintage screen print artwork, 1950s drive-in creature feature poster crossed with a xeroxed 1980s punk show flyer, a gigantic brine shrimp (Artemia, segmented translucent body, feathery leaf-like legs, two eyes on stalks, forked tail) rearing out of a pink salt lake, low black desert mountains, a crowd of tiny punk silhouettes below with white X's on the backs of their raised hands, empty halftone sky across the top third for a title, loose gnarly brush and ink, heavy halftone dots, photocopier grain, two inks only black and faded salmon pink on plain off-white paper, poster artwork only, edge to edge --ar 4:5 --v 7 --style raw --stylize 250 --sw 150 --no text, letters, words, typography, logos, sponsor logos, t-shirt, garment, clothing, blue
```

Style refs: `29-flickr-flyer-a`, `04-online-ceramics-slaughterhouse-longsleeve`. Image prompt: `S1-sketch-crop.jpg`.
Job: https://www.midjourney.com/jobs/ed7ff7bf-d54f-4243-94cd-5180b1d78127 (variant 2, index 1)
Upscale (Subtle): https://www.midjourney.com/jobs/8af61cf7-b221-45d0-b392-0882fee5a10b

Why variant 2: the clearest read of the card's subject. Stalked eyes, forked tail, the shrimp rising out of a pink lake with dark mountains behind, and a clean row of X'd hands. Two inks only. Its lettering was still junk (the sketch carries type), so Gemini replaced all of it.

### Gemini (Nano Banana, Images tool)

Chat inputs in order: image 1 `S1-mj.png`, image 2 `07-pleasures-suburbs-longsleeve-lookbook.jpg`, image 3 `09-stray-rats-homepage-2026.jpg`.

Shot 1, first attempt passed:

```
Take the attached graphic (image 1) and print it as a 2-color water-based screen print, slightly cracked and sun-faded, across the front of a heavyweight boxy cream 7 oz t-shirt. Keep the brine shrimp monster, the pink lake, the mountains and the crowd with X's on their hands exactly as drawn in image 1. Replace all of the lettering in image 1: the only text on the shirt is the title IT CAME FROM THE GREAT SALT LAKE, in drippy 1950s B-movie hand lettering in the black and salmon pink inks, across the top. Spell every letter exactly: IT CAME FROM THE GREAT SALT LAKE. Remove every other word, badge and small text block from the graphic. Shoot it as a flat lay on pale concrete in soft window light, like a premium vintage-band-tee product page. No other text, no logos.
```

Shot 2, passed on attempt 3. Attempt 1 vanished with no response and attempt 2 returned "Something went wrong". Both used the card prompt plus a line keeping the door stickers wordless. Attempt 3 asked for an invented model and used image 2 for framing only, which is likely what cleared it:

```
Now show that same cream t-shirt being worn. Invent a new model, a skinny 20-something with a buzzcut, not anyone from the reference photos. They stand against a door covered in plain colored stickers and doodles outside a small music venue at night, lit by harsh on-camera flash, candid snapshot feel. Use image 2 only as a guide for framing and casual styling. The shirt print must be identical to the flat lay you made, title IT CAME FROM THE GREAT SALT LAKE spelled exactly. A faint mountain silhouette down the street. No readable words anywhere else, no logos.
```

Checks: title exact in both shots, print matches image 1, no brand logos, nothing from the banned list.

Notes: shot 2 has a cropped sign fragment ("...NER") at the top of the door and doodle tags. No brand marks. Gemini rendered the lake as a pink field with black outline, slightly flatter than the Midjourney halftone.

## P1, Five A.M.

Status: Midjourney design done. Gemini shots not made: Gemini refused shot 1 three times, so shot 2 (which builds on it) wasn't attempted. Needs a decision before the full run.

Files: `P1-mj.png` (Midjourney film-on-navy art with blank type bars, 1920x2400), `P1-sketch-crop.jpg` (the chest type crop from the concept board).

### Midjourney

Run 1 (failed). Prompt as on the card, style refs `49-nike-1990-group-therapy-ad` and `50-nike-1990-stress-management-ad`, image prompt `P1-sketch-crop.jpg`, `--sw 150`. The copy was garbled in all four, and all four had Nike swooshes pulled in from the style refs.
Job: https://www.midjourney.com/jobs/3f520b11-740d-4eb5-b003-5ef5f71b5605

Run 2 (picked). Per the text rule, the design was made without text, as the reflective-film material and stacked layout, so Gemini could set the exact copy. No refs, to keep swooshes out:

```
flat chest graphic artwork for a technical running shirt, minimal 1990 print ad layout, five stacked horizontal bars of silver-grey retroreflective heat-transfer film, ragged center widths like lines of extra-condensed type, set on deep matte navy, faint micro glass-bead sparkle in the film, crisp edges, quiet and graphic, flat artwork only, edge to edge --ar 4:5 --v 7 --style raw --stylize 50 --no text, letters, words, typography, logo, swoosh, garment, person
```

Job: https://www.midjourney.com/jobs/3e0924db-ea82-4444-849a-8f29ea1f0cc0 (variant 2, index 1)
Upscale (Subtle): https://www.midjourney.com/jobs/94c5f26b-f768-420c-8869-10375d54beaf

Why variant 2: the crispest film edges and the most convincing retroreflective texture on matte navy. Its bar count (eight) doesn't matter because Gemini replaces the bars with the five exact lines.

### Gemini (failed, 3 attempts)

Attempt 1: image 1 `P1-mj.png`, image 2 `07-district-vision-lab-tights-film.jpg`, image 3 `20-bst-trail-runner-deseret-2025.jpg`, image 4 `P1-sketch-crop.jpg` (for exact type layout), with the card's prompt 1 reworded to take the words from image 4. Result: "I seem to be encountering an error."
Attempt 2: same chat, Try again. Result: "I'm having a hard time fulfilling your request."
Attempt 3: fresh chat without the news photo of a real runner (image 1 `P1-mj.png`, image 2 District Vision, image 3 `P1-sketch-crop.jpg`):

```
Product photo of a running shirt. Make a slim navy bonded technical long-sleeve running shirt with laser-perforated underarm panels, hung on a hanger against a concrete wall, cold flat daylight, film grain like image 2. Across the chest is a reflective heat-transfer print made of the silver-grey retroreflective film shown in image 1. The print is five centered lines of very bold extra-condensed capital letters laid out like image 3, reading exactly: NOBODY / IS WATCHING / AT 5 A.M. / THAT IS / THE POINT. Spell every letter and keep both periods. By day the type looks quiet silver-grey. No other text, no logos.
```

Result: "I'm having a hard time fulfilling your request."

Problem: two outright declines and one error, with the real-person photo removed. The likely trigger is the copy itself: "NOBODY IS WATCHING" may read to Gemini's filter as surveillance or stalking. Options for Yid: (a) run P1's shots in a different image model, (b) test whether Gemini accepts the shirt with the type added afterwards in Photoshop or Figma from `P1-sketch-crop.jpg`, (c) approve a one-off test of the line split across two prompts.

## W1, Paintbrush Yoke Shirt

Status: Midjourney design and the back-yoke shot done. The optional "Albion Basin" cuff detail didn't complete (see problems).

Files: `W1-mj.png` (Midjourney embroidery, 2464x1856), `W1-shot-1.png` (back yoke, worn, golden hour), `W1-sketch-crop.jpg` (image prompt: the yoke close-up panel from the concept board).

### Midjourney

Run 1 (failed). Prompt as on the card, style refs `11-fort-lonesome-chainstitch-machine` and `06-fort-lonesome-texas-suit`, image prompts `W1-sketch-crop.jpg` and `23-albion-basin-indian-paintbrush.jpg`, `--sw 250`. All four were full-frame dense meadows in satin stitch, and the card asks for one small chain-stitch cluster. The Albion Basin photo pushed the density.
Job: https://www.midjourney.com/jobs/428123dc-565d-43ec-b7a3-adaf94d0710f

Run 2 (picked). Dropped the meadow photo, kept the Fort Lonesome style refs, image prompt `W1-sketch-crop.jpg` only:

```
chain stitch embroidery design, one small isolated cluster of three Indian paintbrush stems in red and orange with two purple-blue lupine spikes and thin sage green stems, worked entirely in looped single-line chain stitch like a vintage chainstitch machine, rows of visible chain loops following each petal, small western yoke motif centered on a large field of plain deep navy brushed twill with lots of empty fabric around it, close-up flat view --ar 4:3 --v 7 --style raw --stylize 200 --sw 250 --iw 1.5 --no text, letters, logo, satin stitch, meadow, dense field
```

Job: https://www.midjourney.com/jobs/e82f8348-9227-4418-ad10-cac37d864e63 (variant 4, index 3)
Upscale (Subtle): https://www.midjourney.com/jobs/60be233d-bc92-4a76-95cc-c6cbd1123649

Why variant 4: closest to the sketch. Three paintbrush heads over blue lupine spikes on sage stems, with visible chain-stitch loop texture, on navy twill.

### Gemini (Nano Banana, Images tool)

Chat inputs in order: image 1 `W1-mj.png`, image 2 `03-ginew-western-snap-chambray.jpg`, image 3 `18-ginew-gently-strikes-wild-rag-portrait.jpg`.

Shot 1, first attempt passed:

```
Put the attached chain-stitch embroidery (image 1), about 4.5 inches wide, centered on the back yoke of a Mountain Navy brushed-twill western snap shirt with pearl snaps. Keep the paintbrush and lupine cluster and its chain-stitch loops exactly as in image 1. Shot from behind on a person at golden hour in a mountain meadow with wildflowers. Invent a new model, not anyone from the reference photos; use image 2 only as a guide for the warm natural light and framing. The front of the shirt is plain. No text, no logos.
```

Checks: no text, no logos, embroidery matches image 1, placed on the back yoke.

Problems:
- Shot 1 carried over a short stitched seam line from the Midjourney variant (a pocket edge in the source), just left of the stems. Easy to retouch, or rerun with "no seams near the embroidery".
- Optional cuff detail ("Albion Basin" chain-stitched inside the rolled left cuff): attempt 1 vanished from the chat with no response (the same Gemini behavior seen on S1). Attempt 2 was still generating after several minutes when this was logged; see the pilot review note.

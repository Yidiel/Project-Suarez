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

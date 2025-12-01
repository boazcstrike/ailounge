
# LORAS

https://civitai.com/models/273909/picxer
<lora:picxer_real:0.65> it's a realistic enhancer, but like PicX_real, it can be used for sci-fi, fantasy, with different styles and lora (also compatible with PicX_real)
<lora:picxer_bside:0.8> it's a atmosphere enhancer that goes well with the aesthetic of dark shots, gloom, horror, fashion, and similar things
===
https://civitai.com/models/112552/weight-slider-lora
<lora:weight_slider_v2:3>
weight: -3.0 to 3.0
positive: more weight
negative: less weight
===
https://civitai.com/models/13941/epinoiseoffset
<lora:epiNoiseoffset_v2:1>
better contrast and darker images.
Works better if u use good keywords like: dark studio, rim lighting, two tone lighting, dimly lit, low key etc.
===
https://civitai.com/models/76937/hairstyles-collection
lora:short_dreads_hairstyle:0.5>
Sampler: DPM++ SDE Karras (Recommended for best quality, you may try other samplers)
CFG Scale : 5 to 10
===
LORA weight for txt2img: reccomended 0.2-0.5.
https://civitai.com/models/117761/tiny-home-concept
interiortinyhouse
<lora:ARWinteriortinyhouse:1>
===
https://civitai.com/models/82098/add-more-details-detail-enhancer-tweaker-lora
<lora:more_details:0.5>  between 0.5 and 1 weight
===
https://civitai.com/models/58390/detail-tweaker-lora-lora
<lora:add_detail:1> can be utilized for any weight up/down to 2/-2!
===
https://civitai.com/models/264290/styles-for-pony-diffusion-v6-xl-not-artists-styles?modelVersionId=365402
oil painting, traditional media, realistic,

====================================
NSFW
====================================
https://civitai.com/models/12955?modelVersionId=15264
<lora:ak47_7:0.95>
0.85 ~ 1 Recommended
※ Trigger Words: AK-47, AKM, kalashnikov_rifle, assault_rifle, holding_gun
===
https://civitai.com/models/12519/handk-hk416-lora
(holding weapon, aiming at viewer, assault rifle,left view:1.5)
<lora:HK416-v2:0.6>
===
https://civitai.com/models/53983/gun-aiming-at-you-concept
<lora:gunatyou:0.5-0.8>
===
<lora:MS_Real_PantsDown:0.9>
===
https://civitai.com/models/9155/ahegao-rolling-eyesrealistic
0.5~0.95
<lora:ahegao:0.9>
<lora:rolling_eyes:0.9>
===
https://civitai.com/models/244864/realisticandanimesexy-clothing-collection-oror-andyuan
<lora:2B_WhiteDress:0.9>
===
https://civitai.com/models/198860/bikini-collection-by-stable-yogi
Leather CropTop, High Leg Bikini
<lora:Leather_CropTop_High-leg_Panty_By_Stable_Yogi:1>
===
https://civitai.com/models/131864/breast-size-slider
<lora:breastsizeslideroffset:0.1>
===
https://civitai.com/models/106844/orgasming-face-by-edg
edgOrgasm,face focus,
woman with edgOrgasm_face<lora:edgOrgasm_v2:0.75>
===
https://civitai.com/models/264290/styles-for-pony-diffusion-v6-xl-not-artists-styles

This asset is designed to work best with the Pony Diffusion XL model, it will work with other SDXL models but may not look as intended.

CLIP SKIP in ComfyUI

-1 gray picture with noise and spots

-2 picture looks the same as in the preview

If you do not add the CLIP Set Last Layer node, the result will be exactly the same as -2.

(It will not work correctly with other SDXL checkpoints.)

Does not work with any other models!

except Pony Diffusion V6 XL or models with Pony Diffusion V6 XL in the merge!

You can of course use with other models you no one forbids it, but I do not guarantee a good result!

LoRAs without Trigger Words! but there are words used in training! (Some models have Trigger Words)

Tokens that can enhance the style or change it!

Summer Night - dark theme, low light,

Cold Oil/Cold Oil Gothic - oil painting, traditional media, realistic,

Cold Night - dark theme, low light,

Digital Art - digital art, realistic,

Concept Art/Concept Art Twilight - concept art, realistic, & concept art, horror (theme), monochrome, fog, realistic,

Oil Gothic - painting (medium), traditional media, realistic,

Gothic Art - painting (medium), traditional media, realistic,

Line Art - lineart, monochrome, greyscale,

Oil Painting - traditional media, realistic,

Photo/Photo 2 - RAW, photo, realistic,

The previews were made without using ADetailer

TRAINED

Smooth, Anime, Ink, Oil Painting, Photo, Line Art, Summer Days, Gothic Art, Concept Art ,Smooth 2, Anime 2, Digital Art, Rainbow, Photo 2, Cold Night, Cold Oil, Summer Days 2, Summer Night

MERGE

Smooth Anime - Smooth + Anime

Smooth Anime 2 - Smooth 2 + Anime 2

Oil Gothic - Oil Painting + Gothic Art

Concept Art Twilight - Concept Art + Concept Art Dark + Concept Art Negative

Cold Oil Gothic - Cold Oil + Gothic Art Sharp

Styles are based partially or entirely on images created by the AI

https://civitai.com/models/301472/fictional-women-megapack
fic-zoe
Each version features a different person! The trigger word for all models is a woman
Use a weight of 0.8 to 1.
============================
https://civitai.com/models/202866/all-princesses-from-disneys-ralph-2-ralph-breaks-the-internet-or-all-in-one-lora-model

Bonus Characters
Additionally, this model includes representations of other characters like Vanellope, Shank, Raya, Namaari, Asha, and Rapunzel with short hair. While these extras are included, the quality may vary.

Quick Tips
Direct Name Usage: You can summon any princess by directly invoking their names, such as Anna, Ariel, Aurora, Belle, Cinderella, Elsa, Asha, Jasmine, Merida, Moana, Mulan, Namaari, Pocahontas, Rapunzel, Raya, Shank, Snow White, Tiana, Vanellope.

LoRA Scale: Optimal LoRA scales range between 0.6-0.7 for close-up character generation and 0.3-0.5 for full-body generation. Combining these scales using the ADetailer plugin can yield enhanced results. Ensure an adequate number of sampling steps for better output.

Base Models: Although various base models can function, models with animation styles like DreamShaper, RealCartoon, RevAnime, or AnimeMerge are preferred for optimal performance.
# SD Models

## [WildCardX-XL LIGHTNING⚡⚡⚡](https://civitai.com/models/321320/wildcardx-xl-lightning?modelVersionId=360292)

Prompt: simple but detailed prompt
```
Negative: "(worst quality, low quality, normal quality, lowres, low details, oversaturated, undersaturated, overexposed, underexposed, grayscale, bw, bad photo, bad photography, bad art:1.4), (watermark, signature, text font, username, error, logo, words, letters, digits, autograph, trademark, name:1.2), "
```

Steps: 5-7  
Clip Skip: 1-2  
CFG Scale: 1.5-2  
Sampler: Any Sampler but will give good results with DPM++ or DPM++ SDE Karras  
Size: 832 x 1216

Hires upscaler: 4x-UltraSharp, ESRGAN_4x,Lanczos, any of your favorite upscaler.

## [RealCartoon-3D](https://civitai.com/models/94809/realcartoon3d)
Sampling methods DPM++ SDE Karra and DPM++ 2M Karras do well as well.  
Euler A  
sampling steps 40

Hires.fix settings: Upscaler (R-ESRGAN 4x+, 4k-UltraSharp most of the time)  
Hires Steps (10-20)  
Denoising Str (0.34 - 0.45 normally)  
Upscale (1.5 or 2 does well)

## [RealCartoon-Realistic](https://civitai.com/models/97744/realcartoon-realistic)
Width: 512 (normally would not adjust unless I flipped the height and width)  
Height: 768 (Have done up to 1024, but 904 is doing really well)  
Sampling Method: "Eular A", "DPM++ SDE Karra" and "DPM++ 2M Karras"  
Sampling steps: 30-50 normally (30 being my starting point, but going up to 45 a lot of the time)  

Hires.fix settings: Upscaler (R-ESRGAN 4x+, 4k-UltraSharp most of the time)  
Hires Steps (10-20)  
Denoising Str (0.34 - 0.45 normally)  
Upscale (1.5 or 2 does well)  

Clip Skip: 2

## [RealCartoon-Anime](https://civitai.com/models/96629/realcartoon-anime)

Sampling methods DPM++ SDE Karra and DPM++ 2M Karras do well as well.  
Upscaler is either R-ESRGAN 4x+ or 4k-UltraSharp for most of my images.  
Please be careful on the strength you add to LoRas as this can affect the overall look with the checkpoint. Stronger does not always mean better. I normally run 0.4 - 1 strengths depending on the LoRa.  
What is first in your prompt has higher priority.  
Having parathesis increases a priority, but having everything in them is almost as good as typing without them.  
Subtle changes in a prompt (to include punctuation) can change the image  
The seed helps in producing similar images with similar software and settings. It does not guarantee the same image as even a difference in software (I.E. ComfyUI) or hardware can affect it.  
If you want a more cartoon look (at least with this checkpoint) use the following near the front of the prompt: Anime, Cartoon, painted, or comic. This does not guarantee a look depending on the version; but it will lean more that way. This also works for Realistic looks (Realistic, real, etc).  
If you want Safe for work or not nudity to show up then make sure you put the following in your negative prompt: nude, nudity, naked, NSFW, nipples. Of course if you have this in your actual prompt then it will more then likely do it.

The following is what I normally run in a negative prompt (you can click on easynagative or badhandv4 to get the files):
```
easynegative,(badhandv4),(bad quality:1.3),(worst quality:1.3),watermark,(blurry),5-funny-looking-fingers
```

NOTE: Badhandv4 is an embedding. So goes in the embedding folder of A1111


## [RealVisXL V4.0](https://civitai.com/models/139562/realvisxl-v40)

Use Turbo models  
DPM++ SDE Karras sampler  
4-10 steps  
CFG Scale 1-2.5

Use Lightning models  
DPM++ SDE Karras / DPM++ SDE sampler  
4-6 steps  
CFG Scale 1-2

## [AstrAnime](https://civitai.com/models/248011?modelVersionId=334482)

clipskip: 2 (sometimes 1)  
Samplers: 2m karras - eluer a - DIMM  
highres fix: 2x latent / 4x_foolhardy_remacri / R-ESRGAN 4x+ Anime6b

## [Dreamshaper v8](https://civitai.com/models/4384/dreamshaper)

##### LCM  
Being a distilled model it has lower quality compared to the base one. However it's MUCH faster and perfect for video and real time applications.

Use it with 5-15 steps, ~2 cfg. IT WORKS ONLY WITH LCM SAMPLER (as of December 2023, Auto1111 requires an external plugin for it).  
comfyUI - 10 sampling steps  
2.8 cfg


## [Dreamshaper XL](https://civitai.com/models/112902/dreamshaper-xl)
CFG scale 2  
4-8 sampling steps  
DPM++ SDE Karras (NOT 2M)  

You can use this with LCM sampler, but don't do it unless you need speed vs quality.
Sampler comparison at 8 steps: https://civitai.com/posts/951781

UPDATE: Lightning version targets 3-6 sampling steps at CFG scale 2 and should also work only with DPM++ SDE Karras. Avoid going too far above 1024 in either direction for the 1st step.

notes:
* took me around 15 minutes just to make 4 pictures with other samplers

## [JuggernautXL](https://civitai.com/models/133005/juggernaut-xl)
##### Lightning Version:
Res: 832*1216  
Sampler: DPM++ SDE  
Steps: 4-6  
CFG: 1-2  
Negative: Start with no negative, and add afterwards the Stuff you don´t wanna see in that image.  
HiRes: 4x_NMKD-Siax_200k with 2 Steps and 0.35 Denoise + 1.5 Upscale  

##### Recommended Settings for the Normal Version:
Res: 832*1216  
Sampler: DPM++ 2M Karras  
Steps: 30-40  
CFG: 3-7 (less is a bit more realistic)  
Negative: Start with no negative, and add afterwards the Stuff you don´t wanna see in that image. I don´t recommend using my Negative Prompt, i simply use it because i am lazy :D  
VAE is already Baked In  
HiRes: 4xNMKD-Siax_200k with 15 Steps and 0.3 Denoise + 1.5 Upscale  

notes:
* took me almost 30 minutes per photo with the correct settings

## [PicXreal](https://civitai.com/models/241415/picxreal)
This model is less boring-rough and more diverse than the "ultra-realistic" models, and less animesh-asian and more realistic than the "soft-realistic" models. This makes it more balanced, flexible and gives the characters a softer appearance without losing the realistic part.

The flexibility of the model means that a basic understanding of how to write a prompt is required - describe desired main style, main scene, details, effects and artistic techniques, and in response it will show something pleasant. Everything else is traditionally on the preview.
## [AAM-XL-Anime-Mix](https://civitai.com/models/269232/aam-xl-anime-mix)
I suggest you use CFG 5-7 (not higher than 8), 20-30 steps with Euler a.
Upscalers suggestions are None (bicubic upscaling in comfyui), any good GAN for anime or Latent (only if you know what you're doing).
For Turbo I suggest you use CFG 3-4 and 8 steps Euler a or 15 steps LCM.

## [T3 - model for asians](https://civitai.com/models/110053/t3)

## [ChilloutMix - model for asians](https://civitai.com/models/6424/chilloutmix?modelVersionId=11745)

## [MajicMix-realistic - model for asians](https://civitai.com/models/43331/majicmix-realistic?modelVersionId=176425)
推荐参数 Recommended Parameters for V7:  
Sampler: Euler a, Euler, restart  
Steps: 20~40  
Hires upscaler: ESRGAN 4x or 4x-UltraSharp or 8x_NMKD-Superscale_150000_G  
Hires upscale: 2+  
Hires steps: 15+  
Hires denoising strength: 0.05~0.5  
clip skip 2

Sampler: Euler a, Euler, DPM++ 2M Karras (bug-fixed) or DPM++ SDE Karras  
Steps: 20~40  
Hires upscaler: R-ESRGAN 4x+ or 4x-UltraSharp  
Hires upscale: 2  
Hires steps: 15  
Denoising strength: 0.2~0.5  
CFG scale: 6-8  
clip skip 2

## [PonyDiffusionV6XL](https://civitai.com/models/257749/pony-diffusion-v6-xl)
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up and score_8 to score_8, score_7_up, score_6_up, score_5_up, score_4_up

Make sure you load this model with clip skip 2 (or -2 in some software), otherwise you will be getting low quality blobs.

(previous Pony Diffusion models used a simpler score_9 quality modifier, the longer version of V6 XL version is a training issue that was too late to correct during training, you can still use score_9 but it has a much weaker effect compared to full string. You can learn more about these tags here).

The model is designed to **not need negative prompts** **in most cases and does not need other quality modifiers** like `hd`, `masterpiece`, etc...

Other special data selection tags include, `source_pony`, `source_furry`, `source_cartoon` and `source_anime` and ratings of `rating_safe`, `rating_questionable` and `rating_explicit`.

This model is trained on combination of natural language prompts and tags and is capable of understanding both, so describing intended result using normal language works in most cases, although you can add some tags after the main prompt to boost them.

Using Euler a with 25 steps and resolution of 1024px is recommended although model generally can do most supported SDXL resolution.

This model will sometimes generate pseudo signatures that are hard to remove even with negative prompts, this is unfortunately a training issue that would be corrected in future models. If that's an issue for you I suggest trying V5.5 or inpainting

Tokens that can enhance the style or change it!

* Summer Night - dark theme, low light,
* Cold Oil/Cold Oil Gothic - oil painting, traditional media, realistic,
* Cold Night - dark theme, low light,
* Digital Art - digital art, realistic,
* Concept Art/Concept Art Twilight - concept art, realistic, & concept art, horror (theme), monochrome, fog, realistic,
* Oil Gothic - painting (medium), traditional media, realistic,
* Gothic Art - painting (medium), traditional media, realistic,
* Line Art - lineart, monochrome, greyscale,
* Oil Painting - traditional media, realistic,
* Photo/Photo 2 - RAW, photo, realistic,

TRAINED
```
Smooth, Anime, Ink, Oil Painting, Photo, Line Art, Summer Days, Gothic Art, Concept Art ,Smooth 2, Anime 2, Digital Art, Rainbow, Photo 2, Cold Night, Cold Oil, Summer Days 2, Summer Night, Smooth Night
```
MERGE
```
Smooth Anime - Smooth + Anime
Smooth Anime 2 - Smooth 2 + Anime 2
Smooth Anime Night - Smooth Night + Cold Night
Oil Gothic - Oil Painting + Gothic Art
Concept Art Twilight - Concept Art + Concept Art Dark + Concept Art Negative
Cold Oil Gothic - Cold Oil + Gothic Art Sharp
```

## [PPPanime](https://civitai.com/models/230310/pppanime)
CFG scale: 6 to 8  
Denoise 3.5 to 6 (maybe)　SFW : 4 to 6 NSFW : 3.5 to 4.3  
STEP : 40 / highres STEP : 20 / sampler : DPM++3M SDE Karras or DDIM/  
Hires sampling method : DPM++3M SDE

## [ParchartXL](https://civitai.com/models/141471/parchartxl?modelVersionId=318677)
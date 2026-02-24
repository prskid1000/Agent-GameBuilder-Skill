# Asset Prompt Generation for ComfyUI (OpenDUI, Flux Kontext, Chatterbox TTS)

When generating or requesting game assets, produce **independent, complete prompts** suitable for ComfyUI workflows. Each prompt must work standalone (no reliance on other prompts or context). Prefer **one prompt per asset**; for folders with many similar assets, use **one PROMPTS.md per folder** that lists each asset and its full prompt.

---

## 1. OpenDUI / OpenDiT (Text-to-Image)

**Use for:** Sprites, tiles, icons, portraits, environment art, VFX textures.

**Prompt rules:**
- **Plain text** primary description; keep specific and concise.
- Add quality tags: `masterpiece, best quality, 4k` (or `pixel art, 16x16 sprite sheet` for pixel assets).
- Use weight syntax for emphasis: `(keyword:1.2)`.
- Separate concepts with English commas; prefer short phrases over long sentences.
- **One prompt per output image.** Include style, perspective, and technical specs in the same prompt.
- For spritesheet tiles: specify pixel art style, size (e.g. 16x16px), transparent background (PNG), and view (top-down or isometric).

**Per-asset file:** For each image asset, create a `.txt` or `.md` next to it or in a `prompts/` subfolder, e.g. `graphics/characters/hero/prompt_hero_sprite.txt`.

**OpenDiTConditioning (optional):** If the workflow supports it, you can add:
- **Primary prompt:** main description (as above)
- **Aesthetic score:** e.g. 7.5
- **Flow score:** e.g. 5.0

---

## 2. Flux Kontext (Image Edit / Style / Consistency)

**Use for:** Editing existing sprites, style transfer, character consistency across frames, targeted changes (e.g. recolor, add weapon, add hat).

**Prompt rules:**
- **Detailed, specific** edit instructions. Vague prompts give poor results.
- Describe exactly what to change and what to preserve (e.g. "change shirt color to red, keep face and pose unchanged").
- For character consistency: "same character, same style, [specific action or pose]".
- One prompt per edit operation; each prompt must fully define the edit.

**Per-asset or per-batch:** Use one prompt per generated/edited image. For a set of frames, either one PROMPTS.md listing each frame's prompt or one prompt file per frame.

---

## 3. Chatterbox TTS (Text-to-Speech)

**Use for:** Dialogue lines, NPC barks, menu narration, voice-over.

**Prompt rules:**
- **Input = script text** to be spoken. One script per line or per file; each file is one TTS input.
- Use **paralinguistic tags** for reactions: `[laugh]`, `[chuckle]`, `[sigh]`, `[gasp]`, `[cough]`.
- Control **emotion** via API/slider if available: 0.1-0.3 monotone, 1.0 neutral, 1.7-2.0 very expressive.
- **Zero-shot voice:** Reference audio (5-20 s) can define voice; prompt text stays independent and complete for the line itself.

**Per-asset:** One script/prompt per audio file. Store in `audio/prompts/` or next to the target file, e.g. `audio/dialogue/npc_guard_01_line1.txt`.

Keep the **spoken text self-contained**; comments or metadata (emotion, voice ID) can live in the same file or a sidecar JSON.

---

## 4. Where to Put Prompts (Per-Asset vs Per-Folder)

| Approach | When to use | Format |
|----------|-------------|--------|
| **Per-asset** | One image/audio per file; prompts are long or very specific | `graphics/characters/hero/prompt_hero.txt` or `audio/prompts/axe_swing.txt` |
| **Per-folder PROMPTS.md** | Many related assets (e.g. all tiles, all NPC lines, all plant stages) | Single `PROMPTS.md` in folder; each section = asset name + full prompt |

**Per-folder PROMPTS.md template:**
```markdown
# [Folder name] -- ComfyUI prompts

## [asset_name_1]
**Model:** OpenDUI / Flux Kontext / Chatterbox TTS
**Output:** path/to/asset_1.png (or .wav)

[Full standalone prompt here.]

## [asset_name_2]
...
```

Each entry must be **independent and complete**: copy-pasting one block into the model must be enough to reproduce that asset.

---

## 5. Checklist for Every Generated Prompt

- [ ] **Standalone:** No "same as above" or "like the previous"; full description in one place.
- [ ] **Model-specific:** OpenDUI = quality + description; Flux = what to change/preserve; Chatterbox = script + optional tags.
- [ ] **Output target:** Filename or path noted so the pipeline knows where to save.
- [ ] **Technical specs** (for images): resolution, transparency, sprite sheet layout if relevant.

---
---

## 2D Adventure RPG Assets

### OpenDUI Examples

**Pixel art sprite sheet (RPG hero):**
```
pixel art sprite sheet, top-down 2D RPG hero, 4 directions idle and walk, 16x16 per frame, consistent lighting, game asset, no background, transparent, (masterpiece:1.1), best quality
```

**Character portrait:**
```
character portrait, fantasy knight, face only, neutral expression, painterly style, (masterpiece:1.2), best quality, 4k
```

### Flux Kontext Examples

**Recolor (armor):**
```
same character and pose, change armor color to dark blue with gold trim, keep face and weapon identical, consistent lighting
```

**New pose, same character:**
```
same fantasy knight character, walking pose to the right, same armor and art style, top-down game sprite, 16x16, transparent background
```

### Chatterbox TTS Examples

**Dialogue line:**
```
I've never seen anyone fight like that. [laugh] You might just survive the dungeon after all.
```

**Bark:**
```
Enemy spotted! Take positions!
```

**With emotion hint:**
```
<!-- emotion: 1.4 --> I'm sorry, hero. The king has fallen. We need you now more than ever.
```

---

## 2D Farming Game Assets

### OpenDUI Examples

**Pixel art sprite sheet (farmer):**
```
pixel art sprite sheet, top-down farmer character, 33 columns 4 rows, idle and walk and tool animations, 16x16 per cell, Stardew Valley style, (masterpiece:1.1), best quality, transparent
```

**Tileset:**
```
pixel art terrain tileset, grass and dirt transitions, 16x16 tiles, top-down 2D, game terrain, match corners and sides, (masterpiece:1.1)
```

### Flux Kontext Examples

**Hat variant:**
```
same farmer character and pose, add cowboy hat, keep body and animation frame identical, pixel art 16x16, Stardew style, transparent
```

**Plant growth stage:**
```
same tomato plant style, growth stage 2, middle height, green leaves, small green fruits, pixel art 16x16, game asset
```

### Chatterbox TTS Examples

**NPC dialogue:**
```
Welcome to the farm. [chuckle] Don't mind the blobs -- they're mostly harmless.
```

**Bark:**
```
Your crops are ready to harvest!
```

**With emotion hint:**
```
<!-- emotion: 1.2 --> The weather's going to turn. Better water the plants before the heat hits.
```

---

## 3D Voxel Open-World Assets

### Spritesheet Tiles -- Row 0

#### GRASS top (column 0, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Grass surface, bright green with small texture variation (lighter and darker green dots), no border, seamless, flat color with dithered detail. Transparent background. PNG.
```

#### DIRT (column 1, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Dirt/soil texture, medium brown (#8B5E3C) with darker brown speckles, slightly rough look, seamless tile, no border. Transparent background. PNG.
```

#### GRASS side (column 2, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, side view. Top half: bright green grass fringe (irregular edge), bottom half: brown dirt. Clean flat colors with dithered transition line. Seamless horizontal tile. Transparent background. PNG.
```

#### STONE (column 3, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Stone/rock texture, medium gray with darker gray cracks and subtle highlights. Seamless tile, no border. Transparent background. PNG.
```

#### WATER (column 4, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Water surface, semi-transparent blue (#3A7BCC at 70% opacity), small white highlight dots in one corner, flat and clean. PNG with alpha channel.
```

#### LOG top (column 5, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Tree log cross-section, concentric brown rings (light tan center, dark brown outer ring), clean dithered rings. Seamless tile. Transparent background. PNG.
```

#### LOG side / bark (column 6, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, side view. Tree bark texture, vertical stripes in medium brown with dark brown grooves, slightly rough, seamless horizontal tile. Transparent background. PNG.
```

#### LEAVES (column 7, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Leaf cluster, irregular dark green pattern with gaps (checkerboard-like alpha cutout holes), bright green highlights. PNG with transparent holes (alpha cutout). Not fully opaque.
```

#### SAND (column 8, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Sandy beach texture, light tan/beige (#E8D5A3) with subtle lighter and darker specks, seamless, flat look. Transparent background. PNG.
```

#### BUSH (column 9, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Small dense bush, rounded dark green cluster with a few bright green highlights, black outline. Transparent background (PNG with alpha). Size: 16x16px.
```

#### POPPY (column 10, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Poppy flower: thin green stem, two small red petals at top, small yellow center dot. Black outline, transparent background. PNG.
```

#### DANDELION (column 11, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Dandelion: thin green stem, fluffy white round head with small radiating dots. Black outline, transparent background. PNG.
```

#### DAISY (column 12, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Daisy flower: green stem, white petals radiating from yellow center. Black outline, transparent background. PNG.
```

#### CORNFLOWER (column 13, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Cornflower: thin green stem, blue-violet petals around small dark center. Black outline, transparent background. PNG.
```

#### MARIGOLD (column 14, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Marigold flower: thick green stem, dense orange petals in layered circular pattern. Black outline, transparent background. PNG.
```

#### LAVENDER (column 15, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Lavender sprig: thin green stem, cluster of small purple dots at top forming a spike shape. Black outline, transparent background. PNG.
```

### Spritesheet Tiles -- Row 1

#### YELLOW_TORCH (column 0, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Wooden torch with bright yellow flame at top. Brown stick bottom half, orange/yellow glow flame top half, small white highlight on flame. Black outline, transparent background. PNG.
```

#### RED_TORCH (column 1, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright red (#FF2200). Keep the brown wooden handle unchanged. Keep all outlines black. Preserve pixel art style exactly.
```
*(Reference: YELLOW_TORCH tile from above)*

#### BLUE_TORCH (column 2, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright blue (#2244FF). Keep the brown wooden handle unchanged. Keep all outlines black. Preserve pixel art style exactly.
```

#### GREEN_TORCH (column 3, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright green (#00CC44). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

#### CYAN_TORCH (column 4, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to cyan (#00FFEE). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

#### MAGENTA_TORCH (column 5, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to magenta/pink (#FF00CC). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

#### WHITE_TORCH (column 6, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to white (#FFFFFF) with a very light gray glow. Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

#### PLANKS (column 7, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Wooden planks texture, light tan wood (#C8A46A) with horizontal grain lines in darker brown, seamless tile. No border, transparent background. PNG.
```

#### GLASS (column 8, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Glass block, mostly transparent (40% opacity light blue #AACCFF), thin white/light frame on edges to show the block shape. PNG with alpha channel.
```

### Full Spritesheet Assembly

**OpenDUI prompt (generate all at once as a sheet):**
```
Pixel art spritesheet, 256x32 pixels (16 columns, 2 rows, each tile 16x16px). Minecraft-like voxel game block textures. Row 0 left to right: grass top (green), dirt (brown), grass side (green+brown), stone (gray), water (blue semi-transparent), log top (concentric rings), log bark (vertical stripes), leaves (green holes), sand (tan), bush (green blob), poppy (red), dandelion (white), daisy (white+yellow), cornflower (blue), marigold (orange), lavender (purple). Row 1 left to right: yellow torch, red torch, blue torch, green torch, cyan torch, magenta torch, white torch, wood planks, glass. Pixel art style, crisp colors, no anti-aliasing, transparent PNG.
```

### UI Assets

#### Crosshair

**OpenDUI prompt:**
```
Pixel art crosshair/reticle, 16x16 pixels. Simple plus (+) shape, 1-pixel-wide lines, white (#FFFFFF) with 1px black border. Centered. Transparent background. PNG.
```

#### Block selector highlight

**OpenDUI prompt:**
```
Pixel art 64x64 image. Square frame/border, 4px thick, white with subtle yellow glow, rounded inner corner hint. Transparent interior. Used to highlight selected block in inventory. PNG with alpha.
```

### Chatterbox TTS Examples

**Ambient world narration:**
```
Voice: calm, slightly mysterious male narrator.
Text: "The world stretches endlessly in every direction. Mountains rise from the noise of the land, and rivers of stone carve through the valleys. Whatever you build here, will last."
Speed: slow and measured. No music.
```

**Block break sound cue script:**
```
Voice: short, punchy, robotic.
Text: "Block removed."
Very short, under 0.5 seconds. No reverb.
```

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

**Per-asset file:** For each image asset, create a `.txt` or `.md` next to it or in a `prompts/` subfolder, e.g. `graphics/characters/main/prompt_main_basic.txt`.

**Example (pixel art sprite sheet, farming):**
```
pixel art sprite sheet, top-down farmer character, 33 columns 4 rows, idle and walk and tool animations, 16x16 per cell, Stardew Valley style, (masterpiece:1.1), best quality, transparent
```

**Example (tileset):**
```
pixel art terrain tileset, grass and dirt transitions, 16x16 tiles, top-down 2D, game terrain, match corners and sides, (masterpiece:1.1)
```

**OpenDiTConditioning (optional):** If the workflow supports it, you can add:
- **Primary prompt:** main description (as above)
- **Aesthetic score:** e.g. 7.5
- **Flow score:** e.g. 5.0

---

## 2. Flux Kontext (Image Edit / Style / Consistency)

**Use for:** Editing existing sprites, style transfer, character consistency across frames, targeted changes (e.g. recolor, add hat).

**Prompt rules:**
- **Detailed, specific** edit instructions. Vague prompts give poor results.
- Describe exactly what to change and what to preserve (e.g. "change hat to cowboy hat, keep body and pose unchanged").
- For character consistency: "same character, same style, [specific action or pose]".
- One prompt per edit operation; each prompt must fully define the edit.

**Per-asset or per-batch:** Use one prompt per generated/edited image. For a set of frames, either one PROMPTS.md listing each frame’s prompt or one prompt file per frame.

**Example (hat variant):**
```
same farmer character and pose, add cowboy hat, keep body and animation frame identical, pixel art 16x16, Stardew style, transparent
```

**Example (plant growth stage):**
```
same tomato plant style, growth stage 2, middle height, green leaves, small green fruits, pixel art 16x16, game asset
```

---

## 3. Chatterbox TTS (Text-to-Speech)

**Use for:** Dialogue lines, NPC barks, menu narration, voice-over.

**Prompt rules:**
- **Input = script text** to be spoken. One script per line or per file; each file is one TTS input.
- Use **paralinguistic tags** for reactions: `[laugh]`, `[chuckle]`, `[sigh]`, `[gasp]`, `[cough]`.
- Control **emotion** via API/slider if available: 0.1–0.3 monotone, 1.0 neutral, 1.7–2.0 very expressive.
- **Zero-shot voice:** Reference audio (5–20 s) can define voice; prompt text stays independent and complete for the line itself.

**Per-asset:** One script/prompt per audio file. Store in `audio/prompts/` or next to the target file, e.g. `audio/dialogue/cat_npc_line1.txt`.

**Example (NPC dialogue):**
```
Welcome to the farm. [chuckle] Don't mind the blobs — they're mostly harmless.
```

**Example (bark):**
```
Your crops are ready to harvest!
```

**Example (with emotion hint in comment for pipeline):**
```
<!-- emotion: 1.2 --> The weather's going to turn. Better water the plants before the heat hits.
```

Keep the **spoken text self-contained**; comments or metadata (emotion, voice ID) can live in the same file or a sidecar JSON.

---

## 4. Where to Put Prompts (Per-Asset vs Per-Folder)

| Approach | When to use | Format |
|----------|-------------|--------|
| **Per-asset** | One image/audio per file; prompts are long or very specific | `graphics/plants/prompt_tomato.txt` or `audio/prompts/axe_swing.txt` |
| **Per-folder PROMPTS.md** | Many related assets (e.g. all tiles, all plant stages) | Single `PROMPTS.md` in folder; each section = asset name + full prompt |

**Per-folder PROMPTS.md template:**
```markdown
# [Folder name] — ComfyUI prompts

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

For this project’s asset paths and naming, see [assets.md](assets.md).

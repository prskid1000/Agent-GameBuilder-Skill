# Asset Prompts for ComfyUI

Prompts for generating assets for the GDCraft voxel game using OpenDUI (text-to-image),
Flux Kontext (image edit / style transfer), and Chatterbox TTS (audio).

Each prompt is **standalone and complete** — no "same as above" or implicit context.
Use one prompt per asset or per group of tiles in the same spritesheet row.

---

## Rules

- **OpenDUI / OpenDiT:** text-to-image for new sprites and tile art.
- **Flux Kontext:** edit / repaint / restyle existing images (e.g. recolor a tile).
- **Chatterbox TTS:** text-to-speech for ambient narration or UI sounds.
- Every prompt must be self-contained: state style, size, color palette, subject, background, and format.
- For spritesheet tiles: specify pixel art style, 16×16px, transparent background (PNG), top-down or isometric if relevant.

---

## Spritesheet Tiles — Row 0

### GRASS top (column 0, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Grass surface, bright green with small texture variation (lighter and darker green dots), no border, seamless, flat color with dithered detail. Transparent background. PNG.
```

### DIRT (column 1, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Dirt/soil texture, medium brown (#8B5E3C) with darker brown speckles, slightly rough look, seamless tile, no border. Transparent background. PNG.
```

### GRASS side (column 2, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, side view. Top half: bright green grass fringe (irregular edge), bottom half: brown dirt. Clean flat colors with dithered transition line. Seamless horizontal tile. Transparent background. PNG.
```

### STONE (column 3, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Stone/rock texture, medium gray with darker gray cracks and subtle highlights. Seamless tile, no border. Transparent background. PNG.
```

### WATER (column 4, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Water surface, semi-transparent blue (#3A7BCC at 70% opacity), small white highlight dots in one corner, flat and clean. PNG with alpha channel.
```

### LOG top (column 5, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Tree log cross-section, concentric brown rings (light tan center, dark brown outer ring), clean dithered rings. Seamless tile. Transparent background. PNG.
```

### LOG side / bark (column 6, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, side view. Tree bark texture, vertical stripes in medium brown with dark brown grooves, slightly rough, seamless horizontal tile. Transparent background. PNG.
```

### LEAVES (column 7, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Leaf cluster, irregular dark green pattern with gaps (checkerboard-like alpha cutout holes), bright green highlights. PNG with transparent holes (alpha cutout). Not fully opaque.
```

### SAND (column 8, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Sandy beach texture, light tan/beige (#E8D5A3) with subtle lighter and darker specks, seamless, flat look. Transparent background. PNG.
```

### BUSH (column 9, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Small dense bush, rounded dark green cluster with a few bright green highlights, black outline. Transparent background (PNG with alpha). Size: 16x16px.
```

### POPPY (column 10, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Poppy flower: thin green stem, two small red petals at top, small yellow center dot. Black outline, transparent background. PNG.
```

### DANDELION (column 11, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Dandelion: thin green stem, fluffy white round head with small radiating dots. Black outline, transparent background. PNG.
```

### DAISY (column 12, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Daisy flower: green stem, white petals radiating from yellow center. Black outline, transparent background. PNG.
```

### CORNFLOWER (column 13, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Cornflower: thin green stem, blue-violet petals around small dark center. Black outline, transparent background. PNG.
```

### MARIGOLD (column 14, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Marigold flower: thick green stem, dense orange petals in layered circular pattern. Black outline, transparent background. PNG.
```

### LAVENDER (column 15, row 0)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Lavender sprig: thin green stem, cluster of small purple dots at top forming a spike shape. Black outline, transparent background. PNG.
```

---

## Spritesheet Tiles — Row 1

### YELLOW_TORCH (column 0, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 sprite, front view for cross-shaped 3D placement. Wooden torch with bright yellow flame at top. Brown stick bottom half, orange/yellow glow flame top half, small white highlight on flame. Black outline, transparent background. PNG.
```

### RED_TORCH (column 1, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright red (#FF2200). Keep the brown wooden handle unchanged. Keep all outlines black. Preserve pixel art style exactly.
```
*(Reference: YELLOW_TORCH tile from above)*

### BLUE_TORCH (column 2, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright blue (#2244FF). Keep the brown wooden handle unchanged. Keep all outlines black. Preserve pixel art style exactly.
```

### GREEN_TORCH (column 3, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to bright green (#00CC44). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

### CYAN_TORCH (column 4, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to cyan (#00FFEE). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

### MAGENTA_TORCH (column 5, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to magenta/pink (#FF00CC). Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

### WHITE_TORCH (column 6, row 1)

**Flux Kontext prompt:**
```
Take this pixel art torch sprite (16x16, transparent background). Recolor the flame from yellow/orange to white (#FFFFFF) with a very light gray glow. Keep the brown wooden handle unchanged. Preserve pixel art style exactly.
```

### PLANKS (column 7, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Wooden planks texture, light tan wood (#C8A46A) with horizontal grain lines in darker brown, seamless tile. No border, transparent background. PNG.
```

### GLASS (column 8, row 1)

**OpenDUI prompt:**
```
Pixel art 16x16 tile, top-down view. Glass block, mostly transparent (40% opacity light blue #AACCFF), thin white/light frame on edges to show the block shape. PNG with alpha channel.
```

---

## Full Spritesheet Assembly

**OpenDUI prompt (generate all at once as a sheet):**
```
Pixel art spritesheet, 256x32 pixels (16 columns, 2 rows, each tile 16x16px). Minecraft-like voxel game block textures. Row 0 left to right: grass top (green), dirt (brown), grass side (green+brown), stone (gray), water (blue semi-transparent), log top (concentric rings), log bark (vertical stripes), leaves (green holes), sand (tan), bush (green blob), poppy (red), dandelion (white), daisy (white+yellow), cornflower (blue), marigold (orange), lavender (purple). Row 1 left to right: yellow torch, red torch, blue torch, green torch, cyan torch, magenta torch, white torch, wood planks, glass. Pixel art style, crisp colors, no anti-aliasing, transparent PNG.
```

---

## UI Assets

### Crosshair

**OpenDUI prompt:**
```
Pixel art crosshair/reticle, 16x16 pixels. Simple plus (+) shape, 1-pixel-wide lines, white (#FFFFFF) with 1px black border. Centered. Transparent background. PNG.
```

### Block selector highlight

**OpenDUI prompt:**
```
Pixel art 64x64 image. Square frame/border, 4px thick, white with subtle yellow glow, rounded inner corner hint. Transparent interior. Used to highlight selected block in inventory. PNG with alpha.
```

---

## Chatterbox TTS

### Ambient world narration

```
Voice: calm, slightly mysterious male narrator.
Text: "The world stretches endlessly in every direction. Mountains rise from the noise of the land, and rivers of stone carve through the valleys. Whatever you build here, will last."
Speed: slow and measured. No music.
```

### Block break sound cue script

```
Voice: short, punchy, robotic.
Text: "Block removed."
Very short, under 0.5 seconds. No reverb.
```

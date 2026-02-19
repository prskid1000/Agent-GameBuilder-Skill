<span id="class_ResourceImporterDynamicFont"></span>

## ResourceImporterDynamicFont

**Inherits:** [ResourceImporter](class_resourceimporter.md#class_ResourceImporter) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Imports a TTF, TTC, OTF, OTC, WOFF or WOFF2 font file for font rendering that adapts to any size.

### Description

Unlike bitmap fonts, dynamic fonts can be resized to any size and still look crisp. Dynamic fonts also optionally support MSDF font rendering, which allows for run-time scale changes with no re-rasterization cost.

While WOFF and especially WOFF2 tend to result in smaller file sizes, there is no universally "better" font format. In most situations, it's recommended to use the font format that was shipped on the font developer's website.

See also [ResourceImporterBMFont](class_resourceimporterbmfont.md#class_ResourceImporterBMFont) and [ResourceImporterImageFont](class_resourceimporterimagefont.md#class_ResourceImporterImageFont).

### Tutorials

- `Dynamic fonts - Using fonts <../tutorials/ui/gui_using_fonts.html#dynamic-fonts>`__

### Properties


| [bool](class_bool.md#class_bool) | [allow_system_fallback](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_allow_system_fallback) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [antialiasing](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_antialiasing) | `1` |
| [bool](class_bool.md#class_bool) | [compress](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_compress) | `true` |
| [bool](class_bool.md#class_bool) | [disable_embedded_bitmaps](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_disable_embedded_bitmaps) | `true` |
| [Array](class_array.md#class_Array) | [fallbacks](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_fallbacks) | `[]` |
| [bool](class_bool.md#class_bool) | [force_autohinter](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_force_autohinter) | `false` |
| [bool](class_bool.md#class_bool) | [generate_mipmaps](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_generate_mipmaps) | `false` |
| [int](class_int.md#class_int) | [hinting](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_hinting) | `3` |
| [bool](class_bool.md#class_bool) | [keep_rounding_remainders](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_keep_rounding_remainders) | `true` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [language_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_language_support) | `{}` |
| [bool](class_bool.md#class_bool) | [modulate_color_glyphs](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_modulate_color_glyphs) | `false` |
| [int](class_int.md#class_int) | [msdf_pixel_range](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_pixel_range) | `8` |
| [int](class_int.md#class_int) | [msdf_size](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_size) | `48` |
| [bool](class_bool.md#class_bool) | [multichannel_signed_distance_field](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field) | `false` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [opentype_features](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_opentype_features) | `{}` |
| [float](class_float.md#class_float) | [oversampling](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_oversampling) | `0.0` |
| [Array](class_array.md#class_Array) | [preload](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_preload) | `[]` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [script_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_script_support) | `{}` |
| [int](class_int.md#class_int) | [subpixel_positioning](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_subpixel_positioning) | `4` |

---

### Property Descriptions

<span id="class_ResourceImporterDynamicFont_property_allow_system_fallback"></span>

[bool](class_bool.md#class_bool) **allow_system_fallback** = `true` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_allow_system_fallback)

If `true`, automatically use system fonts as a fallback if a glyph isn't found in this dynamic font. This makes supporting CJK characters or emoji more straightforward, as you don't need to include a CJK/emoji font in your project. See also [fallbacks](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_fallbacks).

 **Note:** The appearance of system fonts varies across platforms. Loading system fonts is only supported on Windows, macOS, Linux, Android and iOS.

---

<span id="class_ResourceImporterDynamicFont_property_antialiasing"></span>

[int](class_int.md#class_int) **antialiasing** = `1` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_antialiasing)

The font antialiasing method to use.

 **Disabled:** Most suited for pixel art fonts, although you do not *have* to change the antialiasing from the default **Grayscale** if the font file was well-created and the font is used at an integer multiple of its intended size. If pixel art fonts have a bad appearance at their intended size, try setting [subpixel_positioning](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_subpixel_positioning) to **Disabled** instead.

 **Grayscale:** Use grayscale antialiasing. This is the approach used by the operating system on macOS, Android and iOS.

 **LCD Subpixel:** Use antialiasing with subpixel patterns to make fonts sharper on LCD displays. This is the approach used by the operating system on Windows and most Linux distributions. The downside is that this can introduce "fringing" on edges, especially on display technologies that don't use standard RGB subpixels (such as OLED displays). The LCD subpixel layout is globally controlled by ProjectSettings.gui/theme/lcd_subpixel_layout, which also allows falling back to grayscale antialiasing.

---

<span id="class_ResourceImporterDynamicFont_property_compress"></span>

[bool](class_bool.md#class_bool) **compress** = `true` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_compress)

If `true`, uses lossless compression for the resulting font.

---

<span id="class_ResourceImporterDynamicFont_property_disable_embedded_bitmaps"></span>

[bool](class_bool.md#class_bool) **disable_embedded_bitmaps** = `true` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_disable_embedded_bitmaps)

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---

<span id="class_ResourceImporterDynamicFont_property_fallbacks"></span>

[Array](class_array.md#class_Array) **fallbacks** = `[]` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_fallbacks)

List of font fallbacks to use if a glyph isn't found in this dynamic font. Fonts at the beginning of the array are attempted first, but fallback fonts that don't support the glyph's language and script are attempted last (see [language_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_language_support) and [script_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_script_support)). See also [allow_system_fallback](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_allow_system_fallback).

---

<span id="class_ResourceImporterDynamicFont_property_force_autohinter"></span>

[bool](class_bool.md#class_bool) **force_autohinter** = `false` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_force_autohinter)

If `true`, forces generation of hinting data for the font using FreeType's autohinter. This will make [hinting](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_hinting) effective with fonts that don't include hinting data.

---

<span id="class_ResourceImporterDynamicFont_property_generate_mipmaps"></span>

[bool](class_bool.md#class_bool) **generate_mipmaps** = `false` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_generate_mipmaps)

If `true`, this font will have mipmaps generated. This prevents text from looking grainy when a [Control](class_control.md#class_Control) is scaled down, or when a [Label3D](class_label3d.md#class_Label3D) is viewed from a long distance (if [Label3D.texture_filter](class_label3d.md#class_Label3D_property_texture_filter) is set to a mode that displays mipmaps).

Enabling [generate_mipmaps](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_generate_mipmaps) increases font generation time and memory usage. Only enable this setting if you actually need it.

---

<span id="class_ResourceImporterDynamicFont_property_hinting"></span>

[int](class_int.md#class_int) **hinting** = `3` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_hinting)

The hinting mode to use. This controls how aggressively glyph edges should be snapped to pixels when rasterizing the font. Depending on personal preference, you may prefer using one hinting mode over the other. Hinting modes other than **None** are only effective if the font contains hinting data (see [force_autohinter](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_force_autohinter)).

 **None:** Smoothest appearance, which can make the font look blurry at small sizes.

 **Light:** Sharp result by snapping glyph edges to pixels on the Y axis only.

 **Normal:** Sharpest by snapping glyph edges to pixels on both X and Y axes.

 **Light (Except Pixel Fonts):** **Disabled** for pixel style fonts (each glyph's contours contain only straight horizontal and vertical lines), **Light** for other fonts.

 **Normal (Except Pixel Fonts):** **Disabled** for pixel style fonts (each glyph's contours contain only straight horizontal and vertical lines), **Normal** for other fonts.

---

<span id="class_ResourceImporterDynamicFont_property_keep_rounding_remainders"></span>

[bool](class_bool.md#class_bool) **keep_rounding_remainders** = `true` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_keep_rounding_remainders)

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

<span id="class_ResourceImporterDynamicFont_property_language_support"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **language_support** = `{}` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_language_support)

Override the list of languages supported by this font. If left empty, this is supplied by the font metadata. There is usually no need to change this. See also [script_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_script_support).

---

<span id="class_ResourceImporterDynamicFont_property_modulate_color_glyphs"></span>

[bool](class_bool.md#class_bool) **modulate_color_glyphs** = `false` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_modulate_color_glyphs)

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

<span id="class_ResourceImporterDynamicFont_property_msdf_pixel_range"></span>

[int](class_int.md#class_int) **msdf_pixel_range** = `8` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_pixel_range)

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, [msdf_pixel_range](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_pixel_range) must be set to at least *twice* the size of the largest font outline. The default [msdf_pixel_range](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_pixel_range) value of `8` allows outline sizes up to `4` to look correct.

---

<span id="class_ResourceImporterDynamicFont_property_msdf_size"></span>

[int](class_int.md#class_int) **msdf_size** = `48` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_msdf_size)

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering. Only effective if [multichannel_signed_distance_field](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field) is `true`.

---

<span id="class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field"></span>

[bool](class_bool.md#class_bool) **multichannel_signed_distance_field** = `false` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field)

If set to `true`, the font will use multichannel signed distance field (MSDF) for crisp rendering at any size. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy for [Control](class_control.md#class_Control) s that are scaled down (or for [Label3D](class_label3d.md#class_Label3D) s viewed from a long distance).

MSDF font rendering can be combined with [generate_mipmaps](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_generate_mipmaps) to further improve font rendering quality when scaled down.

---

<span id="class_ResourceImporterDynamicFont_property_opentype_features"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **opentype_features** = `{}` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_opentype_features)

The OpenType features to enable, disable or set a value for this font. This can be used to enable optional features provided by the font, such as ligatures or alternative glyphs. The list of supported OpenType features varies on a per-font basis.

---

<span id="class_ResourceImporterDynamicFont_property_oversampling"></span>

[float](class_float.md#class_float) **oversampling** = `0.0` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_oversampling)

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class_Viewport_property_oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods.

---

<span id="class_ResourceImporterDynamicFont_property_preload"></span>

[Array](class_array.md#class_Array) **preload** = `[]` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_preload)

The glyph ranges to prerender. This can avoid stuttering during gameplay when new characters need to be rendered, especially if [subpixel_positioning](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_subpixel_positioning) is enabled. The downside of using preloading is that initial project load times will increase, as well as memory usage.

---

<span id="class_ResourceImporterDynamicFont_property_script_support"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **script_support** = `{}` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_script_support)

Override the list of language scripts supported by this font. If left empty, this is supplied by the font metadata. There is usually no need to change this. See also [language_support](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_language_support).

---

<span id="class_ResourceImporterDynamicFont_property_subpixel_positioning"></span>

[int](class_int.md#class_int) **subpixel_positioning** = `4` [🔗](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_subpixel_positioning)

Subpixel positioning improves font rendering appearance, especially at smaller font sizes. The downside is that it takes more time to initially render the font, which can cause stuttering during gameplay, especially if used with large font sizes. This should be set to **Disabled** for fonts with a pixel art appearance.

 **Disabled:** No subpixel positioning. Lowest quality, fastest rendering.

 **Auto:** Use subpixel positioning at small font sizes (the chosen quality varies depending on font size). Large fonts will not use subpixel positioning. This is a good tradeoff between performance and quality.

 **One Half of a Pixel:** Always perform intermediate subpixel positioning regardless of font size. High quality, slow rendering.

 **One Quarter of a Pixel:** Always perform precise subpixel positioning regardless of font size. Highest quality, slowest rendering.

 **Auto (Except Pixel Fonts):** **Disabled** for pixel style fonts (each glyph's contours contain only straight horizontal and vertical lines), **Auto** for other fonts.

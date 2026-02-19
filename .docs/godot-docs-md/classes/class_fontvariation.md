<span id="class_FontVariation"></span>

## FontVariation

**Inherits:** [Font](class_font.md#class_Font) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A variation of a font with additional settings.

### Description

Provides OpenType variations, simulated bold / slant, and additional font settings like OpenType features and extra spacing.

To use simulated bold font variant:

.. tabs::

```
```

    var fv = FontVariation.new()
    fv.base_font = load("res://BarlowCondensed-Regular.ttf")
    fv.variation_embolden = 1.2
    $Label.add_theme_font_override("font", fv)
    $Label.add_theme_font_size_override("font_size", 64)

```
```

    var fv = new FontVariation();
    fv.SetBaseFont(ResourceLoader.Load<FontFile>("res://BarlowCondensed-Regular.ttf"));
    fv.SetVariationEmbolden(1.2);
    GetNode("Label").AddThemeFontOverride("font", fv);
    GetNode("Label").AddThemeFontSizeOverride("font_size", 64);

To set the coordinate of multiple variation axes:

::

    var fv = FontVariation.new();
    var ts = TextServerManager.get_primary_interface()
    fv.base_font = load("res://BarlowCondensed-Regular.ttf")
    fv.variation_opentype = { ts.name_to_tag("wght"): 900, ts.name_to_tag("custom_hght"): 900 }

### Properties


| [Font](class_font.md#class_Font) | [base_font](class_fontvariation.md#class_FontVariation_property_base_font) |
| --- | --- |
| [float](class_float.md#class_float) | [baseline_offset](class_fontvariation.md#class_FontVariation_property_baseline_offset) | `0.0` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [opentype_features](class_fontvariation.md#class_FontVariation_property_opentype_features) | `{}` |
| [int](class_int.md#class_int) | [spacing_bottom](class_fontvariation.md#class_FontVariation_property_spacing_bottom) | `0` |
| [int](class_int.md#class_int) | [spacing_glyph](class_fontvariation.md#class_FontVariation_property_spacing_glyph) | `0` |
| [int](class_int.md#class_int) | [spacing_space](class_fontvariation.md#class_FontVariation_property_spacing_space) | `0` |
| [int](class_int.md#class_int) | [spacing_top](class_fontvariation.md#class_FontVariation_property_spacing_top) | `0` |
| [float](class_float.md#class_float) | [variation_embolden](class_fontvariation.md#class_FontVariation_property_variation_embolden) | `0.0` |
| [int](class_int.md#class_int) | [variation_face_index](class_fontvariation.md#class_FontVariation_property_variation_face_index) | `0` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [variation_opentype](class_fontvariation.md#class_FontVariation_property_variation_opentype) | `{}` |
| [Transform2D](class_transform2d.md#class_Transform2D) | [variation_transform](class_fontvariation.md#class_FontVariation_property_variation_transform) | `Transform2D(1, 0, 0, 1, 0, 0)` |

### Methods


| void | [set_spacing](class_fontvariation.md#class_FontVariation_method_set_spacing) ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) |
| --- | --- |

---

### Property Descriptions

<span id="class_FontVariation_property_base_font"></span>

[Font](class_font.md#class_Font) **base_font** [🔗](class_fontvariation.md#class_FontVariation_property_base_font)

- void **set_base_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_base_font** ( )

Base font used to create a variation. If not set, default [Theme](class_theme.md#class_Theme) font is used.

---

<span id="class_FontVariation_property_baseline_offset"></span>

[float](class_float.md#class_float) **baseline_offset** = `0.0` [🔗](class_fontvariation.md#class_FontVariation_property_baseline_offset)

- void **set_baseline_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_baseline_offset** ( )

Extra baseline offset (as a fraction of font height).

---

<span id="class_FontVariation_property_opentype_features"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **opentype_features** = `{}` [🔗](class_fontvariation.md#class_FontVariation_property_opentype_features)

- void **set_opentype_features** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_opentype_features** ( )

A set of OpenType feature tags. More info: OpenType feature tags.

---

<span id="class_FontVariation_property_spacing_bottom"></span>

[int](class_int.md#class_int) **spacing_bottom** = `0` [🔗](class_fontvariation.md#class_FontVariation_property_spacing_bottom)

- void **set_spacing** ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_spacing** ( )

Extra spacing at the bottom of the line in pixels.

---

<span id="class_FontVariation_property_spacing_glyph"></span>

[int](class_int.md#class_int) **spacing_glyph** = `0` [🔗](class_fontvariation.md#class_FontVariation_property_spacing_glyph)

- void **set_spacing** ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_spacing** ( )

Extra spacing between graphical glyphs.

---

<span id="class_FontVariation_property_spacing_space"></span>

[int](class_int.md#class_int) **spacing_space** = `0` [🔗](class_fontvariation.md#class_FontVariation_property_spacing_space)

- void **set_spacing** ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_spacing** ( )

Extra width of the space glyphs.

---

<span id="class_FontVariation_property_spacing_top"></span>

[int](class_int.md#class_int) **spacing_top** = `0` [🔗](class_fontvariation.md#class_FontVariation_property_spacing_top)

- void **set_spacing** ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_spacing** ( )

Extra spacing at the top of the line in pixels.

---

<span id="class_FontVariation_property_variation_embolden"></span>

[float](class_float.md#class_float) **variation_embolden** = `0.0` [🔗](class_fontvariation.md#class_FontVariation_property_variation_embolden)

- void **set_variation_embolden** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_variation_embolden** ( )

If is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

 **Note:** Emboldened fonts might have self-intersecting outlines, which will prevent MSDF fonts and [TextMesh](class_textmesh.md#class_TextMesh) from working correctly.

---

<span id="class_FontVariation_property_variation_face_index"></span>

[int](class_int.md#class_int) **variation_face_index** = `0` [🔗](class_fontvariation.md#class_FontVariation_property_variation_face_index)

- void **set_variation_face_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_variation_face_index** ( )

Active face index in the TrueType / OpenType collection file.

---

<span id="class_FontVariation_property_variation_opentype"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **variation_opentype** = `{}` [🔗](class_fontvariation.md#class_FontVariation_property_variation_opentype)

- void **set_variation_opentype** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_variation_opentype** ( )

Font OpenType variation coordinates. More info: OpenType variation tags.

 **Note:** This [Dictionary](class_dictionary.md#class_Dictionary) uses OpenType tags as keys. Variation axes can be identified both by tags ([int](class_int.md#class_int), e.g. `0x77678674`) and names ([String](class_string.md#class_String), e.g. `wght`). Some axes might be accessible by multiple names. For example, `wght` refers to the same axis as `weight`. Tags on the other hand are unique. To convert between names and tags, use [TextServer.name_to_tag()](class_textserver.md#class_TextServer_method_name_to_tag) and [TextServer.tag_to_name()](class_textserver.md#class_TextServer_method_tag_to_name).

 **Note:** To get available variation axes of a font, use [Font.get_supported_variation_list()](class_font.md#class_Font_method_get_supported_variation_list).

---

<span id="class_FontVariation_property_variation_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **variation_transform** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗](class_fontvariation.md#class_FontVariation_property_variation_transform)

- void **set_variation_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_variation_transform** ( )

2D transform, applied to the font outlines, can be used for slanting, flipping and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

---

### Method Descriptions

<span id="class_FontVariation_method_set_spacing"></span>

void **set_spacing** ( spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) [🔗](class_fontvariation.md#class_FontVariation_method_set_spacing)

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

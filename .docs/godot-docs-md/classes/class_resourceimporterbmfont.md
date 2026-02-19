<span id="class_ResourceImporterBMFont"></span>

## ResourceImporterBMFont

**Inherits:** [ResourceImporter](class_resourceimporter.md#class_ResourceImporter) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Imports a bitmap font in the BMFont (`.fnt`) format.

### Description

The BMFont format is a format created by the BMFont program. Many BMFont-compatible programs also exist, like BMGlyph.

Compared to [ResourceImporterImageFont](class_resourceimporterimagefont.md#class_ResourceImporterImageFont), **ResourceImporterBMFont** supports bitmap fonts with varying glyph widths/heights.

See also [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont).

### Tutorials

- `Bitmap fonts - Using fonts <../tutorials/ui/gui_using_fonts.html#bitmap-fonts>`__

### Properties


| [bool](class_bool.md#class_bool) | [compress](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_compress) | `true` |
| --- | --- | --- |
| [Array](class_array.md#class_Array) | [fallbacks](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_fallbacks) | `[]` |
| [int](class_int.md#class_int) | [scaling_mode](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_scaling_mode) | `2` |

---

### Property Descriptions

<span id="class_ResourceImporterBMFont_property_compress"></span>

[bool](class_bool.md#class_bool) **compress** = `true` [🔗](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_compress)

If `true`, uses lossless compression for the resulting font.

---

<span id="class_ResourceImporterBMFont_property_fallbacks"></span>

[Array](class_array.md#class_Array) **fallbacks** = `[]` [🔗](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_fallbacks)

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

---

<span id="class_ResourceImporterBMFont_property_scaling_mode"></span>

[int](class_int.md#class_int) **scaling_mode** = `2` [🔗](class_resourceimporterbmfont.md#class_ResourceImporterBMFont_property_scaling_mode)

Font scaling mode.

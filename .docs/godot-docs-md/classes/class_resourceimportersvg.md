<span id="class_ResourceImporterSVG"></span>

## ResourceImporterSVG

**Inherits:** [ResourceImporter](class_resourceimporter.md#class_ResourceImporter) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.

### Description

This importer imports [DPITexture](class_dpitexture.md#class_DPITexture) resources. See also [ResourceImporterTexture](class_resourceimportertexture.md#class_ResourceImporterTexture) and [ResourceImporterImage](class_resourceimporterimage.md#class_ResourceImporterImage).

### Properties


| [float](class_float.md#class_float) | [base_scale](class_resourceimportersvg.md#class_ResourceImporterSVG_property_base_scale) | `1.0` |
| --- | --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [color_map](class_resourceimportersvg.md#class_ResourceImporterSVG_property_color_map) | `{}` |
| [bool](class_bool.md#class_bool) | [compress](class_resourceimportersvg.md#class_ResourceImporterSVG_property_compress) | `true` |
| [float](class_float.md#class_float) | [saturation](class_resourceimportersvg.md#class_ResourceImporterSVG_property_saturation) | `1.0` |

---

### Property Descriptions

<span id="class_ResourceImporterSVG_property_base_scale"></span>

[float](class_float.md#class_float) **base_scale** = `1.0` [🔗](class_resourceimportersvg.md#class_ResourceImporterSVG_property_base_scale)

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---

<span id="class_ResourceImporterSVG_property_color_map"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **color_map** = `{}` [🔗](class_resourceimportersvg.md#class_ResourceImporterSVG_property_color_map)

If set, remaps texture colors according to [Color](class_color.md#class_Color)-[Color](class_color.md#class_Color) map.

---

<span id="class_ResourceImporterSVG_property_compress"></span>

[bool](class_bool.md#class_bool) **compress** = `true` [🔗](class_resourceimportersvg.md#class_ResourceImporterSVG_property_compress)

If `true`, uses lossless compression for the SVG source.

---

<span id="class_ResourceImporterSVG_property_saturation"></span>

[float](class_float.md#class_float) **saturation** = `1.0` [🔗](class_resourceimportersvg.md#class_ResourceImporterSVG_property_saturation)

Overrides texture saturation.

<span id="class_ResourceImporterBitMap"></span>

## ResourceImporterBitMap

**Inherits:** [ResourceImporter](class_resourceimporter.md#class_ResourceImporter) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Imports a [BitMap](class_bitmap.md#class_BitMap) resource (2D array of boolean values).

### Description

[BitMap](class_bitmap.md#class_BitMap) resources are typically used as click masks in [TextureButton](class_texturebutton.md#class_TextureButton) and [TouchScreenButton](class_touchscreenbutton.md#class_TouchScreenButton).

### Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

### Properties


| [int](class_int.md#class_int) | [create_from](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_create_from) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [threshold](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_threshold) | `0.5` |

---

### Property Descriptions

<span id="class_ResourceImporterBitMap_property_create_from"></span>

[int](class_int.md#class_int) **create_from** = `0` [🔗](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_create_from)

The data source to use for generating the bitmap.

 **Black & White:** Pixels whose HSV value is greater than the [threshold](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_threshold) will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

 **Alpha:** Pixels whose alpha value is greater than the [threshold](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_threshold) will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

---

<span id="class_ResourceImporterBitMap_property_threshold"></span>

[float](class_float.md#class_float) **threshold** = `0.5` [🔗](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_threshold)

The threshold to use to determine which bits should be considered enabled or disabled. See also [create_from](class_resourceimporterbitmap.md#class_ResourceImporterBitMap_property_create_from).

<span id="class_BlitMaterial"></span>

## BlitMaterial

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A material that processes blit calls to a DrawableTexture.

### Description

A material resource that can be used by DrawableTextures when processing blit calls to draw.

### Properties


| [BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) | [blend_mode](class_blitmaterial.md#class_BlitMaterial_property_blend_mode) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_BlitMaterial_BlendMode"></span>

enum **BlendMode**: [🔗](class_blitmaterial.md#enum_BlitMaterial_BlendMode)

<span id="class_BlitMaterial_constant_BLEND_MODE_MIX"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

<span id="class_BlitMaterial_constant_BLEND_MODE_ADD"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **BLEND_MODE_ADD** = `1`

Additive blending mode.

<span id="class_BlitMaterial_constant_BLEND_MODE_SUB"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

<span id="class_BlitMaterial_constant_BLEND_MODE_MUL"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

<span id="class_BlitMaterial_constant_BLEND_MODE_DISABLED"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **BLEND_MODE_DISABLED** = `4`

No blending mode, direct color copy.

---

### Property Descriptions

<span id="class_BlitMaterial_property_blend_mode"></span>

[BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **blend_mode** = `0` [🔗](class_blitmaterial.md#class_BlitMaterial_property_blend_mode)

- void **set_blend_mode** ( value: [BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) )
- [BlendMode](class_blitmaterial.md#enum_BlitMaterial_BlendMode) **get_blend_mode** ( )

The manner in which the newly blitted texture is blended with the original DrawableTexture.

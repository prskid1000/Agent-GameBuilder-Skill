<span id="class_Compositor"></span>

## Compositor

**Experimental:** More customization of the rendering pipeline will be added in the future.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Stores attributes used to customize how a Viewport is rendered.

### Description

The compositor resource stores attributes used to customize how a [Viewport](class_viewport.md#class_Viewport) is rendered.

### Tutorials

- [The Compositor](../tutorials/rendering/compositor.md)

### Properties


| [Array](class_array.md#class_Array)\[[CompositorEffect](class_compositoreffect.md#class_CompositorEffect)\] | [compositor_effects](class_compositor.md#class_Compositor_property_compositor_effects) | `[]` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_Compositor_property_compositor_effects"></span>

[Array](class_array.md#class_Array)\[[CompositorEffect](class_compositoreffect.md#class_CompositorEffect)\] **compositor_effects** = `[]` [🔗](class_compositor.md#class_Compositor_property_compositor_effects)

- void **set_compositor_effects** ( value: [Array](class_array.md#class_Array)\[[CompositorEffect](class_compositoreffect.md#class_CompositorEffect)\] )
- [Array](class_array.md#class_Array)\[[CompositorEffect](class_compositoreffect.md#class_CompositorEffect)\] **get_compositor_effects** ( )

The custom [CompositorEffect](class_compositoreffect.md#class_CompositorEffect) s that are applied during rendering of viewports using this compositor.

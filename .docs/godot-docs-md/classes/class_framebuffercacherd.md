<span id="class_FramebufferCacheRD"></span>

## FramebufferCacheRD

**Inherits:** [Object](class_object.md#class_Object)

Framebuffer cache manager for Rendering Device based renderers.

### Description

Framebuffer cache manager for [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)-based renderers. Provides a way to create a framebuffer and reuse it in subsequent calls for as long as the used textures exists. Framebuffers will automatically be cleaned up when dependent objects are freed.

### Methods


| [RID](class_rid.md#class_RID) | [get_cache_multipass](class_framebuffercacherd.md#class_FramebufferCacheRD_method_get_cache_multipass) ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], views: [int](class_int.md#class_int) ) static |
| --- | --- |

---

### Method Descriptions

<span id="class_FramebufferCacheRD_method_get_cache_multipass"></span>

[RID](class_rid.md#class_RID) **get_cache_multipass** ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], views: [int](class_int.md#class_int) ) *static* [🔗](class_framebuffercacherd.md#class_FramebufferCacheRD_method_get_cache_multipass)

Creates, or obtains a cached, framebuffer. `textures` lists textures accessed. `passes` defines the subpasses and texture allocation, if left empty a single pass is created and textures are allocated depending on their usage flags. `views` defines the number of views used when rendering.

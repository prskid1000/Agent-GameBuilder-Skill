<span id="class_ImageTexture3D"></span>

## ImageTexture3D

**Inherits:** [Texture3D](class_texture3d.md#class_Texture3D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture with 3 dimensions.

### Description

**ImageTexture3D** is a 3-dimensional [ImageTexture](class_imagetexture.md#class_ImageTexture) that has a width, height, and depth. See also [ImageTextureLayered](class_imagetexturelayered.md#class_ImageTextureLayered).

3D textures are typically used to store density maps for [FogMaterial](class_fogmaterial.md#class_FogMaterial), color correction LUTs for [Environment](class_environment.md#class_Environment), vector fields for [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D) and collision maps for [GPUParticlesCollisionSDF3D](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D). 3D textures can also be used in custom shaders.

### Methods


| Error | [create](class_imagetexture3d.md#class_ImageTexture3D_method_create) ( format: [Format](class_image.md#enum_Image_Format), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) |
| --- | --- |
| void | [update](class_imagetexture3d.md#class_ImageTexture3D_method_update) ( data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) |

---

### Method Descriptions

<span id="class_ImageTexture3D_method_create"></span>

Error **create** ( format: [Format](class_image.md#enum_Image_Format), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) [🔗](class_imagetexture3d.md#class_ImageTexture3D_method_create)

Creates the **ImageTexture3D** with specified `format`, `width`, `height`, and `depth`. If `use_mipmaps` is `true`, generates mipmaps for the **ImageTexture3D**.

---

<span id="class_ImageTexture3D_method_update"></span>

void **update** ( data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) [🔗](class_imagetexture3d.md#class_ImageTexture3D_method_update)

Replaces the texture's existing data with the layers specified in `data`. The size of `data` must match the parameters that were used for [create()](class_imagetexture3d.md#class_ImageTexture3D_method_create). In other words, the texture cannot be resized or have its format changed by calling [update()](class_imagetexture3d.md#class_ImageTexture3D_method_update).

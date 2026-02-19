<span id="class_ImageTexture"></span>

## ImageTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Texture2D](class_texture2d.md#class_Texture2D) based on an [Image](class_image.md#class_Image).

### Description

A [Texture2D](class_texture2d.md#class_Texture2D) based on an [Image](class_image.md#class_Image). For an image to be displayed, an **ImageTexture** has to be created from it using the [create_from_image()](class_imagetexture.md#class_ImageTexture_method_create_from_image) method:

::

    var image = Image.load_from_file("res://icon.svg")
    var texture = ImageTexture.create_from_image(image)
    $Sprite2D.texture = texture

This way, textures can be created at run-time by loading images both from within the editor and externally.

 **Warning:** Prefer to load imported textures with @GDScript.load() over loading them from within the filesystem dynamically with [Image.load()](class_image.md#class_Image_method_load), as it may not work in exported projects:

::

    var texture = load("res://icon.svg")
    $Sprite2D.texture = texture

This is because images have to be imported as a [CompressedTexture2D](class_compressedtexture2d.md#class_CompressedTexture2D) first to be loaded with @GDScript.load(). If you'd still like to load an image file just like any other [Resource](class_resource.md#class_Resource), import it as an [Image](class_image.md#class_Image) resource instead, and then load it normally using the @GDScript.load() method.

 **Note:** The image can be retrieved from an imported texture using the [Texture2D.get_image()](class_texture2d.md#class_Texture2D_method_get_image) method, which returns a copy of the image:

::

    var texture = load("res://icon.svg")
    var image = texture.get_image()

An **ImageTexture** is not meant to be operated from within the editor interface directly, and is mostly useful for rendering images on screen dynamically via code. If you need to generate images procedurally from within the editor, consider saving and importing images as custom texture resources implementing a new [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin).

 **Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations.

### Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |

### Methods


| [ImageTexture](class_imagetexture.md#class_ImageTexture) | [create_from_image](class_imagetexture.md#class_ImageTexture_method_create_from_image) ( image: [Image](class_image.md#class_Image) ) static |
| --- | --- |
| [Format](class_image.md#enum_Image_Format) | [get_format](class_imagetexture.md#class_ImageTexture_method_get_format) ( ) const |
| void | [set_image](class_imagetexture.md#class_ImageTexture_method_set_image) ( image: [Image](class_image.md#class_Image) ) |
| void | [set_size_override](class_imagetexture.md#class_ImageTexture_method_set_size_override) ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [update](class_imagetexture.md#class_ImageTexture_method_update) ( image: [Image](class_image.md#class_Image) ) |

---

### Method Descriptions

<span id="class_ImageTexture_method_create_from_image"></span>

[ImageTexture](class_imagetexture.md#class_ImageTexture) **create_from_image** ( image: [Image](class_image.md#class_Image) ) *static* [🔗](class_imagetexture.md#class_ImageTexture_method_create_from_image)

Creates a new **ImageTexture** and initializes it by allocating and setting the data from an [Image](class_image.md#class_Image).

---

<span id="class_ImageTexture_method_get_format"></span>

[Format](class_image.md#enum_Image_Format) **get_format** ( ) *const* [🔗](class_imagetexture.md#class_ImageTexture_method_get_format)

Returns the format of the texture.

---

<span id="class_ImageTexture_method_set_image"></span>

void **set_image** ( image: [Image](class_image.md#class_Image) ) [🔗](class_imagetexture.md#class_ImageTexture_method_set_image)

Replaces the texture's data with a new [Image](class_image.md#class_Image). This will re-allocate new memory for the texture.

If you want to update the image, but don't need to change its parameters (format, size), use [update()](class_imagetexture.md#class_ImageTexture_method_update) instead for better performance.

---

<span id="class_ImageTexture_method_set_size_override"></span>

void **set_size_override** ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_imagetexture.md#class_ImageTexture_method_set_size_override)

Resizes the texture to the specified dimensions.

---

<span id="class_ImageTexture_method_update"></span>

void **update** ( image: [Image](class_image.md#class_Image) ) [🔗](class_imagetexture.md#class_ImageTexture_method_update)

Replaces the texture's data with a new [Image](class_image.md#class_Image).

 **Note:** The texture has to be created using [create_from_image()](class_imagetexture.md#class_ImageTexture_method_create_from_image) or initialized first with the [set_image()](class_imagetexture.md#class_ImageTexture_method_set_image) method before it can be updated. The new image dimensions, format, and mipmaps configuration should match the existing texture's image configuration.

Use this method over [set_image()](class_imagetexture.md#class_ImageTexture_method_set_image) if you need to update the texture frequently, which is faster than allocating additional memory for a new texture each time.

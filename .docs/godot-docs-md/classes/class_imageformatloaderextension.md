<span id="class_ImageFormatLoaderExtension"></span>

## ImageFormatLoaderExtension

**Inherits:** [ImageFormatLoader](class_imageformatloader.md#class_ImageFormatLoader) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for creating [ImageFormatLoader](class_imageformatloader.md#class_ImageFormatLoader) extensions (adding support for extra image formats).

### Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

Be sure to respect the documented return types and values. You should create an instance of it, and call [add_format_loader()](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_method_add_format_loader) to register that loader during the initialization phase.

### Methods


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_recognized_extensions](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_private_method__get_recognized_extensions) ( ) | virtual | const |
| --- | --- | --- | --- |
| Error | [_load_image](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_private_method__load_image) ( image: [Image](class_image.md#class_Image), fileaccess: [FileAccess](class_fileaccess.md#class_FileAccess), flags: | bitfield | \[[LoaderFlags](class_imageformatloader.md#enum_ImageFormatLoader_LoaderFlags)\], scale: [float](class_float.md#class_float) ) | virtual |
| void | [add_format_loader](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_method_add_format_loader) ( ) |
| void | [remove_format_loader](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_method_remove_format_loader) ( ) |

---

### Method Descriptions

<span id="class_ImageFormatLoaderExtension_private_method__get_recognized_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_recognized_extensions** ( ) *virtual* *const* [🔗](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_private_method__get_recognized_extensions)

Returns the list of file extensions for this image format. Files with the given extensions will be treated as image file and loaded using this class.

---

<span id="class_ImageFormatLoaderExtension_private_method__load_image"></span>

Error **_load_image** ( image: [Image](class_image.md#class_Image), fileaccess: [FileAccess](class_fileaccess.md#class_FileAccess), flags: *BitField*\[[LoaderFlags](class_imageformatloader.md#enum_ImageFormatLoader_LoaderFlags)\], scale: [float](class_float.md#class_float) ) *virtual* [🔗](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_private_method__load_image)

Loads the content of `fileaccess` into the provided `image`.

---

<span id="class_ImageFormatLoaderExtension_method_add_format_loader"></span>

void **add_format_loader** ( ) [🔗](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_method_add_format_loader)

Add this format loader to the engine, allowing it to recognize the file extensions returned by [_get_recognized_extensions()](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_private_method__get_recognized_extensions).

---

<span id="class_ImageFormatLoaderExtension_method_remove_format_loader"></span>

void **remove_format_loader** ( ) [🔗](class_imageformatloaderextension.md#class_ImageFormatLoaderExtension_method_remove_format_loader)

Remove this format loader from the engine.

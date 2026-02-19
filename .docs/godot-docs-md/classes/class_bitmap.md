<span id="class_BitMap"></span>

## BitMap

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Boolean matrix.

### Description

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

### Methods


| [Image](class_image.md#class_Image) | [convert_to_image](class_bitmap.md#class_BitMap_method_convert_to_image) ( ) const |
| --- | --- |
| void | [create](class_bitmap.md#class_BitMap_method_create) ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [create_from_image_alpha](class_bitmap.md#class_BitMap_method_create_from_image_alpha) ( image: [Image](class_image.md#class_Image), threshold: [float](class_float.md#class_float) = 0.1 ) |
| [bool](class_bool.md#class_bool) | [get_bit](class_bitmap.md#class_BitMap_method_get_bit) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_bitv](class_bitmap.md#class_BitMap_method_get_bitv) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_size](class_bitmap.md#class_BitMap_method_get_size) ( ) const |
| [int](class_int.md#class_int) | [get_true_bit_count](class_bitmap.md#class_BitMap_method_get_true_bit_count) ( ) const |
| void | [grow_mask](class_bitmap.md#class_BitMap_method_grow_mask) ( pixels: [int](class_int.md#class_int), rect: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] | [opaque_to_polygons](class_bitmap.md#class_BitMap_method_opaque_to_polygons) ( rect: [Rect2i](class_rect2i.md#class_Rect2i), epsilon: [float](class_float.md#class_float) = 2.0 ) const |
| void | [resize](class_bitmap.md#class_BitMap_method_resize) ( new_size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [set_bit](class_bitmap.md#class_BitMap_method_set_bit) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), bit: [bool](class_bool.md#class_bool) ) |
| void | [set_bit_rect](class_bitmap.md#class_BitMap_method_set_bit_rect) ( rect: [Rect2i](class_rect2i.md#class_Rect2i), bit: [bool](class_bool.md#class_bool) ) |
| void | [set_bitv](class_bitmap.md#class_BitMap_method_set_bitv) ( position: [Vector2i](class_vector2i.md#class_Vector2i), bit: [bool](class_bool.md#class_bool) ) |

---

### Method Descriptions

<span id="class_BitMap_method_convert_to_image"></span>

[Image](class_image.md#class_Image) **convert_to_image** ( ) *const* [🔗](class_bitmap.md#class_BitMap_method_convert_to_image)

Returns an image of the same size as the bitmap and with an [Format](class_image.md#enum_Image_Format) of type [Image.FORMAT_L8](class_image.md#class_Image_constant_FORMAT_L8). `true` bits of the bitmap are being converted into white pixels, and `false` bits into black.

---

<span id="class_BitMap_method_create"></span>

void **create** ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_bitmap.md#class_BitMap_method_create)

Creates a bitmap with the specified size, filled with `false`.

---

<span id="class_BitMap_method_create_from_image_alpha"></span>

void **create_from_image_alpha** ( image: [Image](class_image.md#class_Image), threshold: [float](class_float.md#class_float) = 0.1 ) [🔗](class_bitmap.md#class_BitMap_method_create_from_image_alpha)

Creates a bitmap that matches the given image dimensions, every element of the bitmap is set to `false` if the alpha value of the image at that position is equal to `threshold` or less, and `true` in other case.

---

<span id="class_BitMap_method_get_bit"></span>

[bool](class_bool.md#class_bool) **get_bit** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) *const* [🔗](class_bitmap.md#class_BitMap_method_get_bit)

Returns bitmap's value at the specified position.

---

<span id="class_BitMap_method_get_bitv"></span>

[bool](class_bool.md#class_bool) **get_bitv** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_bitmap.md#class_BitMap_method_get_bitv)

Returns bitmap's value at the specified position.

---

<span id="class_BitMap_method_get_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( ) *const* [🔗](class_bitmap.md#class_BitMap_method_get_size)

Returns bitmap's dimensions.

---

<span id="class_BitMap_method_get_true_bit_count"></span>

[int](class_int.md#class_int) **get_true_bit_count** ( ) *const* [🔗](class_bitmap.md#class_BitMap_method_get_true_bit_count)

Returns the number of bitmap elements that are set to `true`.

---

<span id="class_BitMap_method_grow_mask"></span>

void **grow_mask** ( pixels: [int](class_int.md#class_int), rect: [Rect2i](class_rect2i.md#class_Rect2i) ) [🔗](class_bitmap.md#class_BitMap_method_grow_mask)

Applies morphological dilation or erosion to the bitmap. If `pixels` is positive, dilation is applied to the bitmap. If `pixels` is negative, erosion is applied to the bitmap. `rect` defines the area where the morphological operation is applied. Pixels located outside the `rect` are unaffected by [grow_mask()](class_bitmap.md#class_BitMap_method_grow_mask).

---

<span id="class_BitMap_method_opaque_to_polygons"></span>

[Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] **opaque_to_polygons** ( rect: [Rect2i](class_rect2i.md#class_Rect2i), epsilon: [float](class_float.md#class_float) = 2.0 ) *const* [🔗](class_bitmap.md#class_BitMap_method_opaque_to_polygons)

Creates an [Array](class_array.md#class_Array) of polygons covering a rectangular portion of the bitmap. It uses a marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP) reduction of the number of vertices. Each polygon is described as a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) of its vertices.

To get polygons covering the whole bitmap, pass:

::

    Rect2(Vector2(), get_size())

 `epsilon` is passed to RDP to control how accurately the polygons cover the bitmap: a lower `epsilon` corresponds to more points in the polygons.

---

<span id="class_BitMap_method_resize"></span>

void **resize** ( new_size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_bitmap.md#class_BitMap_method_resize)

Resizes the image to `new_size`.

---

<span id="class_BitMap_method_set_bit"></span>

void **set_bit** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), bit: [bool](class_bool.md#class_bool) ) [🔗](class_bitmap.md#class_BitMap_method_set_bit)

Sets the bitmap's element at the specified position, to the specified value.

---

<span id="class_BitMap_method_set_bit_rect"></span>

void **set_bit_rect** ( rect: [Rect2i](class_rect2i.md#class_Rect2i), bit: [bool](class_bool.md#class_bool) ) [🔗](class_bitmap.md#class_BitMap_method_set_bit_rect)

Sets a rectangular portion of the bitmap to the specified value.

---

<span id="class_BitMap_method_set_bitv"></span>

void **set_bitv** ( position: [Vector2i](class_vector2i.md#class_Vector2i), bit: [bool](class_bool.md#class_bool) ) [🔗](class_bitmap.md#class_BitMap_method_set_bitv)

Sets the bitmap's element at the specified position, to the specified value.

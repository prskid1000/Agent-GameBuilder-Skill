.. _class_@GDScript:

## @GDScript

Built-in GDScript constants, functions, and annotations.

### Description

A list of utility functions and annotations accessible from any script written in GDScript.

For the list of global functions and constants that can be accessed in any scripting language, see @GlobalScope.

### Tutorials

- [GDScript exports](../tutorials/scripting/gdscript/gdscript_exports.md)

### Methods


| [Color](class_color.md#class_Color) | Color8 ( r8: [int](class_int.md#class_int), g8: [int](class_int.md#class_int), b8: [int](class_int.md#class_int), a8: [int](class_int.md#class_int) = 255 ) |
| --- | --- |
| void | assert ( condition: [bool](class_bool.md#class_bool), message: [String](class_string.md#class_String) = "" ) |
| [String](class_string.md#class_String) | char ( code: [int](class_int.md#class_int) ) |
| [Variant](class_variant.md#class_Variant) | convert ( what: [Variant](class_variant.md#class_Variant), type: Variant.Type ) |
| [Object](class_object.md#class_Object) | dict_to_inst ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| [Array](class_array.md#class_Array) | get_stack ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | inst_to_dict ( instance: [Object](class_object.md#class_Object) ) |
| [bool](class_bool.md#class_bool) | is_instance_of ( value: [Variant](class_variant.md#class_Variant), type: [Variant](class_variant.md#class_Variant) ) |
| [int](class_int.md#class_int) | len ( var: [Variant](class_variant.md#class_Variant) ) |
| [Resource](class_resource.md#class_Resource) | load ( path: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | ord ( char: [String](class_string.md#class_String) ) |
| [Resource](class_resource.md#class_Resource) | preload ( path: [String](class_string.md#class_String) ) |
| void | print_debug ( ... ) vararg |
| void | print_stack ( ) |
| [Array](class_array.md#class_Array) | range ( ... ) vararg |
| [bool](class_bool.md#class_bool) | type_exists ( type: [StringName](class_stringname.md#class_StringName) ) |

---

### Constants

.. _class_@GDScript_constant_PI:

**PI** = `3.14159265358979` 🔗

Constant that represents how many times the diameter of a circle fits around its perimeter. This is equivalent to `TAU / 2`, or 180 degrees in rotations.

.. _class_@GDScript_constant_TAU:

**TAU** = `6.28318530717959` 🔗

The circle constant, the circumference of the unit circle in radians. This is equivalent to `PI * 2`, or 360 degrees in rotations.

.. _class_@GDScript_constant_INF:

**INF** = `inf` 🔗

Positive floating-point infinity. This is the result of floating-point division when the divisor is `0.0`. For negative infinity, use `-INF`. Dividing by `-0.0` will result in negative infinity if the numerator is positive, so dividing by `0.0` is not the same as dividing by `-0.0` (despite `0.0 == -0.0` returning `true`).

 **Warning:** Numeric infinity is only a concept with floating-point numbers, and has no equivalent for integers. Dividing an integer number by `0` will not result in INF and will result in a run-time error instead.

.. _class_@GDScript_constant_NAN:

**NAN** = `nan` 🔗

"Not a Number", an invalid floating-point value. It is returned by some invalid operations, such as dividing floating-point `0.0` by `0.0`.

 NAN has special properties, including that `!=` always returns `true`, while other comparison operators always return `false`. This is true even when comparing with itself (`NAN == NAN` returns `false` and `NAN != NAN` returns `true`). Due to this, you must use @GlobalScope.is_nan() to check whether a number is equal to NAN.

 **Warning:** "Not a Number" is only a concept with floating-point numbers, and has no equivalent for integers. Dividing an integer `0` by `0` will not result in NAN and will result in a run-time error instead.

---

### Annotations

.. _class_@GDScript_annotation_@abstract:

**@abstract** ( ) 🔗

Marks a class or a method as abstract.

An abstract class is a class that cannot be instantiated directly. Instead, it is meant to be inherited by other classes. Attempting to instantiate an abstract class will result in an error.

An abstract method is a method that has no implementation. Therefore, a newline or a semicolon is expected after the function header. This defines a contract that inheriting classes must conform to, because the method signature must be compatible when overriding.

Inheriting classes must either provide implementations for all abstract methods, or the inheriting class must be marked as abstract. If a class has at least one abstract method (either its own or an unimplemented inherited one), then it must also be marked as abstract. However, the reverse is not true: an abstract class is allowed to have no abstract methods.

::

    @abstract class Shape:
        @abstract func draw()

    class Circle extends Shape:
        func draw():
            print("Drawing a circle.")

    class Square extends Shape:
        func draw():
            print("Drawing a square.")

---

.. _class_@GDScript_annotation_@export:

**@export** ( ) 🔗

Mark the following property as exported (editable in the Inspector dock and saved to disk). To control the type of the exported property, use the type hint notation.

::

    extends Node

    enum Direction {LEFT, RIGHT, UP, DOWN}

    # Built-in types.
    @export var string = ""
    @export var int_number = 5
    @export var float_number: float = 5

    # Enums.
    @export var type: Variant.Type
    @export var format: Image.Format
    @export var direction: Direction

    # Resources.
    @export var image: Image
    @export var custom_resource: CustomResource

    # Nodes.
    @export var node: Node
    @export var custom_node: CustomNode

    # Typed arrays.
    @export var int_array: Array[int]
    @export var direction_array: Array[Direction]
    @export var image_array: Array[Image]
    @export var node_array: Array[Node]

 **Note:** Custom resources and nodes should be registered as global classes using `class_name`, since the Inspector currently only supports global classes. Otherwise, a less specific type will be exported instead.

 **Note:** Node export is only supported in [Node](class_node.md#class_Node)-derived classes and has a number of other limitations.

---

.. _class_@GDScript_annotation_@export_category:

**@export_category** ( name: [String](class_string.md#class_String) ) 🔗

Define a new category for the following exported properties. This helps to organize properties in the Inspector dock.

See also @GlobalScope.PROPERTY_USAGE_CATEGORY.

::

    @export_category("Statistics")
    @export var hp = 30
    @export var speed = 1.25

 **Note:** Categories in the Inspector dock's list usually divide properties coming from different classes (Node, Node2D, Sprite, etc.). For better clarity, it's recommended to use @export_group and @export_subgroup, instead.

---

.. _class_@GDScript_annotation_@export_color_no_alpha:

**@export_color_no_alpha** ( ) 🔗

Export a [Color](class_color.md#class_Color), [Array](class_array.md#class_Array) \[[Color](class_color.md#class_Color) \], or [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) property without allowing its transparency ([Color.a](class_color.md#class_Color_property_a)) to be edited.

See also @GlobalScope.PROPERTY_HINT_COLOR_NO_ALPHA.

::

    @export_color_no_alpha var dye_color: Color
    @export_color_no_alpha var dye_colors: Array[Color]

---

.. _class_@GDScript_annotation_@export_custom:

**@export_custom** ( hint: PropertyHint, hint_string: [String](class_string.md#class_String), usage: *BitField*\[PropertyUsageFlags\] = 6 ) 🔗

Allows you to set a custom hint, hint string, and usage flags for the exported property. Note that there's no validation done in GDScript, it will just pass the parameters to the editor.

::

    @export_custom(PROPERTY_HINT_NONE, "suffix:m") var suffix: Vector3

 **Note:** Regardless of the `usage` value, the @GlobalScope.PROPERTY_USAGE_SCRIPT_VARIABLE flag is always added, as with any explicitly declared script variable.

---

.. _class_@GDScript_annotation_@export_dir:

**@export_dir** ( ) 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property as a path to a directory. The path will be limited to the project folder and its subfolders. See @export_global_dir to allow picking from the entire filesystem.

See also @GlobalScope.PROPERTY_HINT_DIR.

::

    @export_dir var sprite_folder_path: String
    @export_dir var sprite_folder_paths: Array[String]

---

.. _class_@GDScript_annotation_@export_enum:

**@export_enum** ( names: [String](class_string.md#class_String), ... ) *vararg* 🔗

Export an [int](class_int.md#class_int), [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[int](class_int.md#class_int) \], [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array), or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property as an enumerated list of options (or an array of options). If the property is an [int](class_int.md#class_int), then the index of the value is stored, in the same order the values are provided. You can add explicit values using a colon. If the property is a [String](class_string.md#class_String), then the value is stored.

See also @GlobalScope.PROPERTY_HINT_ENUM.

::

    @export_enum("Warrior", "Magician", "Thief") var character_class: int
    @export_enum("Slow:30", "Average:60", "Very Fast:200") var character_speed: int
    @export_enum("Rebecca", "Mary", "Leah") var character_name: String

    @export_enum("Sword", "Spear", "Mace") var character_items: Array[int]
    @export_enum("double_jump", "climb", "dash") var character_skills: Array[String]

If you want to set an initial value, you must specify it explicitly:

::

    @export_enum("Rebecca", "Mary", "Leah") var character_name: String = "Rebecca"

If you want to use named GDScript enums, then use @export instead:

::

    enum CharacterName {REBECCA, MARY, LEAH}
    @export var character_name: CharacterName

    enum CharacterItem {SWORD, SPEAR, MACE}
    @export var character_items: Array[CharacterItem]

---

.. _class_@GDScript_annotation_@export_exp_easing:

**@export_exp_easing** ( hints: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export a floating-point property with an easing editor widget. Additional hints can be provided to adjust the behavior of the widget. `"attenuation"` flips the curve, which makes it more intuitive for editing attenuation properties. `"positive_only"` limits values to only be greater than or equal to zero.

See also @GlobalScope.PROPERTY_HINT_EXP_EASING.

::

    @export_exp_easing var transition_speed
    @export_exp_easing("attenuation") var fading_attenuation
    @export_exp_easing("positive_only") var effect_power
    @export_exp_easing var speeds: Array[float]

---

.. _class_@GDScript_annotation_@export_file:

**@export_file** ( filter: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property as a path to a file. The path will be limited to the project folder and its subfolders. See @export_global_file to allow picking from the entire filesystem.

If `filter` is provided, only matching files will be available for picking.

See also @GlobalScope.PROPERTY_HINT_FILE.

::

    @export_file var sound_effect_path: String
    @export_file("*.txt") var notes_path: String
    @export_file var level_paths: Array[String]

 **Note:** The file will be stored and referenced as UID, if available. This ensures that the reference is valid even when the file is moved. You can use [ResourceUID](class_resourceuid.md#class_ResourceUID) methods to convert it to path.

---

.. _class_@GDScript_annotation_@export_file_path:

**@export_file_path** ( filter: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Same as @export_file, except the file will be stored as a raw path. This means that it may become invalid when the file is moved. If you are exporting a [Resource](class_resource.md#class_Resource) path, consider using @export_file instead.

---

.. _class_@GDScript_annotation_@export_flags:

**@export_flags** ( names: [String](class_string.md#class_String), ... ) *vararg* 🔗

Export an integer property as a bit flag field. This allows to store several "checked" or `true` values with one property, and comfortably select them from the Inspector dock.

See also @GlobalScope.PROPERTY_HINT_FLAGS.

::

    @export_flags("Fire", "Water", "Earth", "Wind") var spell_elements = 0

You can add explicit values using a colon:

::

    @export_flags("Self:4", "Allies:8", "Foes:16") var spell_targets = 0

You can also combine several flags:

::

    @export_flags("Self:4", "Allies:8", "Self and Allies:12", "Foes:16")
    var spell_targets = 0

 **Note:** A flag value must be at least `1` and at most `2 ** 32 - 1`.

 **Note:** Unlike @export_enum, the previous explicit value is not taken into account. In the following example, A is 16, B is 2, C is 4.

::

    @export_flags("A:16", "B", "C") var x

You can also use the annotation on [Array](class_array.md#class_Array) \[[int](class_int.md#class_int) \], [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), and [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array)

::

    @export_flags("Fire", "Water", "Earth", "Wind") var phase_elements: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_2d_navigation:

**@export_flags_2d_navigation** ( ) 🔗

Export an integer property as a bit flag field for 2D navigation layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/2d_navigation/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_2D_NAVIGATION.

::

    @export_flags_2d_navigation var navigation_layers: int
    @export_flags_2d_navigation var navigation_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_2d_physics:

**@export_flags_2d_physics** ( ) 🔗

Export an integer property as a bit flag field for 2D physics layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/2d_physics/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_2D_PHYSICS.

::

    @export_flags_2d_physics var physics_layers: int
    @export_flags_2d_physics var physics_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_2d_render:

**@export_flags_2d_render** ( ) 🔗

Export an integer property as a bit flag field for 2D render layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/2d_render/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_2D_RENDER.

::

    @export_flags_2d_render var render_layers: int
    @export_flags_2d_render var render_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_3d_navigation:

**@export_flags_3d_navigation** ( ) 🔗

Export an integer property as a bit flag field for 3D navigation layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/3d_navigation/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_3D_NAVIGATION.

::

    @export_flags_3d_navigation var navigation_layers: int
    @export_flags_3d_navigation var navigation_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_3d_physics:

**@export_flags_3d_physics** ( ) 🔗

Export an integer property as a bit flag field for 3D physics layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/3d_physics/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_3D_PHYSICS.

::

    @export_flags_3d_physics var physics_layers: int
    @export_flags_3d_physics var physics_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_3d_render:

**@export_flags_3d_render** ( ) 🔗

Export an integer property as a bit flag field for 3D render layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/3d_render/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_3D_RENDER.

::

    @export_flags_3d_render var render_layers: int
    @export_flags_3d_render var render_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_flags_avoidance:

**@export_flags_avoidance** ( ) 🔗

Export an integer property as a bit flag field for navigation avoidance layers. The widget in the Inspector dock will use the layer names defined in ProjectSettings.layer_names/avoidance/layer_1.

See also @GlobalScope.PROPERTY_HINT_LAYERS_AVOIDANCE.

::

    @export_flags_avoidance var avoidance_layers: int
    @export_flags_avoidance var avoidance_layers_array: Array[int]

---

.. _class_@GDScript_annotation_@export_global_dir:

**@export_global_dir** ( ) 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property as an absolute path to a directory. The path can be picked from the entire filesystem. See @export_dir to limit it to the project folder and its subfolders.

See also @GlobalScope.PROPERTY_HINT_GLOBAL_DIR.

::

    @export_global_dir var sprite_folder_path: String
    @export_global_dir var sprite_folder_paths: Array[String]

---

.. _class_@GDScript_annotation_@export_global_file:

**@export_global_file** ( filter: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property as an absolute path to a file. The path can be picked from the entire filesystem. See @export_file to limit it to the project folder and its subfolders.

If `filter` is provided, only matching files will be available for picking.

See also @GlobalScope.PROPERTY_HINT_GLOBAL_FILE.

::

    @export_global_file var sound_effect_path: String
    @export_global_file("*.txt") var notes_path: String
    @export_global_file var multiple_paths: Array[String]

---

.. _class_@GDScript_annotation_@export_group:

**@export_group** ( name: [String](class_string.md#class_String), prefix: [String](class_string.md#class_String) = "" ) 🔗

Define a new group for the following exported properties. This helps to organize properties in the Inspector dock. Groups can be added with an optional `prefix`, which would make group to only consider properties that have this prefix. The grouping will break on the first property that doesn't have a prefix. The prefix is also removed from the property's name in the Inspector dock.

If no `prefix` is provided, then every following property will be added to the group. The group ends when then next group or category is defined. You can also force end a group by using this annotation with empty strings for parameters, `@export_group("", "")`.

Groups cannot be nested, use @export_subgroup to add subgroups within groups.

See also @GlobalScope.PROPERTY_USAGE_GROUP.

::

    @export_group("Racer Properties")
    @export var nickname = "Nick"
    @export var age = 26

    @export_group("Car Properties", "car_")
    @export var car_label = "Speedy"
    @export var car_number = 3

    @export_group("", "")
    @export var ungrouped_number = 3

---

.. _class_@GDScript_annotation_@export_multiline:

**@export_multiline** ( hint: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), [Dictionary](class_dictionary.md#class_Dictionary) or [Array](class_array.md#class_Array) \[[Dictionary](class_dictionary.md#class_Dictionary) \] property with a large [TextEdit](class_textedit.md#class_TextEdit) widget instead of a [LineEdit](class_lineedit.md#class_LineEdit). This adds support for multiline content and makes it easier to edit large amount of text stored in the property.

See also @GlobalScope.PROPERTY_HINT_MULTILINE_TEXT.

::

    @export_multiline var character_biography
    @export_multiline var npc_dialogs: Array[String]
    @export_multiline("monospace", "no_wrap") var favorite_ascii_art: String

---

.. _class_@GDScript_annotation_@export_node_path:

**@export_node_path** ( type: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export a [NodePath](class_nodepath.md#class_NodePath) or [Array](class_array.md#class_Array) \[[NodePath](class_nodepath.md#class_NodePath) \] property with a filter for allowed node types.

See also @GlobalScope.PROPERTY_HINT_NODE_PATH_VALID_TYPES.

::

    @export_node_path("Button", "TouchScreenButton") var some_button
    @export_node_path("Button", "TouchScreenButton") var many_buttons: Array[NodePath]

 **Note:** The type must be a native class or a globally registered script (using the `class_name` keyword) that inherits [Node](class_node.md#class_Node).

---

.. _class_@GDScript_annotation_@export_placeholder:

**@export_placeholder** ( placeholder: [String](class_string.md#class_String) ) 🔗

Export a [String](class_string.md#class_String), [Array](class_array.md#class_Array) \[[String](class_string.md#class_String) \], or [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) property with a placeholder text displayed in the editor widget when no value is present.

See also @GlobalScope.PROPERTY_HINT_PLACEHOLDER_TEXT.

::

    @export_placeholder("Name in lowercase") var character_id: String
    @export_placeholder("Name in lowercase") var friend_ids: Array[String]

---

.. _class_@GDScript_annotation_@export_range:

**@export_range** ( min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), step: [float](class_float.md#class_float) = 1.0, extra_hints: [String](class_string.md#class_String) = "", ... ) *vararg* 🔗

Export an [int](class_int.md#class_int), [float](class_float.md#class_float), [Array](class_array.md#class_Array) \[[int](class_int.md#class_int) \], [Array](class_array.md#class_Array) \[[float](class_float.md#class_float) \], [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array), [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), or [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) property as a range value. The range must be defined by `min` and `max`, as well as an optional `step` and a variety of extra hints. The `step` defaults to `1` for integer properties. For floating-point numbers this value depends on your EditorSettings.interface/inspector/default_float_step setting.

If hints `"or_greater"` and `"or_less"` are provided, the editor widget will not cap the value at range boundaries. The `"exp"` hint will make the edited values on range to change exponentially. The `"prefer_slider"` hint will make integer values use the slider instead of arrows for editing, while `"hide_control"` will hide the element controlling the value of the editor widget.

Hints also allow to indicate the units for the edited value. Using `"radians_as_degrees"` you can specify that the actual value is in radians, but should be displayed in degrees in the Inspector dock (the range values are also in degrees). `"degrees"` allows to add a degree sign as a unit suffix (the value is unchanged). Finally, a custom suffix can be provided using `"suffix:unit"`, where "unit" can be any string.

See also @GlobalScope.PROPERTY_HINT_RANGE.

::

    @export_range(0, 20) var number
    @export_range(-10, 20) var number
    @export_range(-10, 20, 0.2) var number: float
    @export_range(0, 20) var numbers: Array[float]

    @export_range(0, 100, 1, "or_greater") var power_percent
    @export_range(0, 100, 1, "or_greater", "or_less") var health_delta

    @export_range(-180, 180, 0.001, "radians_as_degrees") var angle_radians
    @export_range(0, 360, 1, "degrees") var angle_degrees
    @export_range(-8, 8, 2, "suffix:px") var target_offset

---

.. _class_@GDScript_annotation_@export_storage:

**@export_storage** ( ) 🔗

Export a property with @GlobalScope.PROPERTY_USAGE_STORAGE flag. The property is not displayed in the editor, but it is serialized and stored in the scene or resource file. This can be useful for @tool scripts. Also the property value is copied when [Resource.duplicate()](class_resource.md#class_Resource_method_duplicate) or [Node.duplicate()](class_node.md#class_Node_method_duplicate) is called, unlike non-exported variables.

::

    var a # Not stored in the file, not displayed in the editor.
    @export_storage var b # Stored in the file, not displayed in the editor.
    @export var c: int # Stored in the file, displayed in the editor.

---

.. _class_@GDScript_annotation_@export_subgroup:

**@export_subgroup** ( name: [String](class_string.md#class_String), prefix: [String](class_string.md#class_String) = "" ) 🔗

Define a new subgroup for the following exported properties. This helps to organize properties in the Inspector dock. Subgroups work exactly like groups, except they need a parent group to exist. See @export_group.

See also @GlobalScope.PROPERTY_USAGE_SUBGROUP.

::

    @export_group("Racer Properties")
    @export var nickname = "Nick"
    @export var age = 26

    @export_subgroup("Car Properties", "car_")
    @export var car_label = "Speedy"
    @export var car_number = 3

 **Note:** Subgroups cannot be nested, but you can use the slash separator (`/`) to achieve the desired effect:

::

    @export_group("Car Properties")
    @export_subgroup("Wheels", "wheel_")
    @export_subgroup("Wheels/Front", "front_wheel_")
    @export var front_wheel_strength = 10
    @export var front_wheel_mobility = 5
    @export_subgroup("Wheels/Rear", "rear_wheel_")
    @export var rear_wheel_strength = 8
    @export var rear_wheel_mobility = 3
    @export_subgroup("Wheels", "wheel_")
    @export var wheel_material: PhysicsMaterial

---

.. _class_@GDScript_annotation_@export_tool_button:

**@export_tool_button** ( text: [String](class_string.md#class_String), icon: [String](class_string.md#class_String) = "" ) 🔗

Export a [Callable](class_callable.md#class_Callable) property as a clickable button with the label `text`. When the button is pressed, the callable is called.

If `icon` is specified, it is used to fetch an icon for the button via [Control.get_theme_icon()](class_control.md#class_Control_method_get_theme_icon), from the `"EditorIcons"` theme type. If `icon` is omitted, the default `"Callable"` icon is used instead.

Consider using the [EditorUndoRedoManager](class_editorundoredomanager.md#class_EditorUndoRedoManager) to allow the action to be reverted safely.

See also @GlobalScope.PROPERTY_HINT_TOOL_BUTTON.

::

    @tool
    extends Sprite2D

    @export_tool_button("Hello") var hello_action = hello
    @export_tool_button("Randomize the color!", "ColorRect")
    var randomize_color_action = randomize_color

    func hello():
        print("Hello world!")

    func randomize_color():
        var undo_redo = EditorInterface.get_editor_undo_redo()
        undo_redo.create_action("Randomized Sprite2D Color")
        undo_redo.add_do_property(self, &"self_modulate", Color(randf(), randf(), randf()))
        undo_redo.add_undo_property(self, &"self_modulate", self_modulate)
        undo_redo.commit_action()

 **Note:** The property is exported without the @GlobalScope.PROPERTY_USAGE_STORAGE flag because a [Callable](class_callable.md#class_Callable) cannot be properly serialized and stored in a file.

 **Note:** In an exported project neither [EditorInterface](class_editorinterface.md#class_EditorInterface) nor [EditorUndoRedoManager](class_editorundoredomanager.md#class_EditorUndoRedoManager) exist, which may cause some scripts to break. To prevent this, you can use [Engine.get_singleton()](class_engine.md#class_Engine_method_get_singleton) and omit the static type from the variable declaration:

::

    var undo_redo = Engine.get_singleton(&"EditorInterface").get_editor_undo_redo()

 **Note:** Avoid storing lambda callables in member variables of [RefCounted](class_refcounted.md#class_RefCounted)-based classes (e.g. resources), as this can lead to memory leaks. Use only method callables and optionally [Callable.bind()](class_callable.md#class_Callable_method_bind) or [Callable.unbind()](class_callable.md#class_Callable_method_unbind).

---

.. _class_@GDScript_annotation_@icon:

**@icon** ( icon_path: [String](class_string.md#class_String) ) 🔗

Add a custom icon to the current script. The icon specified at `icon_path` is displayed in the Scene dock for every node of that class, as well as in various editor dialogs.

::

    @icon("res://path/to/class/icon.svg")

 **Note:** Only the script can have a custom icon. Inner classes are not supported.

 **Note:** As annotations describe their subject, the @icon annotation must be placed before the class definition and inheritance.

 **Note:** Unlike most other annotations, the argument of the @icon annotation must be a string literal (constant expressions are not supported).

---

.. _class_@GDScript_annotation_@onready:

**@onready** ( ) 🔗

Mark the following property as assigned when the [Node](class_node.md#class_Node) is ready. Values for these properties are not assigned immediately when the node is initialized ([Object._init()](class_object.md#class_Object_private_method__init)), and instead are computed and stored right before [Node._ready()](class_node.md#class_Node_private_method__ready).

::

    @onready var character_name = $Label

---

.. _class_@GDScript_annotation_@rpc:

**@rpc** ( mode: [String](class_string.md#class_String) = "authority", sync: [String](class_string.md#class_String) = "call_remote", transfer_mode: [String](class_string.md#class_String) = "reliable", transfer_channel: [int](class_int.md#class_int) = 0 ) 🔗

Mark the following method for remote procedure calls. See [High-level multiplayer](../tutorials/networking/high_level_multiplayer.md).

If `mode` is set as `"any_peer"`, allows any peer to call this RPC function. Otherwise, only the authority peer is allowed to call it and `mode` should be kept as `"authority"`. When configuring functions as RPCs with [Node.rpc_config()](class_node.md#class_Node_method_rpc_config), each of these modes respectively corresponds to the [MultiplayerAPI.RPC_MODE_AUTHORITY](class_multiplayerapi.md#class_MultiplayerAPI_constant_RPC_MODE_AUTHORITY) and [MultiplayerAPI.RPC_MODE_ANY_PEER](class_multiplayerapi.md#class_MultiplayerAPI_constant_RPC_MODE_ANY_PEER) RPC modes. See [RPCMode](class_multiplayerapi.md#enum_MultiplayerAPI_RPCMode). If a peer that is not the authority tries to call a function that is only allowed for the authority, the function will not be executed. If the error can be detected locally (when the RPC configuration is consistent between the local and the remote peer), an error message will be displayed on the sender peer. Otherwise, the remote peer will detect the error and print an error there.

If `sync` is set as `"call_remote"`, the function will only be executed on the remote peer, but not locally. To run this function locally too, set `sync` to `"call_local"`. When configuring functions as RPCs with [Node.rpc_config()](class_node.md#class_Node_method_rpc_config), this is equivalent to setting `call_local` to `true`.

The `transfer_mode` accepted values are `"unreliable"`, `"unreliable_ordered"`, or `"reliable"`. It sets the transfer mode of the underlying [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer). See [MultiplayerPeer.transfer_mode](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_mode).

The `transfer_channel` defines the channel of the underlying [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer). See [MultiplayerPeer.transfer_channel](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_channel).

The order of `mode`, `sync` and `transfer_mode` does not matter, but values related to the same argument must not be used more than once. `transfer_channel` always has to be the 4th argument (you must specify 3 preceding arguments).

::

    @rpc
    func fn(): pass

    @rpc("any_peer", "unreliable_ordered")
    func fn_update_pos(): pass

    @rpc("authority", "call_remote", "reliable", 0) # Equivalent to @rpc
    func fn_default(): pass

 **Note:** Methods annotated with @rpc cannot receive objects which define required parameters in [Object._init()](class_object.md#class_Object_private_method__init). See [Object._init()](class_object.md#class_Object_private_method__init) for more details.

---

.. _class_@GDScript_annotation_@static_unload:

**@static_unload** ( ) 🔗

Make a script with static variables to not persist after all references are lost. If the script is loaded again the static variables will revert to their default values.

 **Note:** As annotations describe their subject, the @static_unload annotation must be placed before the class definition and inheritance.

 **Warning:** Currently, due to a bug, scripts are never freed, even if @static_unload annotation is used.

---

.. _class_@GDScript_annotation_@tool:

**@tool** ( ) 🔗

Mark the current script as a tool script, allowing it to be loaded and executed by the editor. See [Running code in the editor](../tutorials/plugins/running_code_in_the_editor.md).

::

    @tool
    extends Node

 **Note:** As annotations describe their subject, the @tool annotation must be placed before the class definition and inheritance.

---

.. _class_@GDScript_annotation_@warning_ignore:

**@warning_ignore** ( warning: [String](class_string.md#class_String), ... ) *vararg* 🔗

Mark the following statement to ignore the specified `warning`. See [GDScript warning system](../tutorials/scripting/gdscript/warning_system.md).

::

    func test():
        print("hello")
        return
        @warning_ignore("unreachable_code")
        print("unreachable")

See also @warning_ignore_start and @warning_ignore_restore.

---

.. _class_@GDScript_annotation_@warning_ignore_restore:

**@warning_ignore_restore** ( warning: [String](class_string.md#class_String), ... ) *vararg* 🔗

Stops ignoring the listed warning types after @warning_ignore_start. Ignoring the specified warning types will be reset to Project Settings. This annotation can be omitted to ignore the warning types until the end of the file.

 **Note:** Unlike most other annotations, arguments of the @warning_ignore_restore annotation must be string literals (constant expressions are not supported).

---

.. _class_@GDScript_annotation_@warning_ignore_start:

**@warning_ignore_start** ( warning: [String](class_string.md#class_String), ... ) *vararg* 🔗

Starts ignoring the listed warning types until the end of the file or the @warning_ignore_restore annotation with the given warning type.

::

    func test():
        var a = 1 # Warning (if enabled in the Project Settings).
        @warning_ignore_start("unused_variable")
        var b = 2 # No warning.
        var c = 3 # No warning.
        @warning_ignore_restore("unused_variable")
        var d = 4 # Warning (if enabled in the Project Settings).

 **Note:** To suppress a single warning, use @warning_ignore instead.

 **Note:** Unlike most other annotations, arguments of the @warning_ignore_start annotation must be string literals (constant expressions are not supported).

---

### Method Descriptions

.. _class_@GDScript_method_Color8:

[Color](class_color.md#class_Color) **Color8** ( r8: [int](class_int.md#class_int), g8: [int](class_int.md#class_int), b8: [int](class_int.md#class_int), a8: [int](class_int.md#class_int) = 255 ) 🔗

**Deprecated:** Use [Color.from_rgba8()](class_color.md#class_Color_method_from_rgba8) instead.

Returns a [Color](class_color.md#class_Color) constructed from red (`r8`), green (`g8`), blue (`b8`), and optionally alpha (`a8`) integer channels, each divided by `255.0` for their final value. Using Color8() instead of the standard [Color](class_color.md#class_Color) constructor is useful when you need to match exact color values in an [Image](class_image.md#class_Image).

::

    var red = Color8(255, 0, 0)             # Same as Color(1, 0, 0).
    var dark_blue = Color8(0, 0, 51)        # Same as Color(0, 0, 0.2).
    var my_color = Color8(306, 255, 0, 102) # Same as Color(1.2, 1, 0, 0.4).

 **Note:** Due to the lower precision of Color8() compared to the standard [Color](class_color.md#class_Color) constructor, a color created with Color8() will generally not be equal to the same color created with the standard [Color](class_color.md#class_Color) constructor. Use [Color.is_equal_approx()](class_color.md#class_Color_method_is_equal_approx) for comparisons to avoid issues with floating-point precision error.

---

.. _class_@GDScript_method_assert:

void **assert** ( condition: [bool](class_bool.md#class_bool), message: [String](class_string.md#class_String) = "" ) 🔗

Asserts that the `condition` is `true`. If the `condition` is `false`, an error is generated. When running from the editor, the running project will also be paused until you resume it. This can be used as a stronger form of @GlobalScope.push_error() for reporting errors to project developers or add-on users.

An optional `message` can be shown in addition to the generic "Assertion failed" message. You can use this to provide additional details about why the assertion failed.

 **Warning:** For performance reasons, the code inside assert() is only executed in debug builds or when running the project from the editor. Don't include code that has side effects in an assert() call. Otherwise, the project will behave differently when exported in release mode.

::

    # Imagine we always want speed to be between 0 and 20.
    var speed = -10
    assert(speed < 20) # True, the program will continue.
    assert(speed >= 0) # False, the program will stop.
    assert(speed >= 0 and speed < 20) # You can also combine the two conditional statements in one check.
    assert(speed < 20, "the speed limit is 20") # Show a message.

 **Note:** assert() is a keyword, not a function. So you cannot access it as a [Callable](class_callable.md#class_Callable) or use it inside expressions.

---

.. _class_@GDScript_method_char:

[String](class_string.md#class_String) **char** ( code: [int](class_int.md#class_int) ) 🔗

Returns a single character (as a [String](class_string.md#class_String) of length 1) of the given Unicode code point `code`.

::

    print(char(65))     # Prints "A"
    print(char(129302)) # Prints "🤖" (robot face emoji)

This is the inverse of ord(). See also [String.chr()](class_string.md#class_String_method_chr) and [String.unicode_at()](class_string.md#class_String_method_unicode_at).

---

.. _class_@GDScript_method_convert:

[Variant](class_variant.md#class_Variant) **convert** ( what: [Variant](class_variant.md#class_Variant), type: Variant.Type ) 🔗

**Deprecated:** Use @GlobalScope.type_convert() instead.

Converts `what` to `type` in the best way possible. The `type` uses the Variant.Type values.

::

    var a = [4, 2.5, 1.2]
    print(a is Array) # Prints true

    var b = convert(a, TYPE_PACKED_BYTE_ARRAY)
    print(b)          # Prints [4, 2, 1]
    print(b is Array) # Prints false

---

.. _class_@GDScript_method_dict_to_inst:

[Object](class_object.md#class_Object) **dict_to_inst** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) 🔗

**Deprecated:** Consider using [JSON.to_native()](class_json.md#class_JSON_method_to_native) or [Object.get_property_list()](class_object.md#class_Object_method_get_property_list) instead.

Converts a `dictionary` (created with inst_to_dict()) back to an Object instance. Can be useful for deserializing.

---

.. _class_@GDScript_method_get_stack:

[Array](class_array.md#class_Array) **get_stack** ( ) 🔗

Returns an array of dictionaries representing the current call stack.

::

    func _ready():
        foo()

    func foo():
        bar()

    func bar():
        print(get_stack())

Starting from `_ready()`, `bar()` would print:

.. code:: text

    [{function:bar, line:12, source:res://script.gd}, {function:foo, line:9, source:res://script.gd}, {function:_ready, line:6, source:res://script.gd}]

See also print_debug(), print_stack(), and [Engine.capture_script_backtraces()](class_engine.md#class_Engine_method_capture_script_backtraces).

 **Note:** By default, backtraces are only available in editor builds and debug builds. To enable them for release builds as well, you need to enable ProjectSettings.debug/settings/gdscript/always_track_call_stacks.

---

.. _class_@GDScript_method_inst_to_dict:

[Dictionary](class_dictionary.md#class_Dictionary) **inst_to_dict** ( instance: [Object](class_object.md#class_Object) ) 🔗

**Deprecated:** Consider using [JSON.from_native()](class_json.md#class_JSON_method_from_native) or [Object.get_property_list()](class_object.md#class_Object_method_get_property_list) instead.

Returns the passed `instance` converted to a [Dictionary](class_dictionary.md#class_Dictionary). Can be useful for serializing.

::

    var foo = "bar"
    func _ready():
        var d = inst_to_dict(self)
        print(d.keys())
        print(d.values())

Prints out:

.. code:: text

    [@subpath, @path, foo]
    [, res://test.gd, bar]

 **Note:** This function can only be used to serialize objects with an attached [GDScript](class_gdscript.md#class_GDScript) stored in a separate file. Objects without an attached script, with a script written in another language, or with a built-in script are not supported.

 **Note:** This function is not recursive, which means that nested objects will not be represented as dictionaries. Also, properties passed by reference ([Object](class_object.md#class_Object), [Dictionary](class_dictionary.md#class_Dictionary), [Array](class_array.md#class_Array), and packed arrays) are copied by reference, not duplicated.

---

.. _class_@GDScript_method_is_instance_of:

[bool](class_bool.md#class_bool) **is_instance_of** ( value: [Variant](class_variant.md#class_Variant), type: [Variant](class_variant.md#class_Variant) ) 🔗

Returns `true` if `value` is an instance of `type`. The `type` value must be one of the following:

- A constant from the Variant.Type enumeration, for example @GlobalScope.TYPE_INT.

- An [Object](class_object.md#class_Object)-derived class which exists in [ClassDB](class_classdb.md#class_ClassDB), for example [Node](class_node.md#class_Node).

- A [Script](class_script.md#class_Script) (you can use any class, including inner one).

Unlike the right operand of the `is` operator, `type` can be a non-constant value. The `is` operator supports more features (such as typed arrays). Use the operator instead of this method if you do not need to check the type dynamically.

 **Examples:**

::

    print(is_instance_of(a, TYPE_INT))
    print(is_instance_of(a, Node))
    print(is_instance_of(a, MyClass))
    print(is_instance_of(a, MyClass.InnerClass))

 **Note:** If `value` and/or `type` are freed objects (see @GlobalScope.is_instance_valid()), or `type` is not one of the above options, this method will raise a runtime error.

See also @GlobalScope.typeof(), type_exists(), [Array.is_same_typed()](class_array.md#class_Array_method_is_same_typed) (and other [Array](class_array.md#class_Array) methods).

---

.. _class_@GDScript_method_len:

[int](class_int.md#class_int) **len** ( var: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the length of the given Variant `var`. The length can be the character count of a [String](class_string.md#class_String) or [StringName](class_stringname.md#class_StringName), the element count of any array type, or the size of a [Dictionary](class_dictionary.md#class_Dictionary). For every other Variant type, a run-time error is generated and execution is stopped.

::

    var a = [1, 2, 3, 4]
    len(a) # Returns 4

    var b = "Hello!"
    len(b) # Returns 6

---

.. _class_@GDScript_method_load:

[Resource](class_resource.md#class_Resource) **load** ( path: [String](class_string.md#class_String) ) 🔗

Returns a [Resource](class_resource.md#class_Resource) from the filesystem located at the absolute `path`. Unless it's already referenced elsewhere (such as in another script or in the scene), the resource is loaded from disk on function call, which might cause a slight delay, especially when loading large scenes. To avoid unnecessary delays when loading something multiple times, either store the resource in a variable or use preload(). This method is equivalent of using [ResourceLoader.load()](class_resourceloader.md#class_ResourceLoader_method_load) with [ResourceLoader.CACHE_MODE_REUSE](class_resourceloader.md#class_ResourceLoader_constant_CACHE_MODE_REUSE).

 **Note:** Resource paths can be obtained by right-clicking on a resource in the FileSystem dock and choosing "Copy Path", or by dragging the file from the FileSystem dock into the current script.

::

    # Load a scene called "main" located in the root of the project directory and cache it in a variable.
    var main = load("res://main.tscn") # main will contain a PackedScene resource.

 **Important:** Relative paths are *not* relative to the script calling this method, instead it is prefixed with `"res://"`. Loading from relative paths might not work as expected.

This function is a simplified version of [ResourceLoader.load()](class_resourceloader.md#class_ResourceLoader_method_load), which can be used for more advanced scenarios.

 **Note:** Files have to be imported into the engine first to load them using this function. If you want to load [Image](class_image.md#class_Image) s at run-time, you may use [Image.load()](class_image.md#class_Image_method_load). If you want to import audio files, you can use the snippet described in [AudioStreamMP3.data](class_audiostreammp3.md#class_AudioStreamMP3_property_data).

 **Note:** If ProjectSettings.editor/export/convert_text_resources_to_binary is `true`, load() will not be able to read converted files in an exported project. If you rely on run-time loading of files present within the PCK, set ProjectSettings.editor/export/convert_text_resources_to_binary to `false`.

---

.. _class_@GDScript_method_ord:

[int](class_int.md#class_int) **ord** ( char: [String](class_string.md#class_String) ) 🔗

Returns an integer representing the Unicode code point of the given character `char`, which should be a string of length 1.

::

    print(ord("A")) # Prints 65
    print(ord("🤖")) # Prints 129302

This is the inverse of char(). See also [String.chr()](class_string.md#class_String_method_chr) and [String.unicode_at()](class_string.md#class_String_method_unicode_at).

---

.. _class_@GDScript_method_preload:

[Resource](class_resource.md#class_Resource) **preload** ( path: [String](class_string.md#class_String) ) 🔗

Returns a [Resource](class_resource.md#class_Resource) from the filesystem located at `path`. During run-time, the resource is loaded when the script is being parsed. This function effectively acts as a reference to that resource. Note that this function requires `path` to be a constant [String](class_string.md#class_String). If you want to load a resource from a dynamic/variable path, use load().

 **Note:** Resource paths can be obtained by right-clicking on a resource in the Assets Panel and choosing "Copy Path", or by dragging the file from the FileSystem dock into the current script.

::

    # Create instance of a scene.
    var diamond = preload("res://diamond.tscn").instantiate()

 **Note:** preload() is a keyword, not a function. So you cannot access it as a [Callable](class_callable.md#class_Callable).

---

.. _class_@GDScript_method_print_debug:

void **print_debug** ( ... ) *vararg* 🔗

Like @GlobalScope.print(), but includes the current stack frame when running with the debugger turned on.

The output in the console may look like the following:

.. code:: text

    Test print
    At: res://test.gd:15:_process()

See also print_stack(), get_stack(), and [Engine.capture_script_backtraces()](class_engine.md#class_Engine_method_capture_script_backtraces).

 **Note:** By default, backtraces are only available in editor builds and debug builds. To enable them for release builds as well, you need to enable ProjectSettings.debug/settings/gdscript/always_track_call_stacks.

---

.. _class_@GDScript_method_print_stack:

void **print_stack** ( ) 🔗

Prints a stack trace at the current code location.

The output in the console may look like the following:

.. code:: text

    Frame 0 - res://test.gd:16 in function '_process'

See also print_debug(), get_stack(), and [Engine.capture_script_backtraces()](class_engine.md#class_Engine_method_capture_script_backtraces).

 **Note:** By default, backtraces are only available in editor builds and debug builds. To enable them for release builds as well, you need to enable ProjectSettings.debug/settings/gdscript/always_track_call_stacks.

---

.. _class_@GDScript_method_range:

[Array](class_array.md#class_Array) **range** ( ... ) *vararg* 🔗

Returns an array with the given range. range() can be called in three ways:

 `range(n: int)`: Starts from 0, increases by steps of 1, and stops *before* `n`. The argument `n` is **exclusive**.

 `range(b: int, n: int)`: Starts from `b`, increases by steps of 1, and stops *before* `n`. The arguments `b` and `n` are **inclusive** and **exclusive**, respectively.

 `range(b: int, n: int, s: int)`: Starts from `b`, increases/decreases by steps of `s`, and stops *before* `n`. The arguments `b` and `n` are **inclusive** and **exclusive**, respectively. The argument `s` **can** be negative, but not `0`. If `s` is `0`, an error message is printed.

 range() converts all arguments to [int](class_int.md#class_int) before processing.

 **Note:** Returns an empty array if no value meets the value constraint (e.g. `range(2, 5, -1)` or `range(5, 5, 1)`).

 **Examples:**

::

    print(range(4))        # Prints [0, 1, 2, 3]
    print(range(2, 5))     # Prints [2, 3, 4]
    print(range(0, 6, 2))  # Prints [0, 2, 4]
    print(range(4, 1, -1)) # Prints [4, 3, 2]

To iterate over an [Array](class_array.md#class_Array) backwards, use:

::

    var array = [3, 6, 9]
    for i in range(array.size() - 1, -1, -1):
        print(array[i])

Output:

.. code:: text

    9
    6
    3

To iterate over [float](class_float.md#class_float), convert them in the loop.

::

    for i in range (3, 0, -1):
        print(i / 10.0)

Output:

.. code:: text

    0.3
    0.2
    0.1

---

.. _class_@GDScript_method_type_exists:

[bool](class_bool.md#class_bool) **type_exists** ( type: [StringName](class_stringname.md#class_StringName) ) 🔗

Returns `true` if the given [Object](class_object.md#class_Object)-derived class exists in [ClassDB](class_classdb.md#class_ClassDB). Note that [Variant](class_variant.md#class_Variant) data types are not registered in [ClassDB](class_classdb.md#class_ClassDB).

::

    type_exists("Sprite2D") # Returns true
    type_exists("NonExistentClass") # Returns false

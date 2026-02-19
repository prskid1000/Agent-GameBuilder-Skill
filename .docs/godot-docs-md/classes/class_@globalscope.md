.. _class_@GlobalScope:

## @GlobalScope

Global scope constants and functions.

### Description

A list of global scope enumerated constants and built-in functions. This is all that resides in the globals, constants regarding error codes, keycodes, property hints, etc.

Singletons are also documented here, since they can be accessed from anywhere.

For the entries that can only be accessed from scripts written in GDScript, see @GDScript.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Random number generation](../tutorials/math/random_number_generation.md)

### Properties


| [AudioServer](class_audioserver.md#class_AudioServer) | AudioServer |
| --- | --- |
| [CameraServer](class_cameraserver.md#class_CameraServer) | CameraServer |
| [ClassDB](class_classdb.md#class_ClassDB) | ClassDB |
| [DisplayServer](class_displayserver.md#class_DisplayServer) | DisplayServer |
| [EditorInterface](class_editorinterface.md#class_EditorInterface) | EditorInterface |
| [Engine](class_engine.md#class_Engine) | Engine |
| [EngineDebugger](class_enginedebugger.md#class_EngineDebugger) | EngineDebugger |
| [GDExtensionManager](class_gdextensionmanager.md#class_GDExtensionManager) | GDExtensionManager |
| [Geometry2D](class_geometry2d.md#class_Geometry2D) | Geometry2D |
| [Geometry3D](class_geometry3d.md#class_Geometry3D) | Geometry3D |
| [IP](class_ip.md#class_IP) | IP |
| [Input](class_input.md#class_Input) | Input |
| [InputMap](class_inputmap.md#class_InputMap) | InputMap |
| [JavaClassWrapper](class_javaclasswrapper.md#class_JavaClassWrapper) | JavaClassWrapper |
| [JavaScriptBridge](class_javascriptbridge.md#class_JavaScriptBridge) | JavaScriptBridge |
| [Marshalls](class_marshalls.md#class_Marshalls) | Marshalls |
| [NativeMenu](class_nativemenu.md#class_NativeMenu) | NativeMenu |
| [NavigationMeshGenerator](class_navigationmeshgenerator.md#class_NavigationMeshGenerator) | NavigationMeshGenerator |
| [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) | NavigationServer2D |
| [NavigationServer2DManager](class_navigationserver2dmanager.md#class_NavigationServer2DManager) | NavigationServer2DManager |
| [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D) | NavigationServer3D |
| [NavigationServer3DManager](class_navigationserver3dmanager.md#class_NavigationServer3DManager) | NavigationServer3DManager |
| [OS](class_os.md#class_OS) | OS |
| [Performance](class_performance.md#class_Performance) | Performance |
| [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) | PhysicsServer2D |
| [PhysicsServer2DManager](class_physicsserver2dmanager.md#class_PhysicsServer2DManager) | PhysicsServer2DManager |
| [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) | PhysicsServer3D |
| [PhysicsServer3DManager](class_physicsserver3dmanager.md#class_PhysicsServer3DManager) | PhysicsServer3DManager |
| [ProjectSettings](class_projectsettings.md#class_ProjectSettings) | ProjectSettings |
| [RenderingServer](class_renderingserver.md#class_RenderingServer) | RenderingServer |
| [ResourceLoader](class_resourceloader.md#class_ResourceLoader) | ResourceLoader |
| [ResourceSaver](class_resourcesaver.md#class_ResourceSaver) | ResourceSaver |
| [ResourceUID](class_resourceuid.md#class_ResourceUID) | ResourceUID |
| [TextServerManager](class_textservermanager.md#class_TextServerManager) | TextServerManager |
| [ThemeDB](class_themedb.md#class_ThemeDB) | ThemeDB |
| [Time](class_time.md#class_Time) | Time |
| [TranslationServer](class_translationserver.md#class_TranslationServer) | TranslationServer |
| [WorkerThreadPool](class_workerthreadpool.md#class_WorkerThreadPool) | WorkerThreadPool |
| [XRServer](class_xrserver.md#class_XRServer) | XRServer |

### Methods


| [Variant](class_variant.md#class_Variant) | abs ( x: [Variant](class_variant.md#class_Variant) ) |
| --- | --- |
| [float](class_float.md#class_float) | absf ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | absi ( x: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | acos ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | acosh ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | angle_difference ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | asin ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | asinh ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | atan ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | atan2 ( y: [float](class_float.md#class_float), x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | atanh ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | bezier_derivative ( start: [float](class_float.md#class_float), control_1: [float](class_float.md#class_float), control_2: [float](class_float.md#class_float), end: [float](class_float.md#class_float), t: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | bezier_interpolate ( start: [float](class_float.md#class_float), control_1: [float](class_float.md#class_float), control_2: [float](class_float.md#class_float), end: [float](class_float.md#class_float), t: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | bytes_to_var ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [Variant](class_variant.md#class_Variant) | bytes_to_var_with_objects ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [Variant](class_variant.md#class_Variant) | ceil ( x: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | ceilf ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | ceili ( x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | clamp ( value: [Variant](class_variant.md#class_Variant), min: [Variant](class_variant.md#class_Variant), max: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | clampf ( value: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | clampi ( value: [int](class_int.md#class_int), min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | cos ( angle_rad: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | cosh ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | cubic_interpolate ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | cubic_interpolate_angle ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | cubic_interpolate_angle_in_time ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float), to_t: [float](class_float.md#class_float), pre_t: [float](class_float.md#class_float), post_t: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | cubic_interpolate_in_time ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float), to_t: [float](class_float.md#class_float), pre_t: [float](class_float.md#class_float), post_t: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | db_to_linear ( db: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | deg_to_rad ( deg: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | ease ( x: [float](class_float.md#class_float), curve: [float](class_float.md#class_float) ) |
| [String](class_string.md#class_String) | error_string ( error: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | exp ( x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | floor ( x: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | floorf ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | floori ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | fmod ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | fposmod ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | hash ( variable: [Variant](class_variant.md#class_Variant) ) |
| [Object](class_object.md#class_Object) | instance_from_id ( instance_id: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | inverse_lerp ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | is_equal_approx ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | is_finite ( x: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | is_inf ( x: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | is_instance_id_valid ( id: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | is_instance_valid ( instance: [Variant](class_variant.md#class_Variant) ) |
| [bool](class_bool.md#class_bool) | is_nan ( x: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | is_same ( a: [Variant](class_variant.md#class_Variant), b: [Variant](class_variant.md#class_Variant) ) |
| [bool](class_bool.md#class_bool) | is_zero_approx ( x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | lerp ( from: [Variant](class_variant.md#class_Variant), to: [Variant](class_variant.md#class_Variant), weight: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | lerp_angle ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | lerpf ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | linear_to_db ( lin: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | log ( x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | max ( ... ) vararg |
| [float](class_float.md#class_float) | maxf ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | maxi ( a: [int](class_int.md#class_int), b: [int](class_int.md#class_int) ) |
| [Variant](class_variant.md#class_Variant) | min ( ... ) vararg |
| [float](class_float.md#class_float) | minf ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | mini ( a: [int](class_int.md#class_int), b: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | move_toward ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), delta: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | nearest_po2 ( value: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | pingpong ( value: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | posmod ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | pow ( base: [float](class_float.md#class_float), exp: [float](class_float.md#class_float) ) |
| void | print ( ... ) vararg |
| void | print_rich ( ... ) vararg |
| void | print_verbose ( ... ) vararg |
| void | printerr ( ... ) vararg |
| void | printraw ( ... ) vararg |
| void | prints ( ... ) vararg |
| void | printt ( ... ) vararg |
| void | push_error ( ... ) vararg |
| void | push_warning ( ... ) vararg |
| [float](class_float.md#class_float) | rad_to_deg ( rad: [float](class_float.md#class_float) ) |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | rand_from_seed ( seed: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | randf ( ) |
| [float](class_float.md#class_float) | randf_range ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | randfn ( mean: [float](class_float.md#class_float), deviation: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | randi ( ) |
| [int](class_int.md#class_int) | randi_range ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) |
| void | randomize ( ) |
| [float](class_float.md#class_float) | remap ( value: [float](class_float.md#class_float), istart: [float](class_float.md#class_float), istop: [float](class_float.md#class_float), ostart: [float](class_float.md#class_float), ostop: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | rid_allocate_id ( ) |
| [RID](class_rid.md#class_RID) | rid_from_int64 ( base: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | rotate_toward ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), delta: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | round ( x: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | roundf ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | roundi ( x: [float](class_float.md#class_float) ) |
| void | seed ( base: [int](class_int.md#class_int) ) |
| [Variant](class_variant.md#class_Variant) | sign ( x: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | signf ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | signi ( x: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | sin ( angle_rad: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | sinh ( x: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | smoothstep ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | snapped ( x: [Variant](class_variant.md#class_Variant), step: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | snappedf ( x: [float](class_float.md#class_float), step: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | snappedi ( x: [float](class_float.md#class_float), step: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | sqrt ( x: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | step_decimals ( x: [float](class_float.md#class_float) ) |
| [String](class_string.md#class_String) | str ( ... ) vararg |
| [Variant](class_variant.md#class_Variant) | str_to_var ( string: [String](class_string.md#class_String) ) |
| [float](class_float.md#class_float) | tan ( angle_rad: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | tanh ( x: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | type_convert ( variant: [Variant](class_variant.md#class_Variant), type: [int](class_int.md#class_int) ) |
| [String](class_string.md#class_String) | type_string ( type: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | typeof ( variable: [Variant](class_variant.md#class_Variant) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | var_to_bytes ( variable: [Variant](class_variant.md#class_Variant) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | var_to_bytes_with_objects ( variable: [Variant](class_variant.md#class_Variant) ) |
| [String](class_string.md#class_String) | var_to_str ( variable: [Variant](class_variant.md#class_Variant) ) |
| [Variant](class_variant.md#class_Variant) | weakref ( obj: [Variant](class_variant.md#class_Variant) ) |
| [Variant](class_variant.md#class_Variant) | wrap ( value: [Variant](class_variant.md#class_Variant), min: [Variant](class_variant.md#class_Variant), max: [Variant](class_variant.md#class_Variant) ) |
| [float](class_float.md#class_float) | wrapf ( value: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | wrapi ( value: [int](class_int.md#class_int), min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) |

---

### Enumerations

.. _enum_@GlobalScope_Side:

enum **Side**: 🔗

.. _class_@GlobalScope_constant_SIDE_LEFT:

Side **SIDE_LEFT** = `0`

Left side, usually used for [Control](class_control.md#class_Control) or [StyleBox](class_stylebox.md#class_StyleBox)-derived classes.

.. _class_@GlobalScope_constant_SIDE_TOP:

Side **SIDE_TOP** = `1`

Top side, usually used for [Control](class_control.md#class_Control) or [StyleBox](class_stylebox.md#class_StyleBox)-derived classes.

.. _class_@GlobalScope_constant_SIDE_RIGHT:

Side **SIDE_RIGHT** = `2`

Right side, usually used for [Control](class_control.md#class_Control) or [StyleBox](class_stylebox.md#class_StyleBox)-derived classes.

.. _class_@GlobalScope_constant_SIDE_BOTTOM:

Side **SIDE_BOTTOM** = `3`

Bottom side, usually used for [Control](class_control.md#class_Control) or [StyleBox](class_stylebox.md#class_StyleBox)-derived classes.

---

.. _enum_@GlobalScope_Corner:

enum **Corner**: 🔗

.. _class_@GlobalScope_constant_CORNER_TOP_LEFT:

Corner **CORNER_TOP_LEFT** = `0`

Top-left corner.

.. _class_@GlobalScope_constant_CORNER_TOP_RIGHT:

Corner **CORNER_TOP_RIGHT** = `1`

Top-right corner.

.. _class_@GlobalScope_constant_CORNER_BOTTOM_RIGHT:

Corner **CORNER_BOTTOM_RIGHT** = `2`

Bottom-right corner.

.. _class_@GlobalScope_constant_CORNER_BOTTOM_LEFT:

Corner **CORNER_BOTTOM_LEFT** = `3`

Bottom-left corner.

---

.. _enum_@GlobalScope_Orientation:

enum **Orientation**: 🔗

.. _class_@GlobalScope_constant_VERTICAL:

Orientation **VERTICAL** = `1`

General vertical alignment, usually used for [Separator](class_separator.md#class_Separator), [ScrollBar](class_scrollbar.md#class_ScrollBar), [Slider](class_slider.md#class_Slider), etc.

.. _class_@GlobalScope_constant_HORIZONTAL:

Orientation **HORIZONTAL** = `0`

General horizontal alignment, usually used for [Separator](class_separator.md#class_Separator), [ScrollBar](class_scrollbar.md#class_ScrollBar), [Slider](class_slider.md#class_Slider), etc.

---

.. _enum_@GlobalScope_ClockDirection:

enum **ClockDirection**: 🔗

.. _class_@GlobalScope_constant_CLOCKWISE:

ClockDirection **CLOCKWISE** = `0`

Clockwise rotation. Used by some methods (e.g. [Image.rotate_90()](class_image.md#class_Image_method_rotate_90)).

.. _class_@GlobalScope_constant_COUNTERCLOCKWISE:

ClockDirection **COUNTERCLOCKWISE** = `1`

Counter-clockwise rotation. Used by some methods (e.g. [Image.rotate_90()](class_image.md#class_Image_method_rotate_90)).

---

.. _enum_@GlobalScope_HorizontalAlignment:

enum **HorizontalAlignment**: 🔗

.. _class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_LEFT:

HorizontalAlignment **HORIZONTAL_ALIGNMENT_LEFT** = `0`

Horizontal left alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_CENTER:

HorizontalAlignment **HORIZONTAL_ALIGNMENT_CENTER** = `1`

Horizontal center alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_RIGHT:

HorizontalAlignment **HORIZONTAL_ALIGNMENT_RIGHT** = `2`

Horizontal right alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_FILL:

HorizontalAlignment **HORIZONTAL_ALIGNMENT_FILL** = `3`

Expand row to fit width, usually for text-derived classes.

---

.. _enum_@GlobalScope_VerticalAlignment:

enum **VerticalAlignment**: 🔗

.. _class_@GlobalScope_constant_VERTICAL_ALIGNMENT_TOP:

VerticalAlignment **VERTICAL_ALIGNMENT_TOP** = `0`

Vertical top alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_VERTICAL_ALIGNMENT_CENTER:

VerticalAlignment **VERTICAL_ALIGNMENT_CENTER** = `1`

Vertical center alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_VERTICAL_ALIGNMENT_BOTTOM:

VerticalAlignment **VERTICAL_ALIGNMENT_BOTTOM** = `2`

Vertical bottom alignment, usually for text-derived classes.

.. _class_@GlobalScope_constant_VERTICAL_ALIGNMENT_FILL:

VerticalAlignment **VERTICAL_ALIGNMENT_FILL** = `3`

Expand rows to fit height, usually for text-derived classes.

---

.. _enum_@GlobalScope_InlineAlignment:

enum **InlineAlignment**: 🔗

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TOP_TO:

InlineAlignment **INLINE_ALIGNMENT_TOP_TO** = `0`

Aligns the top of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_CENTER_TO:

InlineAlignment **INLINE_ALIGNMENT_CENTER_TO** = `1`

Aligns the center of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_BASELINE_TO:

InlineAlignment **INLINE_ALIGNMENT_BASELINE_TO** = `3`

Aligns the baseline (user defined) of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_BOTTOM_TO:

InlineAlignment **INLINE_ALIGNMENT_BOTTOM_TO** = `2`

Aligns the bottom of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_TOP:

InlineAlignment **INLINE_ALIGNMENT_TO_TOP** = `0`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the top of the text.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_CENTER:

InlineAlignment **INLINE_ALIGNMENT_TO_CENTER** = `4`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the center of the text.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_BASELINE:

InlineAlignment **INLINE_ALIGNMENT_TO_BASELINE** = `8`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the baseline of the text.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_BOTTOM:

InlineAlignment **INLINE_ALIGNMENT_TO_BOTTOM** = `12`

Aligns inline object (e.g. image, table) to the bottom of the text.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TOP:

InlineAlignment **INLINE_ALIGNMENT_TOP** = `0`

Aligns top of the inline object (e.g. image, table) to the top of the text. Equivalent to `INLINE_ALIGNMENT_TOP_TO | INLINE_ALIGNMENT_TO_TOP`.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_CENTER:

InlineAlignment **INLINE_ALIGNMENT_CENTER** = `5`

Aligns center of the inline object (e.g. image, table) to the center of the text. Equivalent to `INLINE_ALIGNMENT_CENTER_TO | INLINE_ALIGNMENT_TO_CENTER`.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_BOTTOM:

InlineAlignment **INLINE_ALIGNMENT_BOTTOM** = `14`

Aligns bottom of the inline object (e.g. image, table) to the bottom of the text. Equivalent to `INLINE_ALIGNMENT_BOTTOM_TO | INLINE_ALIGNMENT_TO_BOTTOM`.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_IMAGE_MASK:

InlineAlignment **INLINE_ALIGNMENT_IMAGE_MASK** = `3`

A bit mask for `INLINE_ALIGNMENT_*_TO` alignment constants.

.. _class_@GlobalScope_constant_INLINE_ALIGNMENT_TEXT_MASK:

InlineAlignment **INLINE_ALIGNMENT_TEXT_MASK** = `12`

A bit mask for `INLINE_ALIGNMENT_TO_*` alignment constants.

---

.. _enum_@GlobalScope_EulerOrder:

enum **EulerOrder**: 🔗

.. _class_@GlobalScope_constant_EULER_ORDER_XYZ:

EulerOrder **EULER_ORDER_XYZ** = `0`

Specifies that Euler angles should be in XYZ order. When composing, the order is X, Y, Z. When decomposing, the order is reversed, first Z, then Y, and X last.

.. _class_@GlobalScope_constant_EULER_ORDER_XZY:

EulerOrder **EULER_ORDER_XZY** = `1`

Specifies that Euler angles should be in XZY order. When composing, the order is X, Z, Y. When decomposing, the order is reversed, first Y, then Z, and X last.

.. _class_@GlobalScope_constant_EULER_ORDER_YXZ:

EulerOrder **EULER_ORDER_YXZ** = `2`

Specifies that Euler angles should be in YXZ order. When composing, the order is Y, X, Z. When decomposing, the order is reversed, first Z, then X, and Y last.

.. _class_@GlobalScope_constant_EULER_ORDER_YZX:

EulerOrder **EULER_ORDER_YZX** = `3`

Specifies that Euler angles should be in YZX order. When composing, the order is Y, Z, X. When decomposing, the order is reversed, first X, then Z, and Y last.

.. _class_@GlobalScope_constant_EULER_ORDER_ZXY:

EulerOrder **EULER_ORDER_ZXY** = `4`

Specifies that Euler angles should be in ZXY order. When composing, the order is Z, X, Y. When decomposing, the order is reversed, first Y, then X, and Z last.

.. _class_@GlobalScope_constant_EULER_ORDER_ZYX:

EulerOrder **EULER_ORDER_ZYX** = `5`

Specifies that Euler angles should be in ZYX order. When composing, the order is Z, Y, X. When decomposing, the order is reversed, first X, then Y, and Z last.

---

.. _enum_@GlobalScope_Key:

enum **Key**: 🔗

.. _class_@GlobalScope_constant_KEY_NONE:

Key **KEY_NONE** = `0`

Enum value which doesn't correspond to any key. This is used to initialize Key properties with a generic state.

.. _class_@GlobalScope_constant_KEY_SPECIAL:

Key **KEY_SPECIAL** = `4194304`

Keycodes with this bit applied are non-printable.

.. _class_@GlobalScope_constant_KEY_ESCAPE:

Key **KEY_ESCAPE** = `4194305`

Escape key.

.. _class_@GlobalScope_constant_KEY_TAB:

Key **KEY_TAB** = `4194306`

Tab key.

.. _class_@GlobalScope_constant_KEY_BACKTAB:

Key **KEY_BACKTAB** = `4194307`

Shift + Tab key.

.. _class_@GlobalScope_constant_KEY_BACKSPACE:

Key **KEY_BACKSPACE** = `4194308`

Backspace key.

.. _class_@GlobalScope_constant_KEY_ENTER:

Key **KEY_ENTER** = `4194309`

Return key (on the main keyboard).

.. _class_@GlobalScope_constant_KEY_KP_ENTER:

Key **KEY_KP_ENTER** = `4194310`

Enter key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_INSERT:

Key **KEY_INSERT** = `4194311`

Insert key.

.. _class_@GlobalScope_constant_KEY_DELETE:

Key **KEY_DELETE** = `4194312`

Delete key.

.. _class_@GlobalScope_constant_KEY_PAUSE:

Key **KEY_PAUSE** = `4194313`

Pause key.

.. _class_@GlobalScope_constant_KEY_PRINT:

Key **KEY_PRINT** = `4194314`

Print Screen key.

.. _class_@GlobalScope_constant_KEY_SYSREQ:

Key **KEY_SYSREQ** = `4194315`

System Request key.

.. _class_@GlobalScope_constant_KEY_CLEAR:

Key **KEY_CLEAR** = `4194316`

Clear key.

.. _class_@GlobalScope_constant_KEY_HOME:

Key **KEY_HOME** = `4194317`

Home key.

.. _class_@GlobalScope_constant_KEY_END:

Key **KEY_END** = `4194318`

End key.

.. _class_@GlobalScope_constant_KEY_LEFT:

Key **KEY_LEFT** = `4194319`

Left arrow key.

.. _class_@GlobalScope_constant_KEY_UP:

Key **KEY_UP** = `4194320`

Up arrow key.

.. _class_@GlobalScope_constant_KEY_RIGHT:

Key **KEY_RIGHT** = `4194321`

Right arrow key.

.. _class_@GlobalScope_constant_KEY_DOWN:

Key **KEY_DOWN** = `4194322`

Down arrow key.

.. _class_@GlobalScope_constant_KEY_PAGEUP:

Key **KEY_PAGEUP** = `4194323`

Page Up key.

.. _class_@GlobalScope_constant_KEY_PAGEDOWN:

Key **KEY_PAGEDOWN** = `4194324`

Page Down key.

.. _class_@GlobalScope_constant_KEY_SHIFT:

Key **KEY_SHIFT** = `4194325`

Shift key.

.. _class_@GlobalScope_constant_KEY_CTRL:

Key **KEY_CTRL** = `4194326`

Control key.

.. _class_@GlobalScope_constant_KEY_META:

Key **KEY_META** = `4194327`

Meta key.

.. _class_@GlobalScope_constant_KEY_ALT:

Key **KEY_ALT** = `4194328`

Alt key.

.. _class_@GlobalScope_constant_KEY_CAPSLOCK:

Key **KEY_CAPSLOCK** = `4194329`

Caps Lock key.

.. _class_@GlobalScope_constant_KEY_NUMLOCK:

Key **KEY_NUMLOCK** = `4194330`

Num Lock key.

.. _class_@GlobalScope_constant_KEY_SCROLLLOCK:

Key **KEY_SCROLLLOCK** = `4194331`

Scroll Lock key.

.. _class_@GlobalScope_constant_KEY_F1:

Key **KEY_F1** = `4194332`

F1 key.

.. _class_@GlobalScope_constant_KEY_F2:

Key **KEY_F2** = `4194333`

F2 key.

.. _class_@GlobalScope_constant_KEY_F3:

Key **KEY_F3** = `4194334`

F3 key.

.. _class_@GlobalScope_constant_KEY_F4:

Key **KEY_F4** = `4194335`

F4 key.

.. _class_@GlobalScope_constant_KEY_F5:

Key **KEY_F5** = `4194336`

F5 key.

.. _class_@GlobalScope_constant_KEY_F6:

Key **KEY_F6** = `4194337`

F6 key.

.. _class_@GlobalScope_constant_KEY_F7:

Key **KEY_F7** = `4194338`

F7 key.

.. _class_@GlobalScope_constant_KEY_F8:

Key **KEY_F8** = `4194339`

F8 key.

.. _class_@GlobalScope_constant_KEY_F9:

Key **KEY_F9** = `4194340`

F9 key.

.. _class_@GlobalScope_constant_KEY_F10:

Key **KEY_F10** = `4194341`

F10 key.

.. _class_@GlobalScope_constant_KEY_F11:

Key **KEY_F11** = `4194342`

F11 key.

.. _class_@GlobalScope_constant_KEY_F12:

Key **KEY_F12** = `4194343`

F12 key.

.. _class_@GlobalScope_constant_KEY_F13:

Key **KEY_F13** = `4194344`

F13 key.

.. _class_@GlobalScope_constant_KEY_F14:

Key **KEY_F14** = `4194345`

F14 key.

.. _class_@GlobalScope_constant_KEY_F15:

Key **KEY_F15** = `4194346`

F15 key.

.. _class_@GlobalScope_constant_KEY_F16:

Key **KEY_F16** = `4194347`

F16 key.

.. _class_@GlobalScope_constant_KEY_F17:

Key **KEY_F17** = `4194348`

F17 key.

.. _class_@GlobalScope_constant_KEY_F18:

Key **KEY_F18** = `4194349`

F18 key.

.. _class_@GlobalScope_constant_KEY_F19:

Key **KEY_F19** = `4194350`

F19 key.

.. _class_@GlobalScope_constant_KEY_F20:

Key **KEY_F20** = `4194351`

F20 key.

.. _class_@GlobalScope_constant_KEY_F21:

Key **KEY_F21** = `4194352`

F21 key.

.. _class_@GlobalScope_constant_KEY_F22:

Key **KEY_F22** = `4194353`

F22 key.

.. _class_@GlobalScope_constant_KEY_F23:

Key **KEY_F23** = `4194354`

F23 key.

.. _class_@GlobalScope_constant_KEY_F24:

Key **KEY_F24** = `4194355`

F24 key.

.. _class_@GlobalScope_constant_KEY_F25:

Key **KEY_F25** = `4194356`

F25 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F26:

Key **KEY_F26** = `4194357`

F26 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F27:

Key **KEY_F27** = `4194358`

F27 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F28:

Key **KEY_F28** = `4194359`

F28 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F29:

Key **KEY_F29** = `4194360`

F29 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F30:

Key **KEY_F30** = `4194361`

F30 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F31:

Key **KEY_F31** = `4194362`

F31 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F32:

Key **KEY_F32** = `4194363`

F32 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F33:

Key **KEY_F33** = `4194364`

F33 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F34:

Key **KEY_F34** = `4194365`

F34 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_F35:

Key **KEY_F35** = `4194366`

F35 key. Only supported on macOS and Linux due to a Windows limitation.

.. _class_@GlobalScope_constant_KEY_KP_MULTIPLY:

Key **KEY_KP_MULTIPLY** = `4194433`

Multiply (\*) key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_DIVIDE:

Key **KEY_KP_DIVIDE** = `4194434`

Divide (/) key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_SUBTRACT:

Key **KEY_KP_SUBTRACT** = `4194435`

Subtract (-) key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_PERIOD:

Key **KEY_KP_PERIOD** = `4194436`

Period (.) key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_ADD:

Key **KEY_KP_ADD** = `4194437`

Add (+) key on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_0:

Key **KEY_KP_0** = `4194438`

Number 0 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_1:

Key **KEY_KP_1** = `4194439`

Number 1 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_2:

Key **KEY_KP_2** = `4194440`

Number 2 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_3:

Key **KEY_KP_3** = `4194441`

Number 3 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_4:

Key **KEY_KP_4** = `4194442`

Number 4 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_5:

Key **KEY_KP_5** = `4194443`

Number 5 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_6:

Key **KEY_KP_6** = `4194444`

Number 6 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_7:

Key **KEY_KP_7** = `4194445`

Number 7 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_8:

Key **KEY_KP_8** = `4194446`

Number 8 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_KP_9:

Key **KEY_KP_9** = `4194447`

Number 9 on the numeric keypad.

.. _class_@GlobalScope_constant_KEY_MENU:

Key **KEY_MENU** = `4194370`

Context menu key.

.. _class_@GlobalScope_constant_KEY_HYPER:

Key **KEY_HYPER** = `4194371`

Hyper key. (On Linux/X11 only).

.. _class_@GlobalScope_constant_KEY_HELP:

Key **KEY_HELP** = `4194373`

Help key.

.. _class_@GlobalScope_constant_KEY_BACK:

Key **KEY_BACK** = `4194376`

Back key.

.. _class_@GlobalScope_constant_KEY_FORWARD:

Key **KEY_FORWARD** = `4194377`

Forward key.

.. _class_@GlobalScope_constant_KEY_STOP:

Key **KEY_STOP** = `4194378`

Media stop key.

.. _class_@GlobalScope_constant_KEY_REFRESH:

Key **KEY_REFRESH** = `4194379`

Refresh key.

.. _class_@GlobalScope_constant_KEY_VOLUMEDOWN:

Key **KEY_VOLUMEDOWN** = `4194380`

Volume down key.

.. _class_@GlobalScope_constant_KEY_VOLUMEMUTE:

Key **KEY_VOLUMEMUTE** = `4194381`

Mute volume key.

.. _class_@GlobalScope_constant_KEY_VOLUMEUP:

Key **KEY_VOLUMEUP** = `4194382`

Volume up key.

.. _class_@GlobalScope_constant_KEY_MEDIAPLAY:

Key **KEY_MEDIAPLAY** = `4194388`

Media play key.

.. _class_@GlobalScope_constant_KEY_MEDIASTOP:

Key **KEY_MEDIASTOP** = `4194389`

Media stop key.

.. _class_@GlobalScope_constant_KEY_MEDIAPREVIOUS:

Key **KEY_MEDIAPREVIOUS** = `4194390`

Previous song key.

.. _class_@GlobalScope_constant_KEY_MEDIANEXT:

Key **KEY_MEDIANEXT** = `4194391`

Next song key.

.. _class_@GlobalScope_constant_KEY_MEDIARECORD:

Key **KEY_MEDIARECORD** = `4194392`

Media record key.

.. _class_@GlobalScope_constant_KEY_HOMEPAGE:

Key **KEY_HOMEPAGE** = `4194393`

Home page key.

.. _class_@GlobalScope_constant_KEY_FAVORITES:

Key **KEY_FAVORITES** = `4194394`

Favorites key.

.. _class_@GlobalScope_constant_KEY_SEARCH:

Key **KEY_SEARCH** = `4194395`

Search key.

.. _class_@GlobalScope_constant_KEY_STANDBY:

Key **KEY_STANDBY** = `4194396`

Standby key.

.. _class_@GlobalScope_constant_KEY_OPENURL:

Key **KEY_OPENURL** = `4194397`

Open URL / Launch Browser key.

.. _class_@GlobalScope_constant_KEY_LAUNCHMAIL:

Key **KEY_LAUNCHMAIL** = `4194398`

Launch Mail key.

.. _class_@GlobalScope_constant_KEY_LAUNCHMEDIA:

Key **KEY_LAUNCHMEDIA** = `4194399`

Launch Media key.

.. _class_@GlobalScope_constant_KEY_LAUNCH0:

Key **KEY_LAUNCH0** = `4194400`

Launch Shortcut 0 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH1:

Key **KEY_LAUNCH1** = `4194401`

Launch Shortcut 1 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH2:

Key **KEY_LAUNCH2** = `4194402`

Launch Shortcut 2 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH3:

Key **KEY_LAUNCH3** = `4194403`

Launch Shortcut 3 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH4:

Key **KEY_LAUNCH4** = `4194404`

Launch Shortcut 4 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH5:

Key **KEY_LAUNCH5** = `4194405`

Launch Shortcut 5 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH6:

Key **KEY_LAUNCH6** = `4194406`

Launch Shortcut 6 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH7:

Key **KEY_LAUNCH7** = `4194407`

Launch Shortcut 7 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH8:

Key **KEY_LAUNCH8** = `4194408`

Launch Shortcut 8 key.

.. _class_@GlobalScope_constant_KEY_LAUNCH9:

Key **KEY_LAUNCH9** = `4194409`

Launch Shortcut 9 key.

.. _class_@GlobalScope_constant_KEY_LAUNCHA:

Key **KEY_LAUNCHA** = `4194410`

Launch Shortcut A key.

.. _class_@GlobalScope_constant_KEY_LAUNCHB:

Key **KEY_LAUNCHB** = `4194411`

Launch Shortcut B key.

.. _class_@GlobalScope_constant_KEY_LAUNCHC:

Key **KEY_LAUNCHC** = `4194412`

Launch Shortcut C key.

.. _class_@GlobalScope_constant_KEY_LAUNCHD:

Key **KEY_LAUNCHD** = `4194413`

Launch Shortcut D key.

.. _class_@GlobalScope_constant_KEY_LAUNCHE:

Key **KEY_LAUNCHE** = `4194414`

Launch Shortcut E key.

.. _class_@GlobalScope_constant_KEY_LAUNCHF:

Key **KEY_LAUNCHF** = `4194415`

Launch Shortcut F key.

.. _class_@GlobalScope_constant_KEY_GLOBE:

Key **KEY_GLOBE** = `4194416`

"Globe" key on Mac / iPad keyboard.

.. _class_@GlobalScope_constant_KEY_KEYBOARD:

Key **KEY_KEYBOARD** = `4194417`

"On-screen keyboard" key on iPad keyboard.

.. _class_@GlobalScope_constant_KEY_JIS_EISU:

Key **KEY_JIS_EISU** = `4194418`

英数 key on Mac keyboard.

.. _class_@GlobalScope_constant_KEY_JIS_KANA:

Key **KEY_JIS_KANA** = `4194419`

かな key on Mac keyboard.

.. _class_@GlobalScope_constant_KEY_UNKNOWN:

Key **KEY_UNKNOWN** = `8388607`

Unknown key.

.. _class_@GlobalScope_constant_KEY_SPACE:

Key **KEY_SPACE** = `32`

Space key.

.. _class_@GlobalScope_constant_KEY_EXCLAM:

Key **KEY_EXCLAM** = `33`

Exclamation mark (`!`) key.

.. _class_@GlobalScope_constant_KEY_QUOTEDBL:

Key **KEY_QUOTEDBL** = `34`

Double quotation mark (`"`) key.

.. _class_@GlobalScope_constant_KEY_NUMBERSIGN:

Key **KEY_NUMBERSIGN** = `35`

Number sign or *hash* (`#`) key.

.. _class_@GlobalScope_constant_KEY_DOLLAR:

Key **KEY_DOLLAR** = `36`

Dollar sign (`$`) key.

.. _class_@GlobalScope_constant_KEY_PERCENT:

Key **KEY_PERCENT** = `37`

Percent sign (`%`) key.

.. _class_@GlobalScope_constant_KEY_AMPERSAND:

Key **KEY_AMPERSAND** = `38`

Ampersand (`&`) key.

.. _class_@GlobalScope_constant_KEY_APOSTROPHE:

Key **KEY_APOSTROPHE** = `39`

Apostrophe (`'`) key.

.. _class_@GlobalScope_constant_KEY_PARENLEFT:

Key **KEY_PARENLEFT** = `40`

Left parenthesis (`(`) key.

.. _class_@GlobalScope_constant_KEY_PARENRIGHT:

Key **KEY_PARENRIGHT** = `41`

Right parenthesis (`)`) key.

.. _class_@GlobalScope_constant_KEY_ASTERISK:

Key **KEY_ASTERISK** = `42`

Asterisk (`*`) key.

.. _class_@GlobalScope_constant_KEY_PLUS:

Key **KEY_PLUS** = `43`

Plus (`+`) key.

.. _class_@GlobalScope_constant_KEY_COMMA:

Key **KEY_COMMA** = `44`

Comma (`,`) key.

.. _class_@GlobalScope_constant_KEY_MINUS:

Key **KEY_MINUS** = `45`

Minus (`-`) key.

.. _class_@GlobalScope_constant_KEY_PERIOD:

Key **KEY_PERIOD** = `46`

Period (`.`) key.

.. _class_@GlobalScope_constant_KEY_SLASH:

Key **KEY_SLASH** = `47`

Slash (`/`) key.

.. _class_@GlobalScope_constant_KEY_0:

Key **KEY_0** = `48`

Number 0 key.

.. _class_@GlobalScope_constant_KEY_1:

Key **KEY_1** = `49`

Number 1 key.

.. _class_@GlobalScope_constant_KEY_2:

Key **KEY_2** = `50`

Number 2 key.

.. _class_@GlobalScope_constant_KEY_3:

Key **KEY_3** = `51`

Number 3 key.

.. _class_@GlobalScope_constant_KEY_4:

Key **KEY_4** = `52`

Number 4 key.

.. _class_@GlobalScope_constant_KEY_5:

Key **KEY_5** = `53`

Number 5 key.

.. _class_@GlobalScope_constant_KEY_6:

Key **KEY_6** = `54`

Number 6 key.

.. _class_@GlobalScope_constant_KEY_7:

Key **KEY_7** = `55`

Number 7 key.

.. _class_@GlobalScope_constant_KEY_8:

Key **KEY_8** = `56`

Number 8 key.

.. _class_@GlobalScope_constant_KEY_9:

Key **KEY_9** = `57`

Number 9 key.

.. _class_@GlobalScope_constant_KEY_COLON:

Key **KEY_COLON** = `58`

Colon (`:`) key.

.. _class_@GlobalScope_constant_KEY_SEMICOLON:

Key **KEY_SEMICOLON** = `59`

Semicolon (`;`) key.

.. _class_@GlobalScope_constant_KEY_LESS:

Key **KEY_LESS** = `60`

Less-than sign (`<`) key.

.. _class_@GlobalScope_constant_KEY_EQUAL:

Key **KEY_EQUAL** = `61`

Equal sign (`=`) key.

.. _class_@GlobalScope_constant_KEY_GREATER:

Key **KEY_GREATER** = `62`

Greater-than sign (`>`) key.

.. _class_@GlobalScope_constant_KEY_QUESTION:

Key **KEY_QUESTION** = `63`

Question mark (`?`) key.

.. _class_@GlobalScope_constant_KEY_AT:

Key **KEY_AT** = `64`

At sign (`@`) key.

.. _class_@GlobalScope_constant_KEY_A:

Key **KEY_A** = `65`

A key.

.. _class_@GlobalScope_constant_KEY_B:

Key **KEY_B** = `66`

B key.

.. _class_@GlobalScope_constant_KEY_C:

Key **KEY_C** = `67`

C key.

.. _class_@GlobalScope_constant_KEY_D:

Key **KEY_D** = `68`

D key.

.. _class_@GlobalScope_constant_KEY_E:

Key **KEY_E** = `69`

E key.

.. _class_@GlobalScope_constant_KEY_F:

Key **KEY_F** = `70`

F key.

.. _class_@GlobalScope_constant_KEY_G:

Key **KEY_G** = `71`

G key.

.. _class_@GlobalScope_constant_KEY_H:

Key **KEY_H** = `72`

H key.

.. _class_@GlobalScope_constant_KEY_I:

Key **KEY_I** = `73`

I key.

.. _class_@GlobalScope_constant_KEY_J:

Key **KEY_J** = `74`

J key.

.. _class_@GlobalScope_constant_KEY_K:

Key **KEY_K** = `75`

K key.

.. _class_@GlobalScope_constant_KEY_L:

Key **KEY_L** = `76`

L key.

.. _class_@GlobalScope_constant_KEY_M:

Key **KEY_M** = `77`

M key.

.. _class_@GlobalScope_constant_KEY_N:

Key **KEY_N** = `78`

N key.

.. _class_@GlobalScope_constant_KEY_O:

Key **KEY_O** = `79`

O key.

.. _class_@GlobalScope_constant_KEY_P:

Key **KEY_P** = `80`

P key.

.. _class_@GlobalScope_constant_KEY_Q:

Key **KEY_Q** = `81`

Q key.

.. _class_@GlobalScope_constant_KEY_R:

Key **KEY_R** = `82`

R key.

.. _class_@GlobalScope_constant_KEY_S:

Key **KEY_S** = `83`

S key.

.. _class_@GlobalScope_constant_KEY_T:

Key **KEY_T** = `84`

T key.

.. _class_@GlobalScope_constant_KEY_U:

Key **KEY_U** = `85`

U key.

.. _class_@GlobalScope_constant_KEY_V:

Key **KEY_V** = `86`

V key.

.. _class_@GlobalScope_constant_KEY_W:

Key **KEY_W** = `87`

W key.

.. _class_@GlobalScope_constant_KEY_X:

Key **KEY_X** = `88`

X key.

.. _class_@GlobalScope_constant_KEY_Y:

Key **KEY_Y** = `89`

Y key.

.. _class_@GlobalScope_constant_KEY_Z:

Key **KEY_Z** = `90`

Z key.

.. _class_@GlobalScope_constant_KEY_BRACKETLEFT:

Key **KEY_BRACKETLEFT** = `91`

Left bracket (`[lb]`) key.

.. _class_@GlobalScope_constant_KEY_BACKSLASH:

Key **KEY_BACKSLASH** = `92`

Backslash (`\`) key.

.. _class_@GlobalScope_constant_KEY_BRACKETRIGHT:

Key **KEY_BRACKETRIGHT** = `93`

Right bracket (`[rb]`) key.

.. _class_@GlobalScope_constant_KEY_ASCIICIRCUM:

Key **KEY_ASCIICIRCUM** = `94`

Caret (`^`) key.

.. _class_@GlobalScope_constant_KEY_UNDERSCORE:

Key **KEY_UNDERSCORE** = `95`

Underscore (`_`) key.

.. _class_@GlobalScope_constant_KEY_QUOTELEFT:

Key **KEY_QUOTELEFT** = `96`

Backtick (`````) key.

.. _class_@GlobalScope_constant_KEY_BRACELEFT:

Key **KEY_BRACELEFT** = `123`

Left brace (`{`) key.

.. _class_@GlobalScope_constant_KEY_BAR:

Key **KEY_BAR** = `124`

Vertical bar or *pipe* (`|`) key.

.. _class_@GlobalScope_constant_KEY_BRACERIGHT:

Key **KEY_BRACERIGHT** = `125`

Right brace (`}`) key.

.. _class_@GlobalScope_constant_KEY_ASCIITILDE:

Key **KEY_ASCIITILDE** = `126`

Tilde (`~`) key.

.. _class_@GlobalScope_constant_KEY_YEN:

Key **KEY_YEN** = `165`

Yen symbol (`¥`) key.

.. _class_@GlobalScope_constant_KEY_SECTION:

Key **KEY_SECTION** = `167`

Section sign (`§`) key.

---

.. _enum_@GlobalScope_KeyModifierMask:

flags **KeyModifierMask**: 🔗

.. _class_@GlobalScope_constant_KEY_CODE_MASK:

KeyModifierMask **KEY_CODE_MASK** = `8388607`

Key Code mask.

.. _class_@GlobalScope_constant_KEY_MODIFIER_MASK:

KeyModifierMask **KEY_MODIFIER_MASK** = `2130706432`

Modifier key mask.

.. _class_@GlobalScope_constant_KEY_MASK_CMD_OR_CTRL:

KeyModifierMask **KEY_MASK_CMD_OR_CTRL** = `16777216`

Automatically remapped to KEY_META on macOS and KEY_CTRL on other platforms, this mask is never set in the actual events, and should be used for key mapping only.

.. _class_@GlobalScope_constant_KEY_MASK_SHIFT:

KeyModifierMask **KEY_MASK_SHIFT** = `33554432`

Shift key mask.

.. _class_@GlobalScope_constant_KEY_MASK_ALT:

KeyModifierMask **KEY_MASK_ALT** = `67108864`

Alt or Option (on macOS) key mask.

.. _class_@GlobalScope_constant_KEY_MASK_META:

KeyModifierMask **KEY_MASK_META** = `134217728`

Command (on macOS) or Meta/Windows key mask.

.. _class_@GlobalScope_constant_KEY_MASK_CTRL:

KeyModifierMask **KEY_MASK_CTRL** = `268435456`

Control key mask.

.. _class_@GlobalScope_constant_KEY_MASK_KPAD:

KeyModifierMask **KEY_MASK_KPAD** = `536870912`

Keypad key mask.

.. _class_@GlobalScope_constant_KEY_MASK_GROUP_SWITCH:

KeyModifierMask **KEY_MASK_GROUP_SWITCH** = `1073741824`

Group Switch key mask.

---

.. _enum_@GlobalScope_KeyLocation:

enum **KeyLocation**: 🔗

.. _class_@GlobalScope_constant_KEY_LOCATION_UNSPECIFIED:

KeyLocation **KEY_LOCATION_UNSPECIFIED** = `0`

Used for keys which only appear once, or when a comparison doesn't need to differentiate the `LEFT` and `RIGHT` versions.

For example, when using [InputEvent.is_match()](class_inputevent.md#class_InputEvent_method_is_match), an event which has KEY_LOCATION_UNSPECIFIED will match any KeyLocation on the passed event.

.. _class_@GlobalScope_constant_KEY_LOCATION_LEFT:

KeyLocation **KEY_LOCATION_LEFT** = `1`

A key which is to the left of its twin.

.. _class_@GlobalScope_constant_KEY_LOCATION_RIGHT:

KeyLocation **KEY_LOCATION_RIGHT** = `2`

A key which is to the right of its twin.

---

.. _enum_@GlobalScope_MouseButton:

enum **MouseButton**: 🔗

.. _class_@GlobalScope_constant_MOUSE_BUTTON_NONE:

MouseButton **MOUSE_BUTTON_NONE** = `0`

Enum value which doesn't correspond to any mouse button. This is used to initialize MouseButton properties with a generic state.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_LEFT:

MouseButton **MOUSE_BUTTON_LEFT** = `1`

Primary mouse button, usually assigned to the left button.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_RIGHT:

MouseButton **MOUSE_BUTTON_RIGHT** = `2`

Secondary mouse button, usually assigned to the right button.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MIDDLE:

MouseButton **MOUSE_BUTTON_MIDDLE** = `3`

Middle mouse button.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_UP:

MouseButton **MOUSE_BUTTON_WHEEL_UP** = `4`

Mouse wheel scrolling up.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_DOWN:

MouseButton **MOUSE_BUTTON_WHEEL_DOWN** = `5`

Mouse wheel scrolling down.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_LEFT:

MouseButton **MOUSE_BUTTON_WHEEL_LEFT** = `6`

Mouse wheel left button (only present on some mice).

.. _class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_RIGHT:

MouseButton **MOUSE_BUTTON_WHEEL_RIGHT** = `7`

Mouse wheel right button (only present on some mice).

.. _class_@GlobalScope_constant_MOUSE_BUTTON_XBUTTON1:

MouseButton **MOUSE_BUTTON_XBUTTON1** = `8`

Extra mouse button 1. This is sometimes present, usually to the sides of the mouse.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_XBUTTON2:

MouseButton **MOUSE_BUTTON_XBUTTON2** = `9`

Extra mouse button 2. This is sometimes present, usually to the sides of the mouse.

---

.. _enum_@GlobalScope_MouseButtonMask:

flags **MouseButtonMask**: 🔗

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MASK_LEFT:

MouseButtonMask **MOUSE_BUTTON_MASK_LEFT** = `1`

Primary mouse button mask, usually for the left button.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MASK_RIGHT:

MouseButtonMask **MOUSE_BUTTON_MASK_RIGHT** = `2`

Secondary mouse button mask, usually for the right button.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MIDDLE:

MouseButtonMask **MOUSE_BUTTON_MASK_MIDDLE** = `4`

Middle mouse button mask.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MB_XBUTTON1:

MouseButtonMask **MOUSE_BUTTON_MASK_MB_XBUTTON1** = `128`

Extra mouse button 1 mask.

.. _class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MB_XBUTTON2:

MouseButtonMask **MOUSE_BUTTON_MASK_MB_XBUTTON2** = `256`

Extra mouse button 2 mask.

---

.. _enum_@GlobalScope_JoyButton:

enum **JoyButton**: 🔗

.. _class_@GlobalScope_constant_JOY_BUTTON_INVALID:

JoyButton **JOY_BUTTON_INVALID** = `-1`

An invalid game controller button.

.. _class_@GlobalScope_constant_JOY_BUTTON_A:

JoyButton **JOY_BUTTON_A** = `0`

Game controller SDL button A. Corresponds to the bottom action button: Sony Cross, Xbox A, Nintendo B.

.. _class_@GlobalScope_constant_JOY_BUTTON_B:

JoyButton **JOY_BUTTON_B** = `1`

Game controller SDL button B. Corresponds to the right action button: Sony Circle, Xbox B, Nintendo A.

.. _class_@GlobalScope_constant_JOY_BUTTON_X:

JoyButton **JOY_BUTTON_X** = `2`

Game controller SDL button X. Corresponds to the left action button: Sony Square, Xbox X, Nintendo Y.

.. _class_@GlobalScope_constant_JOY_BUTTON_Y:

JoyButton **JOY_BUTTON_Y** = `3`

Game controller SDL button Y. Corresponds to the top action button: Sony Triangle, Xbox Y, Nintendo X.

.. _class_@GlobalScope_constant_JOY_BUTTON_BACK:

JoyButton **JOY_BUTTON_BACK** = `4`

Game controller SDL back button. Corresponds to the Sony Select, Xbox Back, Nintendo - button.

.. _class_@GlobalScope_constant_JOY_BUTTON_GUIDE:

JoyButton **JOY_BUTTON_GUIDE** = `5`

Game controller SDL guide button. Corresponds to the Sony PS, Xbox Home button.

.. _class_@GlobalScope_constant_JOY_BUTTON_START:

JoyButton **JOY_BUTTON_START** = `6`

Game controller SDL start button. Corresponds to the Sony Options, Xbox Menu, Nintendo + button.

.. _class_@GlobalScope_constant_JOY_BUTTON_LEFT_STICK:

JoyButton **JOY_BUTTON_LEFT_STICK** = `7`

Game controller SDL left stick button. Corresponds to the Sony L3, Xbox L/LS button.

.. _class_@GlobalScope_constant_JOY_BUTTON_RIGHT_STICK:

JoyButton **JOY_BUTTON_RIGHT_STICK** = `8`

Game controller SDL right stick button. Corresponds to the Sony R3, Xbox R/RS button.

.. _class_@GlobalScope_constant_JOY_BUTTON_LEFT_SHOULDER:

JoyButton **JOY_BUTTON_LEFT_SHOULDER** = `9`

Game controller SDL left shoulder button. Corresponds to the Sony L1, Xbox LB button.

.. _class_@GlobalScope_constant_JOY_BUTTON_RIGHT_SHOULDER:

JoyButton **JOY_BUTTON_RIGHT_SHOULDER** = `10`

Game controller SDL right shoulder button. Corresponds to the Sony R1, Xbox RB button.

.. _class_@GlobalScope_constant_JOY_BUTTON_DPAD_UP:

JoyButton **JOY_BUTTON_DPAD_UP** = `11`

Game controller D-pad up button.

.. _class_@GlobalScope_constant_JOY_BUTTON_DPAD_DOWN:

JoyButton **JOY_BUTTON_DPAD_DOWN** = `12`

Game controller D-pad down button.

.. _class_@GlobalScope_constant_JOY_BUTTON_DPAD_LEFT:

JoyButton **JOY_BUTTON_DPAD_LEFT** = `13`

Game controller D-pad left button.

.. _class_@GlobalScope_constant_JOY_BUTTON_DPAD_RIGHT:

JoyButton **JOY_BUTTON_DPAD_RIGHT** = `14`

Game controller D-pad right button.

.. _class_@GlobalScope_constant_JOY_BUTTON_MISC1:

JoyButton **JOY_BUTTON_MISC1** = `15`

Game controller SDL miscellaneous button. Corresponds to Xbox share button, PS5 microphone button, Nintendo Switch capture button.

.. _class_@GlobalScope_constant_JOY_BUTTON_PADDLE1:

JoyButton **JOY_BUTTON_PADDLE1** = `16`

Game controller SDL paddle 1 button.

.. _class_@GlobalScope_constant_JOY_BUTTON_PADDLE2:

JoyButton **JOY_BUTTON_PADDLE2** = `17`

Game controller SDL paddle 2 button.

.. _class_@GlobalScope_constant_JOY_BUTTON_PADDLE3:

JoyButton **JOY_BUTTON_PADDLE3** = `18`

Game controller SDL paddle 3 button.

.. _class_@GlobalScope_constant_JOY_BUTTON_PADDLE4:

JoyButton **JOY_BUTTON_PADDLE4** = `19`

Game controller SDL paddle 4 button.

.. _class_@GlobalScope_constant_JOY_BUTTON_TOUCHPAD:

JoyButton **JOY_BUTTON_TOUCHPAD** = `20`

Game controller SDL touchpad button.

.. _class_@GlobalScope_constant_JOY_BUTTON_SDL_MAX:

JoyButton **JOY_BUTTON_SDL_MAX** = `21`

The number of SDL game controller buttons.

.. _class_@GlobalScope_constant_JOY_BUTTON_MAX:

JoyButton **JOY_BUTTON_MAX** = `128`

The maximum number of game controller buttons supported by the engine. The actual limit may be lower on specific platforms:

- **Android:** Up to 36 buttons.

- **Linux:** Up to 80 buttons.

- **Windows** and **macOS:** Up to 128 buttons.

---

.. _enum_@GlobalScope_JoyAxis:

enum **JoyAxis**: 🔗

.. _class_@GlobalScope_constant_JOY_AXIS_INVALID:

JoyAxis **JOY_AXIS_INVALID** = `-1`

An invalid game controller axis.

.. _class_@GlobalScope_constant_JOY_AXIS_LEFT_X:

JoyAxis **JOY_AXIS_LEFT_X** = `0`

Game controller left joystick x-axis.

.. _class_@GlobalScope_constant_JOY_AXIS_LEFT_Y:

JoyAxis **JOY_AXIS_LEFT_Y** = `1`

Game controller left joystick y-axis.

.. _class_@GlobalScope_constant_JOY_AXIS_RIGHT_X:

JoyAxis **JOY_AXIS_RIGHT_X** = `2`

Game controller right joystick x-axis.

.. _class_@GlobalScope_constant_JOY_AXIS_RIGHT_Y:

JoyAxis **JOY_AXIS_RIGHT_Y** = `3`

Game controller right joystick y-axis.

.. _class_@GlobalScope_constant_JOY_AXIS_TRIGGER_LEFT:

JoyAxis **JOY_AXIS_TRIGGER_LEFT** = `4`

Game controller left trigger axis.

.. _class_@GlobalScope_constant_JOY_AXIS_TRIGGER_RIGHT:

JoyAxis **JOY_AXIS_TRIGGER_RIGHT** = `5`

Game controller right trigger axis.

.. _class_@GlobalScope_constant_JOY_AXIS_SDL_MAX:

JoyAxis **JOY_AXIS_SDL_MAX** = `6`

The number of SDL game controller axes.

.. _class_@GlobalScope_constant_JOY_AXIS_MAX:

JoyAxis **JOY_AXIS_MAX** = `10`

The maximum number of game controller axes: OpenVR supports up to 5 Joysticks making a total of 10 axes.

---

.. _enum_@GlobalScope_MIDIMessage:

enum **MIDIMessage**: 🔗

.. _class_@GlobalScope_constant_MIDI_MESSAGE_NONE:

MIDIMessage **MIDI_MESSAGE_NONE** = `0`

Does not correspond to any MIDI message. This is the default value of [InputEventMIDI.message](class_inputeventmidi.md#class_InputEventMIDI_property_message).

.. _class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_OFF:

MIDIMessage **MIDI_MESSAGE_NOTE_OFF** = `8`

MIDI message sent when a note is released.

 **Note:** Not all MIDI devices send this message; some may send MIDI_MESSAGE_NOTE_ON with [InputEventMIDI.velocity](class_inputeventmidi.md#class_InputEventMIDI_property_velocity) set to `0`.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_ON:

MIDIMessage **MIDI_MESSAGE_NOTE_ON** = `9`

MIDI message sent when a note is pressed.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_AFTERTOUCH:

MIDIMessage **MIDI_MESSAGE_AFTERTOUCH** = `10`

MIDI message sent to indicate a change in pressure while a note is being pressed down, also called aftertouch.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_CONTROL_CHANGE:

MIDIMessage **MIDI_MESSAGE_CONTROL_CHANGE** = `11`

MIDI message sent when a controller value changes. In a MIDI device, a controller is any input that doesn't play notes. These may include sliders for volume, balance, and panning, as well as switches and pedals. See the General MIDI specification for a small list.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_PROGRAM_CHANGE:

MIDIMessage **MIDI_MESSAGE_PROGRAM_CHANGE** = `12`

MIDI message sent when the MIDI device changes its current instrument (also called *program* or *preset*).

.. _class_@GlobalScope_constant_MIDI_MESSAGE_CHANNEL_PRESSURE:

MIDIMessage **MIDI_MESSAGE_CHANNEL_PRESSURE** = `13`

MIDI message sent to indicate a change in pressure for the whole channel. Some MIDI devices may send this instead of MIDI_MESSAGE_AFTERTOUCH.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_PITCH_BEND:

MIDIMessage **MIDI_MESSAGE_PITCH_BEND** = `14`

MIDI message sent when the value of the pitch bender changes, usually a wheel on the MIDI device.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_SYSTEM_EXCLUSIVE:

MIDIMessage **MIDI_MESSAGE_SYSTEM_EXCLUSIVE** = `240`

MIDI system exclusive (SysEx) message. This type of message is not standardized and it's highly dependent on the MIDI device sending it.

 **Note:** Getting this message's data from [InputEventMIDI](class_inputeventmidi.md#class_InputEventMIDI) is not implemented.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_QUARTER_FRAME:

MIDIMessage **MIDI_MESSAGE_QUARTER_FRAME** = `241`

MIDI message sent every quarter frame to keep connected MIDI devices synchronized. Related to MIDI_MESSAGE_TIMING_CLOCK.

 **Note:** Getting this message's data from [InputEventMIDI](class_inputeventmidi.md#class_InputEventMIDI) is not implemented.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_SONG_POSITION_POINTER:

MIDIMessage **MIDI_MESSAGE_SONG_POSITION_POINTER** = `242`

MIDI message sent to jump onto a new position in the current sequence or song.

 **Note:** Getting this message's data from [InputEventMIDI](class_inputeventmidi.md#class_InputEventMIDI) is not implemented.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_SONG_SELECT:

MIDIMessage **MIDI_MESSAGE_SONG_SELECT** = `243`

MIDI message sent to select a sequence or song to play.

 **Note:** Getting this message's data from [InputEventMIDI](class_inputeventmidi.md#class_InputEventMIDI) is not implemented.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_TUNE_REQUEST:

MIDIMessage **MIDI_MESSAGE_TUNE_REQUEST** = `246`

MIDI message sent to request a tuning calibration. Used on analog synthesizers. Most modern MIDI devices do not need this message.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_TIMING_CLOCK:

MIDIMessage **MIDI_MESSAGE_TIMING_CLOCK** = `248`

MIDI message sent 24 times after MIDI_MESSAGE_QUARTER_FRAME, to keep connected MIDI devices synchronized.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_START:

MIDIMessage **MIDI_MESSAGE_START** = `250`

MIDI message sent to start the current sequence or song from the beginning.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_CONTINUE:

MIDIMessage **MIDI_MESSAGE_CONTINUE** = `251`

MIDI message sent to resume from the point the current sequence or song was paused.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_STOP:

MIDIMessage **MIDI_MESSAGE_STOP** = `252`

MIDI message sent to pause the current sequence or song.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_ACTIVE_SENSING:

MIDIMessage **MIDI_MESSAGE_ACTIVE_SENSING** = `254`

MIDI message sent repeatedly while the MIDI device is idle, to tell the receiver that the connection is alive. Most MIDI devices do not send this message.

.. _class_@GlobalScope_constant_MIDI_MESSAGE_SYSTEM_RESET:

MIDIMessage **MIDI_MESSAGE_SYSTEM_RESET** = `255`

MIDI message sent to reset a MIDI device to its default state, as if it was just turned on. It should not be sent when the MIDI device is being turned on.

---

.. _enum_@GlobalScope_Error:

enum **Error**: 🔗

.. _class_@GlobalScope_constant_OK:

Error **OK** = `0`

Methods that return Error return OK when no error occurred.

Since OK has value `0`, and all other error constants are positive integers, it can also be used in boolean checks.

::

    var error = method_that_returns_error()
    if error != OK:
        printerr("Failure!")

    # Or, alternatively:
    if error:
        printerr("Still failing!")

 **Note:** Many functions do not return an error code, but will print error messages to standard output.

.. _class_@GlobalScope_constant_FAILED:

Error **FAILED** = `1`

Generic error.

.. _class_@GlobalScope_constant_ERR_UNAVAILABLE:

Error **ERR_UNAVAILABLE** = `2`

Unavailable error.

.. _class_@GlobalScope_constant_ERR_UNCONFIGURED:

Error **ERR_UNCONFIGURED** = `3`

Unconfigured error.

.. _class_@GlobalScope_constant_ERR_UNAUTHORIZED:

Error **ERR_UNAUTHORIZED** = `4`

Unauthorized error.

.. _class_@GlobalScope_constant_ERR_PARAMETER_RANGE_ERROR:

Error **ERR_PARAMETER_RANGE_ERROR** = `5`

Parameter range error.

.. _class_@GlobalScope_constant_ERR_OUT_OF_MEMORY:

Error **ERR_OUT_OF_MEMORY** = `6`

Out of memory (OOM) error.

.. _class_@GlobalScope_constant_ERR_FILE_NOT_FOUND:

Error **ERR_FILE_NOT_FOUND** = `7`

File: Not found error.

.. _class_@GlobalScope_constant_ERR_FILE_BAD_DRIVE:

Error **ERR_FILE_BAD_DRIVE** = `8`

File: Bad drive error.

.. _class_@GlobalScope_constant_ERR_FILE_BAD_PATH:

Error **ERR_FILE_BAD_PATH** = `9`

File: Bad path error.

.. _class_@GlobalScope_constant_ERR_FILE_NO_PERMISSION:

Error **ERR_FILE_NO_PERMISSION** = `10`

File: No permission error.

.. _class_@GlobalScope_constant_ERR_FILE_ALREADY_IN_USE:

Error **ERR_FILE_ALREADY_IN_USE** = `11`

File: Already in use error.

.. _class_@GlobalScope_constant_ERR_FILE_CANT_OPEN:

Error **ERR_FILE_CANT_OPEN** = `12`

File: Can't open error.

.. _class_@GlobalScope_constant_ERR_FILE_CANT_WRITE:

Error **ERR_FILE_CANT_WRITE** = `13`

File: Can't write error.

.. _class_@GlobalScope_constant_ERR_FILE_CANT_READ:

Error **ERR_FILE_CANT_READ** = `14`

File: Can't read error.

.. _class_@GlobalScope_constant_ERR_FILE_UNRECOGNIZED:

Error **ERR_FILE_UNRECOGNIZED** = `15`

File: Unrecognized error.

.. _class_@GlobalScope_constant_ERR_FILE_CORRUPT:

Error **ERR_FILE_CORRUPT** = `16`

File: Corrupt error.

.. _class_@GlobalScope_constant_ERR_FILE_MISSING_DEPENDENCIES:

Error **ERR_FILE_MISSING_DEPENDENCIES** = `17`

File: Missing dependencies error.

.. _class_@GlobalScope_constant_ERR_FILE_EOF:

Error **ERR_FILE_EOF** = `18`

File: End of file (EOF) error.

.. _class_@GlobalScope_constant_ERR_CANT_OPEN:

Error **ERR_CANT_OPEN** = `19`

Can't open error.

.. _class_@GlobalScope_constant_ERR_CANT_CREATE:

Error **ERR_CANT_CREATE** = `20`

Can't create error.

.. _class_@GlobalScope_constant_ERR_QUERY_FAILED:

Error **ERR_QUERY_FAILED** = `21`

Query failed error.

.. _class_@GlobalScope_constant_ERR_ALREADY_IN_USE:

Error **ERR_ALREADY_IN_USE** = `22`

Already in use error.

.. _class_@GlobalScope_constant_ERR_LOCKED:

Error **ERR_LOCKED** = `23`

Locked error.

.. _class_@GlobalScope_constant_ERR_TIMEOUT:

Error **ERR_TIMEOUT** = `24`

Timeout error.

.. _class_@GlobalScope_constant_ERR_CANT_CONNECT:

Error **ERR_CANT_CONNECT** = `25`

Can't connect error.

.. _class_@GlobalScope_constant_ERR_CANT_RESOLVE:

Error **ERR_CANT_RESOLVE** = `26`

Can't resolve error.

.. _class_@GlobalScope_constant_ERR_CONNECTION_ERROR:

Error **ERR_CONNECTION_ERROR** = `27`

Connection error.

.. _class_@GlobalScope_constant_ERR_CANT_ACQUIRE_RESOURCE:

Error **ERR_CANT_ACQUIRE_RESOURCE** = `28`

Can't acquire resource error.

.. _class_@GlobalScope_constant_ERR_CANT_FORK:

Error **ERR_CANT_FORK** = `29`

Can't fork process error.

.. _class_@GlobalScope_constant_ERR_INVALID_DATA:

Error **ERR_INVALID_DATA** = `30`

Invalid data error.

.. _class_@GlobalScope_constant_ERR_INVALID_PARAMETER:

Error **ERR_INVALID_PARAMETER** = `31`

Invalid parameter error.

.. _class_@GlobalScope_constant_ERR_ALREADY_EXISTS:

Error **ERR_ALREADY_EXISTS** = `32`

Already exists error.

.. _class_@GlobalScope_constant_ERR_DOES_NOT_EXIST:

Error **ERR_DOES_NOT_EXIST** = `33`

Does not exist error.

.. _class_@GlobalScope_constant_ERR_DATABASE_CANT_READ:

Error **ERR_DATABASE_CANT_READ** = `34`

Database: Read error.

.. _class_@GlobalScope_constant_ERR_DATABASE_CANT_WRITE:

Error **ERR_DATABASE_CANT_WRITE** = `35`

Database: Write error.

.. _class_@GlobalScope_constant_ERR_COMPILATION_FAILED:

Error **ERR_COMPILATION_FAILED** = `36`

Compilation failed error.

.. _class_@GlobalScope_constant_ERR_METHOD_NOT_FOUND:

Error **ERR_METHOD_NOT_FOUND** = `37`

Method not found error.

.. _class_@GlobalScope_constant_ERR_LINK_FAILED:

Error **ERR_LINK_FAILED** = `38`

Linking failed error.

.. _class_@GlobalScope_constant_ERR_SCRIPT_FAILED:

Error **ERR_SCRIPT_FAILED** = `39`

Script failed error.

.. _class_@GlobalScope_constant_ERR_CYCLIC_LINK:

Error **ERR_CYCLIC_LINK** = `40`

Cycling link (import cycle) error.

.. _class_@GlobalScope_constant_ERR_INVALID_DECLARATION:

Error **ERR_INVALID_DECLARATION** = `41`

Invalid declaration error.

.. _class_@GlobalScope_constant_ERR_DUPLICATE_SYMBOL:

Error **ERR_DUPLICATE_SYMBOL** = `42`

Duplicate symbol error.

.. _class_@GlobalScope_constant_ERR_PARSE_ERROR:

Error **ERR_PARSE_ERROR** = `43`

Parse error.

.. _class_@GlobalScope_constant_ERR_BUSY:

Error **ERR_BUSY** = `44`

Busy error.

.. _class_@GlobalScope_constant_ERR_SKIP:

Error **ERR_SKIP** = `45`

Skip error.

.. _class_@GlobalScope_constant_ERR_HELP:

Error **ERR_HELP** = `46`

Help error. Used internally when passing `--version` or `--help` as executable options.

.. _class_@GlobalScope_constant_ERR_BUG:

Error **ERR_BUG** = `47`

Bug error, caused by an implementation issue in the method.

 **Note:** If a built-in method returns this code, please open an issue on the GitHub Issue Tracker.

.. _class_@GlobalScope_constant_ERR_PRINTER_ON_FIRE:

Error **ERR_PRINTER_ON_FIRE** = `48`

Printer on fire error (This is an easter egg, no built-in methods return this error code).

---

.. _enum_@GlobalScope_PropertyHint:

enum **PropertyHint**: 🔗

.. _class_@GlobalScope_constant_PROPERTY_HINT_NONE:

PropertyHint **PROPERTY_HINT_NONE** = `0`

The property has no hint for the editor.

.. _class_@GlobalScope_constant_PROPERTY_HINT_RANGE:

PropertyHint **PROPERTY_HINT_RANGE** = `1`

Hints that an [int](class_int.md#class_int) or [float](class_float.md#class_float) property should be within a range specified via the hint string `"min,max"` or `"min,max,step"`. The hint string can optionally include `"or_greater"` and/or `"or_less"` to allow manual input going respectively above the max or below the min values.

 **Example:** `"-360,360,1,or_greater,or_less"`.

Additionally, other keywords can be included: `"exp"` for exponential range editing, `"radians_as_degrees"` for editing radian angles in degrees (the range values are also in degrees), `"degrees"` to hint at an angle, `"prefer_slider"` to show the slider for integers, `"hide_control"` to hide the slider or up-down arrows, and `"suffix:px/s"` to display a suffix indicating the value's unit (e.g. `px/s` for pixels per second).

.. _class_@GlobalScope_constant_PROPERTY_HINT_ENUM:

PropertyHint **PROPERTY_HINT_ENUM** = `2`

Hints that an [int](class_int.md#class_int), [String](class_string.md#class_String), or [StringName](class_stringname.md#class_StringName) property is an enumerated value to pick in a list specified via a hint string.

The hint string is a comma separated list of names such as `"Hello,Something,Else"`. Whitespace is **not** removed from either end of a name. For integer properties, the first name in the list has value 0, the next 1, and so on. Explicit values can also be specified by appending `:integer` to the name, e.g. `"Zero,One,Three:3,Four,Six:6"`.

.. _class_@GlobalScope_constant_PROPERTY_HINT_ENUM_SUGGESTION:

PropertyHint **PROPERTY_HINT_ENUM_SUGGESTION** = `3`

Hints that a [String](class_string.md#class_String) or [StringName](class_stringname.md#class_StringName) property can be an enumerated value to pick in a list specified via a hint string such as `"Hello,Something,Else"`. See PROPERTY_HINT_ENUM for details.

Unlike PROPERTY_HINT_ENUM, a property with this hint still accepts arbitrary values and can be empty. The list of values serves to suggest possible values.

.. _class_@GlobalScope_constant_PROPERTY_HINT_EXP_EASING:

PropertyHint **PROPERTY_HINT_EXP_EASING** = `4`

Hints that a [float](class_float.md#class_float) property should be edited via an exponential easing function. The hint string can include `"attenuation"` to flip the curve horizontally and/or `"positive_only"` to exclude in/out easing and limit values to be greater than or equal to zero.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LINK:

PropertyHint **PROPERTY_HINT_LINK** = `5`

Hints that a vector property should allow its components to be linked. For example, this allows [Vector2.x](class_vector2.md#class_Vector2_property_x) and [Vector2.y](class_vector2.md#class_Vector2_property_y) to be edited together.

.. _class_@GlobalScope_constant_PROPERTY_HINT_FLAGS:

PropertyHint **PROPERTY_HINT_FLAGS** = `6`

Hints that an [int](class_int.md#class_int) property is a bitmask with named bit flags.

The hint string is a comma separated list of names such as `"Bit0,Bit1,Bit2,Bit3"`. Whitespace is **not** removed from either end of a name. The first name in the list has value 1, the next 2, then 4, 8, 16 and so on. Explicit values can also be specified by appending `:integer` to the name, e.g. `"A:4,B:8,C:16"`. You can also combine several flags (`"A:4,B:8,AB:12,C:16"`).

 **Note:** A flag value must be at least `1` and at most `2 ** 32 - 1`.

 **Note:** Unlike PROPERTY_HINT_ENUM, the previous explicit value is not taken into account. For the hint `"A:16,B,C"`, A is 16, B is 2, C is 4.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_RENDER:

PropertyHint **PROPERTY_HINT_LAYERS_2D_RENDER** = `7`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 2D render layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_PHYSICS:

PropertyHint **PROPERTY_HINT_LAYERS_2D_PHYSICS** = `8`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 2D physics layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_NAVIGATION:

PropertyHint **PROPERTY_HINT_LAYERS_2D_NAVIGATION** = `9`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 2D navigation layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_RENDER:

PropertyHint **PROPERTY_HINT_LAYERS_3D_RENDER** = `10`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 3D render layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_PHYSICS:

PropertyHint **PROPERTY_HINT_LAYERS_3D_PHYSICS** = `11`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 3D physics layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_NAVIGATION:

PropertyHint **PROPERTY_HINT_LAYERS_3D_NAVIGATION** = `12`

Hints that an [int](class_int.md#class_int) property is a bitmask using the optionally named 3D navigation layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_AVOIDANCE:

PropertyHint **PROPERTY_HINT_LAYERS_AVOIDANCE** = `37`

Hints that an integer property is a bitmask using the optionally named avoidance layers.

.. _class_@GlobalScope_constant_PROPERTY_HINT_FILE:

PropertyHint **PROPERTY_HINT_FILE** = `13`

Hints that a [String](class_string.md#class_String) property is a path to a file. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. By default the file will be stored as UID whenever available. You can use [ResourceUID](class_resourceuid.md#class_ResourceUID) methods to convert it back to path. For storing a raw path, use PROPERTY_HINT_FILE_PATH.

.. _class_@GlobalScope_constant_PROPERTY_HINT_DIR:

PropertyHint **PROPERTY_HINT_DIR** = `14`

Hints that a [String](class_string.md#class_String) property is a path to a directory. Editing it will show a file dialog for picking the path.

.. _class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_FILE:

PropertyHint **PROPERTY_HINT_GLOBAL_FILE** = `15`

Hints that a [String](class_string.md#class_String) property is an absolute path to a file outside the project folder. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards, like `"*.png,*.jpg"`.

.. _class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_DIR:

PropertyHint **PROPERTY_HINT_GLOBAL_DIR** = `16`

Hints that a [String](class_string.md#class_String) property is an absolute path to a directory outside the project folder. Editing it will show a file dialog for picking the path.

.. _class_@GlobalScope_constant_PROPERTY_HINT_RESOURCE_TYPE:

PropertyHint **PROPERTY_HINT_RESOURCE_TYPE** = `17`

Hints that a property is an instance of a [Resource](class_resource.md#class_Resource)-derived type, optionally specified via the hint string (e.g. `"Texture2D"`). Editing it will show a popup menu of valid resource types to instantiate.

.. _class_@GlobalScope_constant_PROPERTY_HINT_MULTILINE_TEXT:

PropertyHint **PROPERTY_HINT_MULTILINE_TEXT** = `18`

Hints that a [String](class_string.md#class_String) property is text with line breaks. Editing it will show a text input field where line breaks can be typed.

The hint string can be set to `"monospace"` to force the input field to use a monospaced font.

If the hint string `"no_wrap"` is set, the input field will not wrap lines at boundaries, instead resorting to making the area scrollable.

.. _class_@GlobalScope_constant_PROPERTY_HINT_EXPRESSION:

PropertyHint **PROPERTY_HINT_EXPRESSION** = `19`

Hints that a [String](class_string.md#class_String) property is an [Expression](class_expression.md#class_Expression).

.. _class_@GlobalScope_constant_PROPERTY_HINT_PLACEHOLDER_TEXT:

PropertyHint **PROPERTY_HINT_PLACEHOLDER_TEXT** = `20`

Hints that a [String](class_string.md#class_String) property should show a placeholder text on its input field, if empty. The hint string is the placeholder text to use.

.. _class_@GlobalScope_constant_PROPERTY_HINT_COLOR_NO_ALPHA:

PropertyHint **PROPERTY_HINT_COLOR_NO_ALPHA** = `21`

Hints that a [Color](class_color.md#class_Color) property should be edited without affecting its transparency ([Color.a](class_color.md#class_Color_property_a) is not editable).

.. _class_@GlobalScope_constant_PROPERTY_HINT_OBJECT_ID:

PropertyHint **PROPERTY_HINT_OBJECT_ID** = `22`

Hints that the property's value is an object encoded as object ID, with its type specified in the hint string. Used by the debugger.

.. _class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING:

PropertyHint **PROPERTY_HINT_TYPE_STRING** = `23`

If a property is [String](class_string.md#class_String), hints that the property represents a particular type (class). This allows to select a type from the create dialog. The property will store the selected type as a string.

If a property is [Array](class_array.md#class_Array), hints the editor how to show elements. The `hint_string` must encode nested types using `":"` and `"/"`.

If a property is [Dictionary](class_dictionary.md#class_Dictionary), hints the editor how to show elements. The `hint_string` is the same as [Array](class_array.md#class_Array), with a `";"` separating the key and value.

.. tabs::

```
```

    # Array of elem_type.
    hint_string = "%d:" % [elem_type]
    hint_string = "%d/%d:%s" % [elem_type, elem_hint, elem_hint_string]
    # Two-dimensional array of elem_type (array of arrays of elem_type).
    hint_string = "%d:%d:" % [TYPE_ARRAY, elem_type]
    hint_string = "%d:%d/%d:%s" % [TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]
    # Three-dimensional array of elem_type (array of arrays of arrays of elem_type).
    hint_string = "%d:%d:%d:" % [TYPE_ARRAY, TYPE_ARRAY, elem_type]
    hint_string = "%d:%d:%d/%d:%s" % [TYPE_ARRAY, TYPE_ARRAY, elem_type, elem_hint, elem_hint_string]

```
```

    // Array of elemType.
    hintString = $"{elemType:D}:";
    hintString = $"{elemType:}/{elemHint:D}:{elemHintString}";
    // Two-dimensional array of elemType (array of arrays of elemType).
    hintString = $"{Variant.Type.Array:D}:{elemType:D}:";
    hintString = $"{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";
    // Three-dimensional array of elemType (array of arrays of arrays of elemType).
    hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}:";
    hintString = $"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";

 **Examples:**

.. tabs::

```
```

    hint_string = "%d:" % [TYPE_INT] # Array of integers.
    hint_string = "%d/%d:1,10,1" % [TYPE_INT, PROPERTY_HINT_RANGE] # Array of integers (in range from 1 to 10).
    hint_string = "%d/%d:Zero,One,Two" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
    hint_string = "%d/%d:Zero,One,Three:3,Six:6" % [TYPE_INT, PROPERTY_HINT_ENUM] # Array of integers (an enum).
    hint_string = "%d/%d:*.png" % [TYPE_STRING, PROPERTY_HINT_FILE] # Array of strings (file paths).
    hint_string = "%d/%d:Texture2D" % [TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE] # Array of textures.

    hint_string = "%d:%d:" % [TYPE_ARRAY, TYPE_FLOAT] # Two-dimensional array of floats.
    hint_string = "%d:%d/%d:" % [TYPE_ARRAY, TYPE_STRING, PROPERTY_HINT_MULTILINE_TEXT] # Two-dimensional array of multiline strings.
    hint_string = "%d:%d/%d:-1,1,0.1" % [TYPE_ARRAY, TYPE_FLOAT, PROPERTY_HINT_RANGE] # Two-dimensional array of floats (in range from -1 to 1).
    hint_string = "%d:%d/%d:Texture2D" % [TYPE_ARRAY, TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE] # Two-dimensional array of textures.

```
```

    hintString = $"{Variant.Type.Int:D}/{PropertyHint.Range:D}:1,10,1"; // Array of integers (in range from 1 to 10).
    hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Two"; // Array of integers (an enum).
    hintString = $"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Three:3,Six:6"; // Array of integers (an enum).
    hintString = $"{Variant.Type.String:D}/{PropertyHint.File:D}:*.png"; // Array of strings (file paths).
    hintString = $"{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Array of textures.

    hintString = $"{Variant.Type.Array:D}:{Variant.Type.Float:D}:"; // Two-dimensional array of floats.
    hintString = $"{Variant.Type.Array:D}:{Variant.Type.String:D}/{PropertyHint.MultilineText:D}:"; // Two-dimensional array of multiline strings.
    hintString = $"{Variant.Type.Array:D}:{Variant.Type.Float:D}/{PropertyHint.Range:D}:-1,1,0.1"; // Two-dimensional array of floats (in range from -1 to 1).
    hintString = $"{Variant.Type.Array:D}:{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Two-dimensional array of textures.

 **Note:** The trailing colon is required for properly detecting built-in types.

.. _class_@GlobalScope_constant_PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE:

PropertyHint **PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE** = `24`

**Deprecated:** This hint is not used by the engine.

.. _class_@GlobalScope_constant_PROPERTY_HINT_OBJECT_TOO_BIG:

PropertyHint **PROPERTY_HINT_OBJECT_TOO_BIG** = `25`

Hints that an object is too big to be sent via the debugger.

.. _class_@GlobalScope_constant_PROPERTY_HINT_NODE_PATH_VALID_TYPES:

PropertyHint **PROPERTY_HINT_NODE_PATH_VALID_TYPES** = `26`

Hints that the hint string specifies valid node types for property of type [NodePath](class_nodepath.md#class_NodePath).

.. _class_@GlobalScope_constant_PROPERTY_HINT_SAVE_FILE:

PropertyHint **PROPERTY_HINT_SAVE_FILE** = `27`

Hints that a [String](class_string.md#class_String) property is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the project's directory. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. See also [FileDialog.filters](class_filedialog.md#class_FileDialog_property_filters).

.. _class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_SAVE_FILE:

PropertyHint **PROPERTY_HINT_GLOBAL_SAVE_FILE** = `28`

Hints that a [String](class_string.md#class_String) property is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the entire filesystem. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. See also [FileDialog.filters](class_filedialog.md#class_FileDialog_property_filters).

.. _class_@GlobalScope_constant_PROPERTY_HINT_INT_IS_OBJECTID:

PropertyHint **PROPERTY_HINT_INT_IS_OBJECTID** = `29`

**Deprecated:** This hint is not used by the engine.

.. _class_@GlobalScope_constant_PROPERTY_HINT_INT_IS_POINTER:

PropertyHint **PROPERTY_HINT_INT_IS_POINTER** = `30`

Hints that an [int](class_int.md#class_int) property is a pointer. Used by GDExtension.

.. _class_@GlobalScope_constant_PROPERTY_HINT_ARRAY_TYPE:

PropertyHint **PROPERTY_HINT_ARRAY_TYPE** = `31`

Hints that a property is an [Array](class_array.md#class_Array) with the stored type specified in the hint string. The hint string contains the type of the array (e.g. `"String"`).

Use the hint string format from PROPERTY_HINT_TYPE_STRING for more control over the stored type.

.. _class_@GlobalScope_constant_PROPERTY_HINT_DICTIONARY_TYPE:

PropertyHint **PROPERTY_HINT_DICTIONARY_TYPE** = `38`

Hints that a property is a [Dictionary](class_dictionary.md#class_Dictionary) with the stored types specified in the hint string. The hint string contains the key and value types separated by a semicolon (e.g. `"int;String"`).

Use the hint string format from PROPERTY_HINT_TYPE_STRING for more control over the stored types.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LOCALE_ID:

PropertyHint **PROPERTY_HINT_LOCALE_ID** = `32`

Hints that a string property is a locale code. Editing it will show a locale dialog for picking language and country.

.. _class_@GlobalScope_constant_PROPERTY_HINT_LOCALIZABLE_STRING:

PropertyHint **PROPERTY_HINT_LOCALIZABLE_STRING** = `33`

Hints that a dictionary property is string translation map. Dictionary keys are locale codes and, values are translated strings.

.. _class_@GlobalScope_constant_PROPERTY_HINT_NODE_TYPE:

PropertyHint **PROPERTY_HINT_NODE_TYPE** = `34`

Hints that a property is an instance of a [Node](class_node.md#class_Node)-derived type, optionally specified via the hint string (e.g. `"Node2D"`). Editing it will show a dialog for picking a node from the scene.

.. _class_@GlobalScope_constant_PROPERTY_HINT_HIDE_QUATERNION_EDIT:

PropertyHint **PROPERTY_HINT_HIDE_QUATERNION_EDIT** = `35`

Hints that a quaternion property should disable the temporary euler editor.

.. _class_@GlobalScope_constant_PROPERTY_HINT_PASSWORD:

PropertyHint **PROPERTY_HINT_PASSWORD** = `36`

Hints that a string property is a password, and every character is replaced with the secret character.

.. _class_@GlobalScope_constant_PROPERTY_HINT_TOOL_BUTTON:

PropertyHint **PROPERTY_HINT_TOOL_BUTTON** = `39`

Hints that a [Callable](class_callable.md#class_Callable) property should be displayed as a clickable button. When the button is pressed, the callable is called. The hint string specifies the button text and optionally an icon from the `"EditorIcons"` theme type.

.. code:: text

    "Click me!" - A button with the text "Click me!" and the default "Callable" icon.
    "Click me!,ColorRect" - A button with the text "Click me!" and the "ColorRect" icon.

 **Note:** A [Callable](class_callable.md#class_Callable) cannot be properly serialized and stored in a file, so it is recommended to use PROPERTY_USAGE_EDITOR instead of PROPERTY_USAGE_DEFAULT.

.. _class_@GlobalScope_constant_PROPERTY_HINT_ONESHOT:

PropertyHint **PROPERTY_HINT_ONESHOT** = `40`

Hints that a property will be changed on its own after setting, such as [AudioStreamPlayer.playing](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playing) or [GPUParticles3D.emitting](class_gpuparticles3d.md#class_GPUParticles3D_property_emitting).

.. _class_@GlobalScope_constant_PROPERTY_HINT_GROUP_ENABLE:

PropertyHint **PROPERTY_HINT_GROUP_ENABLE** = `42`

Hints that a boolean property will enable the feature associated with the group that it occurs in. The property will be displayed as a checkbox on the group header. Only works within a group or subgroup.

By default, disabling the property hides all properties in the group. Use the optional hint string `"checkbox_only"` to disable this behavior.

.. _class_@GlobalScope_constant_PROPERTY_HINT_INPUT_NAME:

PropertyHint **PROPERTY_HINT_INPUT_NAME** = `43`

Hints that a [String](class_string.md#class_String) or [StringName](class_stringname.md#class_StringName) property is the name of an input action. This allows the selection of any action name from the Input Map in the Project Settings. The hint string may contain two options separated by commas:

- If it contains `"show_builtin"`, built-in input actions are included in the selection.

- If it contains `"loose_mode"`, loose mode is enabled. This allows inserting any action name even if it's not present in the input map.

.. _class_@GlobalScope_constant_PROPERTY_HINT_FILE_PATH:

PropertyHint **PROPERTY_HINT_FILE_PATH** = `44`

Like PROPERTY_HINT_FILE, but the property is stored as a raw path, not UID. That means the reference will be broken if you move the file. Consider using PROPERTY_HINT_FILE when possible.

.. _class_@GlobalScope_constant_PROPERTY_HINT_MAX:

PropertyHint **PROPERTY_HINT_MAX** = `45`

Represents the size of the PropertyHint enum.

---

.. _enum_@GlobalScope_PropertyUsageFlags:

flags **PropertyUsageFlags**: 🔗

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NONE:

PropertyUsageFlags **PROPERTY_USAGE_NONE** = `0`

The property is not stored, and does not display in the editor. This is the default for non-exported properties.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE:

PropertyUsageFlags **PROPERTY_USAGE_STORAGE** = `2`

The property is serialized and saved in the scene file (default for exported properties).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR:

PropertyUsageFlags **PROPERTY_USAGE_EDITOR** = `4`

The property is shown in the [EditorInspector](class_editorinspector.md#class_EditorInspector) (default for exported properties).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_INTERNAL:

PropertyUsageFlags **PROPERTY_USAGE_INTERNAL** = `8`

The property is excluded from the class reference.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_CHECKABLE:

PropertyUsageFlags **PROPERTY_USAGE_CHECKABLE** = `16`

The property can be checked in the [EditorInspector](class_editorinspector.md#class_EditorInspector).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_CHECKED:

PropertyUsageFlags **PROPERTY_USAGE_CHECKED** = `32`

The property is checked in the [EditorInspector](class_editorinspector.md#class_EditorInspector).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_GROUP:

PropertyUsageFlags **PROPERTY_USAGE_GROUP** = `64`

Used to group properties together in the editor. See [EditorInspector](class_editorinspector.md#class_EditorInspector).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_CATEGORY:

PropertyUsageFlags **PROPERTY_USAGE_CATEGORY** = `128`

Used to categorize properties together in the editor.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_SUBGROUP:

PropertyUsageFlags **PROPERTY_USAGE_SUBGROUP** = `256`

Used to group properties together in the editor in a subgroup (under a group). See [EditorInspector](class_editorinspector.md#class_EditorInspector).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_CLASS_IS_BITFIELD:

PropertyUsageFlags **PROPERTY_USAGE_CLASS_IS_BITFIELD** = `512`

The property is a bitfield, i.e. it contains multiple flags represented as bits.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NO_INSTANCE_STATE:

PropertyUsageFlags **PROPERTY_USAGE_NO_INSTANCE_STATE** = `1024`

The property does not save its state in [PackedScene](class_packedscene.md#class_PackedScene).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_RESTART_IF_CHANGED:

PropertyUsageFlags **PROPERTY_USAGE_RESTART_IF_CHANGED** = `2048`

Editing the property prompts the user for restarting the editor.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE:

PropertyUsageFlags **PROPERTY_USAGE_SCRIPT_VARIABLE** = `4096`

The property is a script variable. PROPERTY_USAGE_SCRIPT_VARIABLE can be used to distinguish between exported script variables from built-in variables (which don't have this usage flag). By default, PROPERTY_USAGE_SCRIPT_VARIABLE is **not** applied to variables that are created by overriding [Object._get_property_list()](class_object.md#class_Object_private_method__get_property_list) in a script.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_STORE_IF_NULL:

PropertyUsageFlags **PROPERTY_USAGE_STORE_IF_NULL** = `8192`

The property value of type [Object](class_object.md#class_Object) will be stored even if its value is `null`.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED:

PropertyUsageFlags **PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED** = `16384`

If this property is modified, all inspector fields will be refreshed.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE:

PropertyUsageFlags **PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE** = `32768`

**Deprecated:** This flag is not used by the engine.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_CLASS_IS_ENUM:

PropertyUsageFlags **PROPERTY_USAGE_CLASS_IS_ENUM** = `65536`

The property is a variable of enum type, i.e. it only takes named integer constants from its associated enumeration.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NIL_IS_VARIANT:

PropertyUsageFlags **PROPERTY_USAGE_NIL_IS_VARIANT** = `131072`

If property has `nil` as default value, its type will be [Variant](class_variant.md#class_Variant).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_ARRAY:

PropertyUsageFlags **PROPERTY_USAGE_ARRAY** = `262144`

The property is the element count of a property array, i.e. a list of groups of related properties. Properties defined with this usage also need a specific `class_name` field in the form of `label,prefix`. The field may also include additional comma-separated options:

- `page_size=N`: Overrides EditorSettings.interface/inspector/max_array_dictionary_items_per_page for this array.

- `add_button_text=text`: The text displayed by the "Add Element" button.

- `static`: The elements can't be re-arranged.

- `const`: New elements can't be added.

- `numbered`: An index will appear next to each element.

- `unfoldable`: The array can't be folded.

- `swap_method=method_name`: The method that will be called when two elements switch places. The method should take 2 [int](class_int.md#class_int) parameters, which will be indices of the elements being swapped.

Note that making a full-fledged property array requires boilerplate code involving [Object._get_property_list()](class_object.md#class_Object_private_method__get_property_list).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_ALWAYS_DUPLICATE:

PropertyUsageFlags **PROPERTY_USAGE_ALWAYS_DUPLICATE** = `524288`

When duplicating a resource with [Resource.duplicate()](class_resource.md#class_Resource_method_duplicate), and this flag is set on a property of that resource, the property should always be duplicated, regardless of the `subresources` bool parameter.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NEVER_DUPLICATE:

PropertyUsageFlags **PROPERTY_USAGE_NEVER_DUPLICATE** = `1048576`

When duplicating a resource with [Resource.duplicate()](class_resource.md#class_Resource_method_duplicate), and this flag is set on a property of that resource, the property should never be duplicated, regardless of the `subresources` bool parameter.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_HIGH_END_GFX:

PropertyUsageFlags **PROPERTY_USAGE_HIGH_END_GFX** = `2097152`

The property is only shown in the editor if modern renderers are supported (the Compatibility rendering method is excluded).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT:

PropertyUsageFlags **PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT** = `4194304`

The [NodePath](class_nodepath.md#class_NodePath) property will always be relative to the scene's root. Mostly useful for local resources.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT:

PropertyUsageFlags **PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT** = `8388608`

Use when a resource is created on the fly, i.e. the getter will always return a different instance. [ResourceSaver](class_resourcesaver.md#class_ResourceSaver) needs this information to properly save such resources.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_KEYING_INCREMENTS:

PropertyUsageFlags **PROPERTY_USAGE_KEYING_INCREMENTS** = `16777216`

Inserting an animation key frame of this property will automatically increment the value, allowing to easily keyframe multiple values in a row.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_DEFERRED_SET_RESOURCE:

PropertyUsageFlags **PROPERTY_USAGE_DEFERRED_SET_RESOURCE** = `33554432`

**Deprecated:** This flag is not used by the engine.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT:

PropertyUsageFlags **PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT** = `67108864`

When this property is a [Resource](class_resource.md#class_Resource) and base object is a [Node](class_node.md#class_Node), a resource instance will be automatically created whenever the node is created in the editor.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR_BASIC_SETTING:

PropertyUsageFlags **PROPERTY_USAGE_EDITOR_BASIC_SETTING** = `134217728`

The property is considered a basic setting and will appear even when advanced mode is disabled. Used for project settings.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_READ_ONLY:

PropertyUsageFlags **PROPERTY_USAGE_READ_ONLY** = `268435456`

The property is read-only in the [EditorInspector](class_editorinspector.md#class_EditorInspector).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_SECRET:

PropertyUsageFlags **PROPERTY_USAGE_SECRET** = `536870912`

An export preset property with this flag contains confidential information and is stored separately from the rest of the export preset configuration.

.. _class_@GlobalScope_constant_PROPERTY_USAGE_DEFAULT:

PropertyUsageFlags **PROPERTY_USAGE_DEFAULT** = `6`

Default usage (storage and editor).

.. _class_@GlobalScope_constant_PROPERTY_USAGE_NO_EDITOR:

PropertyUsageFlags **PROPERTY_USAGE_NO_EDITOR** = `2`

Default usage but without showing the property in the editor (storage).

---

.. _enum_@GlobalScope_MethodFlags:

flags **MethodFlags**: 🔗

.. _class_@GlobalScope_constant_METHOD_FLAG_NORMAL:

MethodFlags **METHOD_FLAG_NORMAL** = `1`

Flag for a normal method.

.. _class_@GlobalScope_constant_METHOD_FLAG_EDITOR:

MethodFlags **METHOD_FLAG_EDITOR** = `2`

Flag for an editor method.

.. _class_@GlobalScope_constant_METHOD_FLAG_CONST:

MethodFlags **METHOD_FLAG_CONST** = `4`

Flag for a constant method.

.. _class_@GlobalScope_constant_METHOD_FLAG_VIRTUAL:

MethodFlags **METHOD_FLAG_VIRTUAL** = `8`

Flag for a virtual method.

.. _class_@GlobalScope_constant_METHOD_FLAG_VARARG:

MethodFlags **METHOD_FLAG_VARARG** = `16`

Flag for a method with a variable number of arguments.

.. _class_@GlobalScope_constant_METHOD_FLAG_STATIC:

MethodFlags **METHOD_FLAG_STATIC** = `32`

Flag for a static method.

.. _class_@GlobalScope_constant_METHOD_FLAG_OBJECT_CORE:

MethodFlags **METHOD_FLAG_OBJECT_CORE** = `64`

Used internally. Allows to not dump core virtual methods (such as [Object._notification()](class_object.md#class_Object_private_method__notification)) to the JSON API.

.. _class_@GlobalScope_constant_METHOD_FLAG_VIRTUAL_REQUIRED:

MethodFlags **METHOD_FLAG_VIRTUAL_REQUIRED** = `128`

Flag for a virtual method that is required. In GDScript, this flag is set for abstract functions.

.. _class_@GlobalScope_constant_METHOD_FLAGS_DEFAULT:

MethodFlags **METHOD_FLAGS_DEFAULT** = `1`

Default method flags (normal).

---

.. _enum_@GlobalScope_Variant.Type:

enum **Variant.Type**: 🔗

.. _class_@GlobalScope_constant_TYPE_NIL:

Variant.Type **TYPE_NIL** = `0`

Variable is `null`.

.. _class_@GlobalScope_constant_TYPE_BOOL:

Variant.Type **TYPE_BOOL** = `1`

Variable is of type [bool](class_bool.md#class_bool).

.. _class_@GlobalScope_constant_TYPE_INT:

Variant.Type **TYPE_INT** = `2`

Variable is of type [int](class_int.md#class_int).

.. _class_@GlobalScope_constant_TYPE_FLOAT:

Variant.Type **TYPE_FLOAT** = `3`

Variable is of type [float](class_float.md#class_float).

.. _class_@GlobalScope_constant_TYPE_STRING:

Variant.Type **TYPE_STRING** = `4`

Variable is of type [String](class_string.md#class_String).

.. _class_@GlobalScope_constant_TYPE_VECTOR2:

Variant.Type **TYPE_VECTOR2** = `5`

Variable is of type [Vector2](class_vector2.md#class_Vector2).

.. _class_@GlobalScope_constant_TYPE_VECTOR2I:

Variant.Type **TYPE_VECTOR2I** = `6`

Variable is of type [Vector2i](class_vector2i.md#class_Vector2i).

.. _class_@GlobalScope_constant_TYPE_RECT2:

Variant.Type **TYPE_RECT2** = `7`

Variable is of type [Rect2](class_rect2.md#class_Rect2).

.. _class_@GlobalScope_constant_TYPE_RECT2I:

Variant.Type **TYPE_RECT2I** = `8`

Variable is of type [Rect2i](class_rect2i.md#class_Rect2i).

.. _class_@GlobalScope_constant_TYPE_VECTOR3:

Variant.Type **TYPE_VECTOR3** = `9`

Variable is of type [Vector3](class_vector3.md#class_Vector3).

.. _class_@GlobalScope_constant_TYPE_VECTOR3I:

Variant.Type **TYPE_VECTOR3I** = `10`

Variable is of type [Vector3i](class_vector3i.md#class_Vector3i).

.. _class_@GlobalScope_constant_TYPE_TRANSFORM2D:

Variant.Type **TYPE_TRANSFORM2D** = `11`

Variable is of type [Transform2D](class_transform2d.md#class_Transform2D).

.. _class_@GlobalScope_constant_TYPE_VECTOR4:

Variant.Type **TYPE_VECTOR4** = `12`

Variable is of type [Vector4](class_vector4.md#class_Vector4).

.. _class_@GlobalScope_constant_TYPE_VECTOR4I:

Variant.Type **TYPE_VECTOR4I** = `13`

Variable is of type [Vector4i](class_vector4i.md#class_Vector4i).

.. _class_@GlobalScope_constant_TYPE_PLANE:

Variant.Type **TYPE_PLANE** = `14`

Variable is of type [Plane](class_plane.md#class_Plane).

.. _class_@GlobalScope_constant_TYPE_QUATERNION:

Variant.Type **TYPE_QUATERNION** = `15`

Variable is of type [Quaternion](class_quaternion.md#class_Quaternion).

.. _class_@GlobalScope_constant_TYPE_AABB:

Variant.Type **TYPE_AABB** = `16`

Variable is of type [AABB](class_aabb.md#class_AABB).

.. _class_@GlobalScope_constant_TYPE_BASIS:

Variant.Type **TYPE_BASIS** = `17`

Variable is of type [Basis](class_basis.md#class_Basis).

.. _class_@GlobalScope_constant_TYPE_TRANSFORM3D:

Variant.Type **TYPE_TRANSFORM3D** = `18`

Variable is of type [Transform3D](class_transform3d.md#class_Transform3D).

.. _class_@GlobalScope_constant_TYPE_PROJECTION:

Variant.Type **TYPE_PROJECTION** = `19`

Variable is of type [Projection](class_projection.md#class_Projection).

.. _class_@GlobalScope_constant_TYPE_COLOR:

Variant.Type **TYPE_COLOR** = `20`

Variable is of type [Color](class_color.md#class_Color).

.. _class_@GlobalScope_constant_TYPE_STRING_NAME:

Variant.Type **TYPE_STRING_NAME** = `21`

Variable is of type [StringName](class_stringname.md#class_StringName).

.. _class_@GlobalScope_constant_TYPE_NODE_PATH:

Variant.Type **TYPE_NODE_PATH** = `22`

Variable is of type [NodePath](class_nodepath.md#class_NodePath).

.. _class_@GlobalScope_constant_TYPE_RID:

Variant.Type **TYPE_RID** = `23`

Variable is of type [RID](class_rid.md#class_RID).

.. _class_@GlobalScope_constant_TYPE_OBJECT:

Variant.Type **TYPE_OBJECT** = `24`

Variable is of type [Object](class_object.md#class_Object).

.. _class_@GlobalScope_constant_TYPE_CALLABLE:

Variant.Type **TYPE_CALLABLE** = `25`

Variable is of type [Callable](class_callable.md#class_Callable).

.. _class_@GlobalScope_constant_TYPE_SIGNAL:

Variant.Type **TYPE_SIGNAL** = `26`

Variable is of type [Signal](class_signal.md#class_Signal).

.. _class_@GlobalScope_constant_TYPE_DICTIONARY:

Variant.Type **TYPE_DICTIONARY** = `27`

Variable is of type [Dictionary](class_dictionary.md#class_Dictionary).

.. _class_@GlobalScope_constant_TYPE_ARRAY:

Variant.Type **TYPE_ARRAY** = `28`

Variable is of type [Array](class_array.md#class_Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_BYTE_ARRAY:

Variant.Type **TYPE_PACKED_BYTE_ARRAY** = `29`

Variable is of type [PackedByteArray](class_packedbytearray.md#class_PackedByteArray).

.. _class_@GlobalScope_constant_TYPE_PACKED_INT32_ARRAY:

Variant.Type **TYPE_PACKED_INT32_ARRAY** = `30`

Variable is of type [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_INT64_ARRAY:

Variant.Type **TYPE_PACKED_INT64_ARRAY** = `31`

Variable is of type [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_FLOAT32_ARRAY:

Variant.Type **TYPE_PACKED_FLOAT32_ARRAY** = `32`

Variable is of type [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_FLOAT64_ARRAY:

Variant.Type **TYPE_PACKED_FLOAT64_ARRAY** = `33`

Variable is of type [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_STRING_ARRAY:

Variant.Type **TYPE_PACKED_STRING_ARRAY** = `34`

Variable is of type [PackedStringArray](class_packedstringarray.md#class_PackedStringArray).

.. _class_@GlobalScope_constant_TYPE_PACKED_VECTOR2_ARRAY:

Variant.Type **TYPE_PACKED_VECTOR2_ARRAY** = `35`

Variable is of type [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_VECTOR3_ARRAY:

Variant.Type **TYPE_PACKED_VECTOR3_ARRAY** = `36`

Variable is of type [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array).

.. _class_@GlobalScope_constant_TYPE_PACKED_COLOR_ARRAY:

Variant.Type **TYPE_PACKED_COLOR_ARRAY** = `37`

Variable is of type [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray).

.. _class_@GlobalScope_constant_TYPE_PACKED_VECTOR4_ARRAY:

Variant.Type **TYPE_PACKED_VECTOR4_ARRAY** = `38`

Variable is of type [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array).

.. _class_@GlobalScope_constant_TYPE_MAX:

Variant.Type **TYPE_MAX** = `39`

Represents the size of the Variant.Type enum.

---

.. _enum_@GlobalScope_Variant.Operator:

enum **Variant.Operator**: 🔗

.. _class_@GlobalScope_constant_OP_EQUAL:

Variant.Operator **OP_EQUAL** = `0`

Equality operator (`==`).

.. _class_@GlobalScope_constant_OP_NOT_EQUAL:

Variant.Operator **OP_NOT_EQUAL** = `1`

Inequality operator (`!=`).

.. _class_@GlobalScope_constant_OP_LESS:

Variant.Operator **OP_LESS** = `2`

Less than operator (`<`).

.. _class_@GlobalScope_constant_OP_LESS_EQUAL:

Variant.Operator **OP_LESS_EQUAL** = `3`

Less than or equal operator (`<=`).

.. _class_@GlobalScope_constant_OP_GREATER:

Variant.Operator **OP_GREATER** = `4`

Greater than operator (`>`).

.. _class_@GlobalScope_constant_OP_GREATER_EQUAL:

Variant.Operator **OP_GREATER_EQUAL** = `5`

Greater than or equal operator (`>=`).

.. _class_@GlobalScope_constant_OP_ADD:

Variant.Operator **OP_ADD** = `6`

Addition operator (`+`).

.. _class_@GlobalScope_constant_OP_SUBTRACT:

Variant.Operator **OP_SUBTRACT** = `7`

Subtraction operator (`-`).

.. _class_@GlobalScope_constant_OP_MULTIPLY:

Variant.Operator **OP_MULTIPLY** = `8`

Multiplication operator (`*`).

.. _class_@GlobalScope_constant_OP_DIVIDE:

Variant.Operator **OP_DIVIDE** = `9`

Division operator (`/`).

.. _class_@GlobalScope_constant_OP_NEGATE:

Variant.Operator **OP_NEGATE** = `10`

Unary negation operator (`-`).

.. _class_@GlobalScope_constant_OP_POSITIVE:

Variant.Operator **OP_POSITIVE** = `11`

Unary plus operator (`+`).

.. _class_@GlobalScope_constant_OP_MODULE:

Variant.Operator **OP_MODULE** = `12`

Remainder/modulo operator (`%`).

.. _class_@GlobalScope_constant_OP_POWER:

Variant.Operator **OP_POWER** = `13`

Power operator (`**`).

.. _class_@GlobalScope_constant_OP_SHIFT_LEFT:

Variant.Operator **OP_SHIFT_LEFT** = `14`

Left shift operator (`<<`).

.. _class_@GlobalScope_constant_OP_SHIFT_RIGHT:

Variant.Operator **OP_SHIFT_RIGHT** = `15`

Right shift operator (`>>`).

.. _class_@GlobalScope_constant_OP_BIT_AND:

Variant.Operator **OP_BIT_AND** = `16`

Bitwise AND operator (`&`).

.. _class_@GlobalScope_constant_OP_BIT_OR:

Variant.Operator **OP_BIT_OR** = `17`

Bitwise OR operator (`|`).

.. _class_@GlobalScope_constant_OP_BIT_XOR:

Variant.Operator **OP_BIT_XOR** = `18`

Bitwise XOR operator (`^`).

.. _class_@GlobalScope_constant_OP_BIT_NEGATE:

Variant.Operator **OP_BIT_NEGATE** = `19`

Bitwise NOT operator (`~`).

.. _class_@GlobalScope_constant_OP_AND:

Variant.Operator **OP_AND** = `20`

Logical AND operator (`and` or `&&`).

.. _class_@GlobalScope_constant_OP_OR:

Variant.Operator **OP_OR** = `21`

Logical OR operator (`or` or `||`).

.. _class_@GlobalScope_constant_OP_XOR:

Variant.Operator **OP_XOR** = `22`

Logical XOR operator (not implemented in GDScript).

.. _class_@GlobalScope_constant_OP_NOT:

Variant.Operator **OP_NOT** = `23`

Logical NOT operator (`not` or `!`).

.. _class_@GlobalScope_constant_OP_IN:

Variant.Operator **OP_IN** = `24`

Logical IN operator (`in`).

.. _class_@GlobalScope_constant_OP_MAX:

Variant.Operator **OP_MAX** = `25`

Represents the size of the Variant.Operator enum.

---

### Property Descriptions

.. _class_@GlobalScope_property_AudioServer:

[AudioServer](class_audioserver.md#class_AudioServer) **AudioServer** 🔗

The [AudioServer](class_audioserver.md#class_AudioServer) singleton.

---

.. _class_@GlobalScope_property_CameraServer:

[CameraServer](class_cameraserver.md#class_CameraServer) **CameraServer** 🔗

The [CameraServer](class_cameraserver.md#class_CameraServer) singleton.

---

.. _class_@GlobalScope_property_ClassDB:

[ClassDB](class_classdb.md#class_ClassDB) **ClassDB** 🔗

The [ClassDB](class_classdb.md#class_ClassDB) singleton.

---

.. _class_@GlobalScope_property_DisplayServer:

[DisplayServer](class_displayserver.md#class_DisplayServer) **DisplayServer** 🔗

The [DisplayServer](class_displayserver.md#class_DisplayServer) singleton.

---

.. _class_@GlobalScope_property_EditorInterface:

[EditorInterface](class_editorinterface.md#class_EditorInterface) **EditorInterface** 🔗

The [EditorInterface](class_editorinterface.md#class_EditorInterface) singleton.

 **Note:** Only available in editor builds.

---

.. _class_@GlobalScope_property_Engine:

[Engine](class_engine.md#class_Engine) **Engine** 🔗

The [Engine](class_engine.md#class_Engine) singleton.

---

.. _class_@GlobalScope_property_EngineDebugger:

[EngineDebugger](class_enginedebugger.md#class_EngineDebugger) **EngineDebugger** 🔗

The [EngineDebugger](class_enginedebugger.md#class_EngineDebugger) singleton.

---

.. _class_@GlobalScope_property_GDExtensionManager:

[GDExtensionManager](class_gdextensionmanager.md#class_GDExtensionManager) **GDExtensionManager** 🔗

The [GDExtensionManager](class_gdextensionmanager.md#class_GDExtensionManager) singleton.

---

.. _class_@GlobalScope_property_Geometry2D:

[Geometry2D](class_geometry2d.md#class_Geometry2D) **Geometry2D** 🔗

The [Geometry2D](class_geometry2d.md#class_Geometry2D) singleton.

---

.. _class_@GlobalScope_property_Geometry3D:

[Geometry3D](class_geometry3d.md#class_Geometry3D) **Geometry3D** 🔗

The [Geometry3D](class_geometry3d.md#class_Geometry3D) singleton.

---

.. _class_@GlobalScope_property_IP:

[IP](class_ip.md#class_IP) **IP** 🔗

The [IP](class_ip.md#class_IP) singleton.

---

.. _class_@GlobalScope_property_Input:

[Input](class_input.md#class_Input) **Input** 🔗

The [Input](class_input.md#class_Input) singleton.

---

.. _class_@GlobalScope_property_InputMap:

[InputMap](class_inputmap.md#class_InputMap) **InputMap** 🔗

The [InputMap](class_inputmap.md#class_InputMap) singleton.

---

.. _class_@GlobalScope_property_JavaClassWrapper:

[JavaClassWrapper](class_javaclasswrapper.md#class_JavaClassWrapper) **JavaClassWrapper** 🔗

The [JavaClassWrapper](class_javaclasswrapper.md#class_JavaClassWrapper) singleton.

 **Note:** Only implemented on Android.

---

.. _class_@GlobalScope_property_JavaScriptBridge:

[JavaScriptBridge](class_javascriptbridge.md#class_JavaScriptBridge) **JavaScriptBridge** 🔗

The [JavaScriptBridge](class_javascriptbridge.md#class_JavaScriptBridge) singleton.

 **Note:** Only implemented on the Web platform.

---

.. _class_@GlobalScope_property_Marshalls:

[Marshalls](class_marshalls.md#class_Marshalls) **Marshalls** 🔗

The [Marshalls](class_marshalls.md#class_Marshalls) singleton.

---

.. _class_@GlobalScope_property_NativeMenu:

[NativeMenu](class_nativemenu.md#class_NativeMenu) **NativeMenu** 🔗

The [NativeMenu](class_nativemenu.md#class_NativeMenu) singleton.

 **Note:** Only implemented on macOS.

---

.. _class_@GlobalScope_property_NavigationMeshGenerator:

[NavigationMeshGenerator](class_navigationmeshgenerator.md#class_NavigationMeshGenerator) **NavigationMeshGenerator** 🔗

The [NavigationMeshGenerator](class_navigationmeshgenerator.md#class_NavigationMeshGenerator) singleton.

---

.. _class_@GlobalScope_property_NavigationServer2D:

[NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) **NavigationServer2D** 🔗

The [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) singleton.

---

.. _class_@GlobalScope_property_NavigationServer2DManager:

[NavigationServer2DManager](class_navigationserver2dmanager.md#class_NavigationServer2DManager) **NavigationServer2DManager** 🔗

The [NavigationServer2DManager](class_navigationserver2dmanager.md#class_NavigationServer2DManager) singleton.

---

.. _class_@GlobalScope_property_NavigationServer3D:

[NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D) **NavigationServer3D** 🔗

The [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D) singleton.

---

.. _class_@GlobalScope_property_NavigationServer3DManager:

[NavigationServer3DManager](class_navigationserver3dmanager.md#class_NavigationServer3DManager) **NavigationServer3DManager** 🔗

The [NavigationServer3DManager](class_navigationserver3dmanager.md#class_NavigationServer3DManager) singleton.

---

.. _class_@GlobalScope_property_OS:

[OS](class_os.md#class_OS) **OS** 🔗

The [OS](class_os.md#class_OS) singleton.

---

.. _class_@GlobalScope_property_Performance:

[Performance](class_performance.md#class_Performance) **Performance** 🔗

The [Performance](class_performance.md#class_Performance) singleton.

---

.. _class_@GlobalScope_property_PhysicsServer2D:

[PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) **PhysicsServer2D** 🔗

The [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) singleton.

---

.. _class_@GlobalScope_property_PhysicsServer2DManager:

[PhysicsServer2DManager](class_physicsserver2dmanager.md#class_PhysicsServer2DManager) **PhysicsServer2DManager** 🔗

The [PhysicsServer2DManager](class_physicsserver2dmanager.md#class_PhysicsServer2DManager) singleton.

---

.. _class_@GlobalScope_property_PhysicsServer3D:

[PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) **PhysicsServer3D** 🔗

The [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) singleton.

---

.. _class_@GlobalScope_property_PhysicsServer3DManager:

[PhysicsServer3DManager](class_physicsserver3dmanager.md#class_PhysicsServer3DManager) **PhysicsServer3DManager** 🔗

The [PhysicsServer3DManager](class_physicsserver3dmanager.md#class_PhysicsServer3DManager) singleton.

---

.. _class_@GlobalScope_property_ProjectSettings:

[ProjectSettings](class_projectsettings.md#class_ProjectSettings) **ProjectSettings** 🔗

The [ProjectSettings](class_projectsettings.md#class_ProjectSettings) singleton.

---

.. _class_@GlobalScope_property_RenderingServer:

[RenderingServer](class_renderingserver.md#class_RenderingServer) **RenderingServer** 🔗

The [RenderingServer](class_renderingserver.md#class_RenderingServer) singleton.

---

.. _class_@GlobalScope_property_ResourceLoader:

[ResourceLoader](class_resourceloader.md#class_ResourceLoader) **ResourceLoader** 🔗

The [ResourceLoader](class_resourceloader.md#class_ResourceLoader) singleton.

---

.. _class_@GlobalScope_property_ResourceSaver:

[ResourceSaver](class_resourcesaver.md#class_ResourceSaver) **ResourceSaver** 🔗

The [ResourceSaver](class_resourcesaver.md#class_ResourceSaver) singleton.

---

.. _class_@GlobalScope_property_ResourceUID:

[ResourceUID](class_resourceuid.md#class_ResourceUID) **ResourceUID** 🔗

The [ResourceUID](class_resourceuid.md#class_ResourceUID) singleton.

---

.. _class_@GlobalScope_property_TextServerManager:

[TextServerManager](class_textservermanager.md#class_TextServerManager) **TextServerManager** 🔗

The [TextServerManager](class_textservermanager.md#class_TextServerManager) singleton.

---

.. _class_@GlobalScope_property_ThemeDB:

[ThemeDB](class_themedb.md#class_ThemeDB) **ThemeDB** 🔗

The [ThemeDB](class_themedb.md#class_ThemeDB) singleton.

---

.. _class_@GlobalScope_property_Time:

[Time](class_time.md#class_Time) **Time** 🔗

The [Time](class_time.md#class_Time) singleton.

---

.. _class_@GlobalScope_property_TranslationServer:

[TranslationServer](class_translationserver.md#class_TranslationServer) **TranslationServer** 🔗

The [TranslationServer](class_translationserver.md#class_TranslationServer) singleton.

---

.. _class_@GlobalScope_property_WorkerThreadPool:

[WorkerThreadPool](class_workerthreadpool.md#class_WorkerThreadPool) **WorkerThreadPool** 🔗

The [WorkerThreadPool](class_workerthreadpool.md#class_WorkerThreadPool) singleton.

---

.. _class_@GlobalScope_property_XRServer:

[XRServer](class_xrserver.md#class_XRServer) **XRServer** 🔗

The [XRServer](class_xrserver.md#class_XRServer) singleton.

---

### Method Descriptions

.. _class_@GlobalScope_method_abs:

[Variant](class_variant.md#class_Variant) **abs** ( x: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the absolute value of a [Variant](class_variant.md#class_Variant) parameter `x` (i.e. non-negative value). Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    var a = abs(-1)
    # a is 1

    var b = abs(-1.2)
    # b is 1.2

    var c = abs(Vector2(-3.5, -4))
    # c is (3.5, 4)

    var d = abs(Vector2i(-5, -6))
    # d is (5, 6)

    var e = abs(Vector3(-7, 8.5, -3.8))
    # e is (7, 8.5, 3.8)

    var f = abs(Vector3i(-7, -8, -9))
    # f is (7, 8, 9)

 **Note:** For better type safety, use absf(), absi(), [Vector2.abs()](class_vector2.md#class_Vector2_method_abs), [Vector2i.abs()](class_vector2i.md#class_Vector2i_method_abs), [Vector3.abs()](class_vector3.md#class_Vector3_method_abs), [Vector3i.abs()](class_vector3i.md#class_Vector3i_method_abs), [Vector4.abs()](class_vector4.md#class_Vector4_method_abs), or [Vector4i.abs()](class_vector4i.md#class_Vector4i_method_abs).

---

.. _class_@GlobalScope_method_absf:

[float](class_float.md#class_float) **absf** ( x: [float](class_float.md#class_float) ) 🔗

Returns the absolute value of float parameter `x` (i.e. positive value).

::

    # a is 1.2
    var a = absf(-1.2)

---

.. _class_@GlobalScope_method_absi:

[int](class_int.md#class_int) **absi** ( x: [int](class_int.md#class_int) ) 🔗

Returns the absolute value of int parameter `x` (i.e. positive value).

::

    # a is 1
    var a = absi(-1)

---

.. _class_@GlobalScope_method_acos:

[float](class_float.md#class_float) **acos** ( x: [float](class_float.md#class_float) ) 🔗

Returns the arc cosine of `x` in radians. Use to get the angle of cosine `x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order to prevent acos() from returning @GDScript.NAN.

::

    # c is 0.523599 or 30 degrees if converted with rad_to_deg(c)
    var c = acos(0.866025)

---

.. _class_@GlobalScope_method_acosh:

[float](class_float.md#class_float) **acosh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic arc (also called inverse) cosine of `x`, returning a value in radians. Use it to get the angle from an angle's cosine in hyperbolic space if `x` is larger or equal to 1. For values of `x` lower than 1, it will return 0, in order to prevent acosh() from returning @GDScript.NAN.

::

    var a = acosh(2) # Returns 1.31695789692482
    cosh(a) # Returns 2

    var b = acosh(-1) # Returns 0

---

.. _class_@GlobalScope_method_angle_difference:

[float](class_float.md#class_float) **angle_difference** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) 🔗

Returns the difference between the two angles (in radians), in the range of `[-PI, +PI]`. When `from` and `to` are opposite, returns `-PI` if `from` is smaller than `to`, or `PI` otherwise.

---

.. _class_@GlobalScope_method_asin:

[float](class_float.md#class_float) **asin** ( x: [float](class_float.md#class_float) ) 🔗

Returns the arc sine of `x` in radians. Use to get the angle of sine `x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order to prevent asin() from returning @GDScript.NAN.

::

    # s is 0.523599 or 30 degrees if converted with rad_to_deg(s)
    var s = asin(0.5)

---

.. _class_@GlobalScope_method_asinh:

[float](class_float.md#class_float) **asinh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic arc (also called inverse) sine of `x`, returning a value in radians. Use it to get the angle from an angle's sine in hyperbolic space.

::

    var a = asinh(0.9) # Returns 0.8088669356527824
    sinh(a) # Returns 0.9

---

.. _class_@GlobalScope_method_atan:

[float](class_float.md#class_float) **atan** ( x: [float](class_float.md#class_float) ) 🔗

Returns the arc tangent of `x` in radians. Use it to get the angle from an angle's tangent in trigonometry.

The method cannot know in which quadrant the angle should fall. See atan2() if you have both `y` and `x`.

::

    var a = atan(0.5) # a is 0.463648

If `x` is between `-PI / 2` and `PI / 2` (inclusive), `atan(tan(x))` is equal to `x`.

---

.. _class_@GlobalScope_method_atan2:

[float](class_float.md#class_float) **atan2** ( y: [float](class_float.md#class_float), x: [float](class_float.md#class_float) ) 🔗

Returns the arc tangent of `y/x` in radians. Use to get the angle of tangent `y/x`. To compute the value, the method takes into account the sign of both arguments in order to determine the quadrant.

Important note: The Y coordinate comes first, by convention.

::

    var a = atan2(0, -1) # a is 3.141593

---

.. _class_@GlobalScope_method_atanh:

[float](class_float.md#class_float) **atanh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic arc (also called inverse) tangent of `x`, returning a value in radians. Use it to get the angle from an angle's tangent in hyperbolic space if `x` is between -1 and 1 (non-inclusive).

In mathematics, the inverse hyperbolic tangent is only defined for -1 < `x` < 1 in the real set, so values equal or lower to -1 for `x` return negative @GDScript.INF and values equal or higher than 1 return positive @GDScript.INF in order to prevent atanh() from returning @GDScript.NAN.

::

    var a = atanh(0.9) # Returns 1.47221948958322
    tanh(a) # Returns 0.9

    var b = atanh(-2) # Returns -inf
    tanh(b) # Returns -1

---

.. _class_@GlobalScope_method_bezier_derivative:

[float](class_float.md#class_float) **bezier_derivative** ( start: [float](class_float.md#class_float), control_1: [float](class_float.md#class_float), control_2: [float](class_float.md#class_float), end: [float](class_float.md#class_float), t: [float](class_float.md#class_float) ) 🔗

Returns the derivative at the given `t` on a one-dimensional Bézier curve defined by the given `control_1`, `control_2`, and `end` points.

---

.. _class_@GlobalScope_method_bezier_interpolate:

[float](class_float.md#class_float) **bezier_interpolate** ( start: [float](class_float.md#class_float), control_1: [float](class_float.md#class_float), control_2: [float](class_float.md#class_float), end: [float](class_float.md#class_float), t: [float](class_float.md#class_float) ) 🔗

Returns the point at the given `t` on a one-dimensional Bézier curve defined by the given `control_1`, `control_2`, and `end` points.

---

.. _class_@GlobalScope_method_bytes_to_var:

[Variant](class_variant.md#class_Variant) **bytes_to_var** ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) 🔗

Decodes a byte array back to a [Variant](class_variant.md#class_Variant) value, without decoding objects.

 **Note:** If you need object deserialization, see bytes_to_var_with_objects().

---

.. _class_@GlobalScope_method_bytes_to_var_with_objects:

[Variant](class_variant.md#class_Variant) **bytes_to_var_with_objects** ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) 🔗

Decodes a byte array back to a [Variant](class_variant.md#class_Variant) value. Decoding objects is allowed.

 **Warning:** Deserialized object can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats (remote code execution).

---

.. _class_@GlobalScope_method_ceil:

[Variant](class_variant.md#class_Variant) **ceil** ( x: [Variant](class_variant.md#class_Variant) ) 🔗

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`. Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    var i = ceil(1.45) # i is 2.0
    i = ceil(1.001)    # i is 2.0

See also floor(), round(), and snapped().

 **Note:** For better type safety, use ceilf(), ceili(), [Vector2.ceil()](class_vector2.md#class_Vector2_method_ceil), [Vector3.ceil()](class_vector3.md#class_Vector3_method_ceil), or [Vector4.ceil()](class_vector4.md#class_Vector4_method_ceil).

---

.. _class_@GlobalScope_method_ceilf:

[float](class_float.md#class_float) **ceilf** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`.

A type-safe version of ceil(), returning a [float](class_float.md#class_float).

---

.. _class_@GlobalScope_method_ceili:

[int](class_int.md#class_int) **ceili** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`.

A type-safe version of ceil(), returning an [int](class_int.md#class_int).

---

.. _class_@GlobalScope_method_clamp:

[Variant](class_variant.md#class_Variant) **clamp** ( value: [Variant](class_variant.md#class_Variant), min: [Variant](class_variant.md#class_Variant), max: [Variant](class_variant.md#class_Variant) ) 🔗

Clamps the `value`, returning a [Variant](class_variant.md#class_Variant) not less than `min` and not more than `max`. Any values that can be compared with the less than and greater than operators will work.

::

    var a = clamp(-10, -1, 5)
    # a is -1

    var b = clamp(8.1, 0.9, 5.5)
    # b is 5.5

 **Note:** For better type safety, use clampf(), clampi(), [Vector2.clamp()](class_vector2.md#class_Vector2_method_clamp), [Vector2i.clamp()](class_vector2i.md#class_Vector2i_method_clamp), [Vector3.clamp()](class_vector3.md#class_Vector3_method_clamp), [Vector3i.clamp()](class_vector3i.md#class_Vector3i_method_clamp), [Vector4.clamp()](class_vector4.md#class_Vector4_method_clamp), [Vector4i.clamp()](class_vector4i.md#class_Vector4i_method_clamp), or [Color.clamp()](class_color.md#class_Color_method_clamp) (not currently supported by this method).

 **Note:** When using this on vectors it will *not* perform component-wise clamping, and will pick `min` if `value < min` or `max` if `value > max`. To perform component-wise clamping use the methods listed above.

---

.. _class_@GlobalScope_method_clampf:

[float](class_float.md#class_float) **clampf** ( value: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) 🔗

Clamps the `value`, returning a [float](class_float.md#class_float) not less than `min` and not more than `max`.

::

    var speed = 42.1
    var a = clampf(speed, 1.0, 20.5) # a is 20.5

    speed = -10.0
    var b = clampf(speed, -1.0, 1.0) # b is -1.0

---

.. _class_@GlobalScope_method_clampi:

[int](class_int.md#class_int) **clampi** ( value: [int](class_int.md#class_int), min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) 🔗

Clamps the `value`, returning an [int](class_int.md#class_int) not less than `min` and not more than `max`.

::

    var speed = 42
    var a = clampi(speed, 1, 20) # a is 20

    speed = -10
    var b = clampi(speed, -1, 1) # b is -1

---

.. _class_@GlobalScope_method_cos:

[float](class_float.md#class_float) **cos** ( angle_rad: [float](class_float.md#class_float) ) 🔗

Returns the cosine of angle `angle_rad` in radians.

::

    cos(PI * 2)         # Returns 1.0
    cos(PI)             # Returns -1.0
    cos(deg_to_rad(90)) # Returns 0.0

---

.. _class_@GlobalScope_method_cosh:

[float](class_float.md#class_float) **cosh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic cosine of `x` in radians.

::

    print(cosh(1)) # Prints 1.543081

---

.. _class_@GlobalScope_method_cubic_interpolate:

[float](class_float.md#class_float) **cubic_interpolate** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) 🔗

Cubic interpolates between two values by the factor defined in `weight` with `pre` and `post` values.

---

.. _class_@GlobalScope_method_cubic_interpolate_angle:

[float](class_float.md#class_float) **cubic_interpolate_angle** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) 🔗

Cubic interpolates between two rotation values with shortest path by the factor defined in `weight` with `pre` and `post` values. See also lerp_angle().

---

.. _class_@GlobalScope_method_cubic_interpolate_angle_in_time:

[float](class_float.md#class_float) **cubic_interpolate_angle_in_time** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float), to_t: [float](class_float.md#class_float), pre_t: [float](class_float.md#class_float), post_t: [float](class_float.md#class_float) ) 🔗

Cubic interpolates between two rotation values with shortest path by the factor defined in `weight` with `pre` and `post` values. See also lerp_angle().

It can perform smoother interpolation than cubic_interpolate() by the time values.

---

.. _class_@GlobalScope_method_cubic_interpolate_in_time:

[float](class_float.md#class_float) **cubic_interpolate_in_time** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), pre: [float](class_float.md#class_float), post: [float](class_float.md#class_float), weight: [float](class_float.md#class_float), to_t: [float](class_float.md#class_float), pre_t: [float](class_float.md#class_float), post_t: [float](class_float.md#class_float) ) 🔗

Cubic interpolates between two values by the factor defined in `weight` with `pre` and `post` values.

It can perform smoother interpolation than cubic_interpolate() by the time values.

---

.. _class_@GlobalScope_method_db_to_linear:

[float](class_float.md#class_float) **db_to_linear** ( db: [float](class_float.md#class_float) ) 🔗

Converts from decibels to linear energy (audio).

---

.. _class_@GlobalScope_method_deg_to_rad:

[float](class_float.md#class_float) **deg_to_rad** ( deg: [float](class_float.md#class_float) ) 🔗

Converts an angle expressed in degrees to radians.

::

    var r = deg_to_rad(180) # r is 3.141593

---

.. _class_@GlobalScope_method_ease:

[float](class_float.md#class_float) **ease** ( x: [float](class_float.md#class_float), curve: [float](class_float.md#class_float) ) 🔗

Returns an "eased" value of `x` based on an easing function defined with `curve`. This easing function is based on an exponent. The `curve` can be any floating-point number, with specific values leading to the following behaviors:

.. code:: text

    - Lower than -1.0 (exclusive): Ease in-out
    - -1.0: Linear
    - Between -1.0 and 0.0 (exclusive): Ease out-in
    - 0.0: Constant
    - Between 0.0 to 1.0 (exclusive): Ease out
    - 1.0: Linear
    - Greater than 1.0 (exclusive): Ease in

 ease() curve values cheatsheet

See also smoothstep(). If you need to perform more advanced transitions, use [Tween.interpolate_value()](class_tween.md#class_Tween_method_interpolate_value).

---

.. _class_@GlobalScope_method_error_string:

[String](class_string.md#class_String) **error_string** ( error: [int](class_int.md#class_int) ) 🔗

Returns a human-readable name for the given Error code.

::

    print(OK)                              # Prints 0
    print(error_string(OK))                # Prints "OK"
    print(error_string(ERR_BUSY))          # Prints "Busy"
    print(error_string(ERR_OUT_OF_MEMORY)) # Prints "Out of memory"

---

.. _class_@GlobalScope_method_exp:

[float](class_float.md#class_float) **exp** ( x: [float](class_float.md#class_float) ) 🔗

The natural exponential function. It raises the mathematical constant *e* to the power of `x` and returns it.

 *e* has an approximate value of 2.71828, and can be obtained with `exp(1)`.

For exponents to other bases use the method pow().

::

    var a = exp(2) # Approximately 7.39

---

.. _class_@GlobalScope_method_floor:

[Variant](class_variant.md#class_Variant) **floor** ( x: [Variant](class_variant.md#class_Variant) ) 🔗

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`. Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    var a = floor(2.99) # a is 2.0
    a = floor(-2.99)    # a is -3.0

See also ceil(), round(), and snapped().

 **Note:** For better type safety, use floorf(), floori(), [Vector2.floor()](class_vector2.md#class_Vector2_method_floor), [Vector3.floor()](class_vector3.md#class_Vector3_method_floor), or [Vector4.floor()](class_vector4.md#class_Vector4_method_floor).

---

.. _class_@GlobalScope_method_floorf:

[float](class_float.md#class_float) **floorf** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`.

A type-safe version of floor(), returning a [float](class_float.md#class_float).

---

.. _class_@GlobalScope_method_floori:

[int](class_int.md#class_int) **floori** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`.

A type-safe version of floor(), returning an [int](class_int.md#class_int).

 **Note:** This function is *not* the same as `int(x)`, which rounds towards 0.

---

.. _class_@GlobalScope_method_fmod:

[float](class_float.md#class_float) **fmod** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) 🔗

Returns the floating-point remainder of `x` divided by `y`, keeping the sign of `x`.

::

    var remainder = fmod(7, 5.5) # remainder is 1.5

For the integer remainder operation, use the `%` operator.

---

.. _class_@GlobalScope_method_fposmod:

[float](class_float.md#class_float) **fposmod** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) 🔗

Returns the floating-point modulus of `x` divided by `y`, wrapping equally in positive and negative.

::

    print(" (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))")
    for i in 7:
        var x = i * 0.5 - 1.5
        print("%4.1f           %4.1f  | %4.1f" % [x, fmod(x, 1.5), fposmod(x, 1.5)])

Prints:

.. code:: text

     (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))
    -1.5           -0.0  |  0.0
    -1.0           -1.0  |  0.5
    -0.5           -0.5  |  1.0
     0.0            0.0  |  0.0
     0.5            0.5  |  0.5
     1.0            1.0  |  1.0
     1.5            0.0  |  0.0

---

.. _class_@GlobalScope_method_hash:

[int](class_int.md#class_int) **hash** ( variable: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the integer hash of the passed `variable`.

.. tabs::

```
```

    print(hash("a")) # Prints 177670

```
```

    GD.Print(GD.Hash("a")); // Prints 177670

---

.. _class_@GlobalScope_method_instance_from_id:

[Object](class_object.md#class_Object) **instance_from_id** ( instance_id: [int](class_int.md#class_int) ) 🔗

Returns the [Object](class_object.md#class_Object) that corresponds to `instance_id`. All Objects have a unique instance ID. See also [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

.. tabs::

```
```

    var drink = "water"

    func _ready():
        var id = get_instance_id()
        var instance = instance_from_id(id)
        print(instance.drink) # Prints "water"

```
```

    public partial class MyNode : Node
    {
        public string Drink { get; set; } = "water";

        public override void _Ready()
        {
            ulong id = GetInstanceId();
            var instance = (MyNode)InstanceFromId(Id);
            GD.Print(instance.Drink); // Prints "water"
        }
    }

---

.. _class_@GlobalScope_method_inverse_lerp:

[float](class_float.md#class_float) **inverse_lerp** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) 🔗

Returns an interpolation or extrapolation factor considering the range specified in `from` and `to`, and the interpolated value specified in `weight`. The returned value will be between `0.0` and `1.0` if `weight` is between `from` and `to` (inclusive). If `weight` is located outside this range, then an extrapolation factor will be returned (return value lower than `0.0` or greater than `1.0`). Use clamp() on the result of inverse_lerp() if this is not desired.

::

    # The interpolation ratio in the `lerp()` call below is 0.75.
    var middle = lerp(20, 30, 0.75)
    # middle is now 27.5.

    # Now, we pretend to have forgotten the original ratio and want to get it back.
    var ratio = inverse_lerp(20, 30, 27.5)
    # ratio is now 0.75.

See also lerp(), which performs the reverse of this operation, and remap() to map a continuous series of values to another.

---

.. _class_@GlobalScope_method_is_equal_approx:

[bool](class_bool.md#class_bool) **is_equal_approx** ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) 🔗

Returns `true` if `a` and `b` are approximately equal to each other.

Here, "approximately equal" means that `a` and `b` are within a small internal epsilon of each other, which scales with the magnitude of the numbers.

Infinity values of the same sign are considered equal.

---

.. _class_@GlobalScope_method_is_finite:

[bool](class_bool.md#class_bool) **is_finite** ( x: [float](class_float.md#class_float) ) 🔗

Returns whether `x` is a finite value, i.e. it is not @GDScript.NAN, positive infinity, or negative infinity. See also is_inf() and is_nan().

---

.. _class_@GlobalScope_method_is_inf:

[bool](class_bool.md#class_bool) **is_inf** ( x: [float](class_float.md#class_float) ) 🔗

Returns `true` if `x` is either positive infinity or negative infinity. See also is_finite() and is_nan().

---

.. _class_@GlobalScope_method_is_instance_id_valid:

[bool](class_bool.md#class_bool) **is_instance_id_valid** ( id: [int](class_int.md#class_int) ) 🔗

Returns `true` if the Object that corresponds to `id` is a valid object (e.g. has not been deleted from memory). All Objects have a unique instance ID.

---

.. _class_@GlobalScope_method_is_instance_valid:

[bool](class_bool.md#class_bool) **is_instance_valid** ( instance: [Variant](class_variant.md#class_Variant) ) 🔗

Returns `true` if `instance` is a valid Object (e.g. has not been deleted from memory).

---

.. _class_@GlobalScope_method_is_nan:

[bool](class_bool.md#class_bool) **is_nan** ( x: [float](class_float.md#class_float) ) 🔗

Returns `true` if `x` is a NaN ("Not a Number" or invalid) value. This method is needed as @GDScript.NAN is not equal to itself, which means `x == NAN` can't be used to check whether a value is a NaN.

---

.. _class_@GlobalScope_method_is_same:

[bool](class_bool.md#class_bool) **is_same** ( a: [Variant](class_variant.md#class_Variant), b: [Variant](class_variant.md#class_Variant) ) 🔗

Returns `true`, for value types, if `a` and `b` share the same value. Returns `true`, for reference types, if the references of `a` and `b` are the same.

::

    # Vector2 is a value type
    var vec2_a = Vector2(0, 0)
    var vec2_b = Vector2(0, 0)
    var vec2_c = Vector2(1, 1)
    is_same(vec2_a, vec2_a)  # true
    is_same(vec2_a, vec2_b)  # true
    is_same(vec2_a, vec2_c)  # false

    # Array is a reference type
    var arr_a = []
    var arr_b = []
    is_same(arr_a, arr_a)  # true
    is_same(arr_a, arr_b)  # false

These are [Variant](class_variant.md#class_Variant) value types: `null`, [bool](class_bool.md#class_bool), [int](class_int.md#class_int), [float](class_float.md#class_float), [String](class_string.md#class_String), [StringName](class_stringname.md#class_StringName), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i), [Rect2](class_rect2.md#class_Rect2), [Rect2i](class_rect2i.md#class_Rect2i), [Transform2D](class_transform2d.md#class_Transform2D), [Transform3D](class_transform3d.md#class_Transform3D), [Plane](class_plane.md#class_Plane), [Quaternion](class_quaternion.md#class_Quaternion), [AABB](class_aabb.md#class_AABB), [Basis](class_basis.md#class_Basis), [Projection](class_projection.md#class_Projection), [Color](class_color.md#class_Color), [NodePath](class_nodepath.md#class_NodePath), [RID](class_rid.md#class_RID), [Callable](class_callable.md#class_Callable) and [Signal](class_signal.md#class_Signal).

These are [Variant](class_variant.md#class_Variant) reference types: [Object](class_object.md#class_Object), [Dictionary](class_dictionary.md#class_Dictionary), [Array](class_array.md#class_Array), [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array), [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array), [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array), and [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray).

---

.. _class_@GlobalScope_method_is_zero_approx:

[bool](class_bool.md#class_bool) **is_zero_approx** ( x: [float](class_float.md#class_float) ) 🔗

Returns `true` if `x` is zero or almost zero. The comparison is done using a tolerance calculation with a small internal epsilon.

This function is faster than using is_equal_approx() with one value as zero.

---

.. _class_@GlobalScope_method_lerp:

[Variant](class_variant.md#class_Variant) **lerp** ( from: [Variant](class_variant.md#class_Variant), to: [Variant](class_variant.md#class_Variant), weight: [Variant](class_variant.md#class_Variant) ) 🔗

Linearly interpolates between two values by the factor defined in `weight`. To perform interpolation, `weight` should be between `0.0` and `1.0` (inclusive). However, values outside this range are allowed and can be used to perform *extrapolation*. If this is not desired, use clampf() to limit `weight`.

Both `from` and `to` must be the same type. Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector3](class_vector3.md#class_Vector3), [Vector4](class_vector4.md#class_Vector4), [Color](class_color.md#class_Color), [Quaternion](class_quaternion.md#class_Quaternion), [Basis](class_basis.md#class_Basis), [Transform2D](class_transform2d.md#class_Transform2D), [Transform3D](class_transform3d.md#class_Transform3D).

::

    lerp(0, 4, 0.75) # Returns 3.0

See also inverse_lerp() which performs the reverse of this operation. To perform eased interpolation with lerp(), combine it with ease() or smoothstep(). See also remap() to map a continuous series of values to another.

 **Note:** For better type safety, use lerpf(), [Vector2.lerp()](class_vector2.md#class_Vector2_method_lerp), [Vector3.lerp()](class_vector3.md#class_Vector3_method_lerp), [Vector4.lerp()](class_vector4.md#class_Vector4_method_lerp), [Color.lerp()](class_color.md#class_Color_method_lerp), [Quaternion.slerp()](class_quaternion.md#class_Quaternion_method_slerp), [Basis.slerp()](class_basis.md#class_Basis_method_slerp), [Transform2D.interpolate_with()](class_transform2d.md#class_Transform2D_method_interpolate_with), or [Transform3D.interpolate_with()](class_transform3d.md#class_Transform3D_method_interpolate_with).

---

.. _class_@GlobalScope_method_lerp_angle:

[float](class_float.md#class_float) **lerp_angle** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) 🔗

Linearly interpolates between two angles (in radians) by a `weight` value between 0.0 and 1.0.

Similar to lerp(), but interpolates correctly when the angles wrap around @GDScript.TAU. To perform eased interpolation with lerp_angle(), combine it with ease() or smoothstep().

::

    extends Sprite
    var elapsed = 0.0
    func _process(delta):
        var min_angle = deg_to_rad(0.0)
        var max_angle = deg_to_rad(90.0)
        rotation = lerp_angle(min_angle, max_angle, elapsed)
        elapsed += delta

 **Note:** This function lerps through the shortest path between `from` and `to`. However, when these two angles are approximately `PI + k * TAU` apart for any integer `k`, it's not obvious which way they lerp due to floating-point precision errors. For example, `lerp_angle(0, PI, weight)` lerps counter-clockwise, while `lerp_angle(0, PI + 5 * TAU, weight)` lerps clockwise.

---

.. _class_@GlobalScope_method_lerpf:

[float](class_float.md#class_float) **lerpf** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), weight: [float](class_float.md#class_float) ) 🔗

Linearly interpolates between two values by the factor defined in `weight`. To perform interpolation, `weight` should be between `0.0` and `1.0` (inclusive). However, values outside this range are allowed and can be used to perform *extrapolation*. If this is not desired, use clampf() on the result of this function.

::

    lerpf(0, 4, 0.75) # Returns 3.0

See also inverse_lerp() which performs the reverse of this operation. To perform eased interpolation with lerp(), combine it with ease() or smoothstep().

---

.. _class_@GlobalScope_method_linear_to_db:

[float](class_float.md#class_float) **linear_to_db** ( lin: [float](class_float.md#class_float) ) 🔗

Converts from linear energy to decibels (audio). Since volume is not normally linear, this can be used to implement volume sliders that behave as expected.

 **Example:** Change the Master bus's volume through a [Slider](class_slider.md#class_Slider) node, which ranges from `0.0` to `1.0`:

::

    AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), linear_to_db($Slider.value))

---

.. _class_@GlobalScope_method_log:

[float](class_float.md#class_float) **log** ( x: [float](class_float.md#class_float) ) 🔗

Returns the natural logarithm of `x` (base [i]e[/i], with *e* being approximately 2.71828). This is the amount of time needed to reach a certain level of continuous growth.

 **Note:** This is not the same as the "log" function on most calculators, which uses a base 10 logarithm. To use base 10 logarithm, use `log(x) / log(10)`.

::

    log(10) # Returns 2.302585

 **Note:** The logarithm of `0` returns `-inf`, while negative values return `-nan`.

---

.. _class_@GlobalScope_method_max:

[Variant](class_variant.md#class_Variant) **max** ( ... ) *vararg* 🔗

Returns the maximum of the given numeric values. This function can take any number of arguments.

::

    max(1, 7, 3, -6, 5) # Returns 7

 **Note:** When using this on vectors it will *not* perform component-wise maximum, and will pick the largest value when compared using `x < y`. To perform component-wise maximum, use [Vector2.max()](class_vector2.md#class_Vector2_method_max), [Vector2i.max()](class_vector2i.md#class_Vector2i_method_max), [Vector3.max()](class_vector3.md#class_Vector3_method_max), [Vector3i.max()](class_vector3i.md#class_Vector3i_method_max), [Vector4.max()](class_vector4.md#class_Vector4_method_max), and [Vector4i.max()](class_vector4i.md#class_Vector4i_method_max).

---

.. _class_@GlobalScope_method_maxf:

[float](class_float.md#class_float) **maxf** ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) 🔗

Returns the maximum of two [float](class_float.md#class_float) values.

::

    maxf(3.6, 24)   # Returns 24.0
    maxf(-3.99, -4) # Returns -3.99

---

.. _class_@GlobalScope_method_maxi:

[int](class_int.md#class_int) **maxi** ( a: [int](class_int.md#class_int), b: [int](class_int.md#class_int) ) 🔗

Returns the maximum of two [int](class_int.md#class_int) values.

::

    maxi(1, 2)   # Returns 2
    maxi(-3, -4) # Returns -3

---

.. _class_@GlobalScope_method_min:

[Variant](class_variant.md#class_Variant) **min** ( ... ) *vararg* 🔗

Returns the minimum of the given numeric values. This function can take any number of arguments.

::

    min(1, 7, 3, -6, 5) # Returns -6

 **Note:** When using this on vectors it will *not* perform component-wise minimum, and will pick the smallest value when compared using `x < y`. To perform component-wise minimum, use [Vector2.min()](class_vector2.md#class_Vector2_method_min), [Vector2i.min()](class_vector2i.md#class_Vector2i_method_min), [Vector3.min()](class_vector3.md#class_Vector3_method_min), [Vector3i.min()](class_vector3i.md#class_Vector3i_method_min), [Vector4.min()](class_vector4.md#class_Vector4_method_min), and [Vector4i.min()](class_vector4i.md#class_Vector4i_method_min).

---

.. _class_@GlobalScope_method_minf:

[float](class_float.md#class_float) **minf** ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float) ) 🔗

Returns the minimum of two [float](class_float.md#class_float) values.

::

    minf(3.6, 24)   # Returns 3.6
    minf(-3.99, -4) # Returns -4.0

---

.. _class_@GlobalScope_method_mini:

[int](class_int.md#class_int) **mini** ( a: [int](class_int.md#class_int), b: [int](class_int.md#class_int) ) 🔗

Returns the minimum of two [int](class_int.md#class_int) values.

::

    mini(1, 2)   # Returns 1
    mini(-3, -4) # Returns -4

---

.. _class_@GlobalScope_method_move_toward:

[float](class_float.md#class_float) **move_toward** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), delta: [float](class_float.md#class_float) ) 🔗

Moves `from` toward `to` by the `delta` amount. Will not go past `to`.

Use a negative `delta` value to move away.

::

    move_toward(5, 10, 4)    # Returns 9
    move_toward(10, 5, 4)    # Returns 6
    move_toward(5, 10, 9)    # Returns 10
    move_toward(10, 5, -1.5) # Returns 11.5

---

.. _class_@GlobalScope_method_nearest_po2:

[int](class_int.md#class_int) **nearest_po2** ( value: [int](class_int.md#class_int) ) 🔗

Returns the smallest integer power of 2 that is greater than or equal to `value`.

::

    nearest_po2(3) # Returns 4
    nearest_po2(4) # Returns 4
    nearest_po2(5) # Returns 8

    nearest_po2(0)  # Returns 0 (this may not be expected)
    nearest_po2(-1) # Returns 0 (this may not be expected)

 **Warning:** Due to its implementation, this method returns `0` rather than `1` for values less than or equal to `0`, with an exception for `value` being the smallest negative 64-bit integer (`-9223372036854775808`) in which case the `value` is returned unchanged.

---

.. _class_@GlobalScope_method_pingpong:

[float](class_float.md#class_float) **pingpong** ( value: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) 🔗

Wraps `value` between `0` and the `length`. If the limit is reached, the next value the function returns is decreased to the `0` side or increased to the `length` side (like a triangle wave). If `length` is less than zero, it becomes positive.

::

    pingpong(-3.0, 3.0) # Returns 3.0
    pingpong(-2.0, 3.0) # Returns 2.0
    pingpong(-1.0, 3.0) # Returns 1.0
    pingpong(0.0, 3.0)  # Returns 0.0
    pingpong(1.0, 3.0)  # Returns 1.0
    pingpong(2.0, 3.0)  # Returns 2.0
    pingpong(3.0, 3.0)  # Returns 3.0
    pingpong(4.0, 3.0)  # Returns 2.0
    pingpong(5.0, 3.0)  # Returns 1.0
    pingpong(6.0, 3.0)  # Returns 0.0

---

.. _class_@GlobalScope_method_posmod:

[int](class_int.md#class_int) **posmod** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) 🔗

Returns the integer modulus of `x` divided by `y` that wraps equally in positive and negative.

::

    print("#(i)  (i % 3)   (posmod(i, 3))")
    for i in range(-3, 4):
        print("%2d       %2d  | %2d" % [i, i % 3, posmod(i, 3)])

Prints:

.. code:: text

    (i)  (i % 3)   (posmod(i, 3))
    -3        0  |  0
    -2       -2  |  1
    -1       -1  |  2
     0        0  |  0
     1        1  |  1
     2        2  |  2
     3        0  |  0

---

.. _class_@GlobalScope_method_pow:

[float](class_float.md#class_float) **pow** ( base: [float](class_float.md#class_float), exp: [float](class_float.md#class_float) ) 🔗

Returns the result of `base` raised to the power of `exp`.

In GDScript, this is the equivalent of the `**` operator.

::

    pow(2, 5)   # Returns 32.0
    pow(4, 1.5) # Returns 8.0

---

.. _class_@GlobalScope_method_print:

void **print** ( ... ) *vararg* 🔗

Converts one or more arguments of any type to string in the best way possible and prints them to the console.

.. tabs::

```
```

    var a = [1, 2, 3]
    print("a", "b", a) # Prints "ab[1, 2, 3]"

```
```

    Godot.Collections.Array a = [1, 2, 3];
    GD.Print("a", "b", a); // Prints "ab[1, 2, 3]"

 **Note:** Consider using push_error() and push_warning() to print error and warning messages instead of print() or print_rich(). This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed. See also [Engine.print_to_stdout](class_engine.md#class_Engine_property_print_to_stdout) and ProjectSettings.application/run/disable_stdout.

---

.. _class_@GlobalScope_method_print_rich:

void **print_rich** ( ... ) *vararg* 🔗

Converts one or more arguments of any type to string in the best way possible and prints them to the console.

The following BBCode tags are supported: `b`, `i`, `u`, `s`, `indent`, `code`, `url`, `center`, `right`, `color`, `bgcolor`, `fgcolor`.

URL tags only support URLs wrapped by a URL tag, not URLs with a different title.

When printing to standard output, the supported subset of BBCode is converted to ANSI escape codes for the terminal emulator to display. Support for ANSI escape codes varies across terminal emulators, especially for italic and strikethrough. In standard output, `code` is represented with faint text but without any font change. Unsupported tags are left as-is in standard output.

.. tabs::

```
```

    print_rich("[color=green][b]Hello world![/b][/color]") # Prints "Hello world!", in green with a bold font.

```
```

    GD.PrintRich("[color=green][b]Hello world![/b][/color]"); // Prints "Hello world!", in green with a bold font.

 **Note:** Consider using push_error() and push_warning() to print error and warning messages instead of print() or print_rich(). This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed.

 **Note:** Output displayed in the editor supports clickable `[url=address]text[/url]` tags. The `[url]` tag's `address` value is handled by [OS.shell_open()](class_os.md#class_OS_method_shell_open) when clicked.

---

.. _class_@GlobalScope_method_print_verbose:

void **print_verbose** ( ... ) *vararg* 🔗

If verbose mode is enabled ([OS.is_stdout_verbose()](class_os.md#class_OS_method_is_stdout_verbose) returning `true`), converts one or more arguments of any type to string in the best way possible and prints them to the console.

---

.. _class_@GlobalScope_method_printerr:

void **printerr** ( ... ) *vararg* 🔗

Prints one or more arguments to strings in the best way possible to standard error line.

.. tabs::

```
```

    printerr("prints to stderr")

```
```

    GD.PrintErr("prints to stderr");

---

.. _class_@GlobalScope_method_printraw:

void **printraw** ( ... ) *vararg* 🔗

Prints one or more arguments to strings in the best way possible to the OS terminal. Unlike print(), no newline is automatically added at the end.

 **Note:** The OS terminal is *not* the same as the editor's Output dock. The output sent to the OS terminal can be seen when running Godot from a terminal. On Windows, this requires using the `console.exe` executable.

.. tabs::

```
```

    # Prints "ABC" to terminal.
    printraw("A")
    printraw("B")
    printraw("C")

```
```

    // Prints "ABC" to terminal.
    GD.PrintRaw("A");
    GD.PrintRaw("B");
    GD.PrintRaw("C");

---

.. _class_@GlobalScope_method_prints:

void **prints** ( ... ) *vararg* 🔗

Prints one or more arguments to the console with a space between each argument.

.. tabs::

```
```

    prints("A", "B", "C") # Prints "A B C"

```
```

    GD.PrintS("A", "B", "C"); // Prints "A B C"

---

.. _class_@GlobalScope_method_printt:

void **printt** ( ... ) *vararg* 🔗

Prints one or more arguments to the console with a tab between each argument.

.. tabs::

```
```

    printt("A", "B", "C") # Prints "A       B       C"

```
```

    GD.PrintT("A", "B", "C"); // Prints "A       B       C"

---

.. _class_@GlobalScope_method_push_error:

void **push_error** ( ... ) *vararg* 🔗

Pushes an error message to Godot's built-in debugger and to the OS terminal.

.. tabs::

```
```

    push_error("test error") # Prints "test error" to debugger and terminal as an error.

```
```

    GD.PushError("test error"); // Prints "test error" to debugger and terminal as an error.

 **Note:** This function does not pause project execution. To print an error message and pause project execution in debug builds, use `assert(false, "test error")` instead.

---

.. _class_@GlobalScope_method_push_warning:

void **push_warning** ( ... ) *vararg* 🔗

Pushes a warning message to Godot's built-in debugger and to the OS terminal.

.. tabs::

```
```

    push_warning("test warning") # Prints "test warning" to debugger and terminal as a warning.

```
```

    GD.PushWarning("test warning"); // Prints "test warning" to debugger and terminal as a warning.

---

.. _class_@GlobalScope_method_rad_to_deg:

[float](class_float.md#class_float) **rad_to_deg** ( rad: [float](class_float.md#class_float) ) 🔗

Converts an angle expressed in radians to degrees.

::

    rad_to_deg(0.523599) # Returns 30
    rad_to_deg(PI)       # Returns 180
    rad_to_deg(PI * 2)   # Returns 360

---

.. _class_@GlobalScope_method_rand_from_seed:

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **rand_from_seed** ( seed: [int](class_int.md#class_int) ) 🔗

Given a `seed`, returns a [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) of size `2`, where its first element is the randomized [int](class_int.md#class_int) value, and the second element is the same as `seed`. Passing the same `seed` consistently returns the same array.

 **Note:** "Seed" here refers to the internal state of the pseudo random number generator, currently implemented as a 64 bit integer.

::

    var a = rand_from_seed(4)

    print(a[0]) # Prints 2879024997
    print(a[1]) # Prints 4

---

.. _class_@GlobalScope_method_randf:

[float](class_float.md#class_float) **randf** ( ) 🔗

Returns a random floating-point value between `0.0` and `1.0` (inclusive).

.. tabs::

```
```

    randf() # Returns e.g. 0.375671

```
```

    GD.Randf(); // Returns e.g. 0.375671

---

.. _class_@GlobalScope_method_randf_range:

[float](class_float.md#class_float) **randf_range** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) 🔗

Returns a random floating-point value between `from` and `to` (inclusive).

.. tabs::

```
```

    randf_range(0, 20.5) # Returns e.g. 7.45315
    randf_range(-10, 10) # Returns e.g. -3.844535

```
```

    GD.RandRange(0.0, 20.5);   // Returns e.g. 7.45315
    GD.RandRange(-10.0, 10.0); // Returns e.g. -3.844535

---

.. _class_@GlobalScope_method_randfn:

[float](class_float.md#class_float) **randfn** ( mean: [float](class_float.md#class_float), deviation: [float](class_float.md#class_float) ) 🔗

Returns a normally-distributed, pseudo-random floating-point value from the specified `mean` and a standard `deviation`. This is also known as a Gaussian distribution.

 **Note:** This method uses the Box-Muller transform algorithm.

---

.. _class_@GlobalScope_method_randi:

[int](class_int.md#class_int) **randi** ( ) 🔗

Returns a random unsigned 32-bit integer. Use remainder to obtain a random value in the interval `[0, N - 1]` (where N is smaller than 2^32).

.. tabs::

```
```

    randi()           # Returns random integer between 0 and 2^32 - 1
    randi() % 20      # Returns random integer between 0 and 19
    randi() % 100     # Returns random integer between 0 and 99
    randi() % 100 + 1 # Returns random integer between 1 and 100

```
```

    GD.Randi();           // Returns random integer between 0 and 2^32 - 1
    GD.Randi() % 20;      // Returns random integer between 0 and 19
    GD.Randi() % 100;     // Returns random integer between 0 and 99
    GD.Randi() % 100 + 1; // Returns random integer between 1 and 100

---

.. _class_@GlobalScope_method_randi_range:

[int](class_int.md#class_int) **randi_range** ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) 🔗

Returns a random signed 32-bit integer between `from` and `to` (inclusive). If `to` is lesser than `from`, they are swapped.

.. tabs::

```
```

    randi_range(0, 1)      # Returns either 0 or 1
    randi_range(-10, 1000) # Returns random integer between -10 and 1000

```
```

    GD.RandRange(0, 1);      // Returns either 0 or 1
    GD.RandRange(-10, 1000); // Returns random integer between -10 and 1000

---

.. _class_@GlobalScope_method_randomize:

void **randomize** ( ) 🔗

Randomizes the seed (or the internal state) of the random number generator. The current implementation uses a number based on the device's time.

 **Note:** This function is called automatically when the project is run. If you need to fix the seed to have consistent, reproducible results, use seed() to initialize the random number generator.

---

.. _class_@GlobalScope_method_remap:

[float](class_float.md#class_float) **remap** ( value: [float](class_float.md#class_float), istart: [float](class_float.md#class_float), istop: [float](class_float.md#class_float), ostart: [float](class_float.md#class_float), ostop: [float](class_float.md#class_float) ) 🔗

Maps a `value` from range `[istart, istop]` to `[ostart, ostop]`. See also lerp() and inverse_lerp(). If `value` is outside `[istart, istop]`, then the resulting value will also be outside `[ostart, ostop]`. If this is not desired, use clamp() on the result of this function.

::

    remap(75, 0, 100, -1, 1) # Returns 0.5

For complex use cases where multiple ranges are needed, consider using [Curve](class_curve.md#class_Curve) or [Gradient](class_gradient.md#class_Gradient) instead.

 **Note:** If `istart == istop`, the return value is undefined (most likely NaN, INF, or -INF).

---

.. _class_@GlobalScope_method_rid_allocate_id:

[int](class_int.md#class_int) **rid_allocate_id** ( ) 🔗

Allocates a unique ID which can be used by the implementation to construct an RID. This is used mainly from native extensions to implement servers.

---

.. _class_@GlobalScope_method_rid_from_int64:

[RID](class_rid.md#class_RID) **rid_from_int64** ( base: [int](class_int.md#class_int) ) 🔗

Creates an RID from a `base`. This is used mainly from native extensions to build servers.

---

.. _class_@GlobalScope_method_rotate_toward:

[float](class_float.md#class_float) **rotate_toward** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), delta: [float](class_float.md#class_float) ) 🔗

Rotates `from` toward `to` by the `delta` amount. Will not go past `to`.

Similar to move_toward(), but interpolates correctly when the angles wrap around @GDScript.TAU.

If `delta` is negative, this function will rotate away from `to`, toward the opposite angle, and will not go past the opposite angle.

---

.. _class_@GlobalScope_method_round:

[Variant](class_variant.md#class_Variant) **round** ( x: [Variant](class_variant.md#class_Variant) ) 🔗

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0. Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    round(2.4) # Returns 2
    round(2.5) # Returns 3
    round(2.6) # Returns 3

See also floor(), ceil(), and snapped().

 **Note:** For better type safety, use roundf(), roundi(), [Vector2.round()](class_vector2.md#class_Vector2_method_round), [Vector3.round()](class_vector3.md#class_Vector3_method_round), or [Vector4.round()](class_vector4.md#class_Vector4_method_round).

---

.. _class_@GlobalScope_method_roundf:

[float](class_float.md#class_float) **roundf** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0.

A type-safe version of round(), returning a [float](class_float.md#class_float).

---

.. _class_@GlobalScope_method_roundi:

[int](class_int.md#class_int) **roundi** ( x: [float](class_float.md#class_float) ) 🔗

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0.

A type-safe version of round(), returning an [int](class_int.md#class_int).

---

.. _class_@GlobalScope_method_seed:

void **seed** ( base: [int](class_int.md#class_int) ) 🔗

Sets the seed for the random number generator to `base`. Setting the seed manually can ensure consistent, repeatable results for most random functions.

.. tabs::

```
```

    var my_seed = "Godot Rocks".hash()
    seed(my_seed)
    var a = randf() + randi()
    seed(my_seed)
    var b = randf() + randi()
    # a and b are now identical

```
```

    ulong mySeed = (ulong)GD.Hash("Godot Rocks");
    GD.Seed(mySeed);
    var a = GD.Randf() + GD.Randi();
    GD.Seed(mySeed);
    var b = GD.Randf() + GD.Randi();
    // a and b are now identical

---

.. _class_@GlobalScope_method_sign:

[Variant](class_variant.md#class_Variant) **sign** ( x: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the same type of [Variant](class_variant.md#class_Variant) as `x`, with `-1` for negative values, `1` for positive values, and `0` for zeros. For `nan` values it returns 0.

Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    sign(-6.0) # Returns -1
    sign(0.0)  # Returns 0
    sign(6.0)  # Returns 1
    sign(NAN)  # Returns 0

    sign(Vector3(-6.0, 0.0, 6.0)) # Returns (-1, 0, 1)

 **Note:** For better type safety, use signf(), signi(), [Vector2.sign()](class_vector2.md#class_Vector2_method_sign), [Vector2i.sign()](class_vector2i.md#class_Vector2i_method_sign), [Vector3.sign()](class_vector3.md#class_Vector3_method_sign), [Vector3i.sign()](class_vector3i.md#class_Vector3i_method_sign), [Vector4.sign()](class_vector4.md#class_Vector4_method_sign), or [Vector4i.sign()](class_vector4i.md#class_Vector4i_method_sign).

---

.. _class_@GlobalScope_method_signf:

[float](class_float.md#class_float) **signf** ( x: [float](class_float.md#class_float) ) 🔗

Returns `-1.0` if `x` is negative, `1.0` if `x` is positive, and `0.0` if `x` is zero. For `nan` values of `x` it returns 0.0.

::

    signf(-6.5) # Returns -1.0
    signf(0.0)  # Returns 0.0
    signf(6.5)  # Returns 1.0
    signf(NAN)  # Returns 0.0

---

.. _class_@GlobalScope_method_signi:

[int](class_int.md#class_int) **signi** ( x: [int](class_int.md#class_int) ) 🔗

Returns `-1` if `x` is negative, `1` if `x` is positive, and `0` if `x` is zero.

::

    signi(-6) # Returns -1
    signi(0)  # Returns 0
    signi(6)  # Returns 1

---

.. _class_@GlobalScope_method_sin:

[float](class_float.md#class_float) **sin** ( angle_rad: [float](class_float.md#class_float) ) 🔗

Returns the sine of angle `angle_rad` in radians.

::

    sin(0.523599)       # Returns 0.5
    sin(deg_to_rad(90)) # Returns 1.0

---

.. _class_@GlobalScope_method_sinh:

[float](class_float.md#class_float) **sinh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic sine of `x`.

::

    var a = log(2.0) # Returns 0.693147
    sinh(a) # Returns 0.75

---

.. _class_@GlobalScope_method_smoothstep:

[float](class_float.md#class_float) **smoothstep** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float), x: [float](class_float.md#class_float) ) 🔗

Returns a smooth cubic Hermite interpolation between `0` and `1`.

For positive ranges (when `from <= to`) the return value is `0` when `x <= from`, and `1` when `x >= to`. If `x` lies between `from` and `to`, the return value follows an S-shaped curve that smoothly transitions from `0` to `1`.

For negative ranges (when `from > to`) the function is mirrored and returns `1` when `x <= to` and `0` when `x >= from`.

This S-shaped curve is the cubic Hermite interpolator, given by `f(y) = 3*y^2 - 2*y^3` where `y = (x-from) / (to-from)`.

::

    smoothstep(0, 2, -5.0) # Returns 0.0
    smoothstep(0, 2, 0.5) # Returns 0.15625
    smoothstep(0, 2, 1.0) # Returns 0.5
    smoothstep(0, 2, 2.0) # Returns 1.0

Compared to ease() with a curve value of `-1.6521`, smoothstep() returns the smoothest possible curve with no sudden changes in the derivative. If you need to perform more advanced transitions, use [Tween](class_tween.md#class_Tween) or [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer).

 Comparison between smoothstep() and ease(x, -1.6521) return values

 Smoothstep() return values with positive, zero, and negative ranges

---

.. _class_@GlobalScope_method_snapped:

[Variant](class_variant.md#class_Variant) **snapped** ( x: [Variant](class_variant.md#class_Variant), step: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the multiple of `step` that is the closest to `x`. This can also be used to round a floating-point number to an arbitrary number of decimals.

The returned value is the same type of [Variant](class_variant.md#class_Variant) as `step`. Supported types: [int](class_int.md#class_int), [float](class_float.md#class_float), [Vector2](class_vector2.md#class_Vector2), [Vector2i](class_vector2i.md#class_Vector2i), [Vector3](class_vector3.md#class_Vector3), [Vector3i](class_vector3i.md#class_Vector3i), [Vector4](class_vector4.md#class_Vector4), [Vector4i](class_vector4i.md#class_Vector4i).

::

    snapped(100, 32)  # Returns 96
    snapped(3.14159, 0.01)  # Returns 3.14

    snapped(Vector2(34, 70), Vector2(8, 8))  # Returns (32, 72)

See also ceil(), floor(), and round().

 **Note:** For better type safety, use snappedf(), snappedi(), [Vector2.snapped()](class_vector2.md#class_Vector2_method_snapped), [Vector2i.snapped()](class_vector2i.md#class_Vector2i_method_snapped), [Vector3.snapped()](class_vector3.md#class_Vector3_method_snapped), [Vector3i.snapped()](class_vector3i.md#class_Vector3i_method_snapped), [Vector4.snapped()](class_vector4.md#class_Vector4_method_snapped), or [Vector4i.snapped()](class_vector4i.md#class_Vector4i_method_snapped).

---

.. _class_@GlobalScope_method_snappedf:

[float](class_float.md#class_float) **snappedf** ( x: [float](class_float.md#class_float), step: [float](class_float.md#class_float) ) 🔗

Returns the multiple of `step` that is the closest to `x`. This can also be used to round a floating-point number to an arbitrary number of decimals.

A type-safe version of snapped(), returning a [float](class_float.md#class_float).

::

    snappedf(32.0, 2.5)  # Returns 32.5
    snappedf(3.14159, 0.01)  # Returns 3.14

---

.. _class_@GlobalScope_method_snappedi:

[int](class_int.md#class_int) **snappedi** ( x: [float](class_float.md#class_float), step: [int](class_int.md#class_int) ) 🔗

Returns the multiple of `step` that is the closest to `x`.

A type-safe version of snapped(), returning an [int](class_int.md#class_int).

::

    snappedi(53, 16)  # Returns 48
    snappedi(4096, 100)  # Returns 4100

---

.. _class_@GlobalScope_method_sqrt:

[float](class_float.md#class_float) **sqrt** ( x: [float](class_float.md#class_float) ) 🔗

Returns the square root of `x`, where `x` is a non-negative number.

::

    sqrt(9)     # Returns 3
    sqrt(10.24) # Returns 3.2
    sqrt(-1)    # Returns NaN

 **Note:** Negative values of `x` return NaN ("Not a Number"). In C#, if you need negative inputs, use `System.Numerics.Complex`.

---

.. _class_@GlobalScope_method_step_decimals:

[int](class_int.md#class_int) **step_decimals** ( x: [float](class_float.md#class_float) ) 🔗

Returns the position of the first non-zero digit, after the decimal point. Note that the maximum return value is 10, which is a design decision in the implementation.

::

    var n = step_decimals(5)       # n is 0
    n = step_decimals(1.0005)      # n is 4
    n = step_decimals(0.000000005) # n is 9

---

.. _class_@GlobalScope_method_str:

[String](class_string.md#class_String) **str** ( ... ) *vararg* 🔗

Converts one or more arguments of any [Variant](class_variant.md#class_Variant) type to a [String](class_string.md#class_String) in the best way possible.

::

    var a = [10, 20, 30]
    var b = str(a)
    print(len(a)) # Prints 3 (the number of elements in the array).
    print(len(b)) # Prints 12 (the length of the string "[10, 20, 30]").

---

.. _class_@GlobalScope_method_str_to_var:

[Variant](class_variant.md#class_Variant) **str_to_var** ( string: [String](class_string.md#class_String) ) 🔗

Converts a formatted `string` that was returned by var_to_str() to the original [Variant](class_variant.md#class_Variant).

.. tabs::

```
```

    var data = '{ "a": 1, "b": 2 }' # data is a String
    var dict = str_to_var(data)     # dict is a Dictionary
    print(dict["a"])                # Prints 1

```
```

    string data = "{ \"a\": 1, \"b\": 2 }";           // data is a string
    var dict = GD.StrToVar(data).AsGodotDictionary(); // dict is a Dictionary
    GD.Print(dict["a"]);                              // Prints 1

---

.. _class_@GlobalScope_method_tan:

[float](class_float.md#class_float) **tan** ( angle_rad: [float](class_float.md#class_float) ) 🔗

Returns the tangent of angle `angle_rad` in radians.

::

    tan(deg_to_rad(45)) # Returns 1

---

.. _class_@GlobalScope_method_tanh:

[float](class_float.md#class_float) **tanh** ( x: [float](class_float.md#class_float) ) 🔗

Returns the hyperbolic tangent of `x`.

::

    var a = log(2.0) # Returns 0.693147
    tanh(a)          # Returns 0.6

---

.. _class_@GlobalScope_method_type_convert:

[Variant](class_variant.md#class_Variant) **type_convert** ( variant: [Variant](class_variant.md#class_Variant), type: [int](class_int.md#class_int) ) 🔗

Converts the given `variant` to the given `type`, using the Variant.Type values. This method is generous with how it handles types, it can automatically convert between array types, convert numeric [String](class_string.md#class_String) s to [int](class_int.md#class_int), and converting most things to [String](class_string.md#class_String).

If the type conversion cannot be done, this method will return the default value for that type, for example converting [Rect2](class_rect2.md#class_Rect2) to [Vector2](class_vector2.md#class_Vector2) will always return [Vector2.ZERO](class_vector2.md#class_Vector2_constant_ZERO). This method will never show error messages as long as `type` is a valid Variant type.

The returned value is a [Variant](class_variant.md#class_Variant), but the data inside and its type will be the same as the requested type.

::

    type_convert("Hi!", TYPE_INT) # Returns 0
    type_convert("123", TYPE_INT) # Returns 123
    type_convert(123.4, TYPE_INT) # Returns 123
    type_convert(5, TYPE_VECTOR2) # Returns (0, 0)
    type_convert("Hi!", TYPE_NIL) # Returns null

---

.. _class_@GlobalScope_method_type_string:

[String](class_string.md#class_String) **type_string** ( type: [int](class_int.md#class_int) ) 🔗

Returns a human-readable name of the given `type`, using the Variant.Type values.

::

    print(TYPE_INT) # Prints 2
    print(type_string(TYPE_INT)) # Prints "int"
    print(type_string(TYPE_STRING)) # Prints "String"

See also typeof().

---

.. _class_@GlobalScope_method_typeof:

[int](class_int.md#class_int) **typeof** ( variable: [Variant](class_variant.md#class_Variant) ) 🔗

Returns the internal type of the given `variable`, using the Variant.Type values.

::

    var json = JSON.new()
    json.parse('["a", "b", "c"]')
    var result = json.get_data()
    if typeof(result) == TYPE_ARRAY:
        print(result[0]) # Prints "a"
    else:
        print("Unexpected result!")

See also type_string().

---

.. _class_@GlobalScope_method_var_to_bytes:

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **var_to_bytes** ( variable: [Variant](class_variant.md#class_Variant) ) 🔗

Encodes a [Variant](class_variant.md#class_Variant) value to a byte array, without encoding objects. Deserialization can be done with bytes_to_var().

 **Note:** If you need object serialization, see var_to_bytes_with_objects().

 **Note:** Encoding [Callable](class_callable.md#class_Callable) is not supported and will result in an empty value, regardless of the data.

---

.. _class_@GlobalScope_method_var_to_bytes_with_objects:

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **var_to_bytes_with_objects** ( variable: [Variant](class_variant.md#class_Variant) ) 🔗

Encodes a [Variant](class_variant.md#class_Variant) value to a byte array. Encoding objects is allowed (and can potentially include executable code). Deserialization can be done with bytes_to_var_with_objects().

 **Note:** Encoding [Callable](class_callable.md#class_Callable) is not supported and will result in an empty value, regardless of the data.

---

.. _class_@GlobalScope_method_var_to_str:

[String](class_string.md#class_String) **var_to_str** ( variable: [Variant](class_variant.md#class_Variant) ) 🔗

Converts a [Variant](class_variant.md#class_Variant) `variable` to a formatted [String](class_string.md#class_String) that can then be parsed using str_to_var().

.. tabs::

```
```

    var a = { "a": 1, "b": 2 }
    print(var_to_str(a))

```
```

    var a = new Godot.Collections.Dictionary { ["a"] = 1, ["b"] = 2 };
    GD.Print(GD.VarToStr(a));

Prints:

.. code:: text

    {
        "a": 1,
        "b": 2
    }

 **Note:** Converting [Signal](class_signal.md#class_Signal) or [Callable](class_callable.md#class_Callable) is not supported and will result in an empty value for these types, regardless of their data.

---

.. _class_@GlobalScope_method_weakref:

[Variant](class_variant.md#class_Variant) **weakref** ( obj: [Variant](class_variant.md#class_Variant) ) 🔗

Returns a [WeakRef](class_weakref.md#class_WeakRef) instance holding a weak reference to `obj`. Returns an empty [WeakRef](class_weakref.md#class_WeakRef) instance if `obj` is `null`. Prints an error and returns `null` if `obj` is neither [Object](class_object.md#class_Object)-derived nor `null`.

A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.

---

.. _class_@GlobalScope_method_wrap:

[Variant](class_variant.md#class_Variant) **wrap** ( value: [Variant](class_variant.md#class_Variant), min: [Variant](class_variant.md#class_Variant), max: [Variant](class_variant.md#class_Variant) ) 🔗

Wraps the [Variant](class_variant.md#class_Variant) `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

Variant types [int](class_int.md#class_int) and [float](class_float.md#class_float) are supported. If any of the arguments is [float](class_float.md#class_float), this function returns a [float](class_float.md#class_float), otherwise it returns an [int](class_int.md#class_int).

::

    var a = wrap(4, 5, 10)
    # a is 9 (int)

    var a = wrap(7, 5, 10)
    # a is 7 (int)

    var a = wrap(10.5, 5, 10)
    # a is 5.5 (float)

---

.. _class_@GlobalScope_method_wrapf:

[float](class_float.md#class_float) **wrapf** ( value: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) 🔗

Wraps the float `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

::

    # Infinite loop between 5.0 and 9.9
    value = wrapf(value + 0.1, 5.0, 10.0)

::

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, 0.0, TAU)

::

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, -PI, PI)

 **Note:** If `min` is `0`, this is equivalent to fposmod(), so prefer using that instead. wrapf() is more flexible than using the fposmod() approach by giving the user control over the minimum value.

---

.. _class_@GlobalScope_method_wrapi:

[int](class_int.md#class_int) **wrapi** ( value: [int](class_int.md#class_int), min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) 🔗

Wraps the integer `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

::

    # Infinite loop between 5 and 9
    frame = wrapi(frame + 1, 5, 10)

::

    # result is -2
    var result = wrapi(-6, -5, -1)

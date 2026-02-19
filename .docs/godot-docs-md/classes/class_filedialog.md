<span id="class_FileDialog"></span>

## FileDialog

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class_ConfirmationDialog) **<** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) **<** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorFileDialog](class_editorfiledialog.md#class_EditorFileDialog)

A dialog for selecting files or directories in the filesystem.

### Description

**FileDialog** is a preset dialog used to choose files and directories in the filesystem. It supports filter masks. **FileDialog** automatically sets its window title according to the [file_mode](class_filedialog.md#class_FileDialog_property_file_mode). If you want to use a custom title, disable this by setting [mode_overrides_title](class_filedialog.md#class_FileDialog_property_mode_overrides_title) to `false`.

 **Note:** **FileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class_Window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped).

### Properties


| [Access](class_filedialog.md#enum_FileDialog_Access) | [access](class_filedialog.md#class_FileDialog_property_access) | `0` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [current_dir](class_filedialog.md#class_FileDialog_property_current_dir) |
| [String](class_string.md#class_String) | [current_file](class_filedialog.md#class_FileDialog_property_current_file) |
| [String](class_string.md#class_String) | [current_path](class_filedialog.md#class_FileDialog_property_current_path) |
| [bool](class_bool.md#class_bool) | [deleting_enabled](class_filedialog.md#class_FileDialog_property_deleting_enabled) | `true` |
| [bool](class_bool.md#class_bool) | dialog_hide_on_ok | `false` (overrides [AcceptDialog](class_acceptdialog.md#class_AcceptDialog_property_dialog_hide_on_ok)) |
| [DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) | [display_mode](class_filedialog.md#class_FileDialog_property_display_mode) | `0` |
| [bool](class_bool.md#class_bool) | [favorites_enabled](class_filedialog.md#class_FileDialog_property_favorites_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [file_filter_toggle_enabled](class_filedialog.md#class_FileDialog_property_file_filter_toggle_enabled) | `true` |
| [FileMode](class_filedialog.md#enum_FileDialog_FileMode) | [file_mode](class_filedialog.md#class_FileDialog_property_file_mode) | `4` |
| [bool](class_bool.md#class_bool) | [file_sort_options_enabled](class_filedialog.md#class_FileDialog_property_file_sort_options_enabled) | `true` |
| [String](class_string.md#class_String) | [filename_filter](class_filedialog.md#class_FileDialog_property_filename_filter) | `""` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [filters](class_filedialog.md#class_FileDialog_property_filters) | `PackedStringArray()` |
| [bool](class_bool.md#class_bool) | [folder_creation_enabled](class_filedialog.md#class_FileDialog_property_folder_creation_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [hidden_files_toggle_enabled](class_filedialog.md#class_FileDialog_property_hidden_files_toggle_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [layout_toggle_enabled](class_filedialog.md#class_FileDialog_property_layout_toggle_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [mode_overrides_title](class_filedialog.md#class_FileDialog_property_mode_overrides_title) | `true` |
| [int](class_int.md#class_int) | [option_count](class_filedialog.md#class_FileDialog_property_option_count) | `0` |
| [bool](class_bool.md#class_bool) | [overwrite_warning_enabled](class_filedialog.md#class_FileDialog_property_overwrite_warning_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [recent_list_enabled](class_filedialog.md#class_FileDialog_property_recent_list_enabled) | `true` |
| [String](class_string.md#class_String) | [root_subfolder](class_filedialog.md#class_FileDialog_property_root_subfolder) | `""` |
| [bool](class_bool.md#class_bool) | [show_hidden_files](class_filedialog.md#class_FileDialog_property_show_hidden_files) | `false` |
| [Vector2i](class_vector2i.md#class_Vector2i) | size | `Vector2i(640, 360)` (overrides [Window](class_window.md#class_Window_property_size)) |
| [String](class_string.md#class_String) | title | `"Save a File"` (overrides [Window](class_window.md#class_Window_property_title)) |
| [bool](class_bool.md#class_bool) | [use_native_dialog](class_filedialog.md#class_FileDialog_property_use_native_dialog) | `false` |

### Methods


| void | [add_filter](class_filedialog.md#class_FileDialog_method_add_filter) ( filter: [String](class_string.md#class_String), description: [String](class_string.md#class_String) = "", mime_type: [String](class_string.md#class_String) = "" ) |
| --- | --- |
| void | [add_option](class_filedialog.md#class_FileDialog_method_add_option) ( name: [String](class_string.md#class_String), values: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), default_value_index: [int](class_int.md#class_int) ) |
| void | [clear_filename_filter](class_filedialog.md#class_FileDialog_method_clear_filename_filter) ( ) |
| void | [clear_filters](class_filedialog.md#class_FileDialog_method_clear_filters) ( ) |
| void | [deselect_all](class_filedialog.md#class_FileDialog_method_deselect_all) ( ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_favorite_list](class_filedialog.md#class_FileDialog_method_get_favorite_list) ( ) static |
| [LineEdit](class_lineedit.md#class_LineEdit) | [get_line_edit](class_filedialog.md#class_FileDialog_method_get_line_edit) ( ) |
| [int](class_int.md#class_int) | [get_option_default](class_filedialog.md#class_FileDialog_method_get_option_default) ( option: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_option_name](class_filedialog.md#class_FileDialog_method_get_option_name) ( option: [int](class_int.md#class_int) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_option_values](class_filedialog.md#class_FileDialog_method_get_option_values) ( option: [int](class_int.md#class_int) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_recent_list](class_filedialog.md#class_FileDialog_method_get_recent_list) ( ) static |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_selected_options](class_filedialog.md#class_FileDialog_method_get_selected_options) ( ) const |
| [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer) | [get_vbox](class_filedialog.md#class_FileDialog_method_get_vbox) ( ) |
| void | [invalidate](class_filedialog.md#class_FileDialog_method_invalidate) ( ) |
| [bool](class_bool.md#class_bool) | [is_customization_flag_enabled](class_filedialog.md#class_FileDialog_method_is_customization_flag_enabled) ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) const |
| void | [popup_file_dialog](class_filedialog.md#class_FileDialog_method_popup_file_dialog) ( ) |
| void | [set_customization_flag_enabled](class_filedialog.md#class_FileDialog_method_set_customization_flag_enabled) ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_favorite_list](class_filedialog.md#class_FileDialog_method_set_favorite_list) ( favorites: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) static |
| void | [set_get_icon_callback](class_filedialog.md#class_FileDialog_method_set_get_icon_callback) ( callback: [Callable](class_callable.md#class_Callable) ) static |
| void | [set_get_thumbnail_callback](class_filedialog.md#class_FileDialog_method_set_get_thumbnail_callback) ( callback: [Callable](class_callable.md#class_Callable) ) static |
| void | [set_option_default](class_filedialog.md#class_FileDialog_method_set_option_default) ( option: [int](class_int.md#class_int), default_value_index: [int](class_int.md#class_int) ) |
| void | [set_option_name](class_filedialog.md#class_FileDialog_method_set_option_name) ( option: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_option_values](class_filedialog.md#class_FileDialog_method_set_option_values) ( option: [int](class_int.md#class_int), values: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| void | [set_recent_list](class_filedialog.md#class_FileDialog_method_set_recent_list) ( recents: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) static |

### Theme Properties


| [Color](class_color.md#class_Color) | [file_disabled_color](class_filedialog.md#class_FileDialog_theme_color_file_disabled_color) | `Color(1, 1, 1, 0.25)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [file_icon_color](class_filedialog.md#class_FileDialog_theme_color_file_icon_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [folder_icon_color](class_filedialog.md#class_FileDialog_theme_color_folder_icon_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [thumbnail_size](class_filedialog.md#class_FileDialog_theme_constant_thumbnail_size) | `64` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [back_folder](class_filedialog.md#class_FileDialog_theme_icon_back_folder) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [create_folder](class_filedialog.md#class_FileDialog_theme_icon_create_folder) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [favorite](class_filedialog.md#class_FileDialog_theme_icon_favorite) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [favorite_down](class_filedialog.md#class_FileDialog_theme_icon_favorite_down) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [favorite_up](class_filedialog.md#class_FileDialog_theme_icon_favorite_up) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [file](class_filedialog.md#class_FileDialog_theme_icon_file) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [file_thumbnail](class_filedialog.md#class_FileDialog_theme_icon_file_thumbnail) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folder](class_filedialog.md#class_FileDialog_theme_icon_folder) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folder_thumbnail](class_filedialog.md#class_FileDialog_theme_icon_folder_thumbnail) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [forward_folder](class_filedialog.md#class_FileDialog_theme_icon_forward_folder) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [list_mode](class_filedialog.md#class_FileDialog_theme_icon_list_mode) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [parent_folder](class_filedialog.md#class_FileDialog_theme_icon_parent_folder) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [reload](class_filedialog.md#class_FileDialog_theme_icon_reload) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [sort](class_filedialog.md#class_FileDialog_theme_icon_sort) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [thumbnail_mode](class_filedialog.md#class_FileDialog_theme_icon_thumbnail_mode) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [toggle_filename_filter](class_filedialog.md#class_FileDialog_theme_icon_toggle_filename_filter) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [toggle_hidden](class_filedialog.md#class_FileDialog_theme_icon_toggle_hidden) |

---

### Signals

<span id="class_FileDialog_signal_dir_selected"></span>

**dir_selected** ( dir: [String](class_string.md#class_String) ) [🔗](class_filedialog.md#class_FileDialog_signal_dir_selected)

Emitted when the user selects a directory.

---

<span id="class_FileDialog_signal_file_selected"></span>

**file_selected** ( path: [String](class_string.md#class_String) ) [🔗](class_filedialog.md#class_FileDialog_signal_file_selected)

Emitted when the user selects a file by double-clicking it or pressing the **OK** button.

---

<span id="class_FileDialog_signal_filename_filter_changed"></span>

**filename_filter_changed** ( filter: [String](class_string.md#class_String) ) [🔗](class_filedialog.md#class_FileDialog_signal_filename_filter_changed)

Emitted when the filter for file names changes.

---

<span id="class_FileDialog_signal_files_selected"></span>

**files_selected** ( paths: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_filedialog.md#class_FileDialog_signal_files_selected)

Emitted when the user selects multiple files.

---

### Enumerations

<span id="enum_FileDialog_FileMode"></span>

enum **FileMode**: [🔗](class_filedialog.md#enum_FileDialog_FileMode)

<span id="class_FileDialog_constant_FILE_MODE_OPEN_FILE"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **FILE_MODE_OPEN_FILE** = `0`

The dialog allows selecting one, and only one file.

<span id="class_FileDialog_constant_FILE_MODE_OPEN_FILES"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **FILE_MODE_OPEN_FILES** = `1`

The dialog allows selecting multiple files.

<span id="class_FileDialog_constant_FILE_MODE_OPEN_DIR"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **FILE_MODE_OPEN_DIR** = `2`

The dialog only allows selecting a directory, disallowing the selection of any file.

<span id="class_FileDialog_constant_FILE_MODE_OPEN_ANY"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **FILE_MODE_OPEN_ANY** = `3`

The dialog allows selecting one file or directory.

<span id="class_FileDialog_constant_FILE_MODE_SAVE_FILE"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **FILE_MODE_SAVE_FILE** = `4`

The dialog will warn when a file exists.

---

<span id="enum_FileDialog_Access"></span>

enum **Access**: [🔗](class_filedialog.md#enum_FileDialog_Access)

<span id="class_FileDialog_constant_ACCESS_RESOURCES"></span>

[Access](class_filedialog.md#enum_FileDialog_Access) **ACCESS_RESOURCES** = `0`

The dialog only allows accessing files under the [Resource](class_resource.md#class_Resource) path (`res://`).

<span id="class_FileDialog_constant_ACCESS_USERDATA"></span>

[Access](class_filedialog.md#enum_FileDialog_Access) **ACCESS_USERDATA** = `1`

The dialog only allows accessing files under user data path (`user://`).

<span id="class_FileDialog_constant_ACCESS_FILESYSTEM"></span>

[Access](class_filedialog.md#enum_FileDialog_Access) **ACCESS_FILESYSTEM** = `2`

The dialog allows accessing files on the whole file system.

---

<span id="enum_FileDialog_DisplayMode"></span>

enum **DisplayMode**: [🔗](class_filedialog.md#enum_FileDialog_DisplayMode)

<span id="class_FileDialog_constant_DISPLAY_THUMBNAILS"></span>

[DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) **DISPLAY_THUMBNAILS** = `0`

The dialog displays files as a grid of thumbnails. Use [thumbnail_size](class_filedialog.md#class_FileDialog_theme_constant_thumbnail_size) to adjust their size.

<span id="class_FileDialog_constant_DISPLAY_LIST"></span>

[DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) **DISPLAY_LIST** = `1`

The dialog displays files as a list of filenames.

---

<span id="enum_FileDialog_Customization"></span>

enum **Customization**: [🔗](class_filedialog.md#enum_FileDialog_Customization)

<span id="class_FileDialog_constant_CUSTOMIZATION_HIDDEN_FILES"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_HIDDEN_FILES** = `0`

Toggles visibility of the favorite button, and the favorite list on the left side of the dialog.

Equivalent to [hidden_files_toggle_enabled](class_filedialog.md#class_FileDialog_property_hidden_files_toggle_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_CREATE_FOLDER"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_CREATE_FOLDER** = `1`

If enabled, shows the button for creating new directories (when using [FILE_MODE_OPEN_DIR](class_filedialog.md#class_FileDialog_constant_FILE_MODE_OPEN_DIR), [FILE_MODE_OPEN_ANY](class_filedialog.md#class_FileDialog_constant_FILE_MODE_OPEN_ANY), or [FILE_MODE_SAVE_FILE](class_filedialog.md#class_FileDialog_constant_FILE_MODE_SAVE_FILE)).

Equivalent to [folder_creation_enabled](class_filedialog.md#class_FileDialog_property_folder_creation_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_FILE_FILTER"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_FILE_FILTER** = `2`

If enabled, shows the toggle file filter button.

Equivalent to [file_filter_toggle_enabled](class_filedialog.md#class_FileDialog_property_file_filter_toggle_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_FILE_SORT"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_FILE_SORT** = `3`

If enabled, shows the file sorting options button.

Equivalent to [file_sort_options_enabled](class_filedialog.md#class_FileDialog_property_file_sort_options_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_FAVORITES"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_FAVORITES** = `4`

If enabled, shows the toggle favorite button and favorite list on the left side of the dialog.

Equivalent to [favorites_enabled](class_filedialog.md#class_FileDialog_property_favorites_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_RECENT"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_RECENT** = `5`

If enabled, shows the recent directories list on the left side of the dialog.

Equivalent to [recent_list_enabled](class_filedialog.md#class_FileDialog_property_recent_list_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_LAYOUT"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_LAYOUT** = `6`

If enabled, shows the layout switch buttons (list/thumbnails).

Equivalent to [layout_toggle_enabled](class_filedialog.md#class_FileDialog_property_layout_toggle_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_OVERWRITE_WARNING"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_OVERWRITE_WARNING** = `7`

If enabled, the **FileDialog** will warn the user before overwriting files in save mode.

Equivalent to [overwrite_warning_enabled](class_filedialog.md#class_FileDialog_property_overwrite_warning_enabled).

<span id="class_FileDialog_constant_CUSTOMIZATION_DELETE"></span>

[Customization](class_filedialog.md#enum_FileDialog_Customization) **CUSTOMIZATION_DELETE** = `8`

If enabled, the context menu will show the "Delete" option, which allows moving files and folders to trash.

Equivalent to [deleting_enabled](class_filedialog.md#class_FileDialog_property_deleting_enabled).

---

### Property Descriptions

<span id="class_FileDialog_property_access"></span>

[Access](class_filedialog.md#enum_FileDialog_Access) **access** = `0` [🔗](class_filedialog.md#class_FileDialog_property_access)

- void **set_access** ( value: [Access](class_filedialog.md#enum_FileDialog_Access) )
- [Access](class_filedialog.md#enum_FileDialog_Access) **get_access** ( )

The file system access scope.

 **Warning:** In Web builds, FileDialog cannot access the host file system. In sandboxed Linux and macOS environments, [use_native_dialog](class_filedialog.md#class_FileDialog_property_use_native_dialog) is automatically used to allow limited access to host file system.

---

<span id="class_FileDialog_property_current_dir"></span>

[String](class_string.md#class_String) **current_dir** [🔗](class_filedialog.md#class_FileDialog_property_current_dir)

- void **set_current_dir** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_current_dir** ( )

The current working directory of the file dialog.

 **Note:** For native file dialogs, this property is only treated as a hint and may not be respected by specific OS implementations.

---

<span id="class_FileDialog_property_current_file"></span>

[String](class_string.md#class_String) **current_file** [🔗](class_filedialog.md#class_FileDialog_property_current_file)

- void **set_current_file** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_current_file** ( )

The currently selected file of the file dialog.

---

<span id="class_FileDialog_property_current_path"></span>

[String](class_string.md#class_String) **current_path** [🔗](class_filedialog.md#class_FileDialog_property_current_path)

- void **set_current_path** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_current_path** ( )

The currently selected file path of the file dialog.

---

<span id="class_FileDialog_property_deleting_enabled"></span>

[bool](class_bool.md#class_bool) **deleting_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_deleting_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, the context menu will show the "Delete" option, which allows moving files and folders to trash.

---

<span id="class_FileDialog_property_display_mode"></span>

[DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) **display_mode** = `0` [🔗](class_filedialog.md#class_FileDialog_property_display_mode)

- void **set_display_mode** ( value: [DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) )
- [DisplayMode](class_filedialog.md#enum_FileDialog_DisplayMode) **get_display_mode** ( )

Display mode of the dialog's file list.

---

<span id="class_FileDialog_property_favorites_enabled"></span>

[bool](class_bool.md#class_bool) **favorites_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_favorites_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the toggle favorite button and favorite list on the left side of the dialog.

---

<span id="class_FileDialog_property_file_filter_toggle_enabled"></span>

[bool](class_bool.md#class_bool) **file_filter_toggle_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_file_filter_toggle_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the toggle file filter button.

---

<span id="class_FileDialog_property_file_mode"></span>

[FileMode](class_filedialog.md#enum_FileDialog_FileMode) **file_mode** = `4` [🔗](class_filedialog.md#class_FileDialog_property_file_mode)

- void **set_file_mode** ( value: [FileMode](class_filedialog.md#enum_FileDialog_FileMode) )
- [FileMode](class_filedialog.md#enum_FileDialog_FileMode) **get_file_mode** ( )

The dialog's open or save mode, which affects the selection behavior.

---

<span id="class_FileDialog_property_file_sort_options_enabled"></span>

[bool](class_bool.md#class_bool) **file_sort_options_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_file_sort_options_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the file sorting options button.

---

<span id="class_FileDialog_property_filename_filter"></span>

[String](class_string.md#class_String) **filename_filter** = `""` [🔗](class_filedialog.md#class_FileDialog_property_filename_filter)

- void **set_filename_filter** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_filename_filter** ( )

The filter for file names (case-insensitive). When set to a non-empty string, only files that contains the substring will be shown. [filename_filter](class_filedialog.md#class_FileDialog_property_filename_filter) can be edited by the user with the filter button at the top of the file dialog.

See also [filters](class_filedialog.md#class_FileDialog_property_filters), which should be used to restrict the file types that can be selected instead of [filename_filter](class_filedialog.md#class_FileDialog_property_filename_filter) which is meant to be set by the user.

---

<span id="class_FileDialog_property_filters"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **filters** = `PackedStringArray()` [🔗](class_filedialog.md#class_FileDialog_property_filters)

- void **set_filters** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_filters** ( )

The available file type filters. Each filter string in the array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. Both file extensions and MIME type should be always set.

 **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

<span id="class_FileDialog_property_folder_creation_enabled"></span>

[bool](class_bool.md#class_bool) **folder_creation_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_folder_creation_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the button for creating new directories (when using [FILE_MODE_OPEN_DIR](class_filedialog.md#class_FileDialog_constant_FILE_MODE_OPEN_DIR), [FILE_MODE_OPEN_ANY](class_filedialog.md#class_FileDialog_constant_FILE_MODE_OPEN_ANY), or [FILE_MODE_SAVE_FILE](class_filedialog.md#class_FileDialog_constant_FILE_MODE_SAVE_FILE)), and the context menu will have the "New Folder..." option.

---

<span id="class_FileDialog_property_hidden_files_toggle_enabled"></span>

[bool](class_bool.md#class_bool) **hidden_files_toggle_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_hidden_files_toggle_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the toggle hidden files button.

---

<span id="class_FileDialog_property_layout_toggle_enabled"></span>

[bool](class_bool.md#class_bool) **layout_toggle_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_layout_toggle_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the layout switch buttons (list/thumbnails).

---

<span id="class_FileDialog_property_mode_overrides_title"></span>

[bool](class_bool.md#class_bool) **mode_overrides_title** = `true` [🔗](class_filedialog.md#class_FileDialog_property_mode_overrides_title)

- void **set_mode_overrides_title** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_mode_overriding_title** ( )

If `true`, changing the [file_mode](class_filedialog.md#class_FileDialog_property_file_mode) property will set the window title accordingly (e.g. setting [file_mode](class_filedialog.md#class_FileDialog_property_file_mode) to [FILE_MODE_OPEN_FILE](class_filedialog.md#class_FileDialog_constant_FILE_MODE_OPEN_FILE) will change the window title to "Open a File").

---

<span id="class_FileDialog_property_option_count"></span>

[int](class_int.md#class_int) **option_count** = `0` [🔗](class_filedialog.md#class_FileDialog_property_option_count)

- void **set_option_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_option_count** ( )

The number of additional [OptionButton](class_optionbutton.md#class_OptionButton) s and [CheckBox](class_checkbox.md#class_CheckBox) es in the dialog.

---

<span id="class_FileDialog_property_overwrite_warning_enabled"></span>

[bool](class_bool.md#class_bool) **overwrite_warning_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_overwrite_warning_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, the **FileDialog** will warn the user before overwriting files in save mode.

---

<span id="class_FileDialog_property_recent_list_enabled"></span>

[bool](class_bool.md#class_bool) **recent_list_enabled** = `true` [🔗](class_filedialog.md#class_FileDialog_property_recent_list_enabled)

- void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const*

If `true`, shows the recent directories list on the left side of the dialog.

---

<span id="class_FileDialog_property_root_subfolder"></span>

[String](class_string.md#class_String) **root_subfolder** = `""` [🔗](class_filedialog.md#class_FileDialog_property_root_subfolder)

- void **set_root_subfolder** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_root_subfolder** ( )

If non-empty, the given sub-folder will be "root" of this **FileDialog**, i.e. user won't be able to go to its parent directory.

 **Note:** This property is ignored by native file dialogs.

---

<span id="class_FileDialog_property_show_hidden_files"></span>

[bool](class_bool.md#class_bool) **show_hidden_files** = `false` [🔗](class_filedialog.md#class_FileDialog_property_show_hidden_files)

- void **set_show_hidden_files** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_hidden_files** ( )

If `true`, the dialog will show hidden files.

 **Note:** This property is ignored by native file dialogs on Android and Linux.

---

<span id="class_FileDialog_property_use_native_dialog"></span>

[bool](class_bool.md#class_bool) **use_native_dialog** = `false` [🔗](class_filedialog.md#class_FileDialog_property_use_native_dialog)

- void **set_use_native_dialog** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_native_dialog** ( )

If `true`, and if supported by the current [DisplayServer](class_displayserver.md#class_DisplayServer), OS native dialog will be used instead of custom one.

 **Note:** On Android, it is only supported when using [ACCESS_FILESYSTEM](class_filedialog.md#class_FileDialog_constant_ACCESS_FILESYSTEM). For access mode [ACCESS_RESOURCES](class_filedialog.md#class_FileDialog_constant_ACCESS_RESOURCES) and [ACCESS_USERDATA](class_filedialog.md#class_FileDialog_constant_ACCESS_USERDATA), the system will fall back to custom FileDialog.

 **Note:** On Linux and macOS, sandboxed apps always use native dialogs to access the host file system.

 **Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class_OS_method_get_granted_permissions) to get a list of saved bookmarks.

 **Note:** Native dialogs are isolated from the base process, file dialog properties can't be modified once the dialog is shown.

 **Note:** This property is ignored in [EditorFileDialog](class_editorfiledialog.md#class_EditorFileDialog).

---

### Method Descriptions

<span id="class_FileDialog_method_add_filter"></span>

void **add_filter** ( filter: [String](class_string.md#class_String), description: [String](class_string.md#class_String) = "", mime_type: [String](class_string.md#class_String) = "" ) [🔗](class_filedialog.md#class_FileDialog_method_add_filter)

Adds a comma-separated file extension `filter` and comma-separated MIME type `mime_type` option to the **FileDialog** with an optional `description`, which restricts what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename and extension can be `*` to match any string. Filters starting with `.` (i.e. empty filenames) are not allowed.

For example, a `filter` of `"*.png, *.jpg"`, a `mime_type` of `image/png, image/jpeg`, and a `description` of `"Images"` results in filter text "Images (\*.png, \*.jpg)".

 **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

---

<span id="class_FileDialog_method_add_option"></span>

void **add_option** ( name: [String](class_string.md#class_String), values: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), default_value_index: [int](class_int.md#class_int) ) [🔗](class_filedialog.md#class_FileDialog_method_add_option)

Adds an additional [OptionButton](class_optionbutton.md#class_OptionButton) to the file dialog. If `values` is empty, a [CheckBox](class_checkbox.md#class_CheckBox) is added instead.

 `default_value_index` should be an index of the value in the `values`. If `values` is empty it should be either `1` (checked), or `0` (unchecked).

---

<span id="class_FileDialog_method_clear_filename_filter"></span>

void **clear_filename_filter** ( ) [🔗](class_filedialog.md#class_FileDialog_method_clear_filename_filter)

Clear the filter for file names.

---

<span id="class_FileDialog_method_clear_filters"></span>

void **clear_filters** ( ) [🔗](class_filedialog.md#class_FileDialog_method_clear_filters)

Clear all the added filters in the dialog.

---

<span id="class_FileDialog_method_deselect_all"></span>

void **deselect_all** ( ) [🔗](class_filedialog.md#class_FileDialog_method_deselect_all)

Clear all currently selected items in the dialog.

---

<span id="class_FileDialog_method_get_favorite_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_favorite_list** ( ) *static* [🔗](class_filedialog.md#class_FileDialog_method_get_favorite_list)

Returns the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to store the list of favorites between project sessions. This method can be called only from the main thread.

---

<span id="class_FileDialog_method_get_line_edit"></span>

[LineEdit](class_lineedit.md#class_LineEdit) **get_line_edit** ( ) [🔗](class_filedialog.md#class_FileDialog_method_get_line_edit)

Returns the LineEdit for the selected file.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_FileDialog_method_get_option_default"></span>

[int](class_int.md#class_int) **get_option_default** ( option: [int](class_int.md#class_int) ) *const* [🔗](class_filedialog.md#class_FileDialog_method_get_option_default)

Returns the default value index of the [OptionButton](class_optionbutton.md#class_OptionButton) or [CheckBox](class_checkbox.md#class_CheckBox) with index `option`.

---

<span id="class_FileDialog_method_get_option_name"></span>

[String](class_string.md#class_String) **get_option_name** ( option: [int](class_int.md#class_int) ) *const* [🔗](class_filedialog.md#class_FileDialog_method_get_option_name)

Returns the name of the [OptionButton](class_optionbutton.md#class_OptionButton) or [CheckBox](class_checkbox.md#class_CheckBox) with index `option`.

---

<span id="class_FileDialog_method_get_option_values"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_option_values** ( option: [int](class_int.md#class_int) ) *const* [🔗](class_filedialog.md#class_FileDialog_method_get_option_values)

Returns an array of values of the [OptionButton](class_optionbutton.md#class_OptionButton) with index `option`.

---

<span id="class_FileDialog_method_get_recent_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_recent_list** ( ) *static* [🔗](class_filedialog.md#class_FileDialog_method_get_recent_list)

Returns the list of recent directories, which is shared by all **FileDialog** nodes. Useful to store the list of recents between project sessions. This method can be called only from the main thread.

---

<span id="class_FileDialog_method_get_selected_options"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_selected_options** ( ) *const* [🔗](class_filedialog.md#class_FileDialog_method_get_selected_options)

Returns a [Dictionary](class_dictionary.md#class_Dictionary) with the selected values of the additional [OptionButton](class_optionbutton.md#class_OptionButton) s and/or [CheckBox](class_checkbox.md#class_CheckBox) es. [Dictionary](class_dictionary.md#class_Dictionary) keys are names and values are selected value indices.

---

<span id="class_FileDialog_method_get_vbox"></span>

[VBoxContainer](class_vboxcontainer.md#class_VBoxContainer) **get_vbox** ( ) [🔗](class_filedialog.md#class_FileDialog_method_get_vbox)

Returns the vertical box container of the dialog, custom controls can be added to it.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

 **Note:** Changes to this node are ignored by native file dialogs, use [add_option()](class_filedialog.md#class_FileDialog_method_add_option) to add custom elements to the dialog instead.

---

<span id="class_FileDialog_method_invalidate"></span>

void **invalidate** ( ) [🔗](class_filedialog.md#class_FileDialog_method_invalidate)

Invalidates and updates this dialog's content list.

 **Note:** This method does nothing on native file dialogs.

---

<span id="class_FileDialog_method_is_customization_flag_enabled"></span>

[bool](class_bool.md#class_bool) **is_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization) ) *const* [🔗](class_filedialog.md#class_FileDialog_method_is_customization_flag_enabled)

Returns `true` if the provided `flag` is enabled.

---

<span id="class_FileDialog_method_popup_file_dialog"></span>

void **popup_file_dialog** ( ) [🔗](class_filedialog.md#class_FileDialog_method_popup_file_dialog)

Shows the **FileDialog** using the default size and position for file dialogs, and selects the file name if there is a current file.

---

<span id="class_FileDialog_method_set_customization_flag_enabled"></span>

void **set_customization_flag_enabled** ( flag: [Customization](class_filedialog.md#enum_FileDialog_Customization), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_filedialog.md#class_FileDialog_method_set_customization_flag_enabled)

Sets the specified customization `flag`, allowing to customize the features available in this **FileDialog**.

---

<span id="class_FileDialog_method_set_favorite_list"></span>

void **set_favorite_list** ( favorites: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *static* [🔗](class_filedialog.md#class_FileDialog_method_set_favorite_list)

Sets the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to restore the list of favorites saved with [get_favorite_list()](class_filedialog.md#class_FileDialog_method_get_favorite_list). This method can be called only from the main thread.

 **Note:** **FileDialog** will update its internal [ItemList](class_itemlist.md#class_ItemList) of favorites when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.

---

<span id="class_FileDialog_method_set_get_icon_callback"></span>

void **set_get_icon_callback** ( callback: [Callable](class_callable.md#class_Callable) ) *static* [🔗](class_filedialog.md#class_FileDialog_method_set_get_icon_callback)

Sets the callback used by the **FileDialog** nodes to get a file icon, when [DISPLAY_LIST](class_filedialog.md#class_FileDialog_constant_DISPLAY_LIST) mode is used. The callback should take a single [String](class_string.md#class_String) argument (file path), and return a [Texture2D](class_texture2d.md#class_Texture2D). If an invalid texture is returned, the [file](class_filedialog.md#class_FileDialog_theme_icon_file) icon will be used instead.

---

<span id="class_FileDialog_method_set_get_thumbnail_callback"></span>

void **set_get_thumbnail_callback** ( callback: [Callable](class_callable.md#class_Callable) ) *static* [🔗](class_filedialog.md#class_FileDialog_method_set_get_thumbnail_callback)

Sets the callback used by the **FileDialog** nodes to get a file icon, when [DISPLAY_THUMBNAILS](class_filedialog.md#class_FileDialog_constant_DISPLAY_THUMBNAILS) mode is used. The callback should take a single [String](class_string.md#class_String) argument (file path), and return a [Texture2D](class_texture2d.md#class_Texture2D). If an invalid texture is returned, the [file_thumbnail](class_filedialog.md#class_FileDialog_theme_icon_file_thumbnail) icon will be used instead.

Thumbnails are usually more complex and may take a while to load. To avoid stalling the application, you can use [ImageTexture](class_imagetexture.md#class_ImageTexture) to asynchronously create the thumbnail.

::

    func _ready():
        FileDialog.set_get_thumbnail_callback(thumbnail_method)

    func thumbnail_method(path):
        var image_texture = ImageTexture.new()
        make_thumbnail_async(path, image_texture)
        return image_texture

    func make_thumbnail_async(path, image_texture):
        var thumbnail_texture = await generate_thumbnail(path) # Some method that generates a thumbnail.
        image_texture.set_image(thumbnail_texture.get_image())

---

<span id="class_FileDialog_method_set_option_default"></span>

void **set_option_default** ( option: [int](class_int.md#class_int), default_value_index: [int](class_int.md#class_int) ) [🔗](class_filedialog.md#class_FileDialog_method_set_option_default)

Sets the default value index of the [OptionButton](class_optionbutton.md#class_OptionButton) or [CheckBox](class_checkbox.md#class_CheckBox) with index `option`.

---

<span id="class_FileDialog_method_set_option_name"></span>

void **set_option_name** ( option: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_filedialog.md#class_FileDialog_method_set_option_name)

Sets the name of the [OptionButton](class_optionbutton.md#class_OptionButton) or [CheckBox](class_checkbox.md#class_CheckBox) with index `option`.

---

<span id="class_FileDialog_method_set_option_values"></span>

void **set_option_values** ( option: [int](class_int.md#class_int), values: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_filedialog.md#class_FileDialog_method_set_option_values)

Sets the option values of the [OptionButton](class_optionbutton.md#class_OptionButton) with index `option`.

---

<span id="class_FileDialog_method_set_recent_list"></span>

void **set_recent_list** ( recents: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *static* [🔗](class_filedialog.md#class_FileDialog_method_set_recent_list)

Sets the list of recent directories, which is shared by all **FileDialog** nodes. Useful to restore the list of recents saved with [set_recent_list()](class_filedialog.md#class_FileDialog_method_set_recent_list). This method can be called only from the main thread.

 **Note:** **FileDialog** will update its internal [ItemList](class_itemlist.md#class_ItemList) of recent directories when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.

---

### Theme Property Descriptions

<span id="class_FileDialog_theme_color_file_disabled_color"></span>

[Color](class_color.md#class_Color) **file_disabled_color** = `Color(1, 1, 1, 0.25)` [🔗](class_filedialog.md#class_FileDialog_theme_color_file_disabled_color)

The color tint for disabled files (when the **FileDialog** is used in open folder mode).

---

<span id="class_FileDialog_theme_color_file_icon_color"></span>

[Color](class_color.md#class_Color) **file_icon_color** = `Color(1, 1, 1, 1)` [🔗](class_filedialog.md#class_FileDialog_theme_color_file_icon_color)

The color modulation applied to the file icon.

---

<span id="class_FileDialog_theme_color_folder_icon_color"></span>

[Color](class_color.md#class_Color) **folder_icon_color** = `Color(1, 1, 1, 1)` [🔗](class_filedialog.md#class_FileDialog_theme_color_folder_icon_color)

The color modulation applied to the folder icon.

---

<span id="class_FileDialog_theme_constant_thumbnail_size"></span>

[int](class_int.md#class_int) **thumbnail_size** = `64` [🔗](class_filedialog.md#class_FileDialog_theme_constant_thumbnail_size)

The size of thumbnail icons when [DISPLAY_THUMBNAILS](class_filedialog.md#class_FileDialog_constant_DISPLAY_THUMBNAILS) is enabled.

---

<span id="class_FileDialog_theme_icon_back_folder"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **back_folder** [🔗](class_filedialog.md#class_FileDialog_theme_icon_back_folder)

Custom icon for the back arrow.

---

<span id="class_FileDialog_theme_icon_create_folder"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **create_folder** [🔗](class_filedialog.md#class_FileDialog_theme_icon_create_folder)

Custom icon for the create folder button.

---

<span id="class_FileDialog_theme_icon_favorite"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **favorite** [🔗](class_filedialog.md#class_FileDialog_theme_icon_favorite)

Custom icon for favorite folder button.

---

<span id="class_FileDialog_theme_icon_favorite_down"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **favorite_down** [🔗](class_filedialog.md#class_FileDialog_theme_icon_favorite_down)

Custom icon for button to move down a favorite entry.

---

<span id="class_FileDialog_theme_icon_favorite_up"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **favorite_up** [🔗](class_filedialog.md#class_FileDialog_theme_icon_favorite_up)

Custom icon for button to move up a favorite entry.

---

<span id="class_FileDialog_theme_icon_file"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **file** [🔗](class_filedialog.md#class_FileDialog_theme_icon_file)

Custom icon for files.

---

<span id="class_FileDialog_theme_icon_file_thumbnail"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **file_thumbnail** [🔗](class_filedialog.md#class_FileDialog_theme_icon_file_thumbnail)

Icon for files when in thumbnail mode.

---

<span id="class_FileDialog_theme_icon_folder"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folder** [🔗](class_filedialog.md#class_FileDialog_theme_icon_folder)

Custom icon for folders.

---

<span id="class_FileDialog_theme_icon_folder_thumbnail"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folder_thumbnail** [🔗](class_filedialog.md#class_FileDialog_theme_icon_folder_thumbnail)

Icon for folders when in thumbnail mode.

---

<span id="class_FileDialog_theme_icon_forward_folder"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **forward_folder** [🔗](class_filedialog.md#class_FileDialog_theme_icon_forward_folder)

Custom icon for the forward arrow.

---

<span id="class_FileDialog_theme_icon_list_mode"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **list_mode** [🔗](class_filedialog.md#class_FileDialog_theme_icon_list_mode)

Icon for the button that enables list mode.

---

<span id="class_FileDialog_theme_icon_parent_folder"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **parent_folder** [🔗](class_filedialog.md#class_FileDialog_theme_icon_parent_folder)

Custom icon for the parent folder arrow.

---

<span id="class_FileDialog_theme_icon_reload"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **reload** [🔗](class_filedialog.md#class_FileDialog_theme_icon_reload)

Custom icon for the reload button.

---

<span id="class_FileDialog_theme_icon_sort"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **sort** [🔗](class_filedialog.md#class_FileDialog_theme_icon_sort)

Custom icon for the sorting options menu.

---

<span id="class_FileDialog_theme_icon_thumbnail_mode"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **thumbnail_mode** [🔗](class_filedialog.md#class_FileDialog_theme_icon_thumbnail_mode)

Icon for the button that enables thumbnail mode.

---

<span id="class_FileDialog_theme_icon_toggle_filename_filter"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **toggle_filename_filter** [🔗](class_filedialog.md#class_FileDialog_theme_icon_toggle_filename_filter)

Custom icon for the toggle button for the filter for file names.

---

<span id="class_FileDialog_theme_icon_toggle_hidden"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **toggle_hidden** [🔗](class_filedialog.md#class_FileDialog_theme_icon_toggle_hidden)

Custom icon for the toggle hidden button.

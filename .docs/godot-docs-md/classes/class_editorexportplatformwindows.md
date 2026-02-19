<span id="class_EditorExportPlatformWindows"></span>

## EditorExportPlatformWindows

**Inherits:** [EditorExportPlatformPC](class_editorexportplatformpc.md#class_EditorExportPlatformPC) **<** [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Exporter for Windows.

### Description

The Windows exporter customizes how a Windows build is handled. In the editor's "Export" window, it is created when adding a new "Windows" preset.

### Tutorials

- [Exporting for Windows](../tutorials/export/exporting_for_windows.md)

### Properties


| [String](class_string.md#class_String) | application/company_name |
| --- | --- |
| [String](class_string.md#class_String) | application/console_wrapper_icon |
| [String](class_string.md#class_String) | application/copyright |
| [bool](class_bool.md#class_bool) | application/d3d12_agility_sdk_multiarch |
| [int](class_int.md#class_int) | application/export_angle |
| [int](class_int.md#class_int) | application/export_d3d12 |
| [String](class_string.md#class_String) | application/file_description |
| [String](class_string.md#class_String) | application/file_version |
| [String](class_string.md#class_String) | application/icon |
| [int](class_int.md#class_int) | application/icon_interpolation |
| [bool](class_bool.md#class_bool) | application/modify_resources |
| [String](class_string.md#class_String) | application/product_name |
| [String](class_string.md#class_String) | application/product_version |
| [String](class_string.md#class_String) | application/trademarks |
| [String](class_string.md#class_String) | binary_format/architecture |
| [bool](class_bool.md#class_bool) | binary_format/embed_pck |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | codesign/custom_options |
| [String](class_string.md#class_String) | codesign/description |
| [int](class_int.md#class_int) | codesign/digest_algorithm |
| [bool](class_bool.md#class_bool) | codesign/enable |
| [String](class_string.md#class_String) | codesign/identity |
| [int](class_int.md#class_int) | codesign/identity_type |
| [String](class_string.md#class_String) | codesign/password |
| [bool](class_bool.md#class_bool) | codesign/timestamp |
| [String](class_string.md#class_String) | codesign/timestamp_server_url |
| [String](class_string.md#class_String) | custom_template/debug |
| [String](class_string.md#class_String) | custom_template/release |
| [int](class_int.md#class_int) | debug/export_console_wrapper |
| [bool](class_bool.md#class_bool) | shader_baker/enabled |
| [String](class_string.md#class_String) | ssh_remote_deploy/cleanup_script |
| [bool](class_bool.md#class_bool) | ssh_remote_deploy/enabled |
| [String](class_string.md#class_String) | ssh_remote_deploy/extra_args_scp |
| [String](class_string.md#class_String) | ssh_remote_deploy/extra_args_ssh |
| [String](class_string.md#class_String) | ssh_remote_deploy/host |
| [String](class_string.md#class_String) | ssh_remote_deploy/port |
| [String](class_string.md#class_String) | ssh_remote_deploy/run_script |
| [bool](class_bool.md#class_bool) | texture_format/etc2_astc |
| [bool](class_bool.md#class_bool) | texture_format/s3tc_bptc |

---

### Property Descriptions

.. _class_EditorExportPlatformWindows_property_application/company_name:

[String](class_string.md#class_String) **application/company_name** 🔗

Company that produced the application. Required. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/console_wrapper_icon:

[String](class_string.md#class_String) **application/console_wrapper_icon** 🔗

Console wrapper icon file. If left empty, it will fallback to application/icon, then to ProjectSettings.application/config/windows_native_icon, and lastly, ProjectSettings.application/config/icon.

---

.. _class_EditorExportPlatformWindows_property_application/copyright:

[String](class_string.md#class_String) **application/copyright** 🔗

Copyright notice for the bundle visible to the user. Optional. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/d3d12_agility_sdk_multiarch:

[bool](class_bool.md#class_bool) **application/d3d12_agility_sdk_multiarch** 🔗

If `true`, and application/export_d3d12 is set, the Agility SDK DLLs will be stored in arch-specific subdirectories.

---

.. _class_EditorExportPlatformWindows_property_application/export_angle:

[int](class_int.md#class_int) **application/export_angle** 🔗

If set to `1`, ANGLE libraries are exported with the exported application. If set to `0`, ANGLE libraries are exported only if ProjectSettings.rendering/gl_compatibility/driver is set to `"opengl3_angle"`.

---

.. _class_EditorExportPlatformWindows_property_application/export_d3d12:

[int](class_int.md#class_int) **application/export_d3d12** 🔗

If set to `1`, the Direct3D 12 runtime libraries (Agility SDK, PIX) are exported with the exported application. If set to `0`, Direct3D 12 libraries are exported only if ProjectSettings.rendering/rendering_device/driver is set to `"d3d12"`.

---

.. _class_EditorExportPlatformWindows_property_application/file_description:

[String](class_string.md#class_String) **application/file_description** 🔗

File description to be presented to users. Required. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/file_version:

[String](class_string.md#class_String) **application/file_version** 🔗

Version number of the file. Falls back to ProjectSettings.application/config/version if left empty. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/icon:

[String](class_string.md#class_String) **application/icon** 🔗

Application icon file. If left empty, it will fallback to ProjectSettings.application/config/windows_native_icon, and then to ProjectSettings.application/config/icon.

---

.. _class_EditorExportPlatformWindows_property_application/icon_interpolation:

[int](class_int.md#class_int) **application/icon_interpolation** 🔗

Interpolation method used to resize application icon.

---

.. _class_EditorExportPlatformWindows_property_application/modify_resources:

[bool](class_bool.md#class_bool) **application/modify_resources** 🔗

If enabled, icon and metadata of the exported executable is set according to the other `application/*` values.

---

.. _class_EditorExportPlatformWindows_property_application/product_name:

[String](class_string.md#class_String) **application/product_name** 🔗

Name of the application. Required. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/product_version:

[String](class_string.md#class_String) **application/product_version** 🔗

Application version visible to the user. Falls back to ProjectSettings.application/config/version if left empty. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_application/trademarks:

[String](class_string.md#class_String) **application/trademarks** 🔗

Trademarks and registered trademarks that apply to the file. Optional. See StringFileInfo.

---

.. _class_EditorExportPlatformWindows_property_binary_format/architecture:

[String](class_string.md#class_String) **binary_format/architecture** 🔗

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, and `arm64`.

---

.. _class_EditorExportPlatformWindows_property_binary_format/embed_pck:

[bool](class_bool.md#class_bool) **binary_format/embed_pck** 🔗

If `true`, project resources are embedded into the executable.

---

.. _class_EditorExportPlatformWindows_property_codesign/custom_options:

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **codesign/custom_options** 🔗

Array of the additional command line arguments passed to the code signing tool. See Sign Tool.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

.. _class_EditorExportPlatformWindows_property_codesign/description:

[String](class_string.md#class_String) **codesign/description** 🔗

Description of the signed content. See Sign Tool.

---

.. _class_EditorExportPlatformWindows_property_codesign/digest_algorithm:

[int](class_int.md#class_int) **codesign/digest_algorithm** 🔗

Digest algorithm to use for creating signature. See Sign Tool.

---

.. _class_EditorExportPlatformWindows_property_codesign/enable:

[bool](class_bool.md#class_bool) **codesign/enable** 🔗

If `true`, executable signing is enabled.

---

.. _class_EditorExportPlatformWindows_property_codesign/identity:

[String](class_string.md#class_String) **codesign/identity** 🔗

PKCS #12 certificate file used to sign executable or certificate SHA-1 hash (if codesign/identity_type is set to "Use certificate store"). See Sign Tool.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY`.

---

.. _class_EditorExportPlatformWindows_property_codesign/identity_type:

[int](class_int.md#class_int) **codesign/identity_type** 🔗

Type of identity to use. See Sign Tool.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY_TYPE`.

---

.. _class_EditorExportPlatformWindows_property_codesign/password:

[String](class_string.md#class_String) **codesign/password** 🔗

Password for the certificate file used to sign executable. See Sign Tool.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_PASSWORD`.

---

.. _class_EditorExportPlatformWindows_property_codesign/timestamp:

[bool](class_bool.md#class_bool) **codesign/timestamp** 🔗

If `true`, time-stamp is added to the signature. See Sign Tool.

---

.. _class_EditorExportPlatformWindows_property_codesign/timestamp_server_url:

[String](class_string.md#class_String) **codesign/timestamp_server_url** 🔗

URL of the time stamp server. If left empty, the default server is used. See Sign Tool.

---

.. _class_EditorExportPlatformWindows_property_custom_template/debug:

[String](class_string.md#class_String) **custom_template/debug** 🔗

Path to the custom export template. If left empty, default template is used.

---

.. _class_EditorExportPlatformWindows_property_custom_template/release:

[String](class_string.md#class_String) **custom_template/release** 🔗

Path to the custom export template. If left empty, default template is used.

---

.. _class_EditorExportPlatformWindows_property_debug/export_console_wrapper:

[int](class_int.md#class_int) **debug/export_console_wrapper** 🔗

If `true`, a console wrapper executable is exported alongside the main executable, which allows running the project with enabled console output.

---

.. _class_EditorExportPlatformWindows_property_shader_baker/enabled:

[bool](class_bool.md#class_bool) **shader_baker/enabled** 🔗

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ and Mobile renderers.

 **Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/cleanup_script:

[String](class_string.md#class_String) **ssh_remote_deploy/cleanup_script** 🔗

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/enabled:

[bool](class_bool.md#class_bool) **ssh_remote_deploy/enabled** 🔗

Enables remote deploy using SSH/SCP.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_scp:

[String](class_string.md#class_String) **ssh_remote_deploy/extra_args_scp** 🔗

Array of the additional command line arguments passed to the SCP.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_ssh:

[String](class_string.md#class_String) **ssh_remote_deploy/extra_args_ssh** 🔗

Array of the additional command line arguments passed to the SSH.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/host:

[String](class_string.md#class_String) **ssh_remote_deploy/host** 🔗

Remote host SSH user name and address, in `user@address` format.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/port:

[String](class_string.md#class_String) **ssh_remote_deploy/port** 🔗

Remote host SSH port number.

---

.. _class_EditorExportPlatformWindows_property_ssh_remote_deploy/run_script:

[String](class_string.md#class_String) **ssh_remote_deploy/run_script** 🔗

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.

---

.. _class_EditorExportPlatformWindows_property_texture_format/etc2_astc:

[bool](class_bool.md#class_bool) **texture_format/etc2_astc** 🔗

If `true`, project textures are exported in the ETC2/ASTC format.

---

.. _class_EditorExportPlatformWindows_property_texture_format/s3tc_bptc:

[bool](class_bool.md#class_bool) **texture_format/s3tc_bptc** 🔗

If `true`, project textures are exported in the S3TC/BPTC format.

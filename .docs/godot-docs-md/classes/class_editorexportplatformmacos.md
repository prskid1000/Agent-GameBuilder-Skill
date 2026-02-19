<span id="class_EditorExportPlatformMacOS"></span>

## EditorExportPlatformMacOS

**Inherits:** [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Exporter for macOS.

### Tutorials

- [Exporting for macOS](../tutorials/export/exporting_for_macos.md)

- [Running Godot apps on macOS](../tutorials/export/running_on_macos.md)

### Properties


| [String](class_string.md#class_String) | application/additional_plist_content |
| --- | --- |
| [String](class_string.md#class_String) | application/app_category |
| [String](class_string.md#class_String) | application/bundle_identifier |
| [String](class_string.md#class_String) | application/copyright |
| [Dictionary](class_dictionary.md#class_Dictionary) | application/copyright_localized |
| [int](class_int.md#class_int) | application/export_angle |
| [String](class_string.md#class_String) | application/icon |
| [int](class_int.md#class_int) | application/icon_interpolation |
| [String](class_string.md#class_String) | application/liquid_glass_icon |
| [String](class_string.md#class_String) | application/min_macos_version_arm64 |
| [String](class_string.md#class_String) | application/min_macos_version_x86_64 |
| [String](class_string.md#class_String) | application/short_version |
| [String](class_string.md#class_String) | application/signature |
| [String](class_string.md#class_String) | application/version |
| [String](class_string.md#class_String) | binary_format/architecture |
| [String](class_string.md#class_String) | codesign/apple_team_id |
| [String](class_string.md#class_String) | codesign/certificate_file |
| [String](class_string.md#class_String) | codesign/certificate_password |
| [int](class_int.md#class_int) | codesign/codesign |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | codesign/custom_options |
| [String](class_string.md#class_String) | codesign/entitlements/additional |
| [bool](class_bool.md#class_bool) | codesign/entitlements/address_book |
| [bool](class_bool.md#class_bool) | codesign/entitlements/allow_dyld_environment_variables |
| [bool](class_bool.md#class_bool) | codesign/entitlements/allow_jit_code_execution |
| [bool](class_bool.md#class_bool) | codesign/entitlements/allow_unsigned_executable_memory |
| [bool](class_bool.md#class_bool) | codesign/entitlements/app_sandbox/device_bluetooth |
| [bool](class_bool.md#class_bool) | codesign/entitlements/app_sandbox/device_usb |
| [bool](class_bool.md#class_bool) | codesign/entitlements/app_sandbox/enabled |
| [int](class_int.md#class_int) | codesign/entitlements/app_sandbox/files_downloads |
| [int](class_int.md#class_int) | codesign/entitlements/app_sandbox/files_movies |
| [int](class_int.md#class_int) | codesign/entitlements/app_sandbox/files_music |
| [int](class_int.md#class_int) | codesign/entitlements/app_sandbox/files_pictures |
| [int](class_int.md#class_int) | codesign/entitlements/app_sandbox/files_user_selected |
| [Array](class_array.md#class_Array) | codesign/entitlements/app_sandbox/helper_executables |
| [bool](class_bool.md#class_bool) | codesign/entitlements/app_sandbox/network_client |
| [bool](class_bool.md#class_bool) | codesign/entitlements/app_sandbox/network_server |
| [bool](class_bool.md#class_bool) | codesign/entitlements/apple_events |
| [bool](class_bool.md#class_bool) | codesign/entitlements/audio_input |
| [bool](class_bool.md#class_bool) | codesign/entitlements/calendars |
| [bool](class_bool.md#class_bool) | codesign/entitlements/camera |
| [String](class_string.md#class_String) | codesign/entitlements/custom_file |
| [bool](class_bool.md#class_bool) | codesign/entitlements/debugging |
| [bool](class_bool.md#class_bool) | codesign/entitlements/disable_library_validation |
| [bool](class_bool.md#class_bool) | codesign/entitlements/location |
| [bool](class_bool.md#class_bool) | codesign/entitlements/photos_library |
| [String](class_string.md#class_String) | codesign/identity |
| [String](class_string.md#class_String) | codesign/installer_identity |
| [String](class_string.md#class_String) | codesign/provisioning_profile |
| [String](class_string.md#class_String) | custom_template/debug |
| [String](class_string.md#class_String) | custom_template/release |
| [int](class_int.md#class_int) | debug/export_console_wrapper |
| [bool](class_bool.md#class_bool) | display/high_res |
| [int](class_int.md#class_int) | export/distribution_type |
| [String](class_string.md#class_String) | notarization/api_key |
| [String](class_string.md#class_String) | notarization/api_key_id |
| [String](class_string.md#class_String) | notarization/api_uuid |
| [String](class_string.md#class_String) | notarization/apple_id_name |
| [String](class_string.md#class_String) | notarization/apple_id_password |
| [int](class_int.md#class_int) | notarization/notarization |
| [String](class_string.md#class_String) | privacy/address_book_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/address_book_usage_description_localized |
| [String](class_string.md#class_String) | privacy/calendar_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/calendar_usage_description_localized |
| [String](class_string.md#class_String) | privacy/camera_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/camera_usage_description_localized |
| [bool](class_bool.md#class_bool) | privacy/collected_data/advertising_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/advertising_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/advertising_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/advertising_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/audio_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/audio_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/audio_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/audio_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/browsing_history/collected |
| [int](class_int.md#class_int) | privacy/collected_data/browsing_history/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/browsing_history/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/browsing_history/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/coarse_location/collected |
| [int](class_int.md#class_int) | privacy/collected_data/coarse_location/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/coarse_location/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/coarse_location/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/contacts/collected |
| [int](class_int.md#class_int) | privacy/collected_data/contacts/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/contacts/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/contacts/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/crash_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/crash_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/crash_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/crash_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/credit_info/collected |
| [int](class_int.md#class_int) | privacy/collected_data/credit_info/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/credit_info/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/credit_info/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/customer_support/collected |
| [int](class_int.md#class_int) | privacy/collected_data/customer_support/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/customer_support/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/customer_support/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/device_id/collected |
| [int](class_int.md#class_int) | privacy/collected_data/device_id/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/device_id/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/device_id/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/email_address/collected |
| [int](class_int.md#class_int) | privacy/collected_data/email_address/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/email_address/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/email_address/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/emails_or_text_messages/collected |
| [int](class_int.md#class_int) | privacy/collected_data/emails_or_text_messages/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/emails_or_text_messages/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/emails_or_text_messages/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/environment_scanning/collected |
| [int](class_int.md#class_int) | privacy/collected_data/environment_scanning/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/environment_scanning/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/environment_scanning/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/fitness/collected |
| [int](class_int.md#class_int) | privacy/collected_data/fitness/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/fitness/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/fitness/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/gameplay_content/collected |
| [int](class_int.md#class_int) | privacy/collected_data/gameplay_content/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/gameplay_content/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/gameplay_content/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/hands/collected |
| [int](class_int.md#class_int) | privacy/collected_data/hands/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/hands/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/hands/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/head/collected |
| [int](class_int.md#class_int) | privacy/collected_data/head/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/head/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/head/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/health/collected |
| [int](class_int.md#class_int) | privacy/collected_data/health/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/health/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/health/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/name/collected |
| [int](class_int.md#class_int) | privacy/collected_data/name/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/name/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/name/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_contact_info/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_contact_info/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_contact_info/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_contact_info/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_data_types/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_data_types/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_data_types/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_data_types/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_diagnostic_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_diagnostic_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_diagnostic_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_diagnostic_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_financial_info/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_financial_info/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_financial_info/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_financial_info/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_usage_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_usage_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_usage_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_usage_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_user_content/collected |
| [int](class_int.md#class_int) | privacy/collected_data/other_user_content/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_user_content/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/other_user_content/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/payment_info/collected |
| [int](class_int.md#class_int) | privacy/collected_data/payment_info/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/payment_info/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/payment_info/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/performance_data/collected |
| [int](class_int.md#class_int) | privacy/collected_data/performance_data/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/performance_data/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/performance_data/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/phone_number/collected |
| [int](class_int.md#class_int) | privacy/collected_data/phone_number/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/phone_number/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/phone_number/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/photos_or_videos/collected |
| [int](class_int.md#class_int) | privacy/collected_data/photos_or_videos/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/photos_or_videos/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/photos_or_videos/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/physical_address/collected |
| [int](class_int.md#class_int) | privacy/collected_data/physical_address/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/physical_address/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/physical_address/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/precise_location/collected |
| [int](class_int.md#class_int) | privacy/collected_data/precise_location/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/precise_location/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/precise_location/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/product_interaction/collected |
| [int](class_int.md#class_int) | privacy/collected_data/product_interaction/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/product_interaction/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/product_interaction/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/purchase_history/collected |
| [int](class_int.md#class_int) | privacy/collected_data/purchase_history/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/purchase_history/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/purchase_history/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/search_history/collected |
| [int](class_int.md#class_int) | privacy/collected_data/search_history/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/search_history/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/search_history/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/sensitive_info/collected |
| [int](class_int.md#class_int) | privacy/collected_data/sensitive_info/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/sensitive_info/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/sensitive_info/used_for_tracking |
| [bool](class_bool.md#class_bool) | privacy/collected_data/user_id/collected |
| [int](class_int.md#class_int) | privacy/collected_data/user_id/collection_purposes |
| [bool](class_bool.md#class_bool) | privacy/collected_data/user_id/linked_to_user |
| [bool](class_bool.md#class_bool) | privacy/collected_data/user_id/used_for_tracking |
| [String](class_string.md#class_String) | privacy/desktop_folder_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/desktop_folder_usage_description_localized |
| [String](class_string.md#class_String) | privacy/documents_folder_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/documents_folder_usage_description_localized |
| [String](class_string.md#class_String) | privacy/downloads_folder_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/downloads_folder_usage_description_localized |
| [String](class_string.md#class_String) | privacy/location_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/location_usage_description_localized |
| [String](class_string.md#class_String) | privacy/microphone_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/microphone_usage_description_localized |
| [String](class_string.md#class_String) | privacy/network_volumes_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/network_volumes_usage_description_localized |
| [String](class_string.md#class_String) | privacy/photos_library_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/photos_library_usage_description_localized |
| [String](class_string.md#class_String) | privacy/removable_volumes_usage_description |
| [Dictionary](class_dictionary.md#class_Dictionary) | privacy/removable_volumes_usage_description_localized |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | privacy/tracking_domains |
| [bool](class_bool.md#class_bool) | privacy/tracking_enabled |
| [bool](class_bool.md#class_bool) | shader_baker/enabled |
| [String](class_string.md#class_String) | ssh_remote_deploy/cleanup_script |
| [bool](class_bool.md#class_bool) | ssh_remote_deploy/enabled |
| [String](class_string.md#class_String) | ssh_remote_deploy/extra_args_scp |
| [String](class_string.md#class_String) | ssh_remote_deploy/extra_args_ssh |
| [String](class_string.md#class_String) | ssh_remote_deploy/host |
| [String](class_string.md#class_String) | ssh_remote_deploy/port |
| [String](class_string.md#class_String) | ssh_remote_deploy/run_script |
| [String](class_string.md#class_String) | xcode/platform_build |
| [String](class_string.md#class_String) | xcode/sdk_build |
| [String](class_string.md#class_String) | xcode/sdk_name |
| [String](class_string.md#class_String) | xcode/sdk_version |
| [String](class_string.md#class_String) | xcode/xcode_build |
| [String](class_string.md#class_String) | xcode/xcode_version |

---

### Property Descriptions

.. _class_EditorExportPlatformMacOS_property_application/additional_plist_content:

[String](class_string.md#class_String) **application/additional_plist_content** 🔗

Additional data added to the root `<dict>` section of the Info.plist file. The value should be an XML section with pairs of key-value elements, e.g.:

.. code:: text

    <key>key_name</key>
    <string>value</string>

---

.. _class_EditorExportPlatformMacOS_property_application/app_category:

[String](class_string.md#class_String) **application/app_category** 🔗

Application category for the App Store.

---

.. _class_EditorExportPlatformMacOS_property_application/bundle_identifier:

[String](class_string.md#class_String) **application/bundle_identifier** 🔗

Unique application identifier in a reverse-DNS format, can only contain alphanumeric characters (`A-Z`, `a-z`, and `0-9`), hyphens (`-`), and periods (`.`).

---

.. _class_EditorExportPlatformMacOS_property_application/copyright:

[String](class_string.md#class_String) **application/copyright** 🔗

Copyright notice for the bundle visible to the user (in English).

---

.. _class_EditorExportPlatformMacOS_property_application/copyright_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **application/copyright_localized** 🔗

Copyright notice for the bundle visible to the user (localized).

---

.. _class_EditorExportPlatformMacOS_property_application/export_angle:

[int](class_int.md#class_int) **application/export_angle** 🔗

If set to `1`, ANGLE libraries are exported with the exported application. If set to `0`, ANGLE libraries are exported only if ProjectSettings.rendering/gl_compatibility/driver is set to `"opengl3_angle"`.

---

.. _class_EditorExportPlatformMacOS_property_application/icon:

[String](class_string.md#class_String) **application/icon** 🔗

Application icon file. If left empty, it will fallback to ProjectSettings.application/config/macos_native_icon, and then to ProjectSettings.application/config/icon.

---

.. _class_EditorExportPlatformMacOS_property_application/icon_interpolation:

[int](class_int.md#class_int) **application/icon_interpolation** 🔗

Interpolation method used to resize application icon.

---

.. _class_EditorExportPlatformMacOS_property_application/liquid_glass_icon:

[String](class_string.md#class_String) **application/liquid_glass_icon** 🔗

macOS 26 Liquid Glass icon source file. Use Icon Composer to create Liquid Glass icons.

 **Note:** Supported when exporting from macOS only, Xcode 26+ required.

 **Note:** Liquid Glass icons are supported on macOS 26 only, use application/icon to set the icon for older macOS versions.

---

.. _class_EditorExportPlatformMacOS_property_application/min_macos_version_arm64:

[String](class_string.md#class_String) **application/min_macos_version_arm64** 🔗

Minimum version of macOS required for this application to run on Apple Silicon Macs, in the `major.minor.patch` or `major.minor` format, can only contain numeric characters (`0-9`) and periods (`.`).

---

.. _class_EditorExportPlatformMacOS_property_application/min_macos_version_x86_64:

[String](class_string.md#class_String) **application/min_macos_version_x86_64** 🔗

Minimum version of macOS required for this application to run on Intel Macs, in the `major.minor.patch` or `major.minor` format, can only contain numeric characters (`0-9`) and periods (`.`).

---

.. _class_EditorExportPlatformMacOS_property_application/short_version:

[String](class_string.md#class_String) **application/short_version** 🔗

Application version visible to the user. Can only contain numeric characters (`0-9`) and periods (`.`). Falls back to ProjectSettings.application/config/version if left empty.

 **Note:** This value is used for the *Identity > Version* value in the generated Xcode project.

---

.. _class_EditorExportPlatformMacOS_property_application/signature:

[String](class_string.md#class_String) **application/signature** 🔗

A four-character creator code that is specific to the bundle. Optional.

---

.. _class_EditorExportPlatformMacOS_property_application/version:

[String](class_string.md#class_String) **application/version** 🔗

Machine-readable application version in the `major.minor.patch` format. Can only contain numeric characters (`0-9`) and periods (`.`). This must be incremented with every new release pushed to the App Store. Falls back to ProjectSettings.application/config/version if left empty.

 **Note:** This value is used for the *Identity > Build* value in the generated Xcode project.

---

.. _class_EditorExportPlatformMacOS_property_binary_format/architecture:

[String](class_string.md#class_String) **binary_format/architecture** 🔗

Application executable architecture.

Supported architectures: `x86_64`, `arm64`, and `universal` (`x86_64 + arm64`).

Official export templates include `universal` binaries only.

---

.. _class_EditorExportPlatformMacOS_property_codesign/apple_team_id:

[String](class_string.md#class_String) **codesign/apple_team_id** 🔗

Apple Team ID, unique 10-character string. To locate your Team ID check "Membership details" section in your Apple developer account dashboard, or "Organizational Unit" of your code signing certificate. See Locate your Team ID.

---

.. _class_EditorExportPlatformMacOS_property_codesign/certificate_file:

[String](class_string.md#class_String) **codesign/certificate_file** 🔗

PKCS #12 certificate file used to sign `.app` bundle.

Can be overridden with the environment variable `GODOT_MACOS_CODESIGN_CERTIFICATE_FILE`.

---

.. _class_EditorExportPlatformMacOS_property_codesign/certificate_password:

[String](class_string.md#class_String) **codesign/certificate_password** 🔗

Password for the certificate file used to sign `.app` bundle.

Can be overridden with the environment variable `GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD`.

---

.. _class_EditorExportPlatformMacOS_property_codesign/codesign:

[int](class_int.md#class_int) **codesign/codesign** 🔗

Tool to use for code signing.

---

.. _class_EditorExportPlatformMacOS_property_codesign/custom_options:

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **codesign/custom_options** 🔗

Array of the additional command line arguments passed to the code signing tool.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/additional:

[String](class_string.md#class_String) **codesign/entitlements/additional** 🔗

Additional data added to the root `<dict>` section of the .entitlements file. The value should be an XML section with pairs of key-value elements, for example:

.. code:: text

    <key>key_name</key>
    <string>value</string>

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/address_book:

[bool](class_bool.md#class_bool) **codesign/entitlements/address_book** 🔗

Enable to allow access to contacts in the user's address book, if it's enabled you should also provide usage message in the privacy/address_book_usage_description option. See com.apple.security.personal-information.addressbook.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_dyld_environment_variables:

[bool](class_bool.md#class_bool) **codesign/entitlements/allow_dyld_environment_variables** 🔗

Allows app to use dynamic linker environment variables to inject code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. See com.apple.security.cs.allow-dyld-environment-variables.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_jit_code_execution:

[bool](class_bool.md#class_bool) **codesign/entitlements/allow_jit_code_execution** 🔗

Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. See com.apple.security.cs.allow-jit.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_unsigned_executable_memory:

[bool](class_bool.md#class_bool) **codesign/entitlements/allow_unsigned_executable_memory** 🔗

Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. See com.apple.security.cs.allow-unsigned-executable-memory.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_bluetooth:

[bool](class_bool.md#class_bool) **codesign/entitlements/app_sandbox/device_bluetooth** 🔗

Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers. See com.apple.security.device.bluetooth.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_usb:

[bool](class_bool.md#class_bool) **codesign/entitlements/app_sandbox/device_usb** 🔗

Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers. See com.apple.security.device.usb.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/enabled:

[bool](class_bool.md#class_bool) **codesign/entitlements/app_sandbox/enabled** 🔗

Enables App Sandbox. The App Sandbox restricts access to user data, networking, and devices. Sandboxed apps can't access most of the file system, can't use custom file dialogs and execute binaries outside the .app bundle. See App Sandbox.

 **Note:** To distribute an app through the App Store, you must enable the App Sandbox.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_downloads:

[int](class_int.md#class_int) **codesign/entitlements/app_sandbox/files_downloads** 🔗

Allows read or write access to the user's "Downloads" folder. See com.apple.security.files.downloads.read-write.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_movies:

[int](class_int.md#class_int) **codesign/entitlements/app_sandbox/files_movies** 🔗

Allows read or write access to the user's "Movies" folder. See com.apple.security.files.movies.read-write.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_music:

[int](class_int.md#class_int) **codesign/entitlements/app_sandbox/files_music** 🔗

Allows read or write access to the user's "Music" folder. See com.apple.security.files.music.read-write.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_pictures:

[int](class_int.md#class_int) **codesign/entitlements/app_sandbox/files_pictures** 🔗

Allows read or write access to the user's "Pictures" folder. See com.apple.security.files.pictures.read-write.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_user_selected:

[int](class_int.md#class_int) **codesign/entitlements/app_sandbox/files_user_selected** 🔗

Allows read or write access to the locations the user has selected using a native file dialog. See com.apple.security.files.user-selected.read-write.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/helper_executables:

[Array](class_array.md#class_Array) **codesign/entitlements/app_sandbox/helper_executables** 🔗

List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable. See Embedding a command-line tool in a sandboxed app.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_client:

[bool](class_bool.md#class_bool) **codesign/entitlements/app_sandbox/network_client** 🔗

Enable to allow app to establish outgoing network connections. See com.apple.security.network.client.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_server:

[bool](class_bool.md#class_bool) **codesign/entitlements/app_sandbox/network_server** 🔗

Enable to allow app to listen for incoming network connections. See com.apple.security.network.server.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/apple_events:

[bool](class_bool.md#class_bool) **codesign/entitlements/apple_events** 🔗

Enable to allow app to send Apple events to other apps. See com.apple.security.automation.apple-events.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/audio_input:

[bool](class_bool.md#class_bool) **codesign/entitlements/audio_input** 🔗

Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in the privacy/microphone_usage_description option. See com.apple.security.device.audio-input.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/calendars:

[bool](class_bool.md#class_bool) **codesign/entitlements/calendars** 🔗

Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in the privacy/calendar_usage_description option. See com.apple.security.personal-information.calendars.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/camera:

[bool](class_bool.md#class_bool) **codesign/entitlements/camera** 🔗

Enable if you need to use the camera, if it's enabled you should also provide usage message in the privacy/camera_usage_description option. See com.apple.security.device.camera.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/custom_file:

[String](class_string.md#class_String) **codesign/entitlements/custom_file** 🔗

Custom entitlements `.plist` file, if specified the rest of entitlements in the export config are ignored.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/debugging:

[bool](class_bool.md#class_bool) **codesign/entitlements/debugging** 🔗

You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export. See Embedding a command-line tool in a sandboxed app.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/disable_library_validation:

[bool](class_bool.md#class_bool) **codesign/entitlements/disable_library_validation** 🔗

Allows app to load arbitrary libraries and frameworks (not signed with the same Team ID as the main executable or by Apple). Enable it if you are using GDExtension add-ons or ad-hoc signing, or want to support user-provided external add-ons. See com.apple.security.cs.disable-library-validation.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/location:

[bool](class_bool.md#class_bool) **codesign/entitlements/location** 🔗

Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in the privacy/location_usage_description option. See com.apple.security.personal-information.location.

---

.. _class_EditorExportPlatformMacOS_property_codesign/entitlements/photos_library:

[bool](class_bool.md#class_bool) **codesign/entitlements/photos_library** 🔗

Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in the privacy/photos_library_usage_description option. See com.apple.security.personal-information.photos-library.

---

.. _class_EditorExportPlatformMacOS_property_codesign/identity:

[String](class_string.md#class_String) **codesign/identity** 🔗

The "Full Name", "Common Name" or SHA-1 hash of the signing identity used to sign `.app` bundle.

---

.. _class_EditorExportPlatformMacOS_property_codesign/installer_identity:

[String](class_string.md#class_String) **codesign/installer_identity** 🔗

The "Full Name", "Common Name" or SHA-1 hash of the signing identity used to sign `.pkg` installer package for App Store distribution, use `3rd Party Mac Developer Installer: Name.` identity.

---

.. _class_EditorExportPlatformMacOS_property_codesign/provisioning_profile:

[String](class_string.md#class_String) **codesign/provisioning_profile** 🔗

Provisioning profile file downloaded from Apple developer account dashboard. See Edit, download, or delete provisioning profiles.

Can be overridden with the environment variable `GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE`.

---

.. _class_EditorExportPlatformMacOS_property_custom_template/debug:

[String](class_string.md#class_String) **custom_template/debug** 🔗

Path to the custom export template. If left empty, default template is used.

---

.. _class_EditorExportPlatformMacOS_property_custom_template/release:

[String](class_string.md#class_String) **custom_template/release** 🔗

Path to the custom export template. If left empty, default template is used.

---

.. _class_EditorExportPlatformMacOS_property_debug/export_console_wrapper:

[int](class_int.md#class_int) **debug/export_console_wrapper** 🔗

If enabled, a wrapper that can be used to run the application with console output is created alongside the exported application.

---

.. _class_EditorExportPlatformMacOS_property_display/high_res:

[bool](class_bool.md#class_bool) **display/high_res** 🔗

If `true`, the application is rendered at native display resolution, otherwise it is always rendered at loDPI resolution and upscaled by OS when required.

---

.. _class_EditorExportPlatformMacOS_property_export/distribution_type:

[int](class_int.md#class_int) **export/distribution_type** 🔗

Application distribution target.

---

.. _class_EditorExportPlatformMacOS_property_notarization/api_key:

[String](class_string.md#class_String) **notarization/api_key** 🔗

Apple App Store Connect API issuer key file.

Can be overridden with the environment variable `GODOT_MACOS_NOTARIZATION_API_KEY`.

---

.. _class_EditorExportPlatformMacOS_property_notarization/api_key_id:

[String](class_string.md#class_String) **notarization/api_key_id** 🔗

Apple App Store Connect API issuer key ID.

Can be overridden with the environment variable `GODOT_MACOS_NOTARIZATION_API_KEY_ID`.

---

.. _class_EditorExportPlatformMacOS_property_notarization/api_uuid:

[String](class_string.md#class_String) **notarization/api_uuid** 🔗

Apple App Store Connect API issuer UUID.

Can be overridden with the environment variable `GODOT_MACOS_NOTARIZATION_API_UUID`.

---

.. _class_EditorExportPlatformMacOS_property_notarization/apple_id_name:

[String](class_string.md#class_String) **notarization/apple_id_name** 🔗

Apple ID account name (email address).

Can be overridden with the environment variable `GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME`.

---

.. _class_EditorExportPlatformMacOS_property_notarization/apple_id_password:

[String](class_string.md#class_String) **notarization/apple_id_password** 🔗

Apple ID app-specific password.

Can be overridden with the environment variable `GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD`.

---

.. _class_EditorExportPlatformMacOS_property_notarization/notarization:

[int](class_int.md#class_int) **notarization/notarization** 🔗

Tool to use for notarization.

---

.. _class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description:

[String](class_string.md#class_String) **privacy/address_book_usage_description** 🔗

A message displayed when requesting access to the user's contacts (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/address_book_usage_description_localized** 🔗

A message displayed when requesting access to the user's contacts (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description:

[String](class_string.md#class_String) **privacy/calendar_usage_description** 🔗

A message displayed when requesting access to the user's calendar data (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/calendar_usage_description_localized** 🔗

A message displayed when requesting access to the user's calendar data (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/camera_usage_description:

[String](class_string.md#class_String) **privacy/camera_usage_description** 🔗

A message displayed when requesting access to the device's camera (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/camera_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/camera_usage_description_localized** 🔗

A message displayed when requesting access to the device's camera (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/advertising_data/collected** 🔗

Indicates whether your app collects advertising data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/advertising_data/collection_purposes** 🔗

The reasons your app collects advertising data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/advertising_data/linked_to_user** 🔗

Indicates whether your app links advertising data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/advertising_data/used_for_tracking** 🔗

Indicates whether your app uses advertising data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/audio_data/collected** 🔗

Indicates whether your app collects audio data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/audio_data/collection_purposes** 🔗

The reasons your app collects audio data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/audio_data/linked_to_user** 🔗

Indicates whether your app links audio data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/audio_data/used_for_tracking** 🔗

Indicates whether your app uses audio data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/browsing_history/collected** 🔗

Indicates whether your app collects browsing history.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/browsing_history/collection_purposes** 🔗

The reasons your app collects browsing history. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/browsing_history/linked_to_user** 🔗

Indicates whether your app links browsing history to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/browsing_history/used_for_tracking** 🔗

Indicates whether your app uses browsing history for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/coarse_location/collected** 🔗

Indicates whether your app collects coarse location data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/coarse_location/collection_purposes** 🔗

The reasons your app collects coarse location data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/coarse_location/linked_to_user** 🔗

Indicates whether your app links coarse location data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/coarse_location/used_for_tracking** 🔗

Indicates whether your app uses coarse location data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/contacts/collected** 🔗

Indicates whether your app collects contacts.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/contacts/collection_purposes** 🔗

The reasons your app collects contacts. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/contacts/linked_to_user** 🔗

Indicates whether your app links contacts to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/contacts/used_for_tracking** 🔗

Indicates whether your app uses contacts for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/crash_data/collected** 🔗

Indicates whether your app collects crash data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/crash_data/collection_purposes** 🔗

The reasons your app collects crash data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/crash_data/linked_to_user** 🔗

Indicates whether your app links crash data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/crash_data/used_for_tracking** 🔗

Indicates whether your app uses crash data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/credit_info/collected** 🔗

Indicates whether your app collects credit information.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/credit_info/collection_purposes** 🔗

The reasons your app collects credit information. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/credit_info/linked_to_user** 🔗

Indicates whether your app links credit information to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/credit_info/used_for_tracking** 🔗

Indicates whether your app uses credit information for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/customer_support/collected** 🔗

Indicates whether your app collects customer support data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/customer_support/collection_purposes** 🔗

The reasons your app collects customer support data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/customer_support/linked_to_user** 🔗

Indicates whether your app links customer support data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/customer_support/used_for_tracking** 🔗

Indicates whether your app uses customer support data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/device_id/collected** 🔗

Indicates whether your app collects device IDs.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/device_id/collection_purposes** 🔗

The reasons your app collects device IDs. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/device_id/linked_to_user** 🔗

Indicates whether your app links device IDs to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/device_id/used_for_tracking** 🔗

Indicates whether your app uses device IDs for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/email_address/collected** 🔗

Indicates whether your app collects email address.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/email_address/collection_purposes** 🔗

The reasons your app collects email address. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/email_address/linked_to_user** 🔗

Indicates whether your app links email address to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/email_address/used_for_tracking** 🔗

Indicates whether your app uses email address for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/emails_or_text_messages/collected** 🔗

Indicates whether your app collects emails or text messages.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/emails_or_text_messages/collection_purposes** 🔗

The reasons your app collects emails or text messages. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/emails_or_text_messages/linked_to_user** 🔗

Indicates whether your app links emails or text messages to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/emails_or_text_messages/used_for_tracking** 🔗

Indicates whether your app uses emails or text messages for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/environment_scanning/collected** 🔗

Indicates whether your app collects environment scanning data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/environment_scanning/collection_purposes** 🔗

The reasons your app collects environment scanning data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/environment_scanning/linked_to_user** 🔗

Indicates whether your app links environment scanning data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/environment_scanning/used_for_tracking** 🔗

Indicates whether your app uses environment scanning data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/fitness/collected** 🔗

Indicates whether your app collects fitness and exercise data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/fitness/collection_purposes** 🔗

The reasons your app collects fitness and exercise data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/fitness/linked_to_user** 🔗

Indicates whether your app links fitness and exercise data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/fitness/used_for_tracking** 🔗

Indicates whether your app uses fitness and exercise data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/gameplay_content/collected** 🔗

Indicates whether your app collects gameplay content.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/gameplay_content/collection_purposes** 🔗

The reasons your app collects gameplay content. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/gameplay_content/linked_to_user** 🔗

Indicates whether your app links gameplay content to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/gameplay_content/used_for_tracking** 🔗

Indicates whether your app uses gameplay content for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/hands/collected** 🔗

Indicates whether your app collects user's hand structure and hand movements.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/hands/collection_purposes** 🔗

The reasons your app collects user's hand structure and hand movements. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/hands/linked_to_user** 🔗

Indicates whether your app links user's hand structure and hand movements to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/hands/used_for_tracking** 🔗

Indicates whether your app uses user's hand structure and hand movements for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/head/collected** 🔗

Indicates whether your app collects user's head movement.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/head/collection_purposes** 🔗

The reasons your app collects user's head movement. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/head/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/head/linked_to_user** 🔗

Indicates whether your app links user's head movement to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/head/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/head/used_for_tracking** 🔗

Indicates whether your app uses user's head movement for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/health/collected** 🔗

Indicates whether your app collects health and medical data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/health/collection_purposes** 🔗

The reasons your app collects health and medical data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/health/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/health/linked_to_user** 🔗

Indicates whether your app links health and medical data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/health/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/health/used_for_tracking** 🔗

Indicates whether your app uses health and medical data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/name/collected** 🔗

Indicates whether your app collects user's name.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/name/collection_purposes** 🔗

The reasons your app collects user's name. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/name/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/name/linked_to_user** 🔗

Indicates whether your app links user's name to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/name/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/name/used_for_tracking** 🔗

Indicates whether your app uses user's name for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_contact_info/collected** 🔗

Indicates whether your app collects any other contact information.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_contact_info/collection_purposes** 🔗

The reasons your app collects any other contact information. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_contact_info/linked_to_user** 🔗

Indicates whether your app links any other contact information to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_contact_info/used_for_tracking** 🔗

Indicates whether your app uses any other contact information for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_data_types/collected** 🔗

Indicates whether your app collects any other data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_data_types/collection_purposes** 🔗

The reasons your app collects any other data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_data_types/linked_to_user** 🔗

Indicates whether your app links any other data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_data_types/used_for_tracking** 🔗

Indicates whether your app uses any other data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_diagnostic_data/collected** 🔗

Indicates whether your app collects any other diagnostic data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_diagnostic_data/collection_purposes** 🔗

The reasons your app collects any other diagnostic data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_diagnostic_data/linked_to_user** 🔗

Indicates whether your app links any other diagnostic data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_diagnostic_data/used_for_tracking** 🔗

Indicates whether your app uses any other diagnostic data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_financial_info/collected** 🔗

Indicates whether your app collects any other financial information.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_financial_info/collection_purposes** 🔗

The reasons your app collects any other financial information. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_financial_info/linked_to_user** 🔗

Indicates whether your app links any other financial information to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_financial_info/used_for_tracking** 🔗

Indicates whether your app uses any other financial information for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_usage_data/collected** 🔗

Indicates whether your app collects any other usage data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_usage_data/collection_purposes** 🔗

The reasons your app collects any other usage data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_usage_data/linked_to_user** 🔗

Indicates whether your app links any other usage data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_usage_data/used_for_tracking** 🔗

Indicates whether your app uses any other usage data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_user_content/collected** 🔗

Indicates whether your app collects any other user generated content.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/other_user_content/collection_purposes** 🔗

The reasons your app collects any other user generated content. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_user_content/linked_to_user** 🔗

Indicates whether your app links any other user generated content to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/other_user_content/used_for_tracking** 🔗

Indicates whether your app uses any other user generated content for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/payment_info/collected** 🔗

Indicates whether your app collects payment information.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/payment_info/collection_purposes** 🔗

The reasons your app collects payment information. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/payment_info/linked_to_user** 🔗

Indicates whether your app links payment information to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/payment_info/used_for_tracking** 🔗

Indicates whether your app uses payment information for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/performance_data/collected** 🔗

Indicates whether your app collects performance data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/performance_data/collection_purposes** 🔗

The reasons your app collects performance data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/performance_data/linked_to_user** 🔗

Indicates whether your app links performance data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/performance_data/used_for_tracking** 🔗

Indicates whether your app uses performance data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/phone_number/collected** 🔗

Indicates whether your app collects phone number.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/phone_number/collection_purposes** 🔗

The reasons your app collects phone number. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/phone_number/linked_to_user** 🔗

Indicates whether your app links phone number to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/phone_number/used_for_tracking** 🔗

Indicates whether your app uses phone number for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/photos_or_videos/collected** 🔗

Indicates whether your app collects photos or videos.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/photos_or_videos/collection_purposes** 🔗

The reasons your app collects photos or videos. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/photos_or_videos/linked_to_user** 🔗

Indicates whether your app links photos or videos to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/photos_or_videos/used_for_tracking** 🔗

Indicates whether your app uses photos or videos for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/physical_address/collected** 🔗

Indicates whether your app collects physical address.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/physical_address/collection_purposes** 🔗

The reasons your app collects physical address. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/physical_address/linked_to_user** 🔗

Indicates whether your app links physical address to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/physical_address/used_for_tracking** 🔗

Indicates whether your app uses physical address for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/precise_location/collected** 🔗

Indicates whether your app collects precise location data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/precise_location/collection_purposes** 🔗

The reasons your app collects precise location data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/precise_location/linked_to_user** 🔗

Indicates whether your app links precise location data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/precise_location/used_for_tracking** 🔗

Indicates whether your app uses precise location data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/product_interaction/collected** 🔗

Indicates whether your app collects product interaction data.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/product_interaction/collection_purposes** 🔗

The reasons your app collects product interaction data. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/product_interaction/linked_to_user** 🔗

Indicates whether your app links product interaction data to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/product_interaction/used_for_tracking** 🔗

Indicates whether your app uses product interaction data for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/purchase_history/collected** 🔗

Indicates whether your app collects purchase history.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/purchase_history/collection_purposes** 🔗

The reasons your app collects purchase history. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/purchase_history/linked_to_user** 🔗

Indicates whether your app links purchase history to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/purchase_history/used_for_tracking** 🔗

Indicates whether your app uses purchase history for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/search_history/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/search_history/collected** 🔗

Indicates whether your app collects search history.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/search_history/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/search_history/collection_purposes** 🔗

The reasons your app collects search history. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/search_history/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/search_history/linked_to_user** 🔗

Indicates whether your app links search history to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/search_history/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/search_history/used_for_tracking** 🔗

Indicates whether your app uses search history for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/sensitive_info/collected** 🔗

Indicates whether your app collects sensitive user information.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/sensitive_info/collection_purposes** 🔗

The reasons your app collects sensitive user information. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/sensitive_info/linked_to_user** 🔗

Indicates whether your app links sensitive user information to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/sensitive_info/used_for_tracking** 🔗

Indicates whether your app uses sensitive user information for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collected:

[bool](class_bool.md#class_bool) **privacy/collected_data/user_id/collected** 🔗

Indicates whether your app collects user IDs.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collection_purposes:

[int](class_int.md#class_int) **privacy/collected_data/user_id/collection_purposes** 🔗

The reasons your app collects user IDs. See Describing data use in privacy manifests.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/linked_to_user:

[bool](class_bool.md#class_bool) **privacy/collected_data/user_id/linked_to_user** 🔗

Indicates whether your app links user IDs to the user's identity.

---

.. _class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/used_for_tracking:

[bool](class_bool.md#class_bool) **privacy/collected_data/user_id/used_for_tracking** 🔗

Indicates whether your app uses user IDs for tracking.

---

.. _class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description:

[String](class_string.md#class_String) **privacy/desktop_folder_usage_description** 🔗

A message displayed when requesting access to the user's "Desktop" folder (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/desktop_folder_usage_description_localized** 🔗

A message displayed when requesting access to the user's "Desktop" folder (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description:

[String](class_string.md#class_String) **privacy/documents_folder_usage_description** 🔗

A message displayed when requesting access to the user's "Documents" folder (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/documents_folder_usage_description_localized** 🔗

A message displayed when requesting access to the user's "Documents" folder (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description:

[String](class_string.md#class_String) **privacy/downloads_folder_usage_description** 🔗

A message displayed when requesting access to the user's "Downloads" folder (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/downloads_folder_usage_description_localized** 🔗

A message displayed when requesting access to the user's "Downloads" folder (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/location_usage_description:

[String](class_string.md#class_String) **privacy/location_usage_description** 🔗

A message displayed when requesting access to the user's location information (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/location_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/location_usage_description_localized** 🔗

A message displayed when requesting access to the user's location information (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description:

[String](class_string.md#class_String) **privacy/microphone_usage_description** 🔗

A message displayed when requesting access to the device's microphone (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/microphone_usage_description_localized** 🔗

A message displayed when requesting access to the device's microphone (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description:

[String](class_string.md#class_String) **privacy/network_volumes_usage_description** 🔗

A message displayed when requesting access to the user's network drives (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/network_volumes_usage_description_localized** 🔗

A message displayed when requesting access to the user's network drives (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description:

[String](class_string.md#class_String) **privacy/photos_library_usage_description** 🔗

A message displayed when requesting access to the user's photo library (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/photos_library_usage_description_localized** 🔗

A message displayed when requesting access to the user's photo library (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description:

[String](class_string.md#class_String) **privacy/removable_volumes_usage_description** 🔗

A message displayed when requesting access to the user's removable drives (in English).

---

.. _class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description_localized:

[Dictionary](class_dictionary.md#class_Dictionary) **privacy/removable_volumes_usage_description_localized** 🔗

A message displayed when requesting access to the user's removable drives (localized).

---

.. _class_EditorExportPlatformMacOS_property_privacy/tracking_domains:

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **privacy/tracking_domains** 🔗

The list of internet domains your app connects to that engage in tracking. See Privacy manifest files.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

.. _class_EditorExportPlatformMacOS_property_privacy/tracking_enabled:

[bool](class_bool.md#class_bool) **privacy/tracking_enabled** 🔗

Indicates whether your app uses data for tracking. See Privacy manifest files.

---

.. _class_EditorExportPlatformMacOS_property_shader_baker/enabled:

[bool](class_bool.md#class_bool) **shader_baker/enabled** 🔗

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ or Mobile renderers.

 **Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/cleanup_script:

[String](class_string.md#class_String) **ssh_remote_deploy/cleanup_script** 🔗

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/enabled:

[bool](class_bool.md#class_bool) **ssh_remote_deploy/enabled** 🔗

Enables remote deploy using SSH/SCP.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_scp:

[String](class_string.md#class_String) **ssh_remote_deploy/extra_args_scp** 🔗

Array of the additional command line arguments passed to the SCP.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_ssh:

[String](class_string.md#class_String) **ssh_remote_deploy/extra_args_ssh** 🔗

Array of the additional command line arguments passed to the SSH.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/host:

[String](class_string.md#class_String) **ssh_remote_deploy/host** 🔗

Remote host SSH user name and address, in `user@address` format.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/port:

[String](class_string.md#class_String) **ssh_remote_deploy/port** 🔗

Remote host SSH port number.

---

.. _class_EditorExportPlatformMacOS_property_ssh_remote_deploy/run_script:

[String](class_string.md#class_String) **ssh_remote_deploy/run_script** 🔗

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.

---

.. _class_EditorExportPlatformMacOS_property_xcode/platform_build:

[String](class_string.md#class_String) **xcode/platform_build** 🔗

macOS build number used to build application executable.

---

.. _class_EditorExportPlatformMacOS_property_xcode/sdk_build:

[String](class_string.md#class_String) **xcode/sdk_build** 🔗

macOS SDK build number used to build application executable.

---

.. _class_EditorExportPlatformMacOS_property_xcode/sdk_name:

[String](class_string.md#class_String) **xcode/sdk_name** 🔗

macOS SDK name used to build application executable.

---

.. _class_EditorExportPlatformMacOS_property_xcode/sdk_version:

[String](class_string.md#class_String) **xcode/sdk_version** 🔗

macOS SDK version used to build application executable in the `major.minor` format.

---

.. _class_EditorExportPlatformMacOS_property_xcode/xcode_build:

[String](class_string.md#class_String) **xcode/xcode_build** 🔗

Xcode build number used to build application executable.

---

.. _class_EditorExportPlatformMacOS_property_xcode/xcode_version:

[String](class_string.md#class_String) **xcode/xcode_version** 🔗

Xcode version used to build application executable.

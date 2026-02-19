<span id="class_TranslationServer"></span>

## TranslationServer

**Inherits:** [Object](class_object.md#class_Object)

The server responsible for language translations.

### Description

The translation server is the API backend that manages all language translations.

Translations are stored in [TranslationDomain](class_translationdomain.md#class_TranslationDomain) s, which can be accessed by name. The most commonly used translation domain is the main translation domain. It always exists and can be accessed using an empty [StringName](class_stringname.md#class_StringName). The translation server provides wrapper methods for accessing the main translation domain directly, without having to fetch the translation domain first. Custom translation domains are mainly for advanced usages like editor plugins. Names starting with `godot.` are reserved for engine internals.

### Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)

- [Locales](../tutorials/i18n/locales.md)

### Properties


| [bool](class_bool.md#class_bool) | [pseudolocalization_enabled](class_translationserver.md#class_TranslationServer_property_pseudolocalization_enabled) | `false` |
| --- | --- | --- |

### Methods


| void | [add_translation](class_translationserver.md#class_TranslationServer_method_add_translation) ( translation: [Translation](class_translation.md#class_Translation) ) |
| --- | --- |
| void | [clear](class_translationserver.md#class_TranslationServer_method_clear) ( ) |
| [int](class_int.md#class_int) | [compare_locales](class_translationserver.md#class_TranslationServer_method_compare_locales) ( locale_a: [String](class_string.md#class_String), locale_b: [String](class_string.md#class_String) ) const |
| [Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] | [find_translations](class_translationserver.md#class_TranslationServer_method_find_translations) ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) const |
| [String](class_string.md#class_String) | [format_number](class_translationserver.md#class_TranslationServer_method_format_number) ( number: [String](class_string.md#class_String), locale: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_all_countries](class_translationserver.md#class_TranslationServer_method_get_all_countries) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_all_languages](class_translationserver.md#class_TranslationServer_method_get_all_languages) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_all_scripts](class_translationserver.md#class_TranslationServer_method_get_all_scripts) ( ) const |
| [String](class_string.md#class_String) | [get_country_name](class_translationserver.md#class_TranslationServer_method_get_country_name) ( country: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_language_name](class_translationserver.md#class_TranslationServer_method_get_language_name) ( language: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_loaded_locales](class_translationserver.md#class_TranslationServer_method_get_loaded_locales) ( ) const |
| [String](class_string.md#class_String) | [get_locale](class_translationserver.md#class_TranslationServer_method_get_locale) ( ) const |
| [String](class_string.md#class_String) | [get_locale_name](class_translationserver.md#class_TranslationServer_method_get_locale_name) ( locale: [String](class_string.md#class_String) ) const |
| [TranslationDomain](class_translationdomain.md#class_TranslationDomain) | [get_or_add_domain](class_translationserver.md#class_TranslationServer_method_get_or_add_domain) ( domain: [StringName](class_stringname.md#class_StringName) ) |
| [String](class_string.md#class_String) | [get_percent_sign](class_translationserver.md#class_TranslationServer_method_get_percent_sign) ( locale: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_plural_rules](class_translationserver.md#class_TranslationServer_method_get_plural_rules) ( locale: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_script_name](class_translationserver.md#class_TranslationServer_method_get_script_name) ( script: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_tool_locale](class_translationserver.md#class_TranslationServer_method_get_tool_locale) ( ) |
| [Translation](class_translation.md#class_Translation) | [get_translation_object](class_translationserver.md#class_TranslationServer_method_get_translation_object) ( locale: [String](class_string.md#class_String) ) |
| [Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] | [get_translations](class_translationserver.md#class_TranslationServer_method_get_translations) ( ) const |
| [bool](class_bool.md#class_bool) | [has_domain](class_translationserver.md#class_TranslationServer_method_has_domain) ( domain: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_translation](class_translationserver.md#class_TranslationServer_method_has_translation) ( translation: [Translation](class_translation.md#class_Translation) ) const |
| [bool](class_bool.md#class_bool) | [has_translation_for_locale](class_translationserver.md#class_TranslationServer_method_has_translation_for_locale) ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) const |
| [String](class_string.md#class_String) | [parse_number](class_translationserver.md#class_TranslationServer_method_parse_number) ( number: [String](class_string.md#class_String), locale: [String](class_string.md#class_String) ) const |
| [StringName](class_stringname.md#class_StringName) | [pseudolocalize](class_translationserver.md#class_TranslationServer_method_pseudolocalize) ( message: [StringName](class_stringname.md#class_StringName) ) const |
| void | [reload_pseudolocalization](class_translationserver.md#class_TranslationServer_method_reload_pseudolocalization) ( ) |
| void | [remove_domain](class_translationserver.md#class_TranslationServer_method_remove_domain) ( domain: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_translation](class_translationserver.md#class_TranslationServer_method_remove_translation) ( translation: [Translation](class_translation.md#class_Translation) ) |
| void | [set_locale](class_translationserver.md#class_TranslationServer_method_set_locale) ( locale: [String](class_string.md#class_String) ) |
| [String](class_string.md#class_String) | [standardize_locale](class_translationserver.md#class_TranslationServer_method_standardize_locale) ( locale: [String](class_string.md#class_String), add_defaults: [bool](class_bool.md#class_bool) = false ) const |
| [StringName](class_stringname.md#class_StringName) | [translate](class_translationserver.md#class_TranslationServer_method_translate) ( message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [StringName](class_stringname.md#class_StringName) | [translate_plural](class_translationserver.md#class_TranslationServer_method_translate_plural) ( message: [StringName](class_stringname.md#class_StringName), plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |

---

### Property Descriptions

<span id="class_TranslationServer_property_pseudolocalization_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_enabled** = `false` [🔗](class_translationserver.md#class_TranslationServer_property_pseudolocalization_enabled)

- void **set_pseudolocalization_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_enabled** ( )

If `true`, enables the use of pseudolocalization on the main translation domain. See ProjectSettings.internationalization/pseudolocalization/use_pseudolocalization for details.

---

### Method Descriptions

<span id="class_TranslationServer_method_add_translation"></span>

void **add_translation** ( translation: [Translation](class_translation.md#class_Translation) ) [🔗](class_translationserver.md#class_TranslationServer_method_add_translation)

Adds a translation to the main translation domain.

---

<span id="class_TranslationServer_method_clear"></span>

void **clear** ( ) [🔗](class_translationserver.md#class_TranslationServer_method_clear)

Removes all translations from the main translation domain.

---

<span id="class_TranslationServer_method_compare_locales"></span>

[int](class_int.md#class_int) **compare_locales** ( locale_a: [String](class_string.md#class_String), locale_b: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_compare_locales)

Compares two locales and returns a similarity score between `0` (no match) and `10` (full match).

---

<span id="class_TranslationServer_method_find_translations"></span>

[Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] **find_translations** ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_find_translations)

Returns the [Translation](class_translation.md#class_Translation) instances in the main translation domain that match `locale` (see [compare_locales()](class_translationserver.md#class_TranslationServer_method_compare_locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---

<span id="class_TranslationServer_method_format_number"></span>

[String](class_string.md#class_String) **format_number** ( number: [String](class_string.md#class_String), locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_format_number)

Converts a number from Western Arabic (0..9) to the numeral system used in the given `locale`.

---

<span id="class_TranslationServer_method_get_all_countries"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_all_countries** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_all_countries)

Returns an array of known country codes.

---

<span id="class_TranslationServer_method_get_all_languages"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_all_languages** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_all_languages)

Returns array of known language codes.

---

<span id="class_TranslationServer_method_get_all_scripts"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_all_scripts** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_all_scripts)

Returns an array of known script codes.

---

<span id="class_TranslationServer_method_get_country_name"></span>

[String](class_string.md#class_String) **get_country_name** ( country: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_country_name)

Returns a readable country name for the `country` code.

---

<span id="class_TranslationServer_method_get_language_name"></span>

[String](class_string.md#class_String) **get_language_name** ( language: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_language_name)

Returns a readable language name for the `language` code.

---

<span id="class_TranslationServer_method_get_loaded_locales"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_loaded_locales** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_loaded_locales)

Returns an array of all loaded locales of the project.

---

<span id="class_TranslationServer_method_get_locale"></span>

[String](class_string.md#class_String) **get_locale** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_locale)

Returns the current locale of the project.

See also [OS.get_locale()](class_os.md#class_OS_method_get_locale) and [OS.get_locale_language()](class_os.md#class_OS_method_get_locale_language) to query the locale of the user system.

---

<span id="class_TranslationServer_method_get_locale_name"></span>

[String](class_string.md#class_String) **get_locale_name** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_locale_name)

Returns a locale's language and its variant (e.g. `"en_US"` would return `"English (United States)"`).

---

<span id="class_TranslationServer_method_get_or_add_domain"></span>

[TranslationDomain](class_translationdomain.md#class_TranslationDomain) **get_or_add_domain** ( domain: [StringName](class_stringname.md#class_StringName) ) [🔗](class_translationserver.md#class_TranslationServer_method_get_or_add_domain)

Returns the translation domain with the specified name. An empty translation domain will be created and added if it does not exist.

---

<span id="class_TranslationServer_method_get_percent_sign"></span>

[String](class_string.md#class_String) **get_percent_sign** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_percent_sign)

Returns the percent sign used in the given `locale`.

---

<span id="class_TranslationServer_method_get_plural_rules"></span>

[String](class_string.md#class_String) **get_plural_rules** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_plural_rules)

Returns the default plural rules for the `locale`.

---

<span id="class_TranslationServer_method_get_script_name"></span>

[String](class_string.md#class_String) **get_script_name** ( script: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_script_name)

Returns a readable script name for the `script` code.

---

<span id="class_TranslationServer_method_get_tool_locale"></span>

[String](class_string.md#class_String) **get_tool_locale** ( ) [🔗](class_translationserver.md#class_TranslationServer_method_get_tool_locale)

Returns the current locale of the editor.

 **Note:** When called from an exported project returns the same value as [get_locale()](class_translationserver.md#class_TranslationServer_method_get_locale).

---

<span id="class_TranslationServer_method_get_translation_object"></span>

[Translation](class_translation.md#class_Translation) **get_translation_object** ( locale: [String](class_string.md#class_String) ) [🔗](class_translationserver.md#class_TranslationServer_method_get_translation_object)

**Deprecated:** Use [find_translations()](class_translationserver.md#class_TranslationServer_method_find_translations) instead.

Returns the [Translation](class_translation.md#class_Translation) instance that best matches `locale` in the main translation domain. Returns `null` if there are no matches.

---

<span id="class_TranslationServer_method_get_translations"></span>

[Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] **get_translations** ( ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_get_translations)

Returns all available [Translation](class_translation.md#class_Translation) instances in the main translation domain as added by [add_translation()](class_translationserver.md#class_TranslationServer_method_add_translation).

---

<span id="class_TranslationServer_method_has_domain"></span>

[bool](class_bool.md#class_bool) **has_domain** ( domain: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_has_domain)

Returns `true` if a translation domain with the specified name exists.

---

<span id="class_TranslationServer_method_has_translation"></span>

[bool](class_bool.md#class_bool) **has_translation** ( translation: [Translation](class_translation.md#class_Translation) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_has_translation)

Returns `true` if the main translation domain contains the given `translation`.

---

<span id="class_TranslationServer_method_has_translation_for_locale"></span>

[bool](class_bool.md#class_bool) **has_translation_for_locale** ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_has_translation_for_locale)

Returns `true` if there are any [Translation](class_translation.md#class_Translation) instances in the main translation domain that match `locale` (see [compare_locales()](class_translationserver.md#class_TranslationServer_method_compare_locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---

<span id="class_TranslationServer_method_parse_number"></span>

[String](class_string.md#class_String) **parse_number** ( number: [String](class_string.md#class_String), locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_parse_number)

Converts `number` from the numeral system used in the given `locale` to Western Arabic (0..9).

---

<span id="class_TranslationServer_method_pseudolocalize"></span>

[StringName](class_stringname.md#class_StringName) **pseudolocalize** ( message: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_pseudolocalize)

Returns the pseudolocalized string based on the `message` passed in.

 **Note:** This method always uses the main translation domain.

---

<span id="class_TranslationServer_method_reload_pseudolocalization"></span>

void **reload_pseudolocalization** ( ) [🔗](class_translationserver.md#class_TranslationServer_method_reload_pseudolocalization)

Reparses the pseudolocalization options and reloads the translation for the main translation domain.

---

<span id="class_TranslationServer_method_remove_domain"></span>

void **remove_domain** ( domain: [StringName](class_stringname.md#class_StringName) ) [🔗](class_translationserver.md#class_TranslationServer_method_remove_domain)

Removes the translation domain with the specified name.

 **Note:** Trying to remove the main translation domain is an error.

---

<span id="class_TranslationServer_method_remove_translation"></span>

void **remove_translation** ( translation: [Translation](class_translation.md#class_Translation) ) [🔗](class_translationserver.md#class_TranslationServer_method_remove_translation)

Removes the given translation from the main translation domain.

---

<span id="class_TranslationServer_method_set_locale"></span>

void **set_locale** ( locale: [String](class_string.md#class_String) ) [🔗](class_translationserver.md#class_TranslationServer_method_set_locale)

Sets the locale of the project. The `locale` string will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

If translations have been loaded beforehand for the new locale, they will be applied.

---

<span id="class_TranslationServer_method_standardize_locale"></span>

[String](class_string.md#class_String) **standardize_locale** ( locale: [String](class_string.md#class_String), add_defaults: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_standardize_locale)

Returns a `locale` string standardized to match known locales (e.g. `en-US` would be matched to `en_US`). If `add_defaults` is `true`, the locale may have a default script or country added.

---

<span id="class_TranslationServer_method_translate"></span>

[StringName](class_stringname.md#class_StringName) **translate** ( message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_translate)

Returns the current locale's translation for the given message and context.

 **Note:** This method always uses the main translation domain.

---

<span id="class_TranslationServer_method_translate_plural"></span>

[StringName](class_stringname.md#class_StringName) **translate_plural** ( message: [StringName](class_stringname.md#class_StringName), plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translationserver.md#class_TranslationServer_method_translate_plural)

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

 **Note:** This method always uses the main translation domain.

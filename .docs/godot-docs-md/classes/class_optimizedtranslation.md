<span id="class_OptimizedTranslation"></span>

## OptimizedTranslation

**Inherits:** [Translation](class_translation.md#class_Translation) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An optimized translation.

### Description

An optimized translation. Uses real-time compressed translations, which results in very small dictionaries.

This class does not store the untranslated strings for optimization purposes. Therefore, [Translation.get_message_list()](class_translation.md#class_Translation_method_get_message_list) always returns an empty array, and [Translation.get_message_count()](class_translation.md#class_Translation_method_get_message_count) always returns `0`.

### Methods


| void | [generate](class_optimizedtranslation.md#class_OptimizedTranslation_method_generate) ( from: [Translation](class_translation.md#class_Translation) ) |
| --- | --- |

---

### Method Descriptions

<span id="class_OptimizedTranslation_method_generate"></span>

void **generate** ( from: [Translation](class_translation.md#class_Translation) ) [🔗](class_optimizedtranslation.md#class_OptimizedTranslation_method_generate)

Generates and sets an optimized translation from the given [Translation](class_translation.md#class_Translation) resource.

 **Note:** Messages in `from` should not use context or plural forms.

 **Note:** This method is intended to be used in the editor. It does nothing when called from an exported project.

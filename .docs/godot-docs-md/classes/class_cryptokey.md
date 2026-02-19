<span id="class_CryptoKey"></span>

## CryptoKey

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A cryptographic key (RSA or elliptic-curve).

### Description

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other [Resource](class_resource.md#class_Resource).

They can be used to generate a self-signed [X509Certificate](class_x509certificate.md#class_X509Certificate) via [Crypto.generate_self_signed_certificate()](class_crypto.md#class_Crypto_method_generate_self_signed_certificate) and as private key in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream) along with the appropriate certificate.

### Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

### Methods


| [bool](class_bool.md#class_bool) | [is_public_only](class_cryptokey.md#class_CryptoKey_method_is_public_only) ( ) const |
| --- | --- |
| Error | [load](class_cryptokey.md#class_CryptoKey_method_load) ( path: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) |
| Error | [load_from_string](class_cryptokey.md#class_CryptoKey_method_load_from_string) ( string_key: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) |
| Error | [save](class_cryptokey.md#class_CryptoKey_method_save) ( path: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) |
| [String](class_string.md#class_String) | [save_to_string](class_cryptokey.md#class_CryptoKey_method_save_to_string) ( public_only: [bool](class_bool.md#class_bool) = false ) |

---

### Method Descriptions

<span id="class_CryptoKey_method_is_public_only"></span>

[bool](class_bool.md#class_bool) **is_public_only** ( ) *const* [🔗](class_cryptokey.md#class_CryptoKey_method_is_public_only)

Returns `true` if this CryptoKey only has the public part, and not the private one.

---

<span id="class_CryptoKey_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_cryptokey.md#class_CryptoKey_method_load)

Loads a key from `path`. If `public_only` is `true`, only the public key will be loaded.

 **Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---

<span id="class_CryptoKey_method_load_from_string"></span>

Error **load_from_string** ( string_key: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_cryptokey.md#class_CryptoKey_method_load_from_string)

Loads a key from the given `string_key`. If `public_only` is `true`, only the public key will be loaded.

---

<span id="class_CryptoKey_method_save"></span>

Error **save** ( path: [String](class_string.md#class_String), public_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_cryptokey.md#class_CryptoKey_method_save)

Saves a key to the given `path`. If `public_only` is `true`, only the public key will be saved.

 **Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---

<span id="class_CryptoKey_method_save_to_string"></span>

[String](class_string.md#class_String) **save_to_string** ( public_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_cryptokey.md#class_CryptoKey_method_save_to_string)

Returns a string containing the key in PEM format. If `public_only` is `true`, only the public key will be included.

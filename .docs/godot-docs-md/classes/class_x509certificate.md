<span id="class_X509Certificate"></span>

## X509Certificate

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An X509 certificate (e.g. for TLS).

### Description

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other [Resource](class_resource.md#class_Resource).

They can be used as the server certificate in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream) (along with the proper [CryptoKey](class_cryptokey.md#class_CryptoKey)), and to specify the only certificate that should be accepted when connecting to a TLS server via [StreamPeerTLS.connect_to_stream()](class_streampeertls.md#class_StreamPeerTLS_method_connect_to_stream).

### Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

### Methods


| Error | [load](class_x509certificate.md#class_X509Certificate_method_load) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| Error | [load_from_string](class_x509certificate.md#class_X509Certificate_method_load_from_string) ( string: [String](class_string.md#class_String) ) |
| Error | [save](class_x509certificate.md#class_X509Certificate_method_save) ( path: [String](class_string.md#class_String) ) |
| [String](class_string.md#class_String) | [save_to_string](class_x509certificate.md#class_X509Certificate_method_save_to_string) ( ) |

---

### Method Descriptions

<span id="class_X509Certificate_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String) ) [🔗](class_x509certificate.md#class_X509Certificate_method_load)

Loads a certificate from `path` ("\*.crt" file).

---

<span id="class_X509Certificate_method_load_from_string"></span>

Error **load_from_string** ( string: [String](class_string.md#class_String) ) [🔗](class_x509certificate.md#class_X509Certificate_method_load_from_string)

Loads a certificate from the given `string`.

---

<span id="class_X509Certificate_method_save"></span>

Error **save** ( path: [String](class_string.md#class_String) ) [🔗](class_x509certificate.md#class_X509Certificate_method_save)

Saves a certificate to the given `path` (should be a "\*.crt" file).

---

<span id="class_X509Certificate_method_save_to_string"></span>

[String](class_string.md#class_String) **save_to_string** ( ) [🔗](class_x509certificate.md#class_X509Certificate_method_save_to_string)

Returns a string representation of the certificate, or an empty string if the certificate is invalid.

<span id="class_TLSOptions"></span>

## TLSOptions

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

TLS configuration for clients and servers.

### Description

TLSOptions abstracts the configuration options for the [StreamPeerTLS](class_streampeertls.md#class_StreamPeerTLS) and [PacketPeerDTLS](class_packetpeerdtls.md#class_PacketPeerDTLS) classes.

Objects of this class cannot be instantiated directly, and one of the static methods [client()](class_tlsoptions.md#class_TLSOptions_method_client), [client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe), or [server()](class_tlsoptions.md#class_TLSOptions_method_server) should be used instead.

.. tabs::

```
```

    # Create a TLS client configuration which uses our custom trusted CA chain.
    var client_trusted_cas = load("res://my_trusted_cas.crt")
    var client_tls_options = TLSOptions.client(client_trusted_cas)

    # Create a TLS server configuration.
    var server_certs = load("res://my_server_cas.crt")
    var server_key = load("res://my_server_key.key")
    var server_tls_options = TLSOptions.server(server_key, server_certs)

### Methods


| [TLSOptions](class_tlsoptions.md#class_TLSOptions) | [client](class_tlsoptions.md#class_TLSOptions_method_client) ( trusted_chain: [X509Certificate](class_x509certificate.md#class_X509Certificate) = null, common_name_override: [String](class_string.md#class_String) = "" ) static |
| --- | --- |
| [TLSOptions](class_tlsoptions.md#class_TLSOptions) | [client_unsafe](class_tlsoptions.md#class_TLSOptions_method_client_unsafe) ( trusted_chain: [X509Certificate](class_x509certificate.md#class_X509Certificate) = null ) static |
| [String](class_string.md#class_String) | [get_common_name_override](class_tlsoptions.md#class_TLSOptions_method_get_common_name_override) ( ) const |
| [X509Certificate](class_x509certificate.md#class_X509Certificate) | [get_own_certificate](class_tlsoptions.md#class_TLSOptions_method_get_own_certificate) ( ) const |
| [CryptoKey](class_cryptokey.md#class_CryptoKey) | [get_private_key](class_tlsoptions.md#class_TLSOptions_method_get_private_key) ( ) const |
| [X509Certificate](class_x509certificate.md#class_X509Certificate) | [get_trusted_ca_chain](class_tlsoptions.md#class_TLSOptions_method_get_trusted_ca_chain) ( ) const |
| [bool](class_bool.md#class_bool) | [is_server](class_tlsoptions.md#class_TLSOptions_method_is_server) ( ) const |
| [bool](class_bool.md#class_bool) | [is_unsafe_client](class_tlsoptions.md#class_TLSOptions_method_is_unsafe_client) ( ) const |
| [TLSOptions](class_tlsoptions.md#class_TLSOptions) | [server](class_tlsoptions.md#class_TLSOptions_method_server) ( key: [CryptoKey](class_cryptokey.md#class_CryptoKey), certificate: [X509Certificate](class_x509certificate.md#class_X509Certificate) ) static |

---

### Method Descriptions

<span id="class_TLSOptions_method_client"></span>

[TLSOptions](class_tlsoptions.md#class_TLSOptions) **client** ( trusted_chain: [X509Certificate](class_x509certificate.md#class_X509Certificate) = null, common_name_override: [String](class_string.md#class_String) = "" ) *static* [🔗](class_tlsoptions.md#class_TLSOptions_method_client)

Creates a TLS client configuration which validates certificates and their common names (fully qualified domain names).

You can specify a custom `trusted_chain` of certification authorities (the default CA list will be used if `null`), and optionally provide a `common_name_override` if you expect the certificate to have a common name other than the server FQDN.

 **Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.

---

<span id="class_TLSOptions_method_client_unsafe"></span>

[TLSOptions](class_tlsoptions.md#class_TLSOptions) **client_unsafe** ( trusted_chain: [X509Certificate](class_x509certificate.md#class_X509Certificate) = null ) *static* [🔗](class_tlsoptions.md#class_TLSOptions_method_client_unsafe)

Creates an **unsafe** TLS client configuration where certificate validation is optional. You can optionally provide a valid `trusted_chain`, but the common name of the certificates will never be checked. Using this configuration for purposes other than testing **is not recommended**.

 **Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.

---

<span id="class_TLSOptions_method_get_common_name_override"></span>

[String](class_string.md#class_String) **get_common_name_override** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_get_common_name_override)

Returns the common name (domain name) override specified when creating with [client()](class_tlsoptions.md#class_TLSOptions_method_client).

---

<span id="class_TLSOptions_method_get_own_certificate"></span>

[X509Certificate](class_x509certificate.md#class_X509Certificate) **get_own_certificate** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_get_own_certificate)

Returns the [X509Certificate](class_x509certificate.md#class_X509Certificate) specified when creating with [server()](class_tlsoptions.md#class_TLSOptions_method_server).

---

<span id="class_TLSOptions_method_get_private_key"></span>

[CryptoKey](class_cryptokey.md#class_CryptoKey) **get_private_key** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_get_private_key)

Returns the [CryptoKey](class_cryptokey.md#class_CryptoKey) specified when creating with [server()](class_tlsoptions.md#class_TLSOptions_method_server).

---

<span id="class_TLSOptions_method_get_trusted_ca_chain"></span>

[X509Certificate](class_x509certificate.md#class_X509Certificate) **get_trusted_ca_chain** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_get_trusted_ca_chain)

Returns the CA [X509Certificate](class_x509certificate.md#class_X509Certificate) chain specified when creating with [client()](class_tlsoptions.md#class_TLSOptions_method_client) or [client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

---

<span id="class_TLSOptions_method_is_server"></span>

[bool](class_bool.md#class_bool) **is_server** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_is_server)

Returns `true` if created with [server()](class_tlsoptions.md#class_TLSOptions_method_server), `false` otherwise.

---

<span id="class_TLSOptions_method_is_unsafe_client"></span>

[bool](class_bool.md#class_bool) **is_unsafe_client** ( ) *const* [🔗](class_tlsoptions.md#class_TLSOptions_method_is_unsafe_client)

Returns `true` if created with [client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe), `false` otherwise.

---

<span id="class_TLSOptions_method_server"></span>

[TLSOptions](class_tlsoptions.md#class_TLSOptions) **server** ( key: [CryptoKey](class_cryptokey.md#class_CryptoKey), certificate: [X509Certificate](class_x509certificate.md#class_X509Certificate) ) *static* [🔗](class_tlsoptions.md#class_TLSOptions_method_server)

Creates a TLS server configuration using the provided `key` and `certificate`.

 **Note:** The `certificate` should include the full certificate chain up to the signing CA (certificates file can be concatenated using a general purpose text editor).

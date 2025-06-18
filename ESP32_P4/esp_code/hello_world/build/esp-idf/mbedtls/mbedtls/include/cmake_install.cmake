# Install script for directory: /workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "TRUE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mbedtls" TYPE FILE PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ FILES
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/aes.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/aria.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/asn1.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/asn1write.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/base64.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/bignum.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/block_cipher.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/build_info.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/camellia.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ccm.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/chacha20.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/chachapoly.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/check_config.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/cipher.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/cmac.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/compat-2.x.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_legacy_crypto.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_legacy_from_psa.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_psa_from_legacy.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_psa_superset_legacy.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_ssl.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_adjust_x509.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/config_psa.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/constant_time.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ctr_drbg.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/debug.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/des.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/dhm.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ecdh.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ecdsa.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ecjpake.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ecp.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/entropy.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/error.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/gcm.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/hkdf.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/hmac_drbg.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/lms.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/mbedtls_config.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/md.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/md5.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/memory_buffer_alloc.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/net_sockets.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/nist_kw.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/oid.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/pem.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/pk.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/pkcs12.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/pkcs5.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/pkcs7.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/platform.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/platform_time.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/platform_util.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/poly1305.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/private_access.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/psa_util.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ripemd160.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/rsa.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/sha1.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/sha256.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/sha3.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/sha512.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ssl.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ssl_cache.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ssl_ciphersuites.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ssl_cookie.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/ssl_ticket.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/threading.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/timing.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/version.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/x509.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/x509_crl.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/x509_crt.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/mbedtls/x509_csr.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/psa" TYPE FILE PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ FILES
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/build_info.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_adjust_auto_enabled.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_adjust_config_dependencies.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_adjust_config_key_pair_types.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_adjust_config_synonyms.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_builtin_composites.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_builtin_key_derivation.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_builtin_primitives.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_compat.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_config.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_driver_common.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_driver_contexts_composites.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_driver_contexts_key_derivation.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_driver_contexts_primitives.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_extra.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_legacy.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_platform.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_se_driver.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_sizes.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_struct.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_types.h"
    "/workspaces/NeedChange/ESP32_P4/esp/esp-idf/components/mbedtls/mbedtls/include/psa/crypto_values.h"
    )
endif()


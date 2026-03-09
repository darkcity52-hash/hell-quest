[app]
title = CodeQuest
package.name = codequest
package.domain = org.darkcity52
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*, assets/icons/*

# Pantalla de inicio y versión estable
version = 0.1
orientation = portrait
presplash.filename = %(source.dir)s/assets/icons/splash.png
icon.filename = %(source.dir)s/assets/icons/helios.png

# Ajustes de Android para evitar errores de licencia
android.api = 33
android.sdk = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a
requirements = python3,kivy

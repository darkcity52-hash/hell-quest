[app]
title = HellQuest
package.name = hellquest
package.domain = org.darkcity52
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*

version = 0.1
orientation = portrait

# Pantalla de inicio y Icono
presplash.filename = %(source.dir)s/assets/icons/splash.png
icon.filename = %(source.dir)s/assets/icons/helios.png

# Requerimientos estables
requirements = python3,kivy
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

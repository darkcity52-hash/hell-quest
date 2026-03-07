[app]
title = CodeQuest
package.name = codequest
package.domain = org.hellmat
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0

# Requerimientos para Kivy
requirements = python3,kivy==2.3.0,pillow

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21

# Permisos y Licencias
android.permissions = VIBRATE, INTERNET, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

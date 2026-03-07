[app]
title = CodeQuest
package.name = codequest
package.domain = org.hellmat
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0

# Archivos de imagen (Ya los tienes en tu GitHub)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Requerimientos (Cuidado con los espacios aquí)
requirements = python3,kivy==2.3.0,pillow

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 25b

# Permisos y Licencias (Lo que nos faltaba)
android.permissions = VIBRATE, INTERNET, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

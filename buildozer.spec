[app]
# (Sección obligatoria)
title = CodeQuest
package.name = codequest
package.domain = org.darkcity52
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*, assets/icons/*

# Pantalla de inicio corregida
presplash.filename = %(source.dir)s/assets/icons/splash.png
icon.filename = %(source.dir)s/assets/icons/helios.png

version = 0.1
orientation = portrait

# Requerimientos para tu OnePlus 11
requirements = python3,kivy
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

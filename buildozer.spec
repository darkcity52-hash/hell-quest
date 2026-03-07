[app]
title = CodeQuest
package.name = codequest
package.domain = org.hellmat
source.dir = .
source.include_exts = py,png,jpg,kv,json
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
version = 1.0.0
requirements = python3,kivy==2.3.0,pillow,pyjnius
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.window_soft_input_mode = adjustResize
android.permissions = VIBRATE, INTERNET, WRITE_EXTERNAL_STORAGE

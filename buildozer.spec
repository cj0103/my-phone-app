[app]
title = My App
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.minapi = 21
android.archs = arm64-v8a
p4a.bootstrap = sdl2
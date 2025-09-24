[app]
title = 我的手机App
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.ndk = 25b
android.sdk = 34
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
p4a.bootstrap = sdl2
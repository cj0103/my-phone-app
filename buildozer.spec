[app]
title = My App
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy==2.3.0

[buildozer]
log_level = 2

[app:android]
android.ndk = 25b
android.sdk = 34
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
p4a.bootstrap = sdl2
p4a.branch = develop   # 👈 关键：使用最新 p4a
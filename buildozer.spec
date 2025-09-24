[app]
title = My Kivy App
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py
source.exclude_patterns = .git, __pycache__, *.pyc, .github, .gitignore
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.ndk = 25b
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
p4a.bootstrap = sdl2
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
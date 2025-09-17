[app]
title = Digital Encoding Visualizer
package.name = encodingvisualizer
package.domain = org.example
source.dir = .
source.include_exts = py,kv,txt,md
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
log_level = 2

# Use API 28 since you set android.api = 28
android.api = 28
android.minapi = 21
android.archs = arm64-v8a

# Force stable build-tools version (avoids 36.1-rc1 issue)
android.build_tools_version = 30.0.3

# Force NDK version that Buildozer works well with
android.ndk = 21b

# You can add permissions here if needed, for example:
# android.permissions = INTERNET

presplash.filename =
icon.filename =

[buildozer]
log_level = 2
warn_on_root = 0

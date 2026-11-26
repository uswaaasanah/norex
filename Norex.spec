# PyInstaller build configuration for the NOREX Windows GUI application.
from PyInstaller.utils.hooks import collect_all

ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all("customtkinter")

analysis = Analysis(
    ["Norex.py"],
    pathex=[],
    binaries=ctk_binaries,
    datas=ctk_datas,
    hiddenimports=[
        "biseksi2",
        "newraph1",
        "regulaf1",
        "secant1",
        "matplotlib.backends.backend_tkagg",
        *ctk_hiddenimports,
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    [],
    name="NOREX",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

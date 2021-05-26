# -*- mode: python -*-

block_cipher = None
added_files=[('./data/*.*','data'),('./ui/*.*','ui')]

a = Analysis(['main_gia.py'],
             pathex=['C:\\Users\\tasl\\Documents\\bitbucket\\gia_python'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        exclude_binaries=True,
        name='main_gia',
        debug=False,
        strip=False,
        upx=True,
        console=False,
        icon='./data/icon_gia.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main_gia',
               icon='./data/icon_gia.ico')

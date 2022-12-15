import cx_Freeze

executables = [cx_Freeze.Executable("space invader.py")]

cx_Freeze.setup(
    name = "Space Invaders",
    options = {"build.exe": {"packages":["pygame"],
                             "include_files":["background.png","bullet.png","enemy.png","icon.png","ufo.png","player.png"]}},
                             executables = executables)

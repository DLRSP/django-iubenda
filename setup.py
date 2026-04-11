import os
import shutil
import subprocess
import sys
from distutils.cmd import Command
from distutils.command.build import build as _build

from setuptools.command.install_lib import install_lib as _install_lib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


class CompileTranslations(Command):
    description = (
        "compile gettext .po under src/iubenda/locale to .mo via msgfmt --check-format "
        "(same flags as django compilemessages; requires GNU gettext)"
    )
    user_options = []  # type: list

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        msgfmt = shutil.which("msgfmt")
        root = os.path.dirname(os.path.abspath(__file__))
        locale_root = os.path.join(root, "src", "iubenda", "locale")
        if not os.path.isdir(locale_root):
            return
        if not msgfmt:
            print(
                "msgfmt not found; skipping .mo compilation (use checked-in .mo or install gettext)",
                file=sys.stderr,
            )
            return
        for dirpath, _dirnames, filenames in os.walk(locale_root):
            for name in filenames:
                if not name.endswith(".po"):
                    continue
                po_path = os.path.join(dirpath, name)
                mo_path = po_path[:-3] + ".mo"
                subprocess.run(
                    [msgfmt, "--check-format", "-o", mo_path, po_path],
                    check=True,
                )


class Build(_build):
    sub_commands = [("compile_translations", None)] + _build.sub_commands


class InstallLib(_install_lib):
    def run(self):
        self.run_command("compile_translations")
        _install_lib.run(self)


setup(
    cmdclass={
        "build": Build,
        "install_lib": InstallLib,
        "compile_translations": CompileTranslations,
    },
)

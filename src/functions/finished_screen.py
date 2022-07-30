# desktop_screen.py

#
# Copyright 2022 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess
from gi.repository import Gtk, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/finished_screen.ui')
class FinishedScreen(Adw.Bin):
    __gtype_name__='FinishedScreen'

    reboot_button = Gtk.Template.Child()

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.reboot_button.connect("clicked", self.reboot)

    def reboot(self, widget):
        command=subprocess.run(["bash", "-c", "bash -- /app/share/jade-gui/jade_gui/scripts/reboot.sh"], capture_output=False)


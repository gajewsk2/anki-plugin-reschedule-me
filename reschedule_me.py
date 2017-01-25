from PyQt4.QtGui import QShortcut, QKeySequence
import PyQt4.QtCore
import types
from aqt import mw
import anki.hooks

HOTKEY = {      
    'RescheduleMenu': 'Shift+R',
    'RescheduleToday': 'Ctrl+R'
}


def rescheduleToday(self):
    self.model.beginReset()
    self.mw.checkpoint(_("Reschedule"))
    self.col.sched.reschedCards(self.selectedCards(),0,0)
    self.mw.requireReset()
    self.model.endReset()


def setupRescheduleHotkeys(self):
    self.rescheduleToday = types.MethodType(rescheduleToday, self)
    self.hotkeyRescheduleToday = QShortcut(QKeySequence(HOTKEY['RescheduleToday']), self)
    self.hotkeyRescheduleMenu = QShortcut(QKeySequence(HOTKEY['RescheduleMenu']), self)
    self.hotkeyRescheduleToday.activated.connect(self.rescheduleToday)
    self.hotkeyRescheduleMenu.activated.connect(self.reschedule)


mainMenu = mw.menuBar()
anki.hooks.addHook('browser.setupMenus', setupRescheduleHotkeys)

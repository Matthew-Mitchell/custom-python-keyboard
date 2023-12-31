# from PYKB import *
from keyboard import *
from keyboardMod import *
import time

keyboard = Keyboard()

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)
L2D = LAYER_TAP(2, D)
L3B = LAYER_TAP(3, B)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))

# Semicolon & Ctrl
SCC = MODS_TAP(MODS(RCTRL), ';')

keyboard.keymap = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        CAPS,  A,   S, L2D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
        LSFT4, Z,   X,   C,   V, L3B,   N,   M, ',', '.', SLASH,  RSHIFT,
        LCTRL, LGUI, LALT,          SPACE,     RALT, MODS_TAP(MODS(RGUI), LEFT), LAYER_TAP(1, DOWN), MODS_TAP(MODS(RCTRL), RIGHT)
     
    )   
    ,

    # layer 1 Activated with FN (Think this is hardcoded?)
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___, MACRO(8), HOME, END,___,       
        ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___,BOOT, MACRO(0),MACRO(1), ___, INSERT, DELETE,    MODS_TAP(MODS(RSHIFT),  UP),
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 2 Activated with D; see above
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, ___, ___, ___, ___,PGUP, ___, ___, ___,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, ___, ___, ___, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___,PGDN, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3 Activated with B; see above
    (
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
        ___, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 4
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___,   D, ___, ___, ___, ___, ___, ___, ';', ___,      ___,
        ___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

# ORIGINAL CODE
# def macro_handler(dev, n, is_down):
#     if is_down:
#         dev.send_text('You pressed macro #{}\n'.format(n))
#     else:
#         dev.send_text('You released macro #{}\n'.format(n))

#BACKLIGHT POSITIONS:
# ESC(0)    1(1)   2(2)   3(3)   4(4)   5(5)   6(6)   7(7)   8(8)   9(9)   0(10)  -(11)  =(12)  BACKSPACE(13)
# TAB(27)   Q(26)  W(25)  E(24)  R(23)  T(22)  Y(21)  U(20)  I(19)  O(18)  P(17)  [(16)  ](15)   \(14)
# CAPS(28)  A(29)  S(30)  D(31)  F(32)  G(33)  H(34)  J(35)  K(36)  L(37)  ;(38)  "(39)      ENTER(40)
#LSHIFT(52) Z(51)  X(50)  C(49)  V(48)  B(47)  N(46)  M(45)  ,(44)  .(43)  /(42)            RSHIFT(41)
# LCTRL(53)  LGUI(54)  LALT(55)               SPACE(56)          RALT(57)  MENU(58)  Fn(59)  RCTRL(60)

def set_color(dev, r, g, b):
    for i in range(0,28):
        dev.backlight.pixel(i, r, g, b)
    for i in range(29,61):
        dev.backlight.pixel(i, r, g, b)

def color_macro(dev, is_down, r, g, b):
    if is_down:
        set_color(dev, r,g,b)
        dev.backlight.set_brightness(200)
    else:
        pass
    dev.backlight.update()

def lights_off(dev, is_down):
    #Black; turn lights off
    color_macro(dev, is_down, 0, 0, 0)

def lights_purple(dev, is_down):
    #Purple!!
    color_macro(dev, is_down, 153,0,153)

def pulse_lights(dev, is_down):
    #WHILE THIS DOES PULSE THE LIGHTS, THE CONTINUOUS RUN LOCKS OUT ACTUAL KEYBOARD FUNCTION.
    #PERHAPS WOULD WORK WITH THREADING...? POTENTIAL PERFORMANCE ISSUES WITH KEYBOARD RESPONSIVENESS...??
    i = 200 #Starting Brightness
    while True:
        i = (i%255) + 1 #Continually Iterate w/ Modular Arithmetic applied
        dev.backlight.set_brightness(i)
        time.sleep(0.01) #Timing increments...currently linear / uniform

def macro_handler(dev, n, is_down):
    """Macros actually execute twice; once when key is pressed and again when released.
    Differentiate with "is_down"
    not sure why dev needs to be passed to function....
    """
    # DEBUGGING / EXPERIMENT LOGGING CODE:
    #dev.send_text('You just triggered MACRO #{}\n'.format(n))
    #dev.send_text("n equals 0: {}".format(n==0))
    #dev.send_text("keylights are currently: {}".format(keylights))
    if n == 0:
        lights_off(dev, is_down)
    if n == 1:
        lights_purple(dev, is_down) #Purple
    if n == 8:
        pass
        #DOES NOT WORK...
        #pulse_lights(dev, is_down)

def pairs_handler(dev, n):
    dev.send_text('You just triggered pair keys #{}\n'.format(n))


keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# Pairs: J & K, U & I
keyboard.pairs = [{35, 36}, {20, 19}]

keyboard.verbose = False

keyboard.run()
#print("Keyboard attributes: ", dir(keyboard))
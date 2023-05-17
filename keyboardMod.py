from PYKB import *
import time

class KeyboardMod(Keyboard):
	# def __init__(self, keymap=(), verbose=True):
	#         self.keymap = keymap
	#         self.verbose = verbose
	#         self.profiles = {}
	#         self.pairs = ()
	#         self.pairs_handler = do_nothing
	#         self.pair_keys = set()
	#         self.macro_handler = do_nothing
	#         self.layer_mask = 1
	#         self.matrix = Matrix()
	#         self.backlight = Backlight()
	#         self.uid = microcontroller.cpu.uid * 2
	#         self.usb_status = 0
	#         self.tap_delay = 500
	#         self.fast_type_thresh = 200
	#         self.pair_delay = 10
	#         self.adv_timeout = None

	#         size = 4 + self.matrix.keys
	#         self.data = array.array("L", microcontroller.nvm[: size * 4])
	#         if self.data[0] != 0x424B5950:
	#             self.data[0] = 0x424B5950
	#             self.data[1] = 1
	#             for i in range(4, size):
	#                 self.data[i] = 0
	#         self.ble_id = self.data[1]
	#         self.heatmap = memoryview(self.data)[4:]

	#         ble_hid = HIDService()
	#         self.battery = BatteryService()
	#         self.battery.level = battery_level()
	#         self.battery_update_time = time.time() + 360
	#         self.advertisement = ProvideServicesAdvertisement(ble_hid, self.battery)
	#         self.advertisement.appearance = 961
	#         self.ble = BLERadio()
	#         self.set_bt_id(self.ble_id)
	#         self.ble_hid = HID(ble_hid.devices)
	#         self.usb_hid = HID(usb_hid.devices)

	def new_method(self):
		pass

	# def run(self):
	#     self.setup()
	#     log = self.log
	#     matrix = self.matrix
	#     dev = Device(self)
	#     keys = [0] * matrix.keys
	#     ms = matrix.ms
	#     last_time = 0
	#     mouse_action = 0
	#     mouse_time = 0
	#     while True:
	#         t = 20 if self.backlight.check() or mouse_action else 1000
	#         n = matrix.wait(t)
	#         self.check()

	#         if self.pair_keys:
	#             # detecting pair keys
	#             if n == 1:
	#                 key = matrix.view(0)
	#                 if key < 0x80 and key in self.pair_keys:
	#                     n = matrix.wait(
	#                         self.pair_delay
	#                         - ms(matrix.time() - matrix.get_keydown_time(key))
	#                     )

	#             if n >= 2:
	#                 pair = {matrix.view(0), matrix.view(1)}
	#                 if pair in self.pairs:
	#                     pair_index = self.pairs.index(pair)
	#                     key1 = self.get()
	#                     key2 = self.get()

	#                     dt = ms(
	#                         matrix.get_keydown_time(key2)
	#                         - matrix.get_keydown_time(key1)
	#                     )
	#                     log("pair keys {} {}, dt = {}".format(pair_index, pair, dt))
	#                     try:
	#                         self.pairs_handler(dev, pair_index)
	#                     except Exception as e:
	#                         print(e)

	#         while len(matrix):
	#             event = self.get()
	#             key = event & 0x7F
	#             if event & 0x80 == 0:
	#                 action_code = self.action_code(key)
	#                 keys[key] = action_code
	#                 if action_code < 0xFF:
	#                     self.press(action_code)
	#                 else:
	#                     kind = action_code >> 12
	#                     if kind < ACT_MODS_TAP:
	#                         # MODS
	#                         mods = (action_code >> 8) & 0x1F
	#                         keycodes = mods_to_keycodes(mods)
	#                         keycodes.append(action_code & 0xFF)
	#                         self.press(*keycodes)
	#                     elif kind < ACT_USAGE:
	#                         # MODS_TAP
	#                         if self.is_tapping_key(key):
	#                             log("TAP")
	#                             keycode = action_code & 0xFF
	#                             keys[key] = keycode
	#                             self.press(keycode)
	#                         else:
	#                             mods = (action_code >> 8) & 0x1F
	#                             keycodes = mods_to_keycodes(mods)
	#                             self.press(*keycodes)
	#                     elif kind == ACT_USAGE:
	#                         if action_code & 0x400:
	#                             self.send_consumer(action_code & 0x3FF)
	#                     elif kind == ACT_MOUSEKEY:
	#                         if action_code & 0xF00 == 0:
	#                             self.press_mouse(action_code & 0xF)
	#                         else:
	#                             mouse_action = (action_code >> 8) & 0xF
	#                             mouse_time = time.monotonic_ns()
	#                     elif kind == ACT_LAYER_TAP or kind == ACT_LAYER_TAP_EXT:
	#                         layer = (action_code >> 8) & 0x1F
	#                         mask = 1 << layer
	#                         if action_code & 0xE0 == 0xC0:
	#                             log("LAYER_MODS")
	#                             mods = action_code & 0x1F
	#                             keycodes = mods_to_keycodes(mods)
	#                             self.press(*keycodes)
	#                             self.layer_mask |= mask
	#                         elif self.is_tapping_key(key):
	#                             log("TAP")
	#                             keycode = action_code & 0xFF
	#                             if keycode == OP_TAP_TOGGLE:
	#                                 log("TOGGLE {}".format(layer))
	#                                 self.layer_mask = (self.layer_mask & ~mask) | (
	#                                     mask & ~self.layer_mask
	#                                 )
	#                                 keys[key] = 0
	#                             else:
	#                                 keys[key] = keycode
	#                                 self.press(keycode)
	#                         else:
	#                             self.layer_mask |= mask

	#                         log("layer_mask = {}".format(self.layer_mask))
	#                     elif kind == ACT_MACRO:
	#                         if callable(self.macro_handler):
	#                             i = action_code & 0xFFF
	#                             try:
	#                                 self.macro_handler(dev, i, True)
	#                             except Exception as e:
	#                                 print(e)
	#                     elif kind == ACT_BACKLIGHT:
	#                         if action_code == RGB_MOD:
	#                             self.backlight.next()
	#                         elif action_code == RGB_TOGGLE:
	#                             self.backlight.toggle()
	#                         elif action_code == RGB_HUE:
	#                             self.backlight.hue += 8
	#                         elif action_code == HUE_RGB:
	#                             self.backlight.hue -= 8
	#                         elif action_code == RGB_SAT:
	#                             self.backlight.sat += 8
	#                         elif action_code == SAT_RGB:
	#                             self.backlight.sat -= 8
	#                         elif action_code == RGB_VAL:
	#                             self.backlight.val += 8
	#                         elif action_code == VAL_RGB:
	#                             self.backlight.val -= 8
	#                     elif kind == ACT_COMMAND:
	#                         if action_code == BOOTLOADER:
	#                             microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
	#                             microcontroller.reset()
	#                         elif action_code == SUSPEND:
	#                             matrix.suspend()
	#                         elif action_code == SHUTDOWN:
	#                             microcontroller.reset()
	#                         elif action_code == HEATMAP:
	#                             microcontroller.nvm[:272] = struct.pack(
	#                                 "68L", *self.data
	#                             )
	#                             if usb_is_connected():
	#                                 microcontroller.reset()
	#                         elif action_code == USB_TOGGLE:
	#                             self.toggle_usb()
	#                         elif action_code == BT_TOGGLE:
	#                             self.toggle_bt()
	#                         elif BT(0) <= action_code and action_code <= BT(9):
	#                             i = action_code - BT(0)
	#                             log("switch to bt {}".format(i))
	#                             self.change_bt(i)

	#                 if self.verbose:
	#                     keydown_time = matrix.get_keydown_time(key)
	#                     dt = ms(matrix.time() - keydown_time)
	#                     dt2 = ms(keydown_time - last_time)
	#                     last_time = keydown_time
	#                     print(
	#                         "{} {} \\ {} latency {} | {}".format(
	#                             key, key_name(key), hex(action_code), dt, dt2
	#                         )
	#                     )
	#             else:
	#                 action_code = keys[key]
	#                 if action_code < 0xFF:
	#                     self.release(action_code)
	#                 else:
	#                     kind = action_code >> 12
	#                     if kind < ACT_MODS_TAP:
	#                         # MODS
	#                         mods = (action_code >> 8) & 0x1F
	#                         keycodes = mods_to_keycodes(mods)
	#                         keycodes.append(action_code & 0xFF)
	#                         self.release(*keycodes)
	#                     elif kind < ACT_USAGE:
	#                         # MODS_TAP
	#                         mods = (action_code >> 8) & 0x1F
	#                         keycodes = mods_to_keycodes(mods)
	#                         self.release(*keycodes)
	#                     elif kind == ACT_USAGE:
	#                         if action_code & 0x400:
	#                             self.send_consumer(0)
	#                     elif kind == ACT_MOUSEKEY:
	#                         if action_code & 0xF00 == 0:
	#                             self.release_mouse(action_code & 0xF)
	#                         elif (action_code >> 8) & 0xF == mouse_action:
	#                             mouse_action = 0
	#                             self.move_mouse(0, 0, 0)
	#                     elif kind == ACT_LAYER_TAP or kind == ACT_LAYER_TAP_EXT:
	#                         layer = (action_code >> 8) & 0x1F
	#                         keycode = action_code & 0xFF
	#                         if keycode & 0xE0 == 0xC0:
	#                             log("LAYER_MODS")
	#                             mods = keycode & 0x1F
	#                             keycodes = mods_to_keycodes(mods)
	#                             self.release(*keycodes)
	#                         self.layer_mask &= ~(1 << layer)
	#                         log("layer_mask = {}".format(self.layer_mask))
	#                     elif kind == ACT_MACRO:
	#                         i = action_code & 0xFFF
	#                         try:
	#                             self.macro_handler(dev, i, False)
	#                         except Exception as e:
	#                             print(e)

	#                 if self.verbose:
	#                     keyup_time = matrix.get_keyup_time(key)
	#                     dt = ms(matrix.time() - keyup_time)
	#                     dt2 = ms(keyup_time - last_time)
	#                     last_time = keyup_time
	#                     print(
	#                         "{} {} / {} latency {} | {}".format(
	#                             key, key_name(key), hex(action_code), dt, dt2
	#                         )
	#                     )

	#         if mouse_action:
	#             x, y, wheel = MS_MOVEMENT[mouse_action]
	#             dt = 1 + (time.monotonic_ns() - mouse_time) // 8000000
	#             mouse_time = time.monotonic_ns()
	#             self.move_mouse(x * dt, y * dt, wheel * dt)